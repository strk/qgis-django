========================
QGIS Plugins application
========================

Author: Alessandro Pasotti (www.itopen.it)

The Plugin model
================

The plugin model represents a QGIS plugin and holds general informations such as title and description and icon.

The plugin can have zero or more owners, owners have the same permissions of the original creator.

Permissions
-----------

These rules have been implemented:

* every registered user can add a new plugin
* *staff* users can approve or disapprove all plugin versions
* users which have the special permission `plugins.can_approve` can approve their own plugins versions
* users which have the special permission `plugins.can_approve` can approve versions in the plugins they own
* a particular plugin can be deleted and edited only by *staff* users and owners
* if a user without `plugins.can_approve` permission uploads a new version, the plugin version is unapproved.


Trust management
----------------

Staff members can grant *trust* to selected plugin creators setting `plugins.can_approve` permission through the front-end application.

The plugin details view offers direct links to grant trust to the plugin creator or the plugin owners.


The PluginVersion model
=======================

Each plugin can have several versions, a version specify the minimum QGIS version needed in order to run that particular plugin version and other informations such as if the version belongs to the "stable" o to the "experimental" branch.

Validation
----------

The validation takes place in the PluginVersions forms, at loading time, the compressed file is checked for:

* file size <= `PLUGIN_MAX_UPLOAD_SIZE`
* zip contains `__init__.py` in first level dir
* `__init__.py` must contain valid metadata:
    * `name`
    * `description`
    * `version`
    * `qgisMinimumVersion`

* in case of version editing or addition, `name` metadata must be = to plugin's name
* `version` must be unique whithin a plugin
* there must be one and only *last* versions in each plugin's branch



Configuration
=============

All values can be overridden in `settings.py`

========================== ============= =======================
Parameter                  Default       Notes
========================== ============= =======================
PLUGINS_STORAGE_PATH       packages
PLUGIN_MAX_UPLOAD_SIZE     1048576       in bytes
PLUGINS_FRESH_DAYS         30            days
MAIL_FROM_ADDRESS          -             used in email notifications
========================== ============= =======================

