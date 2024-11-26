## File hypotez/src/suppliers/graber.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""
.. module: src.suppliers 
	:platform: Windows, Unix
	:synopsis:  Базовый класс сбора данных со старницы для всех поставщиков.
    асинхронно собирает значения полей или выполняет действие на целевой HTML странице. 
    
\n## Для нестендартной обработки полей товара просто переопределите функцию в своем классе.
Пример:
```python
s = `suppler_prefix`
from src.suppliers imoprt Graber
locator = j_loads(gs.path.src.suppliers / f{s} / \'locators\' / \'product.json`
\nclass G(Graber):
\n    @close_pop_up()
    async def name(self, value: Any = None):
        self.fields.name = <Ваша реализация>
        )
```

"""
MODE = 'dev'


import os
import sys
import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable
from langdetect import detect
from functools import wraps

import header
from src import gs

from src.product.product_fields import ProductFields
from src.category import Category
from src.webdriver import Driver
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png_from_url
from src.utils import pprint
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException
from src.endpoints.prestashop import PrestaShop


# Глобальные настройки через объект `Context`
class Context:
    """
    Класс для хранения глобальных настроек.

    :ivar driver: Объект драйвера, используется для управления браузером или другим интерфейсом.
    :vartype driver: Driver
    :ivar locator: Пространство имен для хранения локаторов.
    :vartype locator: SimpleNamespace
    :ivar supplier_prefix: Префикс поставщика.
    :vartype supplier_prefix: str
    """

    # Атрибуты класса
    driver: Driver = None
    locator_for_decorator: SimpleNamespace = None  # <- Если будет установлен - выполнится декоратор `@close_pop_up`. Устанавливается при инициализации поставщика, например: `Context.locator = self.locator.close_pop_up`
    supplier_prefix: str = None


# Определение декоратора для закрытия всплывающих окон
# В каждом отдельном поставщике (`Supplier`) декоратор может использоваться в индивидуальных целях
# Общее название декоратора `@close_pop_up` можно изменить 
# Если декоратор не используется в поставщике - поставь 
def close_pop_up(value: Any = None) -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    Args:
        value (Any): Дополнительное значение для декоратора.

    Returns:
        Callable: Декоратор, оборачивающий функцию.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if Context.locator_for_decorator:
                try:
                    await Context.driver.execute_locator(Context.locator_for_decorator)  # Await async pop-up close  
                    # ... (Potential pop-up handling code)
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', ex)
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator


class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""

    def __init__(self, supplier_prefix: str, driver: Driver):
        """Инициализация класса Graber.

        Args:
            supplier_prefix (str): Префикс поставщика.
            locator (Locator): Экземпляр класса Locator.
            driver (Driver): Экземпляр класса Driver.
        """
        self.supplier_prefix = supplier_prefix
        self.locator: SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
        self.l = self.locator  # Alias for shorter use
        self.driver: Driver = driver
        self.d = self.driver  # Alias for shorter use
        self.fields: ProductFields = ProductFields()
        Context.driver = self.driver
        Context.supplier_prefix = supplier_prefix


    # ... (many methods for fetching product data using execute_locator)

```

```
<algorithm>
1. **Initialization (Graber.__init__):**
   - Takes `supplier_prefix` (string) and `driver` (Driver object) as input.
   - Loads locators from `product.json` using `j_loads_ns`  from `src.utils.jjson`.
   - Initializes `ProductFields` object.
   - Sets `Context.driver` and `Context.supplier_prefix`.
   - Example: `graber = Graber("example_supplier", driver_instance)`

2. **Data Fetching (Various methods):**
   - Each method (e.g., `name`, `price`, `description`) takes an optional `value` argument. If provided, it's used directly; otherwise, it uses `self.driver.execute_locator` to retrieve data from the page using the corresponding locator from `self.locator`.  
   -  Error handling with `try...except` is included, and logging is implemented using `logger` (likely from `src.logger`).
   - Example: `await graber.name(value="Example Name")` or `await graber.name()`.

3. **Data Validation:**
   - Checks if the fetched `value` is valid. If not, logs a debug message and returns a default value.
   - Example: `if not value: ... return default`

4. **Data Storage:**
   - Stores the fetched `value` in the corresponding attribute of `self.fields` (a `ProductFields` object).
   - Example: `self.fields.name = value`


5. **Field Error Handling (error):**
   - Handles errors during data retrieval.
   - Example: `await graber.error("name")`  if retrieval fails.


6. **Data Collection (grab_page):**
   - Calls other methods to fetch individual product data points.
   - Fetches data based on keywords (e.g., id_product).
   - Returns `self.fields` containing the collected data.
   - Example: `product_data = await graber.grab_page(id_product="123")`


```

