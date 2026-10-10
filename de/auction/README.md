<!-- i18n source=auction/README.md sha=8a52174986d8 -->
# Auktion

Das Auktionsmodul verwaltet Live-Auktions-Sessions, in denen Bieter in Echtzeit um Lose konkurrieren.

## Überblick

Während einer Live-Auktion steuert der Auktionator über den **Clerk Screen** den Auktionsablauf, nimmt Gebote aus mehreren Kanälen entgegen (Saal, Telefon, online) und erfasst die Zuschläge.

## Wichtige Funktionen

- **Gebote in Echtzeit** - Gebote von Saal-, Telefon- und Online-Bietern gleichzeitig entgegennehmen
- **Session-Verwaltung** - Start, Pause und Abschluss der Auktion steuern
- **Gebotsverfolgung** - Alle Gebote mit Bieterinformationen und Zeitstempeln erfassen
- **Losnavigation** - Die Lose der Reihe nach durchgehen oder gezielt zu einem Los springen
- **Ergebniserfassung** - Lose als verkauft, übergangen oder zurückgezogen markieren

## Dokumentation

- **[Ablauf der Live-Auktion](/de/auction/auction-flow.md)** - Der vollständige Auktionsablauf im Überblick
- **[Der Clerk Screen](/de/auction/clerk-screen/README.md)** - Ausführliche Anleitung zum Bedienfeld des Auktionators

## Ablauf

1. Die Auktion mit zugewiesenen Losnummern einrichten
2. Die Auktions-Session konfigurieren
3. Die Auktion starten und den Status auf „live“ setzen
4. Die Gebote Los für Los bearbeiten
5. Das Ergebnis für jedes Los erfassen
6. Die Session am Ende der Auktion abschließen

Eine Schritt-für-Schritt-Anleitung zur Bedienung des Clerk Screens finden Sie in der [Dokumentation zum Clerk Screen](/de/auction/clerk-screen/README.md).
