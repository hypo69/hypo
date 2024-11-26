# How to Use the `affiliated_products_generator.py` Module (AliExpress)

This guide explains how to use the `AliAffiliatedProducts` class within the `affiliated_products_generator.py` module to generate affiliate links and download images/videos for products from AliExpress.

## Prerequisites

- The `affiliated_products_generator.py` module (containing the `AliAffiliatedProducts` class) must be installed and importable.
- You'll need an internet connection.
- (Optional)  A configured environment for saving downloaded images/videos.


## Example Usage

The following example demonstrates how to use the `AliAffiliatedProducts` class to process a list of product IDs or URLs and obtain affiliate links, image paths, and video paths (if available).

```python
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Configuration parameters
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Optional, can be None
    language = "EN"
    currency = "USD"

    # Initialize the parser with campaign details
    parser = AliAffiliatedProducts(
        campaign_name, campaign_category, language, currency
    )

    # List of product IDs or URLs (mix is possible)
    prod_urls = [
        "123",
        "https://www.aliexpress.com/item/123.html",
        "456",
        "https://www.aliexpress.com/item/456.html",
    ]

    # Process the products
    products = parser.process_affiliate_products(prod_urls)

    # Check for results and print product details
    if products:
        print(f"Found {len(products)} affiliate products:")
        for product in products:
            print(f"  Product ID: {product.product_id}")
            print(f"  Affiliate Link: {product.promotion_link}")
            print(f"  Local Image Path: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"  Local Video Path: {product.local_saved_video}")
            print("-" * 20)  # Separator for better readability
    else:
        print("No affiliate products found.")


if __name__ == "__main__":
    main()
```

**Explanation:**

1. **Import the Class:** Import the `AliAffiliatedProducts` class from the correct module.
2. **Configure Campaign:**  Set the `campaign_name`, `campaign_category`, `language`, and `currency`.  Crucially, these parameters are used to shape the requests to the AliExpress API.
3. **Initialize the Parser:** Create an instance of `AliAffiliatedProducts`, passing in the configured parameters.
4. **Product URLs/IDs:** Provide a list of product URLs or IDs.  You can mix both.
5. **Process Products:** Call `parser.process_affiliate_products(prod_urls)` to retrieve affiliate links and potentially save images/videos.
6. **Check and Print Results:** The `products` list will contain `Product` objects.  Iterate through this list to print the relevant attributes.

## Important Considerations

- **Error Handling:** The example lacks error handling.  Add `try...except` blocks to catch potential issues like network problems, invalid product IDs/URLs, or API rate limits.
- **Saving Locations:** The code assumes you have the proper file system setup for saving downloaded images/videos. Ensure correct file paths are used.
- **API Limits:** AliExpress API likely has rate limits. Implement appropriate delays or throttling to avoid exceeding them.
- **`Product` Object Structure:** Ensure the `Product` object within the `AliAffiliatedProducts` class has the necessary attributes like `promotion_link`, `local_saved_image`, and `local_saved_video`.


This guide provides a basic template. Adjust the code to your specific requirements for handling errors, saving media, and processing data after retrieval. Remember to consult the source code of the `affiliated_products_generator.py` module for further details on the `AliAffiliatedProducts` class and its methods.