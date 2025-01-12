# src.suppliers.chat_gpt.gsheet

## Обзор

Модуль `src.suppliers.chat_gpt.gsheet` предназначен для управления Google Sheets в контексте рекламных кампаний AliExpress. Он предоставляет функциональность для чтения и записи данных о кампаниях, категориях и продуктах в Google Sheets.

## Оглавление

1. [Классы](#Классы)
   - [`GptGs`](#GptGs)
2. [Функции](#Функции)
    - [`clear`](#clear)
    - [`update_chat_worksheet`](#update_chat_worksheet)
    - [`get_campaign_worksheet`](#get_campaign_worksheet)
    - [`set_category_worksheet`](#set_category_worksheet)
    - [`get_category_worksheet`](#get_category_worksheet)
    - [`set_categories_worksheet`](#set_categories_worksheet)
    - [`get_categories_worksheet`](#get_categories_worksheet)
    - [`set_product_worksheet`](#set_product_worksheet)
    - [`get_product_worksheet`](#get_product_worksheet)
    - [`set_products_worksheet`](#set_products_worksheet)
    - [`delete_products_worksheets`](#delete_products_worksheets)
    - [`save_categories_from_worksheet`](#save_categories_from_worksheet)
    - [`save_campaign_from_worksheet`](#save_campaign_from_worksheet)

## Классы

### `GptGs`

**Описание**:
Класс `GptGs` управляет Google Sheets в рамках рекламных кампаний AliExpress. Он наследует функциональность от `SpreadSheet` и предназначен для записи данных о категориях, продуктах и форматирования листов Google Sheets.

**Методы**:
- [`__init__`](#__init__)
- [`clear`](#clear)
- [`update_chat_worksheet`](#update_chat_worksheet)
- [`get_campaign_worksheet`](#get_campaign_worksheet)
- [`set_category_worksheet`](#set_category_worksheet)
- [`get_category_worksheet`](#get_category_worksheet)
- [`set_categories_worksheet`](#set_categories_worksheet)
- [`get_categories_worksheet`](#get_categories_worksheet)
- [`set_product_worksheet`](#set_product_worksheet)
- [`get_product_worksheet`](#get_product_worksheet)
- [`set_products_worksheet`](#set_products_worksheet)
- [`delete_products_worksheets`](#delete_products_worksheets)
- [`save_categories_from_worksheet`](#save_categories_from_worksheet)
- [`save_campaign_from_worksheet`](#save_campaign_from_worksheet)

#### `__init__`

**Описание**:
Инициализирует объект `GptGs`, устанавливая ID Google Sheets таблицы.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `category_name` (str): Название категории.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

## Функции

### `clear`

**Описание**:
Очищает содержимое Google Sheets, удаляя листы с продуктами и очищая данные на листах категорий и других указанных листах.

**Вызывает исключения**:
- `Exception`: В случае ошибки при очистке.

### `update_chat_worksheet`

**Описание**:
Записывает данные о кампании в Google Sheets worksheet.

**Параметры**:
- `data` (SimpleNamespace | dict | list): Объект SimpleNamespace или словарь, содержащий данные для записи.
- `conversation_name` (str): Название листа Google Sheets.
- `language` (str, optional): Необязательный параметр языка.

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных.

### `get_campaign_worksheet`

**Описание**:
Читает данные о кампании из листа 'campaign' и возвращает их в виде объекта SimpleNamespace.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с данными кампании.

**Вызывает исключения**:
- `ValueError`: Если лист 'campaign' не найден.
- `Exception`: В случае ошибки при чтении данных.

### `set_category_worksheet`

**Описание**:
Записывает данные о категории вертикально в Google Sheets worksheet 'category'.

**Параметры**:
- `category` (SimpleNamespace | str): Объект SimpleNamespace с данными о категории или строка.

**Вызывает исключения**:
- `TypeError`: Если передан не SimpleNamespace.
- `Exception`: В случае ошибки при записи данных.

### `get_category_worksheet`

**Описание**:
Читает данные о категории из листа 'category' и возвращает их в виде объекта SimpleNamespace.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с данными о категории.

**Вызывает исключения**:
- `ValueError`: Если лист 'category' не найден.
- `Exception`: В случае ошибки при чтении данных.

### `set_categories_worksheet`

**Описание**:
Записывает данные из объекта SimpleNamespace в Google Sheets на лист 'categories'.

**Параметры**:
- `categories` (SimpleNamespace): Объект SimpleNamespace с данными о категориях.

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных.

### `get_categories_worksheet`

**Описание**:
Читает данные из столбцов A-E, начиная со второй строки, из листа 'categories'.

**Возвращает**:
- `List[List[str]]`: Список строк с данными из столбцов A-E.

**Вызывает исключения**:
- `ValueError`: Если лист 'categories' не найден.
- `Exception`: В случае ошибки при чтении данных.

### `set_product_worksheet`

**Описание**:
Записывает данные о продукте в новый Google Sheets worksheet, созданный копированием 'product_template'.

**Параметры**:
- `product` (SimpleNamespace | str): Объект SimpleNamespace с данными о продукте.
- `category_name` (str): Название категории.

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных.

### `get_product_worksheet`

**Описание**:
Читает данные о продукте из листа 'products' и возвращает их в виде объекта SimpleNamespace.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с данными о продукте.

**Вызывает исключения**:
- `ValueError`: Если лист 'products' не найден.
- `Exception`: В случае ошибки при чтении данных.

### `set_products_worksheet`

**Описание**:
Записывает данные из списка объектов SimpleNamespace в Google Sheets worksheet.

**Параметры**:
- `category_name` (str): Название категории.

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных.

### `delete_products_worksheets`

**Описание**:
Удаляет все листы, кроме 'categories', 'product' и 'product_template' из Google Sheets.

**Вызывает исключения**:
- `Exception`: В случае ошибки при удалении листов.

### `save_categories_from_worksheet`

**Описание**:
Сохраняет данные из листа 'categories' в объект кампании.

**Параметры**:
- `update` (bool, optional): Флаг для обновления кампании, по умолчанию `False`.

### `save_campaign_from_worksheet`

**Описание**:
Сохраняет данные о кампании из листа 'campaign' и обновляет объект кампании.