# visualdg

## Overview

This module provides functionalities for handling data acquisition related to VisualDG.  It currently includes a class for data grabbing (`Graber`).


## Classes

### `Graber`

**Description**:  The `Graber` class is responsible for fetching data from VisualDG sources.

**Methods**

- `__init__(url: str, timeout=None, params: Optional[dict] = None, headers: Optional[dict] = None)`
    **Description**: Initializes the `Graber` object.
    
    **Parameters**:
        - `url` (str): The URL of the VisualDG data source.
        - `timeout` (Optional, int, float, default=None):  A timeout for the request. Set to `None` for no timeout.
        - `params` (Optional[dict], optional):  Additional parameters for the request. Defaults to `None`.
        - `headers` (Optional[dict], optional): HTTP headers for the request. Defaults to `None`.

    **Raises**:
        - `ValueError`: If the provided URL is invalid.
        - `ConnectionError`: If there is a connection error during the request.
        - `TimeoutError`: If the request times out.

- `fetch(retries=3)`
    **Description**: Fetches data from the specified URL.
    
    **Parameters**:
        - `retries` (int, optional): The number of times to retry the request if it fails. Defaults to 3.
    
    **Returns**:
        - `dict | None`: Returns the fetched data as a dictionary if successful. Returns `None` if the request fails after all retries.
    
    **Raises**:
        - `ConnectionError`: If a connection error occurs.
        - `TimeoutError`: If a request times out.
        - `RequestException`: If a general request error occurs (e.g., HTTP error).



## Variables

### `MODE`

**Description**: Defines the operational mode of the module.

**Value**: 'dev'