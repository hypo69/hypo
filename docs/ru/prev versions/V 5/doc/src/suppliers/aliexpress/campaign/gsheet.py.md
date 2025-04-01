# Модуль для работы с Google Sheets в кампаниях AliExpress

## Обзор

Модуль `gsheet.py` предназначен для интеграции с Google Sheets для управления рекламными кампаниями AliExpress. Он предоставляет класс `AliCampaignGoogleSheet`, который наследует функциональность из класса `SpreadSheet` и добавляет методы для работы с данными кампаний, категориями и продуктами, хранящимися в Google Sheets. Модуль позволяет автоматизировать чтение, запись и форматирование данных в Google Sheets, что упрощает управление рекламными кампаниями.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации работы с Google Sheets в рамках рекламных кампаний AliExpress. Он предоставляет инструменты для чтения и записи данных о кампаниях, категориях и продуктах, а также для форматирования листов Google Sheets.

Класс `AliCampaignGoogleSheet` наследует класс `SpreadSheet` и добавляет специфические методы для работы с данными рекламных кампаний. Он использует библиотеку `gspread` для взаимодействия с Google Sheets API.

Основные функции модуля:

- Чтение данных о категориях и продуктах из Google Sheets.
- Запись данных о кампаниях, категориях и продуктах в Google Sheets.
- Форматирование листов Google Sheets для улучшения читаемости и организации данных.
- Удаление листов продуктов из Google Sheets.

Модуль использует модуль `logger` для логирования событий и ошибок, что помогает в отладке и мониторинге работы модуля.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress.

**Как работает класс**:
1.  **Инициализация**: При инициализации класса `AliCampaignGoogleSheet` происходит инициализация родительского класса `SpreadSheet` с указанием `spreadsheet_id`. Также можно передать параметры `campaign_name`, `language` и `currency`, которые будут использоваться для работы с данными кампании.
2.  **Удаление листов продуктов**: Метод `delete_products_worksheets` удаляет все листы из Google Sheets, кроме листов 'categories', 'product', 'category' и 'campaign'.
3.  **Запись данных кампании**: Метод `set_campaign_worksheet` записывает данные о кампании в лист 'campaign' Google Sheets.
4.  **Запись данных о продуктах**: Метод `set_products_worksheet` записывает данные о продуктах в лист Google Sheets, созданный на основе шаблона 'product'.
5.  **Запись данных о категориях**: Метод `set_categories_worksheet` записывает данные о категориях в лист 'categories' Google Sheets.
6.  **Получение данных о категориях**: Метод `get_categories` получает данные о категориях из листа 'categories' Google Sheets.
7.  **Форматирование листов**: Методы `_format_categories_worksheet` и `_format_category_products_worksheet` форматируют листы Google Sheets для улучшения читаемости и организации данных.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `AliCampaignGoogleSheet`.
- `clear`: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на других листах.
- `delete_products_worksheets`: Удаляет все листы продуктов из Google Sheets.
- `set_campaign_worksheet`: Записывает данные о кампании в лист 'campaign' Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в лист Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в лист 'categories' Google Sheets.
- `get_categories`: Получает данные о категориях из листа 'categories' Google Sheets.
- `set_category_products`: Записывает данные о продуктах в новую таблицу Google Sheets.
- `_format_categories_worksheet`: Форматирует лист 'categories' Google Sheets.
- `_format_category_products_worksheet`: Форматирует лист с продуктами категории Google Sheets.

**Параметры**:

- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.
- `spreadsheet_id` (str): Идентификатор Google Sheets.
- `spreadsheet` (SpreadSheet): Объект `SpreadSheet` для работы с Google Sheets.
- `worksheet` (Worksheet): Объект `Worksheet` для работы с листом Google Sheets.
- `campaign` (SimpleNamespace | str): Объект `SimpleNamespace` с данными кампании.
- `categories` (SimpleNamespace): Объект `SimpleNamespace` с данными о категориях.
- `products` (dict): Словарь с данными о продуктах.
- `category_name` (str): Название категории.
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from types import SimpleNamespace

