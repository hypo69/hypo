rst
How to use the affiliated_products_generator script
=====================================================

Description
-------------------------
This Python script generates affiliate links for products from AliExpress. It takes a list of product URLs or IDs, extracts product information, and creates affiliate links.  The script also downloads product images (if available) and stores them locally.

Execution steps
-------------------------
1. **Import necessary modules**: The script imports the `AliAffiliatedProducts` class from the `src.suppliers.aliexpress.affiliated_products_generator` module.

2. **Define campaign parameters**: Set variables for the campaign name, category, language, and currency.  These parameters are used to customize the affiliate links.

3. **Instantiate the parser**: Create an instance of the `AliAffiliatedProducts` class, passing in the campaign parameters.

4. **Provide product URLs or IDs**: Create a list of URLs or product IDs for the products you want affiliate links for.

5. **Process affiliate products**: Call the `process_affiliate_products` method of the parser, passing in the list of product URLs/IDs.  This method handles the extraction of affiliate links and image downloading.

6. **Check results**: Check if the `products` list returned by `process_affiliate_products` is not empty.

7. **Print results**: If products were found, iterate through the `products` list and print the product ID, affiliate link, local image path, and local video path (if applicable). Otherwise, print a message indicating that no affiliate products were found.


Usage example
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

    def main():
        # Set campaign parameters
        campaign_name = "summer_sale_2024"
        campaign_category = "electronics"  # Optional, can be None
        language = "EN"
        currency = "USD"

        # Create an instance of the parser
        parser = AliAffiliatedProducts(
            campaign_name,
            campaign_category,
            language,
            currency
        )

        # Example product URLs or IDs
        prod_urls = [
            '123',
            'https://www.aliexpress.com/item/123.html',
            '456',
            'https://www.aliexpress.com/item/456.html',
        ]

        # Process products and get affiliate product links
        products = parser.process_affiliate_products(prod_urls)

        # Check the results
        if products:
            print(f"Retrieved {len(products)} affiliate products.")
            for product in products:
                print(f"Product ID: {product.product_id}")
                print(f"Affiliate link: {product.promotion_link}")
                print(f"Local image path: {product.local_image_path}")
                if product.local_video_path:
                    print(f"Local video path: {product.local_video_path}")
                print()
        else:
            print("Failed to retrieve affiliate products.")

    if __name__ == "__main__":
        main()