```
<explanation>
- **Imports:** The imports define the modules and classes used in the `Graber` class.
    - `asyncio`, `os`, `sys`, `pathlib`: standard python libraries for asynchronous operations, operating system interaction, system related issues, and path handling.
    - `types`: for creating SimpleNamespace.
    - `typing`, `Callable`, `Any`: for type hinting in function definitions.
    - `langdetect`: for language detection.
    - `functools.wraps`: for preserving metadata of the decorated function.
    - `header`: likely a custom module for handling headers (unclear purpose without seeing the code).
    - `gs`: likely a global settings module.
    - `ProductFields`, `Category`, `Driver`: custom classes from `src` for representing product fields, categories, and webdriver interactions, respectively.
    - `j_loads`, `j_loads_ns`, `j_dumps`: for loading and dumping JSON data, potentially from `src.utils.jjson`.
    - `save_png_from_url`, `pprint`: custom functions for handling images (likely from `src.utils.image`) and pretty printing (likely from `src.utils`).
    - `logger`: a logging module for error and debug messages (from `src.logger`).
    - `ExecuteLocatorException`: custom exception for errors during locator execution.
    - `PrestaShop`: class likely for interacting with PrestaShop (a specific e-commerce platform).

- **Classes:**
    - `Context`:  A singleton class to store global context. Holds the `driver` instance,  `locator_for_decorator`, and `supplier_prefix` to manage driver and locator-related activities across multiple Graber instances.  Crucial for the pop-up handling mechanism. This approach avoids having to pass the driver to every method in `Graber`.

    - `Graber`: The base class for scraping data from webpages. It handles the initialization, error handling, and data collection using  `execute_locator` calls to a `driver` object. Each method related to fetching product data is decorated with `@close_pop_up`.  Contains methods for fetching various product fields, such as `name`, `price`, etc., and `grab_page` to collect all the data.

- **Functions:**
    - `close_pop_up`: Creates a decorator to close pop-up windows that might appear before a function is executed (to make the data extraction more stable) using the `execute_locator`.
        -  It's crucial for preventing pop-ups from interfering with scraping. 

- **Variables:**
    - `MODE`: A string variable likely used for defining environments (dev, prod, etc.).
    - `self.supplier_prefix`, `self.locator`: These variables help to manage the data associated with a particular supplier.

- **Potential Errors and Improvements:**
    - The code uses many `...` to indicate sections that need more detailed handling. This makes the code difficult to reason about in isolation.
    - A lot of repeated error handling (`try...except`, `if not value`, etc.) is present. Consider a better way to prevent the spread of logic throughout methods. 
    - The `grab_page` function is currently missing the function `fetch_specific_data`.  It's crucial to implement this function to fetch particular data.
    - The method `additional_categories` is questionable. A function for handling list/dict mapping should exist to avoid redundant logic.

- **Relationship Chain:** The code relies on several other parts of the project, including `gs` (likely for global settings), `src.product.product_fields` for product field representation, `src.webdriver` for web driver interaction, `src.utils` for various utilities (image handling, JSON, etc.), `src.logger` for logging.  A strong dependency on `src.suppliers` exists through the `locator` objects.