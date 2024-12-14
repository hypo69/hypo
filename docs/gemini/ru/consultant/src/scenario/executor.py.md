# Анализ кода модуля `executor.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, разбит на функции, что способствует читаемости и повторному использованию.
    - Используются логирование для отслеживания ошибок и успешного выполнения операций.
    - Применение асинхронных операций улучшает производительность, особенно при работе с сетевыми запросами.
    - Наличие docstring для функций и классов.
- Минусы
    -  Не все функции и методы имеют docstring в формате RST.
    -  Некоторые комментарии не соответствуют формату RST.
    -  Есть повторяющиеся блоки try-except, которые можно упростить с помощью `logger.error`.
    -  Некоторые части кода, такие как обработка `scenario_files_list`, можно сделать более читаемыми.
    -  Обработка ошибок в функции `run_scenario_files` не предоставляет достаточно информации для отладки.
    -  В некоторых местах используется `json.load` вместо `j_loads`.
    -  Функции `run_scenarios` и `run_scenario` имеют схожую логику, что может быть пересмотрено для упрощения.
    -  `_journal` не передается в функцию `run_scenario` хотя определен в сигнатуре.

**Рекомендации по улучшению**

1.  **Формат документации**:
    -   Привести все docstring и комментарии в формат RST.
    -   Использовать одинарные кавычки для строк.
2.  **Обработка данных**:
    -   Заменить все `json.load` на `j_loads` или `j_loads_ns`.
3.  **Анализ структуры**:
    -   Добавить отсутствующие импорты.
    -   Переименовать переменные в соответствии с остальным кодом (например, `f` в `product_fields`).
4.  **Рефакторинг и улучшения**:
    -   Уточнить docstring для всех функций и методов.
    -   Использовать `logger.error` для обработки исключений вместо `try-except` блоков.
    -   Упростить обработку ошибок и предоставить больше контекста для отладки.
    -   Рефакторинг функций `run_scenarios` и `run_scenario` для удаления дублирования кода.
    -   Добавить проверку существования `_journal`, для избежания `KeyError`.
    -   Перенести логику вставки данных в PrestaShop в соответствующий класс.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для выполнения сценариев.
=========================================================================================

Этот модуль содержит функции для выполнения сценариев, загрузки их из файлов,
и управления процессом извлечения информации о продуктах и их вставки в PrestaShop.

Пример использования
--------------------

Пример использования функций модуля:

.. code-block:: python

    from pathlib import Path
    from src.scenario.executor import run_scenario_files

    # Пример запуска сценариев из файлов
    supplier_instance = ...  # Экземпляр поставщика
    scenario_files = [Path("path/to/scenario1.json"), Path("path/to/scenario2.json")]
    run_scenario_files(supplier_instance, scenario_files)
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

import header  # TODO: check if it used
from src import gs
from src.utils.printer import pprint
from src.utils.jjson import j_loads, j_dumps
from src.product import Product, ProductFields, translate_presta_fields_dict
from src.endpoints.prestashop import PrestaShop
from src.db import ProductCampaignsManager
from src.logger.logger import logger
from src.logger.exceptions import ProductFieldException

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
    :raises TypeError: Если scenario_files_list не является списком или Path.
    :return: True, если все сценарии выполнены успешно, иначе False.
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
            # Код исполняет запуск сценария из файла
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
    :return: True, если сценарий выполнен успешно, иначе False.
    """
    try:
        # Код исполняет загрузку сценариев из файла
        scenarios_dict = j_loads(scenario_file)['scenarios']
        for scenario_name, scenario in scenarios_dict.items():
            s.current_scenario = scenario
            # Код исполняет запуск сценария
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
    :return: Результат выполнения сценариев в виде списка или словаря, или False в случае ошибки.

    .. todo::
        Проверить вариант, когда сценарии не указаны ниоткуда. Например, когда s.current_scenario не указан и scenarios не указаны.
    """
    if not scenarios:
        scenarios = [s.current_scenario]
        """
        Если сценарии не указаны, берутся из s.current_scenario.
        .. todo::
            Проверить этот вариант со всех сторон. Например, когда s.current_scenario не указан и scenarios не указаны.
        """
    scenarios = scenarios if isinstance(scenarios, list) else [scenarios]
    res = []
    for scenario in scenarios:
        # Код исполняет запуск сценария
        result = run_scenario(s, scenario, _journal=_journal)
        if _journal and _journal.get('scenario_files') and len(_journal['scenario_files']) > 0:
           _journal['scenario_files'][-1][scenario] = str(result)
           dump_journal(s, _journal)
        res.append(result)
    return res

def run_scenario(supplier, scenario: dict, scenario_name: str = None, _journal=None) -> List | dict | bool:
    """
    Выполняет полученный сценарий.

    :param supplier: Экземпляр поставщика.
    :param scenario: Словарь, содержащий детали сценария.
    :param scenario_name: Название сценария.
    :return: Результат выполнения сценария.

    .. todo::
        Проверить необходимость параметра scenario_name.
    """
    s = supplier
    if scenario_name:
        logger.info(f'Starting scenario: {scenario_name}')
    s.current_scenario = scenario
    d = s.driver
    d.get_url(scenario['url'])

    # Код исполняет получение списка продуктов в категории
    list_products_in_category: list = s.related_modules.get_list_products_in_category(s)

    # Проверка наличия продуктов в категории
    if not list_products_in_category:
        logger.warning('No product list collected from the category page. Possibly an empty category - ', d.current_url)
        return False

    for url in list_products_in_category:
        # Код исполняет переход на страницу продукта
        if not d.get_url(url):
            logger.error(f'Error navigating to product page at: {url}')
            continue  # Пропуск если ошибка навигации

        # Код исполняет сбор полей со страницы продукта
        grabbed_fields = s.related_modules.grab_product_page(s)
        product_fields: ProductFields = asyncio.run(s.related_modules.grab_page(s))
        if not product_fields:
            logger.error(f"Failed to collect product fields")
            continue

        presta_fields_dict, assist_fields_dict = product_fields.presta_fields_dict, product_fields.assist_fields_dict
        try:
            # Код исполняет создание экземпляра Product и вставку данных
            product: Product = Product(supplier_prefix=s.supplier_prefix, presta_fields_dict=presta_fields_dict)
            insert_grabbed_data(product_fields)
        except Exception as ex:
            logger.error(f'Product {product.fields["name"][1]} could not be saved', ex)
            continue

    return list_products_in_category


def insert_grabbed_data(product_fields: ProductFields):
    """
    Вставляет полученные данные продукта в PrestaShop.

    .. todo::
        Перенести эту логику в другой файл. В класс PrestaShop.
    """
    # Код исполняет асинхронный запуск вставки данных
    asyncio.run(execute_PrestaShop_insert(product_fields))


async def execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    # Код исполняет асинхронный запуск вставки данных
    await execute_PrestaShop_insert(f, coupon_code, start_date, end_date)


def execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    """
    Вставляет продукт в PrestaShop.

    :param f: Экземпляр ProductFields, содержащий информацию о продукте.
    :param coupon_code: Опциональный код купона.
    :param start_date: Опциональная дата начала акции.
    :param end_date: Опциональная дата окончания акции.
    :return: True, если вставка прошла успешно, иначе False.
    """
    try:
        presta = PrestaShop()
        # Код исполняет отправку данных продукта в PrestaShop
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