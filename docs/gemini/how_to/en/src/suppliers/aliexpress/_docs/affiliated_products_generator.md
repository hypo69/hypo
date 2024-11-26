# Usage Guide for `affiliated_products_generator.py`

This guide explains how to use the `affiliated_products_generator.py` script, part of the `src.suppliers.aliexpress` module, to fetch and process affiliate product data from AliExpress.

## Prerequisites

- Python 3.x
- Libraries mentioned in the imports section of the file (e.g., `asyncio`, `requests`, `pathlib`, `src.utils`, etc.).  Ensure these are installed.  You'll likely need to install any `src` packages as well.
- An AliExpress affiliate account and API access. This might require obtaining appropriate API keys or credentials.  Crucially, you'll need to ensure proper authorization to use the API.
- Valid product URLs or IDs for AliExpress products.

## Running the Script

1. **Initialization:**

   ```python
   from src.suppliers.aliexpress import AliAffiliatedProducts

   parser = AliAffiliatedProducts(
       campaign_name="MyCampaign",  # Replace with your campaign name
       campaign_category="Electronics",  # Optional category
       language="EN",
       currency="USD"
   )
   ```

   This creates an `AliAffiliatedProducts` object.  Critically, replace `"MyCampaign"` with the actual name of the campaign directory.  This is where the output data (images, videos, JSON files) will be stored.  The `campaign_category` is optional.

2. **Fetching Product Data:**

   ```python
   product_ids_or_urls = [
       "https://www.aliexpress.com/item/1234567890.html",
       "1098765432",  # Or a product ID
       "https://www.aliexpress.com/item/another-product.html"
   ]

   products = parser.process_affiliate_products(product_ids_or_urls)
   ```

   This is the core function. Pass a list of product URLs or IDs to `process_affiliate_products`. It returns a list of `SimpleNamespace` objects containing the product data.  Importantly, if no affiliate link is found for a product, it will be deleted from the processing pipeline, and a log message will be produced.

3. **Handling Results:**

   ```python
   if products:
       for product in products:
           print(f"Product ID: {product.product_id}")
           print(f"Affiliate Link: {product.promotion_link}")
           print(f"Image saved to: {product.local_saved_image}")
           # ... process other product details ...
   else:
       print("No affiliate products found or an error occurred.")
   ```

   Inspect the results; if the list is empty, an error occurred during processing. If there are any processing errors, check the `logger` output for details.

## Important Considerations

- **Error Handling:** The `process_affiliate_products` method includes basic error handling, but robust error handling (e.g., checking for network issues, invalid URLs, non-existent products) should be implemented.  The use of `exc_info` in error handling calls suggests that appropriate logging is employed to help diagnose and troubleshoot problems during processing.

- **Rate Limiting:**  AliExpress's API likely has rate limits. Implement appropriate delays between API calls to avoid exceeding these limits.

- **Asynchronous Operations:** For large numbers of products, consider using `asyncio` for asynchronous requests to improve performance.

- **Output Directory Structure:** The `campaign_path` is critical. The script creates a directory structure under the campaign path that makes sense for storing the parsed product information. Understand and respect this structure for retrieving the data later.

- **Logging:** The code utilizes a logger. Ensure that proper logging is configured and that you are correctly checking logs in case of issues.


## Example Error Handling (Illustrative)

```python
try:
    products = parser.process_affiliate_products(product_ids_or_urls)
except Exception as e:
    print(f"An error occurred: {e}")
    # Handle the exception appropriately, perhaps logging it.
```

This detailed guide provides a comprehensive understanding of how to use `affiliated_products_generator.py`. Remember to adapt the code to your specific needs and integrate it into your broader application. Always refer to the source code and API documentation for the most up-to-date and accurate information.