Certainly! Here’s a detailed breakdown of the `affiliated_products_generator.py` file from the `src.suppliers.aliexpress` module:

---

## `affiliated_products_generator.py` Overview

The `affiliated_products_generator.py` file contains the `AliAffiliatedProducts` class. This class is responsible for generating complete product data from the Aliexpress Affiliate API. It builds on the `AliApi` class to process product URLs or IDs and retrieve details about affiliate products, including saving images, videos, and JSON data.

### Imports and Dependencies

```python
import asyncio
from itertools import count
from math import log
from pathlib import Path
from typing import List, Union, Optional
from types import SimpleNamespace
from urllib.parse import urlparse, parse_qs

from src import gs
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress import Aliexpress
from src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver import AffiliateLinksShortener
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.suppliers.aliexpress.utils.set_full_https import ensure_https
from src.utils.convertor.csv2json import csv2dict 
from src.utils import j_dumps
from src.utils import save_png_from_url, save_video_from_url
from src.utils import pprint 
from src.utils.file import read_text_file, save_text_file

from src.logger import logger
```

- **Standard Libraries:** `asyncio`, `itertools`, `math`, `pathlib`, `typing`, `types`, `urllib.parse`
- **External Libraries:** `src.settings`, `src.suppliers.aliexpress`, `src.utils.convertor`, `src.utils`, `src.logger`

### `AliAffiliatedProducts` Class

#### Class Docstring

```python
class AliAffiliatedProducts(AliApi):
    """ Class to collect full product data from URLs or product IDs
    locator_description For more details on how to create templates for ad campaigns, see the section `Managing Aliexpress Ad Campaigns`
    @code
    # Example usage:
    prod_urls = ['123','456',...]
    prod_urls = ['https://www.aliexpress.com/item/123.html','456',...]

    parser = AliAffiliatedProducts(
                                campaign_name,
                                campaign_category,
                                language,
                                currency)

    products = parser._affiliate_product(prod_urls)
    @endcode
    """
```

- **Purpose:** Collect full product data from URLs or product IDs using the Aliexpress Affiliate API.
- **Usage Example:** Shows how to initialize the class and call the `_affiliate_product` method to process product URLs.

#### Attributes

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

- **`campaign_name`**: Name of the advertising campaign.
- **`campaign_category`**: Category for the campaign (default is `None`).
- **`campaign_path`**: Path to the directory where campaign materials are stored.
- **`language`**: Language for the campaign (default is `'EN'`).
- **`currency`**: Currency for the campaign (default is `'USD'`).

#### Initialization

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    @param campaign_name `str`: Name of the advertising campaign. The directory with the prepared material is taken by name.
    @param campaign_category `Optional[str]`: Category for the campaign (default None).
    @param language `str`: Language for the campaign (default 'EN').
    @param currency `str`: Currency for the campaign (default 'USD').
    @param tracking_id `str`: Tracking ID for Aliexpress API.
    """
    super().__init__(language, currency)

    self.campaign_name = campaign_name
    self.campaign_category = campaign_category
    self.language = language
    self.currency = currency
    self.locale = f"{self.language}_{self.currency}"
    self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
```

- **`super().__init__(language, currency)`**: Calls the parent `AliApi` class’s constructor.
- **`self.campaign_path`**: Constructs the path to the campaign directory based on the `campaign_name` and `campaign_category`.

#### Methods

##### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Processes a list of URLs and returns a list of products with affiliate links and saved images.

    :param prod_urls: List of product URLs or IDs.
    :return: List of processed products.
    """
    ...
    _promotion_links: list = []
    _prod_urls: list = []
    promotional_prod_urls = ensure_https(prod_urls)
    print_flag = 'new_line'
    for prod_url in promotional_prod_urls:
        _link = super().get_affiliate_links(prod_url)
        if _link:
            _link = _link[0]    
        if hasattr(_link, 'promotion_link'):
            _promotion_links.append(_link.promotion_link)
            _prod_urls.append(prod_url)
            
            pprint(f'found affiliate for: {_link.promotion_link}', end=print_flag)
            print_flag = 'inline'
        else:
            logger.info_red(f'Not found affiliate for {prod_url}')
    
    if not _promotion_links:
        logger.error('No affiliate products returned')
        return
    logger.info_red('Start receiving product details...')
    _affiliate_products: SimpleNamespace = self.retrieve_product_details(_prod_urls)
    if not _affiliate_products:
        return 
    
    print_flag = 'new_line'
    for product, promotion_link in zip(_affiliate_products, _promotion_links):
        ...

        if not promotion_link:
            parsed_url = urlparse(product.promotion_link)
            query_params = parse_qs(parsed_url.query)
            aff_short_key = query_params.get('aff_short_key', [None])[0]
            if aff_short_key:
                product.promotion_link = fr'https://s.click.aliexpress.com/e/{aff_short_key}'
            else:
                """ This product is not an affiliate"""
                self.delete_product(product.product_id)
                ...
        else:
            product.promotion_link = promotion_link
        
        image_path = self.campaign_path / 'images' / f"{product.product_id}.png"
        save_png_from_url(product.product_main_image_url, image_path, exc_info=False)
        product.image_local_saved_path = str(image_path)
        if len(product.product_video_url) > 1:
            parsed_url = urlparse(product.product_video_url)
            suffix = Path(parsed_url.path).suffix
            
            video_path = self.campaign_path / 'videos' / f'{product.product_id}.{suffix}'
            save_video_from_url(product.product_video_url, video_path, exc_info=False)
            product.video_local_saved_path = str(video_path)

        pprint(f'caught product - {product.product_id}', end=print_flag)
        print_flag = 'inline'
        
        if not j_dumps(product, self.campaign_path / self.locale / f"{product.product_id}.json", exc_info=False):
            logger.warning(f"""Failed to write dictionary: \n {pprint(product)} \n path: {self.campaign_path / self.locale / product.product_id}.json""", exc_info=False)
            ...
            continue
            
    pprint(f'caught {len(_affiliate_products)}', end='new_line')
    return _affiliate_products
