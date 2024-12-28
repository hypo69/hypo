# Анализ кода модуля `prepare_campaigns.py`

**Качество кода**

-   Соответствие требованиям по оформлению кода: 7/10
    -   **Плюсы:**
        -   Используется `argparse` для обработки аргументов командной строки.
        -   Код разбит на функции, что улучшает читаемость и поддерживаемость.
        -   Присутствуют docstring для функций.
        -   Используется `logger` для логирования.
    -   **Минусы:**
        -   Не все docstring соответствуют формату reStructuredText (RST).
        -   Импорты не все приведены в соответствие с ранее обработанными файлами.
        -   Не везде используются `j_loads_ns`.
        -   В некоторых функциях есть избыточное использование `try-except`.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Привести все docstring к формату RST, включая параметры, возвращаемые значения и примеры.
    -   Добавить более подробные описания к модулю.
2.  **Импорты:**
    -   Проверить и добавить недостающие импорты.
    -   Привести импорты в соответствие с ранее обработанными файлами.
3.  **Обработка данных:**
    -   Убедиться, что `j_loads_ns` используется вместо `json.load` там, где это необходимо.
4.  **Логирование:**
    -   Избегать избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
5.  **Структура:**
    -   Рассмотреть возможность добавления констант для повторяющихся строк.
    -   Использовать более описательные имена переменных.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для подготовки рекламных кампаний AliExpress
=========================================================================================

Этот модуль обрабатывает категории товаров, управляет данными кампаний
и генерирует рекламные материалы для AliExpress.

Примеры использования
--------------------

Для запуска скрипта для конкретной кампании:

.. code-block:: bash

    python src/suppliers/aliexpress/campaign/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD

Для обработки всех кампаний:

.. code-block:: bash

    python src/suppliers/aliexpress/campaign/prepare_campaigns.py --all -l EN -cu USD
