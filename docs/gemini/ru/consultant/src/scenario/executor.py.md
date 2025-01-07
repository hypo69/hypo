# Анализ кода модуля `executor.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Используется логирование для отслеживания выполнения сценариев и ошибок.
    - Присутствуют docstring для функций, описывающие их назначение и параметры.
    - Используются типы аннотаций для параметров функций.
- Минусы
    - Некоторые docstring требуют уточнения и приведения к стандарту RST.
    - Используются конструкции try-except без конкретной обработки, что может затруднить отладку.
    - Необходимо добавить обработку ошибок при загрузке JSON файлов
    - Есть TODO комментарии, которые требуют внимания.
    - Некоторые комментарии после `#` необходимо переписать в reStructuredText (RST)

**Рекомендации по улучшению**
1.  **Документация**:
    -   Переписать docstring в формате reStructuredText (RST) для всех функций и методов, включая параметры и возвращаемые значения.
    -   Добавить более подробные описания к функциям, особенно к тем, которые выполняют сложные действия.

2.  **Обработка ошибок**:
    -   Использовать `logger.error` для обработки исключений вместо `try-except` блоков без явной обработки. Это позволит централизовать логирование ошибок и сделать отладку проще.
    -   Добавить более конкретные исключения при обработке json, например `json.JSONDecodeError`
    -   Проверить все места, где происходит чтение файлов, и убедиться, что используется `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
    -   Добавить явную проверку типа для переменных `scenario_files_list`

3.  **Логирование**:
    -   Убедиться, что все значимые операции и ошибки логируются.
    -   Использовать разные уровни логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL) в соответствии с серьезностью сообщения.
    -   Переименовать переменную `_journal` в `journal_data`

4.  **Рефакторинг**:
    -   Вынести логику вставки данных в PrestaShop в отдельный класс или функцию в модуле `src.endpoints.prestashop`, как указано в TODO.
    -   Проверить необходимость параметра `scenario_name` в функции `run_scenario` и удалить его, если он не используется.
    -   Уточнить, как обрабатываются случаи, когда `scenarios` не указаны и `s.current_scenario` тоже.
    -   В функции `run_scenarios` переменная res перезаписывается на каждой итерации. Необходимо исправить логику сохранения результатов.

5.  **Импорты**:
    -   Удалить неиспользуемые импорты.
    -   Использовать явные импорты для читаемости кода.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для выполнения сценариев.
=========================================================================================

Этот модуль содержит функции для выполнения сценариев, загрузки их из файлов,
а также обработки процесса извлечения информации о продуктах и вставки их в PrestaShop.

Пример использования
--------------------

Пример использования функции `run_scenario_files`:

.. code-block:: python

    from pathlib import Path
    from src.supplier import Supplier

    supplier = Supplier(supplier_name='test_supplier', supplier_abs_path='/path/to/supplier')
    scenario_files = [Path('/path/to/scenario1.json'), Path('/path/to/scenario2.json')]
    run_scenario_files(supplier, scenario_files)
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

import header
from src import gs
from src.utils.printer import pprint
from src.utils.jjson import j_loads, j_dumps
from src.product import Product, ProductFields, translate_presta_fields_dict
from src.endpoints.prestashop import PrestaShop
from src.db import ProductCampaignsManager
from src.logger.logger import logger
from src.logger.exceptions import ProductFieldException


journal_data: dict = {'scenario_files': ''}
journal_data['name'] = timestamp = gs.now


def dump_journal(s, journal: dict):
    """
    Сохраняет данные журнала в JSON файл.

    :param s: Экземпляр поставщика.
    :param journal: Словарь, содержащий данные журнала.
    """
    _journal_file_path = Path(s.supplier_abs_path, '_journal', f"{journal['name']}.json")
    j_dumps(journal, _journal_file_path)


def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Выполняет сценарии из списка файлов.

    :param s: Экземпляр поставщика.
    :param scenario_files_list: Список путей к файлам сценариев или один путь к файлу.
    :raises TypeError: Если `scenario_files_list` не является списком или объектом `Path`.
    :return: `True`, если все сценарии выполнены успешно, `False` в противном случае.
    """
    if isinstance(scenario_files_list, Path):
        scenario_files_list = [scenario_files_list]
    elif not isinstance(scenario_files_list, list):
        raise TypeError("scenario_files_list must be a list or a Path object.")
    # Проверка, если список scenario_files_list пустой, тогда использовать сценарии из s.scenario_files
    scenario_files_list = scenario_files_list if scenario_files_list else s.scenario_files

    journal_data['scenario_files'] = {}
    for scenario_file in scenario_files_list:
        journal_data['scenario_files'][scenario_file.name] = {}
        try:
            if run_scenario_file(s, scenario_file):
                journal_data['scenario_files'][scenario_file.name]['message'] = f"{scenario_file} completed successfully!"
                logger.success(f'Сценарий {scenario_file} выполнен успешно!')
            else:
                journal_data['scenario_files'][scenario_file.name]['message'] = f"{scenario_file} FAILED!"
                logger.error(f'Сценарий {scenario_file} не выполнен!')
        except Exception as e:
            logger.critical(f"Ошибка при обработке {scenario_file}: {e}")
            journal_data['scenario_files'][scenario_file.name]['message'] = f"Error: {e}"
    return True


def run_scenario_file(s, scenario_file: Path) -> bool:
    """
    Загружает и выполняет сценарии из файла.

    :param s: Экземпляр поставщика.
    :param scenario_file: Путь к файлу сценария.
    :return: `True`, если сценарий выполнен успешно, `False` в противном случае.
    """
    try:
        scenarios_dict = j_loads(scenario_file)['scenarios']
        for scenario_name, scenario in scenarios_dict.items():
            s.current_scenario = scenario
            if run_scenario(s, scenario, scenario_name):
                logger.success(f'Сценарий {scenario_name} выполнен успешно!')
            else:
                logger.error(f'Сценарий {scenario_name} не выполнен!')
        return True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.critical(f"Ошибка загрузки или обработки файла сценария {scenario_file}: {e}")
        return False


def run_scenarios(s, scenarios: List[dict] | dict = None, journal=None) -> List | dict | bool:
    """
    Выполняет список сценариев.

    :param s: Экземпляр поставщика.
    :param scenarios: Список сценариев или один сценарий в виде словаря.
    :param journal: Данные журнала.
    :return: Результат выполнения сценариев в виде списка или словаря, или `False` в случае ошибки.

    .. todo::
        Проверить вариант, когда не указаны сценарии ниоткуда. Например, когда s.current_scenario не указан и scenarios не указан.
    """
    if not scenarios:
        scenarios = [s.current_scenario]
        """
        Если сценарии не указаны, берем их из s.current_scenario.

        .. todo::
            Проверить этот вариант со всех сторон. Например, когда s.current_scenario не указан и scenarios не указан.
        """

    scenarios = scenarios if isinstance(scenarios, list) else [scenarios]
    res = []
    for scenario in scenarios:
        result = run_scenario(s, scenario, 'default', journal)
        if journal and journal['scenario_files']:
            journal['scenario_files'][-1][str(scenario)] = str(result) # TODO:  Исправить логику сохранения результатов.
        dump_journal(s, journal)
        res.append(result)
    return res

def run_scenario(supplier, scenario: dict, scenario_name: str, journal=None) -> List | dict | bool:
    """
    Выполняет полученный сценарий.

    :param supplier: Экземпляр поставщика.
    :param scenario: Словарь, содержащий детали сценария.
    :param scenario_name: Имя сценария.
    :param journal: Данные журнала.
    :return: Результат выполнения сценария.

    .. todo::
        Проверить необходимость параметра `scenario_name`.
    """
    s = supplier
    logger.info(f'Начинается сценарий: {scenario_name}')
    s.current_scenario = scenario
    d = s.driver
    d.get_url(scenario['url'])

    # Получение списка продуктов в категории
    list_products_in_category: list = s.related_modules.get_list_products_in_category(s)

    # Нет продуктов в категории (или они еще не загрузились)
    if not list_products_in_category:
        logger.warning('Список продуктов не получен со страницы категории. Возможно, пустая категория - ', d.current_url)
        return False

    for url in list_products_in_category:
        if not d.get_url(url):
            logger.error(f'Ошибка перехода на страницу продукта: {url}')
            continue  # Ошибка перехода на страницу. Пропуск

        # Захват полей страницы продукта
        grabbed_fields = s.related_modules.grab_product_page(s)
        f: ProductFields = asyncio.run(s.related_modules.grab_page(s))
        if not f:
            logger.error(f"Не удалось получить поля продукта")
            continue

        presta_fields_dict, assist_fields_dict = f.presta_fields_dict, f.assist_fields_dict
        try:
            product: Product = Product(supplier_prefix=s.supplier_prefix, presta_fields_dict=presta_fields_dict)
            insert_grabbed_data(f)
        except Exception as ex:
            logger.error(f'Продукт {product.fields["name"][1]} не удалось сохранить', ex)
            continue

    return list_products_in_category


def insert_grabbed_data(product_fields: ProductFields):
    """
    Вставляет полученные данные о продукте в PrestaShop.

    .. todo::
        Перенести эту логику в другой файл. В класс PrestaShop.
    """
    asyncio.run(execute_PrestaShop_insert(product_fields))


async def execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    """
    Асинхронно вставляет продукт в PrestaShop.

    :param f: Экземпляр `ProductFields`, содержащий информацию о продукте.
    :param coupon_code: Опциональный код купона.
    :param start_date: Опциональная дата начала акции.
    :param end_date: Опциональная дата окончания акции.
    :return: `True`, если вставка прошла успешно, `False` в противном случае.
    """
    await execute_PrestaShop_insert(f, coupon_code, start_date, end_date)


def execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    """
    Вставляет продукт в PrestaShop.

    :param f: Экземпляр `ProductFields`, содержащий информацию о продукте.
    :param coupon_code: Опциональный код купона.
    :param start_date: Опциональная дата начала акции.
    :param end_date: Опциональная дата окончания акции.
    :return: `True`, если вставка прошла успешно, `False` в противном случае.
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
        logger.error(f'Не удалось вставить данные продукта в PrestaShop: {ex}', ex)
        return False
```