# hypotez/src/endpoints/advertisement/facebook/facebook.py

## Overview

This module provides functionality for interacting with Facebook's advertising platform via a web driver. It includes methods for login, posting messages, uploading media, and managing accounts.  It leverages the `src.webdriver` module for web driver interactions and `src.utils` for various utility functions.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [Facebook](#facebook)
        * [`__init__`](#__init__)
        * [`login`](#login)
        * [`promote_post`](#promote_post)
        * [`promote_event`](#promote_event)


## Classes

### `Facebook`

**Description**: This class handles interactions with the Facebook platform via a web driver.  It allows for managing accounts, posting messages, and uploading media.

**Attributes**:

* `d`: Instance of `src.webdriver.Driver` object.
* `start_page`: (str) The default starting URL for Facebook.
* `promoter`: (str) The identifier of the promoter account.


#### `__init__`

**Description**: Initializes a Facebook object.  Handles the connection with the facebook platform, optionally using a pre-existing driver instance.

**Parameters**:
* `driver` (Driver): The WebDriver instance (e.g. from Selenium).
* `promoter` (str):  Identifier of the promoter account.
* `group_file_paths` (list[str]): A list of file paths to upload.
* `*args`, `**kwards`: Additional arguments/keyword arguments.


**Raises**:
 * `TypeError`: If the provided driver isn't a valid Driver instance.



#### `login`

**Description**: Logs in to the Facebook account.


**Returns**:
* `bool`: `True` if login is successful, `False` otherwise.


#### `promote_post`

**Description**: Posts a message on a Facebook page.

**Parameters**:
* `item` (SimpleNamespace): An object containing data for the post.


**Returns**:
* `bool`: `True` if the post was successful, `False` otherwise.


#### `promote_event`

**Description**:  Promotes an event on Facebook.

**Parameters**:
* `event` (SimpleNamespace): Object with event details.


**Raises**:
* `Exception`: if any issue occurs during the event promotion.