```rst
post_message_async.py
=======================

.. module:: hypotez.src.endpoints.advertisement.facebook.scenarios.post_message_async
    :platform: Windows, Unix
    :synopsis: This module contains functions for posting messages on Facebook.


Functions
---------

.. autofunction:: hypotez.src.endpoints.advertisement.facebook.scenarios.post_message_async.post_title
.. autofunction:: hypotez.src.endpoints.advertisement.facebook.scenarios.post_message_async.upload_media
.. autofunction:: hypotez.src.endpoints.advertisement.facebook.scenarios.post_message_async.update_images_captions
.. autofunction:: hypotez.src.endpoints.advertisement.facebook.scenarios.post_message_async.promote_post

Module Details
--------------

This module provides asynchronous functions for posting advertisements on Facebook.
It handles tasks such as composing titles and descriptions, uploading media, and publishing the post.


.. note::

   This module relies on the `src.webdriver.Driver` class for interacting with the web browser and `src.logger` for logging operations.  Also, it assumes appropriate locator data is loaded from the JSON file `post_message.json`.
```