# src.suppliers.aliexpress.campaign.gsheets_check_this_code

## Обзор

Модуль `src.suppliers.aliexpress.campaign.gsheets_check_this_code` предназначен для редактирования рекламных кампаний AliExpress с использованием Google Sheets. Он обеспечивает интеграцию между данными кампаний, представленными в Google Sheets, и системой управления рекламными кампаниями AliExpress.

## Подробней

Этот модуль позволяет автоматизировать процесс обновления и управления данными рекламных кампаний, такими как названия, описания, ключевые слова и информация о продуктах, непосредственно из Google Sheets. Это упрощает внесение изменений и обеспечивает централизованное управление данными кампаний. Модуль включает в себя классы и функции для чтения, записи и форматирования данных в Google Sheets, а также для взаимодействия с API AliExpress для применения изменений. Расположение файла в структуре проекта указывает на его роль в качестве компонента, связывающего внешние данные (Google Sheets) с логикой управления кампаниями AliExpress.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliCampaignGoogleSheet`.
- `clear`: Очищает содержимое листов Google Sheets.
- `delete_products_worksheets`: Удаляет все листы продуктов из Google Sheets, кроме основных.
- `set_campaign_worksheet`: Записывает данные кампании в лист Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в лист Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в лист Google Sheets.
- `get_categories`: Получает данные о категориях из Google Sheets.
- `set_category_products`: Записывает данные о продуктах для определенной категории в Google Sheets.
- `_format_categories_worksheet`: Форматирует лист с категориями в Google Sheets.
- `_format_category_products_worksheet`: Форматирует лист с продуктами категории в Google Sheets.

**Параметры**:
- `spreadsheet_id` (str): Идентификатор Google Sheets.
- `spreadsheet` (SpreadSheet): Экземпляр класса `SpreadSheet` для работы с Google Sheets.
- `worksheet` (Worksheet): Экземпляр класса `Worksheet` для работы с листом Google Sheets.
- `driver` (Driver): Экземпляр класса `Driver` для управления веб-браузером.
- `campaign_name` (str): Название кампании.
- `language` (str | dict): Язык кампании.
- `currency` (str): Валюта кампании.

**Примеры**
```python
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet

campaign_name = 'test_campaign'
language = 'ru'
currency = 'USD'

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
```

**Описание**: Инициализирует экземпляр класса `AliCampaignGoogleSheet` с указанным ID Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при инициализации.

**Примеры**:
```python
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet
campaign_name = 'test_campaign'
language = 'ru'
currency = 'USD'

ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
```

### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
```

**Описание**: Очищает содержимое листов Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при очистке листов.

**Примеры**:
```python
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet
campaign_name = 'test_campaign'
language = 'ru'
currency = 'USD'

ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
ali_gsheet.clear()
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ Delete all sheets from the Google Sheets spreadsheet except \'categories\' and \'product_template\'.
    """
```

**Описание**: Удаляет все листы из Google Sheets, кроме листов 'categories', 'product' , 'category', 'campaign'.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при удалении листов.

**Примеры**:
```python
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet
campaign_name = 'test_campaign'
language = 'ru'
currency = 'USD'

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
```

**Описание**: Записывает данные кампании в лист Google Sheets.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании для записи.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных кампании.

**Примеры**:
```python
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet
from types import SimpleNamespace

campaign_name = 'test_campaign'
language = 'ru'
currency = 'USD'

ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)

campaign_data = SimpleNamespace(
    name='Test Campaign',
    title='Test Title',
    language='English',
    currency='USD',
    description='Test Description'
)

ali_gsheet.set_campaign_worksheet(campaign_data)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
```

**Описание**: Записывает данные о продуктах из списка объектов SimpleNamespace в ячейки Google Sheets.

**Параметры**:
- `category_name` (str): Название категории, из которой выбираются продукты.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных о продуктах.

**Примеры**:
```python
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet

campaign_name = 'test_campaign'
language = 'ru'
currency = 'USD'
category_name = 'example_category'

ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
ali_gsheet.set_products_worksheet(category_name)
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

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при обновлении полей из объекта SimpleNamespace.

**Примеры**:
```python
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet
from types import SimpleNamespace

campaign_name = 'test_campaign'
language = 'ru'
currency = 'USD'

ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)

categories_data = SimpleNamespace()
categories_data.category1 = SimpleNamespace(name='Category 1', title='Title 1', description='Description 1', tags=['tag1', 'tag2'], products_count=10)
categories_data.category2 = SimpleNamespace(name='Category 2', title='Title 2', description='Description 2', tags=['tag3', 'tag4'], products_count=20)

ali_gsheet.set_categories_worksheet(categories_data)
```

### `get_categories`

```python
def get_categories(self):
    """ Получение данных из таблицы Google Sheets.
    @return Данные из таблицы в виде списка словарей.
    """
```

**Описание**: Получает данные из таблицы Google Sheets.

**Параметры**:
- `None`

**Возвращает**:
- Данные из таблицы в виде списка словарей.

**Вызывает исключения**:
- `None`

**Примеры**:
```python
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet

campaign_name = 'test_campaign'
language = 'ru'
currency = 'USD'

ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
categories_data = ali_gsheet.get_categories()
```

### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict):
    """ Запись данных о продуктах в новую таблицу Google Sheets.
    @param category_name Название категории.
    @param products Словарь с данными о продуктах.
    """
```

**Описание**: Запись данных о продуктах в новую таблицу Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при обновлении продуктов в таблице.

**Примеры**:
```python
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet

campaign_name = 'test_campaign'
language = 'ru'
currency = 'USD'
category_name = 'example_category'
products_data = {'product1': {'product_id': '123', 'name': 'Product 1'}, 'product2': {'product_id': '456', 'name': 'Product 2'}}

ali_gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
ali_gsheet.set_category_products(category_name, products_data)
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """ Форматирование листа \'categories\'.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Описание**: Форматирование листа 'categories'.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при форматировании листа категорий.

**Примеры**:
```python
#  Этот метод является внутренним и обычно вызывается внутри класса.
```

### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
    """ Форматирование листа с продуктами категории.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Описание**: Форматирование листа с продуктами категории.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при форматировании листа продуктов категории.

**Примеры**:
```python
#  Этот метод является внутренним и обычно вызывается внутри класса.