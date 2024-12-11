rst
How to use the `AliAffiliatedProducts` class
=========================================================================================

Description
-------------------------
This code demonStartes how to use the `AliAffiliatedProducts` class to generate affiliate links for products from AliExpress.  It takes a list of product URLs or IDs, retrieves affiliate links and associated image/video paths, and prints the results.  The code handles setting up campaign parameters like name, category, language, and currency.


Execution steps
-------------------------
1. **Import the `AliAffiliatedProducts` class:** Import the `AliAffiliatedProducts` class from the `affiliated_products_generator` module.

2. **Set campaign parameters:** Define variables for `campaign_name`, `campaign_category` (optional), `language`, and `currency`.  These parameters are used to tailor the affiliate links and associated data.

3. **Create an `AliAffiliatedProducts` instance:** Instantiate the `AliAffiliatedProducts` class, passing the campaign parameters.

4. **Prepare a list of product URLs or IDs:** Create a list (`prod_urls`) containing product URLs (e.g., `https://www.aliexpress.com/item/123.html`) or product IDs (e.g., `123`).

5. **Process affiliate products:** Call the `process_affiliate_products` method of the `AliAffiliatedProducts` instance, passing the `prod_urls` list.  This method gathers affiliate links, downloads images/videos, and stores the results in a list of `Product` objects.

6. **Check for results:** Check if the `products` list returned by `process_affiliate_products` is empty.

7. **Print retrieved results:** If `products` is not empty, print a header indicating the number of affiliate products found. Loop through each `Product` object in the `products` list and print the product ID, affiliate link, local image path, and local video path (if available).

8. **Handle no products found:** If the `products` list is empty, print a message indicating that no affiliate products were found.


Usage example
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

    def main():
        # Set up campaign parameters
        campaign_name = "summer_sale_2024"
        campaign_category = "electronics"
        language = "EN"
        currency = "USD"

        # Create an AliAffiliatedProducts instance
        parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)

        # List of product IDs or URLs
        prod_urls = [
            "123",
            "https://www.aliexpress.com/item/123.html",
            "456",
            "https://www.aliexpress.com/item/456.html",
        ]

        # Process affiliate products
        products = parser.process_affiliate_products(prod_urls)

        # Check for results and print
        if products:
            print(f"Received {len(products)} affiliate products.")
            for product in products:
                print(f"Product ID: {product.product_id}")
                print(f"Affiliate Link: {product.promotion_link}")
                print(f"Local Image Path: {product.local_saved_image}")
                if product.local_saved_video:
                    print(f"Local Video Path: {product.local_saved_video}")
                print()
        else:
            print("No affiliate products found.")

    if __name__ == "__main__":
        main()