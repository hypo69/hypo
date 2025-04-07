# Модуль `ali_promo_campaign.py`

## Обзор

Модуль `ali_promo_campaign.py` предназначен для управления рекламными кампаниями на платформе AliExpress. Он включает в себя обработку данных о категориях и товарах, создание и редактирование JSON-файлов с информацией о кампаниях, а также использование AI для генерации данных о кампаниях.

## Подробней

Этот модуль предоставляет класс `AliPromoCampaign`, который позволяет загружать и обрабатывать данные рекламных кампаний, управлять категориями и товарами, а также использовать ИИ для генерации описаний и других данных. Поддерживаются различные языки и валюты, что обеспечивает гибкость в настройке кампаний.

## Классы

### `AliPromoCampaign`

**Описание**: Класс для управления рекламными кампаниями AliExpress.

**Принцип работы**:

Класс `AliPromoCampaign` предназначен для обработки и управления рекламными кампаниями на AliExpress. Он инициализируется с названием кампании, языком и валютой. При инициализации класс проверяет наличие файла кампании и, если файл отсутствует, запускает процесс создания новой кампании. Класс использует AI модели (Google Gemini и OpenAI) для генерации контента для категорий и товаров.

**Аттрибуты**:

- `language` (str): Язык, используемый в кампании.
- `currency` (str): Валюта, используемая в кампании.
- `base_path` (Path): Базовый путь к файлам кампании.
- `campaign_name` (str): Название кампании.
- `campaign` (SimpleNamespace): Объект, представляющий данные кампании.
- `campaign_ai` (SimpleNamespace): Объект, представляющий данные кампании, сгенерированные ИИ.
- `gemini` (GoogleGenerativeAI): Объект для взаимодействия с моделью Google Gemini.
- `openai` (OpenAIModel): Объект для взаимодействия с моделью OpenAI.

**Методы**:

- `__init__`: Инициализация объекта AliPromoCampaign.
- `_models_payload`: Инициализация моделей AI.
- `process_campaign`: Итерируется по категориям кампании и обрабатывает товары.
- `process_campaign_category`: Обрабатывает определенную категорию кампании для всех языков и валют.
- `process_new_campaign`: Создает новую рекламную кампанию.
- `process_ai_category`: Обрабатывает AI-генерацию данных для категории.
- `process_category_products`: Обрабатывает товары в указанной категории.
- `dump_category_products_files`: Сохраняет данные о товарах в JSON-файлы.
- `set_categories_from_directories`: Устанавливает категории кампании на основе директорий.
- `generate_output`: Сохраняет данные о товарах в различных форматах.
- `generate_html`: Создает HTML-файлы для категорий.
- `generate_html_for_campaign`: Генерирует HTML-страницы для кампании.

## Функции

### `__init__`

```python
def __init__(
    self,
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
    model:str = 'openai'
) -> None:
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

**Назначение**: Инициализация экземпляра класса `AliPromoCampaign`.

**Параметры**:

- `campaign_name` (str): Название кампании.
- `language` (Optional[str]): Язык кампании. По умолчанию `None`.
- `currency` (Optional[str]): Валюта кампании. По умолчанию `None`.
- `model` (str): Используемая модель AI. По умолчанию `'openai'`.

**Как работает функция**:

1.  Устанавливает базовый путь к файлам кампании.
2.  Пытается загрузить файл кампании JSON. Если файл не найден, запускается процесс создания новой рекламной кампании с использованием `process_new_campaign`.
3.  Если файл кампании найден, устанавливает язык и валюту кампании.
4.  Вызывает метод `_models_payload` для инициализации AI моделей.

### `_models_payload`

```python
def _models_payload(self) -> None:
    """ """
    ...
```

**Назначение**: Инициализация AI-моделей для генерации контента кампании.

**Как работает функция**:

1.  Определяет путь к файлу с системными инструкциями для AI.
2.  Считывает системные инструкции из файла.
3.  Инициализирует `GoogleGenerativeAI` с системными инструкциями.

### `process_campaign`

```python
def process_campaign(self) -> None:
    """Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

    Example:
        >>> campaign.process_campaign()
    """
    ...
```

**Назначение**: Обработка рекламной кампании путем итерации по категориям и обработки товаров.

**Как работает функция**:

1.  Получает список названий категорий из директории `category`.
2.  Итерируется по названиям категорий.
3.  Для каждой категории вызывает методы `process_category_products` и `process_ai_category`.

```ascii
    Начало
    │
    Получение списка названий категорий
    │
    Для каждой категории:
    │   Обработка товаров категории
    │   Обработка AI-генерации данных для категории
    │
    Конец
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
    ...
```

**Назначение**: Обрабатывает определенную категорию в рамках кампании для всех языков и валют.

**Параметры**:

- `category_name` (str): Название категории.

**Как работает функция**:

1.  Вызывает `self.process_category_products` для обработки товаров в категории.
2.  Вызывает `self.process_ai_category` для AI-генерации данных в категории.

### `process_new_campaign`

```python
def process_new_campaign(
    self,
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
) -> None:
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

**Назначение**: Создает новую рекламную кампанию, если не найден файл кампании.

