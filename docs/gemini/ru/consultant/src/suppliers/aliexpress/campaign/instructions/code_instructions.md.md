# Анализ кода модуля `code_instructions.md`

**Качество кода**
8
 -  Плюсы
     - Код структурирован и разделен на логические блоки, что облегчает понимание.
     - Приведены примеры кода для основных операций, что помогает в использовании инструкций.
     - Есть разделение на создание и редактирование рекламных кампаний, что удобно для восприятия.
     - Присутствуют инструкции по обработке ошибок и логированию.
 -  Минусы
    -  Отсутствуют необходимые импорты и определения функций, которые упоминаются в примерах.
    -  Код не соответствует стандарту docstring RST.
    -  Комментарии после `#` не полностью соответствуют требованиям.
    -  Не используется `j_loads` или `j_loads_ns` для загрузки данных.
    -  Присутствуют общие `try-except` без обработки конкретных ошибок.
    -  Не используется `logger.error` для логирования ошибок.

**Рекомендации по улучшению**
1.  Добавить необходимые импорты (например, `from src.utils.jjson import j_loads, j_loads_ns`, `from src.logger.logger import logger`).
2.  Переписать все комментарии в формате RST, включая документацию для функций.
3.  Использовать `j_loads` или `j_loads_ns` для загрузки конфигурационных файлов.
4.  Заменить общие `try-except` на более конкретную обработку ошибок и использовать `logger.error` для логирования.
5.  Добавить документацию к функциям `create_campaign` и `edit_campaign` в формате RST.
6.  Уточнить комментарии в коде, чтобы они соответствовали требованиям.

**Оптимизированный код**

```python
"""
Инструкция для программиста по поддержке кода для создания и редактирования рекламных кампаний
=========================================================================================

Этот модуль содержит инструкции и примеры кода для создания и редактирования рекламных кампаний,
а также рекомендации по обработке ошибок и логированию.

Пример использования
--------------------

Пример создания и редактирования рекламной кампании:

.. code-block:: python

    create_campaign(
        campaign_name='example_campaign',
        language='EN',
        currency='USD',
        categories=['electronics', 'fashion'],
        product_urls=['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html']
    )

    edit_campaign(
        campaign_name='example_campaign',
        language='RU',
        categories=['home', 'beauty'],
        product_urls=['https://www.aliexpress.com/item/789.html']
    )
"""
from typing import List
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger


def create_directories(campaign_name: str, categories: List[str]) -> None:
    """
    Создает директории для кампании и категорий.

    :param campaign_name: Имя кампании.
    :param categories: Список категорий.
    :return: None
    """
    # TODO: Реализовать создание директорий
    ...


def save_config(campaign_name: str, campaign_config: dict) -> None:
    """
    Сохраняет конфигурацию кампании в файл.

    :param campaign_name: Имя кампании.
    :param campaign_config: Словарь с конфигурацией кампании.
    :return: None
    """
    # TODO: Реализовать сохранение конфигурации
    ...


def collect_product_data(product_urls: List[str]) -> List[dict]:
    """
    Собирает данные о продуктах по URL.

    :param product_urls: Список URL продуктов.
    :return: Список словарей с данными о продуктах.
    """
    # TODO: Реализовать сбор данных о продуктах
    ...


def save_product_data(campaign_name: str, product_data: List[dict]) -> None:
    """
    Сохраняет данные о продуктах.

    :param campaign_name: Имя кампании.
    :param product_data: Список словарей с данными о продуктах.
    :return: None
    """
    # TODO: Реализовать сохранение данных о продуктах
    ...


def create_promotional_materials(campaign_name: str, product_data: List[dict]) -> None:
    """
    Создает рекламные материалы на основе данных о продуктах.

    :param campaign_name: Имя кампании.
    :param product_data: Список словарей с данными о продуктах.
    :return: None
    """
    # TODO: Реализовать создание рекламных материалов
    ...


def review_campaign(campaign_name: str) -> None:
    """
    Выполняет просмотр кампании.

    :param campaign_name: Имя кампании.
    :return: None
    """
    # TODO: Реализовать просмотр кампании
    ...


def publish_campaign(campaign_name: str) -> None:
    """
    Публикует кампанию.

    :param campaign_name: Имя кампании.
    :return: None
    """
    # TODO: Реализовать публикацию кампании
    ...


def load_config(campaign_name: str) -> dict:
    """
    Загружает конфигурацию кампании из файла.

    :param campaign_name: Имя кампании.
    :return: Словарь с конфигурацией кампании.
    """
    # TODO: Реализовать загрузку конфигурации
    ...


def update_categories(campaign_name: str, new_categories: List[str]) -> None:
    """
    Обновляет список категорий и соответствующие директории.

    :param campaign_name: Имя кампании.
    :param new_categories: Новый список категорий.
    :return: None
    """
    # TODO: Реализовать обновление категорий
    ...


def update_promotional_materials(campaign_name: str, updated_product_data: List[dict]) -> None:
    """
    Обновляет рекламные материалы на основе новых данных о продуктах.

    :param campaign_name: Имя кампании.
    :param updated_product_data: Список словарей с обновленными данными о продуктах.
    :return: None
    """
    # TODO: Реализовать обновление рекламных материалов
    ...


def create_campaign(campaign_name: str, language: str, currency: str, categories: List[str], product_urls: List[str]) -> None:
    """
    Создает рекламную кампанию.

    :param campaign_name: Имя кампании.
    :param language: Язык кампании.
    :param currency: Валюта кампании.
    :param categories: Список категорий.
    :param product_urls: Список URL продуктов.
    :return: None
    """
    # Код создает директории для кампании
    create_directories(campaign_name, categories)
    # Код формирует словарь конфигурации кампании
    campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
    # Код сохраняет конфигурацию кампании
    save_config(campaign_name, campaign_config)
    # Код собирает данные о продуктах
    product_data = collect_product_data(product_urls)
    # Код сохраняет данные о продуктах
    save_product_data(campaign_name, product_data)
    # Код создает рекламные материалы
    create_promotional_materials(campaign_name, product_data)
    # Код выполняет просмотр кампании
    review_campaign(campaign_name)
    # Код публикует кампанию
    publish_campaign(campaign_name)


def edit_campaign(campaign_name: str, language: str, categories: List[str], product_urls: List[str]) -> None:
    """
    Редактирует существующую рекламную кампанию.

    :param campaign_name: Имя кампании.
    :param language: Новый язык кампании.
    :param categories: Новый список категорий.
    :param product_urls: Список URL новых продуктов.
    :return: None
    """
    # Код загружает конфигурацию кампании
    campaign_config = load_config(campaign_name)
    # Код обновляет язык в конфигурации
    campaign_config['language'] = language
    # Код сохраняет обновленную конфигурацию
    save_config(campaign_name, campaign_config)
    # Код обновляет список категорий
    update_categories(campaign_name, categories)
    # Код собирает данные о новых продуктах
    updated_product_data = collect_product_data(product_urls)
    # Код сохраняет новые данные о продуктах
    save_product_data(campaign_name, updated_product_data)
    # Код обновляет рекламные материалы
    update_promotional_materials(campaign_name, updated_product_data)
    # Код выполняет просмотр кампании
    review_campaign(campaign_name)
    # Код публикует кампанию
    publish_campaign(campaign_name)
```