## \file ../src/suppliers/ivory/graber.py
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

supplier_prefix: str = 'ivory'
# Определение декоратора для закрытия всплывающих окон
def close_popup(value: Any = None) -> Callable:
    """Creates a decorator to close pop-ups before executing the main function logic.

    Args:
        d Driver: Driver instance to use for closing the pop-up.
        l SimpleNamespace: Namespace with locators.

    Returns:
        Callable: The decorator wrapping the function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                # await d.execute_locator(l.close_popup)  # Await async pop-up close
                ...
            except ExecuteLocatorException as e:
                logger.debug(f"Error executing locator: {e}")
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator

@dataclass
class Graber(Grbr):
    """Graber class for specific grabbing operations."""
    

    def __init__(self):
        super().__init__(supplier_prefix or self.supplier_prefix)

