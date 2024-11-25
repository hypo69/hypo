manifest.json
==========

.. note::

   This file describes the manifest for the "Borderify" extension.  It defines the extension's metadata, including its name, version, description, icons, and content scripts.


Manifest Data
------------

.. code-block:: json
   :linenos:

   ```json
   {
     "manifest_version": 2,
     "name": "Borderify",
     "version": "1.0",
 
     "description": "Adds a red border to all webpages matching mozilla.org.",
 
     "icons": {
       "48": "icons/icon.png"
     },
 
     "content_scripts": [
       {
         "matches": [ "<all_urls>" ],
         "js": [ "borderify.js" ]
       }
     ]
   }
   ```