```

- **Purpose:** Process a list of product URLs or IDs to retrieve affiliate links, save images and videos, and store product details.
- **Parameters:**
  - **`prod_urls`**: List of product URLs or IDs.
- **Returns:** List of `SimpleNamespace` objects representing the processed products.

##### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Delete a product that does not have an affiliate link"""
    ...
    _product_id = extract_prod_ids(product_id)
    
    product_path = self.campaign_path / 'sources.txt'
    prepared_product_path = self.campaign_path / '_sources.txt'
    products_list = read_text_file(product_path)
    if products_list:
        products_list = convert_list_to_homogeneous_list(products_list)
        for record in products_list:
            if _product_id:
                record_id = extract_prod_ids(record)
                if record_id == str(product_id):
                    products_list.remove(record)
                    save_text_file(list2string(products_list, '\n'), prepared_product_path)
                    break
            else:
                if record == str(product_id):
                    products_list.remove(record)
                    save_text_file(list2string(products_list, '\n'), product_path)
            
    else:
        product_path = self.campaign_path / 'sources' / f'{product_id}.html'    
        try:
            product_path.rename(self.campaign_path / 'sources' / f'{product_id}_.html')
            # product_path.unlink()
            logger.success(f"Product file {product_path} renamed successfully.")
        except FileNotFoundError as ex:
            logger.error(f"Product file {product_path} not found.", exc_info=exc_info)
        except Exception as ex:
            logger.critical(f"An error occurred while deleting the product file {product_path}.", ex)                
    ...
```

- **Purpose:** Remove a product that does

The provided code is a Python implementation of a class `AliAffiliatedProducts` that interacts with the AliExpress Affiliate API to gather product data, including affiliate links and images. The class is designed to process a list of product URLs or IDs, retrieve their details, and save relevant information locally. Additionally, there are unit tests defined using the `pytest` framework to ensure the functionality of the `process_affiliate_products` method.

Here's a breakdown of the key components:
@rst
### Class: `AliAffiliatedProducts`

- **Initialization**: The constructor accepts parameters for language and currency, which are passed to the superclass `AliApi`.
- **Method: `process_affiliate_products`**: - This method takes a list of product IDs or URLs, a path to save images, and a locale.
 - It fetches affiliate links for the provided product IDs, retrieves product details, and saves images and videos locally.
 - It uses helper functions to handle HTTP requests and save media files.
 - The method returns a list of processed products, each represented as a `SimpleNamespace` object.

### Key Functionalities1. **Fetching Page Content**: The `get_page_content` function retrieves the HTML content of a given URL using the `requests` library, handling any potential HTTP errors.

2. **Affiliate Link Retrieval**: The method calls `get_affiliate_links` to obtain affiliate links for each product URL.

3. **Product Details Retrieval**: The method retrieves product details using `retrieve_product_details`.

4. **Media Saving**: It saves product images and videos using utility functions like `save_png_from_url` and `save_video_from_url`.

5. **Logging**: The method logs various stages of processing, including errors and successful retrievals.

### Unit TestsThe unit tests are designed to validate the behavior of the `process_affiliate_products` method under different scenarios:

1. **Successful Processing**: Tests that the method correctly processes product IDs and retrieves affiliate links and product details.

2. **No Affiliate Links**: Tests the method's behavior when no affiliate links are found, expecting an empty return.

3. **No Products Returned**: Tests the method's behavior when no product details are returned, also expecting an empty return.

### Example UsageThe example usage in the class docstring demonstrates how to instantiate the `AliAffiliatedProducts` class and call the `process_affiliate_products` method with a list of product URLs or IDs.

### Improvements and Considerations- **Error Handling**: While there is some error handling in place, further enhancements could be made to handle specific cases more gracefully.
- **Testing Coverage**: Additional tests could be added to cover edge cases, such as invalid URLs or network failures.

- **Performance**: Depending on the number of products processed, consider implementing asynchronous requests to improve performance.

- **Documentation**: Ensure that the code is well-documented, especially for public methods, to facilitate easier understanding and usage by other developers.

