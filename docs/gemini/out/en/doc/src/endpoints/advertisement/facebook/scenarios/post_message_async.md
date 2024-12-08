# hypotez/src/endpoints/advertisement/facebook/scenarios/post_message_async.py

## Overview

This module contains asynchronous functions for posting advertisements on Facebook, specifically focusing on the creation and publishing of posts. It handles the process of adding titles, descriptions, media files, and captions to the post. The module integrates with the `Driver` class for web interaction, `gs` for configuration, and custom logging (`logger`).  It employs asynchronous operations (`asyncio`) to improve efficiency when uploading and adding captions to multiple media files.

## Classes

### (No classes defined in this module)


## Functions

### `post_title`

**Description**: Sends the title and description of a campaign to the Facebook post message box. Handles error cases, including failed scrolling or opening the add post box, by logging errors and returning `None`.

**Parameters**:

- `d` (Driver): The driver instance for interacting with the Facebook webpage.
- `category` (SimpleNamespace): A `SimpleNamespace` object containing the title and description of the campaign.

**Returns**:

- `bool`: `True` if the title and description were sent successfully, otherwise `None`.


### `upload_media`

**Description**: Uploads media files (images or videos) to the Facebook post and updates associated captions.  Handles errors during upload and caption updates, logging them appropriately.  Robustly handles different input types for `products` parameter.

**Parameters**:

- `d` (Driver): The driver instance for interacting with the Facebook webpage.
- `products` (List[SimpleNamespace]): A list of `SimpleNamespace` objects representing the media files to be uploaded, along with other relevant product details.
- `no_video` (bool, optional): Defaults to False. If True, it will only upload images. Defaults to `False`.

**Returns**:

- `bool`: `True` if media files were uploaded successfully, otherwise `None`.

**Raises**:

- `Exception`: If any error occurs during media upload or caption update.  The exception and relevant stack trace are logged.



### `update_images_captions`

**Description**: Asynchronously adds descriptions to the uploaded media files.  Uses localized strings and handles both LTR and RTL text directions for captions. Uses asyncio for asynchronous handling.

**Parameters**:

- `d` (Driver): The driver instance for interacting with the Facebook webpage.
- `products` (List[SimpleNamespace]): List of product details to update captions for.
- `textarea_list` (List[WebElement]): List of textareas where the captions should be added.


**Raises**:

- `Exception`: If any error occurs during caption update.  The exception and relevant stack trace are logged.



### `promote_post`

**Description**: Manages the complete process of promoting a post, including sending the title and description, uploading media, and finishing post editing and publishing. This function is asynchronous and will wait for the upload to complete and for the post to be published.  It provides clear error handling, logging errors, and returning `None` in case of failure at any step.


**Parameters**:

- `d` (Driver): The driver instance used for interacting with the webpage.
- `category` (SimpleNamespace): The details of the campaign for the post title and description.
- `products` (List[SimpleNamespace]): A list of product details for adding media and captions to the post.
- `no_video` (bool, optional): Defaults to False. If True, it will only upload images. Defaults to `False`.

**Returns**:

- `bool`: `True` if the post was promoted successfully. `None` if any step in the process fails.

**Examples**:

The examples in the docstrings showcase usage scenarios and expected input types.


## Modules Used

- `time`
- `asyncio`
- `pathlib`
- `types`
- `typing`
- `selenium.webdriver.remote.webelement`
- `src.gs`
- `src.webdriver.driver`
- `src.utils.jjson`
- `src.logger`