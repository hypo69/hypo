# Модуль `ali_promo_campaign`

## Обзор

Модуль предназначен для управления рекламными кампаниями на платформе AliExpress, включая обработку данных о категориях и товарах, создание и редактирование JSON-файлов с информацией о кампаниях, а также использование AI для генерации данных о кампаниях.

## Содержание

- [Обзор](#обзор)
- [Классы](#классы)
    - [`AliPromoCampaign`](#alipromocampaign)
        - [`__init__`](#__init__)
        - [`_models_payload`](#_models_payload)
        - [`process_campaign`](#process_campaign)
        - [`process_campaign_category`](#process_campaign_category)
        - [`process_new_campaign`](#process_new_campaign)
        - [`process_ai_category`](#process_ai_category)
        - [`process_category_products`](#process_category_products)
        - [`dump_category_products_files`](#dump_category_products_files)
        - [`set_categories_from_directories`](#set_categories_from_directories)
        - [`generate_output`](#generate_output)
        - [`generate_html`](#generate_html)
        - [`generate_html_for_campaign`](#generate_html_for_campaign)
- [Примеры](#примеры)

## Классы

### `AliPromoCampaign`

**Описание**: Класс `AliPromoCampaign` позволяет загружать и обрабатывать данные рекламных кампаний, управлять категориями и товарами, а также использовать ИИ для генерации описаний и других данных. Модуль поддерживает различные языки и валюты, обеспечивая гибкость в настройке кампаний.

#### `__init__`

```python
def __init__(self, campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None, model:str = 'openai') -> None:
    """
    Args:
        campaign_name (str): Название кампании.
        language (Optional[str], optional): Язык, используемый в кампании. По умолчанию `None`.
        currency (Optional[str], optional): Валюта, используемая в кампании. По умолчанию `None`.
        model (str, optional): Модель ИИ, используемая в кампании. По умолчанию `'openai'`.

    Returns:
        None

    Example:
        >>> campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
        >>> print(campaign.campaign_name)
    """
```

**Описание**: Инициализация объекта `AliPromoCampaign` для рекламной кампании.

#### `_models_payload`

```python
def _models_payload(self) -> None:
    """
    Args:
        None

    Returns:
        None
    """
```

**Описание**: Инициализация моделей ИИ для работы с рекламной кампанией.

#### `process_campaign`

```python
def process_campaign(self) -> None:
    """
    Args:
        None

    Returns:
        None

    Example:
        >>> campaign.process_campaign()
    """
```

**Описание**: Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

#### `process_campaign_category`

```python
def process_campaign_category(self, category_name: str) -> list[SimpleNamespace] | None:
    """
    Args:
        category_name (str): Название категории для обработки.

    Returns:
        list[SimpleNamespace] | None: Список объектов SimpleNamespace с товарами категории или None.
    """
```

**Описание**: Обрабатывает определенную категорию в рамках кампании для всех языков и валют.

#### `process_new_campaign`

```python
def process_new_campaign(self, campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """
    Args:
        campaign_name (str): Название рекламной кампании.
        language (Optional[str], optional): Язык для кампании. По умолчанию `None`.
        currency (Optional[str], optional): Валюта для кампании. По умолчанию `None`.

    Returns:
        None

    Example:
        >>> campaign.process_new_campaign(campaign_name="HolidaySale", language="RU", currency="ILS")
    """
```

**Описание**: Создание новой рекламной кампании.

#### `process_ai_category`

```python
def process_ai_category(self, category_name: Optional[str] = None) -> None:
    """
    Args:
        category_name (Optional[str], optional): Название категории для обработки. Если не указано, обрабатываются все категории. По умолчанию `None`.

    Returns:
        None

    Example:
        >>> campaign.process_ai_category("Electronics")
        >>> campaign.process_ai_category()
    """
```

**Описание**: Обрабатывает AI-данные для указанной категории или для всех категорий кампании.

#### `process_category_products`

```python
def process_category_products(self, category_name: str) -> Optional[List[SimpleNamespace]]:
    """
    Args:
        category_name (str): Название категории.

    Returns:
        Optional[List[SimpleNamespace]]: Список объектов `SimpleNamespace`, представляющих товары или `None`.

    Example:
        >>> products: List[SimpleNamespace] = campaign.process_category_products("Electronics")
        >>> print(len(products))
        20
        >>> for product in products:
        >>>     pprint(product)  # Use pprint from `src.utils.pprint`
    """
```

**Описание**: Обрабатывает товары в указанной категории.

#### `dump_category_products_files`

```python
def dump_category_products_files(self, category_name: str, products: List[SimpleNamespace]) -> None:
    """
    Args:
        category_name (str): Имя категории.
        products (List[SimpleNamespace]): Список объектов SimpleNamespace, представляющих товары.

    Returns:
        None

    Example:
        >>> campaign.dump_category_products_files("Electronics", products)
    """
```

**Описание**: Сохранение данных о товарах в JSON файлы.

#### `set_categories_from_directories`

```python
def set_categories_from_directories(self) -> None:
    """
    Args:
         None

    Returns:
        None

    Example:
        >>> self.set_categories_from_directories()
        >>> print(self.campaign.category.category1.category_name)
    """
```

**Описание**: Устанавливает категории рекламной кампании из названий директорий в `category`.

#### `generate_output`

```python
async def generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace) -> None:
    """
    Args:
        campaign_name (str): Название кампании для выходных файлов.
        category_path (str | Path): Путь для сохранения выходных файлов.
        products_list (list[SimpleNamespace] | SimpleNamespace): Список товаров или один товар для сохранения.

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
    """
```

**Описание**: Сохраняет данные о товарах в различных форматах.

#### `generate_html`

```python
async def generate_html(self, campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace) -> None:
    """
    Args:
        campaign_name (str): Название рекламной кампании.
        category_path (str | Path): Путь к категории для сохранения HTML-файла.
        products_list (list[SimpleNamespace] | SimpleNamespace): Список товаров для включения в HTML.

    Returns:
         None
    """
```

**Описание**: Создает HTML-файлы для категории и корневой индексный файл.

#### `generate_html_for_campaign`

```python
def generate_html_for_campaign(self, campaign_name: str) -> None:
    """
    Args:
        campaign_name (str): Имя рекламной кампании.

    Returns:
        None

    Example:
        >>> campaign.generate_html_for_campaign("HolidaySale")
    """
```

**Описание**: Генерирует HTML-страницы для рекламной кампании.

## Примеры

Пример инициализации рекламной кампании:

```python
>>> campaign = AliPromoCampaign("new_campaign", "EN", "USD")
>>> print(campaign.campaign_name)
```

Пример обработки всей кампании:

```python
>>> campaign = AliPromoCampaign("new_campaign", "EN", "USD")
>>> campaign.process_campaign()
```

Пример обработки данных о товарах в категории:

```python
>>> campaign = AliPromoCampaign("new_campaign", "EN", "USD")
>>> products = campaign.process_category_products("electronics")
```

Пример заполнения данных категорий с использованием AI:

```python
>>> campaign = AliPromoCampaign("new_campaign", "EN", "USD")
>>> campaign.process_ai_category("Electronics")
```