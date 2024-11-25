# send_data.js

## Overview

This JavaScript file defines a function to collect page information (title, URL, and body content) and send it to a server via a POST request. The data is formatted as JSON and sent to the specified API endpoint.

## Functions

### `onPageLoad`

**Description**: This function handles the page load event, collects information about the current page, and sends it to the server using `fetch`.


**Parameters**:

None

**Returns**:

None.  (Implied return from `fetch`.)

**Raises**:

- `Error`: If the network response is not OK (e.g., a 4xx or 5xx HTTP status code).


### `fetch`


**Description**: Sends a POST request to an external server with JSON data.


**Parameters**:


- `url` (string): The URL of the server endpoint.
- `options` (object): An object containing the request options, such as headers and body content.

**Returns**:

A Promise that resolves to the response object if the request is successful and rejects with an error if the request fails.


**Raises**:

- `Error`: If the fetch request encounters an error, for example, a network issue or invalid response.


## Example Usage

```javascript
// Example of how to use onPageLoad function
window.addEventListener('load', onPageLoad);
```

This example demonstrates adding an event listener to the `window` object that triggers the `onPageLoad` function when the page loads.  This is the recommended way to ensure the page information is sent after the page has fully loaded.


**Important Considerations**:

* **Error Handling:** The code includes robust error handling using `.catch` to manage potential network issues or server errors. This is crucial for a production-ready script.
* **API Endpoint:** The script sends data to the endpoint `http://127.0.0.1/hypotez.online/api/`.  Replace this with the correct endpoint if needed.
* **Security:**  Ensure the server API endpoint is properly secured and that sensitive data is not transmitted in the request.
* **Data Validation:** Add input validation to the server-side code to prevent potential vulnerabilities, such as injection attacks, if the server expects certain data types or formats.