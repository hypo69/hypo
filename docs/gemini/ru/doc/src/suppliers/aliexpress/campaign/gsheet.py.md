# Модуль `aliexpress.campaign.gsheet`

## Обзор

Модуль `aliexpress.campaign.gsheet` предоставляет класс `AliCampaignGoogleSheet` для работы с Google Sheets в рамках рекламных кампаний AliExpress. Класс наследует функциональность из `SpreadSheet` и добавляет методы для управления листами, записи данных о категориях и продуктах, а также форматирования листов.

## Оглавление

1. [Классы](#Классы)
   - [`AliCampaignGoogleSheet`](#AliCampaignGoogleSheet)
2. [Функции](#Функции)
   - [`clear`](#clear)
   - [`delete_products_worksheets`](#delete_products_worksheets)
   - [`set_campaign_worksheet`](#set_campaign_worksheet)
   - [`set_products_worksheet`](#set_products_worksheet)
   - [`set_categories_worksheet`](#set_categories_worksheet)
   - [`get_categories`](#get_categories)
   - [`set_category_products`](#set_category_products)
   - [`_format_categories_worksheet`](#_format_categories_worksheet)
   - [`_format_category_products_worksheet`](#_format_category_products_worksheet)

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress. Наследует класс `SpreadSheet` и предоставляет дополнительные методы для управления листами Google Sheets, записи данных о категориях и продуктах, и форматирования листов.

**Методы**:

- `__init__`: Инициализирует `AliCampaignGoogleSheet` с указанным идентификатором Google Sheets и дополнительными параметрами.
- `clear`: Очищает содержимое, удаляет листы продуктов и очищает данные на листах категорий.
- `delete_products_worksheets`: Удаляет все листы из таблицы Google Sheets, кроме 'categories', 'product', 'category', 'campaign'.
- `set_campaign_worksheet`: Записывает данные кампании в лист Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в лист Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в лист Google Sheets.
- `get_categories`: Получает данные из листа 'categories' Google Sheets.
- `set_category_products`: Записывает данные о продуктах в новый лист Google Sheets.
- `_format_categories_worksheet`: Форматирует лист 'categories'.
- `_format_category_products_worksheet`: Форматирует лист с продуктами категории.

## Функции

### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None) -> None:
    """
    Args:
        campaign_name (str): Название кампании.
        language (str | dict, optional): Язык кампании. По умолчанию `None`.
        currency (str, optional): Валюта кампании. По умолчанию `None`.

    Returns:
        None: 
    """
```

**Описание**: Инициализирует объект `AliCampaignGoogleSheet` с указанным идентификатором Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык для кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта для кампании. По умолчанию `None`.

**Возвращает**:
- `None`

### `clear`

```python
def clear(self) -> None:
    """
    Args:
        None:

    Returns:
        None:

    Raises:
        Exception: Если произошла ошибка при очистке листов.
    """
```

**Описание**: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при очистке листов.

### `delete_products_worksheets`

```python
def delete_products_worksheets(self) -> None:
    """
    Args:
        None:

    Returns:
        None:

    Raises:
        Exception: Если произошла ошибка при удалении листов.
    """
```

**Описание**: Удаляет все листы из Google Sheets, кроме 'categories', 'product', 'category', 'campaign'.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при удалении листов.

### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace) -> None:
    """
    Args:
        campaign (SimpleNamespace): Объект SimpleNamespace с данными кампании.

    Returns:
        None:

    Raises:
         Exception: Если произошла ошибка при записи данных в лист 'campaign'.
    """
```

**Описание**: Записывает данные кампании в лист Google Sheets под названием 'campaign'.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace, содержащий данные кампании.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных в лист 'campaign'.

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str) -> None:
    """
    Args:
        category_name (str): Имя категории для получения продуктов.

    Returns:
        None:

    Raises:
        Exception: Если произошла ошибка при записи данных в лист продуктов.
    """
```

**Описание**: Записывает данные о продуктах из указанной категории в лист Google Sheets.

**Параметры**:
- `category_name` (str): Название категории для получения продуктов.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных в лист продуктов.

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace) -> None:
    """
    Args:
        categories (SimpleNamespace): Объект SimpleNamespace с данными о категориях.

    Returns:
         None:

    Raises:
         Exception: Если возникла ошибка при записи данных о категориях в лист.
    """
```

**Описание**: Записывает данные о категориях из объекта `SimpleNamespace` в лист Google Sheets 'categories'.

**Параметры**:
- `categories` (SimpleNamespace): Объект `SimpleNamespace`, где ключи — это категории с данными для записи.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных о категориях в лист.

### `get_categories`

```python
def get_categories(self) -> List[Dict[str, Any]]:
    """
    Args:
        None:

    Returns:
        List[Dict[str, Any]]: Данные из таблицы в виде списка словарей.
    """
```

**Описание**: Получает данные из листа 'categories' Google Sheets.

**Параметры**:
- `None`

**Возвращает**:
- `List[Dict[str, Any]]`: Данные из таблицы в виде списка словарей.

### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict) -> None:
    """
    Args:
        category_name (str): Название категории.
        products (dict): Словарь с данными о продуктах.

    Returns:
        None:
    
    Raises:
         Exception: Если возникла ошибка при обновлении продуктов в листе.
    """
```

**Описание**: Записывает данные о продуктах в новый лист Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении продуктов в листе.

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet) -> None:
    """
    Args:
        ws (Worksheet): Лист Google Sheets для форматирования.

    Returns:
        None:

    Raises:
        Exception: Если возникла ошибка при форматировании листа 'categories'.
    """
```

**Описание**: Форматирует лист 'categories' в Google Sheets.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа 'categories'.

### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet) -> None:
    """
    Args:
        ws (Worksheet): Лист Google Sheets для форматирования.

    Returns:
        None:

    Raises:
        Exception: Если возникла ошибка при форматировании листа продуктов категории.
    """
```

**Описание**: Форматирует лист с продуктами категории в Google Sheets.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа продуктов категории.