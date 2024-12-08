rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code snippet demonstrates how to interact with an API using the `iop` library.  It constructs an API request to retrieve product details from an AliExpress-like platform, handling potential errors and printing various aspects of the response.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports the `iop` and `time` libraries. `iop` is likely a custom library for interacting with APIs. `time` is used for timestamp generation.

2. **Initialize the API client:** It creates an instance of the `IopClient` class, providing the API gateway URL, app key, and app secret.  This establishes the connection to the target API.

3. **Create an API request:** An `IopRequest` object is instantiated. It specifies the API endpoint (`/product/item/get`) and the HTTP method (in this case, `GET`), allowing control over the request type.

4. **Add API parameters:** The code adds parameters to the request, including the product `itemId` and `authDO` (likely an authentication object).  These parameters are essential for the API call to function correctly.

5. **Execute the API request:** The `client.execute(request)` method sends the constructed request to the API. The result is stored in the `response` object.

6. **Process the response:** The code checks the `response` object for various attributes:
    - `response.type`: Indicates the type of error (if any) -  `nil` for success, or other error types like `ISP`, `ISV`, or `SYSTEM`.
    - `response.code`: An integer code indicating success or failure (0 usually signifies success).
    - `response.message`: A descriptive error message (if an error occurred).
    - `response.request_id`: A unique ID associated with the API request.
    - `response.body`: The actual response data returned by the API.

7. **Print information:** The code prints the response type, code, message, request ID, and the entire response body to the console.
8. **Generate and print timestamp:** The code generates and prints a timestamp for record-keeping.


Usage example
-------------------------
.. code-block:: python

    import iop
    import time

    # Replace with your API credentials and endpoint
    client = iop.IopClient('https://api-pre.taobao.tw/rest', '100240', 'hLeciS15d7UsmXKoND76sBVPpkzepxex')
    request = iop.IopRequest('/product/item/get', 'GET')
    request.add_api_param('itemId', '123456789')  # Replace with the desired item ID
    request.add_api_param('authDO', '{"sellerId":2000000016002}')

    try:
        response = client.execute(request)
        print(response.type)
        print(response.code)
        print(response.message)
        print(response.request_id)
        print(response.body)
        print(str(round(time.time())) + '000')
    except Exception as e:
        print(f"An error occurred: {e}")