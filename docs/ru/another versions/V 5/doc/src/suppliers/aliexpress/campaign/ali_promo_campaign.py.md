# Модуль `ali_promo_campaign`

## Обзор

Модуль `ali_promo_campaign.py` предназначен для управления рекламными кампаниями на платформе AliExpress. Он включает в себя обработку данных о категориях и товарах, создание и редактирование JSON-файлов с информацией о кампаниях, а также использование AI для генерации данных о кампаниях.

## Подробней

Этот модуль обеспечивает гибкость в настройке рекламных кампаний, поддерживая различные языки и валюты. Он позволяет загружать и обрабатывать данные рекламных кампаний, управлять категориями и товарами, а также использовать ИИ для генерации описаний и других данных. Модуль предназначен для автоматизации и улучшения процессов, связанных с созданием и управлением рекламными кампаниями на AliExpress.

## Классы

### `AliPromoCampaign`

**Описание**: Класс `AliPromoCampaign` предназначен для управления рекламными кампаниями на платформе AliExpress.

**Как работает класс**:
Класс позволяет инициализировать рекламную кампанию, загружать данные о категориях и товарах, обрабатывать информацию о продуктах в каждой категории, а также использовать AI для генерации контента и оптимизации кампании. Он включает методы для создания новых кампаний, обработки существующих, а также для сохранения и генерации HTML-страниц с информацией о продуктах.

**Методы**:
- `__init__`: Инициализирует объект `AliPromoCampaign`.
- `_models_payload`: Подготавливает полезную нагрузку для моделей AI.
- `process_campaign`: Итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.
- `process_campaign_category`: Обрабатывает указанную категорию в кампании для всех языков и валют.
- `process_new_campaign`: Создает новую рекламную кампанию.
- `process_ai_category`: Обрабатывает AI данные для указанной категории или для всех категорий.
- `process_category_products`: Обрабатывает продукты в указанной категории.
- `dump_category_products_files`: Сохраняет данные о товарах в JSON файлы.
- `set_categories_from_directories`: Устанавливает категории рекламной кампании из названий директорий в `category`.
- `generate_output`: Сохраняет данные о продуктах в различных форматах.
- `generate_html`: Создает HTML-файл для категории и корневой индексный файл.
- `generate_html_for_campaign`: Генерирует HTML-страницы для рекламной кампании.

### `__init__`

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
```

**Описание**: Инициализирует объект `AliPromoCampaign` для работы с рекламной кампанией. Устанавливает основные параметры кампании, такие как название, язык и валюта. Загружает данные кампании из JSON-файла, если он существует, или запускает процесс создания новой кампании, если файл отсутствует.

**Как работает функция**:
1. Устанавливает базовый путь к файлам кампании на Google Drive.
2. Пытается загрузить данные кампании из JSON-файла.
3. Если файл не найден, запускает процесс создания новой кампании.
4. Устанавливает язык и валюту кампании на основе загруженных данных или переданных аргументов.
5. Вызывает метод `_models_payload` для подготовки данных для AI моделей.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (Optional[str], optional): Язык, используемый в кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта, используемая в кампании. По умолчанию `None`.
- `model` (str): Модель ИИ, используемая в кампании. По умолчанию 'openai'.

**Возвращает**:
- Объект `AliPromoCampaign`.

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

**Описание**: Метод `_models_payload` предназначен для подготовки и настройки полезной нагрузки (payload) для моделей искусственного интеллекта (AI), которые будут использоваться в процессе обработки рекламной кампании.

**Как работает функция**:

1.  Определяет путь к файлу с системными инструкциями для AI моделей (`system_instruction.txt`).
2.  Считывает содержимое файла с системными инструкциями.
3.  Инициализирует модель `GoogleGenerativeAI` с использованием прочитанных системных инструкций.
4.  Определяет `assistant_id` для ассистента, ответственного за создание категорий и описаний на основе списка названий товаров.

**Параметры**:
-   Нет параметров.

**Возвращает**:
-   Нет возвращаемого значения.

**Примеры**:
```python
campaign._models_payload()
```

### `process_campaign`

```python
def process_campaign(self):
    """Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

    Example:
        >>> campaign.process_campaign()
    """
```

**Описание**: Функция `process_campaign` итерируется по категориям рекламной кампании и обрабатывает товары каждой категории, используя генератор партнерских ссылок.

**Как работает функция**:
1. Получает список названий папок категорий.
2. Для каждой категории выполняет:
   - Вызывает метод `process_category_products` для обработки товаров в категории.
   - Вызывает метод `process_ai_category` для обработки AI данных категории.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

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

**Описание**: Функция обрабатывает конкретную категорию в рамках кампании для всех языков и валют.

**Как работает функция**:
1.  Вызывает `self.process_category_products` для обработки товаров в указанной категории.
2.  Вызывает `self.process_ai_category` для обработки AI-данных в указанной категории.

**Параметры**:
-   `category_name` (str): Название категории для обработки.

**Возвращает**:
-   `list[SimpleNamespace] | None`: Список названий продуктов в категории.

**Примеры**:
```python
campaign.process_campaign_category(category_name="Electronics")
```

### `process_new_campaign`

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
```

**Описание**: Функция `process_new_campaign` создает новую рекламную кампанию, выполняя ряд шагов по настройке и обработке категорий и товаров.

**Как работает функция**:
1. Определяет локали (язык и валюта) для кампании. Если `language` и `currency` не предоставлены, использует стандартные локали.
2. Для каждой локали устанавливает язык и валюту кампании.
3. Инициализирует объект `self.campaign` с основными параметрами кампании.
4. Вызывает метод `set_categories_from_directories` для установки категорий из директорий.
5. Создает копию `self.campaign` в `self.campaign_ai` для параллельной AI обработки.
6. Устанавливает имя файла для AI кампании.
7. Для каждой категории вызывает `process_category_products` и `process_ai_category` для обработки товаров и AI данных.
8. Сохраняет AI данные кампании в JSON файл.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str], optional): Язык для кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта для кампании. По умолчанию `None`.

**Возвращает**:
- Список кортежей с именами категорий и их обработанными результатами.

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
        └───────────────────────────────────────┐
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

**Описание**: Метод `process_ai_category` обрабатывает AI-сгенерированные данные для указанной категории или для всех категорий в кампании.

**Как работает функция**:
1. Создает копию объекта `self.campaign` для AI обработки.
2. Определяет внутреннюю функцию `_process_category` для обработки данных AI для каждой категории.
3. В функции `_process_category`:
   - Считывает названия продуктов из файла `product_titles.txt`.
   - Формирует prompt для AI модели, включающий язык, название категории и названия продуктов.
   - Получает ответ от AI модели.
   - Преобразует ответ AI модели в объект `SimpleNamespace`.
   - Обновляет или создает атрибуты категории в `campaign_ai.category` на основе ответа AI.
4. Итерируется по всем категориям и вызывает `_process_category` для каждой категории.
5. Сохраняет обновленные AI данные кампании в JSON файл.

**Параметры**:
- `category_name` (Optional[str], optional): Название категории для обработки. Если не указано, обрабатываются все категории.

**Возвращает**:
- `None`

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

**Описание**: Функция обрабатывает продукты в указанной категории, извлекая ID продуктов из HTML-файлов и текстовых файлов, а затем генерируя партнерские ссылки для этих продуктов.

**Как работает функция**:
1. Определяет внутреннюю функцию `read_sources` для чтения ID продуктов из файлов.
2. В функции `read_sources`:
   - Ищет HTML-файлы и файл `sources.txt` в директории категории.
   - Извлекает ID продуктов из HTML-файлов и `sources.txt`.
   - Возвращает список ID продуктов.
3. Вызывает `read_sources` для получения ID продуктов.
4. Если ID продуктов не найдены, логирует ошибку и возвращает `None`.
5. Инициализирует объект `AliAffiliatedProducts` с языком и валютой.
6. Вызывает `process_affiliate_products` для генерации партнерских ссылок.
7. Возвращает список объектов `SimpleNamespace`, представляющих продукты.

**Параметры**:
- `category_name` (str): Название категории для обработки.

**Возвращает**:
- `Optional[List[SimpleNamespace]]`: Список объектов `SimpleNamespace`, представляющих продукты. Возвращает `None`, если продукты не найдены.

**Примеры**:
```python
products: List[SimpleNamespace] = campaign.process_category_products("Electronics")
print(len(products))
for product in products:
    pprint(product)  # Используйте pprint из `src.utils.pprint`
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

**Описание**: Функция `dump_category_products_files` сохраняет данные о товарах в JSON-файлы.

**Как работает функция**:
1. Проверяет, есть ли товары для сохранения. Если нет, выводит предупреждение и завершает работу.
2. Формирует путь к директории категории.
3. Для каждого товара в списке:
   - Извлекает `product_id`.
   - Если `product_id` отсутствует, выводит предупреждение и переходит к следующему товару.
   - Сохраняет данные товара в JSON-файл с именем `<product_id>.json` в директории категории.

**Параметры**:
- `category_name` (str): Имя категории.
- `products` (List[SimpleNamespace]): Список объектов `SimpleNamespace`, представляющих товары.

**Возвращает**:
- `None`

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

**Описание**: Метод `set_categories_from_directories` устанавливает категории рекламной кампании на основе названий директорий, находящихся в директории `category`.

**Как работает функция**:
1. Формирует путь к директории `category`.
2. Получает список названий директорий в директории `category`.
3. Проверяет, является ли атрибут `category` объекта `self.campaign` объектом `SimpleNamespace`. Если нет, создает его.
4. Для каждого названия директории создает объект `SimpleNamespace` с атрибутами `category_name`, `title` и `description` и добавляет его в атрибут `category` объекта `self.campaign`.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

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
    └───────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────┐
    │ 3. Save `product` as `<product_id>.json`.     │
    └───────────────────────────────┘
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

**Описание**: Функция `generate_output` сохраняет данные о продуктах в различных форматах, включая JSON-файлы для каждого продукта, общие файлы для AI, списки ссылок на продукты и файлы с названиями продуктов.

**Как работает функция**:
1. Форматирует текущую дату и время для использования в именах файлов.
2. Преобразует `products_list` в список, если это не список.
3. Инициализирует пустые списки `_data_for_openai`, `_promotion_links_list` и `_product_titles`.
4. Для каждого продукта в `products_list`:
   - Создает словарь `categories_convertor` для преобразования категорий.
   - Добавляет `categories_convertor` к продукту.
   - Сохраняет данные продукта в JSON-файл с именем `<product_id>.json`.
   - Добавляет название продукта и ссылку на продукт в соответствующие списки.
5. Вызывает `save_product_titles` для сохранения названий продуктов.
6. Вызывает `save_promotion_links` для сохранения ссылок на продукты.
7. Вызывает `generate_html` для генерации HTML-файла.

**Параметры**:
- `campaign_name` (str): Название кампании для выходных файлов.
- `category_path` (str | Path): Путь для сохранения выходных файлов.
- `products_list` (list[SimpleNamespace] | SimpleNamespace): Список продуктов или один продукт для сохранения.

**Возвращает**:
- `None`

**Примеры**:
```python
products_list: list[SimpleNamespace] = [
    SimpleNamespace(product_id="123", product_title="Product A", promotion_link="http://example.com/product_a", 
                    first_level_category_id=1, first_level_category_name="Category1",
                    second_level_category_id=2, second_level_category_name="Subcategory1", 
                    product_main_image_url="http://example.com/image.png", product_video_url="http://example.com/video.mp4"),
    SimpleNamespace(product_id="124", product_title="Product B", promotion_link="http://example.com/product_b",
                    first_level_category_id=1, first_level_category_name="Category1",
                    second_level_category_id=3, second_level_category_name="Subcategory2",
                    product_main_image_url="http://example.com/image2.png", product_video_url="http://example.com/video2.mp4")
]
category_path: Path = Path("/path/to/category")
await generate_output("CampaignName", category_path, products_list)
```

### `generate_html`

```python
async def generate_html(self, campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
    """ Creates an HTML file for the category and a root index file.
    
    @param products_list: List of products to include in the HTML.
    @param category_path: Path to save the HTML file.
    """
```

**Описание**: Метод `generate_html` создает HTML-файл для категории и корневой индексный файл.

**Как работает функция**:
1.  Проверяет, является ли `products_list` списком, и если нет, преобразует его в список.
2.  Определяет название категории из пути `category_path`.
3.  Формирует путь к HTML-файлу категории.
4.  Инициализирует словарь `category` для хранения названий продуктов.
5.  Формирует HTML-контент, добавляя информацию о каждом продукте из `products_list`.
6.  Сохраняет HTML-контент в файл категории.
7.  Формирует путь к корневому каталогу кампании.
8.  Создает директорию кампании, если она не существует.
9.  Формирует путь к файлу `index.html`.
10. Собирает ссылки на все категории.
11. Формирует HTML-контент для `index.html`, добавляя ссылки на категории.
12. Сохраняет HTML-контент в файл `index.html`.

**Параметры**:
-   `products_list` (list[SimpleNamespace] | SimpleNamespace): Список продуктов для включения в HTML.
-   `category_path` (str | Path): Путь для сохранения HTML-файла.

**Возвращает**:
-   Нет возвращаемого значения.

**Примеры**:
```python
await generate_html(campaign_name="SummerSale", category_path="/path/to/category", products_list=products)
```

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

**Описание**: Функция `generate_html_for_campaign` генерирует HTML-страницы для рекламной кампании.

**Как работает функция**:
1. Формирует путь к корневой директории кампании.
2. Получает