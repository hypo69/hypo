# Модуль `hypotez/src/suppliers/chat_gpt/gsheet.py`

## Обзор

Данный модуль предоставляет класс `GptGs` для управления Google Таблицами в контексте кампаний AliExpress. Класс наследуется от `SpreadSheet` и предоставляет методы для чтения, записи и управления данными о категориях, продуктах и самой кампании.

## Классы

### `GptGs`

**Описание**: Класс `GptGs` предназначен для работы с Google Таблицами в контексте кампаний AliExpress. Он наследуется от `SpreadSheet` и предоставляет методы для работы с данными о категориях, продуктах и кампании в целом.


**Методы**:

#### `__init__(self)`

**Описание**: Инициализирует объект `GptGs`.

**Параметры**:

* `campaign_name` (str): Имя кампании.
* `category_name` (str): Имя категории.
* `language` (str): Язык кампании.
* `currency` (str): Валюта кампании.

**Возвращает**:
    - None

#### `clear(self)`

**Описание**: Очищает содержимое Google Таблицы. Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.

**Параметры**:
- None

**Возвращает**:
- None


#### `update_chat_worksheet(self, data: SimpleNamespace|dict|list, conversation_name:str, language: str = None)`

**Описание**: Записывает данные кампании в лист Google Таблицы.

**Параметры**:

* `data` (SimpleNamespace | dict | list): Данные кампании в формате SimpleNamespace, словаря или списка.
* `conversation_name` (str): Имя листа, куда записывать данные.
* `language` (str, optional): Язык. По умолчанию None.
* `currency` (str, optional): Валюта. По умолчанию None.

**Возвращает**:
- None

**Вызывает исключения**:
- `Exception`:  Любые ошибки, возникающие при записи в таблицу.

#### `get_campaign_worksheet(self) -> SimpleNamespace`

**Описание**: Читает данные кампании из листа 'campaign'.

**Параметры**:
- None

**Возвращает**:
- SimpleNamespace: Объект SimpleNamespace с данными кампании.

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при чтении из таблицы, например, если лист не найден.


#### `set_category_worksheet(self, category: SimpleNamespace | str)`

**Описание**: Записывает данные категории в лист 'category' Google Таблицы.

**Параметры**:

* `category` (SimpleNamespace): Данные категории в формате SimpleNamespace.

**Возвращает**:
- None

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при записи в таблицу.
- `TypeError`: Если параметр `category` не является `SimpleNamespace`.


#### `get_category_worksheet(self) -> SimpleNamespace`

**Описание**: Читает данные категории из листа 'category'.

**Параметры**:
- None

**Возвращает**:
- SimpleNamespace: Объект SimpleNamespace с данными категории.

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при чтении из таблицы, например, если лист не найден.


#### `set_categories_worksheet(self, categories: SimpleNamespace)`

**Описание**: Записывает данные нескольких категорий в лист 'categories'.

**Параметры**:

* `categories` (SimpleNamespace): Объект SimpleNamespace с данными категорий.

**Возвращает**:
- None

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при записи в таблицу.


#### `get_categories_worksheet(self) -> List[List[str]]`

**Описание**: Читает данные из столбцов A-E листа 'categories' с 2-ой строки.

**Параметры**:
- None

**Возвращает**:
- `List[List[str]]`: Данные из листа в виде списка списков строк.

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при чтении из таблицы, например, если лист не найден.


#### `set_product_worksheet(self, product: SimpleNamespace | str, category_name: str)`

**Описание**: Записывает данные продукта в новый лист Google Таблицы.

**Параметры**:

* `category_name` (str): Имя категории.
* `product` (SimpleNamespace): Данные продукта.

**Возвращает**:
- None

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при записи в таблицу.


#### `get_product_worksheet(self) -> SimpleNamespace`

**Описание**: Читает данные продукта из листа 'products'.

**Параметры**:
- None

**Возвращает**:
- SimpleNamespace: Объект SimpleNamespace с данными продукта.

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при чтении из таблицы, например, если лист не найден.


#### `set_products_worksheet(self, category_name:str)`

**Описание**: Записывает данные продуктов для заданной категории.

**Параметры**:

* `category_name` (str): Имя категории.

**Возвращает**:
- None

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при записи в таблицу.


#### `delete_products_worksheets(self)`

**Описание**: Удаляет все листы из Google Таблицы, кроме `categories` и `product_template`.

**Параметры**:
- None

**Возвращает**:
- None

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при удалении листов.


#### `save_categories_from_worksheet(self, update:bool=False)`

**Описание**: Сохраняет данные категорий, изменённые в Google Таблице.

**Параметры**:
- `update` (bool, optional): Флаг, указывающий на обновление кампании. По умолчанию False.

**Возвращает**:
- None

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при сохранении данных.



#### `save_campaign_from_worksheet(self)`

**Описание**: Сохраняет данные кампании из Google Таблицы.

**Параметры**:
- None

**Возвращает**:
- None

**Вызывает исключения**:
- `Exception`: Любые ошибки, возникающие при сохранении данных.


## Функции


(Здесь будут функции, если они есть в файле)