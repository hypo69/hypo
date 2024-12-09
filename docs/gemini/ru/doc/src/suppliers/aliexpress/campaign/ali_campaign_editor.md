# Модуль `hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor.py`

## Обзор

Этот модуль предоставляет редактор для рекламных кампаний AliExpress. Он позволяет пользователю добавлять, удалять, обновлять продукты и категории в кампании, а также получать информацию о них.  Модуль использует данные в формате JSON и взаимодействует с Google Sheets через `AliCampaignGoogleSheet`.

## Оглавление

* [Модуль `AliCampaignEditor`](#модуль-alicampaigneditor)
* [Функция `delete_product`](#функция-delete_product)
* [Функция `update_product`](#функция-update_product)
* [Функция `update_campaign`](#функция-update_campaign)
* [Функция `update_category`](#функция-update_category)
* [Функция `get_category`](#функция-get_category)
* [Функция `list_categories`](#функция-list_categories)
* [Функция `get_category_products`](#функция-get_category_products)


## Модуль `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` расширяет класс `AliPromoCampaign`, предоставляя методы для редактирования кампаний AliExpress. Он инициализируется именем кампании, языком и валютой.

**Методы**:

* `__init__(campaign_name, language=None, currency=None, campaign_file=None)`: Инициализирует редактор кампании.
* `delete_product(product_id, exc_info=False)`: Удаляет продукт, если у него нет аффилиатной ссылки.
* `update_product(category_name, lang, product)`: Обновляет детали продукта в категории.
* `update_campaign()`: Обновляет свойства кампании (описание, теги и т.д.).
* `update_category(json_path, category)`: Обновляет категорию в JSON-файле.
* `get_category(category_name)`: Возвращает объект `SimpleNamespace` для заданного имени категории.
* `list_categories()`: Возвращает список имен категорий в кампании.
* `get_category_products(category_name)`: Чтение данных о товарах из JSON-файлов для конкретной категории.



## Функция `delete_product`

**Описание**: Удаляет продукт, если у него нет аффилиатной ссылки.

**Параметры**:

* `product_id` (str): Идентификатор продукта.
* `exc_info` (bool, опционально):  Включать ли информацию об исключении в лог. По умолчанию `False`.

**Возвращает**:  Не имеет возвращаемого значения.

**Вызывает исключения**:

* `FileNotFoundError`: Если файл продукта не найден.
* `Exception`: При других ошибках при удалении файла продукта.


## Функция `update_product`

**Описание**: Обновляет детали продукта в категории.

**Параметры**:

* `category_name` (str): Имя категории.
* `lang` (str): Язык.
* `product` (dict): Словарь с деталями продукта.

**Возвращает**: Не имеет возвращаемого значения.


## Функция `update_campaign`

**Описание**: Обновляет свойства кампании.

**Параметры**: Нет.

**Возвращает**:  Не имеет возвращаемого значения.


## Функция `update_category`

**Описание**: Обновляет категорию в JSON-файле.

**Параметры**:

* `json_path` (Path): Путь к JSON-файлу.
* `category` (SimpleNamespace): Объект `SimpleNamespace` с данными категории.

**Возвращает**:
* `bool`: `True`, если обновление прошло успешно, `False` - в противном случае.

**Вызывает исключения**: Возможны исключения при работе с JSON-файлом.


## Функция `get_category`

**Описание**: Возвращает объект `SimpleNamespace` для заданного имени категории.

**Параметры**:

* `category_name` (str): Имя категории.

**Возвращает**:
* `Optional[SimpleNamespace]`: Объект `SimpleNamespace` с данными категории или `None`, если категория не найдена.


## Функция `list_categories`

**Описание**: Возвращает список имен категорий в кампании.

**Параметры**: Нет.

**Возвращает**:
* `Optional[List[str]]`: Список имен категорий или `None`, если категории не найдены.


## Функция `get_category_products`

**Описание**: Чтение данных о товарах из JSON файлов для конкретной категории.

**Параметры**:

* `category_name` (str): Имя категории.

**Возвращает**:
* `Optional[List[SimpleNamespace]]`: Список объектов `SimpleNamespace`, представляющих товары или `None` при отсутствии файлов.

**Вызывает исключения**: Логирование ошибок, если JSON-файлы не найдены.