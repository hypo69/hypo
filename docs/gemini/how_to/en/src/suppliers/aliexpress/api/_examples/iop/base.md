```python
"""
Usage Guide for hypotez/src/suppliers/aliexpress/api/_examples/iop/base.py

This file provides a Python SDK for interacting with an API (likely AliExpress).
It handles API requests, signatures, logging, and response parsing.

Key Concepts:

- `IopRequest`: Represents an API request, containing parameters and optional files.
- `IopResponse`: Represents an API response, containing status code, message, and the parsed JSON response body.
- `IopClient`: The main client class for executing API requests.


How to use:

1. **Initialization:**
   - Instantiate the `IopClient` class, providing the API server URL, your app key, app secret, and optional timeout (in seconds).

   ```python
   client = IopClient("your_api_server_url", "your_app_key", "your_app_secret")
   ```

2. **Preparing the Request:**
   - Create an `IopRequest` object.
   - Add API parameters using `add_api_param()`.
   - Add files for uploads using `add_file_param()`.
   - Optionally set `simplify` or specify the response format using `set_simplify()` or `set_format()`.


   ```python
   request = IopRequest("your_api_endpoint")
   request.add_api_param("param1", "value1")
   request.add_api_param("param2", 123)
   # Upload file (replace 'your_file.txt' with actual path)
   request.add_file_param("file", open("your_file.txt", "rb"))
   request.set_format("xml") # Example using XML instead of JSON
   ```

3. **Executing the Request (with optional access token):**
   - Use the `execute()` method of the `IopClient` to send the request.  Pass the `request` object and an optional `access_token` if required.


   ```python
   try:
       response = client.execute(request, access_token="your_access_token")
   except Exception as e:
       print(f"Error executing request: {e}")
       # Handle the exception appropriately (e.g., retry, log)

   ```

4. **Processing the Response:**
   - Check the response status (`response.code`) for success (e.g., "0").
   - Access the response body (`response.body`) for the parsed JSON data.
   - Extract the necessary data from the JSON object.
   - Handle potential errors (`response.message`) and log them using the provided `logApiError()` function for debugging.

   ```python
   if response.code == "0":
       # Access the response body (JSON object).  Example:
       product_details = response.body.get("product_details")
       print(product_details)
   else:
       print(f"API error: {response.message}")
   ```

**Important Considerations:**

- **Error Handling:** The code includes robust error handling (try-except block) to catch potential `requests` library errors and log them using `logApiError()`.
- **Logging:**  Logging is configured to write error messages to a log file (`iopsdk.log`). The log messages contain crucial information for debugging.  Change the log level in `IopClient` to adjust the logging.
- **Authentication:** The code assumes that authentication (`app_key`, `app_secret`) and potentially `access_token` are properly managed.
- **File Uploads:** The `add_file_param()` method allows for file uploads. Make sure to handle file paths correctly.
- **Security:**  Always handle sensitive information (like app secrets) securely.

**Example using get method:**
If your API call uses GET, use `request._http_method = 'GET'` and pass only parameters in the request, avoiding files.

```python
    request = IopRequest("your_api_endpoint", http_method='GET')
```
This guide provides a starting point. Adapt and customize it to match your specific needs and the structure of the AliExpress API.  Carefully review the API documentation for required parameters, data structures, and error codes.
```
```