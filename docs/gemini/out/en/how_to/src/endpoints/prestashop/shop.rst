rst
How to use the PrestaShopShop class
========================================================================================

Description
-------------------------
This code defines a `PrestaShopShop` class, inheriting from the `PrestaShop` class.  This class handles interactions with a PrestaShop store's API.  Critically, it validates that both an `api_domain` and an `api_key` are provided, raising a `ValueError` if either is missing.  This ensures the necessary credentials are available for API calls.

Execution steps
-------------------------
1. **Import necessary modules**: The code imports various modules required for its functionality, including `SimpleNamespace`, `Optional`, `PrestaShop`, custom modules like `logger`, `jjson`, and `gs`, as well as modules for system interaction (`sys`, `os`) and creating attributes (`attr`). This step ensures all the necessary components are available.
2. **Define the `PrestaShopShop` class**: This class is designed to interact with the PrestaShop API.
3. **Initialize the `PrestaShopShop` object**: The `__init__` method of the `PrestaShopShop` class takes optional arguments for `credentials`, `api_domain`, and `api_key`. It handles the scenario where `credentials` is provided as a dictionary or `SimpleNamespace` object, extracting the `api_domain` and `api_key` values accordingly.
4. **Validate credentials**: The code verifies that both `api_domain` and `api_key` are provided. If either is missing, it raises a `ValueError` to indicate an insufficient configuration.
5. **Call parent class's `__init__` method**: The code then calls the `__init__` method of the parent `PrestaShop` class, providing the validated `api_domain` and `api_key`. This step completes the initialization of the API interaction tools.

Usage example
-------------------------
.. code-block:: python

    from types import SimpleNamespace
    from hypotez.src.endpoints.prestashop.shop import PrestaShopShop
    from pathlib import Path

    # Example credentials (replace with your actual values)
    credentials = SimpleNamespace(api_domain="your-api-domain.com", api_key="your-api-key")

    try:
        shop_api = PrestaShopShop(credentials=credentials)
        # Now you can use shop_api to make calls to the PrestaShop API.
        # Example:
        # response = shop_api.get_products()
        # print(response)


    except ValueError as e:
        print(f"Error: {e}")