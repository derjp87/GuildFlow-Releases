# CurseForge-Veröffentlichung / CurseForge publishing

Dieses Dokument richtet sich an Maintainer. Für Installation und Discord-Einrichtung siehe [README](../README.md).

## CurseForge addon updates (GitHub Releases → CurseForge)

**GitHub Releases in this public repository are the only upload trigger for CurseForge.** The private development repository does **not** publish files directly to CurseForge.

The workflow [`Publish GuildFlow to CurseForge`](.github/workflows/publish-curseforge.yml) runs when a **new release is published here**, or manually via **Actions → Publish GuildFlow to CurseForge → Run workflow** for an existing release tag. It fetches the **exact same `GuildFlow.zip`** and `SHA256SUMS` assets from that release, validates the checksum, version and required three addon folders, then submits **the original ZIP unchanged** to CurseForge **project 1742845** for **WoW Forever 1.60.1**.

- **One-time setup (per 2026-10-13 screenshot completed, verify during first run):** Repository owner → **Settings → Secrets and variables → Actions → New repository secret** → name **`CF_API_TOKEN`**; value is your **CurseForge author upload API token**. The token must never appear in the repo, issue, screenshot, release body or chat. The workflow shows a notice and does **not** upload while the secret is missing.
- **Current publishing mode:** uploads are **Beta** and configured to become available **automatically after CurseForge approves the file**. The project can separately remain **Unlisted** until you're ready to launch. Switch the metadata to **release** deliberately when stable and tested.
- **Verified first automatic release:** `v0.18.8` was submitted successfully to moderation (CurseForge file ID `9164783`). **Do not re-run successful releases**; the API creates another file. Old releases such as v0.18.7 should only be backfilled deliberately if necessary.
- **Version compatibility:** the upload uses `gameVersionNames: ["1.60.1"]`; ZIP validation requires `## Interface: 16001`. Verify the first upload is correctly classified as **WoW Forever** in CurseForge.
- **Verified 2026-10-13:** Public GitHub Release **v0.18.8** triggered `Publish GuildFlow to CurseForge` automatically. All validation/upload steps passed, and CurseForge's upload API replied **“CurseForge accepted file ID 9164783 for moderation.”** Destination CurseForge project **1742845**. **The upload is confirmed; moderator approval, final publication and CurseForge client installation have not yet been checked.** Do not manually upload or re-run v0.18.8, to avoid duplicate files.

CurseForge page: [GuildFlow](https://www.curseforge.com/wow/addons/guildflow) · [Author preview](https://www.curseforge.com/wow/addons/guildflow/preview). The Windows `GuildFlowSync-Setup.exe` stays **only on GitHub**, not in the CurseForge addon ZIP.

---

