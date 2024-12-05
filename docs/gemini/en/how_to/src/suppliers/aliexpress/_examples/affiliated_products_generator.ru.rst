rst
How to use the `affiliated_products_generator` module
==========================================================================================

Description
-------------------------
This code demonstrates how to use the `AliAffiliatedProducts` class to collect product data and generate affiliate links from AliExpress.  It shows how to specify campaign details, provide product URLs or IDs, and process them to obtain affiliate product information.  Crucially, it handles potential errors and prints informative messages.

Execution steps
-------------------------
1. **Import the `AliAffiliatedProducts` class:**
   ```python
   from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
   ```
2. **Define campaign parameters:**
   Set the `campaign_name`, `campaign_category` (optional), `language`, and `currency` for the campaign.
   ```python
   campaign_name = "summer_sale_2024"
   campaign_category = "electronics"
   language = "EN"
   currency = "USD"
   ```
3. **Instantiate the `AliAffiliatedProducts` object:**
   Create an instance of the `AliAffiliatedProducts` class, passing the campaign parameters.
   ```python
   parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
   ```
4. **Prepare a list of product URLs or IDs:**
   Provide a list of URLs or IDs of the AliExpress products you want to process.
   ```python
   prod_urls = [
       '123',
       'https://www.aliexpress.com/item/123.html',
       '456',
       'https://www.aliexpress.com/item/456.html',
   ]
   ```
5. **Process the products:**
   Call the `process_affiliate_products` method of the `AliAffiliatedProducts` object, passing the list of URLs or IDs.  This step fetches affiliate links and potentially downloads product images and videos, storing them locally.
   ```python
   products = parser.process_affiliate_products(prod_urls)
   ```
6. **Check and display the results:**
   Check if any products were successfully processed.
   ```python
   if products:
       print(f"Successfully processed {len(products)} affiliate products.")
       for product in products:
           # Print the key product details
           print(f"Product ID: {product.product_id}")
           print(f"Affiliate link: {product.promotion_link}")
           print(f"Local image path: {product.local_saved_image}")
           if product.local_saved_video:
               print(f"Local video path: {product.local_saved_video}")
           print()
   else:
       print("Failed to process any affiliate products.")
   ```


Usage example
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

    def main():
        campaign_name = "summer_sale_2024"
        campaign_category = None
        language = "EN"
        currency = "USD"
        prod_urls = [
            '123',
            'https://www.aliexpress.com/item/123.html',
            '456',
            'https://www.aliexpress.com/item/456.html',
        ]

        parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
        products = parser.process_affiliate_products(prod_urls)
        if products:
            for product in products:
                print(f"ID: {product.product_id}, Link: {product.promotion_link}, Image: {product.local_saved_image}")
        else:
            print("No products processed.")

    if __name__ == "__main__":
        main()