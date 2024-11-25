# hypotez/src/endpoints/advertisement/facebook/scenarios/post_message.py

## Overview

This module contains functions for posting messages to Facebook, including adding titles, descriptions, media files (images/videos), and managing the publishing process.  It leverages the `Driver` class for web interaction and utilizes locators loaded from a JSON file for targeting specific UI elements.


## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
    - [`post_title`](#post_title)
    - [`upload_media`](#upload_media)
    - [`update_images_captions`](#update_images_captions)
    - [`publish`](#publish)
    - [`promote_post`](#promote_post)
    - [`post_message`](#post_message)


## Functions

### `post_title`

**Description**: Sends the title and description of a campaign to the Facebook post message box.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `message` (SimpleNamespace): The category containing the title and description to be sent.


**Returns**:
- `bool`: `True` if the title and description were sent successfully, otherwise `None`.

**Raises**:
- `Exception`: If there's an error during the process, like a scroll or input operation failing.


### `upload_media`

**Description**: Uploads media files (images or videos) to the Facebook post and potentially updates captions.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `media` (SimpleNamespace | List[SimpleNamespace] | str | list[str]): The media files to upload. Can be a single SimpleNamespace or a list of them, or a string or list of paths.
- `no_video` (bool, optional):  If True, skip uploading videos. Defaults to `False`.
- `without_captions` (bool, optional): If True, skip updating captions for uploaded media. Defaults to `False`.

**Returns**:
- `bool`: `True` if media files were uploaded successfully, otherwise `None`.

**Raises**:
- `Exception`: If an error occurs during media upload (e.g., file not found, invalid path).


### `update_images_captions`

**Description**: Adds descriptions (captions) to uploaded media files.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `media` (List[SimpleNamespace]): List of product details.
- `textarea_list` (List[WebElement]): List of textareas where captions should be added.


**Raises**:
- `Exception`: If there's an error updating the media captions.


### `publish`

**Description**: Publishes the created Facebook post.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `attempts` (int, optional): The number of retry attempts if publishing fails. Defaults to `5`.

**Returns**:
- `bool`: `True` if the post was published successfully, otherwise `None`.

**Raises**:
- `Exception`: If errors occur during the publishing process.


### `promote_post`

**Description**: Manages the complete process of creating and promoting a Facebook post.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `category` (SimpleNamespace): Post title and description details.
- `products` (List[SimpleNamespace]): List of products with media and details.
- `no_video` (bool, optional): If True, skip uploading videos. Defaults to `False`.

**Examples**:
  Example usage is provided within the function docstring.

**Returns**:
- `bool`: `True` if the post was promoted successfully, otherwise `None`.


### `post_message`

**Description**:  Manages the process of posting a message to Facebook, handling titles, media, and publishing.


**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `message` (SimpleNamespace): The message details used for the post title and description.
- `no_video` (bool, optional): If True, skip uploading videos. Defaults to `False`.
- `images` (Optional[str | list[str]], optional):  Images to upload. Defaults to `None`.
- `without_captions` (bool, optional): If True, skip updating captions for uploaded media. Defaults to `False`.


**Returns**:
- `bool`: `True` if the message was successfully posted; otherwise `None`.

**Examples**:
  Example usage is provided within the function docstring.