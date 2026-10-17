"""Regression checks for the automatic CurseForge release changelog."""
import hashlib
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from tools import prepare_curseforge_upload as uploader


class CurseForgeMetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.here = Path(self.temp.name)
        archive = self.here / "GuildFlow.zip"
        with zipfile.ZipFile(archive, "w") as z:
            z.writestr("GuildFlow/GuildFlow.toc",
                       "## Interface: 16001\n## Version: 0.18.15\n")
            z.writestr("GuildFlow_Bridge1/GuildFlow_Bridge1.toc", "## Version: 0.18.15")
            z.writestr("GuildFlow_Bridge2/GuildFlow_Bridge2.toc", "## Version: 0.18.15")
        sha = hashlib.sha256(archive.read_bytes()).hexdigest()
        (self.here / "SHA256SUMS").write_text(
            f"{sha}  GuildFlow.zip\n", encoding="utf-8"
        )

    def run_uploader(self, body, tag="v0.18.15"):
        (self.here / "release.json").write_text(
            json.dumps({"tagName": tag, "body": body}), encoding="utf-8"
        )
        with patch.object(uploader, "HERE", self.here), patch.object(
            uploader, "ARCHIVE", self.here / "GuildFlow.zip"
        ):
            uploader.main()
        return json.loads((self.here / "metadata.json").read_text(encoding="utf-8"))

    def test_full_release_body_generates_real_changelog_not_download_links(self):
        body = (
            "## Neu in GuildFlow 0.18.15\n\nDeutsche Änderungen.\n\n"
            "## What's new in GuildFlow 0.18.15\n\n"
            "- New guild interface with improved member equipment display.\n"
            "- Crafting orders and a unified personal shopping list.\n\n"
            "## Download\n\nExternal link and installer instructions.\n"
        )
        metadata = self.run_uploader(body)
        self.assertEqual(metadata["changelogType"], "markdown")
        self.assertEqual(metadata["gameVersionNames"], ["1.60.1"])
        self.assertEqual(metadata["releaseType"], "beta")
        self.assertIn("unified personal shopping list", metadata["changelog"])
        self.assertNotIn("External link", metadata["changelog"])

    def test_missing_notes_refuses_upload(self):
        with self.assertRaisesRegex(SystemExit, "missing the English"):
            self.run_uploader("## Download\n\nJust downloads")

    def test_wrong_version_refuses_upload(self):
        with self.assertRaisesRegex(SystemExit, "missing the English"):
            self.run_uploader(
                "## What's new in GuildFlow 0.18.14\n\n"
                "A reasonable but stale changelog with old features.")
    def test_empty_notes_refuses_upload(self):
        with self.assertRaisesRegex(SystemExit, "too-short"):
            self.run_uploader("## What's new in GuildFlow 0.18.15\n\nFixes.")


if __name__ == "__main__":
    unittest.main()