# Создание экземпляра класса
campaign_name = 'test_campaign'
language = 'ru'
currency = 'RUB'
gsheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)

# Создание объекта SimpleNamespace с данными кампании
campaign_data = SimpleNamespace(
    campaign_name='Test Campaign',
    title='Test Title',
    language='ru',
    currency='RUB',
    description='Test Description'
)

# Запись данных кампании в Google Sheets
gsheet.set_campaign_worksheet(campaign_data)

# Получение данных о категориях из Google Sheets
categories = gsheet.get_categories()
print(categories)
```

## Функции

### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
```

**Описание**: Очищает содержимое Google Sheets.

**Как работает функция**:
1. Вызывает метод `delete_products_worksheets` для удаления всех листов продуктов из Google Sheets.
2.  Обрабатывает исключение `Exception` в случае ошибки при очистке, логируя ошибку с использованием `logger.error`.

**Вызывает исключения**:

- `Exception`: В случае ошибки при очистке содержимого Google Sheets.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Создание экземпляра класса
gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign')

# Очистка содержимого Google Sheets
gsheet.clear()
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
```

**Описание**: Удаляет все листы из Google Sheets, кроме 'categories', 'product' , 'category' и 'campaign'.

**Как работает функция**:
1. Определяет список исключенных названий листов (`excluded_titles`).
2.  Получает список всех листов в Google Sheets с помощью `self.spreadsheet.worksheets()`.
3.  Итерируется по списку листов и удаляет каждый лист, если его название не входит в список исключенных.
4.  Логирует успешное удаление каждого листа с использованием `logger.success`.
5.  Обрабатывает исключение `Exception` в случае ошибки при удалении листов, логируя ошибку с использованием `logger.error` и поднимая исключение.

**Вызывает исключения**:

- `Exception`: В случае ошибки при удалении листов.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Создание экземпляра класса
gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign')

# Удаление листов продуктов
gsheet.delete_products_worksheets()
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

**Описание**: Записывает данные о кампании в лист Google Sheets с названием 'campaign'.

**Как работает функция**:

1.  Получает лист Google Sheets с названием 'campaign' с помощью `self.get_worksheet('campaign')`.
2.  Формирует список кортежей `vertical_data`, содержащий данные для записи в вертикальном формате. Каждый кортеж содержит:
    *   `cell`: Адрес ячейки, в которую нужно записать данные (например, 'A1').
    *   `header`: Заголовок данных (например, 'Campaign Name').
    *   `value`: Значение данных (например, название кампании).
3.  Формирует список `updates`, содержащий операции обновления ячеек Google Sheets. Каждая операция обновления представляет собой словарь со следующими ключами:
    *   `range`: Диапазон ячеек для обновления (например, 'A1').
    *   `values`: Значение для записи в ячейку (например, `[['Campaign Name']]`).
4.  Выполняет пакетное обновление ячеек Google Sheets с помощью `ws.batch_update(updates)`.
5.  Логирует успешную запись данных в лист 'campaign' с использованием `logger.info`.
6.  Обрабатывает исключение `Exception` в случае ошибки при записи данных, логируя ошибку с использованием `logger.error` и поднимая исключение.

**Параметры**:

- `campaign` (SimpleNamespace | str): Объект `SimpleNamespace` с данными о кампании.

**Вызывает исключения**:

- `Exception`: В случае ошибки при записи данных в лист 'campaign'.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from types import SimpleNamespace

# Создание экземпляра класса
gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign')

# Создание объекта SimpleNamespace с данными кампании
campaign_data = SimpleNamespace(
    campaign_name='Test Campaign',
    title='Test Title',
    language='ru',
    currency='RUB',
    description='Test Description'
)

# Запись данных кампании в Google Sheets
gsheet.set_campaign_worksheet(campaign_data)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
```

**Описание**: Записывает данные о продуктах из указанной категории в новый лист Google Sheets.

