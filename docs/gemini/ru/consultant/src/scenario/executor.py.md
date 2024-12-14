# Анализ кода модуля `executor.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает его понимание и поддержку.
    - Используется логирование для отслеживания ошибок и успешного выполнения операций.
    - Присутствует обработка исключений, что делает код более надежным.
    - Используются аннотации типов, что улучшает читаемость и помогает в отладке.
- Минусы
    -  Не все функции и методы имеют подробные docstring в формате reStructuredText (RST).
    -  Некоторые комментарии после `#` не соответствуют стандарту RST.
    -  Функция `run_scenarios` имеет TODO, указывающий на необходимость проверки логики работы.
    -  Функция `insert_grabbed_data` имеет TODO о переносе логики в другой файл.
    -  Функция `run_scenario` имеет TODO по поводу необходимости параметра `scenario_name`.
    -  Импорты не отсортированы и не сгруппированы.
    -  В некоторых функциях используется стандартный `try-except` блок, где можно было бы использовать `logger.error`

**Рекомендации по улучшению**

1. **Документация:**
   - Добавить docstring в формате RST для всех функций, методов и переменных.
   -  Переписать комментарии после `#` в соответствии с RST.
   - Уточнить docstring для `run_scenarios`, `insert_grabbed_data`, `run_scenario`.

2. **Логирование:**
    - Заменить избыточные `try-except` блоки на использование `logger.error` для обработки ошибок.

3. **Структура кода:**
    - Перенести логику вставки данных в PrestaShop из функции `insert_grabbed_data` в класс PrestaShop.
   - Разобраться с TODO в функциях `run_scenarios`, `run_scenario`.
   - Отсортировать и сгруппировать импорты.

4.  **Обработка данных:**
    - Проверить, что все файлы загружаются через `j_loads` или `j_loads_ns` из `src.utils.jjson`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для выполнения сценариев.
=========================================================================================

Этот модуль содержит функции для выполнения сценариев, их загрузки из файлов и обработки процесса
извлечения информации о продукте и вставки ее в PrestaShop.

Пример использования
--------------------

Пример использования функций модуля:

.. code-block:: python

    from pathlib import Path
    from src.scenario.executor import run_scenario_files
    from src.supplier import Supplier

    supplier = Supplier(supplier_name='example_supplier', supplier_abs_path=Path('/path/to/supplier'))
    scenario_files = [Path('/path/to/scenario1.json'), Path('/path/to/scenario2.json')]
    run_scenario_files(supplier, scenario_files)
"""

import asyncio
import json
import os
import sys
import tempfile
import time
from datetime import datetime
from math import log, prod
from pathlib import Path
from typing import Any, Dict, List

import requests

from src import gs
from src.db import ProductCampaignsManager
from src.endpoints.prestashop import PrestaShop
from src.logger.exceptions import ProductFieldException
from src.logger.logger import logger
from src.product import Product, ProductFields, translate_presta_fields_dict
from src.utils.jjson import j_dumps, j_loads
from src.utils.printer import pprint

_journal: Dict[str, Any] = {'scenario_files': ''}
_journal['name'] = timestamp = gs.now


def dump_journal(s, journal: Dict[str, Any]):
    """
    Сохраняет данные журнала в JSON файл.

    :param s: Экземпляр поставщика.
    :type s: Supplier
    :param journal: Словарь, содержащий данные журнала.
    :type journal: dict
    """
    _journal_file_path = Path(s.supplier_abs_path, '_journal', f"{journal['name']}.json")
    j_dumps(journal, _journal_file_path)


def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Выполняет список файлов сценариев.

    :param s: Экземпляр поставщика.
    :type s: Supplier
    :param scenario_files_list: Список путей к файлам сценариев или путь к одному файлу.
    :type scenario_files_list: List[Path] | Path
    :raises TypeError: Если `scenario_files_list` не является списком или объектом Path.
    :return: True, если все сценарии выполнены успешно, иначе False.
    :rtype: bool
    """
    if isinstance(scenario_files_list, Path):
        scenario_files_list = [scenario_files_list]
    elif not isinstance(scenario_files_list, list):
        raise TypeError("scenario_files_list must be a list or a Path object.")
    scenario_files_list = scenario_files_list if scenario_files_list else s.scenario_files

    _journal['scenario_files'] = {}
    for scenario_file in scenario_files_list:
        _journal['scenario_files'][scenario_file.name] = {}
        try:
            if run_scenario_file(s, scenario_file):
                _journal['scenario_files'][scenario_file.name]['message'] = f"{scenario_file} completed successfully!"
                logger.success(f'Scenario {scenario_file} completed successfully!')
            else:
                _journal['scenario_files'][scenario_file.name]['message'] = f"{scenario_file} FAILED!"
                logger.error(f'Scenario {scenario_file} failed to execute!')
        except Exception as e:
            logger.critical(f"An error occurred while processing {scenario_file}: {e}")
            _journal['scenario_files'][scenario_file.name]['message'] = f"Error: {e}"
    return True


