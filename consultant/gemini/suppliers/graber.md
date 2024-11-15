## \file hypotez/consultant/gemini/suppliers/graber.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.suppliers """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.suppliers """
""" Базовый класс сбора данных со старницы для всех поставщиков
"""

import os
import sys
import asyncio
from pathlib import Path
from typing import Any, Callable
from langdetect import detect
from functools import wraps

from __init__ import gs
from src.suppliers.locator import Locator
from src.product.product_fields import ProductFields
from src.category import Category
from src.webdriver import Driver
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png_from_url
from src.utils import pprint
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException
from src.endpoints.prestashop import Prestashop

# Use a global variable for Driver and Locator; important!
d: Driver = None
l: Locator = None


def close_popup(value: Any = None) -> Callable:
    """Creates a decorator to close pop-ups before executing the main function logic.

    Args:
        value (Any): Optional value passed to the decorator.

    Returns:
        Callable: The decorator wrapping the function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                if d and l and hasattr(l, "close_popup"):  # Crucial check!
                    await d.execute_locator(l.close_popup)
            except ExecuteLocatorException as e:
                logger.debug(f"Error executing locator: {e}")
            return await func(*args, **kwargs)
        return wrapper
    return decorator


class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""
    
    def __init__(self, supplier_prefix: str, locator: Locator, driver: Driver):
        """Инициализация класса Graber.

        Args:
            supplier_prefix (str): Префикс поставщика.
            locator (Locator): Экземпляр класса Locator.
            driver (Driver): Экземпляр класса Driver.
        """
        self.supplier_prefix = supplier_prefix
        global l, d
        l = locator
        d = driver
        self.fields = ProductFields()

    async def error(self, field: str):
        """Обработчик ошибок для полей."""
        logger.debug(f"Ошибка заполнения поля {field}")
        # Important:  Returning None or something similar here is vital
        return None


    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = ''
    ) -> Any:
        """Универсальная функция для установки значений полей с обработкой ошибок.
        """
        try:
            locator_result = await asyncio.to_thread(locator_func)
            return value if value else locator_result if locator_result else default
        except Exception as e:
            logger.error(f"Error in set_field_value for {field_name}: {e}")
            await self.error(field_name)  # Log the error and return default
            return default


    # ... (rest of your code)


    # ... other methods ...

    @close_popup()
    async def local_saved_image(self, value: Any = None):
        if not d or not l or not hasattr(l, "default_image_url"):
            logger.error("Driver or locator not properly initialized.")
            return None  # Important: return None on error
        try:
            self.fields.local_saved_image = save_png_from_url(
                d.execute_locator(l.default_image_url), self.fields.id_product
            )
        except Exception as e:
            logger.error(f"Error saving image: {e}")
            return None  # Return None to signal error

    # ...


```

**Key Improvements and Explanations:**

* **Global `d` and `l` variables:**  Crucially, these are _global_ variables and will work as expected because they're defined at the module scope.  This is critical if they are used across methods within your script.
* **Driver and Locator Check:** Added `if d and l` and checks for `hasattr(l, "close_popup")` to avoid `AttributeError` exceptions.  This is a *very* important defensive programming practice.
* **Error Handling in `set_field_value`:** The `try...except` block in `set_field_value` catches any exceptions that might arise during the asynchronous operation and logs the error.  This is vital to prevent your script from crashing.  Now, it returns `default` in case of errors, avoiding a potential crash.
* **Error Handling in `local_saved_image`:** Similar error handling for `local_saved_image` is included. Now it returns `None` on errors.


* **Return `None` on Error:**  All methods should return a meaningful value, even in case of errors (e.g., `None`, an empty string, a specific error code). This is essential for proper error handling in your calling code.


**How to use:**

```python
import asyncio
# ... import your other modules ...
from your_module import Graber, Locator, Driver


async def main():
  # Initialize your driver and locator
  driver = Driver() # Replace with your actual driver initialization
  locator = Locator(driver) # Replace with your actual locator initialization
  graber = Graber("myprefix", locator, driver)
  # ... (code to fetch the product page URL etc.) ...
  product_url = "your_product_url"
  try:
    await driver.open_url(product_url)
    products_data = await graber.grab_page()  # Run the grab_page function
    if products_data:  # Important: check for error conditions
       print(products_data.fields)
  except Exception as e:
    print(f"An error occurred: {e}")


if __name__ == "__main__":
  asyncio.run(main())
```


This revised code is more robust and reliable, handling potential errors and ensuring that functions return predictable values.  Remember to replace placeholders like `"your_product_url"` with your actual values. This is crucial for production-ready code.  Critically, make sure your `Locator` and `Driver` classes are properly initialized and that the locators themselves are valid.