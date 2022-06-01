# Drush

## Category tree - Resave all

Queue all Category term for tree rebuild using advanced queue.

```
$ drush @site-alias scr profiles/backoffice/modules/custom/server_term/script/resave_categories.php
```

{% hint style="info" %}
Go to /admin/reports/queue to monitor AQ tasks.
{% endhint %}

## Set default address

After address migration we need to run this script to set the main client address.

```
$ drush @site-alias scr profiles/backoffice/modules/server_address/drush/set_default_addresses.php
```

## Resave items or any other node type.

Resave a node type.

**Options**

* \-`-type`The node type.
* `--sale_nid`Filter by Sale context.
* `--start_from_nid` and `--range`

```
$ drush @site-alias scr profiles/backoffice/modules/server_general/scripts/resave.php --start_from_nid=1 --range=500 --type=item --sale_nid=123
```

