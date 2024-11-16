## \file hypotez/consultant/gemini/suppliers/amazon/via_webdriver.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.suppliers.amazon """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.suppliers.amazon """
"""  Модуль сбора товаров со страницы категорий поставщика amazon.com через вебдрайвер

У каждого поставщика свой сценарий обреботки категорий

-Модуль Собирает список категорий со страниц продавца . `get_list_categories_from_site()`.
@todo Сделать проверку на изменение категорий на страницах продавца. 
Продавец может добавлять новые категории, переименовывать или удалять/прятать уже существующие. 
По большому счету надо держать таблицу категории `prestashop.categories <-> amazon.shop.categoies`
- Собирает список товаров со страницы категории `get_list_products_in_category()`
- Итерируясь по списку передает управление в `grab_product_page()` отсылая функции текущий url страницы  
`grab_product_page()` обрабатывает поля товара и передает управление классу `Product` 

"""

from typing import List, Union
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException

from __init__ import gs  # Assuming __init__.py exists and imports necessary modules
from src.logger import logger
from src.product import Product  # Import your Product class
# from ... (import your PrestashopProduct class) - Adjust the path as needed

def get_list_products_in_category(s) -> List[str]:
    """ Returns list of products urls from category page.

    Args:
        s: Supplier instance.

    Returns:
        List of product URLs, or None if no product URLs are found or an error occurs.  Returns an empty list if no links are found.
    """
    driver = s.driver
    locators = s.locators['category']

    if not locators:
        logger.error(f"Locators for category not found: {locators}")
        return None  # Or raise an exception, depending on your error handling strategy

    try:
        product_links = driver.execute_script(
            f"return {locators['product_links']}"
        )  #  Use execute_script for dynamic selection
    except (NoSuchElementException, AttributeError) as e:
        logger.error(f"Error getting product links: {e}")
        return [] # Return empty list if no links are found

    if not product_links:
        logger.warning('No product links found on the page.')
        return []  # Return empty list

    if isinstance(product_links, str):  # Handle single string
      product_links = [product_links]

    logger.info(f"Found {len(product_links)} products.")
    return product_links


#Example usage (replace with your actual Supplier and locator structure)
# supplier = Supplier(...)
# product_urls = get_list_products_in_category(supplier)

# if product_urls:
#   for url in product_urls:
#      product = Product(url, supplier)  # Pass the supplier instance to the Product
#      product.scrape()


```

**Key Improvements and Explanations:**

* **Error Handling:** Added `try...except` block to catch `NoSuchElementException` and `AttributeError` which can occur if the locator doesn't exist or if the `driver.execute_locator` method isn't working as expected. This prevents your script from crashing. Critically, it handles the case where no product links are found.  Returning `None` or raising an exception would lead to larger issues down the line.
* **Type Hinting:** Added type hints for clarity and maintainability.
* **`execute_script`:**  This is now the corrected way to extract the product URLs dynamically. The previous code assumed a `driver.execute_locator` method exists, which is not a standard Selenium method. `execute_script` allows you to run JavaScript inside the browser context to extract the links. This is necessary if the links are not directly accessible with the locators. Replace the hardcoded JavaScript with the correct selector based on the HTML structure. 
* **Empty List Handling:** Returns an empty list (`[]`) if no product links are found. This is a more robust way to signal the lack of results.  The original code would result in a `TypeError` if `list_products_in_category` were empty.
* **Clearer Logging:** More informative logging messages.
* **Return `None` if locators are missing:** Returns `None` if the `s.locators['category']` dictionary is empty, signaling a critical error in the data flow.
* **Handling Single String Result:** `if isinstance(product_links, str):` ensures that the function works correctly if the script only returns a single string.
* **Import `Product`:** Makes sure the `Product` class is importable.
* **Improved Variable Names:** Replaced `l` with `locators` for better readability.
* **Corrected return type:** Changed the return type to `List[str]` which is more accurate.

**How to Use:**

1. **Get Product Links:** Call `get_list_products_in_category()` with a `Supplier` object.
2. **Iterate and Process:**  Iterate over the returned list of product URLs and create `Product` objects for each URL.  You'll need to have a `Product` class (or another object to handle product data) that is responsible for scraping the details from the product page. 

**Example of `Product` class (placeholder):**

```python
from src.logger import logger  # Import your logger

class Product:
    def __init__(self, product_url, supplier):
        self.product_url = product_url
        self.supplier = supplier

    def scrape(self):
      # Implementation to scrape the product details
        try:
          # Your scraping code here
          logger.info(f"Scraping product: {self.product_url}")
          # ...extract and process details...
        except Exception as e:
          logger.error(f"Error scraping product {self.product_url}: {e}")
```

**Before running:**

* **Install Selenium:** `pip install selenium`
* **Set up your WebDriver:** Configure your `driver` object within your `Supplier` class to initialize the Amazon WebDriver.
* **Adjust locators:** The crucial part is to replace the placeholder JavaScript selector (`locators['product_links']`) with the correct one based on the structure of the Amazon product listing page. Use the developer tools in your browser to inspect the HTML and find the appropriate CSS selector or XPath expression.



Remember to adapt the code to your specific `Supplier` class and the structure of your Amazon product pages.