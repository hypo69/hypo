## File: hypotez/src/suppliers/bangood/scenario.py

# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""
.. module: src.suppliers.bangood 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'dev'
  
""" module: src.suppliers.bangood """


"""  Модуль сбора товаров со страницы категорий поставщика bangood.co.il через вебдрайвер
У каждого поставщика свой сценарий обреботки категорий

-Модуль Собирает список категорий со страниц продавца . `get_list_categories_from_site()`
@todo Сделать проверку на изменение категорий на страницах продавца. 
Продавец может добавлять новые категории, переименовывать или удалять/прятать уже существующие. 
По большому счету надо держать таблицу категории `PrestaShop.categories <-> aliexpress.shop.categoies`
- Собирает список товаров со страницы категории `get_list_products_in_category()`
- Итерируясь по списку передает управление в `grab_product_page()` отсылая функции текущий url страницы  
`grab_product_page()` обрабатывает поля товара и передает управление классу `Product` 

"""



from typing import Union
from pathlib import Path

from src import gs
from src.logger import logger

def get_list_products_in_category (s) -> list[str, str, None]:    
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
        s - Supplier
    @returns
        list or one of products urls or None
    """
    d = s.driver
    
    l: dict = s.locators['category']
    
    d.execute_locator (s.locators ['product']['close_banner'] )
    
    if not l:
        """ Много проверок, потому, что код можно запускать от лица разных ихполнителей: Supplier, Product, Scenario """
        logger.error(f"А где локаторы? {l}")
        return
    d.scroll()

    #TODO: Нет листалки

    list_products_in_category = d.execute_locator(l['product_links'])
    """ Собирал ссылки на товары.  """
    
    if not list_products_in_category:
        logger.warning('Нет ссылок на товары. Так бывает')
        return
    
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category

    logger.info(f""" Найдено {len(list_products_in_category)} товаров """)
    

    return list_products_in_category

def get_list_categories_from_site(s):
    ...
```

```
<algorithm>

1. **Input:** Supplier object (s) containing driver and locators.
2. **`get_list_products_in_category(s)`:**
   - Retrieves the driver (d) and locators from the supplier object.
   - Executes a locator to close any banner (if exists).  
   - Checks if the category locators exist. If not, logs an error and returns `None`.
   - Calls `d.scroll()` (implied functionality, probably scrolls the page).
   - Executes a locator to retrieve product links.
   - Checks if product links were found. If not, logs a warning and returns `None`.
   - Handles potential cases where the result is a single string (instead of a list).
   - Logs the number of products found.
   - Returns the list of product URLs.

   *Example:*
   Input `s`: A `Supplier` object with a driver and `locators` dictionary. Output: A list of product URLs (`['url1', 'url2']`).

3. **`get_list_categories_from_site(s)`:** (Placeholder - not implemented yet)

   *Example:* 
   Input `s`: A `Supplier` object with a driver. Output: A list of category URLs


```

```
<explanation>

- **Imports:**
    - `typing`: Provides type hints for better code readability and maintainability.
    - `pathlib`:  Used for working with file paths (though not directly used in this snippet).
    - `src.gs`: This import suggests a custom module (`gs`) within the `src` package. Its purpose is unclear from the given code snippet.
    - `src.logger`: Imports a logging module (likely for error handling and debugging). This module should exist within the `src` package.

- **Classes:** The code defines no classes.

- **Functions:**
    - `get_list_products_in_category(s)`:
        - Takes a `Supplier` object (`s`) as input.
        - Returns a list of product URLs (strings).
        - Uses a driver (`d`) and locators from the `Supplier` object (`s`) to locate product links on a category page.  
        - Implements error handling for missing locators and empty product lists.
        - The function `execute_locator` is presumed to be a method of the driver object, used for locating and potentially retrieving the product link(s). `s.driver` is a reference to the driver.
    - `get_list_categories_from_site(s)`:
       -  Not fully implemented.  Takes a `Supplier` object as input.  Purpose is to fetch a list of category URLs from the web page.

- **Variables:**
    - `MODE`: A string variable with the value 'dev'. Used for configuration, potentially controlling different execution modes (e.g., development, production).
    - `s`: A `Supplier` object, providing data to interact with the web page.
    - `d`: A driver object (likely a web driver).
    - `l`: A dictionary containing locators for elements on a webpage. These could be CSS selectors, XPath expressions, etc., crucial for the driver to locate elements on the page.
    - `list_products_in_category`: A list containing URLs of products.


- **Potential Errors/Improvements:**
    - **Missing implementation:**  `get_list_categories_from_site` is incomplete.
    - **`execute_locator`:**  The `execute_locator` function (likely a method) is crucial and needs to be implemented in the `driver` object for reliable element retrieval.  This code assumes such a method exists.
    - **Error Handling:** The error handling for missing locators is good. Adding checks for potential exceptions (like `NoSuchElementException`) during element retrieval would further improve robustness.
    - **Type checking:**  The function `get_list_products_in_category`'s return type annotation (`list[str, str, None]`) is unusual and probably should be clarified and possibly simplified to just `list[str]`.
    - **Unclear Data Flow:** The exact relationship between `src.gs` and this module isn't apparent.
    - **Missing Class `Supplier`:** The code uses `s.driver` and `s.locators` but lacks the definition of the `Supplier` class.

- **Relationships with Other Parts:**
    - The code strongly relies on the `src` package, and particularly `src.logger` and implicitly a `Supplier` class, which is likely defined within the `src` package or an external library.