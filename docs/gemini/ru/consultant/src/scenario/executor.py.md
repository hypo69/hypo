# Анализ кода модуля `executor.py`

**Качество кода: 7/10**
-   **Плюсы:**
    -   Код содержит docstring для модуля и функций, что облегчает понимание назначения кода.
    -   Используется `logger` для логирования, что помогает в отладке и мониторинге.
    -   Присутствует обработка исключений, что делает код более надежным.
    -   Используется `asyncio` для асинхронных операций, что позволяет обрабатывать множество запросов эффективно.
    -   Разделение кода на функции делает его более модульным и читаемым.
    -   Присутствует использование `Pathlib` для работы с путями.
-   **Минусы:**
    -   Используется стандартный `json.load` вместо `j_loads` в `run_scenario_file`, что не соответствует инструкции.
    -   Не везде используются f-строки, где это уместно.
    -   Не хватает более детального описания формата данных в docstring для некоторых функций.
    -   В некоторых местах есть использование `try-except` без конкретной обработки.
    -   В коде присутствуют TODO, которые не были выполнены.
    -   Не все переменные и имена функций соответствуют стилю именования в ранее обработанных файлах.
    -   Имеется неиспользуемый параметр `_journal` в функциях `run_scenarios` и `run_scenario`.

**Рекомендации по улучшению**

1.  **Импорты:**
    -   Уточнить импорты, приведя их в соответствие с другими файлами проекта.
    -   Добавить недостающие импорты, если это необходимо.
2.  **JSON:**
    -   Заменить `json.load` на `j_loads` в функции `run_scenario_file`.
3.  **Логирование:**
    -   Использовать `logger.error` вместо `print` для вывода ошибок.
    -   Применять f-строки для форматирования сообщений логгера.
4.  **Обработка исключений:**
    -   Уточнить обработку исключений, добавляя конкретные действия или сообщения логгера.
5.  **Документация:**
    -   Добавить недостающие docstring к функциям, методам и классам.
    -   Описать более детально типы данных в docstring, включая форматы входных и выходных данных.
    -   Придерживаться стандартов оформления docstring в Python (для Sphinx).
6.  **Рефакторинг:**
    -   Устранить TODO, прокомментировав или выполнив указанные задачи.
    -   Удалить неиспользуемый параметр `_journal` в функциях `run_scenarios` и `run_scenario`.
    -   Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
7.  **Сообщения:**
    -   Использовать конкретные формулировки в комментариях, избегая общих слов, таких как "получаем" или "делаем".
    -   Добавить комментарии к логике кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для выполнения сценариев.
=========================================================================================

Этот модуль содержит функции для выполнения сценариев, загрузки их из файлов
и обработки процесса извлечения информации о продукте и вставки ее в PrestaShop.

.. module:: src.scenario.executor
   :platform: Windows, Unix
   :synopsis: Модуль для выполнения сценариев.
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
from typing import Dict, List, Optional
# from json import load
import json

import header
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


def dump_journal(s, journal: dict) -> None:
    """
    Сохраняет данные журнала в JSON-файл.

    Args:
        s: Экземпляр поставщика.
        journal: Словарь, содержащий данные журнала.
    """
    _journal_file_path = Path(s.supplier_abs_path, '_journal', f"{journal['name']}.json")
    j_dumps(journal, _journal_file_path)


