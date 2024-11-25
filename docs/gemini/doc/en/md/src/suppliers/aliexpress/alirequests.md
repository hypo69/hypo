# alirequests.py

## Overview

This module provides the `AliRequests` class for handling requests to AliExpress. It uses the `requests` library and manages cookies for authentication and session persistence.  The class handles loading cookies from webdriver files, updating session cookies, and making GET requests with cookies, which are crucial for interacting with the AliExpress platform reliably.


## Table of Contents

* [AliRequests](#aliexpress-class)
    * [_load_webdriver_cookies_file](#_load-webdriver-cookies-file)
    * [_refresh_session_cookies](#_refresh-session-cookies)
    * [_handle_session_id](#_handle-session-id)
    * [make_get_request](#make-get-request)
    * [short_affiliate_link](#short-affiliate-link)


## Classes

### `AliRequests`

**Description**: This class handles requests to AliExpress, managing cookies and sessions for reliable interaction.

**Methods**:

#### `__init__`

**Description**: Initializes the `AliRequests` class.

**Parameters**:

- `webdriver_for_cookies` (str, optional): The name of the webdriver to load cookies from. Defaults to "chrome".

**Raises**:
-  No explicit exceptions are raised.


#### `_load_webdriver_cookies_file`

**Description**: Loads cookies from a webdriver cookie file.

**Parameters**:

- `webdriver_for_cookies` (str, optional): The name of the webdriver. Defaults to "chrome".

**Returns**:

- bool: `True` if cookies loaded successfully, `False` otherwise.

**Raises**:

- `FileNotFoundError`: If the cookie file is not found.
- `ValueError`: If there's an issue parsing the cookie data.
- `Exception`: For any other error during cookie loading.


#### `_refresh_session_cookies`

**Description**: Refreshes session cookies by making a request to a specific URL.

**Raises**:

- `requests.RequestException`: If there's an error during the request.
- `Exception`: For any other error during the refresh process.

#### `_handle_session_id`

**Description**: Handles the JSESSIONID in the response cookies.  This is important for maintaining the session.

**Parameters**:
- `response_cookies`:  A cookie jar object from the response.


**Raises**:
- No explicit exceptions are raised, but logs warnings and errors.


#### `make_get_request`

**Description**: Makes a GET request to a given URL with optional cookies and headers.

**Parameters**:

- `url` (str): The URL to make the GET request to.
- `cookies` (List[dict], optional): A list of cookies to include in the request. Defaults to using the saved cookies.
- `headers` (dict, optional): Optional headers to use for the request. Defaults to the class's default headers.

**Returns**:

- `requests.Response`: The response object if successful.
- `False`: If the request fails.

**Raises**:

- `requests.RequestException`: If there's an error during the request.
- `Exception`: For any other error during the request process.


#### `short_affiliate_link`

**Description**: Shortens an affiliate link by making a request to a specific URL.

**Parameters**:

- `link_url` (str): The URL to shorten.

**Returns**:

- `requests.Response`: The response object if successful.
- `False`: If the request fails.


**Raises**:

- `requests.RequestException`: If there's an error during the request.
- `Exception`: For any other error during the request process.