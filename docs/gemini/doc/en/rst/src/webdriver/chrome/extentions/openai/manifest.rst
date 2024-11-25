OpenAI Model Interface Manifest
==============================

.. contents:: Table of Contents
   :depth: 2

This file defines the manifest for the OpenAI Model Interface Chrome extension.  It specifies various aspects of the extension's behavior, including its name, version, description, permissions, background script, action icon and popup, and content security policies.


Manifest File
------------

.. code-block:: json
   :linenos:

   ```json
   {
     "manifest_version": 3,
     "name": "OpenAI Model Interface",
     "version": "1.0",
     "description": "Interface for interacting with OpenAI model",
     "permissions": [
       "activeTab"
     ],
     "background": {
       "service_worker": "background.js"
     },
     "action": {
       "default_popup": "index.html",
       "default_icon": {
         "16": "icons/16.png",
         "48": "icons/48.png",
         "128": "icons/128.png"
       },
       "default_width": 750, // 3/4 ширины экрана
       "default_height": 600
     },
     "icons": {
       "16": "icons/16.png",
       "48": "icons/48.png",
       "128": "icons/128.png"
     },
     "content_security_policy": {
       "extension_pages": "script-src \'self\'; object-src \'self\';"
     }
   }
   ```

Manifest Details
---------------

*   **manifest_version:** Specifies the manifest file version.
*   **name:**  The name of the extension.
*   **version:** The current version of the extension.
*   **description:** A description of the extension's purpose.
*   **permissions:** A list of permissions required by the extension (e.g., `activeTab`).
*   **background:** Configuration for the background script.
*   **service_worker:** The name of the background service worker.
*   **action:** Configuration for the extension's action (e.g., popup).
*   **default_popup:** The name of the HTML file that will be displayed when the extension's action is clicked.
*   **default_icon:** Specifies the icon for the extension.
*   **icons:** Specifies icons for various sizes.
*   **content_security_policy:** Security policy settings for the extension's content.