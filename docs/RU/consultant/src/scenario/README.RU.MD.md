# Анализ кода модуля `src.scenario`

**Качество кода**
7
- Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Присутствует подробное описание модуля и его основных компонентов.
    - Используется `mermaid` для визуализации процесса выполнения.
    - Есть пример сценария в формате JSON.
- Минусы
    - Отсутствует описание работы внутри функций.
    - Нет импортов необходимых модулей.
    - Используются общие исключения, вместо более специфичных.
    - Не используется `logger` для логирования ошибок.
    - Не используется `j_loads` для загрузки `json`.
    - Отсутствуют `docstring` для функций и переменных.
    - Не соблюдены рекомендации по использованию кавычек в python.

**Рекомендации по улучшению**
1.  Добавить импорты необходимых модулей: `json`, `requests`, `asyncio`, `pathlib`, `typing`.
2.  Заменить `json.load` на `j_loads` из `src.utils.jjson`.
3.  Использовать `logger` из `src.logger` для логирования ошибок.
4.  Добавить `docstring` к функциям и переменным.
5.  Уточнить исключения, используя специфичные типы ошибок, а не `Exception`.
6.  Добавить обработку ошибок с помощью `try-except` и `logger.error`.
7.  Использовать одинарные кавычки `'` в коде Python, двойные кавычки `"` только для вывода.
8.  Добавить комментарии с объяснением кода.
9.  Внедрить проверку типов для аргументов функций.
10. Добавить обработку ошибок при записи журнала.

**Оптимизированный код**

