# Модуль `ali_campaign_editor.py`

## Обзор

Модуль `ali_campaign_editor.py` предоставляет класс `AliCampaignEditor`, который используется для редактирования рекламных кампаний AliExpress. Он позволяет создавать, изменять и удалять продукты, обновлять информацию о кампаниях и категориях, а также управлять данными о товарах в формате JSON. Модуль включает в себя функциональность для работы с файлами, чтения и записи JSON данных, а также интеграцию с Google Sheets через класс `AliCampaignGoogleSheet`.

## Подробней

`AliCampaignEditor` является расширением класса `AliPromoCampaign` и предоставляет дополнительные методы для редактирования кампаний. Этот модуль важен для автоматизации управления рекламными кампаниями на AliExpress, позволяя программно обновлять и поддерживать актуальность данных.

## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предназначен для редактирования рекламных кампаний AliExpress. Он наследует функциональность от `AliPromoCampaign` и добавляет методы для управления продуктами, категориями и общими параметрами кампании.

**Как работает класс**:
- Инициализация класса (`__init__`) позволяет создать объект редактора кампании, указав имя кампании, язык и валюту. Можно также загрузить параметры кампании из JSON-файла.
- Методы класса позволяют выполнять операции по добавлению, удалению и обновлению продуктов, а также изменять параметры кампании и категорий.
- Класс использует другие модули, такие как `AliPromoCampaign`, `AliCampaignGoogleSheet`, `j_loads_ns`, `j_loads`, `j_dumps` и другие утилиты для работы с файлами и данными.

**Методы**:
- `__init__`: Инициализация класса `AliCampaignEditor`.
- `delete_product`: Удаление продукта, у которого нет партнерской ссылки.
- `update_product`: Обновление деталей продукта в рамках категории.
- `update_campaign`: Обновление свойств кампании, таких как описание и теги.
- `update_category`: Обновление категории в JSON-файле.
- `get_category`: Получение объекта `SimpleNamespace` для указанной категории.
- `list_categories`: Получение списка категорий в текущей кампании.
- `get_category_products`: Чтение данных о товарах из JSON файлов для конкретной категории.

#### `__init__`

```python
def __init__(self, 
             campaign_name: str, 
             language: Optional[str | dict] = None, 
             currency: Optional[str] = None) -> None:
    """ Initialize the AliCampaignEditor with the given parameters.
    

    Args:
        campaign_name (str): The name of the campaign.
        language (Optional[str | dict], optional): The language of the campaign. Defaults to 'EN'.
        currency (Optional[str], optional): The currency for the campaign. Defaults to 'USD'.
        campaign_file (Optional[str | Path], optional): Optionally load a `<lang>_<currency>.json` file from the campaign root folder. Defaults to `None`.

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

**Описание**: Инициализирует класс `AliCampaignEditor` с заданными параметрами.

**Как работает функция**:
- Принимает имя кампании, язык и валюту в качестве параметров.
- Вызывает конструктор родительского класса `AliPromoCampaign` для инициализации основных параметров кампании.
- Может загружать параметры кампании из JSON-файла, если указан `campaign_file`.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (Optional[str | dict], optional): Язык кампании. По умолчанию 'EN'.
- `currency` (Optional[str], optional): Валюта кампании. По умолчанию 'USD'.
- `campaign_file` (Optional[str | Path], optional): Путь к файлу конфигурации кампании. По умолчанию `None`.

**Вызывает исключения**:
- `CriticalError`: Если не указано имя кампании и не предоставлен файл конфигурации.

**Примеры**:
```python
# 1. Инициализация с параметрами кампании
editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
# 2. Загрузка из файла
editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
```

#### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False) -> None:
    """ Delete a product that does not have an affiliate link.
    

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

**Как работает функция**:
- Извлекает ID продукта с помощью функции `extract_prod_ids`.
- Проверяет наличие файла `sources.txt` в каталоге категории.
- Если файл существует, читает список продуктов из файла и удаляет запись, соответствующую указанному `product_id`.
- Если файл не существует, пытается переименовать HTML-файл продукта, добавляя символ подчеркивания (`_`) в конце имени.

**Параметры**:
- `product_id` (str): ID продукта, который нужно удалить.
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении в логи. По умолчанию `False`.

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.delete_product("12345")
```

#### `update_product`

```python
def update_product(self, category_name: str, lang: str, product: dict) -> None:
    """ Update product details within a category.

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

**Описание**: Обновляет детали продукта в рамках указанной категории.

**Как работает функция**:
- Вызывает метод `dump_category_products_files` для обновления информации о продукте в файлах категории.

**Параметры**:
- `category_name` (str): Имя категории, в которой нужно обновить продукт.
- `lang` (str): Язык кампании.
- `product` (dict): Словарь, содержащий детали продукта.

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
```

#### `update_campaign`

```python
def update_campaign(self) -> None:
    """ Update campaign properties such as `description`, `tags`, etc.
    
    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.update_campaign()
    """
    ...
```

**Описание**: Обновляет свойства кампании, такие как описание и теги.

**Как работает функция**:
- <описание работы функции>

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_campaign()
```

#### `update_category`

```python
def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
    """ Update the category in the JSON file.

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

**Как работает функция**:
- Читает JSON данные из файла, указанного в `json_path`, используя `j_loads`.
- Преобразует объект `SimpleNamespace` категории в словарь и обновляет данные категории в JSON.
- Записывает обновленные JSON данные обратно в файл с помощью `j_dumps`.
- Возвращает `True`, если обновление прошло успешно, и `False` в противном случае.

**Параметры**:
- `json_path` (Path): Путь к JSON-файлу.
- `category` (SimpleNamespace): Объект категории, который нужно обновить.

**Возвращает**:
- `bool`: `True`, если обновление успешно, `False` в противном случае.

**Примеры**:
```python
category = SimpleNamespace(name="New Category", description="Updated description")
editor = AliCampaignEditor(campaign_name="Summer Sale")
result = editor.update_category(Path("category.json"), category)
print(result)  # True if successful
```

#### `get_category`

```python
def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
    """ Returns the SimpleNamespace object for a given category name.

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

**Описание**: Возвращает объект `SimpleNamespace` для указанного имени категории.

**Как работает функция**:
- Проверяет, существует ли атрибут категории с указанным именем в объекте кампании.
- Если категория найдена, возвращает соответствующий объект `SimpleNamespace`.
- Если категория не найдена, записывает предупреждение в лог и возвращает `None`.

**Параметры**:
- `category_name` (str): Имя категории, которую нужно получить.

**Возвращает**:
- `Optional[SimpleNamespace]`: Объект `SimpleNamespace`, представляющий категорию, или `None`, если категория не найдена.

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
category = editor.get_category("Electronics")
print(category)  # SimpleNamespace or None
```

#### `list_categories`

```python
@property
def list_categories(self) -> Optional[List[str]]:
    """ Retrieve a list of categories in the current campaign.

    Returns:
        Optional[List[str]]: A list of category names, or None if no categories are found.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> categories = editor.categories_list
        >>> print(categories)  # ['Electronics', 'Fashion', 'Home']
    """
    ...
```

**Описание**: Получает список категорий в текущей кампании.

**Как работает функция**:
- Проверяет, есть ли у кампании атрибут `category` и является ли он экземпляром `SimpleNamespace`.
- Если категории найдены, возвращает список имен категорий.
- Если категории не найдены, записывает предупреждение в лог и возвращает `None`.

**Возвращает**:
- `Optional[List[str]]`: Список имен категорий или `None`, если категории не найдены.

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
categories = editor.categories_list
print(categories)  # ['Electronics', 'Fashion', 'Home']
```

#### `get_category_products`

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

**Как работает функция**:
- Формирует путь к директории категории на основе базового пути, имени категории, языка и валюты.
- Получает список JSON файлов в директории категории.
- Если JSON файлы найдены, читает данные из каждого файла, преобразует их в объекты `SimpleNamespace` и добавляет в список товаров.
- Если JSON файлы не найдены, записывает ошибку в лог и запускает процесс подготовки товаров для категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращает**:
- `Optional[List[SimpleNamespace]]`: Список объектов `SimpleNamespace`, представляющих товары.

**Примеры**:
```python
products = campaign.get_category_products("Electronics")
print(len(products))
15
```

## Функции

В данном модуле не представлены отдельные функции, не относящиеся к классам.