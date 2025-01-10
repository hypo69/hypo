rst
How to use the `process_affiliate_products` function
=========================================================================================

Description
-------------------------
This function, `process_affiliate_products`, fetches product details from AliExpress, retrieves affiliate links, saves images and videos, and generates and saves campaign data in JSON format.  It takes a list of product IDs or URLs, a category path, and language/currency parameters, and returns a list of processed `SimpleNamespace` objects containing product data with affiliate links and local file paths to saved images and videos.  It handles potential errors like missing affiliate links and gracefully skips products without them.

Execution steps
-------------------------
1. **Input Validation:** Checks if `language` and `currency` are provided. If not, it logs a critical error and exits.

2. **Affiliate Link Retrieval:** Iterates through the provided list of `prod_ids`. For each `prod_id`, it calls `super().get_affiliate_links()` to obtain affiliate links.

3. **Link Processing:** It checks if an affiliate link was found for each product URL. If found, it appends the promotion link and the product URL to the respective lists.  It logs an informational message when an affiliate link is successfully found. If no affiliate link is found, it continues to the next product.

4. **Error Handling (No Affiliate Links):**  If no affiliate links were found for any product, it logs a warning message and returns an empty list, signaling the failure to process any product.

5. **Product Detail Retrieval:** If affiliate links are found, it calls `self.retrieve_product_details()` to fetch the product details using the product URLs.

6. **Image and Video Saving:** For each retrieved product and its corresponding promotion link, it saves the product's main image using `save_png_from_url` and stores the saved image path in the product object. If a video URL is present, it extracts the suffix, saves the video using `save_video_from_url`, and stores the saved video path.  It logs informative messages during image and video saving.

7. **Product Data Formatting:** The function sets the `language` and `promotion_link` attributes of each `SimpleNamespace` object.

8. **Saving Product Data to JSON:** It saves each processed product object as a JSON file within the specified `category_root` directory, using the product ID as the filename. The filename also incorporates the `language` and `currency`.

9. **Saving Product Titles:** Saves a list of product titles to a text file within the category directory.

10. **Return Value:** Returns a list of `SimpleNamespace` objects containing the processed product data, including affiliate links and saved media file paths.


Usage example
-------------------------
.. code-block:: python

    import asyncio
    from pathlib import Path
    from types import SimpleNamespace
    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

    async def main():
        # Replace with actual values
        prod_ids = ["http://example.com/product1", "http://example.com/product2"]
        category_root = Path("./output_data/campaign_category")
        
        aliexpress_instance = AliAffiliatedProducts(language='EN', currency='USD')  # Initialize the class
        products = await aliexpress_instance.process_affiliate_products(prod_ids, category_root)

        if products:
            for product in products:
                print(f"Product Title: {product.product_title}")
                print(f"Affiliate Link: {product.promotion_link}")
                print(f"Image Path: {product.local_image_path}")
                print("---")

    if __name__ == "__main__":
        asyncio.run(main())