```python
"""
Модуль `src.scenario`
=========================================================================================

Модуль `src.scenario` предназначен для автоматизации взаимодействия с поставщиками,
используя сценарии, описанные в JSON-файлах. Он адаптирует процесс извлечения и
обработки данных о продуктах с веб-сайтов поставщиков и синхронизирует эту информацию
с базой данных (например, PrestaShop). Модуль включает чтение сценариев,
взаимодействие с веб-сайтами, обработку данных, запись журнала выполнения и
организацию всего процесса.

Пример использования
--------------------

Пример использования функций модуля:

.. code-block:: python

    from src.scenario import run_scenario_files
    from src.utils.jjson import j_loads
    from pathlib import Path
    import asyncio

    async def main():
        settings = {'db_host': 'localhost', 'db_user': 'user', 'db_pass': 'password', 'db_name': 'database'}
        scenario_files = [Path('scenario1.json'), Path('scenario2.json')]
        await run_scenario_files(settings, scenario_files)

    if __name__ == '__main__':
         asyncio.run(main())
"""
import asyncio
import json
from pathlib import Path
from typing import Any, Dict, List

import requests
from src.logger import logger
from src.utils.jjson import j_loads, j_loads_ns


async def run_scenario_files(s: Dict[str, Any], scenario_files_list: List[Path]) -> None:
    """
    Асинхронно запускает обработку списка файлов сценариев.

    Args:
        s (Dict[str, Any]): Словарь с настройками.
        scenario_files_list (List[Path]): Список путей к файлам сценариев.

    Raises:
        FileNotFoundError: Если файл сценария не найден.
        json.JSONDecodeError: Если файл сценария содержит невалидный JSON.
        Exception: При любых других проблемах при работе со сценариями.

    Example:
        >>> from pathlib import Path
        >>> settings = {'db_host': 'localhost', 'db_user': 'user', 'db_pass': 'password', 'db_name': 'database'}
        >>> scenario_files = [Path('scenario1.json'), Path('scenario2.json')]
        >>> asyncio.run(run_scenario_files(settings, scenario_files))
    """
    # Проходит по списку файлов сценариев.
    for scenario_file in scenario_files_list:
        try:
            # Запускает обработку каждого файла сценария.
            await run_scenario_file(s, scenario_file)
        except FileNotFoundError as e:
            logger.error(f'Файл сценария не найден: {scenario_file}', exc_info=e)
            ... # Точка остановки
        except json.JSONDecodeError as e:
            logger.error(f'Ошибка декодирования JSON в файле: {scenario_file}', exc_info=e)
            ...# Точка остановки
        except Exception as e:
            logger.error(f'Непредвиденная ошибка при обработке файла: {scenario_file}', exc_info=e)
            ...# Точка остановки


async def run_scenario_file(s: Dict[str, Any], scenario_file: Path) -> None:
    """
    Асинхронно загружает и обрабатывает сценарии из файла.

    Args:
        s (Dict[str, Any]): Словарь с настройками.
        scenario_file (Path): Путь к файлу сценария.

    Raises:
        FileNotFoundError: Если файл сценария не найден.
        json.JSONDecodeError: Если файл сценария содержит невалидный JSON.
        Exception: При любых других проблемах при работе со сценариями.

    Example:
        >>> from pathlib import Path
        >>> settings = {'db_host': 'localhost', 'db_user': 'user', 'db_pass': 'password', 'db_name': 'database'}
        >>> scenario_file = Path('scenario1.json')
        >>> asyncio.run(run_scenario_file(settings, scenario_file))

    """
    try:
        # Код загружает содержимое JSON файла
        scenario_data = await j_loads(scenario_file)
        # Код проходит по всем сценариям в файле
        for scenario_name, scenario in scenario_data.get('scenarios', {}).items():
            # Код выполняет каждый сценарий
            await run_scenario(s, scenario)
    except FileNotFoundError as e:
        logger.error(f'Файл сценария не найден: {scenario_file}', exc_info=e)
        ...# Точка остановки
    except json.JSONDecodeError as e:
        logger.error(f'Ошибка декодирования JSON в файле: {scenario_file}', exc_info=e)
        ... # Точка остановки
    except Exception as e:
        logger.error(f'Непредвиденная ошибка при обработке файла: {scenario_file}', exc_info=e)
        ...# Точка остановки

async def run_scenario(s: Dict[str, Any], scenario: Dict[str, Any]) -> None:
    """
    Асинхронно выполняет сценарий: переходит по URL, извлекает данные о продуктах и сохраняет их.

    Args:
        s (Dict[str, Any]): Словарь с настройками.
        scenario (Dict[str, Any]): Словарь, содержащий сценарий (например, с URL, категориями).

    Raises:
        requests.exceptions.RequestException: Если есть проблемы с запросом к веб-сайту.
        Exception: При любых других проблемах в процессе обработки сценария.

    Example:
        >>> settings = {'db_host': 'localhost', 'db_user': 'user', 'db_pass': 'password', 'db_name': 'database'}
        >>> scenario = {
        ...     'url': 'https://example.com/category/mineral-creams/',
        ...     'name': 'минеральные+кремы',
        ...     'presta_categories': {'default_category': 12345, 'additional_categories': [12346, 12347]}
        ... }
        >>> asyncio.run(run_scenario(settings, scenario))
    """
    journal = []
    try:
        # Код получает URL из сценария.
        url = scenario.get('url')
        if not url:
            logger.error(f'URL не найден в сценарии: {scenario}')
            return
        # Код переходит по URL
        response = requests.get(url)
        response.raise_for_status() # Код проверяет статус ответа
        # TODO: Здесь нужно добавить код для извлечения данных о продуктах из HTML
        # TODO: Добавить создание объекта продукта и сохранение его в базу данных.
        # Код добавляет информацию в журнал.
        journal.append({'scenario': scenario.get('name'), 'status': 'success', 'url': url})
    except requests.exceptions.RequestException as e:
        logger.error(f'Ошибка при запросе к URL: {url}', exc_info=e)
        journal.append({'scenario': scenario.get('name'), 'status': 'error', 'url': url, 'error': str(e)})
    except Exception as e:
        logger.error(f'Непредвиденная ошибка при обработке сценария: {scenario}', exc_info=e)
        journal.append({'scenario': scenario.get('name'), 'status': 'error', 'url': url, 'error': str(e)})
    finally:
        # Код сохраняет журнал
        await dump_journal(s, journal)



async def dump_journal(s: Dict[str, Any], journal: List[Dict[str, Any]]) -> None:
    """
    Асинхронно сохраняет журнал выполнения сценариев в файл.

    Args:
        s (Dict[str, Any]): Словарь с настройками.
        journal (List[Dict[str, Any]]): Список записей журнала выполнения.

    Raises:
        Exception: При проблемах с записью в файл.

    Example:
        >>> settings = {'db_host': 'localhost', 'db_user': 'user', 'db_pass': 'password', 'db_name': 'database'}
        >>> journal = [{'scenario': 'test', 'status': 'success'}]
        >>> asyncio.run(dump_journal(settings, journal))
    """
    try:
       # Код формирует имя файла журнала
        journal_file = Path('journal.json')
        # Код сохраняет журнал в JSON файл.
        async with aiofiles.open(journal_file, mode='w') as f:
             await f.write(json.dumps(journal, indent=4))
    except Exception as e:
        # Код логирует ошибку, если не удалось записать журнал
        logger.error(f'Ошибка при записи журнала в файл: {journal_file}', exc_info=e)
        ...# Точка остановки


async def main():
    """
    Основная функция для запуска модуля.
    """
    # Пример настроек
    settings = {'db_host': 'localhost', 'db_user': 'user', 'db_pass': 'password', 'db_name': 'database'}
    # Пример списка файлов сценариев
    scenario_files = [Path('scenario1.json'), Path('scenario2.json')]
    # Код запускает выполнение сценариев
    await run_scenario_files(settings, scenario_files)
    ...# Точка остановки


if __name__ == '__main__':
    # Код запускает асинхронный main
    asyncio.run(main())

```