# Модуль `hypotez/src/suppliers/chat_gpt/gsheet.py`

## Обзор

Этот модуль предоставляет класс `GptGs` для управления Google Таблицами в контексте кампаний AliExpress. Он позволяет читать, писать и обновлять данные о категориях, продуктах и кампаниях в Google Таблицах, используя библиотеку `gspread`.

## Класс `GptGs`

### Описание

Класс `GptGs` наследуется от `SpreadSheet` и предназначен для управления Google Таблицами. Он предоставляет методы для работы с данными кампаний, категорий и продуктов.

### Методы

#### `__init__(self, spreadsheet_id: str)`

**Описание**: Инициализирует объект `GptGs` со ссылкой на Google Таблицу.

**Параметры**:
- `spreadsheet_id` (str): Идентификатор Google Таблицы.


#### `clear(self)`

**Описание**: Очищает содержимое таблицы, удаляя все листы продуктов и очищая данные на листах категорий и кампании.

**Вызывает исключения**:
- `Exception`: Ошибка во время очистки.


#### `update_chat_worksheet(self, data, conversation_name: str, language: str = None)`

**Описание**: Записывает данные кампании в Google Таблицу.

**Параметры**:
- `data` (SimpleNamespace | dict | list): Данные кампании в формате SimpleNamespace, словаря или списка.
- `conversation_name` (str): Имя листа для записи данных.
- `language` (str, optional): Язык кампании. По умолчанию `None`.

**Вызывает исключения**:
- `Exception`: Ошибка во время записи данных.


#### `get_campaign_worksheet(self)`

**Описание**: Читает данные кампании из листа 'campaign'.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace, содержащий данные кампании.

**Вызывает исключения**:
- `ValueError`: Лист 'campaign' не найден.
- `Exception`: Ошибка при чтении данных.


#### `set_category_worksheet(self, category: SimpleNamespace | str)`

**Описание**: Записывает данные категории в вертикальном формате на лист 'category'.

**Параметры**:
- `category` (SimpleNamespace): Данные категории в формате SimpleNamespace.

**Вызывает исключения**:
- `TypeError`: Неверный тип данных для `category`.
- `Exception`: Ошибка при записи данных.


#### `get_category_worksheet(self)`

**Описание**: Читает данные категории из листа 'category'.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace, содержащий данные категории.

**Вызывает исключения**:
- `ValueError`: Лист 'category' не найден.
- `Exception`: Ошибка при чтении данных.


#### `set_categories_worksheet(self, categories: SimpleNamespace)`

**Описание**: Записывает данные списка категорий на лист 'categories'.

**Параметры**:
- `categories` (SimpleNamespace): Данные списка категорий в формате SimpleNamespace.

**Вызывает исключения**:
- `Exception`: Ошибка при записи данных.


#### `get_categories_worksheet(self)`

**Описание**: Читает данные со столбцов A до E с 2-ой строки из листа 'categories'.

**Возвращает**:
- `List[List[str]]`: Список строк со значениями из указанных столбцов.

**Вызывает исключения**:
- `ValueError`: Лист 'categories' не найден.
- `Exception`: Ошибка при чтении данных.


#### `set_product_worksheet(self, product: SimpleNamespace | str, category_name: str)`

**Описание**: Записывает данные продукта на новый лист Google Таблиц, скопированный с шаблона 'product_template'.

**Параметры**:
- `product` (SimpleNamespace): Данные продукта в формате SimpleNamespace.
- `category_name` (str): Имя категории.


**Вызывает исключения**:
- `Exception`: Ошибка при записи данных.


#### `get_product_worksheet(self)`

**Описание**: Читает данные продукта из листа 'products'.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace, содержащий данные продукта.

**Вызывает исключения**:
- `ValueError`: Лист 'products' не найден.
- `Exception`: Ошибка при чтении данных.


#### `set_products_worksheet(self, category_name: str)`

**Описание**: Записывает данные продуктов в лист Google Таблиц.

**Параметры**:
- `category_name` (str): Имя категории.

**Вызывает исключения**:
- `Exception`: Ошибка при записи данных.


#### `delete_products_worksheets(self)`

**Описание**: Удаляет все листы в Google Таблицах, кроме 'categories' и 'product_template'.

**Вызывает исключения**:
- `Exception`: Ошибка при удалении листов.


#### `save_categories_from_worksheet(self, update: bool = False)`

**Описание**: Сохраняет данные категорий, отредактированные в Google Таблице.

**Параметры**:
- `update` (bool, optional): Флаг обновления кампании. По умолчанию `False`.


**Вызывает исключения**:
- `Exception`: Ошибка при сохранении данных.


#### `save_campaign_from_worksheet(self)`

**Описание**: Сохраняет данные кампании из Google Таблицы.


**Вызывает исключения**:
- `Exception`: Ошибка при сохранении данных.


## Функции

(Список функций и методов, если таковые имеются, добавьте сюда их описание)