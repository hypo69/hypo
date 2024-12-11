rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code snippet demonStartes how to interact with the AliExpress IOP API to retrieve seller addresses. It creates an IOP client, defines a GET request for seller addresses, and then executes the request. Finally, it prints the response details, including the response type, code, message, request ID, and the full response body.

Execution steps
-------------------------
1. **Import the `iop` library:** The code starts by importing the necessary `iop` library, which presumably handles the IOP API communication.

2. **Initialize the IOP client:** An `IopClient` object is instantiated, providing the API gateway URL, app key, and app secret as parameters. This step establishes the connection to the API.

3. **Create an API request:** An `IopRequest` object is created, specifying the API method (`aliexpress.logistics.redefining.getlogisticsselleraddresses`) and setting the HTTP method to `POST`.  Note that the code then calls `request.set_simplify()`, which likely simplifies the response handling.

4. **Add API parameters:** The code adds a parameter (`seller_address_query`) with the value `'pickup'` to the request. This parameter likely filters the request to specific seller addresses.

5. **Execute the API request:** The `client.execute()` method is called, passing the request object and a presumably unique request identifier. This step sends the request to the API.

6. **Process the response:** The `response` object contains the API response.  The code prints the response type, code, message, request ID, and the full response body. This allows the user to inspect the outcome of the API call.  The printed information indicates whether the API call was successful or encountered an error.

7. **Handle potential errors:** The presence of checking the response type, code, and message allows for handling potential errors from the API, which is crucial for robust applications.

Usage example
-------------------------
.. code-block:: python

    import iop

    # Replace with your actual API credentials.
    client = iop.IopClient(
        'https://api-pre.aliexpress.com/sync',
        'YOUR_APP_KEY',
        'YOUR_APP_SECRET'
    )

    request = iop.IopRequest(
        'aliexpress.logistics.redefining.getlogisticsselleraddresses', 'POST'
    )
    request.set_simplify()
    request.add_api_param('seller_address_query', 'pickup')

    response = client.execute(request, "YOUR_REQUEST_ID")

    print(f"Response Type: {response.type}")
    print(f"Response Code: {response.code}")
    print(f"Response Message: {response.message}")
    print(f"Request ID: {response.request_id}")
    print(f"Full Response: {response.body}")