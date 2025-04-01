# Модуль `affiliated_products_generator.py`

## Обзор

Модуль `affiliated_products_generator.py` предназначен для получения данных о товарах с AliExpress, включая создание партнерских ссылок, сохранение изображений и видео, а также сохранение информации о товарах в формате JSON. Модуль содержит класс `AliAffiliatedProducts`, который расширяет класс `AliApi` и предоставляет функциональность для обработки списка ID товаров или URL-адресов, получения партнерских ссылок, загрузки изображений и видео, а также сохранения данных о товарах.

## Подробней

Этот модуль является частью системы для работы с партнерской программой AliExpress. Он автоматизирует процесс получения информации о товарах, создания партнерских ссылок и сохранения необходимых медиафайлов для дальнейшего использования в рекламных кампаниях.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора полных данных о товарах из URL-адресов или ID товаров.
Для получения дополнительной информации о том, как создавать шаблоны для рекламных кампаний, см. раздел «Управление рекламными кампаниями AliExpress».

**Наследует**: `AliApi`

**Атрибуты**:

-   `language` (str): Язык кампании.
-   `currency` (str): Валюта кампании.

**Методы**:

-   `__init__`: Инициализирует класс `AliAffiliatedProducts`.
-   `process_affiliate_products`: Обрабатывает список ID или URL товаров, возвращает список товаров с партнерскими ссылками и сохраненными изображениями.

### `__init__`

```python
def __init__(self, language: str | dict = 'EN', currency: str = 'USD', *args, **kwargs):
    """
    Initializes the AliAffiliatedProducts class.
    Args:
        language: Language for the campaign (default 'EN').
        currency: Currency for the campaign (default 'USD').
    """
    ...
```

**Назначение**: Инициализирует класс `AliAffiliatedProducts`, устанавливая язык и валюту для кампании.

**Параметры**:

-   `language` (str | dict, optional): Язык для кампании (по умолчанию 'EN').
-   `currency` (str, optional): Валюта для кампании (по умолчанию 'USD').
-   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
-   `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Как работает функция**:

1.  Проверяет, установлены ли язык и валюта. Если нет, записывает критическую ошибку в лог и завершает работу.
2.  Вызывает конструктор родительского класса `AliApi` с переданными языком и валютой.
3.  Устанавливает атрибуты `language` и `currency` экземпляра класса.

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
    ...
```

**Назначение**: Обрабатывает список ID товаров или URL-адресов, возвращает список товаров с партнерскими ссылками и сохраненными изображениями.

**Параметры**:

-   `prod_ids` (list[str]): Список URL-адресов или ID товаров.
-   `category_root` (Path | str): Корневой путь к категории.

**Возвращает**:

-   `list[SimpleNamespace]`: Список обработанных товаров с партнерскими ссылками и сохраненными изображениями.

**Как работает функция**:

1.  Инициализирует списки `_promotion_links` и `_prod_urls` для хранения партнерских ссылок и URL-адресов товаров соответственно.
2.  Нормализует URL-адреса товаров, приводя их к виду `https://aliexpress.com/item/<product_id>.html` с помощью функции `ensure_https`.
3.  Для каждого нормализованного URL-адреса товара получает партнерские ссылки с помощью метода `get_affiliate_links` родительского класса `AliApi`.
4.  Если партнерская ссылка найдена, добавляет ее в список `_promotion_links` и URL-адрес товара в список `_prod_urls`.
5.  Если партнерские ссылки не найдены, записывает предупреждение в лог и возвращает `None`.
6.  Получает подробную информацию о товарах по URL-адресам с помощью метода `retrieve_product_details`.
7.  Для каждого товара сохраняет изображение с помощью асинхронной функции `save_image_from_url`, устанавливает локальный путь к изображению и, если доступно, сохраняет видео с помощью асинхронной функции `save_video_from_url`, устанавливая локальный путь к видео.
8.  Сохраняет информацию о товаре в формате JSON с помощью функции `j_dumps` и добавляет товар в список `affiliated_products_list`.
9.  Сохраняет список заголовков товаров в текстовый файл с помощью асинхронной функции `save_text_file`.
10. Возвращает список обработанных товаров `affiliated_products_list`.

**Внутренние функции**: Отсутствуют

**ASCII flowchart функции `process_affiliate_products`**:

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
import asyncio
from pathlib import Path
from types import SimpleNamespace

# Пример использования process_affiliate_products
async def main():
    ali_aff_prod = AliAffiliatedProducts(language='RU', currency='RUB')
    product_ids = ["32842496247", "32850327275"]  # Замените на реальные ID товаров
    category_root = Path("./test_category")  # Замените на реальный путь к каталогу
    category_root.mkdir(parents=True, exist_ok=True)

    products = await ali_aff_prod.process_affiliate_products(product_ids, category_root)

    if products:
        for product in products:
            print(f"Product Title: {product.product_title}")
            print(f"Promotion Link: {product.promotion_link}")
            print(f"Local Image Path: {product.local_image_path}")
            if hasattr(product, 'local_video_path'):
                print(f"Local Video Path: {product.local_video_path}")
    else:
        print("No products processed.")

if __name__ == "__main__":
    asyncio.run(main())