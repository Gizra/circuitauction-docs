<!-- i18n source=release-notes/version-3.1.md sha=e6181b9d863c -->
# Version 3.1

Veröffentlicht im Juli 2025. Diese Version führt Inhaltstypen für Lose ein, einen vollständigen Los-Stammbaum bei Einlieferungen, einen KI-Assistenten im Hilfebereich, verbundene Backoffices und mehrere Website-Funktionen für WordPress-Seiten.

## Lose & Katalogisierung

### Auswahl des Inhaltstyps mit dynamischer Vorschau

Lose haben jetzt einen **Content Type**. Wählen Sie ihn aus einer Liste, die Briefmarken, Münzen, Bücher, Postkarten, Baseballkarten, Sport-Memorabilia, Uhren & Schmuck, Wein & Spirituosen, Kunst, Antiquitäten, Sammelkarten und Vintage-Poster umfasst.

- Die Los-Vorschau aktualisiert sich sofort entsprechend dem gewählten Inhaltstyp.
- Es werden nur die Felder angezeigt, die für den gewählten Inhaltstyp relevant sind, was das Losformular übersichtlicher macht.
- Die Funktion steht im Backoffice für alle Kunden zur Verfügung. Die Darstellung der neuen Felder im Frontend setzt die WordPress-Integration voraus.
- Zusätzliche Felder für einen Inhaltstyp können als kostenpflichtige Anpassung ergänzt werden.

### Filter nach Los-Tags und hervorgehobene Lose

- Die Lose-Tabelle hat einen neuen Filter **item tags**, um markierte Lose schneller zu finden.
- WordPress-Seiten können ein **Karussell mit hervorgehobenen Losen** anzeigen, das auf diesen Tags beruht, siehe [Hervorgehobene Lose](../website/featured-items.md).

## Einlieferungen

### Tab All Items (Family Tree)

Ein neuer Tab **All Items (Family Tree)** auf der Einlieferungsseite zeigt alle Lose, die mit der ursprünglichen Einlieferung verbunden sind, über mehrere Auktionen hinweg.

- Verschobene oder geklonte Lose behalten ihre Beziehung zur ursprünglichen Einlieferung.
- Der Verlauf jedes Loses lässt sich in einem Akkordeon aufklappen, und mehrere Verläufe können gleichzeitig geöffnet sein.

## Hilfe & Support

### KI-Assistent

Der Hilfebereich enthält jetzt einen **AI Assistant**, der Fragen auf Support-Level 1 zur Nutzung des Backoffice beantwortet. Er ist rund um die Uhr verfügbar und wird mit dem Wachstum der Wissensdatenbank besser.

## Kunden & Website

### Fachliche Referenzen

Ein neues Feld **Referenzen** in der Circuit User UI wird mit dem Kundendatensatz im Backoffice synchronisiert.

### E-Mail-Einstellungen unter "Mein Konto"

Kunden können direkt auf der Seite **My Account** der Website E-Mails an- oder abbestellen, siehe [Mein Konto](../website/my-account.md).

### Verwaltung von Magazinabonnements (WordPress)

WordPress-Seiten können die Magazinabonnements von Kunden verwalten: Abonnementtypen, automatische Ablaufverfolgung und ein schlanker Abonnementablauf, siehe [Magazinabonnement](../website/subscription-magazine.md).

## Verbundene Backoffices (Beta)

Mehrere Backoffices derselben Gruppe können jetzt miteinander verbunden werden.

- Kunden werden über die E-Mail-Adresse zugeordnet, und ihre Beziehungen werden zwischen den verbundenen Backoffices synchronisiert.
- Lose können von einem Backoffice in ein anderes geklont werden (Beta). Das Klonen erfordert eine individuelle Konfiguration der Feldzuordnung, die als kostenpflichtige Einrichtung angeboten wird.

## Versand

### EasyPost-Integration eingestellt

Wegen anhaltender Zuverlässigkeitsprobleme wurde die EasyPost-Integration aus dem Backoffice entfernt. Eine alternative Versand-API wurde geprüft und in [Version 3.3](version-3.3.md) eingeführt.
