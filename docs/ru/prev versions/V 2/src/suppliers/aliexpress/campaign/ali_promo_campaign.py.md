# Модуль `ali_promo_campaign.py`

## Обзор

Модуль `ali_promo_campaign.py` предназначен для управления рекламными кампаниями на платформе AliExpress. Он включает в себя функциональность для обработки данных о категориях и товарах, создания и редактирования JSON-файлов с информацией о кампаниях, а также использования AI для генерации данных о кампаниях.

## Содержание

1.  [Класс `AliPromoCampaign`](#класс-alipromocampaign)
    *   [Метод `__init__`](#__init__)
    *   [Метод `_models_payload`](#_models_payload)
    *   [Метод `process_campaign`](#process_campaign)
    *   [Метод `process_campaign_category`](#process_campaign_category)
    *   [Метод `process_new_campaign`](#process_new_campaign)
    *   [Метод `process_ai_category`](#process_ai_category)
    *   [Метод `process_category_products`](#process_category_products)
    *   [Метод `dump_category_products_files`](#dump_category_products_files)
    *   [Метод `set_categories_from_directories`](#set_categories_from_directories)
    *   [Метод `generate_output`](#generate_output)
    *   [Метод `generate_html`](#generate_html)
    *   [Метод `generate_html_for_campaign`](#generate_html_for_campaign)

## Класс `AliPromoCampaign`

**Описание**: Управляет рекламной кампанией.

### `__init__`

```python
def __init__(self, campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None, model:str = 'openai') -> None:
    """
    Инициализация объекта AliPromoCampaign для рекламной кампании.

    Args:
        campaign_name (str): Название кампании.
        language (Optional[str], optional): Язык, используемый в кампании. По умолчанию `None`.
        currency (Optional[str], optional): Валюта, используемая в кампании. По умолчанию `None`.
        model (str, optional): Модель AI, используемая в кампании. По умолчанию 'openai'.

    Returns:
        None

    Example:
        >>> campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
        >>> print(campaign.campaign_name)
    """
```

### `_models_payload`

```python
def _models_payload(self) -> None:
    """
    Инициализация AI моделей.
    """
```

### `process_campaign`

```python
def process_campaign(self) -> None:
    """
    Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

    Example:
        >>> campaign.process_campaign()
    """
```

### `process_campaign_category`

```python
def process_campaign_category(self, category_name: str) -> list[SimpleNamespace] | None:
    """
    Processes a specific category within a campaign for all languages and currencies.
    @param category_name: Category for the campaign.
    @return: List of product titles within the category.
    """
```

### `process_new_campaign`

```python
def process_new_campaign(self, campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """
    Создание новой рекламной кампании.
        Условия для создания кампании:
        - директория кампании с питоник названием
        - вложенная директория `campaign`, в ней директории с питоник названиями категорий
        - файл sources.txt и/или директория `sources` с файлами `<product)id>.html`

    Args:
        campaign_name (str): Название рекламной кампании.
        language (Optional[str], optional): Язык для кампании (необязательно).
        currency (Optional[str], optional): Валюта для кампании (необязательно).

    Returns:
        None

    Example:
        >>> campaign.process_new_campaign(campaign_name="HolidaySale", language="RU", currency="ILS")

    Flowchart:
        ┌──────────────────────────────────────────────┐
        │ Start                                        │
        └──────────────────────────────────────────────┘
                          │
                          ▼
        ┌───────────────────────────────────────────────┐
        │ Check if `self.language` and `self.currency`  │
        │ are set                                       │
        └───────────────────────────────────────────────┘
                          │
                ┌─────────┴──────────────────────────┐
                │                                    │
                ▼                                    ▼
        ┌─────────────────────────────┐   ┌──────────────────────────────────────┐
        │Yes: `locale` = `{language:  │   │No: `locale` = {                      │
        │currency}`                   │   │     "EN": "USD",                     │
        │                             │   │     "HE": "ILS",                     │
        │                             │   │     "RU": "ILS"                      │
        │                             │   │    }                                 │
        └─────────────────────────────┘   └──────────────────────────────────────┘
                         │                         │
                         ▼                         ▼
        ┌───────────────────────────────────────────────┐
        │ For each `language`, `currency` in `locale`:  │
        │ - Set `self.language`, `self.currency`        │
        │ - Initialize `self.campaign`                  │
        └───────────────────────────────────────────────┘
                         │
                         ▼
        ┌───────────────────────────────────────────────┐
        │ Call `self.set_categories_from_directories()` │
        │ to populate categories                        │
        └───────────────────────────────────────────────┘
                         │
                         ▼
        ┌───────────────────────────────────────────────┐
        │ Copy `self.campaign` to `self.campaign_ai`    │
        │ and set `self.campaign_ai_file_name`          │
        └───────────────────────────────────────────────┘
                         │
                         ▼
        ┌───────────────────────────────────────────────┐
        │ For each `category_name` in campaign:         │
        │ - Call `self.process_category_products`       │
        │ - Call `self.process_ai_category`             │
        └───────────────────────────────────────────────┘
                         │
                         ▼
        ┌──────────────────────────────────────────────┐
        │ End                                          │
        └──────────────────────────────────────────────┘

    """
```

### `process_ai_category`

```python
def process_ai_category(self, category_name: Optional[str] = None) -> None:
    """
    Processes the AI campaign for a specified category or all categories.

        This method processes AI-generated data for the specified category in the campaign.
        If no category name is provided, it processes all categories.

        Args:
            category_name (Optional[str], optional): The name of the category to process. If not provided, all categories are processed.

        Example:
            >>> campaign.process_ai_category("Electronics")
            >>> campaign.process_ai_category()

        Flowchart:
            ┌──────────────────────────────────────────────┐
            │ Start                                        │
            └──────────────────────────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────────────┐
            │ Load system instructions from JSON file       │
            └───────────────────────────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────────────┐
            │ Initialize AI model with system instructions  │
            └───────────────────────────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────────────┐
            │ Check if `category_name` is provided          │
            └───────────────────────────────────────────────┘
                                │
                ┌─────────────────┴───────────────────┐
                │                                     │
                ▼                                     ▼
        ┌─────────────────────────────────────┐   ┌────────────────────────────────────┐
        │ Process specified category          │   │ Iterate over all categories        │
        │ - Load product titles               │   │ - Call `_process_category`         │
        │ - Generate prompt                   │   │   for each category                │
        │ - Get response from AI model        │   └────────────────────────────────────┘
        │ - Update or add category            │
        └─────────────────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────────────┐
            │ Save updated campaign data to file            │
            └───────────────────────────────────────────────┘
                                │
                                ▼
            ┌──────────────────────────────────────────────┐
            │ End                                          │
            └──────────────────────────────────────────────┘

    """
```

### `process_category_products`

```python
def process_category_products(self, category_name: str) -> Optional[List[SimpleNamespace]]:
    """
    Processes products in a specific category.

            Args:
                category_name (str): The name of the category.

            Returns:
                Optional[List[SimpleNamespace]]: A list of `SimpleNamespace` objects representing the products.
                Returns `None` if no products are found.

            Example:
                >>> products: List[SimpleNamespace] = campaign.process_category_products("Electronics")
                >>> print(len(products))
                20
                >>> for product in products:
                >>>     pprint(product)  # Use pprint from `src.utils.pprint`

            Notes:
                The function attempts to read product IDs from both HTML files and text files within the specified category's
                `sources` directory. If no product IDs are found, an error is logged, and the function returns `None`.
                If affiliated products are found, they are returned; otherwise, an error is logged, and the function returns `None`

            Flowchart:
    ┌───────────────────────────────────────────────────────────┐
    │ Start                                                     │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Call `read_sources(category_name)` to get product IDs     │
    │ - Searches for product IDs in HTML files and sources.txt  │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Check if `prod_ids` is empty                              │
    │ - If empty, log an error and return `None`                │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Initialize `AliAffiliatedProducts` with `language`        │
    │ and `currency`                                            │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Call `process_affiliate_products`                         │
    │ - Pass `campaign`, `category_name`, and `prod_ids`        │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Check if `affiliated_products` is empty                   │
    │ - If empty, log an error and return `None`                │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Return `affiliated_products`                              │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ End                                                       │
    └───────────────────────────────────────────────────────────┘

    """
```

### `dump_category_products_files`

```python
def dump_category_products_files(self, category_name: str, products: List[SimpleNamespace]) -> None:
    """
    Сохранение данных о товарах в JSON файлы.

    Args:
        category_name (str): Имя категории.
        products (List[SimpleNamespace]): Список объектов SimpleNamespace, представляющих товары.

    Example:
        >>> campaign.dump_category_products_files("Electronics", products)
    """
```

### `set_categories_from_directories`

```python
def set_categories_from_directories(self) -> None:
    """
    Устанавливает категории рекламной кампании из названий директорий в `category`.

    Преобразует каждый элемент списка категорий в объект `SimpleNamespace` с атрибутами
    `category_name`, `title`, и `description`.

    Example:
        >>> self.set_categories_from_directories()
        >>> print(self.campaign.category.category1.category_name)
    """
```

### `generate_output`

```python
async def generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace) -> None:
    """
    Saves product data in various formats:

    - `<product_id>.json`: Contains all product parameters, one file per product.
    - `ai_{timestamp}.json`: A common file for all products with specific keys.
    - `promotion_links.txt`: A list of product links, created in the `save_promotion_links()` function.
    - `category_products_titles.json`: File containing title, `product_id`, `first_category_name`, and `second_category_name` of each product in the category.

    Args:
        campaign_name (str): The name of the campaign for the output files.
        category_path (str | Path): The path to save the output files.
        products_list (list[SimpleNamespace] | SimpleNamespace): List of products or a single product to save.

    Returns:
        None

    Example:
        >>> products_list: list[SimpleNamespace] = [
        ...     SimpleNamespace(product_id="123", product_title="Product A", promotion_link="http://example.com/product_a",
        ...                     first_level_category_id=1, first_level_category_name="Category1",
        ...                     second_level_category_id=2, second_level_category_name="Subcategory1",
        ...                     product_main_image_url="http://example.com/image.png", product_video_url="http://example.com/video.mp4"),
        ...     SimpleNamespace(product_id="124", product_title="Product B", promotion_link="http://example.com/product_b",
        ...                     first_level_category_id=1, first_level_category_name="Category1",
        ...                     second_level_category_id=3, second_level_category_name="Subcategory2",
        ...                     product_main_image_url="http://example.com/image2.png", product_video_url="http://example.com/video2.mp4")
        ... ]
        >>> category_path: Path = Path("/path/to/category")
        >>> await generate_output("CampaignName", category_path, products_list)

    Flowchart:
            ┌───────────────────────────────┐
            │  Start `generate_output`      │
            └───────────────────────────────┘
                        │
                        ▼
            ┌───────────────────────────────┐
            │ Format `timestamp` for file   │
            │ names.                        │
            └───────────────────────────────┘
                        │
                        ▼
            ┌───────────────────────────────┐
            │ Check if `products_list` is   │
            │ a list; if not, convert it to │
            │ a list.                       │
            └───────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │ Initialize `_data_for_openai`,│
        │ `_promotion_links_list`, and  │
        │ `_product_titles` lists.      │
        └───────────────────────────────┘
                        │
                        ▼
    ┌─────────────────────────────────────────┐
    │ For each `product` in `products_list`:  │
    └─────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ 1. Create `categories_convertor` dictionary   │
    │ for `product`.                                │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ 2. Add `categories_convertor` to `product`.   │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ 3. Save `product` as `<product_id>.json`.     │
    └───────────────────────────────────────────────┘
                        │
                        ▼
    ┌───────────────────────────────────────────────┐
    │ 4. Append `product_title` and                 │
    │ `promotion_link` to their respective lists.   │
    └───────────────────────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │ Call `save_product_titles`    │
        │ with `_product_titles` and    │
        │ `category_path`.              │
        └───────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │ Call `save_promotion_links`   │
        │ with `_promotion_links_list`  │
        │ and `category_path`.          │
        └───────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │ Call `generate_html` with         │
        │ `campaign_name`, `category_path`, │
        │ and `products_list`.              │
        └───────────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │  End `generate_output`        │
        └───────────────────────────────┘

    ### Flowchart Description

        1. **Start `generate_output`**: The function begins execution.
        2. **Format `timestamp` for file names**: Generate a timestamp to use in filenames.
        3. **Check if `products_list` is a list**: Ensure that `products_list` is in list format.
        4. **Initialize `_data_for_openai`, `_promotion_links_list`, and `_product_titles` lists**: Prepare empty lists to collect data.
        5. **For each `product` in `products_list`**: Process each product in the list.
        - **Create `categories_convertor` dictionary for `product`**: Create a dictionary for category conversion.
        - **Add `categories_convertor` to `product`**: Attach this dictionary to the product.
        - **Save `product` as `<product_id>.json`**: Save product details in a JSON file.
        - **Append `product_title` and `promotion_link` to their respective lists**: Collect titles and links.
        6. **Call `save_product_titles` with `_product_titles` and `category_path`**: Save titles data to a file.
        7. **Call `save_promotion_links` with `_promotion_links_list` and `category_path`**: Save promotion links to a file.
        8. **Call `generate_html` with `campaign_name`, `category_path`, and `products_list`**: Generate HTML output for products.
        9. **End `generate_output`**: The function completes execution.

        This flowchart captures the key steps and processes involved in the `generate_output` function.

    """
```

### `generate_html`

```python
async def generate_html(self, campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace) -> None:
    """
     Creates an HTML file for the category and a root index file.

    @param products_list: List of products to include in the HTML.
    @param category_path: Path to save the HTML file.
    """
```

### `generate_html_for_campaign`

```python
def generate_html_for_campaign(self, campaign_name: str) -> None:
    """
    Генерирует HTML-страницы для рекламной кампании.

    Args:
        campaign_name (str): Имя рекламной кампании.

    Example:
        >>> campaign.generate_html_for_campaign("HolidaySale")
    """
```