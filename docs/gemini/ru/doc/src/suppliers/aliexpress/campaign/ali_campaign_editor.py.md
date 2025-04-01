# Модуль для редактирования рекламных кампаний AliCampaignEditor

## Обзор

Модуль `ali_campaign_editor.py` предоставляет класс `AliCampaignEditor`, который предназначен для редактирования рекламных кампаний на платформе AliExpress. Он позволяет выполнять такие операции, как удаление, обновление и получение информации о продуктах и категориях в рамках кампании.

## Подробней

Этот модуль является частью системы управления рекламными кампаниями AliExpress и предоставляет инструменты для работы с данными кампаний, хранящимися в различных форматах, включая JSON и текстовые файлы. Он использует другие модули проекта, такие как `ali_promo_campaign`, `gsheet` и утилиты для работы с файлами и данными.

## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предназначен для редактирования рекламных кампаний AliExpress. Он наследует функциональность от класса `AliPromoCampaign` и предоставляет методы для управления продуктами и категориями в рамках кампании.

**Принцип работы**:
Класс инициализируется с именем кампании, языком и валютой. Он использует эти параметры для определения местоположения файлов кампании и загрузки необходимых данных. Класс предоставляет методы для удаления продуктов, обновления информации о продуктах, обновления параметров кампании и управления категориями.

**Наследует**:
- `AliPromoCampaign`: Предоставляет базовую функциональность для работы с рекламными кампаниями AliExpress.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliCampaignEditor`.
- `delete_product`: Удаляет продукт из кампании.
- `update_product`: Обновляет информацию о продукте в кампании.
- `update_campaign`: Обновляет параметры кампании.
- `update_category`: Обновляет информацию о категории в JSON-файле.
- `get_category`: Возвращает объект `SimpleNamespace` для заданной категории.
- `list_categories`: Возвращает список категорий в текущей кампании.
- `get_category_products`: Читает данные о товарах из JSON-файлов для конкретной категории.

### `__init__`

```python
def __init__(self, 
             campaign_name: str, 
             language: Optional[str | dict] = None, 
             currency: Optional[str] = None):
    """ Initialize the AliCampaignEditor with the given parameters.
    
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
    super().__init__(campaign_name = campaign_name, language = language, currency = currency)
    #self.google_sheet = AliCampaignGoogleSheet(campaign_name = campaign_name, language = language, currency = currency, campaign_editor = self)
```

**Назначение**: Инициализирует объект `AliCampaignEditor` с указанными параметрами кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (Optional[str | dict]): Язык кампании (по умолчанию 'EN').
- `currency` (Optional[str]): Валюта кампании (по умолчанию 'USD').

**Возвращает**:
- None

**Как работает функция**:
1. Вызывается конструктор родительского класса `AliPromoCampaign` для инициализации базовых параметров кампании.
2. Инициализирует объект `AliCampaignGoogleSheet` для работы с Google Sheets (закомментировано в текущей версии кода).

**Примеры**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
```

### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Delete a product that does not have an affiliate link.
    
    Args:
        product_id (str): The ID of the product to be deleted.
        exc_info (bool): Whether to include exception information in logs. Defaults to `False`.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.delete_product("12345")
    """
    ...
    _product_id = extract_prod_ids(product_id)
    
    product_path = self.category_path / 'sources.txt'
    prepared_product_path = self.category_path / '_sources.txt'
    products_list = read_text_file(product_path)
    if products_list:
        for record in products_list:
            if _product_id:
                record_id = extract_prod_ids(record)
                if record_id == str(product_id):
                    products_list.remove(record)
                    save_text_file((products_list, '\n'), prepared_product_path)
                    break
            else:
                if record == str(product_id):
                    products_list.remove(record)
                    save_text_file((products_list, '\n'), product_path)
                
    else:
        product_path = self.category_path / 'sources' / f'{product_id}.html'    
        try:
            product_path.rename(self.category_path / 'sources' / f'{product_id}_.html')
            logger.success(f"Product file {product_path=} renamed successfully.")
        except FileNotFoundError as ex:
            logger.error(f"Product file {product_path=} not found.", exc_info=exc_info)
        except Exception as ex:
            logger.critical(f"An error occurred while deleting the product file {product_path}.", ex)
