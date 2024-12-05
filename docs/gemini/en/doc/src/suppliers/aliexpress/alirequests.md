# aliexpress/alirequests.py

## Overview

This module provides a class `AliRequests` for handling requests to AliExpress. It utilizes the `requests` library and handles cookies for session management, loading cookies from webdriver files, and making GET requests.


## Table of Contents

* [Classes](#classes)
    * [AliRequests](#alirequests)
* [Functions](#functions)
    * [make_get_request](#make_get_request)
    * [short_affiliate_link](#short_affiliate_link)


## Classes

### `AliRequests`

**Description**: This class handles requests to AliExpress, managing cookies and session data.

**Methods**:

#### `__init__`

**Description**: Initializes the `AliRequests` class.

**Parameters**:
- `webdriver_for_cookies` (str, optional): The name of the webdriver for loading cookies. Defaults to 'chrome'.

#### `_load_webdriver_cookies_file`

**Description**: Loads cookies from a webdriver file.

**Parameters**:
- `webdriver_for_cookies` (str, optional): The name of the webdriver. Defaults to 'chrome'.

**Returns**:
- bool: True if cookies loaded successfully, False otherwise.

**Raises**:
- `FileNotFoundError`: If the cookie file does not exist.
- `ValueError`: If there's an issue parsing the cookie data.
- `Exception`: Any other exception during cookie loading.


#### `_refresh_session_cookies`

**Description**: Refreshes session cookies.

**Raises**:
- `requests.RequestException`: If there's an error during the refresh request.
- `Exception`: Any other exception during the refresh process.

#### `_handle_session_id`

**Description**: Handles the JSESSIONID in response cookies.

**Parameters**:
- `response_cookies`: The cookies from the response.

**Raises**:
- `Exception`: Any exception during handling the session ID.


## Functions

### `make_get_request`

**Description**: Makes a GET request with cookies.

**Parameters**:
- `url` (str): The URL to make the GET request to.
- `cookies` (List[dict], optional): List of cookies to use for the request. Defaults to None.
- `headers` (dict, optional): Optional headers to include in the request. Defaults to None.

**Returns**:
- requests.Response: The response object if successful.
- False: If the request fails.

**Raises**:
- `requests.RequestException`: If there's an error during the request.
- `Exception`: Any other exception during the request process.


### `short_affiliate_link`

**Description**: Get a short affiliate link.

**Parameters**:
- `link_url` (str): The URL to shorten.

**Returns**:
- requests.Response: The response object if successful.
- False: If the request fails.

**Raises**:
- `requests.RequestException`: If there's an error during the request.
- `Exception`: Any other exception during the request process.