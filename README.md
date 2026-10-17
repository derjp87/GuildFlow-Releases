<p align="center">
  <img src="assets/banner.png" alt="GuildFlow – Gildenorganisation für World of Warcraft: Forever" width="100%">
</p>

<p align="center">
  <a href="https://github.com/derjp87/GuildFlow-Releases/releases/latest"><img alt="Neueste Version" src="https://img.shields.io/github/v/release/derjp87/GuildFlow-Releases?style=for-the-badge&label=Version&color=e5bc43&labelColor=242327"></a>
  <img alt="Windows 10 und 11" src="https://img.shields.io/badge/Windows-10%20%7C%2011-e5bc43?style=for-the-badge&labelColor=242327">
  <img alt="World of Warcraft: Forever" src="https://img.shields.io/badge/WoW-Forever-e5bc43?style=for-the-badge&labelColor=242327">
  <img alt="12 Sprachen" src="https://img.shields.io/badge/Sprachen-12-e5bc43?style=for-the-badge&labelColor=242327">
</p>

<p align="center">
  <a href="https://github.com/derjp87/GuildFlow-Releases/releases/latest/download/GuildFlowSync-Setup.exe">
    <img alt="GuildFlow für Windows herunterladen" src="https://img.shields.io/badge/%E2%AC%87%20Herunterladen-GuildFlow%20f%C3%BCr%20Windows-e5bc43?style=for-the-badge&labelColor=141417">
  </a>
  <br>
  <sub>Programm und Addon in einem Setup · aktualisiert sich selbst ·
  <a href="https://github.com/derjp87/GuildFlow-Releases/releases/latest/download/GuildFlow.zip">nur das Addon (ZIP)</a> ·
  <a href="#english">English</a></sub>
</p>

---

## Was ist GuildFlow?

**GuildFlow** ist ein Gilden-Addon für *World of Warcraft: Forever*: Events und Raids mit Anmeldungen, Beute und
Lootcouncil, Berufe, Gildenprojekte, Statistiken – direkt im Spiel, ohne Server und ohne Konto.

**GuildFlow Sync** ist das optionale Windows-Programm dazu. Es gleicht die Gildendaten über einen Discord-Kanal
eurer Gilde ab, damit Events, Anmeldungen und Profile auch dann ankommen, wenn ihr nie gleichzeitig online seid.

<table>
  <tr>
    <th width="50%">Im Spiel (Addon)</th>
    <th width="50%">Auf dem PC (GuildFlow Sync)</th>
  </tr>
  <tr valign="top">
    <td>
      <ul>
        <li>Eigener Kalender mit Raidtagen, Anmeldungen nach Rolle und Spezialisierung, Warteliste, Erinnerungen</li>
        <li>Raidaufstellung mit Buff-Übersicht, Boss-Kills und Raidfortschritt</li>
        <li>Soft-Reserves mit Prioritäten und ein Lootcouncil mit Wunschlisten</li>
        <li>Spezialisierungen aus den Talenten (auch Dualspec), Talente jedes Mitglieds im Profil</li>
        <li>Berufe & Crafting: Rezepte finden, Gildenaufträge mit Materialplan erstellen und übernehmen, Handwerker-Twinks berücksichtigen, mögliche Ausrüstungs-Upgrades entdecken</li>
        <li>Gildenprojekte, Fortschritt, Tickets an die Gildenleitung</li>
        <li>Gildenstatistik direkt im Spiel</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Einrichtungsassistent: Addon installieren, Gilde beitreten oder einrichten</li>
        <li>Offline-Abgleich über Discord – nach jedem <code>/reload</code> und nach dem Spielen</li>
        <li>Lesbare Discord-Beiträge: Events mit Anmeldungen, Ergebnisse mit Bossen und Beute, Wochenrückblick</li>
        <li>Ausführliche Gildenstatistik mit Diagrammen, Vergleich und CSV-Export</li>
        <li>Mehrere Gilden auf einem PC, läuft unsichtbar im Hintergrund (GF-Symbol neben der Uhr)</li>
        <li>Aktualisiert sich selbst – Programm und Addon</li>
      </ul>
    </td>
  </tr>
</table>

<p align="center">
  <img src="assets/screens/main-de.png" alt="Das Hauptfenster von GuildFlow Sync" width="49%">
  <img src="assets/screens/stats-overview-de.png" alt="Die Gildenstatistik" width="49%">
