rst
How to use the endpoints module
=========================================================================================

Description
-------------------------
The `endpoints` module provides an API for interacting with data consumers.  Each subdirectory represents a separate module implementing the API for a specific service.  The `endpoints` module includes submodules for integrating with various consumer systems, ensuring interaction with external services.  It details the structure, installation, and usage of the endpoints module.

Execution steps
-------------------------
1. **Understanding the Module Structure:** The `endpoints` module is organized into subdirectories, each dedicated to a specific service (e.g., PrestaShop, advertisement platforms, Emil service, etc.).  These subdirectories contain the necessary classes and functions for interacting with the corresponding service's API. The provided mermaid diagram visually illustrates this structure.

2. **Identifying the Target Service:** Determine which service you need to interact with (e.g., PrestaShop, advertisement, Emil, etc.).  Refer to the section `Final Consumer Endpoints` and `Description of Modules` for details on the different services and their functionalities.

3. **Importing the Relevant Module:**  Import the necessary module from the `src.endpoints` package.  For example, to interact with the PrestaShop API, import the `PrestashopAPI` class.
   ```python
   from src.endpoints.prestashop import PrestashopAPI
   ```

4. **Instantiating the API object:** Create an instance of the relevant API class.  This might involve providing connection details, API keys, or other necessary configuration.


5. **Invoking API Methods:** Utilize the methods of the instantiated API object to perform operations (e.g., creating products, managing orders, retrieving data from the external service). The module documentation within each service-specific subdirectory (e.g., `prestashop`, `advertisement`, `emil`, etc.) should clearly define available methods and their parameters.

6. **Handling Responses:**  Process the responses returned by the API methods, which may contain data, errors, or status codes. Check for errors and handle them appropriately in your application logic.


Usage example
-------------------------
.. code-block:: python

    from src.endpoints.prestashop import PrestashopAPI

    # Replace with your PrestaShop API credentials.
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"

    try:
        prestashop_api = PrestashopAPI(api_key, api_secret)
        # Example: Retrieving a product
        product_data = prestashop_api.getProduct(product_id=123)
        print(product_data)

    except Exception as e:
        print(f"An error occurred: {e}")