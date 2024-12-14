# Анализ кода модуля `src.scenario`

**Качество кода**
7
-  Плюсы
    -  Хорошая и подробная документация модуля в формате markdown.
    -  Структура документации соответствует заданным требованиям.
    -  Код разбит на логические блоки с описанием.
    -  Приведено описание основных компонентов и функций модуля.
-  Минусы
    -  В коде не хватает обработки ошибок с использованием `logger.error`.
    -  Не используются функции `j_loads` или `j_loads_ns` для чтения JSON.
    -  Отсутствует импорт необходимых модулей.
    -  Необходимо переписать docstring в формате RST.
    -  Отсутствуют примеры кода в RST.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` для чтения JSON.
2.  Добавить необходимые импорты.
3.  Переписать все docstring в формате RST.
4.  Использовать `logger.error` для обработки ошибок.
5.  Добавить примеры использования кода в формате RST.

**Оптимизированный код**

```python
"""
Модуль для автоматизации взаимодействия с поставщиками на основе сценариев.
=========================================================================

Этот модуль предназначен для автоматизации процессов извлечения данных о продуктах с веб-сайтов поставщиков
и их синхронизации с базами данных, такими как PrestaShop. Он включает в себя чтение сценариев из JSON-файлов,
взаимодействие с веб-сайтами, обработку данных и ведение журнала выполнения.

Пример использования
--------------------

Пример запуска обработки сценариев:

.. code-block:: python

    from src.scenario import main
    main()
"""
import asyncio
import json
import os
from typing import Any, Dict, List

import aiohttp
# from src.db.db import db  # TODO: пример импорта
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns


async def run_scenario_files(s: Dict[str, Any], scenario_files_list: List[str]) -> None:
    """
    Выполняет сценарии, описанные в файлах.

    :param s: Словарь настроек.
    :type s: Dict[str, Any]
    :param scenario_files_list: Список путей к файлам сценариев.
    :type scenario_files_list: List[str]
    :raises FileNotFoundError: Если файл сценария не найден.
    :raises json.JSONDecodeError: Если файл сценария содержит невалидный JSON.
    """
    if not isinstance(scenario_files_list, list):
        logger.error(f'Неверный тип данных {scenario_files_list=}')
        return
    for scenario_file in scenario_files_list:
        await run_scenario_file(s, scenario_file)


async def run_scenario_file(s: Dict[str, Any], scenario_file: str) -> None:
    """
    Загружает и выполняет сценарии из указанного файла.

    :param s: Словарь настроек.
    :type s: Dict[str, Any]
    :param scenario_file: Путь к файлу сценария.
    :type scenario_file: str
    :raises FileNotFoundError: Если файл сценария не найден.
    :raises json.JSONDecodeError: Если файл сценария содержит невалидный JSON.
    :raises Exception: При любых других проблемах при работе со сценариями.
    """
    try:
        # код исполняет открытие и чтение файла сценария
        with open(scenario_file, 'r', encoding='utf-8') as f:
            # код исполняет загрузку данных из JSON, используя j_loads
            scenario_data = j_loads(f)
    except FileNotFoundError as e:
        logger.error(f'Файл не найден: {scenario_file}', exc_info=True)
        return
    except json.JSONDecodeError as e:
        logger.error(f'Ошибка декодирования JSON в файле: {scenario_file}', exc_info=True)
        return
    except Exception as e:
        logger.error(f'Неизвестная ошибка при обработке файла: {scenario_file}', exc_info=True)
        return
    # код исполняет проверку существования ключа 'scenarios' в загруженных данных
    if 'scenarios' not in scenario_data:
         logger.error(f'Неверный формат файла {scenario_file=}')
         return
    # код исполняет итерацию по сценариям и их выполнение
    for _, scenario in scenario_data['scenarios'].items():
        await run_scenario(s, scenario)


async def run_scenario(s: Dict[str, Any], scenario: Dict[str, Any]) -> None:
    """
    Выполняет сценарий.

    :param s: Словарь настроек.
    :type s: Dict[str, Any]
    :param scenario: Словарь, содержащий сценарий.
    :type scenario: Dict[str, Any]
    :raises aiohttp.ClientError: Если есть проблемы с запросом к веб-сайту.
    :raises Exception: При любых других проблемах в процессе обработки сценария.
    """
    url = scenario.get('url')
    if not url:
         logger.error(f'В сценарии отсутствует URL {scenario=}')
         return
    # код исполняет переход по URL и последующее извлечение списка продуктов
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                 response.raise_for_status()
                 #TODO: пример как можно извлекать данные
                 # products = await response.json()
                 products = await response.text()
                 logger.debug(f'Успешно обработан url: {url}')
    except aiohttp.ClientError as e:
         logger.error(f'Ошибка при запросе к {url=}', exc_info=True)
         return
    except Exception as e:
         logger.error(f'Неизвестная ошибка при обработке сценария: {scenario=}', exc_info=True)
         return
    #TODO: пример кода обработки данных и запись в базу
    # if products:
    #      for product in products:
    #           # product['presta_categories'] =  scenario.get('presta_categories')
    #            try:
    #                 # await db.insert(product)
    #                 ...
    #            except Exception as e:
    #                 logger.error(f'Ошибка при записи в бд: {product=}', exc_info=True)
    #                 return


def dump_journal(s: Dict[str, Any], journal: List[Dict[str, Any]]) -> None:
    """
    Сохраняет журнал выполнения сценариев в файл.

    :param s: Словарь настроек.
    :type s: Dict[str, Any]
    :param journal: Список записей журнала выполнения.
    :type journal: List[Dict[str, Any]]
    :raises Exception: При проблемах с записью в файл.
    """
    try:
        # код исполняет запись журнала в файл
        with open(s.get('journal_file', 'journal.json'), 'w', encoding='utf-8') as f:
            json.dump(journal, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.error('Ошибка при записи журнала в файл', exc_info=True)


async def main():
    """
    Основная функция для запуска модуля.

    :raises Exception: При любых критических ошибках во время выполнения.
    """
    s = {
        'scenario_dir': 'scenario',
        'journal_file': 'journal.json',
        'debug': True,
        # TODO:  пример добавления настроек для БД
        # 'db': {
        #     'host': 'localhost',
        #     'port': 5432,
        #     'user': 'user',
        #     'password': 'password',
        #     'database': 'database',
        # }
    }
    # код исполняет инициализацию настроек
    if s.get('debug'):
         logger.setLevel('DEBUG')
    else:
         logger.setLevel('INFO')
    # код исполняет проверку существования директории со сценариями
    if not os.path.exists(s.get('scenario_dir', 'scenario')):
        logger.error(f'Директория не существует {s.get("scenario_dir", "scenario")=}')
        return
    scenario_files_list = [
        os.path.join(s.get('scenario_dir', 'scenario'), file)
        for file in os.listdir(s.get('scenario_dir', 'scenario'))
        if file.endswith('.json')
    ]
    # код исполняет проверку наличия файлов со сценариями
    if not scenario_files_list:
         logger.error('Не найдено файлов со сценариями')
         return
    # код исполняет запуск обработки сценариев
    await run_scenario_files(s, scenario_files_list)
    #TODO: пример добавления журнала
    # journal = []
    # dump_journal(s, journal)
    return


if __name__ == '__main__':
    # код исполняет запуск основной функции
    asyncio.run(main())
```