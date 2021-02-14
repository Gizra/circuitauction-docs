# Drush

## Category tree - Resave all

Queue all Category term for tree rebuild using advanced queue.

```text
$ drush @site-alias scr profiles/backoffice/modules/server_term/script/resave_categories.php
```

{% hint style="info" %}
Go to /admin/reports/queue to monitor AQ tasks.
{% endhint %}

## Set default address

After address migration we need to run this script to set the main client address.

```text
$ drush @site-alias scr profiles/backoffice/modules/server_address/drush/set_default_addresses.php
```

