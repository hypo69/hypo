# Анализ кода модуля `src.scenario`

**Качество кода**
6
- Плюсы
    - Документация в Markdown
    - Наличие описания работы модуля и его основных компонентов
    - Присутствие блок-схемы, описывающей логику работы модуля
    - Есть пример JSON-сценария

- Минусы
    - Не используются docstrings и reStructuredText для описания функций и переменных
    - Не используются `j_loads` или `j_loads_ns` для загрузки JSON
    - Нет обработки ошибок с помощью `logger.error`
    - Отсутствуют импорты
    - Наличие лишних комментариев в `markdown`

**Рекомендации по улучшению**

1.  Переписать документацию в формате reStructuredText (RST) для корректного отображения в Sphinx.
2.  Использовать `j_loads` или `j_loads_ns` для загрузки JSON.
3.  Добавить обработку ошибок через `logger.error`.
4.  Добавить необходимые импорты.
5.  Удалить лишние комментарии в `markdown`, оставив только reStructuredText.

**Оптимизированный код**

```python
"""
Модуль для автоматизации взаимодействия с поставщиками на основе сценариев, описанных в JSON-файлах.
====================================================================================================

Этот модуль автоматизирует процесс извлечения и обработки данных о продуктах с веб-сайтов поставщиков
и синхронизирует эту информацию с базой данных (например, PrestaShop).

Основные функции модуля:

1.  **Чтение сценариев**: Загрузка сценариев из JSON-файлов, содержащих информацию о продуктах и URL-адресах.
2.  **Взаимодействие с веб-сайтами**: Обработка URL-адресов из сценариев для извлечения данных о продуктах.
3.  **Обработка данных**: Преобразование извлеченных данных в формат, подходящий для базы данных, и их сохранение.
4.  **Логирование выполнения**: Ведение журналов с деталями выполнения сценариев и результатами.

Структура модуля:

- :func:`run_scenario_files`: Выполняет сценарии из списка файлов.
- :func:`run_scenario_file`: Загружает и выполняет сценарии из одного файла.
- :func:`run_scenario`: Выполняет индивидуальный сценарий.
- :func:`dump_journal`: Сохраняет журнал выполнения.
- :func:`main`: Основная функция для запуска модуля.

Пример использования
--------------------

Для использования модуля необходимо настроить параметры подключения к базе данных,
а также описать сценарии в формате JSON.

.. code-block:: python

    from src.scenario import main
    main()
"""
import asyncio
import json
import os
from typing import Any, Dict, List

from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger

def run_scenario_files(s: Any, scenario_files_list: List[str]) -> None:
    """
    Выполняет сценарии из списка файлов.

    :param s: Объект настроек.
    :type s: Any
    :param scenario_files_list: Список путей к файлам со сценариями.
    :type scenario_files_list: List[str]
    :raises FileNotFoundError: Если файл сценария не найден.
    :raises json.JSONDecodeError: Если файл сценария содержит невалидный JSON.
    """
    for scenario_file in scenario_files_list:
        try:
            # код исполняет запуск сценария из файла
            run_scenario_file(s, scenario_file)
        except FileNotFoundError as e:
           logger.error(f'Файл сценария не найден: {scenario_file}', exc_info=True)
        except json.JSONDecodeError as e:
            logger.error(f'Некорректный JSON в файле сценария: {scenario_file}', exc_info=True)
        except Exception as e:
            logger.error(f'Ошибка при выполнении сценариев из файла: {scenario_file}', exc_info=True)

def run_scenario_file(s: Any, scenario_file: str) -> None:
    """
    Загружает и выполняет сценарии из одного файла.

    :param s: Объект настроек.
    :type s: Any
    :param scenario_file: Путь к файлу со сценариями.
    :type scenario_file: str
    :raises FileNotFoundError: Если файл сценария не найден.
    :raises json.JSONDecodeError: Если файл сценария содержит невалидный JSON.
    :raises Exception: При других ошибках во время выполнения сценария.
    """
    try:
        # код исполняет открытие файла и загрузку json
        with open(scenario_file, 'r', encoding='utf-8') as f:
            scenario_data = j_loads(f)
        for scenario_name, scenario in scenario_data.get('scenarios', {}).items():
            # код исполняет запуск сценария
            run_scenario(s, scenario)
    except FileNotFoundError as e:
       logger.error(f'Файл сценария не найден: {scenario_file}', exc_info=True)
    except json.JSONDecodeError as e:
        logger.error(f'Некорректный JSON в файле сценария: {scenario_file}', exc_info=True)
    except Exception as e:
        logger.error(f'Ошибка при выполнении сценария из файла: {scenario_file}', exc_info=True)

async def run_scenario(s: Any, scenario: Dict[str, Any]) -> None:
    """
    Выполняет индивидуальный сценарий.

    :param s: Объект настроек.
    :type s: Any
    :param scenario: Словарь, содержащий данные сценария.
    :type scenario: Dict[str, Any]
    :raises requests.exceptions.RequestException: Если есть проблемы с запросом к веб-сайту.
    :raises Exception: При других ошибках во время обработки сценария.
    """
    try:
       # Код выполняет навигацию по URL и обработку данных
        url = scenario.get('url')
        if not url:
            logger.error(f'URL не найден в сценарии: {scenario}')
            return
        # TODO: здесь должна быть логика для работы с сайтом и БД.
        logger.info(f'Обработка URL: {url}')
        ...
    except Exception as e:
         logger.error(f'Ошибка при обработке сценария: {scenario}', exc_info=True)

def dump_journal(s: Any, journal: List[Any]) -> None:
    """
    Сохраняет журнал выполнения в файл.

    :param s: Объект настроек.
    :type s: Any
    :param journal: Список записей журнала выполнения.
    :type journal: List[Any]
    :raises Exception: Если есть проблемы при записи в файл.
    """
    try:
        # Код выполняет сохранение журнала в файл
        journal_file = s.get('journal_file', 'journal.json')
        with open(journal_file, 'w', encoding='utf-8') as f:
            json.dump(journal, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.error(f'Ошибка при записи журнала в файл: {journal_file}', exc_info=True)

def main() -> None:
    """
    Основная функция для запуска модуля.

    :raises Exception: При возникновении критических ошибок во время выполнения.
    """
    s = {
         'journal_file': 'journal.json',
         'scenario_dir': 'scenarios' # TODO: change path
        }
    try:
        # Код исполняет запуск обработки файлов сценариев
        scenario_files = [os.path.join(s['scenario_dir'], f) for f in os.listdir(s['scenario_dir']) if f.endswith('.json')]
        run_scenario_files(s, scenario_files)
        logger.info('Завершено выполнение сценариев')
    except Exception as e:
        logger.error('Критическая ошибка при выполнении модуля', exc_info=True)

if __name__ == '__main__':
    main()
```