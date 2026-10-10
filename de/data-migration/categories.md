<!-- i18n source=data-migration/categories.md sha=92603d6352b1 -->

# Kategorien

Handler: `ServerCategoriesDriveMigrate`.

Importiert Terme in das Vokabular `categories`. Der Handler ist für wiederholte Durchläufe ausgelegt: Bestehende Terme werden über ihren Wert `field_hk_cat_id` zugeordnet (gesetzt aus `_hk_id` in der CSV), sodass ein zweiter Durchlauf dieselben Terme aktualisiert, statt Duplikate anzulegen.

Konfiguriert über die Drupal-Variable `migrate_categories_csv`. Ist sie nicht gesetzt, greift der Handler auf die mitgelieferte Datei `data/csv/taxonomy_term/categories_philately.csv` des Moduls zurück.

**Standardquelle:** [https://docs.google.com/spreadsheets/d/1I-TVXkBx3_wnVDEsCbxRu99rO0BFHnmCVtMVTKcOsYk/edit#gid=1962137688](https://docs.google.com/spreadsheets/d/1I-TVXkBx3_wnVDEsCbxRu99rO0BFHnmCVtMVTKcOsYk/edit#gid=1962137688)

## Quelldatei

Tragen Sie die **CSV-Export-URL** Ihres Google Sheets in der Variable `migrate_categories_csv` ein. Die URL muss die CSV-Form sein, nicht der normale `edit`-Link:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/export?format=csv&gid=<SHEET_GID>
```

Die zugehörige Bearbeiten-URL (Ursprung) sieht so aus:

```
https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit?gid=<SHEET_GID>#gid=<SHEET_GID>
```

## Spalten

| Spalte | Ziel |
|---|---|
| `__id` | ID zur Zeilenverfolgung (erforderlich) |
| `_hk_id` | `field_hk_cat_id` — Primärschlüssel, über den bestehende Terme gefunden werden |
| `_pwp_country` | `field_philasearch_id` |
| `_pwp_unterkat` | `field_phila_sub_id` |
| `_name_{language}` | Name des Terms in der jeweiligen Sprache (`_name_en`, `_name_he`, …). Die Standardsprache der Website befüllt den `name` des Terms. |
| `_label_for_catalog_{language}` | `field_label_for_catalogue` in der jeweiligen Sprache |
| `_weight` | Gewichtung des Terms |
| `_cantalogue_context` | `field_category_context` |
| `_heading_level_in_catalog` (konfigurierbar) | `field_heading_level_in_catalog`. Die Quellspalte wird aus `server_migrate_categories_heading_level_in_catalog_column` gelesen. |
| `parent_hk_id` (konfigurierbar) | Suche des hierarchischen Elternterms. Der Name der Quellspalte wird aus `server_migrate_categories_parent_id_column` gelesen. Der Handler ermittelt daraus über `field_hk_cat_id` die `tid` des Elternterms. |

{% hint style="info" %}
Die Standardzuordnung (über den Namen des Terms) ist deaktiviert — Terme werden ausschließlich über `field_hk_cat_id` zugeordnet. Zwei verschiedene HK-IDs mit demselben Namen dürfen absichtlich nebeneinander bestehen.
{% endhint %}

Ein Term, der sich selbst als Elternterm referenziert (`parent_hk_id` ergibt dieselbe `tid`), bleibt stillschweigend ohne Elternterm; zur Nachvollziehbarkeit wird ein Hinweis in die Warteschlange gestellt.
