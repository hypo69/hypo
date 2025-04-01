# Модуль `ali_promo_campaign.py`

## Обзор

Модуль `ali_promo_campaign.py` предназначен для управления рекламными кампаниями на платформе AliExpress. Он включает в себя функциональность для обработки данных о категориях и товарах, создания и редактирования JSON-файлов с информацией о кампаниях, а также использование AI для генерации данных о кампаниях.

## Подробнее

Модуль предоставляет класс `AliPromoCampaign`, который позволяет загружать и обрабатывать данные рекламных кампаний, управлять категориями и товарами, а также использовать ИИ для генерации описаний и других данных. Поддерживаются различные языки и валюты, обеспечивая гибкость в настройке кампаний.

## Классы

### `AliPromoCampaign`

**Описание**: Класс для управления рекламной кампанией AliExpress.

**Принцип работы**:
Класс `AliPromoCampaign` предоставляет методы для инициализации, обработки и управления рекламными кампаниями на платформе AliExpress. Он включает в себя загрузку данных о кампаниях, обработку категорий и товаров, а также использование ИИ для генерации описаний и других данных.

**Методы**:
- `__init__`: Инициализация объекта `AliPromoCampaign`.
- `_models_payload`: Подготовка полезной нагрузки моделей.
- `process_campaign`: Итерация по категориям и обработка товаров.
- `process_campaign_category`: Обработка конкретной категории в кампании.
- `process_new_campaign`: Создание новой рекламной кампании.
- `process_ai_category`: Обработка AI-данных для категории.
- `process_category_products`: Обработка товаров в категории.
- `dump_category_products_files`: Сохранение данных о товарах в JSON-файлы.
- `set_categories_from_directories`: Установка категорий из директорий.
- `generate_output`: Сохранение данных о товарах в различных форматах.
- `generate_html`: Создание HTML-файла для категории.
- `generate_html_for_campaign`: Генерация HTML-страниц для рекламной кампании.

