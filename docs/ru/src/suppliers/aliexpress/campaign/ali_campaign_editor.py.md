# Модуль для редактирования рекламных кампаний AliExpress
## Обзор

Модуль `ali_campaign_editor.py` предоставляет класс `AliCampaignEditor`, предназначенный для редактирования рекламных кампаний на платформе AliExpress. Он расширяет функциональность класса `AliPromoCampaign` и включает методы для управления продуктами, категориями и общими параметрами кампании. Модуль позволяет добавлять, удалять и обновлять информацию о товарах и категориях, а также изменять основные параметры кампании, такие как описание и теги.

## Подробней

`AliCampaignEditor` предназначен для автоматизации процессов редактирования и обновления рекламных кампаний AliExpress. Он предоставляет интерфейс для работы с данными о продуктах и категориях, хранящимися в формате JSON. Класс использует вспомогательные функции из других модулей проекта, таких как `j_loads_ns` и `j_dumps` для работы с JSON-файлами, а также `extract_prod_ids` для извлечения идентификаторов продуктов.

## Классы

### `AliCampaignEditor`

**Описание**: Редактор рекламных кампаний AliExpress.

**Наследует**:
- `AliPromoCampaign`: Предоставляет базовую функциональность для управления рекламными кампаниями.

**Методы**:
- `__init__(campaign_name: str, language: Optional[str | dict] = None, currency: Optional[str] = None)`: Инициализирует экземпляр класса `AliCampaignEditor`.
- `delete_product(product_id: str, exc_info: bool = False)`: Удаляет товар, у которого отсутствует партнерская ссылка.
- `update_product(category_name: str, lang: str, product: dict)`: Обновляет детали товара в указанной категории.
- `update_campaign()`: Обновляет свойства кампании, такие как описание и теги.
- `update_category(json_path: Path, category: SimpleNamespace) -> bool`: Обновляет категорию в JSON-файле.
- `get_category(category_name: str) -> Optional[SimpleNamespace]`: Возвращает объект SimpleNamespace для указанного имени категории.
- `@property list_categories() -> Optional[List[str]]`: Возвращает список категорий в текущей кампании.
- `async get_category_products(category_name: str) -> Optional[List[SimpleNamespace]]`: Читает данные о товарах из JSON файлов для конкретной категории.

### `__init__`

```python
def __init__(self, 
                 campaign_name: str, 
                 language: Optional[str | dict] = None, 
                 currency: Optional[str] = None):
    """ Инициализирует AliCampaignEditor с заданными параметрами.
        
    Args:
        campaign_name (Optional[str]): Имя кампании. По умолчанию `None`.
        language (Optional[str | dict]): Язык кампании. По умолчанию `EN`.
        currency (Optional[str]): Валюта для кампании. По умолчанию `USD`.
        campaign_file (Optional[str | Path]): При необходимости загружает `<lang>_<currency>.json` файл из корневой папки кампании. По умолчанию `None`.

    Raises:
        CriticalError: Если не предоставлены ни `campaign_name`, ни `campaign_file`.
    
    Example:
    # 1. по параметрам кампании
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
    # 2. загрузка из файла
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
    """
    ...
    super().__init__(campaign_name = campaign_name, language = language, currency = currency)
    #self.google_sheet = AliCampaignGoogleSheet(campaign_name = campaign_name, language = language, currency = currency, campaign_editor = self)
```

**Назначение**: Инициализирует экземпляр класса `AliCampaignEditor` с заданными параметрами.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (Optional[str | dict]): Язык кампании (например, "EN" или словарь с языковыми настройками). По умолчанию `None`.
- `currency` (Optional[str]): Валюта кампании (например, "USD"). По умолчанию `None`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Вызывает конструктор родительского класса `AliPromoCampaign` с переданными параметрами `campaign_name`, `language` и `currency` для инициализации базовых свойств кампании.
2. Закомментирована строка, которая создает экземпляр класса `AliCampaignGoogleSheet`. Вероятно, этот функционал связан с интеграцией Google Sheets для управления кампанией, но в текущей версии кода он не используется.

**Примеры**:
```python
# 1. Создание экземпляра редактора кампании с указанием имени, языка и валюты:
editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")

# 2. Создание экземпляра редактора кампании с загрузкой данных из файла:
editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
```

### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Удаляет товар, у которого отсутствует партнерская ссылка.
        
    Args:
        product_id (str): ID товара для удаления.
        exc_info (bool): Включать ли информацию об исключении в логи. По умолчанию `False`.

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

