## Usage Guide for `hypotez/src/suppliers/aliexpress/api/api.py`

This guide describes how to use the `AliexpressApi` class to interact with the AliExpress Open Platform API.  It focuses on retrieving product details, affiliate links, and categories.

**Prerequisites:**

* **Python Installation:** Ensure Python is installed on your system.
* **API Credentials:** Obtain an API key and secret from the AliExpress Open Platform.
* **Dependencies:** Install the required libraries:
  ```bash
  pip install <package_names_from_the_file>
  ```

**1. Importing the `AliexpressApi` Class:**

```python
from hypotez.src.suppliers.aliexpress.api.api import AliexpressApi
from hypotez.src.suppliers.aliexpress.api.models import model_Language, model_Currency, model_LinkType, model_ProductType, model_SortBy  # Replace with your actual import
```

**2. Creating an `AliexpressApi` Instance:**

```python
# Replace with your actual credentials
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
language = model_Language.EN # or model_Language.ZH, etc.
currency = model_Currency.USD  # or model_Currency.EUR, etc.
tracking_id = "YOUR_TRACKING_ID" # Optional


aliexpress_api = AliexpressApi(
    key=api_key,
    secret=api_secret,
    language=language,
    currency=currency,
    tracking_id=tracking_id,
)
```

**3. Retrieving Product Details:**

```python
product_ids = ["PRODUCT_ID_1", "PRODUCT_ID_2"]  # or a string "PRODUCT_ID_1, PRODUCT_ID_2"
fields = ["title", "price"]  # optional, specify fields to retrieve. Defaults to all fields.
country = "US"  # Optional filter, specify a country.

try:
    products = aliexpress_api.retrieve_product_details(product_ids, fields, country)
    for product in products:
        pprint(product)  # Use utils.pprint for pretty printing
except ProductsNotFoudException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

**4. Generating Affiliate Links:**

```python
links = ["PRODUCT_URL_1", "PRODUCT_URL_2"] # or a string "PRODUCT_URL_1, PRODUCT_URL_2"
link_type = model_LinkType.HOTLINK  # Optional, defaults to model_LinkType.NORMAL

try:
    affiliate_links = aliexpress_api.get_affiliate_links(links, link_type)
    for link in affiliate_links:
        pprint(link)
except InvalidTrackingIdException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```


**5. Retrieving Hot Products:**

```python
category_ids = ["CATEGORY_ID_1", "CATEGORY_ID_2"]
delivery_days = 7
try:
   hot_products = aliexpress_api.get_hotproducts(category_ids, delivery_days)
   pprint(hot_products)
except ProductsNotFoudException as e:
   print(f"Error: {e}")
except Exception as e:
   print(f"An unexpected error occurred: {e}")

```

**6. Retrieving Categories:**

```python
try:
    categories = aliexpress_api.get_categories()
    for category in categories:
        pprint(category)
except CategoriesNotFoudException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

**Important Considerations:**

* **Error Handling:** The code includes `try...except` blocks to catch potential exceptions (e.g., `ProductsNotFoudException`, `CategoriesNotFoudException`).  Always handle errors gracefully in your applications.
* **Logging:** The code uses `logger` for logging.  Use a robust logging framework for production applications.
* **Parameter Validation:**  Always validate input parameters to prevent unexpected behavior.
* **Rate Limiting:**  Be mindful of the AliExpress API's rate limits. Implement appropriate delays if necessary to avoid exceeding the limits.
* **`get_list_as_string`:** This function is critical for handling both single strings and lists of strings as input for `product_ids` and other parameters.
* **API Response:** Pay close attention to the response from the API. Check `response.current_record_count` and similar attributes to understand how many results you received.

This guide provides a starting point.  Refer to the API documentation for complete details and specific parameters. Remember to replace placeholders with your actual values. Always refer to the module's docstrings for comprehensive documentation on each method. Remember to use correct model objects for your language, currency, etc. to avoid errors.