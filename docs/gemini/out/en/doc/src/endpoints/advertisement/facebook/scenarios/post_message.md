# hypotez/src/endpoints/advertisement/facebook/scenarios/post_message.py

## Overview

This module contains functions for posting messages to Facebook advertisements. It handles tasks such as inputting titles and descriptions, uploading media (images and videos), and publishing the post.  The module utilizes the `selenium.webdriver.remote.webelement` and `src` modules for web interaction and data handling.  Error handling and logging are implemented.


## Table of Contents

- [Classes](#classes)
- [Functions](#functions)
    - [`post_title`](#post_title)
    - [`upload_media`](#upload_media)
    - [`update_images_captions`](#update_images_captions)
    - [`publish`](#publish)
    - [`promote_post`](#promote_post)
    - [`post_message`](#post_message)


## Functions

### `post_title`

**Description**: Sends the title and description of a campaign to the Facebook post message box.  It handles both `SimpleNamespace` and string input for the message.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `message` (SimpleNamespace | str): The title and description of the campaign.  Can be a `SimpleNamespace` object with `title` and `description` attributes or a string.

**Returns**:
- `bool`: `True` if the title and description were sent successfully, otherwise `None`.  Returns `None` if there's a scroll or add post box failure.


### `upload_media`

**Description**: Uploads media files (images and videos) to the Facebook post and updates captions.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `media` (SimpleNamespace | List[SimpleNamespace] | str | list[str]): The media to upload. Can be a single `SimpleNamespace` object with a `local_image_path` or `local_video_path` attribute or a list of such objects, or a string or list of strings representing media file paths.
- `no_video` (bool, optional): Flag to skip video upload if present. Defaults to `False`.
- `without_captions` (bool, optional): Flag to skip caption update. Defaults to `False`.

**Returns**:
- `bool`: `True` if media files were uploaded successfully, otherwise `None`. Returns `None` or raises exception if `open_add_foto_video_form` is not found.


**Raises**:
- `Exception`: If there's an error during media upload or caption update.


### `update_images_captions`

**Description**: Adds descriptions to uploaded media files based on provided product details. Handles both LTR and RTL language directions.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `media` (List[SimpleNamespace]): List of products with details to update.
- `textarea_list` (List[WebElement]): List of textareas where captions are added.

**Raises**:
- `Exception`: If there's an error updating the media captions.


### `publish`

**Description**: Attempts to publish the post. Handles potential errors during publishing.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `attempts` (int, optional): Number of attempts to publish. Defaults to 5.

**Returns**:
- `bool`: `True` if the post was published successfully, otherwise `None`.


### `promote_post`

**Description**: Manages the process of promoting a Facebook post by first posting the title and description, then uploading media files, and finally publishing the post.


**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `category` (SimpleNamespace): The campaign details (title and description).
- `products` (List[SimpleNamespace]): List of media files to upload.
- `no_video` (bool, optional): Flag to skip video upload. Defaults to `False`.

**Examples**:  (see function docstrings)


### `post_message`

**Description**: Manages the process of posting a message to Facebook Ads, including title, description, media upload, and publishing.

**Parameters**:
- `d` (Driver): The driver instance used for interacting with the webpage.
- `message` (SimpleNamespace): The message details to post.
- `no_video` (bool, optional): Flag to skip video upload. Defaults to `False`.
- `images` (Optional[str | list[str]], optional): Images to upload. Defaults to None.
- `without_captions` (bool, optional): Flag to skip caption update. Defaults to `False`.

**Returns**:
- `bool`: `True` if the post was published successfully, otherwise `None`.


**Examples**: (see function docstrings)

## Classes

(No classes are defined in this module)