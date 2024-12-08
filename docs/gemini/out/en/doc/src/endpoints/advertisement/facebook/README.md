# Facebook Advertisement Endpoints

## Overview

This module provides endpoints for interacting with Facebook advertisements.  It handles tasks such as creating, updating, and retrieving advertisement data.


## Classes

### `FacebookAdvertisementClient`

**Description**: This class provides methods for interacting with Facebook advertisement endpoints.

**Methods**:

- `create_ad(ad_data: dict) -> dict | None`: Creates a new advertisement.
  **Description**: This method takes advertisement data in a dictionary format and attempts to create a new advertisement.

  **Parameters**:
  - `ad_data` (dict): A dictionary containing the advertisement data.  This dictionary must follow the Facebook API specifications.

  **Returns**:
  - `dict | None`:  A dictionary containing the created advertisement details, or `None` if an error occurred.

  **Raises**:
  - `FacebookAPIError`: If there is an error in the Facebook API response.
  - `ValueError`: If `ad_data` is not a valid dictionary.

- `update_ad(ad_id: str, update_data: dict) -> dict | None`: Updates an existing advertisement.
  **Description**: Updates an existing advertisement.

  **Parameters**:
  - `ad_id` (str): The ID of the advertisement to update.
  - `update_data` (dict): A dictionary containing the updates to be applied to the advertisement. This dictionary must follow the Facebook API specifications.

  **Returns**:
  - `dict | None`: A dictionary containing the updated advertisement details, or `None` if an error occurred.

  **Raises**:
  - `FacebookAPIError`: If there is an error in the Facebook API response.
  - `ValueError`: If `update_data` is not a valid dictionary or `ad_id` is not a valid string.
  - `NotFoundError`: If the advertisement with the given `ad_id` does not exist.

- `get_ad(ad_id: str) -> dict | None`: Retrieves an advertisement by ID.
  **Description**: Retrieves an advertisement by its ID.

  **Parameters**:
  - `ad_id` (str): The ID of the advertisement to retrieve.

  **Returns**:
  - `dict | None`: A dictionary containing the advertisement details, or `None` if an error occurred or the advertisement is not found.

  **Raises**:
  - `FacebookAPIError`: If there is an error in the Facebook API response.
  - `NotFoundError`: If the advertisement with the given `ad_id` does not exist.


## Functions

This module does not contain any functions.


## Exceptions

### `FacebookAPIError`

**Description**: This exception is raised for errors related to Facebook API communication.


### `NotFoundError`

**Description**: Raised when a resource (e.g., an advertisement) is not found.


### `ValueError`

**Description**: Raised when invalid input data is provided.