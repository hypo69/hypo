# Анализ кода модуля `code_instructions.md`

**Качество кода**
8
 -  Плюсы
        - Код содержит подробные инструкции для создания и редактирования рекламных кампаний.
        - Инструкции четко структурированы и разделены на логические блоки.
        - Приведены примеры кода для каждого этапа процесса, что упрощает понимание.
        -  Присутствуют разделы по обработке ошибок и логированию.

 -  Минусы
    - Документ не соответствует формату reStructuredText (RST).
    - В коде используются стандартные `print`, `json.load` и отсутствует импорт логгера.
    - Отсутствуют docstring к функциям и классам.
    - Инструкции используют общие формулировки, а не конкретные действия.
    - Не все блоки кода прокомментированы построчно.

**Рекомендации по улучшению**
- Преобразовать весь документ в формат reStructuredText (RST).
- Заменить стандартные `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
- Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
-  Уточнить и детализировать комментарии, используя конкретные формулировки.
- Добавить docstring в формате RST ко всем функциям.
- Использовать `logger.error` вместо общих `try-except` блоков.
- Прокомментировать построчно все блоки кода.
- Использовать одинарные кавычки `'` вместо двойных `"` в Python коде.

**Оптимизиробанный код**
```markdown
# ИНСТРУКЦИЯ ДЛЯ ПРОГРАММИСТА ПО ПОДДЕРЖКЕ КОДА ДЛЯ СОЗДАНИЯ И РЕДАКТИРОВАНИЯ РЕКЛАМНЫХ КАМПАНИЙ
=========================================================================================

Эта инструкция описывает процесс создания и редактирования рекламных кампаний, а также предоставляет рекомендации по поддержке кода.

#### 1. Создание рекламной кампании

1.  **Инициализация кампании**
    -   Введите имя кампании, язык и валюту.
    -   Пример:

        ```python
        campaign_name = 'example_campaign'
        language = 'EN'
        currency = 'USD'
        ```

2.  **Создание директорий для кампании**
    -   Создайте директории для кампании и категорий.
    -   Пример:

        ```python
        categories = ['electronics', 'fashion']
        create_directories(campaign_name, categories)
        ```

3.  **Сохранение конфигурации кампании**
    -   Создайте и сохраните конфигурационный файл кампании.
    -   Пример:

        ```python
        campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
        save_config(campaign_name, campaign_config)
        ```

4.  **Сбор данных о продуктах**
    -   Введите URL или ID продуктов для кампании.
    -   Пример:

        ```python
        product_urls = ['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html']
        product_data = collect_product_data(product_urls)
        ```

5.  **Сохранение данных о продуктах**
    -   Сохраните собранные данные о продуктах.
    -   Пример:

        ```python
        save_product_data(campaign_name, product_data)
        ```

6.  **Создание рекламных материалов**
    -   Создайте рекламные материалы на основе собранных данных.
    -   Пример:

        ```python
        create_promotional_materials(campaign_name, product_data)
        ```

7.  **Просмотр и публикация кампании**
    -   Просмотрите и опубликуйте кампанию.
    -   Пример:

        ```python
        review_campaign(campaign_name)
        publish_campaign(campaign_name)
        ```

#### 2. Редактирование рекламной кампании

1.  **Загрузка существующей конфигурации кампании**
    -   Загрузите конфигурацию существующей кампании.
    -   Пример:

        ```python
        campaign_name = 'example_campaign'
        campaign_config = load_config(campaign_name)
        ```

2.  **Обновление конфигурации кампании**
    -   Обновите параметры кампании, такие как язык и валюту.
    -   Пример:

        ```python
        campaign_config['language'] = 'RU'
        save_config(campaign_name, campaign_config)
        ```

3.  **Обновление категорий и директорий**
    -   Обновите список категорий и соответствующие директории.
    -   Пример:

        ```python
        new_categories = ['home', 'beauty']
        update_categories(campaign_name, new_categories)
        ```

4.  **Сбор новых данных о продуктах**
    -   Введите новые URL или ID продуктов для обновленной кампании.
    -   Пример:

        ```python
        new_product_urls = ['https://www.aliexpress.com/item/789.html']
        updated_product_data = collect_product_data(new_product_urls)
        ```

5.  **Сохранение обновленных данных о продуктах**
    -   Сохраните новые данные о продуктах.
    -   Пример:

        ```python
        save_product_data(campaign_name, updated_product_data)
        ```

6.  **Обновление рекламных материалов**
    -   Обновите рекламные материалы на основе новых данных.
    -   Пример:

        ```python
        update_promotional_materials(campaign_name, updated_product_data)
        ```

7.  **Просмотр и публикация обновленной кампании**
    -   Просмотрите и опубликуйте обновленную кампанию.
    -   Пример:

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
            logger.error('Ошибка', ex)
        ```

2.  **Логирование событий**
    -   Логируйте важные события и ошибки.
    -   Пример:

        ```python
        logger.info('Начало обработки кампании')
        logger.error('Ошибка при обработке кампании', ex)
        ```

### Примерный код

```python
from src.logger.logger import logger  # импорт модуля логгера

def create_campaign(campaign_name: str, language: str, currency: str, categories: list, product_urls: list) -> None:
    """
    Создает рекламную кампанию.

    :param campaign_name: Название кампании.
    :param language: Язык кампании.
    :param currency: Валюта кампании.
    :param categories: Список категорий товаров.
    :param product_urls: Список URL товаров.
    :return: None
    """
    # код выполняет создание директорий для кампании
    create_directories(campaign_name, categories)
    # код создает конфигурацию кампании
    campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
    # код сохраняет конфигурацию кампании
    save_config(campaign_name, campaign_config)
    # код собирает данные о продуктах
    product_data = collect_product_data(product_urls)
    # код сохраняет данные о продуктах
    save_product_data(campaign_name, product_data)
    # код создает рекламные материалы
    create_promotional_materials(campaign_name, product_data)
    # код выполняет просмотр кампании
    review_campaign(campaign_name)
    # код публикует кампанию
    publish_campaign(campaign_name)


def edit_campaign(campaign_name: str, language: str, categories: list, product_urls: list) -> None:
    """
    Редактирует существующую рекламную кампанию.

    :param campaign_name: Название кампании.
    :param language: Новый язык кампании.
    :param categories: Новый список категорий товаров.
    :param product_urls: Новый список URL товаров.
    :return: None
    """
    # код загружает конфигурацию кампании
    campaign_config = load_config(campaign_name)
    # код обновляет язык кампании
    campaign_config['language'] = language
    # код сохраняет конфигурацию кампании
    save_config(campaign_name, campaign_config)
    # код обновляет категории кампании
    update_categories(campaign_name, categories)
    # код собирает данные о продуктах
    updated_product_data = collect_product_data(product_urls)
    # код сохраняет данные о продуктах
    save_product_data(campaign_name, updated_product_data)
    # код обновляет рекламные материалы
    update_promotional_materials(campaign_name, updated_product_data)
    # код выполняет просмотр кампании
    review_campaign(campaign_name)
    # код публикует кампанию
    publish_campaign(campaign_name)
```

### Заключение

Следуя этим инструкциям, вы сможете эффективно создавать и редактировать рекламные кампании, а также поддерживать их актуальность и корректную работу.
```