**Параметры**:

-   `campaign_name` (str): Название кампании.
-   `language` (Optional[str]): Язык кампании. По умолчанию `None`.
-   `currency` (Optional[str]): Валюта кампании. По умолчанию `None`.

**Как работает функция**:

1.  Определяет языковые и валютные параметры, если они не предоставлены.
2.  Для каждой комбинации языка и валюты инициализирует объект `self.campaign`.
3.  Вызывает `self.set_categories_from_directories()` для установки категорий кампании.
4.  Создает копию `self.campaign` в `self.campaign_ai` и устанавливает имя файла для AI-кампании.
5.  Для каждой категории вызывает методы `self.process_category_products()` и `self.process_ai_category()`.
6.  Сохраняет данные кампании в JSON файл.

### `process_ai_category`

```python
def process_ai_category(self, category_name: Optional[str] = None) -> None:
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

**Назначение**: Обрабатывает AI-генерацию данных для указанной категории или всех категорий.

**Параметры**:

-   `category_name` (Optional[str]): Название категории для обработки. Если не указано, обрабатываются все категории.

**Как работает функция**:

1.  Создает копию `self.campaign` в `campaign_ai`.

2.  Определяет внутреннюю функцию `_process_category` для обработки данных категории:

    *   Считывает заголовки продуктов из файла `product_titles.txt`.
    *   Формирует запрос для AI-модели.
    *   Получает ответ от AI-модели с помощью внутренней функции `get_response`.
    *   Преобразует ответ в объект `SimpleNamespace`.
    *   Обновляет или создает категорию в `campaign_ai.category` на основе ответа.

3.  Итерируется по категориям в `campaign_ai.category` и вызывает `_process_category` для каждой категории.
4.  Сохраняет обновленные данные кампании в JSON-файл.

**Внутренние функции**:

#### `_process_category`

```python
def _process_category(category_name: str) -> None:
    """Processes AI-generated category data and updates the campaign category."""
    ...
```

**Назначение**: Обрабатывает AI-сгенерированные данные категории и обновляет категорию кампании.

**Параметры**:

-   `category_name` (str): Название категории для обработки.

**Как работает функция**:

1.  Определяет путь к файлу `product_titles.txt`, содержащему заголовки продуктов.
2.  Считывает заголовки продуктов из файла.
3.  Формирует запрос (`prompt`) для AI-модели, включающий язык, название категории и заголовки продуктов.
4.  Проверяет, инициализированы ли модели `self.gemini` или `self.openai`, и при необходимости вызывает `self._models_payload()`.
5.  Вызывает внутреннюю функцию `get_response` для получения ответа от AI-модели.
6.  Преобразует полученный ответ в объект `SimpleNamespace` (res_ns).
7.  Обновляет или создает атрибуты категории в `campaign_ai.category` на основе данных из `res_ns`.
8.  Логирует информацию об обновлении или создании категории.
9.  Обрабатывает возможные исключения и логирует ошибки.

#### `get_response`

```python
def get_response(_attempts: int = 5) -> None:
    """Gets the response from the AI model."""
    ...
```

**Назначение**: Получает ответ от AI-модели.

**Параметры**:

-   `_attempts` (int): Количество попыток получения ответа от AI-модели. По умолчанию равно 5.

**Как работает функция**:

1.  Формирует запрос (`prompt`), включающий язык, название категории и заголовки продуктов.
2.  Вызывает `self.gemini.ask(prompt)` для получения ответа от AI-модели Gemini.
3.  Возвращает полученный ответ.

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
    ...
```

**Назначение**: Обрабатывает продукты в указанной категории.

**Параметры**:

-   `category_name` (str): Название категории.

**Возвращает**:

-   `Optional[List[SimpleNamespace]]`: Список объектов `SimpleNamespace`, представляющих продукты. Возвращает `None`, если продукты не найдены.

**Как работает функция**:

1.  Определяет внутреннюю функцию `read_sources` для считывания идентификаторов продуктов.
2.  Вызывает `read_sources` для получения списка идентификаторов продуктов.
3.  Если список идентификаторов продуктов пуст, логирует ошибку и возвращает `None`.
4.  Инициализирует `AliAffiliatedProducts` с языком и валютой.
5.  Вызывает `process_affiliate_products` для обработки аффилированных продуктов.
6.  Возвращает список аффилированных продуктов.

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
    ...
```

**Назначение**: Считывает источники продуктов и извлекает идентификаторы продуктов.

**Параметры**:

-   `category_name` (str): Название категории.

**Возвращает**:

-   `Optional[List[str]]`: Список идентификаторов продуктов, если найдены; в противном случае `None`.

**Как работает функция**:

1.  Инициализирует пустой список `product_ids`.
2.  Ищет HTML-файлы в директории `sources` категории и извлекает идентификаторы продуктов из них.
3.  Считывает URL-адреса продуктов из файла `sources.txt` и извлекает идентификаторы продуктов из них.
4.  Если идентификаторы продуктов не найдены, возвращает `None`.
5.  Возвращает список идентификаторов продуктов.

### `dump_category_products_files`

```python
def dump_category_products_files(
    self, category_name: str, products: List[SimpleNamespace]
) -> None:
    """Сохранение данных о товарах в JSON файлы.

    Args:
        category_name (str): Имя категории.
        products (List[SimpleNamespace]): Список объектов SimpleNamespace, представляющих товары.

    Example:
        >>> campaign.dump_category_products_files("Electronics", products)
    """
    ...
```

**Назначение**: Сохраняет данные о товарах в JSON-файлы.

**Параметры**:

-   `category_name` (str): Имя категории.
-   `products` (List[SimpleNamespace]): Список объектов `SimpleNamespace`, представляющих товары.

**Как работает функция**:

1.  Проверяет, есть ли продукты для сохранения. Если нет, логирует предупреждение и завершает работу.
2.  Определяет путь к директории категории.
3.  Для каждого продукта в списке извлекает идентификатор продукта.
4.  Если идентификатор продукта отсутствует, логирует предупреждение и переходит к следующему продукту.
5.  Сохраняет данные продукта в JSON-файл с именем `<product_id>.json` в директории категории.

### `set_categories_from_directories`

```python
def set_categories_from_directories(self) -> None:
    """Устанавливает категории рекламной кампании из названий директорий в `category`.

    Преобразует каждый элемент списка категорий в объект `SimpleNamespace` с атрибутами
    `category_name`, `title`, и `description`.

    Example:
        >>> self.set_categories_from_directories()
        >>> print(self.campaign.category.category1.category_name)
    """
    ...
```

**Назначение**: Устанавливает категории рекламной кампании из названий директорий в `category`.

**Как работает функция**:

1.  Определяет путь к директориям категорий.
2.  Получает список названий директорий категорий.
3.  Проверяет, является ли `self.campaign.category` объектом `SimpleNamespace`. Если нет, создает его.
4.  Для каждого названия категории создает объект `SimpleNamespace` с атрибутами `category_name`, `title` и `description` и добавляет его в `self.campaign.category`.

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
    ...
```

**Назначение**: Сохраняет данные о товарах в различных форматах (JSON, TXT, HTML).

**Параметры**:

-   `campaign_name` (str): Название кампании для выходных файлов.
-   `category_path` (str | Path): Путь для сохранения выходных файлов.
-   `products_list` (list[SimpleNamespace] | SimpleNamespace): Список продуктов или отдельный продукт для сохранения.

**Как работает функция**:

1.  Форматирует текущую дату и время для использования в именах файлов.
2.  Преобразует `products_list` в список, если это не список.
3.  Инициализирует пустые списки и словарь для сбора данных.
4.  Для каждого продукта в `products_list`:
    *   Создает словарь `categories_convertor` для преобразования категорий.
    *   Добавляет `categories_convertor` в объект продукта.
    *   Сохраняет данные продукта в JSON-файл с именем `<product_id>.json`.
    *   Добавляет название продукта и ссылку на продвижение в соответствующие списки.
5.  Вызывает `save_product_titles` для сохранения названий продуктов.
6.  Вызывает `save_promotion_links` для сохранения ссылок на продвижение.
7.  Вызывает `generate_html` для генерации HTML-файла.

### `generate_html`

```python
async def generate_html(self, campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace) -> None:
    """ Creates an HTML file for the category and a root index file.

    @param products_list: List of products to include in the HTML.
    @param category_path: Path to save the HTML file.
    """
    ...
```

**Назначение**: Создает HTML-файл для категории и корневой индексный файл.

**Параметры**:

-   `campaign_name` (str): Название кампании.
-   `category_path` (str | Path): Путь для сохранения HTML-файла.
-   `products_list` (list[SimpleNamespace] | SimpleNamespace): Список продуктов для включения в HTML.

**Как работает функция**:

1.  Преобразует `products_list` в список, если это не список.
2.  Определяет имя категории из `category_path`.
3.  Инициализирует словарь `category` для хранения данных о продуктах.
4.  Создает HTML-контент, добавляя информацию о каждом продукте из `products_list`.
5.  Сохраняет HTML-контент в файл `<category_name>.html`.
6.  Генерирует корневой `index.html` файл, содержащий ссылки на все категории.

### `generate_html_for_campaign`

```python
def generate_html_for_campaign(self, campaign_name: str) -> None:
    """Генерирует HTML-страницы для рекламной кампании.

    Args:
        campaign_name (str): Имя рекламной кампании.

    Example:
        >>> campaign.generate_html_for_campaign("HolidaySale")
    """
    ...
```

**Назначение**: Генерирует HTML-страницы для рекламной кампании.

**Параметры**:

-   `campaign_name` (str): Имя рекламной кампании.

**Как работает функция**:

1.  Определяет корневой путь кампании.
2.  Получает список категорий.
3.  Для каждой категории:
    *   Определяет путь к категории.
    *   Получает список продуктов для категории.
    *   Если продукты найдены, генерирует HTML-страницы для каждого продукта и для категории.
    *   Если продукты не найдены, логирует предупреждение.
4.  Генерирует HTML-страницу для всей рекламной кампании.