**Как работает функция**:

1.  Проверяет, указано ли имя категории (`category_name`). Если нет, логирует предупреждение с использованием `logger.warning` и возвращается.
2.  Получает объект категории (`category`) и список продуктов (`products`) из атрибутов `editor.campaign.category` на основе `category_name`.
3.  Копирует лист 'product' и создает новый лист с названием `category_name` с помощью `self.copy_worksheet('product', category_name)`.
4.  Формирует список `row_data`, содержащий данные о каждом продукте для записи в строки Google Sheets.
    *   Итерируется по списку продуктов (`products`).
    *   Для каждого продукта формирует список значений для записи в строку, извлекая данные из атрибутов продукта с помощью `_.get()`.
5.  Обновляет строки листа Google Sheets данными из `row_data`.
    *   Итерируется по списку `row_data` с использованием `enumerate`, начиная с индекса 2 (чтобы пропустить строку заголовков).
    *   Для каждой строки обновляет соответствующий диапазон ячеек в листе Google Sheets с помощью `ws.update(f'A{index}:Y{index}', [row])`.
    *   Логирует информацию об обновлении каждого продукта с использованием `logger.info`.
6.  Вызывает метод `self._format_category_products_worksheet(ws)` для форматирования листа Google Sheets.
7.  Логирует информацию об успешном обновлении продуктов в листе с использованием `logger.info`.
8.  Обрабатывает исключение `Exception` в случае ошибки при записи данных, логируя ошибку с использованием `logger.error` и поднимая исключение.

**Параметры**:

- `category_name` (str): Название категории, продукты которой нужно записать в Google Sheets.

**Вызывает исключения**:

- `Exception`: В случае ошибки при записи данных о продуктах.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Создание экземпляра класса
gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign')

