# send_data.js

## Overview

This JavaScript file defines a function `onPageLoad` to collect page information (title, URL, body content) and send it to a server at `http://127.0.0.1/hypotez.online/api/` via a POST request.  It uses the `fetch` API for making the request, handling potential errors, and parsing the JSON response.


## Functions

### `onPageLoad`

**Description**: This function collects page information and sends it to the specified server endpoint.

**Parameters**:  None (implicitly receives information from the page's environment).

**Returns**: None.  The function is asynchronous and doesn't directly return a value.  Results are handled through `.then` and `.catch` calls.

**Raises**:
- `Error`: Thrown if the network request is not successful (non-2xx HTTP status code).  Detailed error information is included in the `error` object.