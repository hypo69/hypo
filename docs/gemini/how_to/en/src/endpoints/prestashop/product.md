How to use the `PrestaProduct` class to interact with a PrestaShop product API

This guide demonstrates how to use the `PrestaProduct` class from the `hypotez/src/endpoints/prestashop/product.py` file to perform operations on PrestaShop products.

**Prerequisites**

- You need to have a PrestaShop store with an API enabled.
- You need the `api_domain` and `api_key` for your PrestaShop store.
- Python 3.12 (or later) must be installed with necessary libraries imported.

**Class Description**

The `PrestaProduct` class is a subclass of the `PrestaShop` class. It provides methods to interact with PrestaShop products via its API.  The `PrestaShop` class likely handles the core API communication logic.

**Key Methods**

* **`check(product_reference: str)`:**
    - **Purpose:** Checks for the existence of a product in the PrestaShop database based on the `product_reference`.  This could be the SKU or MKT product identifier.
    - **Input:** `product_reference` (string): The product reference (e.g., SKU).
    - **Output:** A dictionary containing the product details if found, otherwise `False`.
    - **Example:**

```python
product_reference = "your_product_reference"
product_info = presta_product_object.check(product_reference)
if product_info:
    pprint(product_info) # Print the product details
else:
    print("Product not found.")
```

* **`search(filter: str, value: str)`:**
    - **Purpose:** Performs an advanced search on products using specific filters.
    - **Input:**
        - `filter` (string): The filter to apply (e.g., "reference", "name").
        - `value` (string): The value to search for.
    - **Output:** A list of dictionaries containing the search results.
    - **Example:**

```python
filter_criteria = "reference"
search_value = "12345"
search_results = presta_product_object.search(filter_criteria, search_value)
if search_results:
    for product in search_results:
        pprint(product)  # Print each found product
else:
    print("No matching products found.")
```

* **`get(id_product)`:**
    - **Purpose:** Retrieves product information based on its ID.
    - **Input:** `id_product` (integer): The ID of the product.
    - **Output:** A dictionary containing the product details.
    - **Example:**

```python
product_id = 10
product_data = presta_product_object.get(product_id)
if product_data:
    pprint(product_data)
else:
    print(f"Product with ID {product_id} not found.")
```

**Constructor (`__init__`)**

The constructor requires configuration information:

```python
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
presta_product_object = PrestaProduct(credentials=credentials)
```

or

```python
presta_product_object = PrestaProduct(api_domain='your_api_domain', api_key='your_api_key')
```

**Important Notes**

- Replace placeholders like `your_api_domain`, `your_api_key`, and `your_product_reference` with your actual values.
- Ensure the `header` module and `src.logger` are correctly imported and configured.
- The `pprint` function from `src.utils.printer` is used for printing the results, which is recommended for better readability.
- Error handling (using `try...except` blocks) is crucial for production-level code. The code example demonstrates basic error checks but more sophisticated error handling is advised.
- Consult the PrestaShop API documentation for the specific structure of the returned data and possible errors.


This comprehensive guide should help you effectively use the `PrestaProduct` class for your PrestaShop product interactions. Remember to thoroughly test your code with various inputs and scenarios.