# Запись данных о продуктах для категории 'test_category'
gsheet.set_products_worksheet(category_name='test_category')
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
    """
```

**Описание**: Записывает данные о категориях из объекта `SimpleNamespace` в лист Google Sheets с названием 'categories'.

**Как работает функция**:

1.  Получает лист Google Sheets с названием 'categories' с помощью `self.get_worksheet('categories')`.
2.  Очищает содержимое листа с помощью `ws.clear()`.
3.  Получает данные о категориях из объекта `categories` с помощью `categories.__dict__`.
4.  Проверяет, что все объекты категории имеют необходимые атрибуты ('name', 'title', 'description', 'tags', 'products_count').
5.  Формирует заголовки для таблицы Google Sheets: 'Name', 'Title', 'Description', 'Tags', 'Products Count'.
6.  Записывает заголовки в первую строку листа Google Sheets с помощью `ws.update('A1:E1', [headers])`.
7.  Формирует список `rows`, содержащий данные о каждой категории для записи в строки Google Sheets.
    *   Итерируется по значениям (категориям) в `category_data`.
    *   Для каждой категории формирует список значений для записи в строку, извлекая данные из атрибутов категории.
8.  Обновляет строки листа Google Sheets данными из `rows`.
    *   Обновляет соответствующий диапазон ячеек в листе Google Sheets с помощью `ws.update(f'A2:E{1 + len(rows)}', rows)`.
9.  Вызывает метод `self._format_categories_worksheet(ws)` для форматирования листа Google Sheets.
10. Логирует информацию об успешном обновлении полей категорий с использованием `logger.info`.
11. Если не все объекты категории имеют необходимые атрибуты, логирует предупреждение с использованием `logger.warning`.
12. Обрабатывает исключение `Exception` в случае ошибки при записи данных, логируя ошибку с использованием `logger.error` и поднимая исключение.

**Параметры**:

- `categories` (SimpleNamespace): Объект `SimpleNamespace`, где ключи — это категории с данными для записи.

**Вызывает исключения**:

- `Exception`: В случае ошибки при записи данных.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from types import SimpleNamespace

# Создание экземпляра класса
gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign')

# Создание объекта SimpleNamespace с данными о категориях
categories_data = SimpleNamespace()
categories_data.category1 = SimpleNamespace(
    name='Category 1',
    title='Title 1',
    description='Description 1',
    tags=['tag1', 'tag2'],
    products_count=10
)
categories_data.category2 = SimpleNamespace(
    name='Category 2',
    title='Title 2',
    description='Description 2',
    tags=['tag3', 'tag4'],
    products_count=20
)

# Запись данных о категориях в Google Sheets
gsheet.set_categories_worksheet(categories_data)
```

### `get_categories`

```python
def get_categories(self):
    """ Получение данных из таблицы Google Sheets.
    @return Данные из таблицы в виде списка словарей.
    """
```

**Описание**: Получает данные о категориях из листа Google Sheets с названием 'categories'.

**Как работает функция**:

1.  Получает лист Google Sheets с названием 'categories' с помощью `self.get_worksheet('categories')`.
2.  Получает все записи из листа в виде списка словарей с помощью `ws.get_all_records()`.
3.  Логирует информацию об успешном получении данных о категориях с использованием `logger.info`.
4.  Возвращает полученные данные.

**Возвращает**:

- `list[dict]`: Данные из таблицы в виде списка словарей.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Создание экземпляра класса
gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign')

# Получение данных о категориях
categories = gsheet.get_categories()
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

**Описание**: Записывает данные о продуктах для указанной категории в новый лист Google Sheets.

**Как работает функция**:

1.  Проверяет, указано ли имя категории (`category_name`). Если нет, логирует предупреждение с использованием `logger.warning` и возвращается.
2.  Получает объект категории (`category_ns`) и список продуктов (`products_ns`) из атрибутов `editor.campaign.category` на основе `category_name`.
3.  Копирует лист 'product' и создает новый лист с названием `category_name` с помощью `self.copy_worksheet('product', category_name)`.
4.  Определяет список заголовков для таблицы Google Sheets.
5.  Создает список, содержащий словарь с диапазоном ячеек `A1:Y1` и списком заголовков, и присваивает его переменной `updates`.
6.  Формирует список `row_data`, содержащий данные о каждом продукте для записи в строки Google Sheets.
    *   Итерируется по списку продуктов (`products`).
    *   Для каждого продукта формирует список значений для записи в строку, извлекая данные из атрибутов продукта с помощью `_.get()`.
7.  Обновляет строки листа Google Sheets данными из `row_data`.
    *   Итерируется по списку `row_data` с использованием `enumerate`, начиная с индекса 2 (чтобы пропустить строку заголовков).
    *   Для каждой строки обновляет соответствующий диапазон ячеек в листе Google Sheets с помощью `ws.update(f'A{index}:Y{index}', [row])`.
    *   Логирует информацию об обновлении каждого продукта с использованием `logger.info`.
8.  Вызывает метод `self._format_category_products_worksheet(ws)` для форматирования листа Google Sheets.
9.  Логирует информацию об успешном обновлении продуктов в листе с использованием `logger.info`.
10. Обрабатывает исключение `Exception` в случае ошибки при записи данных, логируя ошибку с использованием `logger.error` и поднимая исключение.

**Параметры**:

- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Вызывает исключения**:

- `Exception`: В случае ошибки при записи данных.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet

# Создание экземпляра класса
gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign')

# Данные о продуктах для категории 'test_category'
products_data = [
    {'product_id': '123', 'app_sale_price': '10.00', 'original_price': '12.00', 'sale_price': '11.00', 'discount': '10%',
     'product_main_image_url': 'http://example.com/image1.jpg', 'local_image_path': '/path/to/image1.jpg',
     'product_small_image_urls': ['http://example.com/small_image1.jpg', 'http://example.com/small_image2.jpg'],
     'product_video_url': 'http://example.com/video1.mp4', 'local_video_path': '/path/to/video1.mp4',
     'first_level_category_id': '1', 'first_level_category_name': 'Category 1', 'second_level_category_id': '11',
     'second_level_category_name': 'Subcategory 1', 'target_sale_price': '10.00', 'target_sale_price_currency': 'USD',
     'target_app_sale_price_currency': 'USD', 'target_original_price_currency': 'USD', 'original_price_currency': 'USD',
     'product_title': 'Product 1', 'evaluate_rate': '4.5', 'promotion_link': 'http://example.com/promotion1',
     'shop_url': 'http://example.com/shop1', 'shop_id': 'shop1', 'tags': ['tag1', 'tag2']},
    {'product_id': '456', 'app_sale_price': '20.00', 'original_price': '24.00', 'sale_price': '22.00', 'discount': '8%',
     'product_main_image_url': 'http://example.com/image2.jpg', 'local_image_path': '/path/to/image2.jpg',
     'product_small_image_urls': ['http://example.com/small_image3.jpg', 'http://example.com/small_image4.jpg'],
     'product_video_url': 'http://example.com/video2.mp4', 'local_video_path': '/path/to/video2.mp4',
     'first_level_category_id': '2', 'first_level_category_name': 'Category 2', 'second_level_category_id': '22',
     'second_level_category_name': 'Subcategory 2', 'target_sale_price': '20.00', 'target_sale_price_currency': 'USD',
     'target_app_sale_price_currency': 'USD', 'target_original_price_currency': 'USD', 'original_price_currency': 'USD',
     'product_title': 'Product 2', 'evaluate_rate': '4.8', 'promotion_link': 'http://example.com/promotion2',
     'shop_url': 'http://example.com/shop2', 'shop_id': 'shop2', 'tags': ['tag3', 'tag4']}
]

# Запись данных о продуктах для категории 'test_category'
gsheet.set_category_products(category_name='test_category', products=products_data)
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """ Форматирование листа 'categories'.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Описание**: Форматирует лист Google Sheets с названием 'categories'.

