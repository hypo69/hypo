## \file hypotez/consultant/gemini/suppliers/aliexpress/affiliated_products_generator.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.suppliers.aliexpress """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress """
import asyncio
from datetime import datetime
import html
from pathlib import Path
from urllib.parse import urlparse
from types import SimpleNamespace
from typing import List

from src.logger import logger
from __init__ import gs
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress.campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator 
from src.suppliers.aliexpress.utils.ensure_https import ensure_https
from src.product.product_fields import ProductFields as f
from src.utils.image import save_png_from_url 
from src.utils.video import save_video_from_url
from src.utils.file import get_directory_names, get_filenames, read_text_file, save_text_file
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils import pprint
from src.logger import logger


class AliAffiliatedProducts(AliApi):
    """ Class to collect full product data from URLs or product IDs.
    For more details on how to create templates for ad campaigns, see the section `Managing Aliexpress Ad Campaigns`.
    """
    language: str = None
    currency: str = None

    def __init__(self, language: str | dict = 'EN', currency: str = 'USD', *args, **kwargs):
        """
        Initializes the AliAffiliatedProducts class.
        Args:
            language: Language for the campaign (default 'EN').
            currency: Currency for the campaign (default 'USD').
        """
        if not language or not currency:
            logger.critical("No language or currency specified!")
            return
        super().__init__(language, currency)
        self.language, self.currency = language, currency


    async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
        """
        Processes a list of product IDs or URLs and returns a list of products with affiliate links and saved images.
        """
        category_root = Path(category_root)
        category_root.mkdir(parents=True, exist_ok=True)

        #  Crucial fix:  Make sure category_root is a Path object
        normalized_prod_urls = ensure_https(prod_ids)

        affiliate_products = []
        for prod_url in normalized_prod_urls:
            links = super().get_affiliate_links(prod_url)
            if links and links[0] and links[0].promotion_link:  # Check if links and promotion_link exist
                promotion_link = links[0].promotion_link
                product_data = await self.get_product_details(prod_url)
                if product_data:
                    product_data.language = self.language
                    product_data.promotion_link = promotion_link
                    image_path = category_root / 'images' / f"{product_data.product_id}.png"
                    await save_png_from_url(product_data.product_main_image_url, image_path)
                    product_data.local_saved_image = str(image_path)
                    
                    if product_data.product_video_url:  # Check if video URL exists
                        parsed_url = urlparse(product_data.product_video_url)
                        suffix = Path(parsed_url.path).suffix
                        video_path = category_root / 'videos' / f"{product_data.product_id}{suffix}"
                        await save_video_from_url(product_data.product_video_url, video_path)
                        product_data.local_saved_video = str(video_path)


                    j_dumps(product_data, category_root / f"{self.language}_{self.currency}" / f"{product_data.product_id}.json")
                    affiliate_products.append(product_data)
                    logger.info(f"Processed product: {product_data.product_title}")
                else:
                    logger.warning(f"Failed to retrieve product details for {prod_url}")


        # Create and save product titles
        product_titles = [p.product_title for p in affiliate_products]
        product_titles_path = category_root / f"{self.language}_{self.currency}" / "product_titles.txt"
        save_text_file(product_titles, product_titles_path)

        return affiliate_products
```

**Key Improvements and Explanations:**

* **Error Handling and Robustness:**
    * **`if links and links[0] and links[0].promotion_link:`:**  This crucial check now verifies that `links` isn't empty, `links[0]` exists, and `links[0].promotion_link` is actually present. This prevents crashes if `get_affiliate_links` returns an unexpected value.
    * **`if product_data:`:** Checks if `get_product_details` successfully returned data. This avoids errors if the product page doesn't load or parse correctly.
    * **Logging:** Clearer error logging messages are added. This significantly helps in debugging.


* **Correct Path Handling:**
    * **`category_root = Path(category_root)`:** Converts `category_root` to a `Path` object for correct path manipulation. This is essential for cross-platform compatibility and avoids potential errors.


* **Conciseness and Readability:**
   - Reduced repetition and improved code structure.
   - Added `# Check if video URL exists` comments for clarity.


* **`get_product_details` (Crucial):**
   - The code now *assumes* you have a method `self.get_product_details(prod_url)` defined somewhere.  This method is responsible for fetching and parsing the product details from the URL.   Without it, this function won't work.  Make sure this method is correctly implemented in your `AliApi` class.


**How to Use:**


```python
# Example Usage (assuming you have the necessary imports and 'AliApi' class)
import asyncio

async def main():
    prod_ids = ["your_product_id1", "your_product_id2"]  # Replace with actual product IDs or URLs
    category_name = "your_category"
    
    aliapi_instance = AliApi(your_language, your_currency)
    await aliapi_instance.process_affiliate_products(prod_ids, category_name)



if __name__ == "__main__":
    asyncio.run(main())

```

Remember to replace placeholders like `"your_product_id1"`, `"your_product_id2"`, `your_category`, `your_language`, and `your_currency` with your actual values.  Crucially, you need to implement the `get_product_details` method in your `AliApi` class. This revised code significantly improves error handling and code robustness, addressing potential issues in the original version. Please provide the `AliApi` class and `get_product_details` method if you need further assistance.