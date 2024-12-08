# amazon/scenario.py

## Overview

This module defines the scenario for collecting product data from Amazon category pages.  It outlines the steps for retrieving a list of categories, products within those categories, and ultimately processing individual product pages.  The module leverages a web driver (`driver`) and locators (`locators`) for interacting with the Amazon website.  Critical functionalities include `get_list_products_in_category` for extracting product URLs from category pages and supporting asynchronous processing.  The module also demonstrates handling potential errors and logging informative messages.


## Functions

### `get_list_products_in_category`

**Description**: Retrieves a list of product URLs from a given category page on Amazon.  It interacts with the web driver (`driver`) to locate and collect product links, handling potential errors and logging progress.


**Parameters**:

- `s` (Supplier): An instance of the Supplier class, representing the current supplier and containing necessary data.


**Returns**:

- `list[str, str, None]`: A list of product URLs if successful, or `None` if no product URLs are found or an error occurs during the process.  May return a list with a single string if only one product link is found


**Raises**:

- `NoneType`: If the locators for product links are not found or if no product links are present on the page.


```
```python
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
    #    _asin = asin.split(f'//')[0][-2]
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


## Module-Level Constants

### `MODE`

**Description**: Defines the operating mode for the module. Currently set to 'dev'.  This constant can be used to control the behavior of the module in different environments.

```python
MODE = 'dev'
```


```