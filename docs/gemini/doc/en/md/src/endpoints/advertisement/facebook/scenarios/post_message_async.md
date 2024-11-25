# hypotez/src/endpoints/advertisement/facebook/scenarios/post_message_async.py

## Overview

This module provides asynchronous functions for posting messages to Facebook, including adding a title and description, uploading media files, and updating captions. It leverages the `Driver` class for interacting with the Facebook web page and `SimpleNamespace` for structured data handling.  The module relies on JSON locators for various elements on the page.

## Table of Contents

* [post_title](#post-title)
* [upload_media](#upload-media)
* [update_images_captions](#update-images-captions)
* [promote_post](#promote-post)


## Functions

### `post_title`

**Description**: Sends the title and description of a campaign to the Facebook post message box.  It handles scrolling and opening the post box before adding the message.

**Parameters**:

- `d` (Driver): The driver instance used for interacting with the webpage.
- `category` (SimpleNamespace): The category containing the title and description to be sent.

**Returns**:

- `bool`: `True` if the title and description were sent successfully, otherwise `None` is returned implicitly indicating failure.

**Examples**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
post_title(driver, category) # Returns True or implicitly returns None
```

**Raises**:

- `None` (implicit):  Returns `None` if there's an error during any of the webpage interactions (scroll, open post box, add message).   Error details are logged using `logger`.


### `upload_media`

**Description**: Asynchronously uploads media files to the images section and updates captions.

**Parameters**:

- `d` (Driver): The driver instance used for interacting with the webpage.
- `products` (List[SimpleNamespace]): List of products containing media file paths.
- `no_video` (bool, optional):  Flag to skip uploading video if present. Defaults to `False`.

**Returns**:

- `bool`: `True` if media files were uploaded successfully, otherwise `None` is returned implicitly indicating failure.

**Raises**:

- `Exception`: If there is an error during media upload or caption update. Error details are logged using `logger`.


### `update_images_captions`

**Description**: Adds descriptions to uploaded media files asynchronously using a separate thread.

**Parameters**:

- `d` (Driver): The driver instance used for interacting with the webpage.
- `products` (List[SimpleNamespace]): List of products with details to update.
- `textarea_list` (List[WebElement]): List of textareas where captions are added.

**Raises**:

- `Exception`: If there's an error updating the media captions. Error details are logged using `logger`.


### `promote_post`

**Description**: Manages the entire process of promoting a post with a title, description, and media files.  This function orchestrates calls to other functions.

**Parameters**:

- `d` (Driver): The driver instance used for interacting with the webpage.
- `category` (SimpleNamespace): The category details used for the post title and description.
- `products` (List[SimpleNamespace]): List of products containing media and details to be posted.
- `no_video` (bool, optional):  Flag to skip uploading video if present. Defaults to `False`.

**Examples**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
await promote_post(driver, category, products)
```

**Returns**:

- `bool`: `True` if the post was promoted successfully.  Implicitly returns `None` if there is an error at any stage of the process.

**Raises**:

- `None` (implicit): Returns `None` if errors occur during `post_title`, `upload_media`, or any other function call. Error details are logged using `logger`.