**Назначение**: Удаляет товар из списка, если у него отсутствует партнерская ссылка.

**Параметры**:
- `product_id` (str): Идентификатор товара, который необходимо удалить.
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении в логи. По умолчанию `False`.

**Возвращает**:
- `None`

**Как работает функция**:

```
A[Извлечение ID товара]
    |
B[Проверка списка товаров]
    |
C[Если список существует] -- Да --> D[Поиск товара в списке]
    |   
    |   
    |   
    |   
    |   
C[Если список существует] -- Нет --> E[Поиск HTML файла товара]
    |
D[Поиск товара в списке] -- Нашел --> F[Удаление товара из списка]
    |
    |
D[Поиск товара в списке] -- Не нашел --> G[Завершение]
    |
F[Удаление товара из списка] --> H[Сохранение списка]
    |
    |
E[Поиск HTML файла товара] -- Нашел --> I[Переименование HTML файла]
    |
    |
E[Поиск HTML файла товара] -- Не нашел --> J[Лог ошибки]
    |
I[Переименование HTML файла] --> K[Лог успеха]
    |
H[Сохранение списка] --> G[Завершение]
J[Лог ошибки] --> G[Завершение]
K[Лог успеха] --> G[Завершение]
```

1.  **Извлечение ID товара**: Извлекает идентификатор товара из входного параметра `product_id` с использованием функции `extract_prod_ids`. Результат сохраняется в переменной `_product_id`.
2.  **Определение путей к файлам**:
    *   Определяет путь к файлу `sources.txt`, который предположительно содержит список идентификаторов товаров, и путь к временному файлу `_sources.txt`, который будет использоваться для сохранения обновленного списка.
3.  **Чтение списка товаров**: Считывает содержимое файла `sources.txt` в список `products_list` с использованием функции `read_text_file`.
4.  **Проверка существования списка товаров**: Проверяет, был ли успешно прочитан список товаров из файла.
5.  **Поиск и удаление товара из списка**:
    *   Если список товаров существует, функция перебирает каждый элемент списка `products_list`.
    *   Если `_product_id` не пустой, извлекается идентификатор из текущей записи `record` и сравнивается с `product_id`. Если идентификаторы совпадают, запись удаляется из списка, и обновленный список сохраняется во временный файл `_sources.txt` с использованием функции `save_text_file`.
    *   Если `_product_id` пустой, сравнивается текущая запись `record` с `product_id`. Если они совпадают, запись удаляется из списка, и обновленный список сохраняется в файл `sources.txt`.
6.  **Обработка случая, когда список товаров не существует**:
    *   Если список товаров не был найден (файл `sources.txt` отсутствует), функция пытается переименовать HTML-файл товара, добавляя к его имени символ подчеркивания. Это может быть альтернативным способом "удаления" товара, если список товаров отсутствует.
    *   Определяет путь к HTML-файлу товара на основе `product_id`.
    *   Пытается переименовать файл товара, добавляя символ `_` в конец имени файла.
    *   Логирует успешное переименование файла, если операция выполнена успешно.
    *   В случае, если файл не найден, логирует ошибку `FileNotFoundError`.
    *   В случае других исключений логирует критическую ошибку.

**Примеры**:
```python
# 1. Удаление товара с указанным ID:
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.delete_product("12345")

# 2. Удаление товара с указанием необходимости логирования информации об исключениях:
editor.delete_product("67890", exc_info=True)
```

### `update_product`

```python
def update_product(self, category_name: str, lang: str, product: dict):
    """ Обновляет детали товара в указанной категории.

    Args:
        category_name (str): Название категории, в которой нужно обновить товар.
        lang (str): Язык кампании.
        product (dict): Словарь, содержащий детали товара.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
    """
    ...
    self.dump_category_products_files(category_name, lang, product)
```

**Назначение**: Обновляет детали товара в указанной категории.

**Параметры**:
- `category_name` (str): Название категории, в которой нужно обновить товар.
- `lang` (str): Язык кампании.
- `product` (dict): Словарь, содержащий детали товара.

**Возвращает**:
- `None`

**Как работает функция**:
1.  **Вызов функции `dump_category_products_files`**: Вызывает метод `dump_category_products_files` с переданными параметрами `category_name`, `lang` и `product`. Этот метод, вероятно, отвечает за сохранение информации о продукте в файловой системе, обновляя соответствующие JSON-файлы.

