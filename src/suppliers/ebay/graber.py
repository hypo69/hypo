## \file ../src/suppliers/ebay/graber.py
## \file ../src/suppliers/ebay/graber.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


import asyncio
from pathlib import Path
from typing import Any, Callable, Optional
from dataclasses import dataclass, field
from functools import wraps

from src import gs
from src.suppliers import Graber as Grbr
from src.product import ProductFields
from src.webdriver import Driver
from src.utils.jjson import j_loads_ns
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException

@dataclass
class Graber(Grbr):
    """Graber class for specific grabbing operations."""
    supplier_prefix: str = 'ebay'

    def __init__(self, supplier_prefix: Optional[str] = None):
        super().__init__(supplier_prefix or self.supplier_prefix)

    def close_popup(self, value: Any = None) -> Callable:
        """Decorator to call `self.driver.execute_locator` before the actual function logic."""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def wrapper(*args, **kwargs):
                try:
                    await self.driver.execute_locator(self.l.close_popup)  # Await for async function
                except ExecuteLocatorException as e:
                    logger.debug(f"Ошибка выполнения локатора: {e}")
                return await func(*args, **kwargs)  # Await the original function call
            return wrapper
        return decorator
