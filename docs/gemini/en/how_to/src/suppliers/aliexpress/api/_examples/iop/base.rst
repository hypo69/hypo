rst
How to use the IopClient class for interacting with an API
===================================================================================================

Description
-------------------------
This code defines classes for making API requests to an unspecified platform (likely a custom API).  `IopClient` is the core class responsible for handling the API communication, including signing requests, handling errors, and parsing responses. It relies on `IopRequest` for constructing the request parameters and `IopResponse` for storing and returning the response.  Crucially, it logs errors to a file, `iopsdk.log`.

Execution steps
-------------------------
1. **Initialization:** Create an instance of `IopClient`.
   - Provide the API endpoint (`server_url`), application key (`app_key`), and secret (`app_secret`).
   - Optionally, set a timeout for requests (`timeout`).


2. **Request Construction:** Create an instance of `IopRequest` to specify the API endpoint (`api_pame`), HTTP method (default `POST`),  additional parameters (`add_api_param`), and potentially file parameters (`add_file_param`).  Configure `simplify` and `format` as needed.

3. **Parameter Addition:** Add parameters to the `IopRequest` object using `add_api_param`.

4. **Sign the Request:**
   - Generate a timestamp.
   - Construct a dictionary (`sys_parameters`) containing essential parameters like the app key, timestamp, sign method, partner ID (SDK version), the API method (`request._api_pame`) the format and simplify.
   - Add any additional parameters from the `IopRequest` (`application_parameter`).
   - Compute the signature (`sign`) using the app secret and the combined parameters. Include the API endpoint in the signature calculation if it contains `/`.

5. **Form the URL:** Construct the full API request URL using the combined parameters.

6. **Execute the Request:** Use `IopClient.execute()` to send the request.
   - Pass the `IopRequest` object and, optionally, an access token (`access_token`).
   - The function constructs the request URL, sends the request (`requests.post` or `requests.get` based on the `http_method`), and handles potential exceptions during the request.

7. **Handle the Response:**
   - Parse the JSON response received from the API.
   - Check the response code. If it's not successful (e.g., "0"), log the error using `logApiError`.
   - Populate the `IopResponse` object with the response data.  Store the `json` response as the `body`.

8. **Return the Response:** Return the populated `IopResponse` object containing the response code, message, request ID, and response body.

Usage example
-------------------------
.. code-block:: python

    import time
    from hypotez.src.suppliers.aliexpress.api._examples.iop.base import IopClient, IopRequest, IopResponse

    # Replace with your actual values
    server_url = "your_api_endpoint"
    app_key = "your_app_key"
    app_secret = "your_app_secret"

    # Create an IopClient instance
    client = IopClient(server_url, app_key, app_secret)

    # Create an IopRequest object for a POST request
    request = IopRequest("your_api_endpoint_path", http_method="POST")  # Replace with the actual API path

    # Add parameters
    request.add_api_param("param1", "value1")
    request.add_api_param("param2", 123)


    # Execute the request
    response = client.execute(request)

    # Print the response
    print(response)
    print(response.body)