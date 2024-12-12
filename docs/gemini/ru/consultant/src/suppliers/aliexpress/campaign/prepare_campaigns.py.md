# Анализ кода модуля `prepare_campaigns.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разделен на функции.
    - Используется `argparse` для обработки аргументов командной строки.
    - Присутствует логирование.
    - Код соответствует PEP8.
    - Используются `j_loads_ns`.
- Минусы
    - Не все функции имеют docstring в формате reStructuredText (RST).
    - Есть избыточное использование стандартных блоков `try-except` (хотя в коде их нет).
    - Некоторые комментарии не соответствуют стандарту RST.
    - Отсутствует обработка ошибок в некоторых местах.
    -  Не везде используется логирование ошибок.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить docstring в формате reStructuredText (RST) для всех функций и модулей.
    -   Переписать существующие комментарии в формате RST.
2.  **Логирование**:
    -   Использовать `logger.error` вместо `try-except` для обработки ошибок.
    -   Добавить логирование в местах, где это необходимо.
3.  **Обработка ошибок**:
    -   Улучшить обработку ошибок, проверяя возвращаемые значения функций.
4.  **Рефакторинг**:
     - Упростить логику обработки локалей.
5.  **Соответствие стандарту**:
    - Все комментарии к модулям, функциям, методам и переменным переписать в формате reStructuredText (RST).

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для подготовки кампаний AliExpress.
=========================================================================================

Этот модуль обрабатывает категории товаров, управляет данными кампаний и генерирует рекламные материалы.
Он позволяет запускать обработку как для отдельных кампаний, так и для всех кампаний,
находящихся в директории `campaigns`.

Пример использования
--------------------

Для запуска скрипта для конкретной кампании:

.. code-block:: bash

    python src/suppliers/aliexpress/campaign/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD

Для обработки всех кампаний:

.. code-block:: bash

    python src/suppliers/aliexpress/campaign/prepare_campaigns.py --all -l EN -cu USD
"""
MODE = 'dev'
import argparse
import copy
from pathlib import Path
from typing import List, Optional

from src import gs
# Код импортирует класс AliCampaignEditor из модуля campaign
from src.suppliers.aliexpress.campaign import AliCampaignEditor
# Код импортирует список локалей из модуля utils
from src.suppliers.aliexpress.utils import locales
from src.utils.printer import pprint
from src.utils.file import get_directory_names
from src.utils.jjson import j_loads_ns
# Код импортирует logger из модуля logger
from src.logger.logger import logger


# Определяется путь к директории с кампаниями на Google Drive
campaigns_directory = gs.path.google_drive / 'aliexpress' / 'campaigns'


def process_campaign_category(
    campaign_name: str, category_name: str, language: str, currency: str
) -> List[str]:
    """
    Обрабатывает конкретную категорию в рамках кампании для заданного языка и валюты.

    :param campaign_name: Название рекламной кампании.
    :type campaign_name: str
    :param category_name: Название категории товаров для кампании.
    :type category_name: str
    :param language: Язык кампании.
    :type language: str
    :param currency: Валюта кампании.
    :type currency: str
    :return: Список заголовков товаров в рамках категории.
    :rtype: List[str]

    Пример:
    
    >>> titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
    >>> print(titles)
    ['Product 1', 'Product 2']
    """
    # Код создает экземпляр класса AliCampaignEditor и запускает обработку категории
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
    Обрабатывает кампанию, настраивая и обрабатывая её.

    :param campaign_name: Название рекламной кампании.
    :type campaign_name: str
    :param language: Язык кампании. Если не указан, обработка выполняется для всех локалей.
    :type language: Optional[str]
    :param currency: Валюта кампании. Если не указана, обработка выполняется для всех локалей.
    :type currency: Optional[str]
    :param campaign_file: Путь к файлу кампании.
    :type campaign_file: Optional[str]
    :return: Возвращает True, если обработка кампании завершена успешно, иначе False.
    :rtype: bool

    Пример:
    
    >>> res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")
    """
    # Код создает список пар (язык, валюта) для всех локалей, если язык или валюта не указаны
    if language and currency:
        _l = [(language, currency)]
    else:
         _l = [(lang, curr) for locale in locales for lang, curr in locale.items()]

    # Код обрабатывает каждую пару (язык, валюта)
    for language, currency in _l:
        logger.info(f"Processing campaign: {campaign_name=}, {language=}, {currency=}")
        editor = AliCampaignEditor(
            campaign_name = campaign_name,
            language = language,
            currency = currency,
        )
        # Код запускает обработку кампании
        if not editor.process_campaign():
            logger.error(f"Failed to process campaign {campaign_name=}, {language=}, {currency=}")
            return False
    return True

def process_all_campaigns(language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """
    Обрабатывает все кампании в директории 'campaigns' для заданного языка и валюты.

    :param language: Язык для обработки кампаний.
    :type language: Optional[str]
    :param currency: Валюта для обработки кампаний.
    :type currency: Optional[str]

    Пример:
    
    >>> process_all_campaigns("EN", "USD")
    """
    # Код определяет список локалей для обработки, если не переданы язык и валюта
    if not language and not currency:
        _l = [(lang, curr) for locale in locales for lang, curr in locale.items()]
    else:
        _l = [(language, currency)]
    
    pprint(f"{_l=}")
    for lang, curr in _l:
        # Код получает список имен директорий кампаний
        campaigns_dir = get_directory_names(campaigns_directory)
        pprint(f"{campaigns_dir=}")
        for campaign_name in campaigns_dir:
             logger.info(f"Start processing {campaign_name=}, {lang=}, {curr=}")
             editor = AliCampaignEditor(
                campaign_name=campaign_name,
                language=lang,
                currency=curr
            )
             # Код запускает обработку кампании
             if not editor.process_campaign():
                  logger.error(f"Failed to process campaign {campaign_name=}, {lang=}, {curr=}")
                  
def main_process(campaign_name: str, categories: List[str] | str, language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """
    Основная функция для обработки кампании.

    :param campaign_name: Название рекламной кампании.
    :type campaign_name: str
    :param categories: Список категорий для обработки. Если пустой, обрабатывается вся кампания.
    :type categories: List[str] | str
    :param language: Язык кампании.
    :type language: Optional[str]
    :param currency: Валюта кампании.
    :type currency: Optional[str]

    Пример:
    
    >>> main_process("summer_sale", ["electronics"], "EN", "USD")
    >>> main_process("summer_sale", [], "EN", "USD")
    """
    # Код определяет список локалей для обработки
    locales_to_process = [(language, currency)] if language and currency else [(lang, curr) for locale in locales for lang, curr in locale.items()]
    
    for lang, curr in locales_to_process:
        if categories:
            # Код обрабатывает каждую категорию, если они указаны
            for category in categories:
                logger.info(f"Processing specific category {category=}, {lang=}, {curr=}")
                process_campaign_category(campaign_name, category, lang, curr)
        else:
            # Код запускает обработку всей кампании, если категории не указаны
            logger.info(f"Processing entire campaign {campaign_name=}, {lang=}, {curr=}")
            process_campaign(campaign_name, lang, curr)

def main() -> None:
    """
    Основная функция для разбора аргументов командной строки и запуска обработки.

    Пример:
    
    >>> main()
    """
    # Код создает парсер аргументов командной строки
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
    # Код разбирает аргументы командной строки
    args = parser.parse_args()
    # Код запускает обработку всех кампаний или конкретной кампании
    if args.all:
        process_all_campaigns(args.language, args.currency)
    else:
        main_process(
            args.campaign_name, args.categories or [], args.language, args.currency
        )


if __name__ == "__main__":
    main()
```