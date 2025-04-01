# Модуль `src.suppliers.aliexpress.campaign.gsheet`

## Обзор

Модуль `src.suppliers.aliexpress.campaign.gsheet` предназначен для работы с Google Sheets в контексте рекламных кампаний на AliExpress. Он предоставляет инструменты для создания, редактирования и форматирования таблиц, содержащих информацию о кампаниях, категориях и продуктах. Модуль позволяет автоматизировать процесс обновления данных в Google Sheets, что упрощает управление рекламными кампаниями.

## Подробней

Этот модуль является частью проекта `hypotez` и используется для интеграции с Google Sheets, чтобы управлять рекламными кампаниями AliExpress. Он включает в себя функциональность для очистки, создания и форматирования листов Google Sheets, а также для записи данных о категориях и продуктах.

## Классы

### `AliCampaignGoogleSheet`

**Описание**:
Класс `AliCampaignGoogleSheet` предназначен для работы с Google Sheets в рамках кампаний AliExpress. Он наследует класс `SpreadSheet` и предоставляет методы для управления листами, записи данных о категориях и продуктах, а также для форматирования листов.

**Принцип работы**:
Класс инициализируется с указанием идентификатора Google Sheets, имени кампании, языка и валюты. Он использует класс `SpreadSheet` для базовых операций с Google Sheets и добавляет специфические методы для работы с данными AliExpress.

**Методы**:

- `__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)`
- `clear(self)`
- `delete_products_worksheets(self)`
- `set_campaign_worksheet(self, campaign: SimpleNamespace)`
- `set_products_worksheet(self, category_name: str)`
- `set_categories_worksheet(self, categories: SimpleNamespace)`
- `get_categories(self)`
- `set_category_products(self, category_name: str, products: dict)`
- `_format_categories_worksheet(self, ws: Worksheet)`
- `_format_category_products_worksheet(self, ws: Worksheet)`

#### `__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)`

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

**Назначение**:
Инициализирует экземпляр класса `AliCampaignGoogleSheet` с указанным идентификатором Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык для кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта для кампании. По умолчанию `None`.

**Как работает функция**:

1. Вызывает конструктор родительского класса `SpreadSheet` с идентификатором Google Sheets, хранящимся в `self.spreadsheet_id`.
2. Инициализирует атрибуты экземпляра класса с переданными значениями имени кампании, языка и валюты.

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale', language='en', currency='USD')
```

#### `clear(self)`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
    ...
```

**Назначение**:
Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.

**Как работает функция**:

1.  Вызывает метод `delete_products_worksheets` для удаления листов продуктов.
2.  Ловит возможные исключения и логирует их с помощью `logger.error`.

**Примеры**:

```python
campaign_sheet.clear()
```

#### `delete_products_worksheets(self)`

```python
def delete_products_worksheets(self):
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
    ...
```

**Назначение**:
Удаляет все листы из Google Sheets, кроме листов 'categories', 'product', 'category', и 'campaign'.

**Как работает функция**:

1.  Определяет множество `excluded_titles`, содержащее названия листов, которые не нужно удалять (`categories`, `product`, `category`, `campaign`).
2.  Получает список всех листов в Google Sheets с помощью `self.spreadsheet.worksheets()`.
3.  Итерируется по листам и удаляет каждый лист, если его название не содержится в `excluded_titles`.
4.  Логирует успешное удаление каждого листа с помощью `logger.success`.
5.  В случае возникновения исключения, логирует ошибку с помощью `logger.error` и поднимает исключение.

**Примеры**:

```python
campaign_sheet.delete_products_worksheets()
```

#### `set_campaign_worksheet(self, campaign: SimpleNamespace)`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace):
    """ Write campaign data to a Google Sheets worksheet.
    @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
    @param language `str`: Optional language parameter.
    @param currency `str`: Optional currency parameter.
    """
    ...
```

**Назначение**:
Записывает данные кампании в Google Sheets на лист 'campaign'.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании для записи.

**Как работает функция**:

1.  Получает лист с названием 'campaign' с помощью `self.get_worksheet('campaign')`.
2.  Формирует список `updates`, содержащий данные для записи в вертикальном формате.
3.  Итерируется по данным и добавляет операции обновления в список `updates`.
4.  Выполняет пакетное обновление листа с помощью `ws.batch_update(updates)`.
5.  Логирует успешную запись данных с помощью `logger.info`.
6.  В случае возникновения исключения, логирует ошибку с помощью `logger.error` и поднимает исключение.

**Примеры**:

```python
campaign_data = SimpleNamespace(campaign_name='SummerSale', title='Summer Sale Campaign', language='en', currency='USD', description='Summer sale campaign description')
campaign_sheet.set_campaign_worksheet(campaign_data)
```

#### `set_products_worksheet(self, category_name: str)`

```python
def set_products_worksheet(self, category_name: str):
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
    ...
