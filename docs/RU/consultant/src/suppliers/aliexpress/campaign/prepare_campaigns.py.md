# Анализ кода модуля `prepare_campaigns.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает понимание и поддержку.
    - Присутствует документация в формате docstring для функций.
    - Используется `argparse` для обработки аргументов командной строки.
    - Логирование осуществляется через `logger`.
    - Используется `j_loads_ns` для загрузки данных из JSON.
- Минусы
    - Не все docstring соответствуют стандарту Sphinx (отсутствуют `Returns`, `Args`, `Example` для некоторых функций).
    - Не везде используется `logger.error` для обработки исключений.
    - Отсутствует описание модуля в начале файла.
    - Использование `copy` не наблюдается, хотя импорт есть.
    - Излишнее использование `pprint`.
    - Нарушение стиля написания кода: где-то используем одинарные кавычки где-то двойные.

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить описание модуля в начале файла.
    - Заполнить отсутствующие `Args`, `Returns`, `Example` в docstring для всех функций.
    - Привести все docstring к единому стандарту Sphinx.
2.  **Обработка ошибок:**
    -  Заменить `print` на `logger.info` или `logger.debug` в цикле вывода информации о процессе, в `process_all_campaigns`.
    - Использовать `logger.error` для обработки исключений в функциях.
3.  **Стиль кода:**
    - Использовать одинарные кавычки для строк в коде Python, двойные только в операциях вывода.
    - Удалить неиспользуемый импорт `copy`.
    - Избавиться от избыточного использования `pprint`, заменив на `logger.info`.
4.  **Улучшение логики:**
    - Упростить логику обработки локалей.
5.  **Комментарии:**
   - Уточнить комментарии, где это необходимо.
6.  **Унификация импортов:**
    - Всегда использовать `from src.logger.logger import logger`.
   
**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для подготовки кампаний AliExpress.
=========================================================================================

Этот модуль отвечает за обработку кампаний AliExpress, включая загрузку данных о кампаниях,
обработку категорий, управление языками и валютами, и создание рекламных материалов.

Модуль предоставляет функциональность для обработки конкретных кампаний по категориям,
а также для обработки всех кампаний в директории.

Пример использования
--------------------

Пример запуска скрипта для конкретной кампании:

.. code-block:: python

    python src/suppliers/aliexpress/campaign/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD

Пример обработки всех кампаний:

.. code-block:: python

    python src/suppliers/aliexpress/campaign/prepare_campaigns.py --all -l EN -cu USD
"""
import argparse
from pathlib import Path
from typing import List, Optional

from src import gs
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.utils import locales
from src.utils.file import get_directory_names
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

# Define the path to the directory with campaigns
campaigns_directory = gs.path.google_drive / 'aliexpress' / 'campaigns'


def process_campaign_category(
    campaign_name: str, category_name: str, language: str, currency: str
) -> List[str]:
    """
    Обрабатывает конкретную категорию в рамках кампании.

    Args:
        campaign_name (str): Название рекламной кампании.
        category_name (str): Название категории для обработки.
        language (str): Язык кампании.
        currency (str): Валюта кампании.

    Returns:
        List[str]: Список заголовков товаров в данной категории.

    Example:
        >>> titles: List[str] = process_campaign_category('summer_sale', 'electronics', 'EN', 'USD')
        >>> print(titles)
        ['Product 1', 'Product 2']
    """
    # Создание экземпляра класса AliCampaignEditor и запуск процесса обработки категории
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
    Обрабатывает кампанию для заданных языка и валюты.

    Args:
        campaign_name (str): Название рекламной кампании.
        language (Optional[str]): Язык кампании. Если не указан, обрабатывает все локали.
        currency (Optional[str]): Валюта кампании. Если не указана, обрабатывает все локали.
        campaign_file (Optional[str]): Путь к файлу кампании (необязательно).

    Returns:
        bool: True, если кампания обработана успешно, иначе False.

    Example:
        >>> res = process_campaign('summer_sale', 'EN', 'USD', 'campaign_file.json')
    """
    # Формируем список локалей для обработки
    _l = [(lang, curr) for locale in locales for lang, curr in locale.items()]
    # Если указаны язык и валюта, фильтруем список
    if language and currency:
        _l = [(language, currency)]

    # Проходим по всем локалям и обрабатываем кампанию
    for language, currency in _l:
        logger.info(f'Processing campaign: {campaign_name=}, {language=}, {currency=}')
        editor = AliCampaignEditor(
            campaign_name=campaign_name,
            language=language,
            currency=currency,
        )
        editor.process_campaign()

    return True  # Предполагаем, что кампания всегда успешно обрабатывается


