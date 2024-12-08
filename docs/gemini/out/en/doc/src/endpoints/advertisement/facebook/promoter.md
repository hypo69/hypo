# hypotez/src/endpoints/advertisement/facebook/promoter.py

## Overview

This module handles the promotion of messages and events in Facebook groups. It processes campaigns and events, posting them to Facebook groups while avoiding duplicate promotions.  It leverages a WebDriver instance for browser automation.

## Table of Contents

* [Classes](#classes)
    * [FacebookPromoter](#facebookpromoter)
* [Functions](#functions)
    * [get_event_url](#geteventurl)
* [Error Handling](#error-handling)
* [Module Level Constants](#module-level-constants)


## Classes

### FacebookPromoter

**Description**: A class for promoting AliExpress products and events in Facebook groups. It automates posting promotions to Facebook groups, ensuring categories and events are promoted and avoiding duplicates.

**Attributes**:

- `d` (Driver): WebDriver instance for browser automation.
- `group_file_paths`: List of file paths containing group data.
- `no_video` (bool): Flag to disable videos in posts.
- `promoter` (str): Identifier for the promoter (e.g., 'aliexpress').
- `spinner` (spinning_cursor): Instance for displaying a spinner during promotion.

**Methods**:

#### `__init__`

**Description**: Initializes the promoter for Facebook groups.

**Parameters**:

- `d` (Driver): WebDriver instance for browser automation.
- `promoter` (str): Identifier for the promoter (e.g., 'aliexpress').
- `group_file_paths` (list[str | Path] | str | Path, optional): List of file paths containing group data. Defaults to fetching files from a predefined path.
- `no_video` (bool, optional): Flag to disable videos in posts. Defaults to `False`.


#### `promote`

**Description**: Promotes a category or event in a Facebook group.

**Parameters**:

- `group` (SimpleNamespace): Data about the Facebook group.
- `item` (SimpleNamespace): Data about the category or event to promote.
- `is_event` (bool, optional): Flag to indicate if the promotion is for an event. Defaults to `False`.
- `language` (str, optional): Language for promotion.
- `currency` (str, optional): Currency for promotion.

**Returns**:
- `bool`: `True` if promotion was successful, `False` otherwise.

#### `log_promotion_error`

**Description**: Logs an error during promotion.

**Parameters**:

- `is_event` (bool): Indicates whether promotion was for an event.
- `item_name` (str): Name of the item that failed to promote.

#### `update_group_promotion_data`

**Description**: Updates group promotion data with the new promotion.

**Parameters**:

- `group` (SimpleNamespace): Data about the Facebook group.
- `item_name` (str): Name of the promoted item.
- `is_event` (bool, optional):  Indicates whether promotion was for an event. Defaults to `False`.

#### `process_groups`

**Description**: Processes all groups for the current campaign or event promotion.

**Parameters**:

- `campaign_name` (str, optional): Name of the campaign.
- `events` (list[SimpleNamespace], optional): List of events to promote.
- `is_event` (bool, optional): Flag to indicate if the promotion is for events. Defaults to `False`.
- `group_file_paths` (list[str], optional): List of group file paths to process.
- `group_categories_to_adv` (list[str], optional): List of group categories to advertise. Defaults to ['sales'].
- `language` (str, optional): Language for promotion.
- `currency` (str, optional): Currency for promotion.


#### `get_category_item`

**Description**: Fetches the category item for promotion based on the campaign and promoter.

**Parameters**:

- `campaign_name` (str): Name of the campaign.
- `group` (SimpleNamespace): Data about the Facebook group.
- `language` (str): Language for promotion.
- `currency` (str): Currency for promotion.


**Returns**:
- `SimpleNamespace`: Item to promote.

#### `check_interval`

**Description**: Checks if the interval between promotions has passed for a group.

**Parameters**:

- `group` (SimpleNamespace): Data about the Facebook group.

**Returns**:
- `bool`: `True` if interval has passed, `False` otherwise.


## Functions

### get_event_url

**Description**: Returns the modified URL for creating an event on Facebook.

**Parameters**:

- `group_url` (str): Facebook group URL containing `group_id`.
- `event_id` (str): Event identifier.

**Returns**:
- `str`: Modified URL for creating the event.


## Error Handling

The code includes `logger.error` and `logger.debug` calls to log errors and debug messages. It also includes `if not` checks to handle potential `None` values and exceptions like file reading errors.


## Module Level Constants

The code defines a `MODE` constant.