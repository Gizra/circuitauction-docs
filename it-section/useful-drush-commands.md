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

## Resave items

Reasve a node type.

**Options**
* --type={node type}
* --sale_nid={Sale context}
* --start_from_nid and --range=500 

```text
$ drush @site-alias scr profiles/backoffice/modules/server_general/scripts/resave.php --start_from_nid=1 --range=500 --type=item --sale_nid=123
```

