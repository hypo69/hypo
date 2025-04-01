# Модуль `affiliated_products_generator.py`

## Обзор

Модуль `affiliated_products_generator.py` предназначен для получения данных о товарах с AliExpress, включая создание партнерских ссылок, сохранение изображений и видео, а также сохранение данных о товарах в формате JSON. Этот модуль является частью проекта `hypotez` и используется для автоматизации процесса создания рекламных кампаний на основе партнерских товаров с AliExpress.

## Подробней

Модуль содержит класс `AliAffiliatedProducts`, который наследуется от класса `AliApi`. Он предоставляет функциональность для обработки списка идентификаторов или URL-адресов продуктов, получения партнерских ссылок, извлечения подробной информации о продуктах и сохранения изображений и видео, связанных с этими продуктами.  Модуль также включает функции для сохранения данных о продуктах в формате JSON и создания текстовых файлов, содержащих заголовки продуктов.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора полных данных о продуктах из URL-адресов или идентификаторов продуктов. Предоставляет методы для получения партнерских ссылок, сохранения изображений и видео, а также сохранения данных о продуктах в формате JSON.

**Как работает класс**:

1.  Инициализируется с указанием языка и валюты.
2.  Использует метод `process_affiliate_products` для обработки списка идентификаторов или URL-адресов продуктов.
3.  Получает партнерские ссылки для каждого продукта.
4.  Извлекает подробную информацию о продуктах, используя метод `retrieve_product_details`.
5.  Сохраняет изображения и видео, связанные с продуктами.
6.  Сохраняет данные о продуктах в формате JSON.

**Методы**:

*   `__init__`: Инициализирует класс `AliAffiliatedProducts`.
*   `process_affiliate_products`: Обрабатывает список идентификаторов или URL-адресов продуктов, получает партнерские ссылки, извлекает подробную информацию о продуктах, сохраняет изображения и видео, а также сохраняет данные о продуктах в формате JSON.

**Параметры**:

*   `language` (str | dict): Язык для рекламной кампании (по умолчанию 'EN').
*   `currency` (str): Валюта для рекламной кампании (по умолчанию 'USD').

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

**Описание**: Инициализирует класс `AliAffiliatedProducts`.

**Как работает функция**:
Функция инициализирует экземпляр класса `AliAffiliatedProducts`, устанавливая язык и валюту для рекламной кампании. Если язык или валюта не указаны, регистрируется критическая ошибка. Вызывает конструктор родительского класса `AliApi` и сохраняет значения языка и валюты в атрибутах экземпляра.

**Параметры**:

*   `language` (str | dict): Язык для рекламной кампании (по умолчанию 'EN').
*   `currency` (str): Валюта для рекламной кампании (по умолчанию 'USD').
*   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
*   `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

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

    Flowchart:
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
    """
```

**Описание**: Обрабатывает список идентификаторов или URL-адресов продуктов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.

**Как работает функция**:

1.  Приводит список URL-адресов продуктов к виду `https://aliexpress.com/item/<product_id>.html` с помощью функции `ensure_https`.
2.  Получает партнерские ссылки для каждого продукта, используя метод `get_affiliate_links` родительского класса `AliApi`.
3.  Извлекает подробную информацию о продуктах, используя метод `retrieve_product_details`.
4.  Сохраняет изображения и видео, связанные с продуктами, используя функции `save_image_from_url_async` и `save_video_from_url`.
5.  Сохраняет данные о продуктах в формате JSON, используя функцию `j_dumps`.
6.  Сохраняет список заголовков продуктов в текстовый файл, используя функцию `save_text_file`.

**Параметры**:

*   `prod_ids` (list[str]): Список URL-адресов или идентификаторов продуктов.
*   `category_root` (Path | str): Корневой путь к категории, в которой будут сохранены изображения и видео.

**Возвращает**:

*   `list[SimpleNamespace]`: Список обработанных продуктов с партнерскими ссылками и сохраненными изображениями.

**Примеры**:

```python
prod_ids = ["http://example.com/product1", "http://example.com/product2"]
category_root = "/path/to/category"
affiliated_products = await affiliated_products.process_affiliate_products(prod_ids, category_root)
for product in affiliated_products:
    print(product.product_title)
```
```
"Product 1 Title"
"Product 2 Title"
```
```