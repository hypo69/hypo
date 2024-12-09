# Модуль hypotez/src/suppliers/aliexpress/campaign/gsheet.py

## Обзор

Модуль `gsheet.py` предоставляет класс `AliCampaignGoogleSheet` для работы с Google Таблицами в контексте рекламных кампаний AliExpress.  Он позволяет записывать данные о кампаниях, категориях и продуктах в таблицы, а также форматировать их.  Модуль использует библиотеку gspread для взаимодействия с Google Таблицами и предоставляет функции для управления рабочими листами, очистки данных и настройки формата.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для управления Google Таблицами в контексте рекламных кампаний AliExpress.  Наследует класс `SpreadSheet`.  Предоставляет методы для работы с рабочими листами, записи данных о категориях и продуктах, а также форматирования.

**Атрибуты**:

- `spreadsheet_id`:  ID Google Таблицы.
- `spreadsheet`: Объект `SpreadSheet`, представляющий таблицу.
- `worksheet`: Объект `Worksheet`, представляющий текущий рабочий лист.


**Методы**:

#### `__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)`

**Описание**: Инициализирует объект `AliCampaignGoogleSheet`.

**Параметры**:

- `campaign_name` (str): Название рекламной кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.


#### `clear(self)`

**Описание**: Очищает содержимое таблицы. Удаляет листы с продуктами и очищает данные на листах категорий и других.


#### `delete_products_worksheets(self)`

**Описание**: Удаляет все листы Google Таблицы, кроме листов 'categories' и 'product_template'.

**Вызывает исключения**:

- Любые исключения, возникающие при удалении листов.


#### `set_campaign_worksheet(self, campaign: SimpleNamespace)`

**Описание**: Записывает данные о кампании в Google Таблицу на лист 'campaign'.

**Параметры**:

- `campaign` (SimpleNamespace): Объект с данными о кампании.


#### `set_products_worksheet(self, category_name: str)`

**Описание**: Записывает данные о продуктах в Google Таблицу на лист, соответствующий названию категории.

**Параметры**:

- `category_name` (str): Название категории.


#### `set_categories_worksheet(self, categories: SimpleNamespace)`

**Описание**: Записывает данные о категориях в Google Таблицу на лист 'categories'.

**Параметры**:

- `categories` (SimpleNamespace): Объект с данными о категориях.


#### `get_categories(self)`

**Описание**: Возвращает данные о категориях из Google Таблицы.

**Возвращает**:

- Список словарей с данными о категориях.


#### `set_category_products(self, category_name: str, products: dict)`

**Описание**: Записывает данные о продуктах в Google Таблицу для указанной категории.

**Параметры**:

- `category_name` (str): Название категории.
- `products` (dict): Данные о продуктах.


#### `_format_categories_worksheet(self, ws: Worksheet)`

**Описание**: Форматирует лист 'categories' Google Таблицы.

**Параметры**:

- `ws` (Worksheet): Рабочий лист для форматирования.


#### `_format_category_products_worksheet(self, ws: Worksheet)`

**Описание**: Форматирует лист с продуктами категории Google Таблицы.

**Параметры**:

- `ws` (Worksheet): Рабочий лист для форматирования.


## Функции


##  Примечания:

- Документация содержит переводы и уточнения.
- Не все комментарии в коде были полностью переведены на русский язык.
- Используются типизации `SimpleNamespace`, `Optional`, `List`, `Dict`.