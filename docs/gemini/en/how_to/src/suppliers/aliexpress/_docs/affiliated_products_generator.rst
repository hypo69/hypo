rst
How to use the affiliated_products_generator.py code block
=========================================================

Description
-------------------------
This code defines the `AliAffiliatedProducts` class, which is responsible for fetching and processing product data from the AliExpress Affiliate API. It extracts product details, affiliate links, saves images and videos, and stores the collected data in a structured format.  The class handles product URLs or IDs, ensuring robust processing of affiliate product information.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports various libraries needed for asynchronous operations, data manipulation, file handling, and interactions with the AliExpress API.  These include `asyncio`, `pathlib`, `urllib`, external libraries from the `src` module (e.g., `AliApi`, `gs`, `save_png_from_url`), and more.


2. **Define the `AliAffiliatedProducts` class:** This class inherits from the `AliApi` class, extending its functionality with affiliate-specific operations.

3. **Initialize the class:**  The `__init__` method initializes `campaign_name`, `campaign_category`, `language`, and `currency` attributes, using these to construct paths for saving campaign materials.

4. **Process affiliate products:**  The `process_affiliate_products` method takes a list of product URLs or IDs as input.
    - It retrieves affiliate links for each product.
    - If a link is found, it saves the affiliate link.
    - It then retrieves the product details (image, video, etc.) using methods inherited from the `AliApi` class.
    - It saves images and videos to the designated campaign directory.
    - It stores the extracted product details in JSON format in the same campaign directory.


5. **Handle missing affiliate links:**  If an affiliate link isn't found for a product, it logs a warning and, crucially, removes the product from further processing.
    
6. **Error handling and logging:** The code includes logging statements to track processing progress and catch potential errors, such as network issues or invalid URLs, providing detailed information about failed operations.  This ensures that problematic products are identified and prevented from accumulating unnecessary errors.


7. **Deleting Products (if no affiliate link found):** The `delete_product` method is used to remove products lacking affiliate links from various data sources (e.g., source text files) by updating associated files.


Usage example
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress import AliAffiliatedProducts
    import asyncio  #For asynchronous operations
    import pathlib


    async def main():
        # Replace with your actual values
        campaign_name = "my_campaign"
        prod_urls = ["https://www.aliexpress.com/item/123456789.html", "https://www.aliexpress.com/item/987654321.html"]

        parser = AliAffiliatedProducts(
            campaign_name=campaign_name,
            language='EN',
            currency='USD'
        )

        products = await parser.process_affiliate_products(prod_urls)
        
        if products:
            for product in products:
                print(f"Product ID: {product.product_id}, Affiliate Link: {product.promotion_link}")



    if __name__ == "__main__":
        asyncio.run(main())