```

**Назначение**:
Записывает данные о продуктах из указанной категории в Google Sheets на лист, скопированный из шаблона 'product'.

**Параметры**:
- `category_name` (str): Название категории, продукты из которой нужно записать.

**Как работает функция**:

1.  Если `category_name` не указан, логирует предупреждение и выходит из функции.
2.  Копирует лист 'product' и присваивает ему имя `category_name` с помощью `self.copy_worksheet('product', category_name)`.
3.  Формирует список `row_data`, содержащий данные о продуктах для записи.
4.  Итерируется по продуктам и добавляет данные каждого продукта в список `row_data`.
5.  Обновляет строки листа данными из `row_data` с помощью `ws.update`.
6.  Вызывает метод `self._format_category_products_worksheet(ws)` для форматирования листа.
7.  Логирует успешное обновление данных с помощью `logger.info`.
8.  В случае возникновения исключения, логирует ошибку с помощью `logger.error` и поднимает исключение.

**Примеры**:

```python
campaign_sheet.set_products_worksheet(category_name='shoes')
```

#### `set_categories_worksheet(self, categories: SimpleNamespace)`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
    """
    ...
```

**Назначение**:
Записывает данные о категориях из объекта `SimpleNamespace` в Google Sheets на лист 'categories'.

**Параметры**:
- `categories` (SimpleNamespace): Объект, содержащий данные о категориях.

**Как работает функция**:

1.  Получает лист 'categories' с помощью `self.get_worksheet('categories')` и очищает его.
2.  Получает данные о категориях из атрибута `__dict__` объекта `categories`.
3.  Проверяет, что все объекты категории имеют необходимые атрибуты (`name`, `title`, `description`, `tags`, `products_count`).
4.  Формирует заголовки таблицы и записывает их на лист.
5.  Формирует список `rows`, содержащий данные о категориях для записи.
6.  Обновляет строки листа данными из `rows` с помощью `ws.update`.
7.  Вызывает метод `self._format_categories_worksheet(ws)` для форматирования листа.
8.  Логирует успешную запись данных с помощью `logger.info`.
9.  В случае возникновения исключения, логирует ошибку с помощью `logger.error` и поднимает исключение.

**Примеры**:

```python
categories_data = SimpleNamespace(
    category1=SimpleNamespace(name='shoes', title='Shoes', description='Shoes category', tags=['shoes', 'footwear'], products_count=100),
    category2=SimpleNamespace(name='shirts', title='Shirts', description='Shirts category', tags=['shirts', 'clothing'], products_count=50)
)
campaign_sheet.set_categories_worksheet(categories_data)
```

#### `get_categories(self)`

```python
def get_categories(self):
    """ Получение данных из таблицы Google Sheets.
    @return Данные из таблицы в виде списка словарей.
    """
    ...
```

**Назначение**:
Получает данные о категориях из Google Sheets с листа 'categories'.

**Возвращает**:
- list[dict]: Данные из таблицы в виде списка словарей.

**Как работает функция**:

1.  Получает лист 'categories' с помощью `self.get_worksheet('categories')`.
2.  Получает все записи с листа в виде списка словарей с помощью `ws.get_all_records()`.
3.  Логирует успешное получение данных с помощью `logger.info`.
4.  Возвращает полученные данные.

**Примеры**:

```python
categories = campaign_sheet.get_categories()
```

#### `set_category_products(self, category_name: str, products: dict)`

```python
def set_category_products(self, category_name: str, products: dict):
    """ Запись данных о продуктах в новую таблицу Google Sheets.
    @param category_name Название категории.
    @param products Словарь с данными о продуктах.
    """
    ...
```

**Назначение**:
Записывает данные о продуктах указанной категории в Google Sheets на новый лист, скопированный из шаблона 'product'.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Как работает функция**:

1.  Если `category_name` не указан, логирует предупреждение и выходит из функции.
2.  Копирует лист 'product' и присваивает ему имя `category_name` с помощью `self.copy_worksheet('product', category_name)`.
3.  Определяет заголовки таблицы.
4.  Формирует список `row_data`, содержащий данные о продуктах для записи.
5.  Итерируется по продуктам и добавляет данные каждого продукта в список `row_data`.
6.  Обновляет строки листа данными из `row_data` с помощью `ws.update`.
7.  Вызывает метод `self._format_category_products_worksheet(ws)` для форматирования листа.
8.  Логирует успешное обновление данных с помощью `logger.info`.
9.  В случае возникновения исключения, логирует ошибку с помощью `logger.error` и поднимает исключение.