def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Выполняет список файлов сценариев.

    Args:
        s: Экземпляр поставщика.
        scenario_files_list: Список путей к файлам сценариев или один путь к файлу.

    Returns:
        True, если все сценарии были выполнены успешно, False в противном случае.

    Raises:
        TypeError: если `scenario_files_list` не является списком или строкой.
    """
    if isinstance(scenario_files_list, Path):
        scenario_files_list = [scenario_files_list]
    elif not isinstance(scenario_files_list, list):
        raise TypeError('scenario_files_list must be a list or a Path object.')
    scenario_files_list = scenario_files_list if scenario_files_list else s.scenario_files

    _journal['scenario_files'] = {}
    for scenario_file in scenario_files_list:
        _journal['scenario_files'][scenario_file.name] = {}
        try:
            if run_scenario_file(s, scenario_file):
                _journal['scenario_files'][scenario_file.name]['message'] = f'{scenario_file} completed successfully!'
                logger.success(f'Сценарий {scenario_file} выполнен успешно!')
            else:
                _journal['scenario_files'][scenario_file.name]['message'] = f'{scenario_file} FAILED!'
                logger.error(f'Сценарий {scenario_file} не выполнен!')
        except Exception as e:
            logger.critical(f'Произошла ошибка при обработке {scenario_file}: {e}')
            _journal['scenario_files'][scenario_file.name]['message'] = f'Ошибка: {e}'
    return True


def run_scenario_file(s, scenario_file: Path) -> bool:
    """
    Загружает и выполняет сценарии из файла.

    Args:
        s: Экземпляр поставщика.
        scenario_file: Путь к файлу сценария.

    Returns:
        True, если сценарий был выполнен успешно, False в противном случае.
    """
    try:
        # Код загружает JSON из файла сценария
        scenarios_dict = j_loads(scenario_file)['scenarios']
        for scenario_name, scenario in scenarios_dict.items():
            s.current_scenario = scenario
            if run_scenario(s, scenario, scenario_name):
                logger.success(f'Сценарий {scenario_name} выполнен успешно!')
            else:
                logger.error(f'Сценарий {scenario_name} не выполнен!')
        return True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.critical(f'Ошибка загрузки или обработки файла сценария {scenario_file}: {e}')
        return False


def run_scenarios(s, scenarios: Optional[List[dict] | dict] = None) -> List | dict | bool:
    """
    Выполняет список сценариев (НЕ ФАЙЛЫ).

    Args:
        s: Экземпляр поставщика.
        scenarios: Список сценариев или один сценарий в виде словаря.

    Returns:
        Результат выполнения сценариев в виде списка или словаря,
        в зависимости от типа входных данных, или False в случае ошибки.

    """
    if not scenarios:
        scenarios = [s.current_scenario]
        # Если сценарии не указаны, используются из s.current_scenario.
    scenarios = scenarios if isinstance(scenarios, list) else [scenarios]
    res = []
    for scenario in scenarios:
        res = run_scenario(s, scenario)
        # _journal['scenario_files'][-1][scenario] = str(res)
        # dump_journal(s, _journal)
    return res


def run_scenario(supplier, scenario: dict, scenario_name: str) -> List | dict | bool:
    """
    Выполняет полученный сценарий.

    Args:
        supplier: Экземпляр поставщика.
        scenario: Словарь, содержащий детали сценария.
        scenario_name: Имя сценария.

    Returns:
         Результат выполнения сценария.
    """
    s = supplier
    logger.info(f'Начинается сценарий: {scenario_name}')
    s.current_scenario = scenario
    d = s.driver
    d.get_url(scenario['url'])

    # Получение списка продуктов в категории
    list_products_in_category: list = s.related_modules.get_list_products_in_category(s)

    # Проверка, если нет продуктов в категории (или они еще не загрузились)
    if not list_products_in_category:
        logger.warning(f'Список продуктов не собран со страницы категории. Возможно, пустая категория - {d.current_url}')
        return False

    for url in list_products_in_category:
        if not d.get_url(url):
            logger.error(f'Ошибка при переходе на страницу продукта: {url}')
            continue  # <- Ошибка навигации. Пропуск

        # Сбор полей со страницы продукта
        grabbed_fields = s.related_modules.grab_product_page(s)
        f: ProductFields = asyncio.run(s.related_modules.grab_page(s))
        if not f:
            logger.error('Не удалось собрать поля продукта')
            continue

        presta_fields_dict, assist_fields_dict = f.presta_fields_dict, f.assist_fields_dict
        try:
            product: Product = Product(supplier_prefix=s.supplier_prefix, presta_fields_dict=presta_fields_dict)
            insert_grabbed_data(f)
        except Exception as ex:
            logger.error(f'Продукт {product.fields["name"][1]} не удалось сохранить', ex)
            continue

    return list_products_in_category


async def insert_grabbed_data_to_prestashop(
    f: ProductFields, coupon_code: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None
) -> bool:
    """
    Вставляет данные о продукте в PrestaShop.

    Args:
        f: Экземпляр ProductFields, содержащий информацию о продукте.
        coupon_code: Опциональный код купона.
        start_date: Опциональная начальная дата акции.
        end_date: Опциональная конечная дата акции.

    Returns:
        True, если вставка прошла успешно, False в противном случае.
    """
    try:
        presta = PrestaShop()
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
        logger.error('Не удалось вставить данные продукта в PrestaShop: ', ex)
        return False


def insert_grabbed_data(f: ProductFields):
    """
    Вставляет данные продукта.

    Args:
        f: Экземпляр ProductFields, содержащий информацию о продукте.
    """
    ...
```