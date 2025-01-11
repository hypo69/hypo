# Анализ кода модуля `code_instructions.md`

**Качество кода**
7
- Плюсы
    - Документ содержит подробные инструкции по созданию и редактированию рекламных кампаний.
    - Приведены примеры кода для основных шагов, что облегчает понимание процесса.
    - Инструкция содержит разделы по обработке ошибок и логированию, что важно для надежности системы.
- Минусы
    - Отсутствуют импорты для функций и классов, используемых в примерах кода.
    - Некоторые функции не имеют четкого описания и документации, например, что именно они делают.
    - Используются не все лучшие практики, например `try-except` блоки используются без необходимости, отсутствует явное логирование ошибок.

**Рекомендации по улучшению**

1.  **Импорты**: Добавьте необходимые импорты для функций и классов, используемых в коде.
2.  **Документация**: Добавьте docstring к функциям, методам и классам, чтобы описать их назначение, аргументы и возвращаемые значения. Используйте формат RST для документации.
3.  **Логирование**: Используйте `logger.error` для логирования ошибок вместо общих `except` блоков.
4.  **Форматирование кода**: Приведите примеры кода к общему стилю, используйте одинарные кавычки для строк в Python.
5.  **Описание модуля**: В начале файла должно быть описание модуля, например, для чего он предназначен.
6.  **Комментарии**:  Добавьте подробные комментарии к блокам кода, описывающие их назначение.
7.  **Избегать избыточности**: Упростить код, убрав избыточные try-except блоки и объединив их в общую обработку ошибок с использованием `logger.error`.

**Оптимизированный код**

