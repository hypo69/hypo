Catch Page Manifest
====================

This file defines the manifest for the "Catch Page" Chrome extension.  It specifies the extension's name, version, description, and various configuration options.

.. code-block:: json
   :linenos:

   ```json
   {
     "manifest_version": 3,
     "name": "URL Sender",
     "version": "1.0",
     "description": "Sends the URL of the current page to a local server.",
     "action": {
       "default_popup": "popup.html"
     },
     "background": {
       "service_worker": "background.js"
     },
     "permissions": [ "activeTab", "storage" ]
   }
   ```