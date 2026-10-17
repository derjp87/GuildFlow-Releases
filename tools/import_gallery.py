"""Import ALL 12 prepared 840px images and update the public README gallery.

One-time Windows use (Python 3 and authenticated GitHub CLI are required):
  python UPLOAD_GITHUB.py
This module can also be run from a checkout:
  python tools/import_gallery.py GuildFlow_0.18.15_Alle_12_Screenshots.zip --apply

The twelve screenshots are uploaded as ordinary versioned GitHub repository
files. Only AFTER all files have passed checksum/width validation and uploaded
successfully does this script add/update the actual Markdown images at the
BOTTOM of the public README. The public release workflow separately bundles
these images as a release ZIP; CurseForge PROJECT gallery is still managed
by the CurseForge project owner, not by the add-on upload API.
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
START = "<!-- guildflow-gallery-0.18.15:start -->"
END = "<!-- guildflow-gallery-0.18.15:end -->"
CAPTIONS = [
    "Overview / Übersicht",
    "Members / Mitglieder",
    "In-game equipment and 3D character / Ausrüstung im Spiel",
    "Talents / Talente",
    "Raids and sign-ups / Raids und Anmeldungen",
    "Guild calendar / Gildenkalender",
    "Professions and recipes / Berufe und Rezepte",
    "Personal shopping list / Persönliche Einkaufsliste",
    "Create a guild order / Gildenauftrag erstellen",
    "GuildFlow Sync – Windows companion / Windows-Client",
    "Windows 3D Armory / 3D-Ausrüstung im Windows-Client",
    "Windows guild statistics / Windows-Gildenstatistik",
]


def github_api(args: list[str], data: dict | None = None, missing_ok=False):
    cmd = ["gh", "api", *args]
    result = subprocess.run(
        cmd, input=json.dumps(data) if data is not None else None,
        capture_output=True, text=True, encoding="utf-8", check=False,
    )
    if result.returncode:
        if missing_ok and "404" in result.stderr:
            return None
        raise RuntimeError(result.stderr.strip() or f"GitHub API failed: {cmd!r}")
    return json.loads(result.stdout)


def valid_png(raw: bytes):
    if raw[:8] != b"\x89PNG\r\n\x1a\n" or raw[12:16] != b"IHDR":
        raise ValueError("Not a PNG image")
    return struct.unpack(">II", raw[16:24])


def upload_contents(target: str, data: bytes, message: str):
    endpoint = f"repos/{REPO}/contents/{quote(target)}"
    old = github_api(["-X", "GET", endpoint, "-f", f"ref={BRANCH}"],
                     missing_ok=True)
    old_sha = old["sha"] if old else None
    checksum = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if old_sha == checksum:
        print(f"UNCHANGED {target}")
        return
    payload = {
        "message": message,
        "branch": BRANCH,
        "content": base64.b64encode(data).decode("ascii"),
    }
    if old_sha:
        payload["sha"] = old_sha
    github_api(["-X", "PUT", endpoint, "--input", "-"], data=payload)
    print(f"UPLOADED {target}")


def gallery_markdown(filenames: list[str]) -> str:
    lines = [
        START,
        "",
        "## Screenshots / Bildergalerie",
        "",
        "GuildFlow 0.18.15 – real in-game views and the optional Windows companion.",
        "Die Bilder zeigen echte Ansichten aus WoW und dem optionalen Windows-Client.",
        "",
    ]
    for i in range(0, len(filenames), 2):
        left, right = filenames[i:i + 2]
        lines += [
            f"| {CAPTIONS[i]} | {CAPTIONS[i + 1]} |",
            "|:--|:--|",
            f"| [![{CAPTIONS[i]}]({PREFIX}/{left})]({PREFIX}/{left}) | "
            f"[![{CAPTIONS[i + 1]}]({PREFIX}/{right})]({PREFIX}/{right}) |",
            "",
        ]
    return "\n".join(lines + [END])


def update_readme(filenames: list[str]):
    endpoint = f"repos/{REPO}/contents/README.md"
    old = github_api(["-X", "GET", endpoint, "-f", f"ref={BRANCH}"])
    readme = base64.b64decode(old["content"]).decode("utf-8")
    block = gallery_markdown(filenames)
    if START in readme and END in readme:
        begin, finish = readme.index(START), readme.index(END) + len(END)
        updated = readme[:begin] + block + readme[finish:]
    elif START not in readme and END not in readme:
        updated = readme.rstrip() + "\n\n---\n\n" + block + "\n"
    else:
        raise ValueError("README has inconsistent gallery markers; refusing to overwrite")
    if readme == updated:
        print("README already contains the current 12-image gallery")
        return
    github_api(
        ["-X", "PUT", endpoint, "--input", "-"],
        data={
            "message": "docs: display all twelve GuildFlow 0.18.15 images at README bottom",
            "branch": BRANCH,
            "sha": old["sha"],
            "content": base64.b64encode(updated.encode("utf-8")).decode("ascii"),
        },
    )
    print("UPDATED README.md – all 12 images embedded at the very bottom")


def upload(zip_path: Path, apply: bool):
    with ZipFile(zip_path) as archive:
        manifest = json.loads(archive.read("manifest.json"))
        filenames = [entry["file"] for entry in manifest]
        if len(filenames) != 12 or len(set(filenames)) != 12:
            raise ValueError("The complete gallery must contain exactly 12 PNG screenshots")
        for i, filename in enumerate(filenames, 1):
            if not re.fullmatch(r"\d\d-[a-z0-9-]+\.png", filename):
                raise ValueError(f"Unsafe name: {filename}")
            if not filename.startswith(f"{i:02d}-"):
                raise ValueError(f"Missing gallery picture {i:02d}")
        # Validate ALL files before making any network changes.
        payloads = []
        for entry in manifest:
            raw = archive.read(entry["file"])
            w, h = valid_png(raw)
            if not (1 <= w <= 840 and 1 <= h <= 3000):
                raise ValueError(f"Screenshot too large: {entry['file']} ({w}×{h})")
            if hashlib.sha256(raw).hexdigest() != entry["sha256"]:
                raise ValueError(f"Corrupt screenshot: {entry['file']}")
            payloads.append((entry["file"], raw, w, h))
        if not apply:
            for filename, raw, w, h in payloads:
                print(f"PREVIEW {filename}: {w}×{h}, {len(raw)} bytes")
            print("PREVIEW: README images will be added only after all 12 are uploaded.")
            return
        for filename, raw, _, _ in payloads:
            upload_contents(
                f"{PREFIX}/{filename}", raw,
                f"media: add GuildFlow 0.18.15 screenshot {filename}",
            )
        update_readme(filenames)
        print(f"DONE: all images are in {REPO} and visible at the bottom of README.md")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    upload(args.zip, args.apply)


if __name__ == "__main__":
    main()
