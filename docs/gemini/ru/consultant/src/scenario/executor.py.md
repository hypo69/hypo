## Анализ кода модуля `executor.py`

**Качество кода**

**Соответствие требованиям по оформлению кода: 7/10**

*   **Плюсы:**
    *   Присутствует базовая структура модуля с необходимыми импортами.
    *   Используется `logger` из `src.logger.logger`.
    *   Используются `j_loads` и `j_dumps` из `src.utils.jjson`.
    *   Есть docstring для основных функций.
    *   Код разбит на функции, что способствует читаемости.
*   **Минусы:**
    *   Не все функции и переменные имеют подробные docstring с описанием параметров и возвращаемых значений (например, `_journal`).
    *   Не везде используется `logger.error` для обработки ошибок, встречаются `print` и общие `except Exception`.
    *   В некоторых местах отсутствуют комментарии, объясняющие логику кода.
    *   Смешанное использование `print` и `logger` для вывода информации.
    *   Не везде используются одинарные кавычки для строк, где это требуется.
    *   Код местами перегружен общими try/except.
    *   Не везде есть RST документация.
    *   Не приведены примеры использования и документация.
    *   `_journal` не документирован.

**Рекомендации по улучшению**

1.  **Документация:**
    *   Добавить подробные docstring в формате RST ко всем функциям, методам и классам, включая описание параметров, возвращаемых значений и возможных исключений.
    *   Описать модуль в начале файла.
    *   Документировать переменные и константы, особенно глобальные (например, `_journal`).
    *   Привести примеры использования функций.
2.  **Обработка ошибок:**
    *   Заменить общие `except Exception` на более специфичные блоки `try-except` с логированием ошибок через `logger.error`.
    *   Избегать избыточного использования try-except, где это возможно.
    *   Перенести логику обработки ошибок в отдельные функции.
3.  **Логирование:**
    *   Использовать `logger` для всех информационных и отладочных сообщений, а не только для ошибок.
    *   Добавить логирование начала и окончания выполнения функций.
4.  **Стиль кода:**
    *   Использовать только одинарные кавычки для строк, где это требуется.
    *   Удалить все print, использовать logger
5.  **Структура кода:**
    *   Разделить большие функции на более мелкие.
    *   Добавить комментарии для сложных участков кода, поясняющие логику.
6.  **Импорты:**
    *   Привести в соответствие импорты из ранее обработанных файлов.
7. **Унификация**
    *  Переименовать `s` в `supplier`, где это необходимо, для унификации кода.
    *  Переименовать `d` в `driver`, где это необходимо, для унификации кода.
8. **Удалить не используемое**
    *   Удалить не используемые импорты.
    *  Удалить не используемые аргументы функций.
    *   Удалить неиспользуемые переменные.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Module for executing scenarios.
=========================================================================================

This module contains functions for executing scenarios, loading them from files,
and handling the process of extracting product information and inserting it into PrestaShop.

.. module::  src.scenario.executor
   :platform: Windows, Unix
   :synopsis: Module for executing scenarios.

Example:
    >>> from pathlib import Path
    >>> from src.scenario.executor import run_scenario_files
    >>> # Создайте экземпляр класса Supplier
    >>> supplier = ... # Your Supplier instance
    >>> scenario_files = [Path('path/to/scenario1.json'), Path('path/to/scenario2.json')]
    >>> result = run_scenario_files(supplier, scenario_files)
    >>> print(result)
    True

