# Facebook Advertisement Endpoints

## Overview

This module contains endpoints for interacting with Facebook advertisement services.  It provides functions for various advertisement management tasks.


## Table of Contents

* [Overview](#overview)
* [Functions](#functions)


## Functions

### `create_ad_campaign`

**Description**: Creates a new Facebook ad campaign.

**Parameters**:
- `campaign_data` (dict): A dictionary containing the campaign data, including name, budget, targeting, and other relevant details.  This dictionary should conform to the Facebook API specifications.

**Returns**:
- `dict | None`: Returns a dictionary containing the created campaign's details, or `None` if the operation fails.


**Raises**:
- `FacebookAPIError`: Raised if there's an issue interacting with the Facebook API, such as an invalid API key, authentication problems, or network connectivity issues.
- `ValueError`: Raised if the `campaign_data` is invalid or incomplete. For example, if a required field is missing or the data format is incorrect.


### `update_ad_campaign`

**Description**: Updates an existing Facebook ad campaign.


**Parameters**:
- `campaign_id` (str): The ID of the campaign to update.
- `update_data` (dict): A dictionary containing the fields to update, including the new values.  This dictionary should conform to the Facebook API specifications, and should only contain the fields intended to be changed.


**Returns**:
- `dict | None`: Returns a dictionary containing the updated campaign's details, or `None` if the operation fails.


**Raises**:
- `FacebookAPIError`: Raised if there's an issue interacting with the Facebook API.
- `ValueError`: Raised if the `campaign_id` is invalid or the `update_data` is invalid or incomplete.


### `get_ad_campaign`

**Description**: Retrieves details for a specific Facebook ad campaign.

**Parameters**:
- `campaign_id` (str): The ID of the campaign to retrieve.

**Returns**:
- `dict | None`: Returns a dictionary containing the campaign's details, or `None` if the operation fails.


**Raises**:
- `FacebookAPIError`: Raised if there's an issue interacting with the Facebook API.
- `ValueError`: Raised if the `campaign_id` is invalid.