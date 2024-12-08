rst
How to use this code block
=========================================================================================

Description
-------------------------
This code block sends an HTTP POST request to a specified URL with data in the request body.  It handles potential errors during the request and provides informative error messages.

Execution steps
-------------------------
1. Import the necessary libraries (e.g., `requests`).
2. Define the URL to send the POST request to.
3. Prepare the data to be sent in the request body.  This likely involves constructing a dictionary or similar data structure.
4. Construct the POST request using the `requests` library.  Specify the URL and the prepared data.  Crucially, ensure the data is properly formatted for the target API.  For example, if the API requires JSON, convert the data into JSON format.
5. Send the POST request.
6. Check the response status code. If the status code indicates success (e.g., 200), proceed.
7. If the status code indicates failure, handle the error accordingly. This might include logging the error, returning an appropriate error code or message, or reattempting the request after a delay. Extract any relevant information from the error response, like the error message from the server.
8. If successful, extract the response data.
9. Process the response data as needed.

Usage example
-------------------------
.. code-block:: python

    import requests
    import json
    import logging

    def send_post_request(url, data):
        """Sends a POST request to the given URL with the provided data."""
        try:
            headers = {'Content-type': 'application/json'}  # Crucial for JSON data
            response = requests.post(url, headers=headers, data=json.dumps(data))

            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

            # Extract and return the response data
            return response.json()


        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP request failed: {e}")
            return None  # Or raise an exception, depending on desired behavior

        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON response: {e}")
            return None

    # Example usage
    url = "https://api.example.com/endpoint"
    data = {"key1": "value1", "key2": "value2"}

    response_data = send_post_request(url, data)

    if response_data:
        print("Success!")
        print(response_data)
    else:
        print("Request failed.")