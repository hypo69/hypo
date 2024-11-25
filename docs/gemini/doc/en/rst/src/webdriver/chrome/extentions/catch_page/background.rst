background.js
============

This file contains the background script for a Chrome extension, specifically handling messages and sending collected data to a server.  It listens for messages with the action 'collectData' and triggers a data sending function.


.. autofunction:: sendDataToServer
   :noindex:
   :show-inheritance:

.. autofunction:: chrome.action.onClicked.addListener
   :noindex:
   :show-inheritance:

.. autofunction:: chrome.tabs.sendMessage
   :noindex:
   :show-inheritance:

.. autofunction:: chrome.runtime.onMessage.addListener
   :noindex:
   :show-inheritance:

.. autofunction:: chrome.storage.local.get
   :noindex:
   :show-inheritance:


Functions
--------


.. autofunction:: sendDataToServer
   :noindex:
   :show-inheritance:
   :members: