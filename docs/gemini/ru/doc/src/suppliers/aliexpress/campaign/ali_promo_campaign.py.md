# Модуль `ali_promo_campaign.py`

## Обзор

Модуль предназначен для управления рекламными кампаниями на платформе AliExpress, включая обработку данных о категориях и товарах, создание и редактирование JSON-файлов с информацией о кампаниях, а также использование AI для генерации данных о кампаниях.

## Подробнее

Класс `AliPromoCampaign` позволяет загружать и обрабатывать данные рекламных кампаний, управлять категориями и товарами, а также использовать ИИ для генерации описаний и других данных. Модуль поддерживает различные языки и валюты, обеспечивая гибкость в настройке кампаний.

## Классы

### `AliPromoCampaign`

**Описание**: Управление рекламной кампанией.

**Принцип работы**:
Класс `AliPromoCampaign` предназначен для управления рекламными кампаниями на платформе AliExpress. Он позволяет инициализировать рекламную кампанию, обрабатывать данные о категориях и товарах, использовать ИИ для генерации данных о кампаниях, а также сохранять сгенерированные данные в JSON-файлы. Класс поддерживает различные языки и валюты, обеспечивая гибкость в настройке кампаний.

**Методы**:
- `__init__`: Инициализация объекта `AliPromoCampaign`.
- `_models_payload`:
- `process_campaign`: Итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.
- `process_campaign_category`: Processes a specific category within a campaign for all languages and currencies.
- `process_new_campaign`: Создание новой рекламной кампании.
- `process_ai_category`: Processes the AI campaign for a specified category or all categories.
- `process_category_products`: Processes products in a specific category.
- `dump_category_products_files`: Сохранение данных о товарах в JSON файлы.
- `set_categories_from_directories`: Устанавливает категории рекламной кампании из названий директорий в `category`.
- `generate_output`:
- `generate_html`: Creates an HTML file for the category and a root index file.
- `generate_html_for_campaign`: Генерирует HTML-страницы для рекламной кампании.

### `__init__`

```python
def __init__(
    self,
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
    model:str = 'openai'
)
```

**Назначение**: Инициализация объекта AliPromoCampaign для рекламной кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (Optional[str], optional): Язык, используемый в кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта, используемая в кампании. По умолчанию `None`.
- `model` (str): Модель для обработки. По умолчанию `openai`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Функция инициализирует объект `AliPromoCampaign` с заданными параметрами, такими как название кампании, язык и валюта.
2.  Определяется базовый путь к файлам кампании в Google Drive.
3.  Загружается файл кампании, если он существует. Если файл не найден, запускается процесс создания новой рекламной кампании.
4.  Инициализируются модели AI для дальнейшей обработки данных.

```ascii
   Начало
     ↓
   Определение базового пути к файлам кампании
     ↓
   Загрузка файла кампании (JSON)
     ↓
   Файл существует?
     ├ Да: Продолжение работы с загруженными данными
     └ Нет: Запуск процесса создания новой рекламной кампании
     ↓
   Инициализация моделей AI
     ↓
   Конец
```

**Примеры**:

```python
campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
print(campaign.campaign_name)
```

### `_models_payload`

```python
def _models_payload(self):
    """ """
```

**Назначение**:

**Как работает функция**:
1. Определяется путь к файлу с системными инструкциями для AI.
2. Считываются системные инструкции из файла.
3. Инициализируется модель Google Gemini с системными инструкциями.

```ascii
    Начало
     ↓
    Определение пути к файлу с системными инструкциями для AI
     ↓
    Считывание системных инструкций из файла
     ↓
    Инициализация модели Google Gemini с системными инструкциями
     ↓
    Конец
```

### `process_campaign`

```python
def process_campaign(self):
    """Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

    Example:
        >>> campaign.process_campaign()
    """
```

**Назначение**: Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

**Параметры**:
- `self` (AliPromoCampaign): Экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Функция получает список названий категорий из директорий в базовом пути кампании.
2.  Для каждой категории вызывается метод `process_category_products` для обработки товаров в категории.
3.  Затем вызывается метод `process_ai_category` для обработки данных категории с использованием AI.

```ascii
   Начало
     ↓
   Получение списка названий категорий
     ↓
   Для каждой категории:
     ├─> Обработка товаров в категории (`process_category_products`)
     └─> Обработка данных категории с использованием AI (`process_ai_category`)
     ↓
   Конец
```

**Примеры**:

```python
campaign.process_campaign()
```

### `process_campaign_category`

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
```

**Назначение**: Processes a specific category within a campaign for all languages and currencies.

**Как работает функция**:

1.  Вызывается метод `process_category_products` для обработки товаров в категории.
2.  Вызывается метод `process_ai_category` для обработки данных категории с использованием AI.

```ascii
     Начало
      ↓
     Обработка товаров в категории (process_category_products)
      ↓
     Обработка данных категории с использованием AI (process_ai_category)
      ↓
     Конец
```

### `process_new_campaign`

```python
def process_new_campaign(
    self,
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
)
```

**Назначение**: Создание новой рекламной кампании.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str], optional): Язык для кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта для кампании. По умолчанию `None`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Определяется локаль кампании (язык и валюта). Если язык и валюта не предоставлены, используются значения по умолчанию.
2.  Для каждой локали устанавливаются язык и валюта кампании.
3.  Инициализируется объект кампании.
4.  Устанавливаются категории из названий директорий.
5.  Создается копия кампании для AI.
6.  Для каждой категории обрабатываются товары и AI-данные.
7.  Сохраняются AI-данные кампании в JSON-файл.

```ascii
   Начало
     ↓
   Проверка наличия языка и валюты
     ├ Нет: Использование локалей по умолчанию
     ↓
   Для каждой локали:
     ├─> Установка языка и валюты кампании
     ├─> Инициализация объекта кампании
     ├─> Установка категорий из директорий
     ├─> Создание копии кампании для AI
     ├─> Для каждой категории:
     │   ├─> Обработка товаров (`process_category_products`)
     │   └─> Обработка AI-данных (`process_ai_category`)
     └─> Сохранение AI-данных кампании в JSON-файл
     ↓
   Конец
```

**Примеры**:

```python
campaign.process_new_campaign(campaign_name="HolidaySale", language="RU", currency="ILS")
```

### `process_ai_category`

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
```

**Назначение**: Processes the AI campaign for a specified category or all categories.

**Параметры**:
- `category_name` (Optional[str], optional): Имя категории для обработки. Если не указано, обрабатываются все категории.

**Как работает функция**:

1.  Создается копия объекта кампании для AI.
2.  Определяется внутренняя функция `_process_category`, которая обрабатывает данные AI для указанной категории.
    - Считываются названия товаров из файла.
    - Формируется запрос для AI.
    - Получается ответ от AI-модели.
    - Обновляются или создаются данные категории в объекте кампании.
3.  Для каждой категории вызывается функция `_process_category`.
4.  Сохраняются обновленные данные кампании в файл.

**Внутренние функции**:

#### `_process_category`

```python
def _process_category(category_name: str):
    """Processes AI-generated category data and updates the campaign category."""
```

**Назначение**: Processes AI-generated category data and updates the campaign category.

**Параметры**:
- `category_name` (str): Имя категории для обработки.

**Как работает функция**:

1.  Определяется путь к файлу с названиями товаров для указанной категории.
2.  Считываются названия товаров из файла.
3.  Формируется запрос для AI на основе языка кампании, названия категории и списка товаров.
4.  Получается ответ от AI-модели.
5.  Преобразуется ответ машины в объект `SimpleNamespace`.
6.  Если категория существует, обновляются ее атрибуты. Если категория не существует, она создается.
7.  Логируются сообщения об обновлении или создании категории.

##### `get_response`

```python
def get_response(_attempts: int = 5):
    """Gets the response from the AI model."""
```

**Назначение**: Gets the response from the AI model.

**Как работает функция**:
1. Выполняется запрос к модели gemini

**Примеры**:

```python
campaign.process_ai_category("Electronics")
campaign.process_ai_category()
```

### `process_category_products`

```python
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
```

**Назначение**: Processes products in a specific category.

**Параметры**:
- `category_name` (str): The name of the category.

**Возвращает**:
- `Optional[List[SimpleNamespace]]`: A list of `SimpleNamespace` objects representing the products. Returns `None` if no products are found.

**Как работает функция**:

1.  Определяется внутренняя функция `read_sources`, которая считывает источники продуктов и извлекает ID продуктов.
2.  Вызывается функция `read_sources` для получения ID продуктов.
3.  Если ID продуктов не найдены, логируется ошибка и возвращается `None`.
4.  Инициализируется объект `AliAffiliatedProducts` с языком и валютой кампании.
5.  Вызывается метод `process_affiliate_products` для обработки партнерских продуктов.
6.  Если партнерские продукты не найдены, логируется ошибка и возвращается `None`.
7.  Возвращается список партнерских продуктов.

**Внутренние функции**:

#### `read_sources`

```python
def read_sources(category_name: str) -> Optional[List[str]]:
    """Reads product sources and extracts product IDs.

    Args:
        category_name (str): The name of the category.

    Returns:
        Optional[List[str]]: A list of product IDs if found; otherwise, `None`.

    Example:
        >>> product_ids: Optional[List[str]] = read_sources("Electronics")
        >>> print(product_ids)
        ['12345', '67890', ...]

    Notes:
        This function looks for product IDs in both HTML files and a `sources.txt` file located
        in the category\'s `sources` directory. If no product IDs are found, it returns `None`.
    """
```

**Назначение**: Reads product sources and extracts product IDs.

**Параметры**:
- `category_name` (str): The name of the category.

**Возвращает**:
- `Optional[List[str]]`: A list of product IDs if found; otherwise, `None`.

**Как работает функция**:

1.  Инициализируется пустой список `product_ids`.
2.  Получаются имена HTML файлов из директории `sources` указанной категории.
3.  Если HTML файлы найдены, извлекаются ID продуктов из HTML файлов и добавляются в список `product_ids`.
4.  Считываются URL продуктов из файла `sources.txt`.
5.  Если URL продуктов найдены, извлекаются ID продуктов из URL и добавляются в список `product_ids`.
6.  Если список `product_ids` пуст, возвращается `None`.
7.  Возвращается список `product_ids`.

**Примеры**:

```python
products: List[SimpleNamespace] = campaign.process_category_products("Electronics")
print(len(products))
for product in products:
    pprint(product)
```

### `dump_category_products_files`

```python
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
```

**Назначение**: Сохранение данных о товарах в JSON файлы.

**Параметры**:
- `category_name` (str): Имя категории.
- `products` (List[SimpleNamespace]): Список объектов SimpleNamespace, представляющих товары.

**Как работает функция**:

1.  Проверяется, есть ли товары для сохранения. Если нет, функция завершается.
2.  Определяется путь к директории категории.
3.  Для каждого товара в списке:
    - Извлекается `product_id`. Если его нет, товар пропускается.
    - Данные товара сохраняются в JSON файл с именем `{product_id}.json` в директории категории.
4.  Логируется сообщение о сохранении товара.

**Примеры**:

```python
campaign.dump_category_products_files("Electronics", products)
```

### `set_categories_from_directories`

```python
def set_categories_from_directories(self):
    """Устанавливает категории рекламной кампании из названий директорий в `category`.

    Преобразует каждый элемент списка категорий в объект `SimpleNamespace` с атрибутами
    `category_name`, `title`, и `description`.

    Example:
        >>> self.set_categories_from_directories()
        >>> print(self.campaign.category.category1.category_name)
    """
```

