# Code Explanation: hypotez/src/suppliers/amazon/scenario.py

## <input code>

```python
## \file hypotez/src/suppliers/amazon/scenario.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.amazon 
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
  
""" module: src.suppliers.amazon """


"""  Модуль сбора товаров со страницы категорий поставщика aliexpress.com через вебдрайвер

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

def get_list_products_in_category(s) -> list[str,str,None]:    
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
    @param s: Supplier - Supplier intstance
    @returns list or one of products urls or None
    """
    d = s.driver
    l: dict = s.locators['category']
    if not l:
        """ Много проверок, потому, что код можно запускать от лица разных ихполнителей: Supplier, Product, Scenario """
        logger.error(f"А где локаторы? {l}")
        return
    d.scroll()

    #TODO: Нет листалки

    list_products_in_category = d.execute_locator(l['product_links'])
    """ Собираю ссылки на товары.  """
    if not list_products_in_category:
        logger.warning('Нет ссылок на товары')
        return
    
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category


    logger.info(f""" Найдено {len(list_products_in_category)} товаров """)
    
    #""" Проверяю наличие товара в базе данных магазина """
    #for asin in list_products_in_category:
    #    _asin = asin.split(f'/')[-2]
    #    _sku = f'{s.supplier_id}_{_asin}' 
    #    if PrestaShopProduct.check(_sku) == False:
    #        """ Синтаксис для того, чтобы помнить,
    #        что я проверяю ОТСУТСТВИЕ товара в базе данных
    #        """
    #        continue
    #    else:
    #        """ Товар в базе данных """
    #        continue
                #TODO: Логику 


    return list_products_in_category
```

## <algorithm>

```mermaid
graph TD
    A[get_list_products_in_category(s)] --> B{Check locators};
    B -- Yes --> C[d.scroll()];
    B -- No --> D[logger.error];
    C --> E[execute_locator(l['product_links'])];
    E --> F{Check list_products_in_category};
    F -- Yes --> G[logger.info];
    F -- No --> H[logger.warning];
    G --> I[return list_products_in_category];
    H --> I;
    D --> I;
```

**Explanation:** The function `get_list_products_in_category` retrieves product URLs from a category page.  It first checks for the presence of locators (`s.locators['category']`). If locators exist, it scrolls the page and then retrieves product links using `d.execute_locator(l['product_links'])`.  It validates whether the retrieved links are empty, then logs success or warnings accordingly. Finally, it returns the list of product URLs.


## <mermaid>

```mermaid
graph LR
    subgraph Imports
        src --> gs
        src --> logger
    end
    subgraph Functions
        "get_list_products_in_category" --> "execute_locator";
        "execute_locator" --> logger;
        "get_list_products_in_category" --> logger;
    end
    subgraph Classes
        Supplier --> driver
        Supplier --> locators
    end

    logger -- logs --> console
    gs -- data access --> database
    
    Supplier -- data --> get_list_products_in_category
    get_list_products_in_category -- links --> PrestaShopProduct(Implicit)
```

**Explanation:** This diagram illustrates the code's dependencies. `src.gs` and `src.logger` are imported, suggesting a relationship with other parts of the project handling database interactions and logging, respectively. The diagram also visualizes the function `get_list_products_in_category` interacting with a `Supplier` object. The `Supplier` class possesses a `driver` (presumably a WebDriver instance for web interaction) and `locators` for locating elements on webpages, which are critical for the function's operation. Implicit dependency on `PrestaShopProduct` class is shown for database checks.


## <explanation>

**Imports:**

- `from typing import Union`: Used for type hinting.
- `from pathlib import Path`: Used for working with file paths (not used in this function).
- `from src import gs`: Imports the `gs` module from the `src` package, likely for database interaction or general helper functions.
- `from src.logger import logger`: Imports the `logger` object from the `src.logger` module, for logging messages.  This module is fundamental to the code for monitoring and debugging.

**Classes:**

- `Supplier`:  Implied as the input (`s`) to the function. It contains attributes `driver` (for web interaction) and `locators` (for locating elements on web pages).  The `Supplier` class is presumably defined elsewhere in the project and is crucial for this function's operation.

**Functions:**

- `get_list_products_in_category(s)`: Takes a `Supplier` object (`s`) as input.  It attempts to retrieve product URLs from a category page via locators. Returns a list of product URLs or `None` if no links are found. This function is the core of the script, handling the retrieval of product links.

**Variables:**

- `MODE`: A global variable set to `'dev'`. This probably controls some configurations or modes (like development versus production).
- `d`: Represents the WebDriver instance, used for interacting with the web page.
- `l`: Stores the locators dictionary obtained from the `Supplier` object.
- `list_products_in_category`: Holds the retrieved URLs of the products.


**Potential Errors/Improvements:**

- **Hardcoded paths/config:** The use of `! venv/Scripts/python.exe` and `#! venv/bin/python/python3.12` is unconventional. These lines are likely interpreted by an IDE or shell to tell it which Python interpreter to use. This is a reasonable practice, but consider configuration files instead of hardcoding these directly in the script.
- **Missing error handling:** The function has basic error handling for missing locators and empty result sets. However, more robust checks are needed for handling other potential errors during web interactions or database lookups.
- **Lack of pagination:** The code lacks the functionality to handle pagination if there are multiple pages of products. The `TODO` comment highlights the need for pagination logic (handling scrolling and more URLs).
- **Missing database integration:** The commented-out code suggests a database lookup to check if a product already exists. Implement this database integration.
- **Type Hinting:** Improve type hinting; the type signature `-> list[str,str,None]` is unusual.  Perhaps it should be something like `-> list[str]`.


**Relationships:**

This script interacts with various parts of the project, primarily through the `Supplier`, `driver`, `locators`, and the database lookup (`PrestaShopProduct` class). This script depends on `gs` for database access and `logger` for logging. The `PrestaShopProduct` class, which handles checking for product existence, is a crucial part of the workflow. A more detailed understanding of the `Supplier` and `Product` classes would be necessary for a more comprehensive analysis of relationships.