# hypotez/src/endpoints/advertisement/facebook/scenarios/__init__.py

## Overview

This module provides functions for interacting with Facebook advertisements.  It handles various scenarios, including login, posting messages, switching accounts, and posting events/ads.

## Table of Contents

- [Login](#login)
- [Post Message](#post-message)
- [Switch Account](#switch-account)
- [Post Event](#post-event)
- [Post Ad](#post-ad)

## Functions

### `login`

**Description**:  Handles Facebook login.

**Parameters**:
None

**Returns**:
- `dict | None`: Returns a dictionary containing login information, or `None` on failure.


**Raises**:
- `LoginError`:  If login fails.


### `post_message`

**Description**: Posts a message to a Facebook page.


**Parameters**:
-  None

**Returns**:
-  `dict | None`:  Returns a dictionary with post details on success or `None` on failure.

**Raises**:
- `PostError`: If the post fails to publish.


### `post_message_title`

**Description**: Sets the title of a Facebook message post.


**Parameters**:
- None

**Returns**:
- `dict | None`:  Returns a dictionary with post details on success or `None` on failure.

**Raises**:
- `TitleError`: If the title cannot be set.


### `upload_post_media`

**Description**: Uploads media (images) for a Facebook post.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary containing media upload information on success or `None` on failure.

**Raises**:
- `UploadError`: If media upload fails.

### `update_post_media_captions`

**Description**: Updates captions for images in a Facebook post.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary containing updated caption details on success or `None` on failure.

**Raises**:
- `CaptionError`: If caption updates fail.


### `message_publish`

**Description**: Publishes a Facebook message post.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary with post details on success or `None` on failure.

**Raises**:
- `PublishError`: If publishing the post fails.



### `switch_account`

**Description**: Switches to a different Facebook account.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary with account switch details on success, or `None` on failure.

**Raises**:
- `SwitchError`: If switching accounts fails.



### `post_event_title`

**Description**: Sets the title of a Facebook event post.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary with event title details on success or `None` on failure.

**Raises**:
- `TitleError`: If the title cannot be set.



### `post_event_description`

**Description**: Sets the description of a Facebook event post.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary with event description details on success or `None` on failure.

**Raises**:
- `DescriptionError`: If the description cannot be set.


### `post_date`

**Description**: Sets the date of a Facebook event post.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary with event date details on success or `None` on failure.

**Raises**:
- `DateError`: If the date cannot be set.


### `post_time`

**Description**: Sets the time of a Facebook event post.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary with event time details on success or `None` on failure.

**Raises**:
- `TimeError`: If the time cannot be set.



### `post_event`

**Description**: Posts a Facebook event.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary with event details on success or `None` on failure.

**Raises**:
- `EventError`: If the event fails to publish.



### `post_ad`

**Description**: Posts a Facebook ad.


**Parameters**:
- None

**Returns**:
- `dict | None`: Returns a dictionary with ad details on success or `None` on failure.

**Raises**:
- `AdError`: If the ad fails to publish.