</p>
<p align="center"><sub>Alle Bilder zeigen eine erfundene Testgilde.</sub></p>

## Neu: Gildenaufträge & mögliche Upgrades (ab 0.18.11)

**Handwerk innerhalb der Gilde koordinieren:** Unter **Berufe & Crafting** zeigt GuildFlow, welche Gildenmitglieder ein Rezept kennen. Wähle ein Rezept, klicke **„Rezept planen“** und erstelle einen **Gildenauftrag** mit gewünschter Anzahl und Materialzuständigkeit (Auftraggeber, Handwerker oder gemeinsame Absprache). Jeder passende Gildenhandwerker kann sich melden; die Zuteilung wird vom Auftraggeber-Charakter bestätigt, sobald dieser die Zusage online empfängt.

- **Neue Aufträge nicht verpassen:** Ein Handwerkssymbol an der **Minimap** zeigt mit einer Zahl neue Aufträge an, die du herstellen kannst. Die Kachel **„Aufträge für dich“** auf der Übersicht und eine dauerhafte Anzahl im GuildFlow-Menü zeigen passende offene Aufträge an, auch nachdem du die Minimap-Meldung gelesen hast. Kein aufdringliches Popup und kein Benachrichtigungston.
- **Handwerker-Twinks:** Wenn eigene Charaktere in GuildFlow **gegenseitig bestätigt verknüpft** sind, kannst du auch dann passende Aufträge sehen und die Herstellung anbieten, wenn das Rezept von einem anderen deiner verknüpften Charaktere beherrscht wird. GuildFlow merkt sich den tatsächlichen Rezeptbesitzer.
- **Aufträge und Materialien:** Im Auftrag werden – soweit der WoW-Client die Rezeptdaten bereitstellt – benötigte Zutaten, Gesamtmengen und die Materialzuständigkeit angezeigt. Der Status führt den zugeteilten Handwerker auf. Nach dem Herstellen markiert der Handwerker den Auftrag als gefertigt; der Auftraggeber bestätigt nach der Übergabe den Abschluss. Handel und Post bleiben im Spiel.
- **Ausrüstungsverbesserungen:** Die Kachel **„Upgrades für dich“** zeigt mögliche von Gildenmitgliedern herstellbare Rüstung und Schmuckstücke, **ausschließlich für deinen derzeit eingeloggten Charakter**, niemals für offline gespielte Twinks. Item-Tooltips zeigen die Werte; bei der Handwerkeranzahl werden Namen und Online-Status eingeblendet. Vor dem Erstellen eines Auftrags öffnet sich der Materialplaner.

**Noch in der Erprobung:** Die Upgrade-Vorschläge berücksichtigen bisher vor allem Gegenstandsstufe und grundlegende Eignung, nicht vollständig Klasse/Spezialisierung oder optimale Werte. Waffen und Verzauberungen sind noch nicht abgedeckt. Rezeptmaterialien können fehlen, wenn WoW sie nicht liefert. Die verknüpften Twink- und Offline-Szenarien benötigen weitere Praxistests. Das Addon arbeitet ohne Windows-App; für den optionalen, verzögerten Datenaustausch zwischen getrennten Spielsitzungen kann **GuildFlow Sync** verwendet werden.

## Welche Installation passt zu dir?

