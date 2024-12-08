rst
How to Use the Data Consumer Endpoints Module
=========================================================================================

Description
-------------------------
This module provides APIs for interacting with various data consumers.  Each subdirectory (e.g., `prestashop`, `advertisement`) represents a separate API for a specific service.  This allows seamless integration with external systems.  The module includes endpoints for PrestaShop, advertisement platforms (like Facebook), Emil service, the Hypo69 platform, and Kazarinov service, as well as client frameworks.


Execution steps
-------------------------
1. **Install dependencies:** Ensure all required packages are installed.  Run the following command in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

2. **Import the desired module:**  Import the appropriate endpoint module into your Python script.  For example, to use the PrestaShop API:

   ```python
   from src.endpoints.prestashop import PrestashopAPI
   ```

3. **Instantiate the API object:** Create an instance of the specific API class (e.g., `PrestashopAPI`). This typically involves configuring connection details, such as API keys or URLs.

4. **Make API calls:**  Use the methods provided by the API object to interact with the respective external service.  Refer to the specific module documentation (e.g., `prestashop.py`) for available methods and parameters. For example, to create a product in PrestaShop:


   ```python
   # Assuming you've instantiated the PrestashopAPI object as 'prestashop_api'
   product_data = {
       "name": "New Product",
       "description": "Product description",
       "price": 10.99
   }
   try:
       response = prestashop_api.create_product(product_data)
       # Process the response (e.g., check for success)
   except Exception as e:
       print(f"Error creating product: {e}")
   ```

5. **Handle responses:** Process the responses returned by the API calls to ensure successful interaction and to handle potential errors.

Usage example
-------------------------
```python
from src.endpoints.prestashop import PrestashopAPI

# Replace with your actual PrestaShop API credentials
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
API_URL = "YOUR_API_URL"

try:
    prestashop_api = PrestashopAPI(api_key=API_KEY, api_secret=API_SECRET, api_url=API_URL)
    product_data = {
        "name": "Example Product",
        "description": "Example product description",
        "price": 19.99
    }
    response = prestashop_api.create_product(product_data)

    if response.status_code == 200:
        print("Product created successfully!")
        print(response.json())  # Print the response data
    else:
        print(f"Error creating product: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
```
```
```
```python