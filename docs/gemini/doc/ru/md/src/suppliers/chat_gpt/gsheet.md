# Модуль gsheet.py

## Обзор

Этот модуль предоставляет класс `GptGs`, наследуемый от `SpreadSheet`, для управления Google Таблицами в контексте рекламных кампаний AliExpress.  Класс позволяет записывать и читать данные о категориях, продуктах и кампаниях, а также форматировать листы таблиц.  Он обеспечивает методы для очистки данных, обновления листов, чтения и записи данных в листы `campaign`, `category`, `categories` и для управления продуктовыми листами.

## Классы

### `GptGs`

**Описание**: Класс для управления Google Таблицами в контексте рекламных кампаний AliExpress. Наследуется от `SpreadSheet` и предоставляет методы для работы с конкретными листами.

**Методы:**

#### `__init__(self, spreadsheet_id: str = '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')`

**Описание**: Инициализирует экземпляр класса `GptGs`.

**Параметры**:
- `spreadsheet_id` (str): Идентификатор Google Таблицы. По умолчанию '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'.

#### `clear(self)`

**Описание**: Очищает содержимое Google Таблицы. Удаляет листы с продуктами и очищает данные в листах `category`, `categories` и `campaign`.

**Вызывает исключения**:
- `Exception`: Ошибка при очистке.


#### `update_chat_worksheet(self, data: SimpleNamespace | dict | list, conversation_name: str, language: str = None)`

**Описание**: Записывает данные кампании в лист Google Таблицы.

**Параметры**:
- `data` (SimpleNamespace | dict | list): Данные кампании для записи.
- `conversation_name` (str): Название листа.
- `language` (str, optional): Язык кампании.


**Вызывает исключения**:
- `Exception`: Ошибка при записи данных.

#### `get_campaign_worksheet(self) -> SimpleNamespace`

**Описание**: Читает данные кампании из листа 'campaign'.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с данными кампании.

**Вызывает исключения**:
- `Exception`: Ошибка при чтении данных.
- `ValueError`: Лист 'campaign' не найден.


#### `set_category_worksheet(self, category: SimpleNamespace | str)`

**Описание**: Записывает данные категории в лист 'category'.

**Параметры**:
- `category` (SimpleNamespace): Объект SimpleNamespace с данными категории для записи.

**Вызывает исключения**:
- `Exception`: Ошибка при записи данных.
- `TypeError`: Ожидается `SimpleNamespace` для категории.


#### `get_category_worksheet(self) -> SimpleNamespace`

**Описание**: Читает данные категории из листа 'category'.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с данными категории.

**Вызывает исключения**:
- `Exception`: Ошибка при чтении данных.
- `ValueError`: Лист 'category' не найден.

#### `set_categories_worksheet(self, categories: SimpleNamespace)`

**Описание**: Записывает данные категорий в лист 'categories'.

**Параметры**:
- `categories` (SimpleNamespace): Объект SimpleNamespace с данными категорий для записи.

**Вызывает исключения**:
- `Exception`: Ошибка при записи данных.


#### `get_categories_worksheet(self) -> List[List[str]]`

**Описание**: Читает данные из колонок A-E листа 'categories', начиная со второй строки.

**Возвращает**:
- `List[List[str]]`: Данные из листа 'categories'.

**Вызывает исключения**:
- `Exception`: Ошибка при чтении данных.
- `ValueError`: Лист 'categories' не найден.


#### `set_product_worksheet(self, product: SimpleNamespace | str, category_name: str)`

**Описание**: Записывает данные продукта в новый лист Google Таблицы.

**Параметры**:
- `product` (SimpleNamespace): Объект SimpleNamespace с данными продукта.
- `category_name` (str): Имя категории.

**Вызывает исключения**:
- `Exception`: Ошибка при записи данных.

#### `get_product_worksheet(self) -> SimpleNamespace`

**Описание**: Читает данные продукта из листа 'products'.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с данными продукта.

**Вызывает исключения**:
- `Exception`: Ошибка при чтении данных.
- `ValueError`: Лист 'products' не найден.


#### `set_products_worksheet(self, category_name:str)`

**Описание**: Записывает данные продуктов в лист Google Таблицы, соответствующий указанной категории.


#### `delete_products_worksheets(self)`

**Описание**: Удаляет все листы в Google Таблице, кроме `categories` и `product_template`.

**Вызывает исключения**:
- `Exception`: Ошибка при удалении листов.


#### `save_categories_from_worksheet(self, update: bool = False)`

**Описание**:  Сохраняет данные из листа 'categories' в атрибут `campaign.category`.


#### `save_campaign_from_worksheet(self)`

**Описание**: Сохраняет данные кампании из Google Таблицы в атрибут `self.campaign`.