| Du möchtest … | So geht's |
| --- | --- |
| **Nur das WoW-Addon** | [GuildFlow auf CurseForge](https://www.curseforge.com/wow/addons/guildflow) installieren oder die [Addon-ZIP](https://github.com/derjp87/GuildFlow-Releases/releases/latest/download/GuildFlow.zip) verwenden. Keine Windows-App, kein Discord-Konto erforderlich. |
| **Addon + automatischen Offline-Abgleich + erweiterte Statistiken (Windows)** | [GuildFlowSync-Setup.exe](https://github.com/derjp87/GuildFlow-Releases/releases/latest/download/GuildFlowSync-Setup.exe) installieren. Das Setup enthält **Programm und Addon inklusive der zwei Bridge-Addons**. |
| **Addon auf macOS/Linux** | Die [Addon-ZIP](https://github.com/derjp87/GuildFlow-Releases/releases/latest/download/GuildFlow.zip) manuell installieren; das Windows-Sync-Programm läuft dort nicht. |

**Wichtig:** GuildFlow und GuildFlow Sync sind zwei verschiedene Komponenten. Der CurseForge-Download installiert **nicht** automatisch die Windows-App. Wenn sowohl CurseForge als auch GuildFlow Sync dein Addon aktualisieren, können die Update-Systeme einander überschreiben. Achte auf die installierte Version und vermeide parallele Addon-Updates durch beide Programme, bis eine automatische Erkennung der Installationsverwaltung verfügbar ist.

## Für Gildenmitglieder: GuildFlow Sync einrichten (Windows)

1. **WoW vollständig schließen**, dann [GuildFlowSync-Setup.exe](https://github.com/derjp87/GuildFlow-Releases/releases/latest/download/GuildFlowSync-Setup.exe) vom offiziellen Release herunterladen. Das Setup installiert ohne Administratorrechte. Bei einer SmartScreen-Warnung zunächst **Herkunft und Prüfsumme** anhand von `SHA256SUMS` im Release prüfen; das Setup ist bislang nicht Authenticode-codesigniert.
2. **WoW-Ordner auswählen**, falls er nicht automatisch gefunden wird. Das Setup installiert/aktualisiert GuildFlow und die beiden Bridge-Addons `GuildFlow_Bridge1` und `GuildFlow_Bridge2`; vorhandene Addon-Dateien werden gesichert. **SavedVariables und deine Gildendaten bleiben erhalten.**
3. **WoW neu starten** (nach einer erstmaligen Addon-Installation reicht `/reload` nicht), mit deinem **Gildencharakter** einloggen und GuildFlow aktiviert lassen. Falls nötig einmal `/reload`, damit der aktuelle Stand gespeichert wird.
4. **Normalerweise fertig:** Mit der standardmäßig aktivierten Option **„Gilden automatisch verbinden“** erkennt GuildFlow Sync eine Gilde, die bereits einen GuildFlow-Sync-Abgleich betreibt, und stellt den Beitritt nach einer gültigen Gildenfreigabe automatisch her. **Kein Webhook, kein Einladungslink und kein Discord-Konto für normale Mitglieder nötig.** Das kann über mehrere `/reload`-Vorgänge bzw. Spielsitzungen dauern: Ein GuildFlow-Sync-Nutzer muss als solcher erkannt worden sein, und ein berechtigter Offizier muss die Anfrage genehmigen (oder seine Auto-Freigabe aktiviert haben).
5. **Prüfen:** Öffne das **GuildFlow Sync**-Fenster oder das goldene **GF-Symbol neben der Windows-Uhr**. Dort siehst du Gilde, Verbindungsstatus und Hintergrund-Abgleich. **„Wartet auf Freigabe“** ist noch keine erfolgreiche Verbindung.

**Schnellerer Notweg:** In GuildFlow Sync gibt es unter **Erweitert → + Gilde / Einer Gilde beitreten** den Assistenten. Wenn die Gildenleitung in Discord Einladungslinks veröffentlicht, kannst du den für *deine* Anfrage bestimmten `GFJOIN3`-Link im Programm über **„Einladungslink einfügen“** übernehmen. Alternativ kann ein Offizier einen **Beitrittscode** beantworten. Für die normale Nutzung ist das nicht erforderlich.

<p align="center">
  <img src="assets/screens/wizard-de.png" alt="GuildFlow Sync: optionaler Einrichtungsassistent" width="60%">
</p>

## Für Gildenleitung & Offiziere: Discord einmalig einrichten

**Nur eine berechtigte Person pro Gilde richtet den Sync erstmals ein.** Voraussetzung: GuildFlow **und** GuildFlow Sync laufen auf deren Windows-PC; im Discord-Server sind die Rechte **„Webhooks verwalten“ / „Manage Webhooks“** für die benötigten Kanäle erforderlich.

1. **Auf dem Discord-Server der Gilde zwei Textkanäle anlegen** (Namen nur Beispiele):
   - **`#guildflow-sync` (Pflicht):** Technischer Datenaustausch. **Privat halten**, nur berechtigte Personen sollen die synchronisierten Nachrichten/Dateien sehen oder bearbeiten können; **nichts manuell löschen oder dort chatten**.
   - **`#guildflow-news` (optional):** Für Mitglieder lesbare Beiträge zu Events, Anmeldungen und Raid-Ergebnissen. Ein eigener Kanal mit **eigenem Webhook**.
   - **Optional `#guildflow-invites`:** Nur für Beitrittslinks, falls diese nicht in `#guildflow-news` stehen sollen (dritter, eigener Webhook). **Beitrittslinks posten** lässt sich auch deaktivieren.
2. **Für jeden genutzten Kanal einen Webhook erzeugen:** In Discord den jeweiligen Kanal unter **Kanal bearbeiten → Integrationen → Webhooks → Neuer Webhook → Webhook-URL kopieren** öffnen. Jeder Kanal benötigt seinen passenden Webhook. **Webhook-URLs sind geheime Schreib-Zugangsdaten**, nicht im Discord-Chat, in Bildern oder auf GitHub teilen.
3. **Im Spiel mit einem Gildenmeister-/Offizierscharakter:** GuildFlow öffnen → **Einstellungen → GuildFlow Sync**. Dort den **Sync-Webhook (Pflicht)**, den optionalen **Webhook für lesbare Beiträge** sowie gegebenenfalls den optionalen **Einladungskanal-Webhook** eingeben. Einstellung **„Einladungslinks posten“** wie gewünscht wählen, anschließend **„Speichern und neu laden“**.
4. **Übernahme abwarten:** GuildFlow Sync auf diesem PC muss im Hintergrund laufen. Nach kurzer Wartezeit nochmals **`/reload`** ausführen und im Spiel auf **„Verbunden (eingerichtet von …)“** sowie im Windows-Programm auf eine verbundene Gilde prüfen. Die Webhooks werden nach erfolgreicher Verarbeitung aus den Spieldaten entfernt.
5. **Mitglieder zulassen:** Neue GuildFlow-Sync-Mitglieder fragen normalerweise automatisch über das Spiel an. Unter **Einstellungen → GuildFlow Sync** ist **„Anfragen von Gildenmitgliedern automatisch erlauben“** standardmäßig aktiv; das gilt nur nach Prüfung der Gildenmitgliedschaft und mit einem berechtigten, verbundenen Offiziers-PC. Bei deaktivierter Auto-Freigabe im Spiel die Nachfrage **„Erlauben?“** bestätigen und `/reload` verwenden. Mitglieder müssen weder den Discord-Server betreten noch Battle.net mit Discord verknüpfen.

**So funktionieren die beiden Discord-Kanäle:** Im **Sync-Kanal** speichert GuildFlow Sync technische Gildenpostfächer für den Offline-Abgleich; er ist **nicht** zum Lesen oder Beschreiben durch Mitglieder gedacht. Im **Beitragskanal** erscheinen menschenlesbare Gildenbeiträge; ist dieser nicht eingerichtet, funktioniert der eigentliche Offline-Abgleich trotzdem. Einladungslinks können – je nach Einstellung – dort, in einem dritten Kanal oder gar nicht gepostet werden; der automatische Beitritt über das Spiel bleibt möglich.

**Wichtig bei Mitgliederentfernung / Sicherheitsvorfall:** Einen PC aus GuildFlow Sync zu entfernen widerruft seinen zuvor bekannten Webhook **nicht**. Wenn der Zugriff entzogen werden soll, muss ein Offizier den Discord-Zugang über **„Neue Hooks verbinden“** beziehungsweise den vorgesehenen Rotationsweg ersetzen und danach den **alten Webhook in Discord löschen**. Bei mehreren PCs anschließend die Aktualisierung prüfen.

## Im Alltag und bei Updates

- Die Gildendaten werden nach dem Spielen bzw. bei gespeichertem Stand durch `/reload` mit Discord abgeglichen. Wenn WoW geschlossen ist, lädt GuildFlow Sync Änderungen anderer PCs in konfigurierbaren Abständen. Eingehende Daten stehen spätestens nach dem nächsten geeigneten Laden im Spiel bereit; ein sofortiger Live-Austausch über Discord ist nicht möglich.
- GuildFlow Sync kann im Hintergrund laufen (GF-Symbol im Infobereich). Ein Klick auf **„Nach Updates suchen“** prüft Updates manuell; signierte automatische Programmupdates erfolgen nach der vorgesehenen Prüfung, wenn WoW geschlossen ist.
- Falls du das Addon **über CurseForge** verwaltest, kontrolliere die Version nach einem GuildFlow-Sync-Update. Beide Programme könnten dieselben Addon-Dateien verändern.
- Für das **reine WoW-Addon** ohne Windows-App: Die [GuildFlow.zip](https://github.com/derjp87/GuildFlow-Releases/releases/latest/download/GuildFlow.zip) enthält **drei Ordner** (`GuildFlow`, `GuildFlow_Bridge1`, `GuildFlow_Bridge2`). Entpacke sie **nebeneinander** nach `<WoW-Installation>/Interface/AddOns/`. Alternativ das Addon direkt mit CurseForge installieren. WoW nach der ersten Installation neu starten; öffnen über `/gf` oder den GuildFlow-Reiter im Gildenfenster (`J`).

## Gildenstatistik

<p align="center">
  <img src="assets/screens/stats-loot-de.png" alt="Beute in der Gildenstatistik" width="49%">
  <img src="assets/screens/stats-member-de.png" alt="Verlauf eines Mitglieds" width="49%">
</p>

Übersicht, Mitglieder (mit Verlauf jedes Mitglieds), Events, Beute, Lootcouncil, Raids und Projekte – über 7 Tage
bis zum ganzen Archiv, im Vergleich zum vorherigen Zeitraum. Die Statistik liest nur die Dateien auf deinem PC,
auch während WoW läuft, und braucht keine Gildenverbindung.

## Sicherheit und Datenschutz

- **Kein zusätzlicher Heimserver / Discord-Bot nötig:** Das WoW-Addon nutzt WoW-Addon-Nachrichten. Die **optionale** Windows-App nutzt Discord-Webhooks und Gildenpostfächer – die Gilde benötigt dafür ihren eigenen Discord-Server. Mitglieder brauchen dafür **kein persönliches Discord-Konto**.
- **Technischer Sync-Kanal schützen:** Daten im Discord-Postfach sind **nicht Ende-zu-Ende-verschlüsselt**. Discord-Webhook-URLs erlauben weitreichende Aktionen und werden auf dem PC mit Windows-DPAPI geschützt gespeichert; die URLs niemals weitergeben oder veröffentlichen. Offenlegen oder Verlust eines PCs kann **Webhook-Rotation** erfordern.
- **Private Inhalte:** Private Tickets und vertrauliche Probezeit-/Offiziersnotizen werden **nicht** über das Discord-Postfach ausgetauscht. Das Windows-Statistikfenster wertet lokale WoW-Daten aus.
- **Installationsdateien:** Das Setup ist noch nicht mit einer Windows-Authenticode-Herausgebersignatur versehen. Release-Manifeste nutzen Ed25519-Prüfung für automatische Updates. Die SHA-256-Prüfsummen stehen in **`SHA256SUMS`** beim offiziellen Release. Prüfe Herkunft und Prüfsumme bei Browser-/SmartScreen-/Antivirenwarnungen und melde unerwartete Funde, statt Schutzfunktionen pauschal auszuschalten.

## Häufige Fragen / Troubleshooting

<details>
<summary><b>GuildFlow erscheint nicht im Spiel</b></summary>

WoW nach einer neuen Addon-Installation **vollständig beenden und neu starten**. Prüfe, ob `Interface/AddOns/GuildFlow/GuildFlow.toc` existiert und GuildFlow im Addon-Menü aktiviert ist. Bei der Windows-Komplettinstallation außerdem `GuildFlow_Bridge1` und `GuildFlow_Bridge2` prüfen. `/reload` genügt nur für bereits geladene Addons.
</details>

<details>
<summary><b>GuildFlow Sync zeigt „Wartet auf Freigabe“ oder erkennt keine Gilde</b></summary>

Mit einem **echten Gildencharakter** in der passenden WoW-Installation anmelden, das Addon laden und `/reload` ausführen. Im Windows-Programm **„Gilden automatisch verbinden“** und **Hintergrund-Abgleich** prüfen. Mindestens ein berechtigter GuildFlow-Sync-Offizier muss erreichbar sein bzw. über die Weiterleitung erreicht werden; dessen Freigabe und ein weiterer `/reload`/Spielstart können erforderlich sein. Das Mitglied benötigt **keinen Discord-Webhook**. Wenn es dennoch klemmt: im Programm **Erweitert → + Gilde → Einer Gilde beitreten**, gegebenenfalls den **GFJOIN3**-Link einfügen. Keine Webhooks oder privaten Dateien im Supportchat posten.
</details>

<details>
<summary><b>Die Discord-Beiträge fehlen / ich sehe keine Einladungslinks</b></summary>

Der **Sync-Kanal** enthält nur technische Daten; normale Beiträge brauchen einen **separaten lesbaren Kanal samt Webhook**. Einladungslinks sind optional und können deaktiviert oder in einen dritten Kanal verschoben sein. Ob Mitglieder selbst Zugang zu diesen Kanälen haben, entscheidet die Discord-Gildenleitung; **für den automatischen In-Game-Beitritt ist kein Discord-Zugang erforderlich**.
</details>

<details>
<summary><b>Der Hintergrund-Abgleich ist gestoppt / es erscheinen keine neuen Daten</b></summary>

GuildFlow Sync öffnen, Verbindungs- und Hintergrundstatus prüfen und gegebenenfalls den Abgleich über das Programm erneut starten. Programmversion und Addonversion vergleichen und den letzten Abgleich ansehen. Änderungen in WoW werden erst beim gespeicherten Spielstand (Logout/`/reload`) für das Programm sichtbar; ein Offline-Download wird erst beim geeigneten nächsten Laden ins Spiel eingespielt. Falls der Prozess sofort wieder stoppt, ein **geheimnisfreies** Protokoll aus dem Programm an die Entwickler geben – niemals Webhooks, Einladungsschlüssel oder komplette SavedVariables mitsenden.
</details>

<details>
<summary><b>Windows oder der Browser warnt beim Download</b></summary>

Das Windows-Setup ist noch nicht mit Authenticode signiert; dadurch sind Warnungen möglich. Lade nur aus diesem offiziellen Release-Repository. Vergleiche die SHA-256-Prüfsumme mit `SHA256SUMS` (z. B. PowerShell: `Get-FileHash .\\GuildFlowSync-Setup.exe -Algorithm SHA256`). Bei einem blockierten Download oder Virenscannerfund erst überprüfen und nachfragen, nicht pauschal den Schutz deaktivieren.
</details>

<details>
<summary><b>Warum darf GuildFlow Sync während WoW läuft manches nicht schreiben?</b></summary>

WoW schreibt die gespeicherten Addon-Daten selbst beim Logout/`/reload`. Deshalb überschreibt GuildFlow Sync die Datei `GuildFlow.lua` nicht während WoW läuft. Die beiden optionalen Bridge-Addons ermöglichen ausgewählte Antworten auch während einer laufenden Spielsitzung.
</details>

<details>
<summary><b>Ich habe mehrere Charaktere oder Gilden</b></summary>

GuildFlow Sync kann mehrere WoW-Installationen und Gilden getrennt verwalten; ein Twink derselben Gilde braucht normalerweise keine zweite Verbindung. Im Fenster die richtige Gilde und den entsprechenden Charakterstatus kontrollieren.
</details>

<details>
<summary><b>Wie entferne ich GuildFlow?</b></summary>

In Windows die App **GuildFlow Sync** deinstallieren. Das WoW-Addon kannst du in CurseForge oder durch Entfernen der drei Addon-Ordner deinstallieren. Dabei bleiben deine WoW-SavedVariables und die verschlüsselte lokale GuildFlow-Sync-Konfiguration möglicherweise erhalten; sie nicht unbedacht mitsamt anderen WoW-Daten löschen.
</details>

---

## Neu in GuildFlow 0.18.15 – Überblick und Funktionen

GuildFlow für **World of Warcraft: Forever** unterstützt die Gildenorganisation direkt im Spiel. Die überarbeitete Oberfläche fasst Mitglieder, Termine, aktuelle Aktivitäten und Gildenziele kompakt zusammen.

**Mitglieder und Ausrüstung:** Profile mit Rollen, Berufen, Talenten und Ausrüstungsplätzen. Die Ausrüstungsansicht im Spiel zeigt ein drehbares 3D-Charaktermodell, soweit die WoW-Daten es zulassen. Bei entfernten Charakteren kann eine angenäherte Ansicht angezeigt werden.

**Events, Raids und Beute:** Gildenkalender, Anmeldungen, Rollenplanung, Raidfortschritt, Lootcouncil, Soft Reserves und Gildenstatistiken.

**Berufe und Gildenaufträge:** Rezepte finden, passende Handwerker kontaktieren und einzelne Gildenaufträge mit Menge und Materialverantwortung erstellen. Die persönliche Einkaufsliste fasst Materialien für eigene Herstellungen und Gildenaufträge, bei denen du Materialien stellst, zusammen. Geplante Rezepte bleiben als „Selbst herstellen“ oder „Ohne Auftrag“ gekennzeichnet; die Auswahl eines Eintrags veröffentlicht noch keinen Auftrag.

**Optionaler Windows-Client GuildFlow Sync:** Offline-Datenabgleich zwischen Spielsitzungen, detaillierte Gildenstatistik und eine eigene 3D-Armory mit angelegter Ausrüstung, Drehung, Zoom und Posen. Das WoW-Addon funktioniert auch ohne GuildFlow Sync.

Das vollständige [Changelog und die Downloads](https://github.com/derjp87/GuildFlow-Releases/releases) enthalten die jeweiligen Änderungen pro Version.

<a id="english"></a>

## English – Installation & Discord setup

**GuildFlow** is a standalone guild addon for *World of Warcraft: Forever*: events, raids, raid/loot management, professions, projects and statistics. **GuildFlow Sync** is a **free, optional Windows companion** with Discord-based offline synchronization and extended statistics. The addon works without the Windows app or a Discord account.

### Guild crafting orders & possible upgrades (v0.18.11)

In **Professions & Crafting**, find guild members who know a recipe, choose **Create guild order**, and create a **guild crafting order** specifying quantity and who provides materials (requester, crafter, or arrange together). An eligible crafter offers to craft; the requester's character confirms one assigned crafter upon receiving the offer online. The crafter can mark the item crafted, and the requester confirms delivery.

- **Minimap alerts:** A small crafting icon with an unread count shows newly available orders you can fulfill. The **Jobs you can craft** overview card and persistent Overview count show eligible open requests. No disruptive time-limited popup or sound.
- **Linked crafting alts:** When your own characters are mutually verified and linked in GuildFlow, you can see and offer on jobs even while playing a different linked character; the recipe-owning alt is identified.
- **Order details:** Where WoW supplies the recipe data, see required materials, quantities, supplier responsibility, assigned crafter and Blizzard item tooltips.
- **Possible gear upgrades:** Personal suggestions for guild-craftable armor and jewelry are presented in the overview's relevant next steps for **your currently logged-in character only**. Hover for item stats or crafter names and online status; inspect the material planner before submitting an order.

**Beta limitations:** Suggestions use conservative item-level/basic equipment comparisons, not full class/spec optimization. Weapons and enchants are excluded. Recipe details may be unavailable; alt/offline scenarios still need live verification. GuildFlow Sync is optional and does not guarantee instant offline delivery.

<p align="center">
  <img src="assets/screens/main-en.png" alt="GuildFlow Sync Windows companion" width="49%">
  <img src="assets/screens/stats-overview-en.png" alt="Extended statistics" width="49%">
</p>

### What's new in GuildFlow 0.18.15

**Redesigned in-game guild dashboard** brings together guild status, roles, next steps, upcoming raids and shared goals. **Members and gear** include profile details, talents, equipment slots and a rotatable 3D character where live inspection is supported (or a clearly identified approximation for distant members). **Raids and guild management** include calendars, signups, assignments, loot council, soft reserves and statistics.

**Guild crafting orders and personal shopping:** Find recipes and their crafters, create individual orders specifying quantity and responsibility for reagents, and plan your own crafts. The combined private shopping list tracks materials for your own recipes and confirmed orders where you bring the materials. Each planned recipe can be marked as your own production or as not yet ordered, without automatically creating orders.

**GuildFlow Sync for Windows is optional.** It adds offline guild synchronization, detailed statistics and a separate 3D Armory with equipped characters, zoom and pose controls. The addon works without the Windows app.

See the [releases](https://github.com/derjp87/GuildFlow-Releases/releases) for version-specific changes and downloads.

### For players

1. **Addon only:** install [GuildFlow on CurseForge](https://www.curseforge.com/wow/addons/guildflow), or use [GuildFlow.zip](https://github.com/derjp87/GuildFlow-Releases/releases/latest/download/GuildFlow.zip). The ZIP contains three side-by-side folders (`GuildFlow`, `GuildFlow_Bridge1`, `GuildFlow_Bridge2`) for your `Interface/AddOns` directory.
2. **Optional Windows offline sync:** close WoW, download the official [GuildFlowSync-Setup.exe](https://github.com/derjp87/GuildFlow-Releases/releases/latest/download/GuildFlowSync-Setup.exe), and install. It includes the addon and bridges. Select your WoW folder if needed, then restart WoW completely (not just `/reload` after first-time installation).
3. Log in on a **guild character**. With **Automatically connect guilds** enabled (the default), GuildFlow Sync should request access automatically after your addon has discovered someone using the guild's existing Sync setup. A guild officer must approve (or have eligible auto-approval enabled). You normally **do not** need a Discord login, webhook, invite code or manual wizard. It may take a `/reload`, another game session, or time for the officer's approval.
4. Check the Windows **GuildFlow Sync** window or the gold **GF tray icon**. **Waiting for approval** does not mean Connected. If needed, use **Advanced → + Guild → Join a guild** and paste the request-specific `GFJOIN3` link provided by your officers as a fallback.

### For guild leaders & officers (one-time Discord setup)

1. Create a **private technical sync text channel** on your guild's Discord server (e.g. `#guildflow-sync`). Optionally create a **separate readable posts channel** (e.g. `#guildflow-news`) for event/signup/raid summaries, and optionally a third channel for invitation links. Do not let ordinary members edit or delete technical postbox messages.
2. With **Manage Webhooks** permission, create a **separate webhook per channel**: **Edit Channel → Integrations → Webhooks → New Webhook → Copy Webhook URL**. Treat URLs like passwords: never publish them or paste them in chats/screenshots.
3. Install the **Windows companion + addon** on the officer's PC, sign into WoW on the guild officer character and open **GuildFlow → Settings → GuildFlow Sync** in-game. Enter the **required sync webhook**, optional **readable-posts webhook**, and optional invite channel webhook; configure invite-link posting. Choose **Save and reload**.
4. Keep GuildFlow Sync running in Windows; after a short wait, issue another `/reload` to collect the confirmation. Confirm **Connected** in game and in the Windows program.
5. Member requests are normally sent automatically. **Automatically approve guild-member requests** is enabled by default, but still verifies membership and requires an eligible authorized officer setup. If disabled, approve the request in-game and `/reload`. **Regular members do not need Discord access, a Discord/Battle.net link, or any webhook.**

The technical sync channel is **not** the chat bridge; it stores GuildFlow's offline data. Readable posts are optional and require their own webhook. When someone leaves, simply removing their local GuildFlow Sync connection does **not** revoke a shared webhook: rotate guild Discord access using the in-game **Replace / reconnect hooks** function and delete the old webhook in Discord after the replacement is distributed.

### Updates, safety & help

GuildFlow Sync can update itself and the installed addon. If CurseForge also manages the addon, check for **conflicting addon updates**; the two systems are not yet integrated. A first install requires a full WoW restart. Subsequent data updates may require `/reload`, logging out or another login. The installer is not yet Windows Authenticode-signed; verify downloads against `SHA256SUMS` from this official repository before choosing to run a warned installer.

Discord webhook URLs are sensitive write credentials. The Windows application encrypts them locally with DPAPI, but the shared Discord postbox is **not end-to-end encrypted**. Private tickets and confidential officer/trial notes are **not** sent to Discord. Never include webhooks, access codes, complete SavedVariables, or local configuration secrets in reports.

If you need help, check whether the **addon and both bridge addons** are enabled, your **guild character** was actually logged in, auto-connect and background sync are active, and an **officer** can approve access. The manual **Join a guild** wizard and request-specific invite link are fallbacks. Keep any diagnostic screenshots and logs secret-free.

---

**For maintainers / Für Entwickler:** [CurseForge upload automation](docs/CURSEFORGE_RELEASE_AUTOMATION.md) · [All versions & release notes](https://github.com/derjp87/GuildFlow-Releases/releases).