```python
class AliPromoCampaign:
    """Управление рекламной кампанией."""

    # Class attributes declaration
    language: str = None
    currency: str = None
    base_path: Path = None
    campaign_name: str = None
    campaign: SimpleNamespace = None
    campaign_ai: SimpleNamespace = None
    gemini: GoogleGenerativeAI = None
    openai: OpenAIModel = None

    def __init__(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
        model:str = 'openai'
    ):
        """Инициализация объекта AliPromoCampaign для рекламной кампании.

        Args:
            campaign_file (Optional[str | Path]): Путь к файлу кампании или ссылка для загрузки кампании.
            campaign_name (Optional[str]): Название кампании.
            language (Optional[str | dict]): Язык, используемый в кампании.
            currency (Optional[str]): Валюта, используемая в кампании.

        Returns:
            SimpleNamespace: Объект, представляющий кампанию.

        Example:
            >>> campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
            >>> print(campaign.campaign_name)

        """
        ...

    def _models_payload(self):
        """ """
        ...

    def process_campaign(self):
        """Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

        Example:
            >>> campaign.process_campaign()
        """
        ...

    def process_campaign_category(
        self, category_name: str
    ) -> list[SimpleNamespace] | None:
        """
        Processes a specific category within a campaign for all languages and currencies.
        @param campaign_name: Name of the advertising campaign.
        @param category_name: Category for the campaign.
        @param language: Language for the campaign.
        @param currency: Currency for the campaign.
        @return: List of product titles within the category.
        """
        ...

    def process_new_campaign(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
    ):
        """Создание новой рекламной кампании.
        Условия для создания кампании:
        - директория кампании с питоник названием
        - вложенная директория `campaign`, в ней директории с питоник названиями категорий
        - файл sources.txt и/или директория `sources` с файлами `<product)id>.html`

        Args:
            campaign_name (Optional[str]): Название рекламной кампании.
            language (Optional[str]): Язык для кампании (необязательно).
            currency (Optional[str]): Валюта для кампании (необязательно).

        Returns:
            List[Tuple[str, Any]]: Список кортежей с именами категорий и их обработанными результатами.

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
        ...

    def process_ai_category(self, category_name: Optional[str] = None):
        """Processes the AI campaign for a specified category or all categories.

            This method processes AI-generated data for the specified category in the campaign.
            If no category name is provided, it processes all categories.

            Args:
                category_name (Optional[str]): The name of the category to process. If not provided, all categories are processed.

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
        ...

    def process_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """Processes products in a specific category.

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
                    The function attempts to read product IDs from both HTML files and text files within the specified category\'s
                    `sources` directory. If no product IDs are found, an error is logged, and the function returns `None`.
                    If affiliated products are found, they are returned; otherwise, an error is logged, and the function returns `None`.
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
        ...

    def dump_category_products_files(
        self, category_name: str, products: List[SimpleNamespace]
    ):
        """Сохранение данных о товарах в JSON файлы.

        Args:
            category_name (str): Имя категории.
            products (List[SimpleNamespace]): Список объектов SimpleNamespace, представляющих товары.

        Example:
            >>> campaign.dump_category_products_files("Electronics", products)
        """
        ...

    def set_categories_from_directories(self):
        """Устанавливает категории рекламной кампании из названий директорий в `category`.

        Преобразует каждый элемент списка категорий в объект `SimpleNamespace` с атрибутами
        `category_name`, `title`, и `description`.

        Example:
            >>> self.set_categories_from_directories()
            >>> print(self.campaign.category.category1.category_name)
        """
        ...

    
    async def generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
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

        ```

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
        ...
   
    async def generate_html(self, campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
        """ Creates an HTML file for the category and a root index file.
    
        @param products_list: List of products to include in the HTML.
        @param category_path: Path to save the HTML file.
        """
        ...
    
    def generate_html_for_campaign(self, campaign_name: str):
        """Генерирует HTML-страницы для рекламной кампании.

        Args:
            campaign_name (str): Имя рекламной кампании.

        Example:
            >>> campaign.generate_html_for_campaign("HolidaySale")
        """
        ...
```

### `AliPromoCampaign.__init__`

```python
    def __init__(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
        model:str = 'openai'
    ):
        """Инициализация объекта AliPromoCampaign для рекламной кампании.

        Args:
            campaign_file (Optional[str | Path]): Путь к файлу кампании или ссылка для загрузки кампании.
            campaign_name (Optional[str]): Название кампании.
            language (Optional[str | dict]): Язык, используемый в кампании.
            currency (Optional[str]): Валюта, используемая в кампании.

        Returns:
            SimpleNamespace: Объект, представляющий кампанию.

        Example:
            >>> campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
            >>> print(campaign.campaign_name)

        """
        ...
```

**Назначение**:
Инициализирует объект `AliPromoCampaign` для управления рекламной кампанией. Метод определяет основные атрибуты кампании, такие как название, язык и валюта. Если файл кампании не найден, запускается процесс создания новой кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (Optional[str], optional): Язык, используемый в кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта, используемая в кампании. По умолчанию `None`.
- `model` (str): Используемая модель ИИ. По умолчанию `'openai'`.

**Как работает функция**:

1. **Определение пути к файлу кампании**:
   - Определяется путь к файлу конфигурации кампании на основе названия кампании, языка и валюты.
2. **Загрузка конфигурации кампании**:
   - Пытается загрузить конфигурацию кампании из JSON-файла с использованием `j_loads_ns`.
   - Если файл не найден, логируется предупреждение, и запускается процесс создания новой кампании.
3. **Создание новой кампании**:
   - Если конфигурация кампании не найдена, вызывается метод `process_new_campaign` для создания новой кампании.
4. **Инициализация языка и валюты**:
   - Если язык и валюта указаны в конфигурации кампании, они используются. В противном случае используются переданные значения.
5. **Инициализация моделей**:
   - Вызывается метод `_models_payload` для инициализации используемых моделей машинного обучения.

**Примеры**:
```python
>>> campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
>>> print(campaign.campaign_name)
SummerSale
```

### `AliPromoCampaign._models_payload`

```python
    def _models_payload(self):
        """ """
        ...
```

**Назначение**:
Подготавливает полезную нагрузку для моделей машинного обучения, используемых в кампании.

**Как работает функция**:

1. **Определение пути к файлу системных инструкций**:
   - Определяется путь к файлу, содержащему системные инструкции для моделей машинного обучения.
2. **Чтение системных инструкций**:
   - Считывает содержимое файла системных инструкций с использованием функции `read_text_file`.
3. **Инициализация модели Gemini**:
   - Инициализирует модель `GoogleGenerativeAI` с использованием прочитанных системных инструкций.
4. **Определение ID ассистента**:
   - Определяет ID ассистента, используемого для создания категорий и описаний на основе списка названий товаров.
5. **Опциональная инициализация модели OpenAI**:
   - Комментирует инициализацию модели `OpenAIModel`, возможно, для переключения между моделями.

### `AliPromoCampaign.process_campaign`

```python
    def process_campaign(self):
        """Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

        Example:
            >>> campaign.process_campaign()
        """
        ...
```

**Назначение**:
Итерируется по категориям рекламной кампании и обрабатывает товары каждой категории с использованием генератора партнерских ссылок.

**Как работает функция**:

1. **Получение списка названий категорий**:
   - Получает список названий категорий из директории `category` в базовом пути кампании с использованием функции `get_directory_names`.
2. **Итерация по категориям**:
   - Итерируется по списку названий категорий.
3. **Обработка товаров категории**:
   - Для каждой категории вызывается метод `process_category_products` для обработки товаров.
4. **Обработка AI-данных категории**:
   - Для каждой категории вызывается метод `process_ai_category` для обработки AI-данных.

**Примеры**:
```python
>>> campaign.process_campaign()
```

### `AliPromoCampaign.process_campaign_category`

```python
    def process_campaign_category(
        self, category_name: str
    ) -> list[SimpleNamespace] | None:
        """
        Processes a specific category within a campaign for all languages and currencies.
        @param campaign_name: Name of the advertising campaign.
        @param category_name: Category for the campaign.
        @param language: Language for the campaign.
        @param currency: Currency for the campaign.
        @return: List of product titles within the category.
        """
        ...
```

**Назначение**:
Обрабатывает конкретную категорию в кампании для всех языков и валют.

**Параметры**:
- `category_name` (str): Название категории для обработки.

**Как работает функция**:

1. **Обработка товаров категории**:
   - Вызывает метод `process_category_products` для обработки товаров в указанной категории.
2. **Обработка AI-данных категории**:
   - Вызывает метод `process_ai_category` для обработки AI-данных в указанной категории.

### `AliPromoCampaign.process_new_campaign`

```python
    def process_new_campaign(
        self,
        campaign_name: str,
        language: Optional[str] = None,
        currency: Optional[str] = None,
    ):
        """Создание новой рекламной кампании.
        Условия для создания кампании:
        - директория кампании с питоник названием
        - вложенная директория `campaign`, в ней директории с питоник названиями категорий
        - файл sources.txt и/или директория `sources` с файлами `<product)id>.html`

        Args:
            campaign_name (Optional[str]): Название рекламной кампании.
            language (Optional[str]): Язык для кампании (необязательно).
            currency (Optional[str]): Валюта для кампании (необязательно).

        Returns:
            List[Tuple[str, Any]]: Список кортежей с именами категорий и их обработанными результатами.

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
        ...
```

**Назначение**:
Создает новую рекламную кампанию, включая установку языка, валюты, категорий и обработку данных с использованием AI.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str], optional): Язык для кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта для кампании. По умолчанию `None`.

**Как работает функция**:

1. **Определение локали**:
   - Если язык и валюта не предоставлены, используется предопределенный список локалей.
   - Если язык и валюта предоставлены, используется только указанная локаль.
2. **Итерация по локалям**:
   - Итерируется по списку локалей (язык и валюта).
3. **Инициализация кампании**:
   - Для каждой локали устанавливаются язык и валюта кампании.
   - Создается объект `SimpleNamespace` для представления кампании с основными атрибутами.
4. **Установка категорий**:
   - Вызывается метод `set_categories_from_directories` для установки категорий кампании на основе структуры директорий.
5. **Создание AI-кампании**:
   - Создается копия объекта кампании для AI-обработки.
   - Формируется имя файла для AI-кампании.
6. **Обработка категорий**:
   - Итерируется по категориям кампании.
   - Для каждой категории вызывается метод `process_category_products` для обработки товаров.
   - Для каждой категории вызывается метод `process_ai_category` для обработки AI-данных.
   - Сохраняются AI-данные кампании в JSON-файл.

**Примеры**:
```python
>>> campaign.process_new_campaign(campaign_name="HolidaySale", language="RU", currency="ILS")
```

### `AliPromoCampaign.process_ai_category`

```python
    def process_ai_category(self, category_name: Optional[str] = None):
        """Processes the AI campaign for a specified category or all categories.

            This method processes AI-generated data for the specified category in the campaign.
            If no category name is provided, it processes all categories.

            Args:
                category_name (Optional[str]): The name of the category to process. If not provided, all categories are processed.

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
        ...
```

**Назначение**:
Обрабатывает AI-данные для указанной категории или для всех категорий в кампании.

**Параметры**:
- `category_name` (Optional[str], optional): Название категории для обработки. Если не указано, обрабатываются все категории. По умолчанию `None`.

**Внутренние функции**:
- `_process_category(category_name: str)`: Обрабатывает AI-данные для конкретной категории и обновляет данные кампании.
  - **Назначение**:
    Обрабатывает AI-данные для указанной категории и обновляет данные кампании.
  - **Как работает функция**:
    1. **Определение пути к файлу названий товаров**:
       - Определяет путь к файлу, содержащему названия товаров для указанной категории.
    2. **Чтение названий товаров**:
       - Считывает названия товаров из файла с использованием функции `read_text_file`.
    3. **Формирование запроса**:
       - Формирует запрос, включающий язык кампании, название категории и названия товаров.
    4. **Проверка наличия моделей**:
       - Проверяет, инициализированы ли модели `gemini` и `openai`. Если нет, вызывает метод `_models_payload` для их инициализации.
    5. **Получение ответа от модели**:
       - Определяет функцию `get_response` для получения