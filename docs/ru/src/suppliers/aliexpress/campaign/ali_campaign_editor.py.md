# Модуль ali_campaign_editor

## Обзор

Модуль `ali_campaign_editor.py` предоставляет класс `AliCampaignEditor`, который используется для редактирования рекламных кампаний на AliExpress. Он позволяет добавлять, удалять, обновлять и получать информацию о товарах и категориях в рамках кампании.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для работы с рекламными кампаниями AliExpress. Он предоставляет инструменты для управления категориями и товарами в рамках кампании, включая обновление информации о товарах, удаление товаров, не имеющих партнерских ссылок, и обновление свойств кампании. Модуль использует другие модули проекта, такие как `ali_promo_campaign`, `ali_campaign_gsheet`, `j_loads_ns`, `j_dumps` и другие утилиты для работы с файлами и данными.

## Классы

### `AliCampaignEditor`

**Описание**: Редактор для рекламных кампаний. Наследуется от класса `AliPromoCampaign`.

**Как работает класс**:

1.  **Инициализация**: При инициализации класса создается инстанс класса `AliCampaignEditor` с указанием имени кампании, языка и валюты. Также вызывается конструктор родительского класса `AliPromoCampaign` для инициализации общих параметров кампании.
2.  **Удаление товара**: Метод `delete_product` позволяет удалить товар из кампании, если у него нет партнерской ссылки.
3.  **Обновление товара**: Метод `update_product` позволяет обновить информацию о товаре в рамках определенной категории.
4.  **Обновление кампании**: Метод `update_campaign` позволяет обновить свойства кампании, такие как описание и теги.
5.  **Обновление категории**: Метод `update_category` позволяет обновить информацию о категории в JSON-файле.
6.  **Получение категории**: Метод `get_category` позволяет получить объект `SimpleNamespace`, представляющий категорию по ее имени.
7.  **Получение списка категорий**: Метод `list_categories` позволяет получить список категорий в текущей кампании.
8.  **Получение товаров категории**: Метод `get_category_products` позволяет получить список товаров для заданной категории.

**Методы**:

-   `__init__`: Инициализирует экземпляр класса `AliCampaignEditor`.
-   `delete_product`: Удаляет товар, у которого нет партнерской ссылки.
-   `update_product`: Обновляет информацию о товаре в рамках категории.
-   `update_campaign`: Обновляет свойства кампании, такие как описание и теги.
-   `update_category`: Обновляет категорию в JSON-файле.
-   `get_category`: Возвращает объект `SimpleNamespace` для указанного имени категории.
-   `list_categories`: Возвращает список категорий в текущей кампании.
-   `get_category_products`: Возвращает список товаров для заданной категории.

## Функции

### `__init__`

```python
def __init__(
    self,
    campaign_name: str,
    language: Optional[str | dict] = None,
    currency: Optional[str] = None,
):
    """Инициализирует AliCampaignEditor с заданными параметрами.

    Args:
        campaign_name (str): Название кампании.
        language (Optional[str | dict], optional): Язык кампании. По умолчанию 'EN'.
        currency (Optional[str], optional): Валюта для кампании. По умолчанию 'USD'.

    Raises:
        CriticalError: Если не указаны `campaign_name` и не загружен `campaign_file`.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
    """
```

**Назначение**: Инициализация экземпляра класса `AliCampaignEditor` с заданными параметрами, такими как имя кампании, язык и валюта.

**Параметры**:

-   `campaign_name` (str): Имя кампании.
-   `language` (Optional[str | dict], optional): Язык кампании. Может быть строкой или словарем. По умолчанию `None`.
-   `currency` (Optional[str], optional): Валюта кампании. По умолчанию `None`.
-   `campaign_file` (Optional[str | Path], optional): Путь к файлу кампании `<lang>_<currency>.json` в корневой папке кампании.

**Как работает функция**:

1.  Вызывается конструктор родительского класса `AliPromoCampaign` с переданными параметрами.
2.  Инициализируется атрибут `google_sheet` экземпляром класса `AliCampaignGoogleSheet`.

### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """Удаляет товар, у которого нет партнерской ссылки.

    Args:
        product_id (str): ID товара, который нужно удалить.
        exc_info (bool): Включать ли информацию об исключении в логи. По умолчанию `False`.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.delete_product("12345")
    """
```

**Назначение**: Удаление товара из кампании, если у него нет партнерской ссылки.

**Параметры**:

-   `product_id` (str): ID товара, который необходимо удалить.
-   `exc_info` (bool): Флаг, указывающий, следует ли включать информацию об исключении в логи. По умолчанию `False`.

**Как работает функция**:

1.  Извлекает ID товара из строки `product_id` с помощью функции `extract_prod_ids`.
2.  Определяет пути к файлу `sources.txt` и временному файлу `_sources.txt` в директории категории.
3.  Читает содержимое файла `sources.txt` с помощью функции `read_text_file`.
4.  Если файл `sources.txt` существует, то перебирает записи в списке товаров.
    -   Если `_product_id` не пустой, извлекает ID записи и сравнивает с `product_id`. Если ID совпадают, удаляет запись из списка, сохраняет обновленный список во временный файл `_sources.txt` и прерывает цикл.
    -   Если `_product_id` пустой, сравнивает запись с `product_id`. Если они совпадают, удаляет запись из списка и сохраняет обновленный список в файл `sources.txt`.
5.  Если файл `sources.txt` не существует, формирует путь к файлу товара в директории `sources` и переименовывает его, добавляя символ `_` в конце имени файла.
6.  Логирует успешное переименование файла товара.
7.  Обрабатывает исключения `FileNotFoundError` и `Exception`, логируя ошибки с использованием модуля `logger`.

### `update_product`

```python
def update_product(self, category_name: str, lang: str, product: dict):
    """Обновляет детали товара в категории.

    Args:
        category_name (str): Название категории, в которой нужно обновить товар.
        lang (str): Язык кампании.
        product (dict): Словарь с деталями товара.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
    """
```

**Назначение**: Обновление информации о товаре в указанной категории.

**Параметры**:

-   `category_name` (str): Название категории, в которой необходимо обновить информацию о товаре.
-   `lang` (str): Язык кампании.
-   `product` (dict): Словарь, содержащий информацию о товаре, которую необходимо обновить.

**Как работает функция**:

1.  Вызывает метод `dump_category_products_files` для сохранения информации о товаре в файле категории.

### `update_campaign`

```python
def update_campaign(self):
    """Обновляет свойства кампании, такие как описание, теги и т.д.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> editor.update_campaign()
    """
```

**Назначение**: Обновление свойств рекламной кампании, таких как описание и теги.

**Как работает функция**:

1.  Функция пока не реализована (`...`).
    <инструкция для модели gemini:Опиши что делает функция, после ее реализации>

### `update_category`

```python
def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
    """Обновляет категорию в JSON-файле.

    Args:
        json_path (Path): Путь к JSON-файлу.
        category (SimpleNamespace): Объект категории для обновления.

    Returns:
        bool: True, если обновление успешно, False в противном случае.

    Example:
        >>> category = SimpleNamespace(name="New Category", description="Updated description")
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> result = editor.update_category(Path("category.json"), category)
        >>> print(result)  # True, если успешно
    """
```

**Назначение**: Обновление информации о категории в JSON-файле.

**Параметры**:

-   `json_path` (Path): Путь к JSON-файлу, который необходимо обновить.
-   `category` (SimpleNamespace): Объект `SimpleNamespace`, содержащий информацию о категории, которую необходимо обновить.

**Как работает функция**:

1.  Загружает данные из JSON-файла по указанному пути с помощью функции `j_loads`.
2.  Преобразует объект `SimpleNamespace` в словарь и присваивает его ключу `'category'` в загруженных данных.
3.  Записывает обновленные данные обратно в JSON-файл с помощью функции `j_dumps`.
4.  Возвращает `True`, если обновление выполнено успешно, и `False` в случае ошибки.
5.  В случае возникновения исключения, логирует ошибку с использованием модуля `logger` и возвращает `False`.

### `get_category`

```python
def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
    """Возвращает объект SimpleNamespace для указанного имени категории.

    Args:
        category_name (str): Имя категории для получения.

    Returns:
        Optional[SimpleNamespace]: Объект SimpleNamespace, представляющий категорию, или None, если категория не найдена.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> category = editor.get_category("Electronics")
        >>> print(category)  # SimpleNamespace или None
    """
```

**Назначение**: Получение объекта `SimpleNamespace`, представляющего категорию по ее имени.

**Параметры**:

-   `category_name` (str): Имя категории, которую необходимо получить.

**Как работает функция**:

1.  Проверяет, существует ли атрибут с именем `category_name` в атрибуте `self.campaign.category`.
2.  Если категория найдена, возвращает объект `SimpleNamespace`, представляющий категорию.
3.  Если категория не найдена, логирует предупреждение с использованием модуля `logger` и возвращает `None`.
4.  В случае возникновения ошибки, логирует ошибку с использованием модуля `logger` и возвращает `None`.

### `list_categories`

```python
@property
def list_categories(self) -> Optional[List[str]]:
    """Получает список категорий в текущей кампании.

    Returns:
        Optional[List[str]]: Список названий категорий или None, если категории не найдены.

    Example:
        >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
        >>> categories = editor.categories_list
        >>> print(categories)  # ['Electronics', 'Fashion', 'Home']
    """
```

**Назначение**: Получение списка категорий в текущей кампании.

**Как работает функция**:

1.  Проверяет, существует ли атрибут `category` в объекте `self.campaign` и является ли он экземпляром класса `SimpleNamespace`.
2.  Если категория существует, возвращает список ключей словаря, полученного из атрибута `category` с помощью функции `vars`.
3.  Если категория не найдена, логирует предупреждение с использованием модуля `logger` и возвращает `None`.
4.  В случае возникновения ошибки, логирует ошибку с использованием модуля `logger` и возвращает `None`.

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
```

**Назначение**: Чтение данных о товарах из JSON-файлов для указанной категории.

**Параметры**:

-   `category_name` (str): Имя категории, для которой необходимо получить список товаров.

**Как работает функция**:

1.  Формирует путь к директории категории, используя базовый путь, имя категории, язык и валюту.
2.  Получает список JSON-файлов в директории категории с помощью асинхронной функции `get_filenames_from_directory`.
3.  Если JSON-файлы найдены, то для каждого файла:
    -   Загружает данные из JSON-файла с помощью функции `j_loads_ns`.
    -   Преобразует данные в объект `SimpleNamespace`.
    -   Добавляет объект `SimpleNamespace` в список товаров.
4.  Возвращает список товаров.
5.  Если JSON-файлы не найдены, логирует ошибку с использованием модуля `logger`, вызывает метод `process_category_products` для подготовки категории и возвращает `None`.