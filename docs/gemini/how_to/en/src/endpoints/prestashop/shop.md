How to use the `PrestaShopShop` class in `hypotez/src/endpoints/prestashop/shop.py`

This guide explains how to utilize the `PrestaShopShop` class for interacting with PrestaShop stores.  The class is designed to simplify API interactions with the PrestaShop platform.

**1. Importing the Class**

```python
from hypotez.src.endpoints.prestashop.shop import PrestaShopShop
```

**2.  Initialization**

The `PrestaShopShop` class requires initialization with API credentials.  There are several ways to provide these:

* **Using a dictionary:**

```python
credentials = {
    'api_domain': 'your_api_domain',
    'api_key': 'your_api_key'
}
shop = PrestaShopShop(credentials=credentials)
```

* **Using a SimpleNamespace object:**

```python
from types import SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
shop = PrestaShopShop(credentials=credentials)
```

* **Providing individual parameters:**

```python
shop = PrestaShopShop(api_domain='your_api_domain', api_key='your_api_key')
```

**Crucially**:  You *must* provide both `api_domain` and `api_key`.  Failing to do so will raise a `ValueError`.  The code will attempt to use the provided dictionary/object to fill in missing values.


**3. Example Usage (Basic):**

```python
# Assuming you've initialized the 'shop' object correctly

try:
    # Example: Get store information
    store_data = shop.get_store_data()
    print(store_data)  # Output will depend on the specific PrestaShop API endpoint.
    
except PrestaShopException as e:
    logger.error(f"An error occurred: {e}")
except Exception as e:
    logger.error(f"An unexpected error occurred: {e}")
```


**Important Considerations:**

* **Error Handling:**  The example includes a `try...except` block.  This is *essential* when interacting with APIs.  PrestaShopException (and general exceptions) are caught and logged, preventing your application from crashing.
* **`PrestaShopException`:** This custom exception type (defined in `src.logger.exceptions`) is likely used for handling errors specific to the PrestaShop API.  Consult the relevant documentation to understand possible error conditions and how to appropriately handle them.
* **`credentials` Parameter Flexibility:** The `credentials` parameter allows you to pass either a dictionary or a `SimpleNamespace` object.  This provides flexibility in how you manage and store your API credentials within your application.
* **`api_domain` and `api_key`:** Always validate these credentials to ensure their correctness, especially in production environments.
* **`*args, **kwards`:** The `*args, **kwards` in the `__init__` method suggests the class might accept additional parameters for future extensibility.  Check the class documentation to see if any are currently supported and applicable to your usage.


**Before using this code:**

* **Install the required libraries:** Ensure that the necessary libraries (likely `prestashop-api`, `attr`, and others referenced in the file) are installed in your project environment.
* **API Documentation:** Refer to the official PrestaShop API documentation for detailed information on available endpoints, data structures, and error codes to accurately adapt your usage.

This comprehensive guide should help you effectively utilize the `PrestaShopShop` class within your project. Remember to replace placeholder values like `'your_api_domain'` and `'your_api_key'` with your actual credentials.