**Примеры**:
```python
# 1. Обновление товара в категории "Electronics" на английском языке:
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
```

### `update_campaign`

```python
def update_campaign(self):
    """ Обновляет свойства кампании, такие как `description`, `tags` и т.д.
    
    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.update_campaign()
    """
    ...
```

**Назначение**: Обновляет свойства кампании, такие как описание и теги.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `None`

**Как работает функция**:
1.  **Заглушка**: В текущей версии кода функция не содержит реализации (`...`). Это означает, что функциональность обновления свойств кампании не реализована или находится в разработке.

**Примеры**:
```python
# 1. Обновление параметров кампании:
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_campaign()
```

### `update_category`

```python
def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
    """ Обновляет категорию в JSON-файле.

    Args:
        json_path (Path): Путь к JSON-файлу.
        category (SimpleNamespace): Объект категории для обновления.

    Returns:
        bool: True, если обновление выполнено успешно, False в противном случае.

    Example:
        >>> category = SimpleNamespace(name="New Category", description="Updated description")
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> result = editor.update_category(Path("category.json"), category)
        >>> print(result)  # True, если успешно
    """
    ...
    try:
        data = j_loads(json_path)  # Читаем JSON данные из файла
        data['category'] = category.__dict__  # Преобразуем SimpleNamespace в dict
        j_dumps(data, json_path)  # Записываем обновленные JSON данные обратно в файл
        return True
    except Exception as ex:
        logger.error(f"Failed to update category {json_path}: {ex}")
        return False
```

**Назначение**: Обновляет категорию в JSON-файле.

**Параметры**:
- `json_path` (Path): Путь к JSON-файлу, который нужно обновить.
- `category` (SimpleNamespace): Объект `SimpleNamespace`, содержащий обновленные данные категории.

**Возвращает**:
- `bool`: `True`, если обновление выполнено успешно, `False` в противном случае.

**Как работает функция**:

```
A[Чтение JSON данных]
    |
B[Преобразование данных категории]
    |
C[Запись JSON данных]
    |
D[Обработка ошибок]
```

1.  **Чтение JSON данных**: Читает содержимое JSON-файла, расположенного по пути `json_path`, используя функцию `j_loads`. Полученные данные сохраняются в переменной `data`.
2.  **Преобразование данных категории**: Преобразует объект `category` типа `SimpleNamespace` в словарь с помощью атрибута `__dict__`. Этот словарь присваивается ключу `'category'` в словаре `data`.
3.  **Запись JSON данных**: Записывает обновленные данные, содержащиеся в словаре `data`, обратно в JSON-файл, расположенный по пути `json_path`, используя функцию `j_dumps`.
4.  **Обработка ошибок**: Если в процессе чтения или записи JSON-файла возникает исключение, функция перехватывает его, логирует сообщение об ошибке с использованием `logger.error` и возвращает `False`. Если операция выполнена успешно, функция возвращает `True`.

**Примеры**:
```python
# 1. Обновление категории в файле "category.json":
category = SimpleNamespace(name="New Category", description="Updated description")
editor = AliCampaignEditor(campaign_name="Summer Sale")
result = editor.update_category(Path("category.json"), category)
print(result)  # True, если успешно
```

### `get_category`

```python
def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
    """ Возвращает объект SimpleNamespace для указанного имени категории.

    Args:
        category_name (str): Название категории для получения.

    Returns:
        Optional[SimpleNamespace]: Объект SimpleNamespace, представляющий категорию, или `None`, если категория не найдена.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> category = editor.get_category("Electronics")
        >>> print(category)  # SimpleNamespace или None
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
- `category_name` (str): Название категории, которую нужно получить.

**Возвращает**:
- `Optional[SimpleNamespace]`: Объект `SimpleNamespace`, представляющий категорию, или `None`, если категория не найдена.

**Как работает функция**:

```
A[Проверка наличия категории]
    |
B[Возврат категории]   -- Категория найдена --> C[Возврат объекта SimpleNamespace]
    |
    |
B[Возврат категории]   -- Категория не найдена --> D[Лог предупреждения]
    |