```

**Назначение**: Удаляет продукт, у которого нет партнерской ссылки, из списка продуктов в файле `sources.txt` или переименовывает HTML-файл продукта, если список продуктов не найден.

**Параметры**:
- `product_id` (str): Идентификатор продукта, который нужно удалить.
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении в логи (по умолчанию `False`).

**Возвращает**:
- None

**Как работает функция**:
1. Извлекает идентификатор продукта из переданного `product_id`.
2. Определяет пути к файлам `sources.txt` и `_sources.txt` в каталоге категории.
3. Пытается прочитать список продуктов из файла `sources.txt`.
4. Если список продуктов найден, перебирает записи в списке и удаляет соответствующую запись, если идентификатор продукта совпадает.
5. Если список продуктов не найден, пытается переименовать HTML-файл продукта, добавляя символ `_` в конец имени файла.
6. Логирует успешное переименование файла или ошибки, если файл не найден или произошла другая ошибка.

```
Удаление продукта
    Начало
    │
    ├───▶ Извлечение идентификатора продукта (_product_id)
    │
    ├───▶ Определение путей к файлам (product_path, prepared_product_path)
    │
    ├───▶ Чтение списка продуктов из файла sources.txt (products_list)
    │
    ├───▶ Проверка наличия списка продуктов
    │   └───▶ Список продуктов найден
    │       └───▶ Перебор записей в списке продуктов
    │           └───▶ Сравнение идентификаторов продуктов
    │               └───▶ Идентификаторы совпадают
    │                   └───▶ Удаление записи из списка
    │                   └───▶ Сохранение обновленного списка в файл _sources.txt
    │   └───▶ Список продуктов не найден
    │       └───▶ Определение пути к HTML-файлу продукта
    │           └───▶ Переименование HTML-файла продукта (добавление "_")
    │           └───▶ Логирование успешного переименования или ошибки
    │
    └───▶ Завершение
```

**Примеры**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.delete_product("12345")
```

### `update_product`

```python
def update_product(self, category_name: str, lang: str, product: dict):
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
    self.dump_category_products_files(category_name, lang, product)
```

**Назначение**: Обновляет детали продукта в указанной категории.

**Параметры**:
- `category_name` (str): Название категории, в которой нужно обновить продукт.
- `lang` (str): Язык кампании.
- `product` (dict): Словарь, содержащий детали продукта.

**Возвращает**:
- None

**Как работает функция**:
1. Вызывает метод `dump_category_products_files` для обновления информации о продукте в файлах категории.

**Примеры**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
```

### `update_campaign`

```python
def update_campaign(self):
    """ Update campaign properties such as `description`, `tags`, etc.
    
    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.update_campaign()
    """
    ...
```

**Назначение**: Обновляет свойства кампании, такие как описание, теги и т.д.

**Параметры**:
- None

**Возвращает**:
- None

**Как работает функция**:
1.  Функция <обновляет свойства кампании>. В данном коде функция не выполняет никаких действий. Предположительно, логика обновления кампании должна быть реализована в дальнейшем.

**Примеры**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_campaign()
```

### `update_category`

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
    try:
        data = j_loads(json_path)  # Read JSON data from file
        data['category'] = category.__dict__  # Convert SimpleNamespace to dict
        j_dumps(data, json_path)  # Write updated JSON data back to file
        return True
    except Exception as ex:
        logger.error(f"Failed to update category {json_path}: {ex}")
        return False
```

**Назначение**: Обновляет категорию в JSON-файле.

**Параметры**:
- `json_path` (Path): Путь к JSON-файлу.
- `category` (SimpleNamespace): Объект категории для обновления.

**Возвращает**:
- `bool`: `True`, если обновление прошло успешно, `False` в противном случае.

**Как работает функция**:
1. Пытается прочитать данные из JSON-файла, используя `j_loads`.
2. Преобразует объект `SimpleNamespace` категории в словарь и обновляет данные в прочитанном JSON.
3. Записывает обновленные данные обратно в JSON-файл, используя `j_dumps`.
4. Возвращает `True`, если обновление прошло успешно, и `False` в случае ошибки.
5. Логирует ошибки, если не удалось обновить категорию.

```
Обновление категории в JSON-файле
    Начало
    │
    ├───▶ Чтение данных из JSON-файла (data)
    │
    ├───▶ Преобразование объекта SimpleNamespace категории в словарь
    │
    ├───▶ Обновление данных категории в прочитанном JSON (data['category'])
    │
    ├───▶ Запись обновленных данных обратно в JSON-файл
    │
    ├───▶ Обработка исключений
    │   └───▶ Произошла ошибка
    │       └───▶ Логирование ошибки
    │       └───▶ Возврат False
    │   └───▶ Ошибок не произошло
    │       └───▶ Возврат True
    │
    └───▶ Завершение
```

**Примеры**:

```python
category = SimpleNamespace(name="New Category", description="Updated description")
editor = AliCampaignEditor(campaign_name="Summer Sale")
result = editor.update_category(Path("category.json"), category)
print(result)
```

### `get_category`

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
    try:
        if hasattr(self.campaign.category, category_name):
            return getattr(self.campaign.category, category_name)
        else:
            logger.warning(f"Category {category_name} not found in the campaign.")
            return
    except Exception as ex:
        logger.error(f"Error retrieving category {category_name}.", ex, exc_info=True)
        return
```

**Назначение**: Возвращает объект `SimpleNamespace` для указанного имени категории.

**Параметры**:
- `category_name` (str): Имя категории, которую нужно получить.

**Возвращает**:
- `Optional[SimpleNamespace]`: Объект `SimpleNamespace`, представляющий категорию, или `None`, если категория не найдена.

**Как работает функция**:
1. Пытается получить категорию из атрибута `category` объекта `self.campaign`.
2. Если категория найдена, возвращает объект `SimpleNamespace`, представляющий категорию.
3. Если категория не найдена, логирует предупреждение и возвращает `None`.
4. Логирует ошибки, если не удалось получить категорию.

```
Получение категории
    Начало
    │
    ├───▶ Проверка наличия атрибута category у объекта self.campaign
    │
    ├───▶ Проверка наличия категории с указанным именем
    │   └───▶ Категория найдена
    │       └───▶ Возврат объекта SimpleNamespace, представляющего категорию
    │   └───▶ Категория не найдена
    │       └───▶ Логирование предупреждения
    │       └───▶ Возврат None
    │
    ├───▶ Обработка исключений
    │   └───▶ Произошла ошибка
    │       └───▶ Логирование ошибки
    │       └───▶ Возврат None
    │
    └───▶ Завершение
```

**Примеры**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
category = editor.get_category("Electronics")
print(category)
```

### `list_categories`

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

**Назначение**: Получает список категорий в текущей кампании.

**Параметры**:
- None

**Возвращает**:
- `Optional[List[str]]`: Список имен категорий или `None`, если категории не найдены.

**Как работает функция**:
1. Проверяет, есть ли у объекта `self.campaign` атрибут `category` и является ли он экземпляром `SimpleNamespace`.
2. Если атрибут `category` существует и является экземпляром `SimpleNamespace`, возвращает список ключей атрибута, представляющих имена категорий.
3. Если атрибут `category` не существует или не является экземпляром `SimpleNamespace`, логирует предупреждение и возвращает `None`.
4. Логирует ошибки, если не удалось получить список категорий.

```
Получение списка категорий
    Начало
    │
    ├───▶ Проверка наличия атрибута category у объекта self.campaign
    │
    ├───▶ Проверка, является ли атрибут category экземпляром SimpleNamespace
    │   └───▶ Атрибут category существует и является экземпляром SimpleNamespace
    │       └───▶ Возврат списка ключей атрибута category (имена категорий)
    │   └───▶ Атрибут category не существует или не является экземпляром SimpleNamespace
    │       └───▶ Логирование предупреждения
    │       └───▶ Возврат None
    │
    ├───▶ Обработка исключений
    │   └───▶ Произошла ошибка
    │       └───▶ Логирование ошибки
    │       └───▶ Возврат None
    │
    └───▶ Завершение
```

**Примеры**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
categories = editor.categories_list
print(categories)
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
            f"No JSON files found for {category_name=} at {category_path=}.\\nStart prepare category"
        )
        self.process_category_products(category_name)
        return
```

**Назначение**: Читает данные о товарах из JSON-файлов для конкретной категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращает**:
- `Optional[List[SimpleNamespace]]`: Список объектов `SimpleNamespace`, представляющих товары.

**Как работает функция**:
1. Формирует путь к каталогу категории на основе имени категории, языка и валюты.
2. Получает список JSON-файлов в каталоге категории.
3. Если JSON-файлы найдены, читает данные из каждого файла и создает объекты `SimpleNamespace`, представляющие товары.
4. Если JSON-файлы не найдены, логирует ошибку и вызывает метод `process_category_products` для подготовки категории.

```
Чтение данных о товарах из JSON-файлов для категории
    Начало
    │
    ├───▶ Формирование пути к каталогу категории (category_path)
    │
    ├───▶ Получение списка JSON-файлов в каталоге категории (json_filenames)
    │
    ├───▶ Проверка наличия JSON-файлов
    │   └───▶ JSON-файлы найдены
    │       └───▶ Перебор JSON-файлов
    │           └───▶ Чтение данных из JSON-файла (product_data)
    │           └───▶ Создание объекта SimpleNamespace, представляющего товар
    │           └───▶ Добавление объекта в список товаров (products)
    │       └───▶ Возврат списка товаров (products)
    │   └───▶ JSON-файлы не найдены
    │       └───▶ Логирование ошибки
    │       └───▶ Вызов метода process_category_products для подготовки категории
    │       └───▶ Возврат None
    │
    └───▶ Завершение
```

**Примеры**:

```python
products = campaign.get_category_products("Electronics")
print(len(products))