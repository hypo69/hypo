# Модуль `gsheets_check_this_code`

## Обзор

Модуль предназначен для работы с Google Sheets в контексте управления рекламными кампаниями на AliExpress. Он предоставляет функциональность для создания, редактирования и форматирования таблиц Google Sheets, используемых для хранения и управления данными о кампаниях, категориях и продуктах. Модуль включает классы для взаимодействия с Google Sheets API, управления данными и интеграции с другими компонентами системы, такими как драйверы веб-браузеров и инструменты для работы с данными AliExpress.

## Подробней

Модуль `gsheets_check_this_code.py` является частью проекта `hypotez` и предназначен для автоматизации работы с Google Sheets при управлении рекламными кампаниями на AliExpress. Он обеспечивает интеграцию с Google Sheets API для создания, редактирования и форматирования таблиц, используемых для хранения данных о кампаниях, категориях и продуктах.

Основная задача модуля - упростить процесс управления рекламными кампаниями, предоставляя инструменты для автоматической записи и обновления данных в Google Sheets, а также для извлечения информации из таблиц для дальнейшей обработки. Модуль включает классы для взаимодействия с Google Sheets API, управления данными и интеграции с другими компонентами системы, такими как драйверы веб-браузеров и инструменты для работы с данными AliExpress.

Модуль использует следующие основные компоненты:

- `AliCampaignGoogleSheet`: Класс для работы с Google Sheets в рамках кампаний AliExpress.
- `SpreadSheet`: Класс для взаимодействия с Google Sheets API.
- `Worksheet`: Класс для работы с отдельными листами Google Sheets.
- `Driver`: Класс для управления веб-браузером.
- `AliCampaignEditor`: Класс для редактирования рекламных кампаний AliExpress.
- `logger`: Модуль для логирования событий и ошибок.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress. Наследует класс `SpreadSheet` и предоставляет дополнительные методы для управления листами Google Sheets, записи данных о категориях и продуктах, и форматирования листов.

**Как работает класс**:
- Инициализируется с указанием имени кампании, языка и валюты.
- Использует `AliCampaignEditor` для управления данными кампании.
- Предоставляет методы для очистки листов, удаления листов продуктов, записи данных о кампаниях, категориях и продуктах в листы Google Sheets.
- Форматирует листы для улучшения читаемости и удобства использования.

**Методы**:
- `__init__`: Инициализирует класс `AliCampaignGoogleSheet`.
- `clear`: Очищает содержимое листов.
- `delete_products_worksheets`: Удаляет все листы, кроме 'categories', 'product', 'category', 'campaign'.
- `set_campaign_worksheet`: Записывает данные кампании на лист 'campaign'.
- `set_products_worksheet`: Записывает данные о продуктах на лист категории.
- `set_categories_worksheet`: Записывает данные о категориях на лист 'categories'.
- `get_categories`: Получает данные о категориях из листа 'categories'.
- `set_category_products`: Записывает данные о продуктах категории на лист.
- `_format_categories_worksheet`: Форматирует лист 'categories'.
- `_format_category_products_worksheet`: Форматирует лист с продуктами категории.

#### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
    """Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
    @param campaign_name `str`: The name of the campaign.
    @param category_name `str`: The name of the category.   
    @param language `str`: The language for the campaign.
    @param currency `str`: The currency for the campaign.
    """
```

**Описание**: Инициализирует класс `AliCampaignGoogleSheet` с указанным ID таблицы Google Sheets и дополнительными параметрами.

**Как работает функция**:
- Инициализирует класс `SpreadSheet` с указанным `spreadsheet_id`.
- Создает экземпляр класса `AliCampaignEditor` для редактирования кампании.
- Очищает листы Google Sheets.
- Устанавливает листы для кампании и категорий.
- Открывает таблицу Google Sheets в браузере.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='ru', currency='USD')
```

#### `clear`

```python
def clear(self):
    """Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
```

**Описание**: Очищает содержимое листов. Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.

**Как работает функция**:
- Пытается удалить листы продуктов с помощью метода `delete_products_worksheets`.
- Ловит исключения, возникшие в процессе удаления листов, и логирует ошибки.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
campaign_sheet.clear()
```

#### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
```

**Описание**: Удаляет все листы из таблицы Google Sheets, кроме 'categories', 'product', 'category', 'campaign'.

**Как работает функция**:
- Получает список всех листов в таблице.
- Итерируется по листам и удаляет те, которые не входят в список исключений.
- Логирует успешное удаление каждого листа.
- В случае ошибки логирует ошибку и поднимает исключение.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при удалении листов.

**Примеры**:
```python
campaign_sheet.delete_products_worksheets()
```

#### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace):
    """Write campaign data to a Google Sheets worksheet.
    @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
    @param language `str`: Optional language parameter.
    @param currency `str`: Optional currency parameter.
    """
```

**Описание**: Записывает данные кампании на лист Google Sheets.

**Как работает функция**:
- Получает лист 'campaign'.
- Подготавливает данные для записи в вертикальном формате.
- Записывает данные в ячейки листа.
- Логирует успешную запись данных.
- В случае ошибки логирует ошибку и поднимает исключение.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных на лист.

**Примеры**:
```python
campaign_data = SimpleNamespace(name='test_campaign', title='Test Campaign', language='ru', currency='USD', description='Test description')
campaign_sheet.set_campaign_worksheet(campaign_data)
```

#### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
    """Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
```