"""

import argparse
import copy
from pathlib import Path
from typing import List, Optional

from src import gs
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.utils import locales
from src.utils.printer import pprint
from src.utils.file import get_directory_names
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


# Путь к директории с кампаниями
campaigns_directory = gs.path.google_drive / 'aliexpress' / 'campaigns'

def process_campaign_category(
    campaign_name: str, category_name: str, language: str, currency: str
) -> List[str]:
    """
    Обрабатывает конкретную категорию в рамках кампании.

    :param campaign_name: Название рекламной кампании.
    :type campaign_name: str
    :param category_name: Название категории товаров.
    :type category_name: str
    :param language: Язык кампании.
    :type language: str
    :param currency: Валюта кампании.
    :type currency: str
    :return: Список заголовков продуктов в категории.
    :rtype: List[str]

    :Example:
    >>> titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
    >>> print(titles)
    [\'Product 1\', \'Product 2\']
    """
    #  Код создает и возвращает экземпляр класса AliCampaignEditor, вызывая метод process_campaign_category
    return AliCampaignEditor(
        campaign_name=campaign_name, language=language, currency=currency
    ).process_campaign_category(category_name)


def process_campaign(
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
    campaign_file: Optional[str] = None,
) -> bool:
    """
    Обрабатывает рекламную кампанию.

    :param campaign_name: Название рекламной кампании.
    :type campaign_name: str
    :param language: Язык кампании (необязательно). Если не указан, обрабатываются все языки.
    :type language: Optional[str]
    :param currency: Валюта кампании (необязательно). Если не указана, обрабатываются все валюты.
    :type currency: Optional[str]
    :param campaign_file: Путь к файлу кампании (необязательно).
    :type campaign_file: Optional[str]
    :return: True, если кампания обработана успешно, иначе False.
    :rtype: bool

    :Example:
        >>> res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")
    """
    # Формируется список пар (язык, валюта) для обработки.
    _locales_list = [(lang, curr) for locale in locales for lang, curr in locale.items()]

    # Если указаны язык и валюта, список фильтруется.
    if language and currency:
        _locales_list = [(language, currency)]

    # Код итерируется по списку пар язык-валюта для обработки кампании для каждого языка и валюты
    for language, currency in _locales_list:
        logger.info(f"Processing campaign: {campaign_name=}, {language=}, {currency=}")
        editor = AliCampaignEditor(
            campaign_name = campaign_name,
            language = language,
            currency = currency,
        )
        # Код вызывает метод process_campaign экземпляра AliCampaignEditor
        editor.process_campaign()

    return True


def process_all_campaigns(language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """
    Обрабатывает все кампании в директории 'campaigns'.

    :param language: Язык кампаний (необязательно).
    :type language: Optional[str]
    :param currency: Валюта кампаний (необязательно).
    :type currency: Optional[str]

    :Example:
        >>> process_all_campaigns("EN", "USD")
    """
    #  Формируется список пар (язык, валюта) для обработки всех кампаний.
    if not language and not currency:
        _locales_list = [(lang, curr) for locale in locales for lang, curr in locale.items()]
    else:
        _locales_list = [(language, currency)]
    pprint(f"{_locales_list=}")
    # Код итерируется по списку пар язык-валюта для обработки кампании для каждого языка и валюты
    for lang, curr in _locales_list:
        # Код получает список директорий в директории кампаний
        campaigns_dir = get_directory_names(campaigns_directory)
        pprint(f"{campaigns_dir=}")
        # Код итерируется по каждой кампании в списке
        for campaign_name in campaigns_dir:
             logger.info(f"Start processing {campaign_name=}, {lang=}, {curr=}")
             editor = AliCampaignEditor(
                 campaign_name=campaign_name,
                 language=lang,
                 currency=curr
             )
             # Код вызывает метод process_campaign экземпляра AliCampaignEditor
             editor.process_campaign()

def main_process(campaign_name: str, categories: List[str] | str, language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """
    Главная функция для обработки кампании.

    :param campaign_name: Название рекламной кампании.
    :type campaign_name: str
    :param categories: Список категорий для обработки. Если не указан, обрабатывается вся кампания.
    :type categories: List[str] | str
    :param language: Язык кампании (необязательно).
    :type language: Optional[str]
    :param currency: Валюта кампании (необязательно).
    :type currency: Optional[str]

    :Example:
        >>> main_process("summer_sale", ["electronics"], "EN", "USD")
        >>> main_process("summer_sale", [], "EN", "USD")
    """
    #  Определяются локали для обработки на основе предоставленных языка и валюты.
    locales_to_process = [(language, currency)] if language and currency else [(lang, curr) for locale in locales for lang, curr in locale.items()]
    # Код итерируется по списку пар язык-валюта для обработки кампании для каждого языка и валюты
    for lang, curr in locales_to_process:
        if categories:
            # Код обрабатывает каждую указанную категорию в списке
            for category in categories:
                 logger.info(f"Processing specific category {category=}, {lang=}, {curr=}")
                 process_campaign_category(campaign_name, category, lang, curr)
        else:
            # Если категории не указаны, обрабатывается вся кампания
             logger.info(f"Processing entire campaign {campaign_name=}, {lang=}, {curr=}")
             process_campaign(campaign_name, lang, curr)

def main() -> None:
    """
    Главная функция для запуска обработки кампаний.
    
    :Example:
        >>> main()
    """
    #  Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="Prepare AliExpress Campaign")
    parser.add_argument("campaign_name", type=str, help="Name of the campaign")
    parser.add_argument(
        "-c",
        "--categories",
        nargs="+",
        help="List of categories (if not provided, all categories will be used)",
    )
    parser.add_argument(
        "-l", "--language", type=str, default=None, help="Language for the campaign"
    )
    parser.add_argument(
        "-cu", "--currency", type=str, default=None, help="Currency for the campaign"
    )
    parser.add_argument("--all", action="store_true", help="Process all campaigns")

    # Код парсит аргументы командной строки
    args = parser.parse_args()

    # Код проверяет, был ли указан аргумент --all
    if args.all:
         # Код вызывает функцию process_all_campaigns для обработки всех кампаний
         process_all_campaigns(args.language, args.currency)
    else:
        # Код вызывает функцию main_process для обработки конкретной кампании
         main_process(
            args.campaign_name, args.categories or [], args.language, args.currency
        )

if __name__ == "__main__":
    main()
```