**Примеры**:

```python
products_data = [
    {'product_id': '123', 'app_sale_price': '10.00', 'original_price': '20.00', 'sale_price': '15.00', 'discount': '50%', 'product_main_image_url': 'http://example.com/image1.jpg', 'local_image_path': '/path/to/image1.jpg', 'product_small_image_urls': ['http://example.com/image2.jpg', 'http://example.com/image3.jpg'], 'product_video_url': 'http://example.com/video1.mp4', 'local_video_path': '/path/to/video1.mp4', 'first_level_category_id': '1', 'first_level_category_name': 'Shoes', 'second_level_category_id': '2', 'second_level_category_name': 'Sneakers', 'target_sale_price': '12.00', 'target_sale_price_currency': 'USD', 'target_app_sale_price_currency': 'USD', 'target_original_price_currency': 'USD', 'original_price_currency': 'USD', 'product_title': 'Awesome Sneakers', 'evaluate_rate': '4.5', 'promotion_link': 'http://example.com/promotion1', 'shop_url': 'http://example.com/shop1', 'shop_id': 'shop1', 'tags': ['sneakers', 'shoes']},
    {'product_id': '456', 'app_sale_price': '25.00', 'original_price': '50.00', 'sale_price': '37.50', 'discount': '50%', 'product_main_image_url': 'http://example.com/image4.jpg', 'local_image_path': '/path/to/image4.jpg', 'product_small_image_urls': ['http://example.com/image5.jpg', 'http://example.com/image6.jpg'], 'product_video_url': 'http://example.com/video2.mp4', 'local_video_path': '/path/to/video2.mp4', 'first_level_category_id': '1', 'first_level_category_name': 'Shoes', 'second_level_category_id': '3', 'second_level_category_name': 'Boots', 'target_sale_price': '30.00', 'target_sale_price_currency': 'USD', 'target_app_sale_price_currency': 'USD', 'target_original_price_currency': 'USD', 'original_price_currency': 'USD', 'product_title': 'Cool Boots', 'evaluate_rate': '4.8', 'promotion_link': 'http://example.com/promotion2', 'shop_url': 'http://example.com/shop2', 'shop_id': 'shop2', 'tags': ['boots', 'shoes']}
]
campaign_sheet.set_category_products(category_name='shoes', products=products_data)
```

#### `_format_categories_worksheet(self, ws: Worksheet)`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """ Форматирование листа 'categories'.
    @param ws Лист Google Sheets для форматирования.
    """
    ...
```

**Назначение**:
Форматирует лист 'categories' в Google Sheets, устанавливая ширину столбцов, высоту строк и форматирование заголовков.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:

1.  Устанавливает ширину столбцов A, B, C, D и E с помощью `set_column_width`.
2.  Устанавливает высоту строки 1 с помощью `set_row_height`.
3.  Определяет формат заголовков с помощью `cellFormat`, `textFormat` и `Color`.
4.  Применяет формат заголовков к диапазону A1:E1 с помощью `format_cell_range`.
5.  Логирует успешное форматирование листа с помощью `logger.info`.
6.  В случае возникновения исключения, логирует ошибку с помощью `logger.error` и поднимает исключение.

**Примеры**:

```python
ws = campaign_sheet.get_worksheet('categories')
campaign_sheet._format_categories_worksheet(ws)
```

#### `_format_category_products_worksheet(self, ws: Worksheet)`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
    """ Форматирование листа с продуктами категории.
    @param ws Лист Google Sheets для форматирования.
    """
    ...
```

**Назначение**:
Форматирует лист с продуктами категории в Google Sheets, устанавливая ширину столбцов, высоту строк и форматирование заголовков.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:

1.  Устанавливает ширину столбцов от A до Y с помощью `set_column_width`.
2.  Устанавливает высоту строки 1 с помощью `set_row_height`.
3.  Определяет формат заголовков с помощью `cellFormat`, `textFormat` и `Color`.
4.  Применяет формат заголовков к диапазону A1:Y1 с помощью `format_cell_range`.
5.  Логирует успешное форматирование листа с помощью `logger.info`.
6.  В случае возникновения исключения, логирует ошибку с помощью `logger.error` и поднимает исключение.

**Примеры**:

```python
ws = campaign_sheet.get_worksheet('shoes')
campaign_sheet._format_category_products_worksheet(ws)
```

## Функции

В данном модуле не предоставлено отдельных функций вне класса `AliCampaignGoogleSheet`.