manifest.json
==========

.. automodule:: manifest
    :members:
    :undoc-members:
    :show-inheritance:

Description
-----------

This file defines the manifest for the Hypotez extension.  It specifies the extension's metadata, permissions, background service worker, popup, icons, and host permissions.

Manifest Structure
-----------------

The manifest is a JSON object defining various aspects of the extension.

Key Attributes
~~~~~~~~~~~~~

- ``manifest_version``: The version of the manifest format (currently 3).
- ``name``: The name of the extension ("Hypotez").
- ``version``: The version number of the extension ("1.0").
- ``description``: A description of the extension ("Collects data from web pages and sends it to a server.").
- ``permissions``: An array of permissions required by the extension (["activeTab", "storage", "scripting"]).
- ``background``: Specifies the background service worker file ("borderify.js").
- ``action``: Configuration for the extension's action (e.g., popup).
-   ``default_popup``: Path to the default popup HTML file ("html/popup.html").
-   ``default_icon``: Specifies icons for different sizes ("icons/icon.png").
- ``icons``: Specifies icons for different sizes. Same as action.default_icon, but separate for completeness.
- ``host_permissions``: A list of host permissions to access various web pages. ("https://*/*", "http://*/*").