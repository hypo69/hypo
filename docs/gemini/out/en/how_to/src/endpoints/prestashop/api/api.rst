rst
How to use the PrestaShop API class
========================================================================================

Description
-------------------------
This Python code defines a `PrestaShop` class for interacting with a PrestaShop web service API.  It handles various operations like creating, reading, updating, deleting (CRUD), searching, and uploading images using JSON or XML data formats.  The class provides error handling and methods to process responses from the API.

Execution steps
-------------------------
1. **Initialization:**
   - Instantiate the `PrestaShop` class, providing the API domain, API key, default language, debug mode, and desired data format.
   - Example:
     ```python
     api = PrestaShop(
         API_DOMAIN="https://myPrestaShop.com/api/",
         API_KEY="YOUR_API_KEY",
         default_lang=1,
         debug=True,
         data_format='JSON',
     )
     ```
2. **Authentication (Implicit):**
   - The `__init__` method implicitly establishes authentication using the provided API key.
3. **API Interaction:**
   - Use various methods provided by the class (e.g., `create`, `read`, `write`, `unlink`, `search`, `create_binary`, `upload_image`) to perform operations on PrestaShop resources. These methods accept parameters for resource, resource ID, data, filters, etc.
   - The `ping` method checks the API connection.
   - Each operation is enclosed within a `try-except` block to manage potential `PrestaShopException` or `PrestaShopAuthenticationError`.
4. **Response Handling:**
   - The class handles the response from the API based on the `status_code`.
   - If the status code is 200 or 201, the response data is parsed and returned.
   - Otherwise, an error is logged using the `logger` module, and `False` is returned to signal the failure.
5. **Error Parsing (XML):**
   - For XML responses, the class parses error messages from the XML structure. Error code and message are logged for debugging.
6. **Image Upload:**
   - Use `create_binary` or `upload_image` to upload binary data (images) to the PrestaShop API.  These methods handle downloading images from URLs, saving them temporarily, and then uploading them to the API.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.api import PrestaShop

    # Replace with your PrestaShop API details
    api = PrestaShop(
        API_DOMAIN="https://your-prestashop-domain.com/api/",
        API_KEY="YOUR_API_KEY",
        data_format='JSON'
    )

    # Example: Creating a tax record
    tax_data = {
        'tax': {
            'rate': 3.00,
            'active': '1',
            'name': {
                'language': {
                    'attrs': {'id': '1'},
                    'value': '3% tax'
                }
            }
        }
    }

    try:
        new_tax = api.create('taxes', tax_data)
        print(f"Tax created successfully: {new_tax}")
    except Exception as e:
        print(f"Error creating tax: {e}")

    # Example: Getting product images
    try:
        product_images = api.get_product_images(123) # Replace 123 with the product ID
        if product_images:
            print(f"Product images: {product_images}")
        else:
            print("Error getting product images.")
    except Exception as e:
        print(f"Error getting product images: {e}")