**Описание**: Записывает данные о продуктах из списка объектов `SimpleNamespace` в ячейки Google Sheets.

**Как работает функция**:
- Получает категорию и список продуктов из `AliCampaignEditor`.
- Копирует лист 'product' и переименовывает его в название категории.
- Записывает данные о продуктах в ячейки листа.
- Форматирует лист с продуктами.
- Логирует успешную запись данных.
- В случае ошибки логирует ошибку и поднимает исключение.

**Параметры**:
- `category_name` (str): Название категории для получения продуктов.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных на лист.

**Примеры**:
```python
campaign_sheet.set_products_worksheet(category_name='test_category')
```

#### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
    """
```

**Описание**: Записывает данные из объекта `SimpleNamespace` с категориями в ячейки Google Sheets.

**Как работает функция**:
- Получает лист 'categories'.
- Очищает лист.
- Получает данные о категориях из объекта `SimpleNamespace`.
- Записывает заголовки таблицы.
- Записывает данные о категориях в ячейки листа.
- Форматирует лист с категориями.
- Логирует успешную запись данных.
- В случае ошибки логирует ошибку и поднимает исключение.

**Параметры**:
- `categories` (SimpleNamespace): Объект, где ключи — это категории с данными для записи.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных на лист.

**Примеры**:
```python
categories_data = SimpleNamespace(category1=SimpleNamespace(name='cat1', title='Category 1', description='Description 1', tags=['tag1', 'tag2'], products_count=10), category2=SimpleNamespace(name='cat2', title='Category 2', description='Description 2', tags=['tag3', 'tag4'], products_count=20))
campaign_sheet.set_categories_worksheet(categories_data)
```

#### `get_categories`

```python
def get_categories(self):
    """Получение данных из таблицы Google Sheets.
    @return Данные из таблицы в виде списка словарей.
    """
```

**Описание**: Получает данные из таблицы Google Sheets.

**Как работает функция**:
- Получает лист 'categories'.
- Получает все записи из листа.
- Логирует успешное получение данных.
- Возвращает данные в виде списка словарей.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `list[dict]`: Данные из таблицы в виде списка словарей.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
categories = campaign_sheet.get_categories()
print(categories)
```

#### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict):
    """Запись данных о продуктах в новую таблицу Google Sheets.
    @param category_name Название категории.
    @param products Словарь с данными о продуктах.
    """
```

**Описание**: Запись данных о продуктах в новую таблицу Google Sheets.

**Как работает функция**:
- Получает категорию и список продуктов из `AliCampaignEditor`.
- Копирует лист 'product' и переименовывает его в название категории.
- Записывает заголовки таблицы.
- Записывает данные о продуктах в ячейки листа.
- Форматирует лист с продуктами.
- Логирует успешную запись данных.
- В случае ошибки логирует ошибку и поднимает исключение.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных на лист.

**Примеры**:
```python
products_data = [{'product_id': '123', 'app_sale_price': '10.00', 'original_price': '15.00', 'sale_price': '12.00', 'discount': '20%', 'product_main_image_url': 'http://example.com/image.jpg', 'local_image_path': '/path/to/image.jpg', 'product_small_image_urls': [], 'product_video_url': 'http://example.com/video.mp4', 'local_video_path': '/path/to/video.mp4', 'first_level_category_id': '1', 'first_level_category_name': 'Category 1', 'second_level_category_id': '2', 'second_level_category_name': 'Category 2', 'target_sale_price': '11.00', 'target_sale_price_currency': 'USD', 'target_app_sale_price_currency': 'USD', 'target_original_price_currency': 'USD', 'original_price_currency': 'USD', 'product_title': 'Product Title', 'evaluate_rate': '4.5', 'promotion_link': 'http://example.com/promotion', 'shop_url': 'http://example.com/shop', 'shop_id': '12345', 'tags': []}]
campaign_sheet.set_category_products(category_name='test_category', products=products_data)
```

#### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """Форматирование листа 'categories'.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Описание**: Форматирование листа 'categories'.

**Как работает функция**:
- Устанавливает ширину столбцов.
- Устанавливает высоту строк.
- Форматирует заголовки.
- Логирует успешное форматирование листа.
- В случае ошибки логирует ошибку и поднимает исключение.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа.

**Примеры**:
```python
ws = campaign_sheet.get_worksheet('categories')
campaign_sheet._format_categories_worksheet(ws)
```

#### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
    """Форматирование листа с продуктами категории.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Описание**: Форматирование листа с продуктами категории.

**Как работает функция**:
- Устанавливает ширину столбцов.
- Устанавливает высоту строк.
- Форматирует заголовки.
- Логирует успешное форматирование листа.
- В случае ошибки логирует ошибку и поднимает исключение.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при форматировании листа.

**Примеры**:
```python
ws = campaign_sheet.get_worksheet('test_category')
campaign_sheet._format_category_products_worksheet(ws)
```