def process_all_campaigns(language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """
    Обрабатывает все кампании в директории.

    Args:
        language (Optional[str]): Язык для обработки.
        currency (Optional[str]): Валюта для обработки.

    Example:
        >>> process_all_campaigns('EN', 'USD')
    """
    # Выбираем локали для обработки
    if not language and not currency:
        _l = [(lang, curr) for locale in locales for lang, curr in locale.items()]
    else:
        _l = [(language, currency)]
    logger.debug(f'{_l=}')

    # Обрабатываем все кампании для каждой локали
    for lang, curr in _l:
        campaigns_dir = get_directory_names(campaigns_directory)
        logger.debug(f'{campaigns_dir=}')
        for campaign_name in campaigns_dir:
            logger.info(f'Start processing {campaign_name=}, {lang=}, {curr=}')
            editor = AliCampaignEditor(
                campaign_name=campaign_name,
                language=lang,
                currency=curr
            )
            editor.process_campaign()


def main_process(campaign_name: str, categories: List[str] | str, language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """
    Главная функция для обработки кампании.

    Args:
        campaign_name (str): Название рекламной кампании.
        categories (List[str] | str): Список категорий для обработки. Если пустой, обрабатывает всю кампанию.
        language (Optional[str]): Язык кампании.
        currency (Optional[str]): Валюта кампании.

    Example:
        >>> main_process('summer_sale', ['electronics'], 'EN', 'USD')
        >>> main_process('summer_sale', [], 'EN', 'USD')
    """
    # Определяем локали для обработки
    locales_to_process = [(language, currency)] if language and currency else [(lang, curr) for locale in locales for lang, curr in locale.items()]

    for lang, curr in locales_to_process:
        if categories:
            # Обрабатываем все указанные категории
            for category in categories:
                logger.info(f'Processing specific category {category=}, {lang=}, {curr=}')
                process_campaign_category(campaign_name, category, lang, curr)
        else:
            # Обрабатываем всю кампанию, если категории не указаны
            logger.info(f'Processing entire campaign {campaign_name=}, {lang=}, {curr=}')
            process_campaign(campaign_name, lang, curr)


def main() -> None:
    """
    Основная функция для запуска обработки кампаний.

    Example:
        >>> main()
    """
    # Настройка парсера аргументов
    parser = argparse.ArgumentParser(description='Prepare AliExpress Campaign')
    parser.add_argument('campaign_name', type=str, help='Name of the campaign')
    parser.add_argument(
        '-c',
        '--categories',
        nargs='+',
        help='List of categories (if not provided, all categories will be used)',
    )
    parser.add_argument(
        '-l', '--language', type=str, default=None, help='Language for the campaign'
    )
    parser.add_argument(
        '-cu', '--currency', type=str, default=None, help='Currency for the campaign'
    )
    parser.add_argument('--all', action='store_true', help='Process all campaigns')

    args = parser.parse_args()

    # Выбор режима обработки: одной кампании или всех
    if args.all:
        process_all_campaigns(args.language, args.currency)
    else:
        main_process(
            args.campaign_name, args.categories or [], args.language, args.currency
        )


if __name__ == '__main__':
    main()
```