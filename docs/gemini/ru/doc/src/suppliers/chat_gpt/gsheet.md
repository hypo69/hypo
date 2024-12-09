# Модуль `hypotez/src/suppliers/chat_gpt/gsheet.py`

## Обзор

Данный модуль предоставляет класс `GptGs` для взаимодействия с Google Таблицами в контексте управления рекламными кампаниями AliExpress.  Класс наследуется от `SpreadSheet` и содержит методы для чтения, записи и управления данными в таблицах, включая категории, продукты и общие данные кампании.

## Класс `GptGs`

**Описание**: Класс для управления Google Таблицами в контексте рекламных кампаний AliExpress. Наследуется от `SpreadSheet` для работы с Google Таблицами.

**Методы**:

### `__init__(self, spreadsheet_id: str = '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')`

**Описание**: Инициализирует объект `GptGs`.

**Параметры**:

- `spreadsheet_id` (str): ID Google Таблицы. По умолчанию `'1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'`.

**Возвращает**:
-  None

### `clear(self)`

**Описание**: Очищает содержимое Google Таблицы, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.

**Параметры**:
-  None

**Возвращает**:
-  None

**Возможные исключения**:
- `Exception`: Общие ошибки при работе с Google Таблицами.


### `update_chat_worksheet(self, data: SimpleNamespace | dict | list, conversation_name: str, language: str = None, currency: str = None)`

**Описание**: Записывает данные кампании в лист Google Таблицы.

**Параметры**:

- `data` (SimpleNamespace | dict | list): Данные для записи. Ожидается объект `SimpleNamespace` или словарь/список.
- `conversation_name` (str): Имя листа Google Таблицы.
- `language` (str, optional): Язык кампании.
- `currency` (str, optional): Валюта кампании.

**Возвращает**:
-  None

**Возможные исключения**:
- `Exception`: Общие ошибки при записи данных в Google Таблицы.

### `get_campaign_worksheet(self) -> SimpleNamespace`

**Описание**: Чтение данных кампании из листа 'campaign'.

**Параметры**:
-  None

**Возвращает**:
- SimpleNamespace: Объект `SimpleNamespace` с данными кампании.

**Возможные исключения**:
- `ValueError`: Если лист 'campaign' не найден.
- `Exception`: Другие ошибки при чтении данных.


### `set_category_worksheet(self, category: SimpleNamespace | str)`

**Описание**: Запись данных категории в Google Таблицу на лист 'category'.

**Параметры**:

- `category` (SimpleNamespace | str): Данные категории. Может быть объектом `SimpleNamespace` или строкой.

**Возвращает**:
-  None

**Возможные исключения**:
- `TypeError`: Если `category` не является `SimpleNamespace`.
- `Exception`: Другие ошибки при записи.


### `get_category_worksheet(self) -> SimpleNamespace`

**Описание**: Чтение данных категории из листа 'category'.

**Параметры**:
-  None

**Возвращает**:
- SimpleNamespace: Объект `SimpleNamespace` с данными категории.

**Возможные исключения**:
- `ValueError`: Если лист 'category' не найден.
- `Exception`: Другие ошибки при чтении данных.


### `set_categories_worksheet(self, categories: SimpleNamespace)`

**Описание**: Запись данных множества категорий в лист 'categories'.

**Параметры**:
- `categories` (SimpleNamespace): Объект `SimpleNamespace` содержащий данные категорий.

**Возвращает**:
-  None

**Возможные исключения**:
- `Exception`: Общие ошибки при записи данных.



### `get_categories_worksheet(self) -> List[List[str]]`

**Описание**: Чтение данных со столбцов A до E листа 'categories' начиная со второй строки.

**Параметры**:
-  None

**Возвращает**:
-  List[List[str]]: Список строк со значениями.

**Возможные исключения**:
- `ValueError`: Если лист 'categories' не найден.
- `Exception`: Другие ошибки при чтении данных.


### `set_product_worksheet(self, product: SimpleNamespace | str, category_name: str)`

**Описание**: Запись данных продукта в новую таблицу Google.

**Параметры**:

- `category_name` (str): Название категории.
- `product` (SimpleNamespace | str): Объект `SimpleNamespace` с данными продукта.

**Возвращает**:
-  None

**Возможные исключения**:
- `Exception`: Общие ошибки при работе с Google Таблицами.



### `get_product_worksheet(self) -> SimpleNamespace`

**Описание**: Чтение данных продукта из листа 'products'.

**Параметры**:
-  None

**Возвращает**:
- SimpleNamespace: Объект `SimpleNamespace` с данными продукта.

**Возможные исключения**:
- `ValueError`: Если лист 'products' не найден.
- `Exception`: Другие ошибки при чтении данных.


### `set_products_worksheet(self, category_name: str)`

**Описание**: Запись данных продуктов для определенной категории в лист Google Таблиц.

**Параметры**:
- `category_name` (str): Название категории.

**Возвращает**:
-  None

**Возможные исключения**:
- `Exception`: Общие ошибки при записи данных.


### `delete_products_worksheets(self)`

**Описание**: Удаляет все листы Google Таблицы, кроме 'categories' и 'product_template'.

**Параметры**:
-  None

**Возвращает**:
-  None

**Возможные исключения**:
- `Exception`: Общие ошибки при работе с Google Таблицами.



### `save_categories_from_worksheet(self, update: bool = False)`

**Описание**: Сохранение отредактированных данных категорий из Google Таблицы.

**Параметры**:
- `update` (bool, optional): Если True, обновляет данные кампании. По умолчанию False.

**Возвращает**:
- None

**Возможные исключения**:
- `Exception`: Общие ошибки при работе с Google Таблицами.


### `save_campaign_from_worksheet(self)`

**Описание**: Сохранение данных рекламной кампании из Google Таблицы.

**Параметры**:
-  None

**Возвращает**:
- None

**Возможные исключения**:
- `Exception`: Общие ошибки при работе с Google Таблицами.