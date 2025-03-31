# Модуль `gsheets_check_this_code`

## Обзор

Модуль предназначен для работы с Google Sheets в контексте рекламных кампаний AliExpress. Он обеспечивает интеграцию с Google Sheets для чтения, записи и форматирования данных, связанных с кампаниями, категориями и продуктами.

## Подробней

Этот модуль предоставляет класс `AliCampaignGoogleSheet`, который наследуется от класса `SpreadSheet` и расширяет его функциональность для работы с данными AliExpress кампаний. Он позволяет автоматизировать процессы, такие как обновление информации о кампаниях, категориях и продуктах в Google Sheets, а также форматирование листов для удобства просмотра и анализа данных. Модуль использует библиотеки `gspread`, `gspread_formatting` и другие для взаимодействия с Google Sheets API и выполнения операций форматирования.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliCampaignGoogleSheet`.
- `clear`: Очищает содержимое листов Google Sheets.
- `delete_products_worksheets`: Удаляет все листы, кроме 'categories', 'product', 'category' и 'campaign'.
- `set_campaign_worksheet`: Записывает данные кампании в лист Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в лист Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в лист Google Sheets.
- `get_categories`: Получает данные о категориях из листа Google Sheets.
- `set_category_products`: Записывает данные о продуктах категории в лист Google Sheets.
- `_format_categories_worksheet`: Форматирует лист 'categories' в Google Sheets.
- `_format_category_products_worksheet`: Форматирует лист с продуктами категории в Google Sheets.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Примеры**
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
```

## Функции

### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
    """ Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
    @param campaign_name `str`: The name of the campaign.
    @param category_name `str`: The name of the category.   
    @param language `str`: The language for the campaign.
    @param currency `str`: The currency for the campaign.
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `AliCampaignGoogleSheet` с указанным ID таблицы Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
```

### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
    ...
```

**Описание**: Очищает содержимое листов Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при очистке листов.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
    ali_gsheet.clear()
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
    ...
```

**Описание**: Удаляет все листы из таблицы Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при удалении листов.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
    ali_gsheet.delete_products_worksheets()
```

### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace):
    """ Write campaign data to a Google Sheets worksheet.
    @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
    @param language `str`: Optional language parameter.
    @param currency `str`: Optional currency parameter.
    """
    ...
```

**Описание**: Записывает данные кампании в лист Google Sheets.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных кампании.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
    campaign_data = SimpleNamespace(name='Test Campaign', title='Test Title', language='ru', currency='RUB', description='Test Description')
    ali_gsheet.set_campaign_worksheet(campaign_data)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
    ...
```

**Описание**: Записывает данные о продуктах из списка объектов SimpleNamespace в ячейки Google Sheets.

**Параметры**:
- `category_name` (str): Название категории для получения продуктов.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных о продуктах.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
    category_name = 'TestCategory'
    ali_gsheet.set_products_worksheet(category_name)
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
    """
    ...
```

**Описание**: Записывает данные из объекта SimpleNamespace с категориями в ячейки Google Sheets.

**Параметры**:
- `categories` (SimpleNamespace): Объект, где ключи — это категории с данными для записи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении полей из объекта SimpleNamespace.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
    categories_data = SimpleNamespace()
    categories_data.category1 = SimpleNamespace(name='Category1', title='Title1', description='Description1', tags=['tag1', 'tag2'], products_count=10)
    categories_data.category2 = SimpleNamespace(name='Category2', title='Title2', description='Description2', tags=['tag3', 'tag4'], products_count=20)
    ali_gsheet.set_categories_worksheet(categories_data)
```

### `get_categories`

```python
def get_categories(self):
    """ Получение данных из таблицы Google Sheets.
    @return Данные из таблицы в виде списка словарей.
    """
    ...
```

**Описание**: Получает данные о категориях из таблицы Google Sheets.

**Возвращает**:
- Данные из таблицы в виде списка словарей.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
    categories = ali_gsheet.get_categories()
    print(categories)
```

### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict):
    """ Запись данных о продуктах в новую таблицу Google Sheets.
    @param category_name Название категории.
    @param products Словарь с данными о продуктах.
    """
    ...
```

**Описание**: Записывает данные о продуктах в новую таблицу Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении продуктов в worksheet.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
    category_name = 'TestCategory'
    products_data = [{'product_id': '123', 'app_sale_price': '10.00', 'original_price': '12.00', 'sale_price': '11.00', 'discount': '10%', 'product_title': 'Test Product'}]
    ali_gsheet.set_category_products(category_name, products_data)
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """ Форматирование листа 'categories'.
    @param ws Лист Google Sheets для форматирования.
    """
    ...
```

**Описание**: Форматирует лист 'categories' в Google Sheets.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа categories.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
    ws = ali_gsheet.get_worksheet('categories')
    ali_gsheet._format_categories_worksheet(ws)
```

### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
    """ Форматирование листа с продуктами категории.
    @param ws Лист Google Sheets для форматирования.
    """
    ...
```

**Описание**: Форматирует лист с продуктами категории в Google Sheets.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа products.

**Примеры**:
```python
    campaign_name = 'test_campaign'
    language = 'ru'
    currency = 'RUB'
    ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
    ws = ali_gsheet.get_worksheet('product')
    ali_gsheet._format_category_products_worksheet(ws)