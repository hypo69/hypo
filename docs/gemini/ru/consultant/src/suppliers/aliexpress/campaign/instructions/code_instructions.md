## Анализ кода модуля `code_instructions`

**Качество кода**:

- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Инструкция достаточно подробная и охватывает основные этапы создания и редактирования рекламных кампаний.
    - Присутствуют примеры кода для каждой операции.
    - Описаны основные моменты обработки ошибок и логирования.
- **Минусы**:
    -  Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  В примерах кода используются двойные кавычки (`"`) для ключей и значений в словарях и списках.
    -  Отсутствует импорт `logger` из `src.logger`.
    -  Нет подробных описаний функций и классов в формате RST.
    -  Используется стандартный `try-except`, вместо `logger.error`.
    -  Не хватает конкретики в инструкциях по обработке ошибок.
    - Код в примере не соответствует стандарту PEP8.

**Рекомендации по улучшению**:

1.  **Использование одинарных кавычек**: Везде, где это не относится к выводу, используйте одинарные кавычки (`'`) для строк, ключей и значений в словарях и списках, как указано в инструкции.
2.  **Импорт logger**: Добавить импорт `logger` из `src.logger`.
3.  **Обработка ошибок**: Замените стандартный `try-except` на использование `logger.error` для логирования ошибок.
4.  **RST-документация**: Добавить документацию в формате RST для всех функций и модулей, как в примерах.
5.  **Использовать `j_loads`**: Заменить `json.load` на `j_loads` или `j_loads_ns` при необходимости.
6.  **Комментарии**: Добавить более точные комментарии, описывающие действия кода.
7.  **PEP8**: Отформатировать код согласно стандартам PEP8.

**Оптимизированный код**:

```markdown
### Инструкция для программиста по поддержке кода для создания и редактирования рекламных кампаний

#### 1. Создание рекламной кампании

1.  **Инициализация кампании**
    -   Введите имя кампании, язык и валюту.
    -   Пример:
        ```python
        campaign_name = 'example_campaign' # имя кампании
        language = 'EN' # язык
        currency = 'USD' # валюта
        ```

2.  **Создание директорий для кампании**
    -   Создайте директории для кампании и категорий.
    -   Пример:
        ```python
        categories = ['electronics', 'fashion'] # список категорий
        create_directories(campaign_name, categories) # создаем директории
        ```

3.  **Сохранение конфигурации кампании**
    -   Создайте и сохраните конфигурационный файл кампании.
    -   Пример:
        ```python
        campaign_config = {'name': campaign_name, 'language': language, 'currency': currency} # конфигурация кампании
        save_config(campaign_name, campaign_config) # сохраняем конфигурацию
        ```

4.  **Сбор данных о продуктах**
    -   Введите URL или ID продуктов для кампании.
    -   Пример:
        ```python
        product_urls = ['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html'] # список URL продуктов
        product_data = collect_product_data(product_urls) # собираем данные о продуктах
        ```

5.  **Сохранение данных о продуктах**
    -   Сохраните собранные данные о продуктах.
    -   Пример:
        ```python
        save_product_data(campaign_name, product_data) # сохраняем данные о продуктах
        ```

6.  **Создание рекламных материалов**
    -   Создайте рекламные материалы на основе собранных данных.
    -   Пример:
        ```python
        create_promotional_materials(campaign_name, product_data) # создаем рекламные материалы
        ```

7.  **Просмотр и публикация кампании**
    -   Просмотрите и опубликуйте кампанию.
    -   Пример:
        ```python
        review_campaign(campaign_name) # просматриваем кампанию
        publish_campaign(campaign_name) # публикуем кампанию
        ```

#### 2. Редактирование рекламной кампании

1.  **Загрузка существующей конфигурации кампании**
    -   Загрузите конфигурацию существующей кампании.
    -   Пример:
        ```python
        campaign_name = 'example_campaign' # имя кампании
        campaign_config = load_config(campaign_name) # загружаем конфигурацию кампании
        ```

2.  **Обновление конфигурации кампании**
    -   Обновите параметры кампании, такие как язык и валюту.
    -   Пример:
        ```python
        campaign_config['language'] = 'RU' # обновляем язык
        save_config(campaign_name, campaign_config) # сохраняем конфигурацию
        ```

3.  **Обновление категорий и директорий**
    -   Обновите список категорий и соответствующие директории.
    -   Пример:
        ```python
        new_categories = ['home', 'beauty'] # список новых категорий
        update_categories(campaign_name, new_categories) # обновляем категории
        ```

4.  **Сбор новых данных о продуктах**
    -   Введите новые URL или ID продуктов для обновленной кампании.
    -   Пример:
        ```python
        new_product_urls = ['https://www.aliexpress.com/item/789.html'] # список новых URL продуктов
        updated_product_data = collect_product_data(new_product_urls) # собираем новые данные о продуктах
        ```

5.  **Сохранение обновленных данных о продуктах**
    -   Сохраните новые данные о продуктах.
    -   Пример:
        ```python
        save_product_data(campaign_name, updated_product_data) # сохраняем новые данные о продуктах
        ```

6.  **Обновление рекламных материалов**
    -   Обновите рекламные материалы на основе новых данных.
    -   Пример:
        ```python
        update_promotional_materials(campaign_name, updated_product_data) # обновляем рекламные материалы
        ```

7.  **Просмотр и публикация обновленной кампании**
    -   Просмотрите и опубликуйте обновленную кампанию.
    -   Пример:
        ```python
        review_campaign(campaign_name) # просматриваем обновленную кампанию
        publish_campaign(campaign_name) # публикуем обновленную кампанию
        ```

#### 3. Обработка ошибок и логирование

1.  **Обработка ошибок**
    -   Используйте `logger.error` для логирования ошибок.
    -   Пример:
        ```python
        from src.logger import logger # импортируем логгер
        try:
            # Ваш код
            ...
        except Exception as ex:
            logger.error('Произошла ошибка при выполнении операции', exc_info=ex) # логгируем ошибку
        ```

2.  **Логирование событий**
    -   Логируйте важные события и ошибки.
    -   Пример:
        ```python
        from src.logger import logger # импортируем логгер
        logger.info('Начало обработки кампании') # логируем начало обработки
        try:
            # Ваш код
             ...
        except Exception as ex:
            logger.error('Ошибка при обработке кампании', exc_info=ex) # логируем ошибку
        ```

### Примерный код

```python
"""
Модуль для создания и редактирования рекламных кампаний.
========================================================

Этот модуль содержит функции для создания и редактирования рекламных кампаний,
включая создание директорий, сохранение конфигурации, сбор данных о продуктах,
создание рекламных материалов и логирование.

Пример использования:
---------------------
.. code-block:: python

    create_campaign('new_campaign', 'EN', 'USD', ['electronics'], ['https://www.aliexpress.com/item/123.html'])
    edit_campaign('existing_campaign', 'RU', ['home'], ['https://www.aliexpress.com/item/456.html'])
"""
from src.logger import logger  # импортируем логгер


