<!-- i18n source=website/user-block.md sha=2879617de865 -->
# Benutzermenü

**Selektor:** `#user-block` &nbsp;•&nbsp; *einmal pro Seite*

## Funktion

Das Konto-Widget für den Seitenkopf Ihrer Website. Ist der Besucher **abgemeldet**, zeigt es Links zum Anmelden bzw. Registrieren. Ist er **angemeldet**, zeigt es seinen Namen mit dem Anfangsbuchstaben als Avatar und ein Dropdown-Menü: *My Account, My Bids & Credit, Billing, My Favorites, My Interests, Logout*. Der Eintrag „Billing“ erscheint nur, wenn die Abrechnung für Ihre Website aktiviert ist.

Es aktualisiert sich automatisch, wenn sich der Benutzer an- oder abmeldet (kein Neuladen der Seite nötig).

## So fügen Sie es hinzu

```html
<div id="user-block" class="circuit-user-ui"></div>
```

## Optionen

Keine. Das Menü wird anhand des angemeldeten Benutzers und Ihrer Website-Konfiguration dargestellt.

## Siehe auch

- [Anmeldung](/de/website/login.md), [Registrierung](/de/website/register.md) — die Seiten, auf die die Links für abgemeldete Besucher verweisen
- Die Menüeinträge entsprechen [Mein Konto](/de/website/my-account.md), [Meine Gebote](/de/website/my-bids.md), [Abrechnung & Zahlungen](/de/website/billing.md), [Meine Favoriten](/de/website/my-favorites.md) und [Meine Interessen](/de/website/my-interests.md)
