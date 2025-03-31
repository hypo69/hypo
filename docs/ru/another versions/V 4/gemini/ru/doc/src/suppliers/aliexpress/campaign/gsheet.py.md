# Модуль `gsheet`

## Обзор

Модуль `gsheet` предназначен для работы с Google Sheets в контексте управления рекламными кампаниями AliExpress. Он предоставляет функциональность для чтения, записи и форматирования данных в Google Sheets, что позволяет автоматизировать процесс управления кампаниями. Модуль включает в себя классы и методы для работы с листами категорий, продуктами и данными кампаний.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с Google Sheets API, чтобы обеспечить удобный интерфейс для управления данными, связанными с рекламными кампаниями AliExpress. Он использует класс `SpreadSheet` из модуля `src.goog.spreadsheet.spreadsheet` для базовых операций с Google Sheets и расширяет его функциональность для конкретных нужд кампаний AliExpress.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс `AliCampaignGoogleSheet` расширяет класс `SpreadSheet` и предоставляет методы для управления Google Sheets, используемыми в кампаниях AliExpress. Он позволяет записывать данные о категориях и продуктах, а также форматировать листы.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliCampaignGoogleSheet`.
- `clear`: Очищает содержимое листов, связанных с продуктами и категориями.
- `delete_products_worksheets`: Удаляет все листы, кроме листов категорий, продуктов и кампаний.
- `set_campaign_worksheet`: Записывает данные кампании в лист Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в лист Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в лист Google Sheets.
- `get_categories`: Получает данные о категориях из листа Google Sheets.
- `set_category_products`: Записывает данные о продуктах для определенной категории в лист Google Sheets.
- `_format_categories_worksheet`: Форматирует лист с категориями.
- `_format_category_products_worksheet`: Форматирует лист с продуктами категории.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Примеры**
```python
    campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='ru', currency='USD')
    campaign_sheet.clear()
```

## Функции

### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
    """Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
    @param campaign_name `str`: The name of the campaign.
    @param category_name `str`: The name of the category.   
    @param language `str`: The language for the campaign.
    @param currency `str`: The currency for the campaign.
    """
```

**Описание**: Инициализирует объект `AliCampaignGoogleSheet` с указанным ID таблицы Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык для кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта для кампании. По умолчанию `None`.

**Примеры**:
```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale', language='en', currency='USD')
```

### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
```

**Описание**: Очищает содержимое, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.

**Примеры**:
```python
campaign_sheet.clear()
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
```

**Описание**: Удаляет все листы из таблицы Google Sheets, кроме листов 'categories', 'product' , 'category' и 'campaign'.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при удалении листов.

**Примеры**:
```python
campaign_sheet.delete_products_worksheets()
```

### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace):
    """ Write campaign data to a Google Sheets worksheet.
    @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
    @param language `str`: Optional language parameter.
    @param currency `str`: Optional currency parameter.
    """
```

**Описание**: Записывает данные кампании в лист Google Sheets.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании для записи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных кампании.

**Примеры**:
```python
campaign_data = SimpleNamespace(campaign_name='SummerSale', title='Летняя распродажа', language='ru', currency='RUB', description='Описание летней распродажи')
campaign_sheet.set_campaign_worksheet(campaign_data)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
```

**Описание**: Записывает данные из списка объектов SimpleNamespace в ячейки Google Sheets.

**Параметры**:
- `category_name` (str): Название категории для получения продуктов.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных о продуктах.

**Примеры**:
```python
campaign_sheet.set_products_worksheet(category_name='clothing')
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
    """
```

**Описание**: Записывает данные из объекта SimpleNamespace с категориями в ячейки Google Sheets.

**Параметры**:
- `categories` (SimpleNamespace): Объект, где ключи — это категории с данными для записи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении полей из объекта SimpleNamespace.

**Примеры**:
```python
categories_data = SimpleNamespace(
    category1=SimpleNamespace(name='clothing', title='Одежда', description='Описание одежды', tags=['fashion', 'стиль'], products_count=100),
    category2=SimpleNamespace(name='shoes', title='Обувь', description='Описание обуви', tags=['shoes', 'обувь'], products_count=50)
)
campaign_sheet.set_categories_worksheet(categories_data)
```

### `get_categories`

```python
def get_categories(self):
    """ Получение данных из таблицы Google Sheets.
    @return Данные из таблицы в виде списка словарей.
    """
```

**Описание**: Получает данные о категориях из таблицы Google Sheets.

**Возвращает**:
- `list[dict]`: Данные из таблицы в виде списка словарей.

**Примеры**:
```python
categories = campaign_sheet.get_categories()
print(categories)
```

### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict):
    """ Запись данных о продуктах в новую таблицу Google Sheets.
    @param category_name Название категории.
    @param products Словарь с данными о продуктах.
    """
```

**Описание**: Записывает данные о продуктах для определенной категории в лист Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении продуктов в таблице.

**Примеры**:
```python
products_data = [
    {'product_id': '123', 'app_sale_price': '10.00', 'original_price': '20.00', 'sale_price': '15.00', 'discount': '50%', 'product_title': 'Футболка'},
    {'product_id': '456', 'app_sale_price': '25.00', 'original_price': '50.00', 'sale_price': '37.50', 'discount': '50%', 'product_title': 'Джинсы'}
]
campaign_sheet.set_category_products(category_name='clothing', products=products_data)
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """ Форматирование листа 'categories'.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Описание**: Форматирует лист 'categories' в Google Sheets.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа категорий.

**Примеры**:
```python
ws = campaign_sheet.get_worksheet('categories')
campaign_sheet._format_categories_worksheet(ws)
```

### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
    """ Форматирование листа с продуктами категории.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Описание**: Форматирует лист с продуктами категории в Google Sheets.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа продуктов категории.

**Примеры**:
```python
ws = campaign_sheet.get_worksheet('clothing')
campaign_sheet._format_category_products_worksheet(ws)