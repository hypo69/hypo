# Анализ кода модуля `executor.py`

**Качество кода**
8
-   Плюсы
    -   Код хорошо структурирован и разбит на функции, что облегчает его чтение и понимание.
    -   Используется логирование для отслеживания ошибок и успешного выполнения сценариев.
    -   Присутствует обработка исключений.
    -   Используется `asyncio` для асинхронных операций.
    -   Присутствуют docstring для функций.
-   Минусы
    -   Некоторые docstring требуют доработки в соответствии с RST.
    -   Используются `try-except` блоки, которые можно заменить на `logger.error`.
    -   Переменная `_journal` объявлена как глобальная, но используется только внутри модуля.
    -   В некоторых местах отсутствует проверка на `None` перед использованием переменных.
    -   В `run_scenario` в блоке try except не обрабатываются исключения FileNotFoundError и JSONDecodeError.

**Рекомендации по улучшению**

1.  **Форматирование docstring**:
    -   Привести все docstring к стандарту reStructuredText (RST).
    -   Добавить описания параметров и возвращаемых значений.
    -   Использовать `:param` и `:return` для описания параметров и возвращаемых значений.

2.  **Обработка ошибок**:
    -   Использовать `logger.error` вместо `try-except` для логирования ошибок.
    -   Добавить обработку конкретных исключений.
    -   Убрать `...` как точки остановки и заменить их на реальную обработку.

3.  **Глобальные переменные**:
    -   Сделать переменную `_journal` локальной для модуля, если это возможно, или передавать ее как параметр.
    -   Передавать `_journal` как аргумент функции или использовать декоратор, если это не повлияет на читаемость.

4.  **Проверки на `None`**:
    -   Добавить проверки на `None` перед использованием переменных, например, `list_products_in_category`.

5.  **Импорты**:
    -   Проверить и добавить недостающие импорты, если такие есть.

6.  **Сообщения в логгере**:
    -   Сделать сообщения в логгере более информативными.
    -   Уточнить сообщения об ошибках и успешном выполнении.

7.  **Переименование переменных**:
    -  Убедиться что имена переменных и функций соответствуют ранее обработанным файлам.

8.  **Удаление todo**:
    -   Удалить все `todo` комментарии.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для выполнения сценариев.
=========================================================================================

Этот модуль содержит функции для выполнения сценариев, их загрузки из файлов и обработки
процесса извлечения информации о продукте и вставки ее в PrestaShop.

"""

import os
import sys
import requests
import asyncio
import time
import tempfile
from datetime import datetime
from math import log, prod
from pathlib import Path
from typing import Dict, List, Any
import json

from src.utils.jjson import j_loads, j_dumps
from src.product import Product, ProductFields
from src.endpoints.prestashop import PrestaShop
from src.db import ProductCampaignsManager
from src.logger.logger import logger
from src.logger.exceptions import ProductFieldException
from src.utils.printer import pprint
from src import gs
import header


_journal: dict = {'scenario_files': ''}
_journal['name'] = timestamp = gs.now


def dump_journal(s, journal: dict):
    """
    Сохраняет данные журнала в файл JSON.

    :param s: Экземпляр поставщика.
    :param journal: Словарь, содержащий данные журнала.
    """
    _journal_file_path = Path(s.supplier_abs_path, '_journal', f"{journal['name']}.json")
    j_dumps(journal, _journal_file_path)

def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Выполняет список файлов сценариев.

    :param s: Экземпляр поставщика.
    :param scenario_files_list: Список путей к файлам сценариев или один путь к файлу.
    :raises TypeError: Если scenario_files_list не является списком или объектом Path.
    :return: True, если все сценарии выполнены успешно, False в противном случае.
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
    :param scenario_file: Путь к файлу сценария.
    :return: True, если сценарий выполнен успешно, False в противном случае.
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
    :param scenarios: Список сценариев или один сценарий в виде словаря.
    :return: Результат выполнения сценариев в виде списка или словаря,
             в зависимости от типа входных данных, или False в случае ошибки.
    """
    if not scenarios:
        if not s.current_scenario:
            logger.error(f'No scenarios were specified, and s.current_scenario is not set.')
            return False
        scenarios = [s.current_scenario]
    
    scenarios = scenarios if isinstance(scenarios, list) else [scenarios]
    res = []
    for scenario in scenarios:
        res = run_scenario(s, scenario)
        if _journal and _journal.get('scenario_files'):
           _journal['scenario_files'][-1][str(scenario)] = str(res)
           dump_journal(s, _journal)
    return res


def run_scenario(supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | bool:
    """
    Выполняет полученный сценарий.

    :param supplier: Экземпляр поставщика.
    :param scenario: Словарь, содержащий детали сценария.
    :param scenario_name: Имя сценария.
    :return: Результат выполнения сценария.
    """
    s = supplier
    logger.info(f'Starting scenario: {scenario_name}')
    s.current_scenario = scenario
    d = s.driver
    if not d.get_url(scenario['url']):
        logger.error(f'Failed to navigate to url: {scenario["url"]}')
        return False

    # Получение списка продуктов в категории
    list_products_in_category: list = s.related_modules.get_list_products_in_category(s)

    # Проверка наличия продуктов в категории
    if not list_products_in_category:
        logger.warning(f'No product list collected from the category page. Possibly an empty category - {d.current_url}')
        return False

    for url in list_products_in_category:
        if not d.get_url(url):
            logger.error(f'Error navigating to product page at: {url}')
            continue  # Ошибка при переходе на страницу. Пропуск.

        # Получение полей страницы продукта
        f: ProductFields = asyncio.run(s.related_modules.grab_page(s))
        if not f:
            logger.error(f"Failed to collect product fields")
            continue
        
        presta_fields_dict, assist_fields_dict = f.presta_fields_dict, f.assist_fields_dict
        try:
            product: Product = Product(supplier_prefix=s.supplier_prefix, presta_fields_dict=presta_fields_dict)
            insert_grabbed_data(f)
        except Exception as ex:
             if hasattr(product, 'fields') and product.fields and product.fields.get('name'):
                logger.error(f'Product {product.fields["name"][1]} could not be saved: {ex}', exc_info=True)
             else:
                 logger.error(f'Product could not be saved: {ex}', exc_info=True)
             continue
            
    return list_products_in_category


def insert_grabbed_data(product_fields: ProductFields):
    """
    Вставляет полученные данные продукта в PrestaShop.
    """
    asyncio.run(execute_PrestaShop_insert(product_fields))


async def execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    """
    Асинхронно вставляет продукт в PrestaShop.

    :param f: Экземпляр ProductFields, содержащий информацию о продукте.
    :param coupon_code: Опциональный код купона.
    :param start_date: Опциональная дата начала акции.
    :param end_date: Опциональная дата окончания акции.
    :return: True, если вставка прошла успешно, False в противном случае.
    """
    await execute_PrestaShop_insert(f, coupon_code, start_date, end_date)


def execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    """
    Вставляет продукт в PrestaShop.

    :param f: Экземпляр ProductFields, содержащий информацию о продукте.
    :param coupon_code: Опциональный код купона.
    :param start_date: Опциональная дата начала акции.
    :param end_date: Опциональная дата окончания акции.
    :return: True, если вставка прошла успешно, False в противном случае.
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
        logger.error(f'Failed to insert product data into PrestaShop: {ex}', exc_info=True)
        return False