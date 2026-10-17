# CurseForge-Veröffentlichung / CurseForge publishing

Dieses Dokument richtet sich an Maintainer. Für Installation und Discord-Einrichtung siehe [README](../README.md).

## CurseForge addon updates (GitHub Releases → CurseForge)

**GitHub Releases in this public repository are the only upload trigger for CurseForge.** The private development repository does **not** publish files directly to CurseForge.

The workflow [`Publish GuildFlow to CurseForge`](.github/workflows/publish-curseforge.yml) runs when a **new release is published here**, or manually via **Actions → Publish GuildFlow to CurseForge → Run workflow** for an existing release tag. It fetches the **exact same `GuildFlow.zip`** and `SHA256SUMS` assets from that release, validates the checksum, version and required three addon folders, then submits **the original ZIP unchanged** to CurseForge **project 1742845** for **WoW Forever 1.60.1**.

- **One-time setup (per 2026-10-13 screenshot completed, verify during first run):** Repository owner → **Settings → Secrets and variables → Actions → New repository secret** → name **`CF_API_TOKEN`**; value is your **CurseForge author upload API token**. The token must never appear in the repo, issue, screenshot, release body or chat. The workflow shows a notice and does **not** upload while the secret is missing.
- **Current publishing mode:** uploads are **Beta** and configured to become available **automatically after CurseForge approves the file**. The project can separately remain **Unlisted** until you're ready to launch. Switch the metadata to **release** deliberately when stable and tested.
- **Verified first automatic release:** `v0.18.8` was submitted successfully to moderation (CurseForge file ID `9164783`). **Do not re-run successful releases**; the API creates another file. Old releases such as v0.18.7 should only be backfilled deliberately if necessary.
- **Version compatibility:** the upload uses `gameVersionNames: ["1.60.1"]`; ZIP validation requires `## Interface: 16001`. Verify the first upload is correctly classified as **WoW Forever** in CurseForge.
- **Verified 2026-10-13:** Public GitHub Release **v0.18.8** triggered `Publish GuildFlow to CurseForge` automatically. All validation/upload steps passed, and CurseForge's upload API replied **“CurseForge accepted file ID 9164783 for moderation.”** Destination CurseForge project **1742845**. **The upload is confirmed.** Do not manually upload or re-run v0.18.8, to avoid duplicate files.
- **Confirmed in CurseForge Files UI (2026-10-13):** Both `GuildFlow 0.18.8 – WoW Forever` (automated API upload, file ID `9164783`) and `GuildFlow 0.18.6 – WoW Forever` (earlier manual upload) show green **Approved**, type **Beta**, game version **1.60.1**. Screenshot showed 0 downloads for 0.18.8 and 3 for 0.18.6 at capture time. This confirms moderation approval. CurseForge client **discovery** was confirmed afterwards; actual installation and update behavior remain to be tested.

- **CurseForge desktop client discovery confirmed (2026-10-13):** A newer client now offers the **Forever** game flavor (the older client had incorrectly labeled the `_classic_beta_` game folder as **MoP Classic Beta**). With **Forever** selected, searching `guildflow` under Browse returns **1 project**: GuildFlow by `derjp87`, game version **1.60.1**. This confirms that the project is discoverable in the CurseForge client **without changing the three-folder ZIP or promoting the Beta release**. **Actual installation/update behavior and interaction with GuildFlow Sync have not yet been tested.**

CurseForge page: [GuildFlow](https://www.curseforge.com/wow/addons/guildflow) · [Author preview](https://www.curseforge.com/wow/addons/guildflow/preview). The Windows `GuildFlowSync-Setup.exe` stays **only on GitHub**, not in the CurseForge addon ZIP.

---

## Image gallery and public README for 0.18.15 (17 October 2026)

The project owner wants **all twelve real screenshots** in the **CurseForge project gallery** and embedded **at the bottom** of this repository's public `README.md`. These include the real in-game equipment/3D view, raid/calendar and crafting, the normal GuildFlow Sync Windows client, Windows Armory and Windows statistics.

- The image pack is provided to the project owner as `GuildFlow_0.18.15_Alle_12_CurseForge_840px.zip`. Each of the 12 PNG files is **at most 840 pixels wide**.
- **One-time GitHub import required before the next release:** extract the pack and run `UPLOAD_GITHUB.cmd` (Python 3 plus authenticated GitHub CLI required). It retrieves the importer from `tools/import_gallery.py`, verifies all 12 images and hashes, commits all PNGs to `assets/screenshots/0.18.15/` and **only then** embeds them as Markdown images at the **end of public README.md**. It is repeat-safe for existing files. No individual browser uploads are needed.
- **Current status:** public repository does not yet contain the binary PNGs; do not assume images are uploaded just because the importer exists. The Windows-side one-time import must complete.
- **Automatic release attachment and description:** `.github/workflows/release-screenshots.yml` runs when a new public release is published, embeds the twelve screenshots at the **bottom of that GitHub Release's description**, and attaches a separate `GuildFlow-0.18.15-Screenshots.zip` containing all 12 versioned images, provided the GitHub import was completed first. No Addon release is created by the screenshot importer.
- **CurseForge project gallery remains manual:** use the project's author dashboard to upload the twelve PNGs and replace outdated ones. The automated CurseForge **addon file + file changelog** upload does not update the project's images or long project description.
- Review real Windows-client images for identifiable guild details before making all 12 screenshots public. Never publish Discord webhooks or access tokens.

