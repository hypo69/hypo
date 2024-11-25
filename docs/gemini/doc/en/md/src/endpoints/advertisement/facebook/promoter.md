# hypotez/src/endpoints/advertisement/facebook/promoter.py

## Overview

This module handles the promotion of messages and events in Facebook groups. It processes campaigns and events, posting them to Facebook groups while avoiding duplicate promotions.  It utilizes a WebDriver instance for browser automation and incorporates error handling and logging.  Crucially, it manages the promotion process by checking intervals between promotions for each group.

## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
    - [`get_event_url`](#get_event_url)
- [Classes](#classes)
    - [`FacebookPromoter`](#facebookpromoter)
        - [`__init__`](#facebookpromoter__init__)
        - [`promote`](#facebookpromoterpromote)
        - [`log_promotion_error`](#facebookpromoterlog_promotion_error)
        - [`update_group_promotion_data`](#facebookpromoterupdate_group_promotion_data)
        - [`process_groups`](#facebookpromoterprocess_groups)
        - [`get_category_item`](#facebookpromoterget_category_item)
        - [`check_interval`](#facebookpromotercheck_interval)
        - [`parse_interval`](#facebookpromoterparse_interval)
        - [`run_campaigns`](#facebookpromoterrun_campaigns)
        - [`run_events`](#facebookpromoterrunevents)
        - [`stop`](#facebookpromoterstop)


## Functions

### `get_event_url`

**Description**: Constructs the URL for creating a Facebook event within a specific group.

**Parameters**:
- `group_url` (str): The URL of the Facebook group.

**Returns**:
- str: The constructed URL for creating the event.


## Classes

### `FacebookPromoter`

**Description**: A class for automating the promotion of AliExpress products and events in Facebook groups. It handles the process of posting, avoiding duplicates, and updating group promotion data.

#### `__init__`

**Description**: Initializes the FacebookPromoter instance.

**Parameters**:
- `d` (Driver): WebDriver instance for browser automation.
- `promoter` (str): Identifier for the promoter (e.g., "aliexpress").
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): List of file paths containing group data. Defaults to reading from a default Google Drive location.
- `no_video` (bool, optional): Flag to disable video posts. Defaults to `False`.

**Raises**:
- `TypeError`: If input types are not as expected.


#### `promote`

**Description**: Promotes a category or event to a Facebook group.

**Parameters**:
- `group` (SimpleNamespace): Information about the group.
- `item` (SimpleNamespace): Information about the item (category or event) to promote.
- `is_event` (bool, optional): Boolean indicating whether the item is an event. Defaults to `False`.
- `language` (str, optional): Promotion language. Defaults to `None`.
- `currency` (str, optional): Promotion currency. Defaults to `None`.


**Returns**:
- bool: `True` if promotion was successful; `False` otherwise.


**Raises**:
- `AttributeError`: If required attributes are missing.


#### `log_promotion_error`

**Description**: Logs an error encountered during promotion.

**Parameters**:
- `is_event` (bool): Indicates whether the promoted item is an event.
- `item_name` (str): Name of the promoted item.

**Raises**:
- `TypeError`: If input types are not as expected.


#### `update_group_promotion_data`

**Description**: Updates promotion data for a Facebook group.

**Parameters**:
- `group` (SimpleNamespace): The group's data.
- `item_name` (str): Name of the promoted item.
- `is_event` (bool, optional): Whether the promoted item is an event. Defaults to `False`.


**Raises**:
- `TypeError`: If input types are not as expected.


#### `process_groups`

**Description**: Processes all groups for the current campaign or event promotion.

**Parameters**:
- `campaign_name` (str, optional): Name of the campaign to promote. Defaults to `None`.
- `events` (list[SimpleNamespace], optional): List of events to promote. Defaults to `None`.
- `is_event` (bool, optional): Boolean indicating whether to promote events. Defaults to `False`.
- `group_file_paths` (list[str], optional): List of file paths for groups to promote. Defaults to the value of the `group_file_paths` attribute.
- `group_categories_to_adv` (list[str], optional): Categories to promote. Defaults to `['sales']`.
- `language` (str, optional): Promotion language. Defaults to `None`.
- `currency` (str, optional): Promotion currency. Defaults to `None`.


**Raises**:
- `TypeError`: If input types are not as expected.



#### `get_category_item`

**Description**: Retrieves the category item for promotion based on campaign and promoter.

**Parameters**:
- `campaign_name` (str): Name of the campaign.
- `group` (SimpleNamespace): Information about the group.
- `language` (str): Language.
- `currency` (str): Currency.


**Returns**:
- SimpleNamespace: The item to promote.


**Raises**:
- `TypeError`: If input types are not as expected.



#### `check_interval`

**Description**: Checks if the promotion interval has elapsed for a given group.

**Parameters**:
- `group` (SimpleNamespace): Information about the group.


**Returns**:
- bool: `True` if the interval has passed, `False` otherwise.


**Raises**:
- `ValueError`: If the interval format is invalid.


#### `parse_interval`

**Description**: Converts a string interval to a timedelta object.

**Parameters**:
- `interval` (str): Interval string (e.g., "1H", "6M").


**Returns**:
- timedelta: The corresponding timedelta object.


**Raises**:
- `ValueError`: If the interval format is invalid.


#### `run_campaigns`

**Description**: Runs the campaign promotion cycle.

**Parameters**:
- `campaigns` (list[str]): List of campaign names.
- `group_file_paths` (list[str], optional): List of group file paths. Defaults to the value of the `group_file_paths` attribute.
- `group_categories_to_adv` (list[str], optional): Categories to promote. Defaults to `['sales']`.
- `language` (str, optional): Promotion language. Defaults to `None`.
- `currency` (str, optional): Promotion currency. Defaults to `None`.
- `no_video` (bool, optional): Flag to disable video posts. Defaults to `False`.

**Raises**:
- `TypeError`: If input types are not as expected.


#### `run_events`

**Description**: Runs the event promotion cycle.

**Parameters**:
- `events_names` (list[str]): List of event names.
- `group_file_paths` (list[str]): List of group file paths.

**Raises**:
- `TypeError`: If input types are not as expected.


#### `stop`

**Description**: Stops the promotion process by quitting the WebDriver.

**Example Usage**

```python
# Example Usage (from the code)
group_files = ["ru_usd.json", "usa.json", "ger_en_eur.json", "he_il.json", "ru_il.json"]
promoter = FacebookPromoter(d=Driver(Chrome), group_file_paths=group_files, no_video=True)
promoter.run_campaigns(campaigns=["campaign1", "campaign2"], group_file_paths=group_files)
promoter.stop()
```