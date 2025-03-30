# Модуль ali_campaign_editor

## Обзор

Модуль `ali_campaign_editor.py` предоставляет класс `AliCampaignEditor`, который используется для редактирования рекламных кампаний AliExpress. Он позволяет добавлять, удалять, обновлять товары, а также управлять категориями и другими параметрами кампании.

## Подробней

`AliCampaignEditor` предназначен для упрощения процесса управления рекламными кампаниями на AliExpress. Он предоставляет методы для выполнения основных операций, таких как добавление и удаление товаров, обновление информации о кампании и категориях, а также получение списка категорий и товаров. Класс использует другие модули проекта, такие как `AliPromoCampaign`, `AliCampaignGoogleSheet` и утилиты для работы с файлами и JSON. Расположен в структуре проекта по пути `/src/suppliers/aliexpress/campaign/`.

## Классы

### `AliCampaignEditor`

**Описание**: Редактор для рекламных кампаний.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliCampaignEditor`.
- `delete_product`: Удаляет продукт, у которого нет партнерской ссылки.
- `update_product`: Обновляет детали продукта в категории.
- `update_campaign`: Обновляет свойства кампании, такие как описание и теги.
- `update_category`: Обновляет категорию в JSON-файле.
- `get_category`: Возвращает объект `SimpleNamespace` для заданного имени категории.
- `list_categories`: Возвращает список категорий в текущей кампании.
- `get_category_products`: Чтение данных о товарах из JSON файлов для конкретной категории.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (Optional[str | dict], optional): Язык кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта для кампании. По умолчанию `None`.

**Примеры**:
```python
# 1. по параметрам кампании
>>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
# 2. загрузка из файла
>>> editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
```

## Функции

### `__init__`

```python
def __init__(
    self,
    campaign_name: str,
    language: Optional[str | dict] = None,
    currency: Optional[str] = None,
):
    """
    Args:
        campaign_name (Optional[str]): The name of the campaign. Defaults to `None`.
        language (Optional[str | dict]): The language of the campaign. Defaults to 'EN'.
        currency (Optional[str]): The currency for the campaign. Defaults to 'USD'.
        campaign_file (Optional[str | Path]): Optionally load a `<lang>_<currency>.json` file from the campaign root folder. Defaults to `None`.

    Raises:
        CriticalError: If neither `campaign_name` nor `campaign_file` is provided.
    
    Example:
    # 1. by campaign parameters
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
    # 2. load fom file
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `AliCampaignEditor` с заданными параметрами.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (Optional[str | dict], optional): Язык кампании. По умолчанию `'EN'`.
- `currency` (Optional[str], optional): Валюта для кампании. По умолчанию `'USD'`.

**Вызывает исключения**:
- `CriticalError`: Если не указано ни `campaign_name`, ни `campaign_file`.

**Примеры**:
```python
# 1. По параметрам кампании
>>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
# 2. Загрузка из файла
>>> editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
```

### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """
    Args:
        product_id (str): The ID of the product to be deleted.
        exc_info (bool): Whether to include exception information in logs. Defaults to `False`.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.delete_product("12345")
    """
    ...
```

**Описание**: Удаляет продукт, у которого нет партнерской ссылки.

**Параметры**:
- `product_id` (str): ID продукта, который нужно удалить.
- `exc_info` (bool, optional): Следует ли включать информацию об исключении в логи. По умолчанию `False`.

**Примеры**:
```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> editor.delete_product("12345")
```

### `update_product`

```python
def update_product(self, category_name: str, lang: str, product: dict):
    """
    Args:
        category_name (str): The name of the category where the product should be updated.
        lang (str): The language of the campaign.
        product (dict): A dictionary containing product details.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
    """
    ...
```

**Описание**: Обновляет детали продукта в категории.

**Параметры**:
- `category_name` (str): Название категории, в которой нужно обновить продукт.
- `lang` (str): Язык кампании.
- `product` (dict): Словарь, содержащий детали продукта.

**Примеры**:
```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
```

### `update_campaign`

```python
def update_campaign(self):
    """
    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.update_campaign()
    """
    ...
```

**Описание**: Обновляет свойства кампании, такие как `description`, `tags` и т.д.

**Примеры**:
```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> editor.update_campaign()
```

### `update_category`

```python
def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
    """
    Args:
        json_path (Path): Path to the JSON file.
        category (SimpleNamespace): Category object to be updated.

    Returns:
        bool: True if update is successful, False otherwise.

    Example:
        >>> category = SimpleNamespace(name="New Category", description="Updated description")
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> result = editor.update_category(Path("category.json"), category)
        >>> print(result)  # True if successful
    """
    ...
```

**Описание**: Обновляет категорию в JSON-файле.

**Параметры**:
- `json_path` (Path): Путь к JSON-файлу.
- `category` (SimpleNamespace): Объект категории для обновления.

**Возвращает**:
- `bool`: `True`, если обновление успешно, `False` в противном случае.

**Примеры**:
```python
>>> category = SimpleNamespace(name="New Category", description="Updated description")
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> result = editor.update_category(Path("category.json"), category)
>>> print(result)  # True, если успешно
```

### `get_category`

```python
def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
    """
    Args:
        category_name (str): The name of the category to retrieve.

    Returns:
        Optional[SimpleNamespace]: SimpleNamespace object representing the category or `None` if not found.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> category = editor.get_category("Electronics")
        >>> print(category)  # SimpleNamespace or None
    """
    ...
```

**Описание**: Возвращает объект `SimpleNamespace` для заданного имени категории.

**Параметры**:
- `category_name` (str): Имя категории для получения.

**Возвращает**:
- `Optional[SimpleNamespace]`: Объект `SimpleNamespace`, представляющий категорию, или `None`, если категория не найдена.

**Примеры**:
```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> category = editor.get_category("Electronics")
>>> print(category)  # SimpleNamespace или None
```

### `list_categories`

```python
@property
def list_categories(self) -> Optional[List[str]]:
    """
    Returns:
        Optional[List[str]]: A list of category names, or None if no categories are found.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> categories = editor.categories_list
        >>> print(categories)  # ['Electronics', 'Fashion', 'Home']
    """
    try:
        # Ensure campaign has a category attribute and it is a SimpleNamespace
        if hasattr(self.campaign, 'category') and isinstance(self.campaign.category, SimpleNamespace):
            return list(vars(self.campaign.category).keys())
        else:
            logger.warning("No categories found in the campaign.")
            return
    except Exception as ex:
        logger.error(f"Error retrieving categories list: {ex}")
        return
```

**Описание**: Возвращает список категорий в текущей кампании.

**Возвращает**:
- `Optional[List[str]]`: Список названий категорий или `None`, если категории не найдены.

**Примеры**:
```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> categories = editor.categories_list
>>> print(categories)  # ['Electronics', 'Fashion', 'Home']
```

### `get_category_products`

```python
async def get_category_products(
    self, category_name: str
) -> Optional[List[SimpleNamespace]]:
    """Чтение данных о товарах из JSON файлов для конкретной категории.

    Args:
        category_name (str): Имя категории.

    Returns:
        Optional[List[SimpleNamespace]]: Список объектов SimpleNamespace, представляющих товары.

    Example:
        >>> products = campaign.get_category_products("Electronics")
        >>> print(len(products))
        15
    """
    category_path = (
        self.base_path
        / "category"
        / category_name
        / f"{self.language}_{self.currency}"
    )
    json_filenames = await get_filenames_from_directory (category_path, extensions="json")
    products = []

    if json_filenames:
        for json_filename in json_filenames:
            product_data = j_loads_ns(category_path / json_filename)
            product = SimpleNamespace(**vars(product_data))
            products.append(product)
        return products
    else:
        logger.error(
            f"No JSON files found for {category_name=} at {category_path=}.\nStart prepare category"
        )
        self.process_category_products(category_name)
        return 
```

**Описание**: Чтение данных о товарах из JSON файлов для конкретной категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращает**:
- `Optional[List[SimpleNamespace]]`: Список объектов SimpleNamespace, представляющих товары.

**Примеры**:
```python
>>> products = campaign.get_category_products("Electronics")
>>> print(len(products))
15