## Usage Guide for `hypotez/src/endpoints/prestashop/supplier.py`

This guide explains how to use the `PrestaSupplier` class for interacting with PrestaShop suppliers via its API.


**1. Class Overview:**

The `PrestaSupplier` class inherits from the `PrestaShop` class, providing methods for common PrestaShop API interactions.  It's specifically designed for handling supplier-related operations.


**2. Initialization (`__init__`)**

The `__init__` method is crucial for setting up the connection to the PrestaShop API.

```python
class PrestaSupplier(PrestaShop):
    # ... (other code)

    def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwards):
        """... (docstring)"""
        if credentials is not None:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)

        if not api_domain or not api_key:
            raise ValueError('Both api_domain and api_key are required.')

        super().__init__(api_domain, api_key, *args, **kwards)
```

* **`credentials` (Optional[dict | SimpleNamespace])**:  Allows you to pass credentials in either a dictionary or a `SimpleNamespace` object.  The `api_domain` and `api_key` will be extracted from this. If not provided, the `api_domain` and `api_key` parameters must be provided directly.

* **`api_domain` (Optional[str])**: The domain of the PrestaShop API. **Required.**

* **`api_key` (Optional[str])**: Your API key for authentication. **Required.**

* **`*args, **kwards`**:  Allow for passing additional arguments to the parent class's `__init__` (useful if you have further configuration for the API connection).

**Crucial Error Handling:** The code includes validation to ensure both `api_domain` and `api_key` are provided.  This prevents common errors.


**3. Example Usage:**

```python
from hypotez.src.endpoints.prestashop.supplier import PrestaSupplier
import json  # Or import a suitable JSON library

# 1. Create credentials (example)
credentials = {
    'api_domain': 'your-api-domain',
    'api_key': 'your-api-key'
}


try:
    supplier = PrestaSupplier(credentials=credentials)
    # 2. Now you can use the methods from PrestaShop, like:
    response = supplier.get_suppliers() # Example call to a method
    
    if response.ok:
      suppliers_data = response.json() # Assuming the response returns JSON data
      print(json.dumps(suppliers_data, indent=2))
    else:
      print(f"Request failed with status code: {response.status_code}")
      print(response.text) # Important for debugging

except ValueError as e:
    print(f"Error: {e}")

```


**Important Considerations:**

* **Error Handling:** The example includes a `try...except` block to catch `ValueError` which is raised if the necessary credentials are missing. This is a crucial best practice for production code.
* **Response Handling:**  The example shows how to check the HTTP status code (`response.ok`) and handle potential errors from the API. Accessing the JSON response (`response.json()`) ensures proper data processing.
* **Dependencies:** Ensure you have the required packages (`header`, `gs`, `logger`, `utils` from `src` and `PrestaShop` from `./api`) installed.
* **Replace Placeholders:** Replace `"your-api-domain"` and `"your-api-key"` with your actual PrestaShop API credentials.



This comprehensive guide provides a structured approach to using the `PrestaSupplier` class, making your PrestaShop API interaction more robust and easier to manage. Remember to consult the documentation of the underlying `PrestaShop` class for further details on its available methods.