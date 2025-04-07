# Модуль для генерации партнерских продуктов AliExpress

## Обзор

Модуль `affiliated_products_generator.py` предназначен для получения полной информации о товарах с AliExpress, включая партнерские ссылки, изображения и видео. Он позволяет автоматизировать процесс сбора данных о товарах для рекламных кампаний. Класс `AliAffiliatedProducts` отвечает за обработку идентификаторов товаров, получение партнерских ссылок, сохранение изображений и видео, а также подготовку данных для дальнейшего использования.

## Подробнее

Модуль является частью системы для работы с AliExpress и предназначен для сбора данных о товарах, которые будут использоваться в рекламных кампаниях. Он использует API AliExpress для получения информации о товарах и партнерских ссылок. Полученные данные сохраняются в виде JSON-файлов, изображений и видео.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора данных о товарах с AliExpress, включая партнерские ссылки, изображения и видео.

**Принцип работы**:
1.  Инициализация класса с указанием языка и валюты.
2.  Обработка списка идентификаторов товаров или URL-адресов.
3.  Получение партнерских ссылок для каждого товара.
4.  Получение подробной информации о товарах по партнерским ссылкам.
5.  Сохранение изображений и видео товаров локально.
6.  Подготовка данных о товарах для дальнейшего использования.

**Наследует**:

*   `AliApi`: Предоставляет методы для взаимодействия с API AliExpress.

**Атрибуты**:

*   `language` (str): Язык для рекламной кампании (по умолчанию 'EN').
*   `currency` (str): Валюта для рекламной кампании (по умолчанию 'USD').

**Методы**:

*   `__init__`: Инициализирует класс `AliAffiliatedProducts`.
*   `process_affiliate_products`: Обрабатывает список идентификаторов товаров или URL-адресов и возвращает список товаров с партнерскими ссылками и сохраненными изображениями.

## Функции

### `__init__`

```python
def __init__(self,
                 language: str | dict = 'EN',
                 currency: str = 'USD',
                 *args, **kwargs):
    """
    Initializes the AliAffiliatedProducts class.
    Args:
        language: Language for the campaign (default 'EN').
        currency: Currency for the campaign (default 'USD').
    """
```

**Назначение**: Инициализирует класс `AliAffiliatedProducts`, устанавливая язык и валюту для рекламной кампании.

**Параметры**:

*   `language` (str | dict): Язык для рекламной кампании (по умолчанию 'EN').
*   `currency` (str): Валюта для рекламной кампании (по умолчанию 'USD').
*   `*args`: Произвольные позиционные аргументы.
*   `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
    - `None`

**Как работает функция**:

1.  Проверяет, указаны ли язык и валюта. Если нет, записывает критическую ошибку в лог и завершает работу.
2.  Вызывает конструктор родительского класса `AliApi`, передавая язык и валюту.
3.  Сохраняет язык и валюту в атрибутах экземпляра класса.

**Примеры**:

```python
affiliated_products = AliAffiliatedProducts(language='RU', currency='RUB')
```

### `process_affiliate_products`

```python
async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
    """
    Processes a list of product IDs or URLs and returns a list of products with affiliate links and saved images.

    Args:
        campaign (SimpleNamespace): The promotional campaign data.
        category_name (str): The name of the category to process.
        prod_ids (list[str]): List of product URLs or IDs.

    Returns:
        list[SimpleNamespace]: A list of processed products with affiliate links and saved images.

    Example:
        >>> campaign = SimpleNamespace(category={})
        >>> category_name = "electronics"
        >>> prod_ids = ["http://example.com/product1", "http://example.com/product2"]
        >>> products = campaign.process_affiliate_products(category_name, prod_ids)
        >>> for product in products:
        ...     print(product.product_title)
        "Product 1 Title"
        "Product 2 Title"

    Raises:
        Exception: If the category name is not found in the campaign.

    Notes:
        - Fetches page content from URLs.
        - Handles affiliate links and image/video saving.
        - Generates and saves campaign data and output files.
    """
```

**Назначение**: Обрабатывает список идентификаторов товаров или URL-адресов и возвращает список товаров с партнерскими ссылками и сохраненными изображениями.

**Параметры**:

*   `prod_ids` (list[str]): Список URL-адресов или идентификаторов товаров.
*   `category_root` (Path | str): Корневой путь к каталогу категории.

**Возвращает**:

*   `list[SimpleNamespace]`: Список обработанных товаров с партнерскими ссылками и сохраненными изображениями.

**Как работает функция**:

1.  Инициализирует списки для хранения партнерских ссылок и URL-адресов товаров.
2.  Нормализует URL-адреса товаров, приводя их к виду `https://aliexpress.com/item/<product_id>.html`.
3.  Для каждого нормализованного URL-адреса товара получает партнерские ссылки с использованием метода `get_affiliate_links` родительского класса `AliApi`.
4.  Если партнерская ссылка найдена, добавляет ее в список `_promotion_links`, а URL-адрес товара — в список `_prod_urls`.
5.  Если партнерские ссылки не найдены, записывает предупреждение в лог и завершает работу.
6.  Получает подробную информацию о товарах по URL-адресам с использованием метода `retrieve_product_details`.
7.  Для каждого товара сохраняет изображение и видео локально.
8.  Сохраняет данные о товаре в формате JSON.
9.  Возвращает список обработанных товаров.

**Внутренние функции**: Отсутствуют.

**Flowchart**:

```
    ┌───────────────────────────────────────────────┐
    │ Start                                         │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌─────────────────────────────────────────────────────────┐
    │ Try to get category from campaign using `category_name` │
    └─────────────────────────────────────────────────────────┘
                        │
                        ┴───────────────────────────────────────────┐
                        │                                           │
                        ▼                                           ▼
    ┌──────────────────────────────────────────────────────┐
    │ Campaign Category found: Initialize paths,           │
    │ set promotional URLs, and process products           │
    └──────────────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ No category found: Create default category    │
    │ and initialize paths, set promotional URLs,   │
    │ and process products                          │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ Initialize paths and prepare data structures  │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ Process products URLs to get affiliate links  │
    └───────────────────────────────────────────────┘
                        │
            ┌───────────┴───────────────────────────┐
            │                                       │
            ▼                                       ▼
    ┌─────────────────────────────────────────────┐
    │ No affiliate links found: Log warning       │
    └─────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ Retrieve product details for affiliate URLs   │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ Process each product and save images/videos   │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ Prepare and save final output data            │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ Return list of affiliated products            │    
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ End                                           │
    └───────────────────────────────────────────────┘
```

**Примеры**:

```python
prod_ids = ["https://aliexpress.com/item/1234567890.html", "https://aliexpress.com/item/0987654321.html"]
category_root = "/path/to/category"
affiliated_products = await process_affiliate_products(prod_ids, category_root)
for product in affiliated_products:
    print(product.product_title)