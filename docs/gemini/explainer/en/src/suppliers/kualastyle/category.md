## File: hypotez/src/suppliers/kualastyle/category.py

# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.kualastyle
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

""" module: src.suppliers.kualastyle """


"""  Модуль сбора товаров со страницы категорий поставщика hb.co.il через вебдрайвер
У каждого поставщика свой сценарий обреботки категорий

-Модуль Собирает список категорий со страниц продавца . `get_list_categories_from_site()`
@todo Сделать проверку на изменение категорий на страницах продавца. 
Продавец может добавлять новые категории, переименовывать или удалять/прятать уже существующие. 
По большому счету надо держать таблицу категории `PrestaShop.categories <-> aliexpress.shop.categoies`
- Собирает список товаров со страницы категории `get_list_products_in_category()`
- Итерируясь по списку передает управление в `grab_product_page()` отсылая функции текущий url страницы  
`grab_product_page()` обрабатывает поля товара и передает управление классу `Product` 

"""
...

from typing import Dict, List
from pathlib import Path

from src import gs
from src.logger import logger
from src.webdriver import Driver
from src.suppliers import Supplier


def get_list_products_in_category (s: Supplier) -> list[str, str, None]:    
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
        s - Supplier
    @returns
        list or one of products urls or None
    """
    ...
    d:Driver = s.driver
    l: dict = s.locators['category']
    ...
    d.wait(1)
    d.execute_locator (s.locators ['product']['close_banner'] )
    d.scroll()
    ...

    list_products_in_category: List = d.execute_locator(l['product_links'])

    if not list_products_in_category:
        logger.warning('Нет ссылок на товары. Так бывает')
        ...
        return
    ...
    while d.current_url != d.previous_url:
        if paginator(d,l,list_products_in_category):
            list_products_in_category.append(d.execute_locator(l['product_links']))
        else:
            break
        
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category

    logger.debug(f""" Found {len(list_products_in_category)} items in category {s.current_scenario['name']} """)
    
    return list_products_in_category


def paginator(d:Driver, locator: dict, list_products_in_category: list):
    """ Листалка """
    response = d.execute_locator(locator['pagination']['<-'])
    if not response or (isinstance(response, list) and len(response) == 0): 
        ...
        return
    return True


def get_list_categories_from_site(s):
    """ сборщик актуальных категорий с сайта """
    ...

```

```
<algorithm>
1. **Initialization:** The code initializes a Supplier object `s` which likely holds data related to the supplier, including a driver (`s.driver`), locators (`s.locators`), and current scenario.
2. **Get Product Links:** `get_list_products_in_category` fetches a list of product URLs (`list_products_in_category`) from the category page using `d.execute_locator`.
3. **Error Handling:** Checks if the list is empty. If so, logs a warning and returns `None`.
4. **Pagination:** Enters a `while` loop to handle pagination. It calls `paginator` to check if there are more pages.
5. **`paginator` function:** This function attempts to locate and interact with the pagination element (e.g., a previous page button). If found, it appends more product URLs to the list. Returns `True` if more pages, `False` otherwise.
6. **Data Formatting:**  Ensures that the `list_products_in_category` is always a list, not a string, and formats it correctly if necessary.
7. **Logging:** Logs the number of products found for the category.
8. **Return Value:** Returns the list of product URLs.
9. **`get_list_categories_from_site`:** This function is placeholder for the logic to retrieve categories from the website.


**Example Data Flow (get_list_products_in_category):**

```
Supplier Object (s) --> Driver (d) --> Locators (l) --> Product Links (list_products_in_category) --> Logger
                                    |                                |
                                    V                                |
                         Check for pagination --> Paginator --> Driver  --> Product Links (list_products_in_category)
```

```
<explanation>

**Imports:**

- `from typing import Dict, List`:  Specifies the types of variables (`Dict` for dictionaries, `List` for lists) for better code readability and maintainability. This is part of the `typing` module, used for static type checking in Python.
- `from pathlib import Path`: Enables working with file paths. Not directly used in the given code snippet but is a common import for file handling.
- `from src import gs`: Imports the `gs` module from the `src` package. The purpose of `gs` is unclear without further context. It's likely a module for Google Sheets or similar services.
- `from src.logger import logger`: Imports the logger function from the `logger` module within the `src` package. This logger is used for logging messages (errors, warnings, debug).  
- `from src.webdriver import Driver`: Imports the `Driver` class from the `webdriver` module, suggesting interaction with a web driver (like Selenium) for automating browser interactions.
- `from src.suppliers import Supplier`: Imports the `Supplier` class from the `suppliers` module within the `src` package. This class likely represents a supplier (e.g., a specific online store) and encapsulates information and operations related to that supplier.

**Classes:**

- `Driver`: A class representing a web driver.  Methods within this class likely handle interactions with a browser, such as finding elements, waiting for elements, and scrolling.

**Functions:**

- `get_list_products_in_category(s: Supplier) -> list[str, str, None]`: Retrieves a list of product URLs from a category page.
  - **Arguments:** `s`: A `Supplier` object.
  - **Return Value:** A list of product URLs or `None` if no URLs are found. It also checks for pagination and fetches product URLs from each page.
- `paginator(d: Driver, locator: dict, list_products_in_category: list)`: Handles pagination on a category page.
  - **Arguments:** `d`: A `Driver` object. `locator`: A dictionary of locators related to the pagination elements. `list_products_in_category`: The list of product URLs that should be updated.
  - **Return Value:** `True` if more pages are available, `False` otherwise.

**Variables:**

- `MODE = 'dev'`: A global variable that is set to 'dev'.  Is likely used in conditional logic or for configuration purposes.
- `s`: Represents the `Supplier` object that holds data for a particular supplier.
- `d`: Represents the `Driver` object created in the supplier context.


**Potential Errors/Improvements:**

- **Error Handling:** The `get_list_products_in_category` function handles the case where no product links are found, but could benefit from more robust error handling for other potential issues (e.g., website changes breaking locators, timeouts).
- **Type Hinting:** The `...` in the `get_list_products_in_category` function body indicates missing or incomplete code; using type hinting could help in maintaining consistency of the code and ensure that the data received from the website adheres to the expected format.
- **Code Comments:** Some comments are present, but could be more descriptive in terms of error conditions and the specific logic behind the functions.
- **`get_list_categories_from_site`:** This function is not implemented yet.


**Relationships:**

The code interacts with the `src` package, specifically modules like `gs`, `logger`, `webdriver`, and `suppliers`. The `Supplier` class likely interacts with other parts of the project for product processing and data storage.
```