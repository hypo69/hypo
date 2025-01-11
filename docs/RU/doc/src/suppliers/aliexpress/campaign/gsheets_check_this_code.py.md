# Модуль `gsheets_check_this_code`

## Обзор

Модуль `gsheets_check_this_code.py` предназначен для работы с Google Sheets в контексте управления рекламными кампаниями AliExpress. Он предоставляет функциональность для создания, редактирования и форматирования данных в Google Sheets, связанных с кампаниями, категориями и продуктами.

## Оглавление

- [Классы](#классы)
    - [`AliCampaignGoogleSheet`](#ali campaigngooglesheet)
- [Функции](#функции)

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress.

Наследует класс `SpreadSheet` и предоставляет дополнительные методы для управления листами Google Sheets, записи данных о категориях и продуктах, и форматирования листов.

**Методы**:
- [`__init__`](#__init__)
- [`clear`](#clear)
- [`delete_products_worksheets`](#delete_products_worksheets)
- [`set_campaign_worksheet`](#set_campaign_worksheet)
- [`set_products_worksheet`](#set_products_worksheet)
- [`set_categories_worksheet`](#set_categories_worksheet)
- [`get_categories`](#get_categories)
- [`set_category_products`](#set_category_products)
- [`_format_categories_worksheet`](#_format_categories_worksheet)
- [`_format_category_products_worksheet`](#_format_category_products_worksheet)


#### `__init__`

**Описание**: Initialize `AliCampaignGoogleSheet` with specified Google Sheets spreadsheet ID and additional parameters.

**Параметры**:
- `campaign_name` (str): The name of the campaign.
- `language` (str | dict, optional): The language for the campaign.
- `currency` (str, optional): The currency for the campaign.

#### `clear`

**Описание**: Clear contents. Delete product sheets and clear data on the categories and other specified sheets.

**Вызывает исключения**:
- `Exception`: Ошибка при очистке.

#### `delete_products_worksheets`

**Описание**: Delete all sheets from the Google Sheets spreadsheet except 'categories', 'product', 'category', 'campaign'.

**Вызывает исключения**:
- `Exception`: Ошибка при удалении листов.

#### `set_campaign_worksheet`

**Описание**: Write campaign data to a Google Sheets worksheet.

**Параметры**:
- `campaign` (`SimpleNamespace`): SimpleNamespace object with campaign data fields for writing.

**Вызывает исключения**:
- `Exception`: Ошибка при записи данных о кампании.

#### `set_products_worksheet`

**Описание**: Write data from a list of SimpleNamespace objects to Google Sheets cells.

**Параметры**:
- `category_name` (str): The name of the category to fetch products from.

**Вызывает исключения**:
- `Exception`: Ошибка при записи данных о продуктах.

#### `set_categories_worksheet`

**Описание**: Запись данных из объекта `SimpleNamespace` с категориями в ячейки Google Sheets.

**Параметры**:
- `categories` (`SimpleNamespace`): Объект, где ключи — это категории с данными для записи.

**Вызывает исключения**:
- `Exception`: Ошибка при обновлении полей из объекта `SimpleNamespace`.

#### `get_categories`

**Описание**: Получение данных из таблицы Google Sheets.

**Возвращает**:
- `list[dict]`: Данные из таблицы в виде списка словарей.

#### `set_category_products`

**Описание**: Запись данных о продуктах в новую таблицу Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Вызывает исключения**:
- `Exception`: Ошибка при обновлении продуктов в таблице.

#### `_format_categories_worksheet`

**Описание**: Форматирование листа 'categories'.

**Параметры**:
- `ws` (`Worksheet`): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Ошибка при форматировании листа категорий.

#### `_format_category_products_worksheet`

**Описание**: Форматирование листа с продуктами категории.

**Параметры**:
- `ws` (`Worksheet`): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Ошибка при форматировании листа с продуктами категории.

## Функции

В данном модуле отсутствуют отдельные функции вне класса.