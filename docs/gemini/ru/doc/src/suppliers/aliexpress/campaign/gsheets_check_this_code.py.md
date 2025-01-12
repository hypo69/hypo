# `src.suppliers.aliexpress.campaign.gsheets_check_this_code.py`

## Обзор

Модуль `src.suppliers.aliexpress.campaign.gsheets_check_this_code.py` предназначен для управления рекламными кампаниями AliExpress через Google Sheets. Он включает в себя класс `AliCampaignGoogleSheet`, который обеспечивает взаимодействие с Google Sheets, включая запись и форматирование данных о кампаниях, категориях и продуктах.

## Оглавление

- [Классы](#классы)
    - [`AliCampaignGoogleSheet`](#alicampaigngooglesheet)
- [Функции](#функции)

## Классы

### `AliCampaignGoogleSheet`

**Описание**:
Класс для работы с Google Sheets в рамках кампаний AliExpress. Наследует класс `SpreadSheet` и предоставляет дополнительные методы для управления листами Google Sheets, записи данных о категориях и продуктах, и форматирования листов.

**Методы**:
- `__init__`: Инициализирует `AliCampaignGoogleSheet` с указанным идентификатором Google Sheets и дополнительными параметрами.
- `clear`: Очищает содержимое, удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.
- `delete_products_worksheets`: Удаляет все листы из таблицы Google Sheets, кроме `'categories'`, `'product'`, `'category'` и `'campaign'`.
- `set_campaign_worksheet`: Записывает данные кампании в лист Google Sheets.
- `set_products_worksheet`: Записывает данные из списка объектов `SimpleNamespace` в ячейки Google Sheets.
- `set_categories_worksheet`: Записывает данные из объекта `SimpleNamespace` с категориями в ячейки Google Sheets.
- `get_categories`: Получает данные из таблицы Google Sheets.
- `set_category_products`: Записывает данные о продуктах в новую таблицу Google Sheets.
- `_format_categories_worksheet`: Форматирует лист `'categories'`.
- `_format_category_products_worksheet`: Форматирует лист с продуктами категории.

#### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None)
```

**Описание**: Инициализирует `AliCampaignGoogleSheet` с указанным идентификатором Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык для кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта для кампании. По умолчанию `None`.

#### `clear`

```python
def clear(self) -> None
```
**Описание**: Очищает содержимое. Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.

#### `delete_products_worksheets`

```python
def delete_products_worksheets(self) -> None
```

**Описание**:
Удаляет все листы из таблицы Google Sheets, кроме `categories`, `product`, `category` и `campaign`.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при удалении листов.

#### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace) -> None
```

**Описание**:
Записывает данные кампании в лист Google Sheets.

**Параметры**:
- `campaign` (SimpleNamespace): Объект `SimpleNamespace` с данными кампании.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при записи данных кампании.

#### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str) -> None
```

**Описание**:
Записывает данные из списка объектов `SimpleNamespace` в ячейки Google Sheets.

**Параметры**:
- `category_name` (str): Название категории, из которой необходимо получить продукты.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при записи данных о продуктах.

#### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace) -> None
```

**Описание**:
Записывает данные из объекта `SimpleNamespace` с категориями в ячейки Google Sheets.

**Параметры**:
- `categories` (SimpleNamespace): Объект `SimpleNamespace`, где ключи - это категории с данными для записи.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при записи данных о категориях.

#### `get_categories`

```python
def get_categories(self) -> List[Dict]
```

**Описание**:
Получает данные из таблицы Google Sheets.

**Возвращает**:
- `List[Dict]`: Данные из таблицы в виде списка словарей.

#### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict) -> None
```

**Описание**:
Записывает данные о продуктах в новую таблицу Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при обновлении продуктов в таблице.

#### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet) -> None
```

**Описание**:
Форматирует лист `categories`.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при форматировании листа.

#### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet) -> None
```

**Описание**:
Форматирует лист с продуктами категории.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при форматировании листа продуктов.

## Функции

В данном файле нет отдельных функций, все методы относятся к классу `AliCampaignGoogleSheet`.