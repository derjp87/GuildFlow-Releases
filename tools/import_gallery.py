"""Upload one prepared screenshot ZIP to GuildFlow-Releases with GitHub CLI.

The screenshot ZIP is assembled from real in-game/Windows captures and contains
eight numbered PNGs, optional extra PNGs, and a manifest.json. No manual
upload of each image in the GitHub browser is needed.

Prerequisites: Python 3.10+ and GitHub CLI ("gh auth login") on your own PC.

Preview: python tools/import_gallery.py GuildFlow_0.18.15_CurseForge_840px.zip
Upload:  python tools/import_gallery.py GuildFlow_0.18.15_CurseForge_840px.zip --apply

Only touches assets/screenshots/0.18.15/ in THIS public repository.
It does not publish an addon release or upload to CurseForge.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import struct
import subprocess
from pathlib import Path
from urllib.parse import quote
from zipfile import ZipFile

REPO = "derjp87/GuildFlow-Releases"
PREFIX = "assets/screenshots/0.18.15"
BRANCH = "main"


def run_gh(args: list[str], *, payload: dict | None = None, missing_ok=False):
    cmd = ["gh", "api", *args]
    result = subprocess.run(
        cmd, input=json.dumps(payload) if payload is not None else None,
        capture_output=True, text=True, encoding="utf-8", check=False,
    )
    if result.returncode:
        if missing_ok and "404" in result.stderr:
            return None
        raise RuntimeError(result.stderr.strip() or f"gh api failed: {cmd!r}")
    return json.loads(result.stdout)


def png_width_height(blob: bytes):
    if not blob.startswith(b"\x89PNG\r\n\x1a\n") or blob[12:16] != b"IHDR":
        raise ValueError("Only true PNG screenshots are accepted")
    return struct.unpack(">II", blob[16:24])


def git_blob_sha(content: bytes):
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()


def upload(zip_path: Path, apply: bool):
    with ZipFile(zip_path) as z:
        manifest = json.loads(z.read("manifest.json"))
        paths = [x["file"] for x in manifest]
        for i in range(1, 9):
            if not any(x.startswith(f"{i:02d}-") for x in paths):
                raise ValueError(f"Gallery screenshot {i:02d} is missing")
        if len(paths) != len(set(paths)):
            raise ValueError("Duplicate screenshot file names")
        for entry in manifest:
            name = entry["file"]
            if not re.fullmatch(r"(?:\d\d|extra)-[a-z0-9-]+\.png", name):
                raise ValueError(f"Unsafe gallery file name: {name}")
            content = z.read(name)
            width, height = png_width_height(content)
            if not 1 <= width <= 840 or not 1 <= height <= 3000:
                raise ValueError(f"Invalid screenshot size: {name}: {width}x{height}")
            if hashlib.sha256(content).hexdigest() != entry["sha256"]:
                raise ValueError(f"Corrupt gallery screenshot: {name}")
            target = f"{PREFIX}/{name}"
            if not apply:
                print(f"PREVIEW {target} ({width}x{height}; {len(content)} bytes)")
                continue
            endpoint = f"repos/{REPO}/contents/{quote(target)}"
            existing = run_gh([endpoint, "-f", f"ref={BRANCH}"], missing_ok=True)
            sha = existing.get("sha") if existing else None
            if sha == git_blob_sha(content):
                print(f"UNCHANGED {target}")
                continue
            body = {
                "message": f"media: add real GuildFlow 0.18.15 screenshot {name}",
                "branch": BRANCH,
                "content": base64.b64encode(content).decode("ascii"),
            }
            if sha:
                body["sha"] = sha
            result = run_gh(["-X", "PUT", endpoint, "--input", "-"], payload=body)
            print(f"UPLOADED {target} ({result['commit']['sha'][:12]})")
        if apply:
            print(f"All gallery screenshots checked in {REPO}/{PREFIX}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("zip", type=Path)
    p.add_argument("--apply", action="store_true", help="Actually upload to GitHub")
    args = p.parse_args()
    upload(args.zip, args.apply)


if __name__ == "__main__":
    main()
