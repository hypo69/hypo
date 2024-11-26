## Usage Guide for hypotez/src/endpoints/prestashop/api/api.py

This guide explains how to use the `PrestaShop` class to interact with the PrestaShop API.  The class allows for various operations, including creating, reading, updating, deleting resources (CRUD), searching, and uploading images.

**1. Installation (Assuming you have `requests` and other required packages):**

Make sure you have the required Python packages installed.  If not, install them using pip:

```bash
pip install requests
# ... other necessary packages...
```

**2. Initialization**

```python
from hypotez.src.endpoints.prestashop.api.api import PrestaShop, Format

api = PrestaShop(
    API_DOMAIN="https://your-prestashop-domain.com/api/",  # Replace with your PrestaShop domain
    API_KEY="YOUR_API_KEY",  # Replace with your PrestaShop API Key
    default_lang=1,  # Optional: Default language ID.
    debug=True, #Optional: Enable debug mode (important for troubleshooting!)
    data_format='JSON' # Optional: default format, JSON is recommended
)
```

**Crucial:** Replace `"https://your-prestashop-domain.com/api/"` and `"YOUR_API_KEY"` with your actual PrestaShop credentials.  These are obtained from your PrestaShop settings.

**3. Basic Interactions (CRUD):**

```python
# Ping to check connection
if api.ping():
    print("Successfully connected to PrestaShop API")
else:
    print("Failed to connect. Check API credentials.")


# Example: Create a tax record
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

created_tax = api.create('taxes', tax_data)
print("Created tax record:", created_tax)

# Example: Update a tax record (using the ID from the creation response)
updated_tax_data = {
    'tax': {
        'id': str(created_tax['tax']['id']), # Crucial: use the ID from the response
        'rate': 3.50,
        'active': '1',
        'name': {
            'language': {
                'attrs': {'id': '1'},
                'value': '3.5% tax'
            }
        }
    }
}

updated_tax = api.write('taxes', updated_tax_data)
print("Updated tax record:", updated_tax)

# Example: Delete a tax record
api.unlink('taxes', str(created_tax['tax']['id']))

# ... similar examples for `read`, `unlink`
```

**4. Search:**

```python
# Search for taxes containing "tax"
search_results = api.search('taxes', filter='[name]=%tax%')
for result in search_results:
  print(result)
```

**5. Uploading Images:**

```python
# Replace with the actual URL of your image
image_url = "https://example.com/image.jpg"
product_id = 123  # Replace with the product ID

uploaded_image = api.upload_image('images/products/' + str(product_id), product_id, image_url)
print("Image uploaded:", uploaded_image)

# Alternative for asynchronous upload
uploaded_image_async = api.upload_image_async('images/products/' + str(product_id), product_id, image_url)

```

**Important Considerations:**

* **Error Handling:** The `PrestaShop` class includes error handling (`_check_response`, `_parse_response_error`).  Pay close attention to the error messages and debug output (especially if `debug=True`) to diagnose issues.
* **Data Format:** The code defaults to JSON.  Use `data_format='XML'` in the `PrestaShop` constructor if needed.
* **File Paths:** Ensure you have the correct paths to files you're uploading.
* **Resource IDs:** Always use the correct resource IDs when updating or deleting resources.
* **Response Parsing:** The `_parse` method is crucial for handling XML responses.
* **`_exec` Method Parameters:** Thoroughly understand and utilize the numerous parameters available in the `_exec` method (e.g., `resource_id`, `data`, `headers`, `filter`, `sort`, `limit`).
* **Security:** Never hardcode your API key in your scripts. Use environment variables or secure configuration methods.


This guide provides a basic overview. Refer to the docstrings within the `api.py` file for detailed explanations of each method's parameters and potential exceptions.  The example usage code snippets should give you a solid starting point. Remember to replace placeholders with your specific values.