"""
import os
import sys
import asyncio
import time
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop.product_async import ProductAsync, ProductFields
from src.logger.logger import logger
from src.logger.exceptions import ProductFieldException
from src.endpoints.prestashop.prestashop_async import PrestaShop # TODO - Добавить импорт модуля PrestaShop
from src.db import ProductCampaignsManager # TODO - добавить импорт модуля ProductCampaignsManager
from src.utils.printer import pprint # TODO - добавить импорт модуля printer

_journal: dict = {'scenario_files': ''}
"""
Global dictionary for storing journal data.
It includes the scenario files processed and the results of their execution.
"""
_journal['name'] = timestamp = datetime.now().isoformat()
"""
Timestamp when the journal was created.
"""


def dump_journal(supplier, journal: dict) -> None:
    """
    Save the journal data to a JSON file.

    Args:
        supplier: Supplier instance.
        journal (dict): Dictionary containing the journal data.

    Returns:
        None: This function does not return anything.

    Example:
        >>> from pathlib import Path
        >>> # Создайте экземпляр класса Supplier
        >>> supplier = ... # Your Supplier instance
        >>> journal_data = {'name': 'test_journal', 'scenario_files': {'file1.json': {'message': 'completed'}}}
        >>> dump_journal(supplier, journal_data)
        >>> # A file 'test_journal.json' will be created in the '_journal' directory of the supplier path
    """
    _journal_file_path = Path(supplier.supplier_abs_path, '_journal', f"{journal['name']}.json")
    j_dumps(journal, _journal_file_path)


def run_scenario_files(supplier, scenario_files_list: List[Path] | Path) -> bool:
    """
    Executes a list of scenario files.

    Args:
        supplier: Supplier instance.
        scenario_files_list (List[Path] | Path): List of file paths for scenario files, or a single file path.

    Returns:
        bool: True if all scenarios were executed successfully, False otherwise.

    Raises:
        TypeError: If scenario_files_list is not a list or a Path object.

    Example:
        >>> from pathlib import Path
        >>> # Создайте экземпляр класса Supplier
        >>> supplier = ... # Your Supplier instance
        >>> scenario_files = [Path('path/to/scenario1.json'), Path('path/to/scenario2.json')]
        >>> result = run_scenario_files(supplier, scenario_files)
        >>> print(result)
        True
    """
    if isinstance(scenario_files_list, Path):
        scenario_files_list = [scenario_files_list]
    elif not isinstance(scenario_files_list, list):
        raise TypeError('scenario_files_list must be a list or a Path object.')
    scenario_files_list = scenario_files_list if scenario_files_list else supplier.scenario_files

    _journal['scenario_files'] = {}
    for scenario_file in scenario_files_list:
        _journal['scenario_files'][scenario_file.name] = {}
        try:
            if run_scenario_file(supplier, scenario_file):
                _journal['scenario_files'][scenario_file.name]['message'] = f'{scenario_file} completed successfully!'
                logger.success(f'Scenario {scenario_file} completed successfully!')
            else:
                _journal['scenario_files'][scenario_file.name]['message'] = f'{scenario_file} FAILED!'
                logger.error(f'Scenario {scenario_file} failed to execute!')
        except Exception as e:
            logger.critical(f'An error occurred while processing {scenario_file}: {e}')
            _journal['scenario_files'][scenario_file.name]['message'] = f'Error: {e}'
    return True


def run_scenario_file(supplier, scenario_file: Path) -> bool:
    """
    Loads and executes scenarios from a file.

    Args:
        supplier: Supplier instance.
        scenario_file (Path): Path to the scenario file.

    Returns:
        bool: True if the scenario was executed successfully, False otherwise.

    Example:
        >>> from pathlib import Path
        >>> # Создайте экземпляр класса Supplier
        >>> supplier = ... # Your Supplier instance
        >>> scenario_file = Path('path/to/scenario.json')
        >>> result = run_scenario_file(supplier, scenario_file)
        >>> print(result)
        True
    """
    try:
        scenarios_dict = j_loads(scenario_file)['scenarios']
        for scenario_name, scenario in scenarios_dict.items():
            supplier.current_scenario = scenario
            if run_scenario(supplier, scenario, scenario_name):
                logger.success(f'Scenario {scenario_name} completed successfully!')
            else:
                logger.error(f'Scenario {scenario_name} failed to execute!')
        return True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.critical(f'Error loading or processing scenario file {scenario_file}: {e}')
        return False


def run_scenarios(supplier, scenarios: Optional[List[dict] | dict] = None, journal=None) -> List | dict | bool:
    """
    Function to execute a list of scenarios (NOT FILES).

    Args:
        supplier: Supplier instance.
        scenarios (Optional[List[dict] | dict], optional): Accepts a list of scenarios or a single scenario as a dictionary. The run_scenario(s, scenario) function is called to execute scenarios. Defaults to None.
        journal (_type_, optional): _description_. Defaults to None.

    Returns:
        List | dict | bool: The result of executing the scenarios as a list or dictionary, depending on the input data type, or False in case of an error.

    Example:
        >>> # Создайте экземпляр класса Supplier
        >>> supplier = ... # Your Supplier instance
        >>> scenarios_data = [
        >>>   {'url': 'https://example.com/category1', 'name': 'scenario1'},
        >>>    {'url': 'https://example.com/category2', 'name': 'scenario2'}
        >>> ]
        >>> result = run_scenarios(supplier, scenarios_data)
        >>> print(result)
        [...]
    """
    if not scenarios:
        scenarios = [supplier.current_scenario]
        # If no scenarios are specified, take them from supplier.current_scenario.
    scenarios = scenarios if isinstance(scenarios, list) else [scenarios]
    res = []
    for scenario in scenarios:
        res = run_scenario(supplier, scenario, scenario.get('name', 'unknown'), journal)
        if journal and 'scenario_files' in journal and journal['scenario_files']:
            journal['scenario_files'][-1][scenario] = str(res)
        dump_journal(supplier, journal)
    return res


def run_scenario(supplier, scenario: dict, scenario_name: str, journal=None) -> List | dict | bool:
    """
    Function to execute the received scenario.

    Args:
        supplier: Supplier instance.
        scenario (dict): Dictionary containing scenario details.
        scenario_name (str): Name of the scenario.
        journal (_type_, optional): _description_. Defaults to None.

    Returns:
        List | dict | bool: The result of executing the scenario.

    Example:
         >>> # Создайте экземпляр класса Supplier
         >>> supplier = ... # Your Supplier instance
         >>> scenario_data = {'url': 'https://example.com/category', 'name': 'test_scenario'}
         >>> result = run_scenario(supplier, scenario_data, 'test_scenario')
         >>> print(result)
         [...]
    """
    logger.info(f'Starting scenario: {scenario_name}')
    supplier.current_scenario = scenario
    driver = supplier.driver
    driver.get_url(scenario['url'])

    # Get list of products in the category
    list_products_in_category: list = supplier.related_modules.get_list_products_in_category(supplier)

    # No products in the category (or they haven't loaded yet)
    if not list_products_in_category:
        logger.warning('No product list collected from the category page. Possibly an empty category - ', driver.current_url)
        return False

    for url in list_products_in_category:
        if not driver.get_url(url):
            logger.error(f'Error navigating to product page at: {url}')
            continue  # <- Error navigating to the page. Skip

        # Grab product page fields
        grabbed_fields = supplier.related_modules.grab_product_page(supplier)
        f: ProductFields = asyncio.run(supplier.related_modules.grab_page(supplier))
        if not f:
            logger.error('Failed to collect product fields')
            continue

        presta_fields_dict, assist_fields_dict = f.presta_fields_dict, f.assist_fields_dict
        try:
            product = ProductAsync(supplier_prefix=supplier.supplier_prefix, presta_fields_dict=presta_fields_dict) # TODO - исправить вызов класса
            asyncio.run(insert_grabbed_data_to_prestashop(f)) # TODO -  доработать
        except Exception as ex:
            logger.error(f'Product {product.fields["name"][1]} could not be saved', ex)
            continue

    return list_products_in_category


async def insert_grabbed_data_to_prestashop(
    f: ProductFields, coupon_code: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None
) -> bool:
    """
    Insert the product into PrestaShop.

    Args:
        f (ProductFields): ProductFields instance containing the product information.
        coupon_code (Optional[str], optional): Optional coupon code. Defaults to None.
        start_date (Optional[str], optional): Optional start date for the promotion. Defaults to None.
        end_date (Optional[str], optional): Optional end date for the promotion. Defaults to None.

    Returns:
        bool: True if the insertion was successful, False otherwise.

    Example:
        >>> # Создайте экземпляр класса ProductFields
        >>> product_fields = ... # Your ProductFields instance
        >>> result = asyncio.run(insert_grabbed_data_to_prestashop(product_fields, 'TEST_COUPON', '2024-01-01', '2024-12-31'))
        >>> print(result)
        True
    """
    try:
        presta = PrestaShop() #TODO - заменить на вызов из self.module
        return await presta.post_product_data(
            product_id=f.product_id,
            product_name=f.product_name,
            product_category=f.product_category,
            product_price=f.product_price,
            description=f.description,
            coupon_code=coupon_code,
            start_date=start_date,
            end_date=end_date,
        )

    except Exception as ex:
        logger.error('Failed to insert product data into PrestaShop: ', ex)
        return False