**Назначение**: Устанавливает категории рекламной кампании из названий директорий в `category`.

**Как работает функция**:

1.  Определяется путь к директории `category`.
2.  Получается список названий директорий в директории `category`.
3.  Проверяется, является ли `self.campaign.category` объектом `SimpleNamespace`. Если нет, он создается.
4.  Для каждой категории в списке:
    - Создается объект `SimpleNamespace` с атрибутами `category_name`, `title` и `description`.
    - Этот объект устанавливается как атрибут `self.campaign.category` с именем категории.

**Примеры**:

```python
self.set_categories_from_directories()
print(self.campaign.category.category1.category_name)
```

### `generate_output`

```python
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

**Назначение**:
Saves product data in various formats.

**Параметры**:
- `campaign_name` (str): The name of the campaign for the output files.
- `category_path` (str | Path): The path to save the output files.
- `products_list` (list[SimpleNamespace] | SimpleNamespace): List of products or a single product to save.

**Как работает функция**:

1.  Форматируется текущая дата и время для использования в именах файлов.
2.  `products_list` преобразуется в список, если это не список.
3.  Инициализируются пустые списки `_data_for_openai`, `_promotion_links_list` и `_product_titles`.
4.  Для каждого товара в `products_list`:
    - Создается словарь `categories_convertor`, содержащий информацию о категориях товара.
    - `categories_convertor` добавляется в объект товара.
    - Сохраняется JSON файл для каждого товара.
    - Заголовок товара добавляется в список `_product_titles`.
    - Ссылка на продвижение товара добавляется в список `_promotion_links_list`.
5.  Вызывается `save_product_titles` для сохранения заголовков товаров.
6.  Вызывается `save_promotion_links` для сохранения ссылок на продвижение товаров.
7.  Вызывается `generate_html` для генерации HTML страницы для товаров.

### `generate_html`

```python
async def generate_html(self, campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
    """ Creates an HTML file for the category and a root index file.

    @param products_list: List of products to include in the HTML.
    @param category_path: Path to save the HTML file.
    """
```

**Назначение**:
Creates an HTML file for the category and a root index file.

**Параметры**:
- `products_list` (list[SimpleNamespace] | SimpleNamespace): List of products to include in the HTML.
- `category_path` (str | Path): Path to save the HTML file.

**Как работает функция**:

1.  Преобразует `products_list` в список, если это не список.
2.  Определяет имя категории из пути `category_path`.
3.  Инициализирует словарь `category` для хранения заголовков товаров.
4.  Создает HTML-контент с заголовками товаров, ценами и ссылками для каждого товара в `products_list`.
5.  Сохраняет HTML-контент в файл с именем категории.
6.  Создает главную страницу `index.html` с ссылками на все категории.
### `generate_html_for_campaign`

```python
def generate_html_for_campaign(self, campaign_name: str):
    """Генерирует HTML-страницы для рекламной кампании.

    Args:
        campaign_name (str): Имя рекламной кампании.

    Example:
        >>> campaign.generate_html_for_campaign("HolidaySale")
    """
```

**Назначение**: Генерирует HTML-страницы для рекламной кампании.

**Параметры**:
- `campaign_name` (str): Имя рекламной кампании.

**Как работает функция**:

1.  Определяется корневой путь к рекламной кампании.
2.  Получается список категорий из директории `category`.
3.  Для каждой категории:
    - Определяется путь к категории.
    - Получаются товары для категории.
    - Если товары найдены:
        - Генерируются HTML-страницы для каждого товара с использованием `ProductHTMLGenerator`.
        - Генерируется HTML-страница категории с использованием `CategoryHTMLGenerator`.
    - Если товары не найдены, логируется предупреждение.
4.  Генерируется HTML-страница рекламной кампании с использованием `CampaignHTMLGenerator`.

**Примеры**:

```python
campaign.generate_html_for_campaign("HolidaySale")