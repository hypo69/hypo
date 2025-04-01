# Модуль `src.suppliers.aliexpress.campaign.gsheet`

## Обзор

Модуль `src.suppliers.aliexpress.campaign.gsheet` предоставляет класс `AliCampaignGoogleSheet` для работы с Google Sheets в рамках рекламных кампаний AliExpress. Он позволяет управлять листами Google Sheets, записывать данные о категориях и продуктах, а также форматировать листы.

## Оглавление

1.  [Классы](#классы)
    -   [`AliCampaignGoogleSheet`](#alicampaigngooglesheet)
2.  [Функции](#функции)
    -   [`__init__`](#__init__)
    -   [`clear`](#clear)
    -   [`delete_products_worksheets`](#delete_products_worksheets)
    -   [`set_campaign_worksheet`](#set_campaign_worksheet)
    -   [`set_products_worksheet`](#set_products_worksheet)
    -  [`set_categories_worksheet`](#set_categories_worksheet)
    -   [`get_categories`](#get_categories)
    -   [`set_category_products`](#set_category_products)
    -   [`_format_categories_worksheet`](#_format_categories_worksheet)
    -   [`_format_category_products_worksheet`](#_format_category_products_worksheet)

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress.
Наследует класс `SpreadSheet` и предоставляет дополнительные методы для управления листами Google Sheets, записи данных о категориях и продуктах, и форматирования листов.

**Методы**:
- [`__init__`](#__init__): Инициализирует объект класса `AliCampaignGoogleSheet`.
- [`clear`](#clear): Очищает содержимое листов Google Sheets.
- [`delete_products_worksheets`](#delete_products_worksheets): Удаляет все листы, кроме 'categories', 'product', 'category' и 'campaign'.
- [`set_campaign_worksheet`](#set_campaign_worksheet): Записывает данные кампании на лист 'campaign'.
- [`set_products_worksheet`](#set_products_worksheet): Записывает данные о продуктах категории на отдельный лист.
- [`set_categories_worksheet`](#set_categories_worksheet): Записывает данные о категориях на лист 'categories'.
- [`get_categories`](#get_categories): Получает данные о категориях с листа 'categories'.
- [`set_category_products`](#set_category_products): Записывает данные о продуктах категории на отдельный лист.
- [`_format_categories_worksheet`](#_format_categories_worksheet): Форматирует лист 'categories'.
- [`_format_category_products_worksheet`](#_format_category_products_worksheet): Форматирует лист с продуктами категории.

## Функции

### `__init__`

**Описание**: Инициализирует объект класса `AliCampaignGoogleSheet`.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`

### `clear`

**Описание**: Очищает содержимое листов Google Sheets.
Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Возникает при ошибке очистки.

### `delete_products_worksheets`

**Описание**: Удаляет все листы из Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Возникает при ошибке удаления листов.

### `set_campaign_worksheet`

**Описание**: Записывает данные кампании в Google Sheets на лист 'campaign'.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании для записи.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Возникает при ошибке записи данных на лист.

### `set_products_worksheet`

**Описание**: Записывает данные о продуктах из списка объектов `SimpleNamespace` в ячейки Google Sheets.

**Параметры**:
- `category_name` (str): Название категории, товары которой будут записаны.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Возникает при ошибке записи данных на лист.

### `set_categories_worksheet`

**Описание**: Запись данных из объекта `SimpleNamespace` с категориями в ячейки Google Sheets.

**Параметры**:
- `categories` (SimpleNamespace): Объект, где ключи — это категории с данными для записи.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Возникает при ошибке записи данных на лист.

### `get_categories`

**Описание**: Получение данных из таблицы Google Sheets.

**Параметры**:
- `None`

**Возвращает**:
- `list[dict]`: Данные из таблицы в виде списка словарей.

**Вызывает исключения**:
- `None`

### `set_category_products`

**Описание**: Запись данных о продуктах в новую таблицу Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Возникает при ошибке записи данных на лист.

### `_format_categories_worksheet`

**Описание**: Форматирование листа 'categories'.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Возникает при ошибке форматирования листа.

### `_format_category_products_worksheet`

**Описание**: Форматирование листа с продуктами категории.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Возникает при ошибке форматирования листа.