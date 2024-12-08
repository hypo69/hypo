rst
How to use this code block
=========================================================================================

Description
-------------------------
This code block describes the process of handling a request to process a list of products using an AI model.  It outlines the interactions between a user, an AI model, and a logger.  The process involves handling potential errors in the response from the AI model, invalid data formats, and extracting relevant data (`ru` and `he` values) from the response.


Execution steps
-------------------------
1. **User initiates the request**: The user sends a request (`products_list`) to the AI model for processing.

2. **AI model processes the request**: The AI model processes the request using its internal logic and command.

3. **Model returns a response**: The AI model returns a response to the user.

4. **Error handling (no response):** If no response is received from the model, an error is logged ("no response from gemini"), and a retry is performed (reducing the `attempts` count).

5. **Error handling (invalid data):** If the received data is invalid, an error is logged ("Error in data from gemini"), and a retry is performed.

6. **Valid response received:** If the response is valid:
    - **List data format:** If the response is a list:
        - **Two elements:**  If the list has two elements (presumably `ru` and `he` values), they are extracted.
        - **One element:** If the list has one element, the `ru` and `he` values are extracted from that element.
        - **Invalid structure:** If the structure is not parsable, an error ("Проблема парсинга ответа") is logged, and the request is retried.
    - **Object data format:** If the response is an object, the `ru` and `he` values are extracted from the object.
    - **Invalid `ru` or `he` values:** If either `ru` or `he` values are invalid, an error is logged ("Invalid ru or he data") and the request is retried.

7. **Data extraction and return:** The `ru` and `he` values are returned as the result of the process.


Usage example
-------------------------
.. code-block:: python

    # (Illustrative example; replace with actual API calls and data handling)
    products_list = ["product1", "product2"]

    try:
        response = process_products(products_list)  # Replace with your AI model processing function

        if response:
            if isinstance(response, list):
                if len(response) == 2:
                    ru_data = response[0]
                    he_data = response[1]
                elif len(response) == 1:
                    ru_data = response[0].get("ru")
                    he_data = response[0].get("he")
                else:
                    raise ValueError("Invalid list format")
            elif isinstance(response, dict):
                ru_data = response.get("ru")
                he_data = response.get("he")
            else:
                raise TypeError("Invalid response format")

            # Use ru_data and he_data
            print(f"ru data: {ru_data}")
            print(f"he data: {he_data}")
        else:
            print("No response from the AI model.")


    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")