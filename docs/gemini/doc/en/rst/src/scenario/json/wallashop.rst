Wallashop Scenario Configuration
==============================

This file configures a scenario for scraping Walla! Shop. It defines parameters such as the supplier, starting URL, pricing rule, and other settings.

.. automodule:: wallashop
    :members:
    :undoc-members:
    :show-inheritance:


General Configuration
---------------------

~ Supplier Details ~
^^^^^

^ Supplier: ^
```python
def supplier(param: str) -> str:
    """
    Args:
        param (str): The supplier name.

    Returns:
        str: The supplier name.
    """
```

^ Supplier Prefix: ^
```python
def supplier_prefix(param: str) -> str:
    """
    Args:
        param (str): The supplier prefix.

    Returns:
        str: The supplier prefix.
    """
```

^ Start URL: ^
```python
def start_url(param: str) -> str:
    """
    Args:
        param (str): The starting URL for scraping.

    Returns:
        str: The starting URL.
    """
```

~ Pricing Rule ~
^^^^^

^ Price Rule: ^
```python
def price_rule(param: str) -> str:
    """
    Args:
        param (str): The price rule to apply.

    Returns:
        str: The price rule.
    """
```

~ Inventory Management ~
^^^^^

^ Number of Items for Flush: ^
```python
def num_items_4_flush(param: int) -> int:
    """
    Args:
        param (int): The number of items to flush.

    Returns:
        int: The number of items to flush.
    """
```

~ Authentication and Collection ~
^^^^^

^ Login Required: ^
```python
def if_login(param: bool) -> bool:
    """
    Args:
        param (bool): Whether login is required.

    Returns:
        bool: Whether login is required.
    """
```

^ Collect Products from Category Page: ^
```python
def collect_products_from_categorypage(param: bool) -> bool:
    """
    Args:
        param (bool): Whether to collect products from category pages.

    Returns:
        bool: Whether to collect products from category pages.
    """
```

~ Scraping Method ~
^^^^^

^ Scraping Method: ^
```python
def parcing_method(param: str) -> str:
    """
    Args:
        param (str): The scraping method (webdriver or api).

    Returns:
        str: The scraping method.
    """
```

^ Scraping Method Details (Web): ^
```python
def about_method_web_scrapping(param: str) -> str:
    """
    Args:
        param (str): The description of the web scraping method.

    Returns:
        str: The description of the web scraping method.
    """
```

~ Scenarios ~
^^^^^

^ Scenarios: ^
```python
def scenarios(param: dict) -> dict:
    """
    Args:
        param (dict): The scenarios configuration.

    Returns:
        dict: The scenarios configuration.
    """
```