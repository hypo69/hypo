```markdown
# AliExpress API Wrapper for Python

## File: `hypotez/src/suppliers/aliexpress/api/api.py`

This Python module provides a wrapper for the AliExpress Open Platform API.  It simplifies interacting with the API, handling requests, responses, and data parsing.


### Class: `AliexpressApi`

This class encapsulates the interaction with the AliExpress API.

#### Constructor (`__init__`)

```python
def __init__(self, key: str, secret: str, language: model_Language, currency: model_Currency, tracking_id: str = None, app_signature: str = None, **kwargs):
```

*   **`key` (str):** Your AliExpress API key.
*   **`secret` (str):** Your AliExpress API secret.
*   **`language` (model_Language):** Language code (e.g., `model_Language.EN`).
*   **`currency` (model_Currency):** Currency code (e.g., `model_Currency.USD`).
*   **`tracking_id` (str, optional):**  Tracking ID for link generation. Defaults to `None`.
*   **`app_signature` (str, optional):** Application signature. Defaults to `None`.
*   **`**kwargs`:** Additional keyword arguments.


#### Methods

##### `retrieve_product_details`

```python
def retrieve_product_details(self, product_ids: str | list, fields: str | list = None, country: str = None, **kwargs) -> List[model_Product]:
```

*   **`product_ids` (str | list[str]):** One or more product IDs or URLs.
*   **`fields` (str | list[str], optional):** Specific fields to retrieve. Defaults to all.
*   **`country` (str, optional):** Country code for price filtering.
*   **Returns:** A list of `model_Product` objects.
*   **Raises:**
    *   `ProductsNotFoudException`: If no products are found.
    *   Other exceptions related to invalid input or API errors.


##### `get_affiliate_links`

```python
def get_affiliate_links(self, links: str | list, link_type: model_LinkType = model_LinkType.NORMAL, **kwargs) -> List[model_AffiliateLink]:
```

*   **`links` (str | list[str]):** List of product IDs or URLs to generate affiliate links for.
*   **`link_type` (model_LinkType, optional):** Type of affiliate link (e.g., normal or hotlink). Defaults to `model_LinkType.NORMAL`.
*   **Returns:** A list of `model_AffiliateLink` objects.
*   **Raises:**
    *   `InvalidTrackingIdException`: If `tracking_id` is missing.
    *   `ProductsNotFoudException`: If no affiliate links are found.
    *   Other exceptions related to invalid input or API errors.


##### `get_hotproducts`

```python
def get_hotproducts(self, ... ) -> model_HotProductsResponse:
```

*   **Detailed Description of Arguments (very important):**  This method is crucial. You need to thoroughly document the parameters to help users understand how to effectively filter products.  Specifically explain how `max_sale_price` and `min_sale_price` work with the currency (e.g., they're in the lowest denomination of the specified currency). Include examples.


##### `get_categories`, `get_parent_categories`, `get_child_categories`

These methods handle category retrieval, with `get_categories` retrieving both parent and child categories, and `get_parent_categories` and `get_child_categories` filtering based on the parent ID. Add detailed descriptions of what each method does and the data types returned.

### Important Considerations

*   **Error Handling:** The code includes `try...except` blocks to catch exceptions and log errors.  This is good practice.  However, consider adding more specific exception handling (e.g., for different types of API errors).
*   **Logging:** `logger` is used for logging. This is excellent.
*   **Type Hinting:** The use of type hinting (`typing`) is good for readability and maintainability.
*   **`model_` prefixes:**  Make sure the `model_*` classes are properly defined in the `models` submodule.
*   **Input Validation:**  Consider adding validation to ensure input parameters are valid (e.g., checking if `product_ids` is a valid list or string).
*   **API Rate Limiting:** Implement mechanisms to handle API rate limits to avoid getting your IP address blocked.


This improved documentation provides a more complete and user-friendly guide for using this AliExpress API wrapper. Remember to thoroughly document the `model_*` classes and other submodules for a comprehensive API reference.
```