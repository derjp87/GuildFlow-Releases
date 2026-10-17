#!/usr/bin/env python3
"""Validate the exact public GuildFlow release ZIP and create CurseForge upload metadata.

Only reads local files downloaded from a published GuildFlow-Releases release.
Never builds the addon from the private development repository.
"""
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

HERE = Path(".curseforge")
ARCHIVE = HERE / "GuildFlow.zip"
EXPECTED_TOCS = {
    "GuildFlow/GuildFlow.toc",
    "GuildFlow_Bridge1/GuildFlow_Bridge1.toc",
    "GuildFlow_Bridge2/GuildFlow_Bridge2.toc",
}
PROJECT_VERSION = re.compile(r"^v([0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.]+)?)$")


def main() -> None:
    release = json.loads((HERE / "release.json").read_text(encoding="utf-8"))
    tag = release.get("tagName", "")
    match = PROJECT_VERSION.fullmatch(tag)
    if not match:
        raise SystemExit(f"Unexpected version tag: {tag!r}")
    version = match.group(1)

    sha_file = (HERE / "SHA256SUMS").read_text(encoding="utf-8")
    expected = [
        m.group(1).lower()
        for line in sha_file.splitlines()
        if (m := re.fullmatch(r"([a-fA-F0-9]{64})\s+\*?GuildFlow\.zip", line.strip()))
    ]
    if len(expected) != 1:
        raise SystemExit("Exactly one SHA256SUMS entry for GuildFlow.zip is required")
    actual = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    if actual != expected[0]:
        raise SystemExit("GuildFlow.zip does not match release SHA256SUMS")

    with zipfile.ZipFile(ARCHIVE) as z:
        names = set(z.namelist())
        if not EXPECTED_TOCS.issubset(names):
            raise SystemExit(f"Missing addon TOC files: {sorted(EXPECTED_TOCS - names)}")
        for name in names:
            parts = PurePosixPath(name).parts
            if (
                not parts
                or parts[0] not in {"GuildFlow", "GuildFlow_Bridge1", "GuildFlow_Bridge2"}
                or ".." in parts
                or name.startswith("/")
                or "\\" in name
            ):
                raise SystemExit(f"Unexpected ZIP path: {name!r}")
        if z.testzip() is not None:
            raise SystemExit("Corrupt ZIP entry found")
        toc = z.read("GuildFlow/GuildFlow.toc").decode("utf-8-sig")
        if not re.search(r"(?m)^## Interface:\s*16001\s*$", toc):
            raise SystemExit("GuildFlow.toc does not target WoW Forever interface 16001")
        toc_version = re.search(r"(?m)^## Version:\s*(\S+)", toc)
        if not toc_version or toc_version.group(1) != version:
            raise SystemExit(f"Release tag {tag} does not match GuildFlow.toc Version")

    body = release.get("body") or ""
    notes = re.search(
        r"(?ms)^## What's new in GuildFlow[^\n]*\n(.*?)(?=^## |\Z)", body
    )
    # Do not silently publish a vague default text instead of a changelog.
    # English release notes in the public GitHub Release are the source of truth.
    if not notes or not re.search(
        rf"(?m)^## What's new in GuildFlow v?{re.escape(version)}\s*$", body
    ):
        raise SystemExit(
            f"GitHub Release {tag} is missing the English What's new section; "
            "CurseForge upload blocked to prevent an empty changelog."
        )
    changelog = notes.group(1).strip()
    # Do not copy the Windows installer links / signatures / downloads section.
    if len(changelog) < 40:
        raise SystemExit(f"GitHub Release {tag} has an empty or too-short changelog")
    changelog = f"GuildFlow {version}\n\n{changelog[:5500]}"

    metadata = {
        "displayName": f"GuildFlow {version} - WoW Forever",
        "changelogType": "markdown",
        "changelog": changelog,
        "gameVersionNames": ["1.60.1"],
        "releaseType": "beta",  # Remain Beta until we explicitly approve a stable CurseForge launch.
        "isMarkedForManualRelease": False,  # Publish after CurseForge moderation, without a manual click.
    }
    (HERE / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Validated official release {tag}: 3 addon folders, Forever 1.60.1, SHA-256 OK")
    print("Prepared CurseForge Beta metadata (automatically published after approval)")


if __name__ == "__main__":
    main()
