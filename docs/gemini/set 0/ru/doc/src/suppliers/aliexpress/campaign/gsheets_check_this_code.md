# Модуль `hypotez/src/suppliers/aliexpress/campaign/gsheets_check_this_code.py`

## Обзор

Модуль `gsheets_check_this_code.py` предоставляет класс `AliCampaignGoogleSheet` для работы с Google Таблицами в контексте управления рекламными кампаниями AliExpress. Он позволяет управлять данными кампании, категориями и продуктами, а также форматировать листы Google Таблиц. Модуль использует библиотеки `gspread`, `gspread-formatting` и другие для взаимодействия с Google Таблицами и управления данными.

## Оглавление

- [Модуль `gsheets_check_this_code.py`](#модуль-gsheets_check_this_codepy)
- [Класс `AliCampaignGoogleSheet`](#класс-alicampaigngooglesheet)
    - [Метод `__init__`](#метод-init)
    - [Метод `clear`](#метод-clear)
    - [Метод `delete_products_worksheets`](#метод-delete_products_worksheets)
    - [Метод `set_campaign_worksheet`](#метод-set_campaign_worksheet)
    - [Метод `set_products_worksheet`](#метод-set_products_worksheet)
    - [Метод `set_categories_worksheet`](#метод-set_categories_worksheet)
    - [Метод `get_categories`](#метод-get_categories)
    - [Метод `set_category_products`](#метод-set_category_products)
    - [Метод `_format_categories_worksheet`](#метод-_format_categories_worksheet)
    - [Метод `_format_category_products_worksheet`](#метод-_format_category_products_worksheet)


## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress. Наследует класс `SpreadSheet` и предоставляет методы для управления листами Google Sheets, записи данных о категориях и продуктах, и форматирования листов.

#### Метод `__init__`

**Описание**: Инициализирует экземпляр класса `AliCampaignGoogleSheet`.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Возвращает**:
- Нет (None).

#### Метод `clear`

**Описание**: Очищает содержимое Google Таблицы. Удаляет листы продуктов и очищает данные на листах категорий.

**Параметры**:
- Нет.

**Возвращает**:
- Нет (None).

**Вызывает исключения**:
- Любое исключение (`Exception`), если произошла ошибка.


#### Метод `delete_products_worksheets`

**Описание**: Удаляет все листы из Google Таблицы, кроме `categories` и `product_template`.

**Параметры**:
- Нет.

**Возвращает**:
- Нет (None).

**Вызывает исключения**:
- Любое исключение (`Exception`), если произошла ошибка.


#### Метод `set_campaign_worksheet`

**Описание**: Записывает данные о кампании на лист Google Таблицы.

**Параметры**:
- `campaign` (SimpleNamespace | str): Объект `SimpleNamespace` с данными о кампании.
- `language` (str, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Возвращает**:
- Нет (None).

**Вызывает исключения**:
- Любое исключение (`Exception`), если произошла ошибка.


#### Метод `set_products_worksheet`

**Описание**: Записывает данные о продуктах в Google Таблицу.

**Параметры**:
- `category_name` (str): Название категории.

**Возвращает**:
- Нет (None).

**Вызывает исключения**:
- Любое исключение (`Exception`), если произошла ошибка.

#### Метод `set_categories_worksheet`

**Описание**: Записывает данные о категориях на лист Google Таблицы.

**Параметры**:
- `categories` (SimpleNamespace): Объект `SimpleNamespace` с данными о категориях.

**Возвращает**:
- Нет (None).

**Вызывает исключения**:
- Любое исключение (`Exception`), если произошла ошибка.

#### Метод `get_categories`

**Описание**: Возвращает данные о категориях из Google Таблицы.

**Параметры**:
- Нет.

**Возвращает**:
- Список словарей: Данные о категориях.

**Вызывает исключения**:
- Любое исключение (`Exception`), если произошла ошибка.

#### Метод `set_category_products`

**Описание**: Записывает данные о продуктах в лист Google Таблицы для указанной категории.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Данные о продуктах.

**Возвращает**:
- Нет (None).

**Вызывает исключения**:
- Любое исключение (`Exception`), если произошла ошибка.


#### Метод `_format_categories_worksheet`

**Описание**: Форматирует лист с категориями.

**Параметры**:
- `ws` (Worksheet): Лист Google Таблицы.

**Возвращает**:
- Нет (None).

**Вызывает исключения**:
- Любое исключение (`Exception`), если произошла ошибка.

#### Метод `_format_category_products_worksheet`

**Описание**: Форматирует лист с продуктами категории.

**Параметры**:
- `ws` (Worksheet): Лист Google Таблицы.

**Возвращает**:
- Нет (None).

**Вызывает исключения**:
- Любое исключение (`Exception`), если произошла ошибка.