**Как работает функция**:

1.  Устанавливает ширину столбцов A, B, C, D и E.
2.  Устанавливает высоту первой строки (заголовков).
3.  Определяет формат для заголовков, включая жирный шрифт, размер шрифта 12, центрирование по горизонтали и вертикали, и цвет фона.
4.  Применяет формат заголовков к диапазону ячеек A1:E1.
5.  Логирует информацию об успешном форматировании листа категорий с использованием `logger.info`.
6.  Обрабатывает исключение `Exception` в случае ошибки при форматировании, логируя ошибку с использованием `logger.error` и поднимая исключение.

**Параметры**:

- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:

- `Exception`: В случае ошибки при форматировании листа 'categories'.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from gspread.worksheet import Worksheet

# Создание экземпляра класса
gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign')

# Получение листа Google Sheets
ws: Worksheet = gsheet.get_worksheet('categories')

# Форматирование листа категорий
gsheet._format_categories_worksheet(ws)
```

### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
    """ Форматирование листа с продуктами категории.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Описание**: Форматирует лист Google Sheets с продуктами категории.

**Как работает функция**:

1.  Устанавливает ширину столбцов от A до Y.
2.  Устанавливает высоту первой строки (заголовков).
3.  Определяет формат для заголовков, включая жирный шрифт, размер шрифта 12, центрирование по горизонтали и вертикали, и цвет фона.
4.  Применяет формат заголовков к диапазону ячеек A1:Y1.
5.  Логирует информацию об успешном форматировании листа продуктов категории с использованием `logger.info`.
6.  Обрабатывает исключение `Exception` в случае ошибки при форматировании, логируя ошибку с использованием `logger.error` и поднимая исключение.

**Параметры**:

- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Вызывает исключения**:

- `Exception`: В случае ошибки при форматировании листа с продуктами категории.

**Примеры**:

```python
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from gspread.worksheet import Worksheet

# Создание экземпляра класса
gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign')

# Получение листа Google Sheets
ws: Worksheet = gsheet.get_worksheet('product')

# Форматирование листа продуктов категории
gsheet._format_category_products_worksheet(ws)