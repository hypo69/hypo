# Модуль для генерации партнерских продуктов AliExpress

## Обзор

Этот модуль предназначен для сбора полных данных о продуктах AliExpress по предоставленным URL или ID продуктов. Он включает в себя функциональность для получения партнерских ссылок, сохранения изображений и видео, а также генерации HTML-шаблонов для рекламных кампаний.

## Подробнее

Модуль `AliAffiliatedProducts` наследуется от класса `AliApi` и расширяет его функциональность для работы с партнерскими продуктами AliExpress. Он позволяет обрабатывать списки ID продуктов или URL, получать партнерские ссылки, сохранять изображения и видео, а также подготавливать данные для рекламных кампаний.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора данных о партнерских продуктах AliExpress.

**Как работает класс**:
1.  Инициализируется с указанием языка и валюты.
2.  Предоставляет метод `process_affiliate_products` для обработки списка ID продуктов или URL.
3.  Получает партнерские ссылки для каждого продукта.
4.  Сохраняет изображения и видео продуктов локально.
5.  Подготавливает данные о продуктах для дальнейшего использования в рекламных кампаниях.

**Методы**:

*   `__init__`: Инициализирует класс `AliAffiliatedProducts`.
*   `process_affiliate_products`: Обрабатывает список ID продуктов или URL и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.

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
        ...
```

**Назначение**: Инициализирует класс `AliAffiliatedProducts`, устанавливая язык и валюту для рекламной кампании.

**Параметры**:

*   `language` (str | dict): Язык для кампании (по умолчанию 'EN').
*   `currency` (str): Валюта для кампании (по умолчанию 'USD').
*   `*args`: Произвольные позиционные аргументы, передаваемые в родительский класс.
*   `**kwargs`: Произвольные именованные аргументы, передаваемые в родительский класс.

**Как работает функция**:

1.  Проверяет, указаны ли язык и валюта. Если нет, логирует критическую ошибку и завершает работу.
2.  Вызывает конструктор родительского класса (`AliApi`) с переданными аргументами.
3.  Устанавливает значения атрибутов `language` и `currency` из переданных параметров.

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
    ...
```

**Назначение**: Обрабатывает список ID продуктов или URL, получает партнерские ссылки и сохраняет изображения и видео продуктов.

**Параметры**:

*   `prod_ids` (list[str]): Список URL или ID продуктов.
*   `category_root` (Path | str): Корневой путь к каталогу категории.

**Возвращает**:

*   `list[SimpleNamespace]`: Список обработанных продуктов с партнерскими ссылками и сохраненными изображениями.

**Как работает функция**:

1.  Инициализирует списки для хранения партнерских ссылок и URL продуктов.
2.  Нормализует URL продуктов, приводя их к виду `https://aliexpress.com/item/<product_id>.html`.
3.  Для каждого URL продукта получает партнерские ссылки с использованием метода `get_affiliate_links` родительского класса `AliApi`.
4.  Если партнерская ссылка найдена, добавляет ее в список `_promotion_links` и URL продукта в список `_prod_urls`.
5.  Если партнерские ссылки не найдены, логирует предупреждение и возвращает `None`.
6.  Получает детали продукта для каждого URL с использованием метода `retrieve_product_details`.
7.  Для каждого продукта сохраняет изображение и, если есть, видео.
8.  Сохраняет данные о продукте в формате JSON.
9.  Возвращает список обработанных продуктов.

**Внутренние переменные и их назначение**:

*   `_promotion_links` (list): Список партнерских ссылок, полученных для продуктов.
*   `_prod_urls` (list): Список URL продуктов, для которых были получены партнерские ссылки.
*   `normilized_prod_urls` (list[str]): Список нормализованных URL продуктов.
*   `print_flag` (str): Флаг для переключения режима печати в одну строку (использовался для отладки).
*   `product_titles` (list): Список названий продуктов.
*   `product_titles_path` (Path): Путь к файлу, в котором сохраняются названия продуктов.
*   `image_path` (Path): Путь, по которому сохраняется изображение продукта.
*   `video_path` (Path): Путь, по которому сохраняется видео продукта.
*   `parsed_url` (Path): Результат парсинга URL видео продукта.
*   `suffix`   (str): Суффикс URL продукта.
*   `affiliated_products_list` (list[SimpleNamespace]): Список, содержащий информацию о всех обработанных товарах.

**Примеры**:

```python
prod_ids = ["https://aliexpress.com/item/1234567890.html", "https://aliexpress.com/item/0987654321.html"]
category_root = "/path/to/category"
affiliated_products = await self.process_affiliate_products(prod_ids, category_root)
for product in affiliated_products:
    print(product.product_title, product.promotion_link)