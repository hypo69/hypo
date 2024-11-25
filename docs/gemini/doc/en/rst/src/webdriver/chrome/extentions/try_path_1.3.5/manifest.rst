manifest.json
==========

This file defines the manifest for the "Try xpath" Chrome extension.  It specifies the extension's metadata, including its version, name, description, icons, permissions, and background scripts.

.. code-block:: json
   :linenos:
   
   {
       "manifest_version": 3,
       "name": "Try xpath",
       "description": "This extension displays the result of evaluating xpath expression or CSS selector.",
       "version": "1.3.5",
       "icons": {
           "48": "icons/icon_48.png"
       },
       "permissions": [
           "<all_urls>",
           "storage"
       ],
       "action": {
           "default_icon": "icons/icon_48.png",
           "default_title": "Try xpath",
           "default_popup": "popup/popup.html"
       },
       "background": {
           "service_worker": "background/try_xpath_background.js"
       },
       "content_scripts": [
           {
               "matches": ["<all_urls>"],
               "js": ["scripts/try_xpath_functions.js"]
           }
       ]
   }

Metadata
--------

The manifest specifies various aspects of the extension, including:


*   **manifest_version**: Defines the version of the manifest file format.
*   **name**: The display name of the extension.
*   **description**: A brief description of the extension's functionality.
*   **version**: The version number of the extension.
*   **icons**:  Specifies icons for different sizes.
*   **permissions**: Lists the permissions required by the extension.
*   **action**: Contains the action metadata, including icon, title, and popup information.
*   **background**: Defines the background script.
*   **content_scripts**: Defines scripts that run in specific web pages.