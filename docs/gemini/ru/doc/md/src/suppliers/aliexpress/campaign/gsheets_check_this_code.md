# Модуль `hypotez/src/suppliers/aliexpress/campaign/gsheets_check_this_code.py`

## Обзор

Модуль `gsheets_check_this_code.py` предоставляет класс `AliCampaignGoogleSheet` для работы с Google Таблицами в контексте управления рекламными кампаниями AliExpress.  Класс наследует функциональность из `SpreadSheet` и расширяет её, включая методы для записи данных о категориях, продуктах и форматирования листов.  Он обрабатывает создание, очистку и обновление листов, содержащих данные кампаний, категорий и продуктов.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Таблицами в контексте управления рекламными кампаниями AliExpress. Предоставляет методы для записи данных о категориях, продуктах и форматирования листов.

**Атрибуты**:

- `spreadsheet_id`: Строка, содержащая ID Google Таблицы.
- `spreadsheet`: Экземпляр класса `SpreadSheet`, представляющий текущую таблицу.
- `worksheet`: Экземпляр класса `Worksheet`, представляющий текущий лист таблицы.
- `driver`: Экземпляр класса `Driver` для работы с браузером (по умолчанию Chrome).


**Методы**:

#### `__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)`

**Описание**: Инициализирует класс `AliCampaignGoogleSheet`.

**Параметры**:

- `campaign_name` (str): Название рекламной кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Возвращает**:

- None

#### `clear(self)`

**Описание**: Очищает содержимое Google Таблицы, удаляя листы продуктов и очищая данные на листах категорий.

**Параметры**:

- Нет

**Возвращает**:

- None

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с Google Таблицами (e.g., `Exception`).


#### `delete_products_worksheets(self)`

**Описание**: Удаляет все листы Google Таблицы, за исключением листов 'categories' и 'product_template'.

**Параметры**:

- Нет

**Возвращает**:

- None

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с Google Таблицами (e.g., `Exception`).

#### `set_campaign_worksheet(self, campaign: SimpleNamespace)`

**Описание**: Записывает данные о кампании в лист Google Таблицы 'campaign'.

**Параметры**:

- `campaign` (SimpleNamespace): Объект с данными о кампании.

**Возвращает**:

- None

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с Google Таблицами (e.g., `Exception`).

#### `set_products_worksheet(self, category_name: str)`

**Описание**: Записывает данные о продуктах определенной категории в отдельный лист.

**Параметры**:

- `category_name` (str): Название категории.

**Возвращает**:

- None

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с Google Таблицами (e.g., `Exception`).

#### `set_categories_worksheet(self, categories: SimpleNamespace)`

**Описание**: Записывает данные о категориях в лист Google Таблицы 'categories'.

**Параметры**:

- `categories` (SimpleNamespace): Объект с данными о категориях.

**Возвращает**:

- None

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с Google Таблицами (e.g., `Exception`).

#### `get_categories(self)`

**Описание**: Возвращает данные о категориях из листа 'categories' в виде списка словарей.

**Параметры**:

- Нет

**Возвращает**:

- list[dict]: Список словарей с данными о категориях.

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с Google Таблицами (e.g., `Exception`).

#### `set_category_products(self, category_name: str, products: dict)`

**Описание**: Запись данных о продуктах в новую таблицу Google Sheets.

**Параметры**:

- `category_name`: Название категории.
- `products`: Словарь с данными о продуктах.

**Возвращает**:
- None

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с Google Таблицами (e.g., `Exception`).


#### `_format_categories_worksheet(self, ws: Worksheet)` и `_format_category_products_worksheet(self, ws: Worksheet)`

**Описание**: Методы форматирования листов с категориями и продуктами (ширина столбцов, высота строк, стили заголовков).


**Параметры**:

- `ws`: Лист Google Sheets для форматирования (экземпляр класса `Worksheet`).

**Возвращает**:

- None

**Вызывает исключения**:
- Любые исключения, возникающие при форматировании.




## Функции


(Нет функций в этом модуле)