D[Лог предупреждения] --> E[Завершение]
C[Возврат объекта SimpleNamespace] --> E[Завершение]
```

1.  **Проверка наличия категории**: Проверяет, существует ли атрибут с именем `category_name` в объекте `self.campaign.category` с помощью функции `hasattr`.
2.  **Возврат категории**:
    *   Если категория существует, функция возвращает значение атрибута `category_name` из объекта `self.campaign.category` с помощью функции `getattr`. Это значение представляет собой объект `SimpleNamespace`, содержащий информацию о категории.
    *   Если категория не найдена, функция логирует предупреждение с использованием `logger.warning` и возвращает `None`.
3.  **Обработка ошибок**: Если в процессе получения категории возникает исключение, функция перехватывает его, логирует сообщение об ошибке с использованием `logger.error` и возвращает `None`.

**Примеры**:
```python
# 1. Получение категории "Electronics":
editor = AliCampaignEditor(campaign_name="Summer Sale")
category = editor.get_category("Electronics")
print(category)  # SimpleNamespace или None
```

### `list_categories`

```python
@property
def list_categories(self) -> Optional[List[str]]:
    """ Получает список категорий в текущей кампании.

    Returns:
        Optional[List[str]]: Список названий категорий или None, если категории не найдены.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> categories = editor.categories_list
        >>> print(categories)  # ['Electronics', 'Fashion', 'Home']
    """
    try:
        # Проверка, что у кампании есть атрибут category и что он является SimpleNamespace
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
- Отсутствуют.

**Возвращает**:
- `Optional[List[str]]`: Список названий категорий или `None`, если категории не найдены.

**Как работает функция**:

```
A[Проверка наличия категорий]
    |
B[Получение списка категорий] -- Категории найдены --> C[Преобразование в список строк]
    |
    |
B[Получение списка категорий] -- Категории не найдены --> D[Лог предупреждения]
    |
D[Лог предупреждения] --> E[Завершение]
C[Преобразование в список строк] --> E[Завершение]
```

1.  **Проверка наличия категорий**: Проверяет, что у объекта `self.campaign` есть атрибут `category` и что этот атрибут является экземпляром класса `SimpleNamespace`.
2.  **Получение списка категорий**:
    *   Если категории найдены, функция извлекает список атрибутов (ключей) из объекта `self.campaign.category` с помощью функции `vars` и преобразует его в список строк. Этот список строк представляет собой список названий категорий.
    *   Если категории не найдены, функция логирует предупреждение с использованием `logger.warning` и возвращает `None`.
3.  **Обработка ошибок**: Если в процессе получения списка категорий возникает исключение, функция перехватывает его, логирует сообщение об ошибке с использованием `logger.error` и возвращает `None`.

**Примеры**:
```python
# 1. Получение списка категорий:
editor = AliCampaignEditor(campaign_name="Summer Sale")
categories = editor.list_categories
print(categories)  # ['Electronics', 'Fashion', 'Home']
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

**Назначение**: Чтение данных о товарах из JSON файлов для конкретной категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращает**:
- `Optional[List[SimpleNamespace]]`: Список объектов SimpleNamespace, представляющих товары.

**Как работает функция**:

```
A[Формирование пути к категории]
    |
B[Получение списка JSON файлов]
    |
C[Проверка наличия JSON файлов]
    |
D[Обработка JSON файлов] -- JSON файлы найдены --> E[Чтение данных из JSON файла]
    |
    |
D[Обработка JSON файлов] -- JSON файлы не найдены --> F[Лог ошибки]
    |
E[Чтение данных из JSON файла] --> G[Создание объекта SimpleNamespace]
    |
G[Создание объекта SimpleNamespace] --> H[Добавление объекта в список]
    |
H[Добавление объекта в список] --> I[Завершение цикла]
    |
F[Лог ошибки] --> J[Обработка продуктов категории]
    |
J[Обработка продуктов категории] --> K[Завершение]
I[Завершение цикла] --> K[Завершение]
```

1.  **Формирование пути к категории**: Формирует путь к директории категории на основе базового пути, имени категории, языка и валюты.
2.  **Получение списка JSON файлов**: Получает список JSON файлов в директории категории с использованием функции `get_filenames_from_directory`.
3.  **Проверка наличия JSON файлов**: Проверяет, найдены ли JSON файлы.
4.  **Обработка JSON файлов**:
    *   Если JSON файлы найдены, функция перебирает каждый файл, читает данные из JSON файла с использованием функции `j_loads_ns`, создает объект `SimpleNamespace` на основе прочитанных данных и добавляет его в список `products`.
    *   Если JSON файлы не найдены, функция логирует ошибку и вызывает функцию `process_category_products` для подготовки продуктов категории.

**Примеры**:
```python
# 1. Получение списка товаров для категории "Electronics":
products = campaign.get_category_products("Electronics")
print(len(products))
15