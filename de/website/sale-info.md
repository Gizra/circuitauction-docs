<!-- i18n source=website/sale-info.md sha=49bd8cd0cd31 -->
# Auktionsinfo

**Selektor:** `#ca-sale-info` &nbsp;•&nbsp; *einmal pro Seite*

## Funktion

Ein eigenständiger Informationsblock für eine einzelne Auktion. Er zeigt Auktionslogo, Titel, Untertitel, formatierten Datumsbereich, Ort, Abteilungsbezeichnungen, eine aufklappbare Beschreibung „About This Sale“ sowie – sofern vorhanden – Download-Links (PDF-Katalog, E-Book, Auktionsergebnisse). Logo und Titel verlinken zur Auktionsseite.

Verwenden Sie ihn als Kopfbereich einer eigenen Auktions-Landingpage, als Sidebar-Widget oder als Abteilungsvorschau — überall dort, wo Sie Auktionsdetails ohne die vollständige Losliste anzeigen möchten.

## So fügen Sie es hinzu

```html
<div id="ca-sale-info" class="circuit-user-ui" data-sale-nid="123"></div>
```

## Optionen

| Attribut | Erforderlich | Wirkung |
|-----------|----------|--------|
| `data-sale-nid` | **Ja** | Die NID der Auktion, die angezeigt werden soll. |

Dieser Block hat keine weiteren Optionen.

### Datumsformatierung

Datumsangaben werden intelligent formatiert:

- Einzelner Tag → `January 11, 2026`
- Gleicher Monat → `January 13–16, 2026`
- Verschiedene Monate → `January 28 – February 3, 2026`
- Verschiedene Jahre → `December 30, 2025 – January 2, 2026`

## Beispiele

```html
<!-- Sale header, then a featured carousel below it -->
<div id="ca-sale-info"      class="circuit-user-ui" data-sale-nid="123"></div>
<div id="ca-featured-items" class="circuit-user-ui" data-sale-nid="123"
     data-item-display="lot-number"></div>
```

> Um mehrere Auktionen gleichzeitig aufzulisten, verwenden Sie stattdessen den Block [Auktionsliste](website/sales-list.md) — Auktionsinformation stellt nur eine einzelne Auktion dar.