def create_campaign(campaign_name: str, language: str, currency: str, categories: list[str], product_urls: list[str]) -> None:
    """
    Создает новую рекламную кампанию.

    :param campaign_name: Название кампании.
    :type campaign_name: str
    :param language: Язык кампании.
    :type language: str
    :param currency: Валюта кампании.
    :type currency: str
    :param categories: Список категорий.
    :type categories: list[str]
    :param product_urls: Список URL продуктов.
    :type product_urls: list[str]
    :raises Exception: В случае ошибки при создании кампании.

    Пример:
        >>> create_campaign('test_campaign', 'EN', 'USD', ['electronics'], ['https://www.aliexpress.com/item/123.html'])
    """
    try:
        create_directories(campaign_name, categories) # создаем директории
        campaign_config = {'name': campaign_name, 'language': language, 'currency': currency} # создаем конфигурацию
        save_config(campaign_name, campaign_config) # сохраняем конфигурацию
        product_data = collect_product_data(product_urls) # собираем данные о продуктах
        save_product_data(campaign_name, product_data) # сохраняем данные о продуктах
        create_promotional_materials(campaign_name, product_data) # создаем рекламные материалы
        review_campaign(campaign_name) # просматриваем кампанию
        publish_campaign(campaign_name) # публикуем кампанию
    except Exception as ex:
        logger.error(f'Ошибка при создании кампании {campaign_name}', exc_info=ex)  # логируем ошибку

def edit_campaign(campaign_name: str, language: str, categories: list[str], product_urls: list[str]) -> None:
    """
    Редактирует существующую рекламную кампанию.

    :param campaign_name: Название кампании.
    :type campaign_name: str
    :param language: Язык кампании.
    :type language: str
    :param categories: Список категорий.
    :type categories: list[str]
    :param product_urls: Список URL продуктов.
    :type product_urls: list[str]
    :raises Exception: В случае ошибки при редактировании кампании.

    Пример:
       >>> edit_campaign('test_campaign', 'RU', ['home'], ['https://www.aliexpress.com/item/456.html'])
    """
    try:
        campaign_config = load_config(campaign_name)  # загружаем конфигурацию кампании
        campaign_config['language'] = language  # обновляем язык
        save_config(campaign_name, campaign_config) # сохраняем конфигурацию
        update_categories(campaign_name, categories) # обновляем категории
        updated_product_data = collect_product_data(product_urls) # собираем новые данные о продуктах
        save_product_data(campaign_name, updated_product_data) # сохраняем новые данные о продуктах
        update_promotional_materials(campaign_name, updated_product_data) # обновляем рекламные материалы
        review_campaign(campaign_name) # просматриваем обновленную кампанию
        publish_campaign(campaign_name) # публикуем обновленную кампанию
    except Exception as ex:
         logger.error(f'Ошибка при редактировании кампании {campaign_name}', exc_info=ex) # логируем ошибку
```

### Заключение

Следуя этим инструкциям, вы сможете эффективно создавать и редактировать рекламные кампании, а также поддерживать их актуальность и корректную работу.
```