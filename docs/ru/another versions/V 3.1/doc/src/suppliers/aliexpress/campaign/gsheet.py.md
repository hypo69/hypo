# Модуль `aliexpress.campaign.gsheet`

## Обзор

Модуль `aliexpress.campaign.gsheet` предназначен для работы с Google Sheets в контексте управления рекламными кампаниями AliExpress. Он предоставляет функциональность для создания, редактирования и форматирования листов Google Sheets, содержащих информацию о категориях и продуктах.

## Подробней

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с Google Sheets для управления данными рекламных кампаний AliExpress. Он использует библиотеку `gspread` для взаимодействия с Google Sheets API и предоставляет удобные методы для записи и чтения данных, а также для форматирования листов.
Основная цель модуля - автоматизировать процесс создания и обновления данных в Google Sheets, используемых для управления рекламными кампаниями, что упрощает работу с большими объемами данных и позволяет эффективно управлять категориями и продуктами.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс `AliCampaignGoogleSheet` предназначен для работы с Google Sheets в рамках кампаний AliExpress. Он наследует класс `SpreadSheet` и предоставляет дополнительные методы для управления листами Google Sheets, записи данных о категориях и продуктах, и форматирования листов.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliCampaignGoogleSheet`.
- `clear`: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и кампаний.
- `delete_products_worksheets`: Удаляет все листы из Google Sheets, кроме листов `'categories'`, `'product'`, `'category'` и `'campaign'`.
- `set_campaign_worksheet`: Записывает данные о кампании в Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в Google Sheets.
- `get_categories`: Получает данные о категориях из Google Sheets.
- `set_category_products`: Записывает данные о продуктах для конкретной категории в Google Sheets.
- `_format_categories_worksheet`: Форматирует лист Google Sheets с категориями.
- `_format_category_products_worksheet`: Форматирует лист Google Sheets с продуктами категории.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример очистки Google Sheets
campaign_sheet.clear()
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

**Описание**: Инициализирует экземпляр класса `AliCampaignGoogleSheet` с указанным ID Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')
```

### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
    ...
```

**Описание**: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и кампаний.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример очистки Google Sheets
campaign_sheet.clear()
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
    ...
```

**Описание**: Удаляет все листы из Google Sheets, кроме листов `'categories'`, `'product'`, `'category'` и `'campaign'`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при удалении листов.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример удаления листов продуктов
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
    ...
```

**Описание**: Записывает данные о кампании в Google Sheets.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных о кампании.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from types import SimpleNamespace

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример создания объекта SimpleNamespace с данными кампании
campaign_data = SimpleNamespace(
    campaign_name='test_campaign',
    title='Test Campaign Title',
    language='en',
    currency='USD',
    description='Test Campaign Description'
)

# Пример записи данных о кампании в Google Sheets
campaign_sheet.set_campaign_worksheet(campaign_data)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
    ...
```

**Описание**: Записывает данные о продуктах в Google Sheets.

**Параметры**:
- `category_name` (str): Имя категории, для которой нужно получить продукты.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных о продуктах.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример записи данных о продуктах в Google Sheets
campaign_sheet.set_products_worksheet(category_name='test_category')
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
    """
    ...
```

**Описание**: Записывает данные о категориях в Google Sheets.

**Параметры**:
- `categories` (SimpleNamespace): Объект SimpleNamespace, содержащий данные о категориях.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных о категориях.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from types import SimpleNamespace

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример создания объекта SimpleNamespace с данными о категориях
categories_data = SimpleNamespace(
    category1=SimpleNamespace(
        name='category1',
        title='Category 1 Title',
        description='Category 1 Description',
        tags=['tag1', 'tag2'],
        products_count=10
    ),
    category2=SimpleNamespace(
        name='category2',
        title='Category 2 Title',
        description='Category 2 Description',
        tags=['tag3', 'tag4'],
        products_count=20
    )
)

# Пример записи данных о категориях в Google Sheets
campaign_sheet.set_categories_worksheet(categories_data)
```

### `get_categories`

```python
def get_categories(self):
    """ Получение данных из таблицы Google Sheets.
    @return Данные из таблицы в виде списка словарей.
    """
    ...
```

**Описание**: Получает данные о категориях из Google Sheets.

**Возвращает**:
- (list[dict]): Данные о категориях в виде списка словарей.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример получения данных о категориях из Google Sheets
categories_data = campaign_sheet.get_categories()
print(categories_data)
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

**Описание**: Записывает данные о продуктах для конкретной категории в Google Sheets.

**Параметры**:
- `category_name` (str): Имя категории.
- `products` (dict): Словарь с данными о продуктах.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример записи данных о продуктах для категории в Google Sheets
products_data = [
    {'product_id': '1', 'product_title': 'Product 1'},
    {'product_id': '2', 'product_title': 'Product 2'}
]
campaign_sheet.set_category_products(category_name='test_category', products=products_data)
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """ Форматирование листа 'categories'.
    @param ws Лист Google Sheets для форматирования.
    """
    ...
```

**Описание**: Форматирует лист Google Sheets с категориями.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from gspread.worksheet import Worksheet

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример получения листа Google Sheets
ws: Worksheet = campaign_sheet.get_worksheet('categories')

# Пример форматирования листа категорий
campaign_sheet._format_categories_worksheet(ws)
```

### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
    """ Форматирование листа с продуктами категории.
    @param ws Лист Google Sheets для форматирования.
    """
    ...
```

**Описание**: Форматирует лист Google Sheets с продуктами категории.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from gspread.worksheet import Worksheet

# Пример инициализации класса
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

# Пример получения листа Google Sheets
ws: Worksheet = campaign_sheet.get_worksheet('products')

# Пример форматирования листа продуктов категории
campaign_sheet._format_category_products_worksheet(ws)
```