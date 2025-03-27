# Модуль `affiliated_products_generator.py`

## Обзор

Модуль `affiliated_products_generator.py` предназначен для получения данных о партнерских продуктах с AliExpress. Он содержит класс `AliAffiliatedProducts`, который позволяет собирать полную информацию о продуктах на основе предоставленных URL-адресов или идентификаторов продуктов. Модуль также включает функциональность для обработки рекламных кампаний, сохранения изображений и видео, а также для подготовки данных для дальнейшего использования.

## Подробнее

Этот модуль является частью системы для работы с партнерской программой AliExpress. Он автоматизирует процесс получения информации о продуктах, создания партнерских ссылок и сохранения необходимых медиафайлов. Класс `AliAffiliatedProducts` наследуется от `AliApi` и расширяет его функциональность, добавляя возможность обработки продуктов и сохранения связанных данных. Модуль использует асинхронные операции для эффективной работы с сетью и файловой системой.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора данных о партнерских продуктах с AliExpress.

**Методы**:
- `__init__`: Инициализирует класс `AliAffiliatedProducts`.
- `process_affiliate_products`: Обрабатывает список идентификаторов или URL-адресов продуктов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.

#### `__init__`

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
        ...
        if not language or not currency:
            logger.critical(f"No language, currency !")
            return
        super().__init__(language, currency)\n        self.language, self.currency = language, currency
```

**Описание**: Инициализирует экземпляр класса `AliAffiliatedProducts`.

**Параметры**:
- `language` (str | dict, optional): Язык для рекламной кампании. По умолчанию `'EN'`.
- `currency` (str, optional): Валюта для рекламной кампании. По умолчанию `'USD'`.

**Примеры**:

```python
ali_products = AliAffiliatedProducts(language='RU', currency='RUB')
```

#### `process_affiliate_products`

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

**Описание**:  Обрабатывает список идентификаторов или URL-адресов продуктов, получает партнерские ссылки, сохраняет изображения и видео.

**Параметры**:
- `prod_ids` (list[str]): Список URL-адресов или идентификаторов продуктов.
- `category_root` (Path | str): Корневой путь к каталогу категории.

**Возвращает**:
- `list[SimpleNamespace]`: Список обработанных продуктов с партнерскими ссылками и сохраненными изображениями.

**Примеры**:

```python
prod_ids = ['1234567890', 'https://aliexpress.com/item/1234567890.html']
category_root = '/path/to/category'
affiliated_products = await ali_api.process_affiliate_products(prod_ids, category_root)
for product in affiliated_products:
    print(product.product_title, product.promotion_link)
```