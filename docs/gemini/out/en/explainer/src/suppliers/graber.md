# Code Explanation for hypotez/src/suppliers/graber.py

## <input code>

```python
## \file hypotez/src/suppliers/graber.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers 
	:platform: Windows, Unix
	:synopsis:  Базовый класс сбора данных со старницы HTML поставщиков.
    Целевые поля страницы (`название`,`описание`,`спецификация`,`артикул`,`цена`,...) собирает вебдрйвер (class: [`Driver`](../webdriver))
    Местополжение поля определяется его локатором. Локаторы хранятся в словарях JSON в директории `locators` каждого поставщика.
    ([подробно о локаторах](locators.ru.md))


## Для нестендартной обработки полей товара просто переопределите функцию в своем классе.
Пример:
```python
s = `suppler_prefix`
from src.suppliers imoprt Graber
locator = j_loads(gs.path.src.suppliers / f{s} / 'locators' / 'product.json`)

class G(Graber):

    @close_pop_up()
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
from src.utils.image import save_png_from_url, save_png
from src.utils.string.normalizer import normalize_string, normalize_int, normalize_float, normalize_boolean
from src.logger.exceptions import ExecuteLocatorException
from src.endpoints.prestashop import PrestaShop
from src.utils import pprint
from src.logger import logger

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
                    ... 
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
        self.l = self.locator
        self.driver: Driver = driver
        self.d = self.driver
        self.fields: ProductFields = ProductFields()
        Context.driver = self.driver
        Context.supplier_prefix = supplier_prefix


# ... (rest of the code)
```

## <algorithm>

**Workflow Diagram:**

1. **Initialization (Graber.__init__):**
   - Takes `supplier_prefix` and `driver` as input.
   - Loads locators from `product.json` using `j_loads_ns`.
   - Initializes `ProductFields` instance.
   - Sets `Context.driver` and `Context.supplier_prefix`.
   - Example: `graber = Graber("supplierA", driver_instance)`

2. **Data Fetching (various methods):**
   - Each method (e.g., `name`, `price`) attempts to fetch data using `await self.d.execute_locator(self.l.field_locator)`.
   - Error handling is implemented with `try...except` blocks for `ExecuteLocatorException`.
   - Example: `await graber.name()` fetches product name.

3. **Data Validation:**
   - Checks if the fetched `value` is valid.
   - Example: Checks for empty strings, empty lists, etc.

4. **Data Normalization and Storage:**
   - Applies necessary normalizations (e.g., `normalize_string`).
   - Stores the fetched and validated `value` into the appropriate `ProductFields` attribute.
   - Example: `self.fields.name = value`.

5. **Data Aggregation (graber.grab_page):**
   - Calls multiple methods to fetch product fields in a structured manner.
   - Returns the populated `ProductFields` object.


## <mermaid>

```mermaid
graph TD
    subgraph Initialization
        A[Graber.__init__(supplier_prefix, driver)] --> B{Load locators};
        B --> C[Initialize ProductFields];
        C --> D[Set Context.driver & Context.supplier_prefix];
    end
    subgraph Data Fetching
        E[async name()] --> F[execute_locator(name locator)];
        F --Success--> G[Normalize String];
        G --> H[Store in ProductFields];
    
        E[async price()] --> F[execute_locator(price locator)];
        F --Success--> G[Normalize Numeric];
        G --> H[Store in ProductFields];
    
        ...other methods like description, etc...
    end
    subgraph Data Aggregation
        I[grab_page()] --> J[Call name(), price(), ...];
        J --> K[Return ProductFields object];
    end

```

**Dependencies Analysis:**

- `asyncio`: For asynchronous operations.
- `pathlib`: For working with file paths.
- `typing`: For type hinting.
- `functools`: For the `wraps` decorator.
- `langdetect`: Detects language from text.
- `header`: Likely handles header-related tasks for the web requests.
- `gs`: Likely a custom module for global settings or utilities.
- `ProductFields`: Stores product data, located in `src.product.product_fields`.
- `Category`: (Likely) Handles product categories.
- `Driver`: Handles web driver interactions, located in `src.webdriver`.
- `jjson`: For loading and saving JSON data.
- `image`: For saving images.
- `normalizer`: For normalizing data.
- `logger`: For logging errors/messages.
- `endpoints.prestashop`: Likely handles PrestaShop-specific endpoint logic.
- `utils`: Likely contains other utility functions.


## <explanation>

- **Imports:** The code imports various modules, including `asyncio` for asynchronous operations, `pathlib` for file paths, `typing` for type hinting, and `langdetect` for language detection.  Crucially, it imports `Driver` from `src.webdriver`, `ProductFields` from `src.product.product_fields`, `j_loads/j_loads_ns` from `src.utils.jjson`, `save_png_from_url` from `src.utils.image` indicating a modular structure for different functionalities (`src` likely denotes a source/main application package).

- **Classes:**
    - `Graber`: The base class for fetching product data from supplier pages.  It takes a `supplier_prefix` and a `driver` instance in its constructor.  It stores locators from `product.json` and manages data via methods to fetch and store values in `ProductFields`. It handles errors using `logger` and `error` method.
    - `Context`: A class for storing global configuration like the `driver` instance and supplier prefix, enhancing reusability and reducing global variables.


- **Functions:** The numerous `async def` functions (e.g., `name`, `price`, `description`) are responsible for fetching specific product details.  Each one takes optional `value` to allow overriding the fetched value if provided from calling code. They call `d.execute_locator` to fetch data based on stored locator information.  The `close_pop_up` decorator is crucial, ensuring a standardized pop-up closure before running the main fetching logic within each function.

- **Variables:**
    - `self.supplier_prefix`: The prefix for a particular supplier.
    - `self.locator`: Holds the locators loaded from `product.json`.
    - `self.fields`: An instance of `ProductFields` containing all collected product details.
    - `Context.driver`:  A shared `Driver` instance used by Graber instances.
    - `Context.locator_for_decorator`: A decorator to handle pop-up closures.

- **Potential Errors and Improvements:**
    - The code relies heavily on the `execute_locator` function of the `driver` object. Missing error handling within the `execute_locator` function itself can lead to silent failures.
    - The `id_product` method has a potential bug, directly embedding the `supplier_prefix` in the product ID which could cause conflicts in database or further processing. This should be handled in a more configurable way.
    - Some methods like `additional_shipping_cost` repeat a lot of error handling and debug logging.  Consider creating a more robust `fetch_and_normalize_field` function to reduce code duplication.

**Chain of Relationships:**

- `Graber` relies on `Driver` to interact with the web page.
- `Graber` utilizes `ProductFields` to store the fetched product data.
- The methods within `Graber` depend on the correct structure of the `locators` file for each supplier.
- `Graber` uses `j_loads/j_loads_ns` and potentially other functions in `src.utils` and `gs`.
- The overall system depends on proper web scraping functionality in `Driver`,  JSON parsing in `src.utils.jjson`, and robust logging system in `src.logger`. The relationships are interconnected to work together to extract and organize product data in a structured format.