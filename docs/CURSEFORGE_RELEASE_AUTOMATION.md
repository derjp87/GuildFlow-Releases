# CurseForge-Veröffentlichung / CurseForge publishing

Dieses Dokument richtet sich an Maintainer. Für Installation und Discord-Einrichtung siehe [README](../README.md).

## CurseForge addon updates (GitHub Releases → CurseForge)

**GitHub Releases in this public repository are the only upload trigger for CurseForge.** The private development repository does **not** publish files directly to CurseForge.

The workflow [`Publish GuildFlow to CurseForge`](.github/workflows/publish-curseforge.yml) runs when a **new release is published here**, or manually via **Actions → Publish GuildFlow to CurseForge → Run workflow** for an existing release tag. It fetches the **exact same `GuildFlow.zip`** and `SHA256SUMS` assets from that release, validates the checksum, version and required three addon folders, then submits **the original ZIP unchanged** to CurseForge **project 1742845** for **WoW Forever 1.60.1**.

- **One-time setup (per 2026-10-13 screenshot completed, verify during first run):** Repository owner → **Settings → Secrets and variables → Actions → New repository secret** → name **`CF_API_TOKEN`**; value is your **CurseForge author upload API token**. The token must never appear in the repo, issue, screenshot, release body or chat. The workflow shows a notice and does **not** upload while the secret is missing.
- **Current publishing mode:** uploads are **Beta** and configured to become available **automatically after CurseForge approves the file**. The project can separately remain **Unlisted** until you're ready to launch. Switch the metadata to **release** deliberately when stable and tested.
- **First/catch-up test:** the workflow did not exist when `v0.18.7` was published, so *after the secret has been added*, you can start it manually for `v0.18.7` **if this version is not already on CurseForge**. **Do not rerun successful uploads**; the API creates a new file each time.
- **Version compatibility:** the upload uses `gameVersionNames: ["1.60.1"]`; ZIP validation requires `## Interface: 16001`. Verify the first upload is correctly classified as **WoW Forever** in CurseForge.
- **Status (2026-10-13):** Workflow vorhanden; Projektinhaber hat die Anlage des GitHub Actions Repository Secret `CF_API_TOKEN` per Screenshot bestätigt. Ein erfolgreicher authentifizierter CurseForge-Upload ist noch nicht nachgewiesen. API-Antwort und Dateistatus im CurseForge-Autorenportal prüfen.

CurseForge page: [GuildFlow](https://www.curseforge.com/wow/addons/guildflow) · [Author preview](https://www.curseforge.com/wow/addons/guildflow/preview). The Windows `GuildFlowSync-Setup.exe` stays **only on GitHub**, not in the CurseForge addon ZIP.

---