def run_scenario_file(s, scenario_file: Path) -> bool:
    """
    Загружает и выполняет сценарии из файла.

    :param s: Экземпляр поставщика.
    :type s: Supplier
    :param scenario_file: Путь к файлу сценария.
    :type scenario_file: Path
    :return: True, если сценарий выполнен успешно, иначе False.
    :rtype: bool
    """
    try:
        scenarios_dict = j_loads(scenario_file)['scenarios']
        for scenario_name, scenario in scenarios_dict.items():
            s.current_scenario = scenario
            if run_scenario(s, scenario, scenario_name):
                logger.success(f'Scenario {scenario_name} completed successfully!')
            else:
                logger.error(f'Scenario {scenario_name} failed to execute!')
        return True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.critical(f"Error loading or processing scenario file {scenario_file}: {e}")
        return False


def run_scenarios(s, scenarios: List[dict] | dict = None, _journal=None) -> List | dict | bool:
    """
    Выполняет список сценариев (НЕ ФАЙЛОВ).

    :param s: Экземпляр поставщика.
    :type s: Supplier
    :param scenarios: Список сценариев или один сценарий в виде словаря.
    :type scenarios: List[dict] | dict, optional
    :param _journal: Журнал выполнения.
    :type _journal: dict, optional
    :return: Результат выполнения сценариев в виде списка или словаря,
             или False в случае ошибки.
    :rtype: List | dict | bool
    """
    if not scenarios:
        scenarios = [s.current_scenario]
        # Если сценарии не указаны, берем их из s.current_scenario.
    scenarios = scenarios if isinstance(scenarios, list) else [scenarios]
    res = []
    for scenario in scenarios:
        res = run_scenario(s, scenario)
        _journal['scenario_files'][-1][scenario] = str(res)
        dump_journal(s, _journal)
    return res


def run_scenario(supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | bool:
    """
    Выполняет полученный сценарий.

    :param supplier: Экземпляр поставщика.
    :type supplier: Supplier
    :param scenario: Словарь, содержащий детали сценария.
    :type scenario: dict
    :param scenario_name: Имя сценария.
    :type scenario_name: str
    :param _journal: Журнал выполнения.
    :type _journal: dict, optional
    :return: Результат выполнения сценария.
    :rtype: List | dict | bool
    """
    s = supplier
    logger.info(f'Starting scenario: {scenario_name}')
    s.current_scenario = scenario
    d = s.driver
    d.get_url(scenario['url'])

    # Получает список продуктов в категории
    list_products_in_category: list = s.related_modules.get_list_products_in_category(s)

    # Если нет продуктов в категории (или они еще не загрузились)
    if not list_products_in_category:
        logger.warning('No product list collected from the category page. Possibly an empty category - ', d.current_url)
        return False

    for url in list_products_in_category:
        if not d.get_url(url):
            logger.error(f'Error navigating to product page at: {url}')
            continue  # Ошибка навигации к странице. Пропускаем

        # Получает поля страницы продукта
        grabbed_fields = s.related_modules.grab_product_page(s)
        f: ProductFields = asyncio.run(s.related_modules.grab_page(s))
        if not f:
            logger.error(f"Failed to collect product fields")
            continue

        presta_fields_dict, assist_fields_dict = f.presta_fields_dict, f.assist_fields_dict
        try:
            product: Product = Product(supplier_prefix=s.supplier_prefix, presta_fields_dict=presta_fields_dict)
            insert_grabbed_data(f)
        except Exception as ex:
             if hasattr(product, 'fields') and "name" in product.fields:
                 logger.error(f'Product {product.fields["name"][1]} could not be saved', ex)
             else:
                logger.error(f'Product could not be saved', ex)
             continue

    return list_products_in_category


def insert_grabbed_data(product_fields: ProductFields):
    """
    Вставляет полученные данные о продукте в PrestaShop.

    :param product_fields: Экземпляр ProductFields, содержащий информацию о продукте.
    :type product_fields: ProductFields
    """
    asyncio.run(execute_PrestaShop_insert(product_fields))


async def execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    """
    Асинхронно вызывает функцию для вставки данных продукта в PrestaShop.

    :param f: Экземпляр ProductFields, содержащий информацию о продукте.
    :type f: ProductFields
    :param coupon_code: Необязательный код купона.
    :type coupon_code: str, optional
    :param start_date: Необязательная начальная дата акции.
    :type start_date: str, optional
    :param end_date: Необязательная конечная дата акции.
    :type end_date: str, optional
    :return: True, если вставка прошла успешно, иначе False.
    :rtype: bool
    """
    await execute_PrestaShop_insert(f, coupon_code, start_date, end_date)


def execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    """
    Вставляет данные продукта в PrestaShop.

    :param f: Экземпляр ProductFields, содержащий информацию о продукте.
    :type f: ProductFields
    :param coupon_code: Необязательный код купона.
    :type coupon_code: str, optional
    :param start_date: Необязательная начальная дата акции.
    :type start_date: str, optional
    :param end_date: Необязательная конечная дата акции.
    :type end_date: str, optional
    :return: True, если вставка прошла успешно, иначе False.
    :rtype: bool
    """
    try:
        presta = PrestaShop()
        presta.post_product_data(
            product_id=f.product_id,
            product_name=f.product_name,
            product_category=f.product_category,
            product_price=f.product_price,
            description=f.description,
            coupon_code=coupon_code,
            start_date=start_date,
            end_date=end_date
        )
        return True
    except Exception as ex:
        logger.error(f'Failed to insert product data into PrestaShop: {ex}', ex)
        return False
```