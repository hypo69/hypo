# Модуль `hypotez/src/suppliers/aliexpress/campaign/gsheet.py`

## Обзор

Модуль `gsheet.py` предоставляет класс `AliCampaignGoogleSheet` для работы с Google Таблицами в контексте управления рекламными кампаниями AliExpress. Он позволяет записывать данные о кампаниях, категориях и продуктах, а также форматировать листы для удобства.  Модуль использует библиотеку `gspread` для взаимодействия с Google Таблицами.


## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс `AliCampaignGoogleSheet` предназначен для работы с Google Таблицами в контексте управления кампаниями AliExpress. Он расширяет функциональность класса `SpreadSheet` из модуля `src.goog.spreadsheet.spreadsheet`, добавляя методы для специфических операций с листами, связанными с кампаниями, категориями и продуктами.


**Атрибуты**:

- `spreadsheet_id`: ID Google Таблицы (строка).
- `spreadsheet`: Объект `SpreadSheet`, представляющий Google Таблицу.
- `worksheet`: Объект `Worksheet`, представляющий текущий лист Google Таблицы.


**Методы**:

#### `__init__`

**Описание**: Инициализирует объект `AliCampaignGoogleSheet`.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Возвращает**:
- `None`

#### `clear`

**Описание**: Очищает содержимое таблицы, удаляя листы с продуктами и очищая данные на листах категорий и других указанных листах.

**Возвращает**:
- `None`

#### `delete_products_worksheets`

**Описание**: Удаляет все листы из Google Таблицы, кроме листов 'categories' и 'product_template'.

**Возвращает**:
- `None`

#### `set_campaign_worksheet`

**Описание**: Записывает данные кампании на лист Google Таблицы с названием 'campaign'.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании.

**Возвращает**:
- `None`

#### `set_products_worksheet`

**Описание**: Записывает данные о продуктах из списка объектов `SimpleNamespace` в Google Таблицу.

**Параметры**:
- `category_name` (str): Название категории.

**Возвращает**:
- `None`

#### `set_categories_worksheet`

**Описание**: Записывает данные о категориях из объекта `SimpleNamespace` в лист Google Таблицы с названием 'categories'.

**Параметры**:
- `categories` (SimpleNamespace): Объект `SimpleNamespace` с данными категорий.

**Возвращает**:
- `None`

#### `get_categories`

**Описание**: Получает данные из листа 'categories' Google Таблицы.

**Возвращает**:
- list[dict]: Список словарей с данными о категориях.

#### `set_category_products`

**Описание**: Записывает данные о продуктах в новый лист Google Таблицы, соответствующий указанной категории.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Возвращает**:
- `None`

#### `_format_categories_worksheet`

**Описание**: Форматирует лист 'categories'.

**Параметры**:
- `ws` (Worksheet): Лист Google Таблицы.

**Возвращает**:
- `None`

#### `_format_category_products_worksheet`

**Описание**: Форматирует лист с продуктами категории.

**Параметры**:
- `ws` (Worksheet): Лист Google Таблицы.

**Возвращает**:
- `None`

## Функции

(Здесь будут описания функций, если они есть в файле)


## Модули

(Здесь будут описания импортируемых модулей)


## Исключения

(Здесь будут описания исключений, если они есть в файле)