```markdown
### Инструкция для программиста по поддержке кода для создания и редактирования рекламных кампаний

#### 1. Создание рекламной кампании

1. **Инициализация кампании**
   - Введите имя кампании, язык и валюту.
   - Пример:
     ```python
     campaign_name = 'example_campaign'
     language = 'EN'
     currency = 'USD'
     ```

2. **Создание директорий для кампании**
   - Создайте директории для кампании и категорий.
   - Пример:
     ```python
     categories = ['electronics', 'fashion']
     create_directories(campaign_name, categories)
     ```

3. **Сохранение конфигурации кампании**
   - Создайте и сохраните конфигурационный файл кампании.
   - Пример:
     ```python
     campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
     save_config(campaign_name, campaign_config)
     ```

4. **Сбор данных о продуктах**
   - Введите URL или ID продуктов для кампании.
   - Пример:
     ```python
     product_urls = ['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html']
     product_data = collect_product_data(product_urls)
     ```

5. **Сохранение данных о продуктах**
   - Сохраните собранные данные о продуктах.
   - Пример:
     ```python
     save_product_data(campaign_name, product_data)
     ```

6. **Создание рекламных материалов**
   - Создайте рекламные материалы на основе собранных данных.
   - Пример:
     ```python
     create_promotional_materials(campaign_name, product_data)
     ```

7. **Просмотр и публикация кампании**
   - Просмотрите и опубликуйте кампанию.
   - Пример:
     ```python
     review_campaign(campaign_name)
     publish_campaign(campaign_name)
     ```

#### 2. Редактирование рекламной кампании

1. **Загрузка существующей конфигурации кампании**
   - Загрузите конфигурацию существующей кампании.
   - Пример:
     ```python
     campaign_name = 'example_campaign'
     campaign_config = load_config(campaign_name)
     ```

2. **Обновление конфигурации кампании**
   - Обновите параметры кампании, такие как язык и валюту.
   - Пример:
     ```python
     campaign_config['language'] = 'RU'
     save_config(campaign_name, campaign_config)
     ```

3. **Обновление категорий и директорий**
   - Обновите список категорий и соответствующие директории.
   - Пример:
     ```python
     new_categories = ['home', 'beauty']
     update_categories(campaign_name, new_categories)
     ```

4. **Сбор новых данных о продуктах**
   - Введите новые URL или ID продуктов для обновленной кампании.
   - Пример:
     ```python
     new_product_urls = ['https://www.aliexpress.com/item/789.html']
     updated_product_data = collect_product_data(new_product_urls)
     ```

5. **Сохранение обновленных данных о продуктах**
   - Сохраните новые данные о продуктах.
   - Пример:
     ```python
     save_product_data(campaign_name, updated_product_data)
     ```

6. **Обновление рекламных материалов**
   - Обновите рекламные материалы на основе новых данных.
   - Пример:
     ```python
     update_promotional_materials(campaign_name, updated_product_data)
     ```

7. **Просмотр и публикация обновленной кампании**
   - Просмотрите и опубликуйте обновленную кампанию.
   - Пример:
     ```python
     review_campaign(campaign_name)
     publish_campaign(campaign_name)
     ```

#### 3. Обработка ошибок и логирование

1.  **Обработка ошибок**
    -   Используйте `try-except` для обработки ошибок.
    -   Пример:
        ```python
        try:
            # Ваш код
            ...
        except Exception as ex:
            logger.error("Ошибка", ex)
        ```

2.  **Логирование событий**
    -   Логируйте важные события и ошибки.
    -   Пример:
        ```python
        logger.info("Начало обработки кампании")
        logger.error("Ошибка при обработке кампании", ex)
        ```

### Примерный код
```python
"""
Модуль для работы с рекламными кампаниями.
=========================================================================================

Этот модуль содержит функции для создания и редактирования рекламных кампаний,
включая сбор данных о продуктах, создание рекламных материалов и управление
конфигурацией кампаний.

Пример использования
--------------------

Пример использования функций для создания и редактирования кампаний:

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
from src.logger import logger  # Импорт logger
# from src.utils.jjson import j_loads, j_loads_ns  # TODO добавить импорт если необходимо
# from typing import Any # TODO добавить импорт если необходимо
# from pathlib import Path # TODO добавить импорт если необходимо

def create_campaign(campaign_name: str, language: str, currency: str, categories: list[str], product_urls: list[str]):
    """
    Создает новую рекламную кампанию.

    Args:
        campaign_name (str): Имя кампании.
        language (str): Язык кампании.
        currency (str): Валюта кампании.
        categories (list[str]): Список категорий товаров.
        product_urls (list[str]): Список URL продуктов.
    """
    # Код создает директории для кампании и категорий
    create_directories(campaign_name, categories)
    # Код формирует словарь с конфигурацией кампании
    campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
    # Код сохраняет конфигурацию кампании
    save_config(campaign_name, campaign_config)
    # Код собирает данные о продуктах
    product_data = collect_product_data(product_urls)
    # Код сохраняет данные о продуктах
    save_product_data(campaign_name, product_data)
    # Код создает рекламные материалы
    create_promotional_materials(campaign_name, product_data)
    # Код проводит просмотр кампании
    review_campaign(campaign_name)
    # Код публикует кампанию
    publish_campaign(campaign_name)

def edit_campaign(campaign_name: str, language: str, categories: list[str], product_urls: list[str]):
    """
    Редактирует существующую рекламную кампанию.

    Args:
        campaign_name (str): Имя кампании.
        language (str): Язык кампании.
        categories (list[str]): Список категорий товаров.
        product_urls (list[str]): Список URL продуктов.
    """
    # Код загружает конфигурацию кампании
    campaign_config = load_config(campaign_name)
    # Код обновляет язык кампании
    campaign_config['language'] = language
    # Код сохраняет обновленную конфигурацию
    save_config(campaign_name, campaign_config)
    # Код обновляет категории
    update_categories(campaign_name, categories)
    # Код собирает новые данные о продуктах
    updated_product_data = collect_product_data(product_urls)
    # Код сохраняет обновленные данные о продуктах
    save_product_data(campaign_name, updated_product_data)
    # Код обновляет рекламные материалы
    update_promotional_materials(campaign_name, updated_product_data)
    # Код проводит просмотр кампании
    review_campaign(campaign_name)
    # Код публикует кампанию
    publish_campaign(campaign_name)

def create_directories(campaign_name: str, categories: list[str]):
    """
    Создает директории для кампании и категорий.

    Args:
        campaign_name (str): Имя кампании.
        categories (list[str]): Список категорий товаров.
    """
    # TODO: Реализовать создание директорий для кампании и категорий
    ...

def save_config(campaign_name: str, campaign_config: dict):
    """
    Сохраняет конфигурацию кампании в файл.

    Args:
        campaign_name (str): Имя кампании.
        campaign_config (dict): Словарь с конфигурацией кампании.
    """
    # TODO: Реализовать сохранение конфигурации кампании
    ...

def collect_product_data(product_urls: list[str]) -> list[dict]:
    """
    Собирает данные о продуктах по списку URL.

    Args:
        product_urls (list[str]): Список URL продуктов.

    Returns:
        list[dict]: Список словарей с данными о продуктах.
    """
    # TODO: Реализовать сбор данных о продуктах
    ...

def save_product_data(campaign_name: str, product_data: list[dict]):
    """
    Сохраняет данные о продуктах в файл.

    Args:
        campaign_name (str): Имя кампании.
        product_data (list[dict]): Список словарей с данными о продуктах.
    """
    # TODO: Реализовать сохранение данных о продуктах
    ...

def create_promotional_materials(campaign_name: str, product_data: list[dict]):
    """
    Создает рекламные материалы на основе данных о продуктах.

    Args:
        campaign_name (str): Имя кампании.
        product_data (list[dict]): Список словарей с данными о продуктах.
    """
     # TODO: Реализовать создание рекламных материалов
    ...

def review_campaign(campaign_name: str):
    """
    Просматривает кампанию перед публикацией.

    Args:
        campaign_name (str): Имя кампании.
    """
     # TODO: Реализовать просмотр кампании
    ...

def publish_campaign(campaign_name: str):
    """
    Публикует кампанию.

    Args:
        campaign_name (str): Имя кампании.
    """
     # TODO: Реализовать публикацию кампании
    ...

def load_config(campaign_name: str) -> dict:
    """
    Загружает конфигурацию кампании из файла.

    Args:
        campaign_name (str): Имя кампании.

    Returns:
        dict: Словарь с конфигурацией кампании.
    """
     # TODO: Реализовать загрузку конфигурации кампании
    ...

def update_categories(campaign_name: str, new_categories: list[str]):
    """
    Обновляет список категорий кампании и соответствующие директории.

    Args:
        campaign_name (str): Имя кампании.
        new_categories (list[str]): Новый список категорий.
    """
    # TODO: Реализовать обновление списка категорий
    ...

def update_promotional_materials(campaign_name: str, updated_product_data: list[dict]):
    """
    Обновляет рекламные материалы на основе новых данных о продуктах.

    Args:
        campaign_name (str): Имя кампании.
        updated_product_data (list[dict]): Список словарей с обновленными данными о продуктах.
    """
     # TODO: Реализовать обновление рекламных материалов
    ...
```

### Заключение

Следуя этим инструкциям, вы сможете эффективно создавать и редактировать рекламные кампании, а также поддерживать их актуальность и корректную работу.
```