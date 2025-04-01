# Модуль для работы с Google Sheets в кампаниях AliExpress
==================================================================

Модуль предназначен для интеграции с Google Sheets и автоматизации работы с данными рекламных кампаний AliExpress. Он предоставляет классы и методы для управления листами Google Sheets, записи и форматирования данных о категориях и продуктах.

## Обзор

Этот модуль предоставляет класс `AliCampaignGoogleSheet`, который наследует функциональность из `SpreadSheet` и добавляет специфические методы для работы с данными кампаний AliExpress в Google Sheets. Он автоматизирует создание, очистку и форматирование листов, а также запись данных о кампаниях, категориях и продуктах.

## Подробнее

Модуль предназначен для упрощения процесса управления рекламными кампаниями AliExpress путем интеграции с Google Sheets. Он позволяет автоматически создавать листы для каждой категории продуктов, записывать данные о продуктах и категориях, а также форматировать листы для удобства просмотра и анализа.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress.

**Наследует**:
- `SpreadSheet`: Предоставляет базовую функциональность для работы с Google Sheets.

**Атрибуты**:
- `spreadsheet_id` (str): ID таблицы Google Sheets, используемой для хранения данных кампании.
- `spreadsheet` (SpreadSheet): Объект SpreadSheet для работы с Google Sheets.
- `worksheet` (Worksheet): Объект Worksheet для работы с конкретным листом Google Sheets.
- `driver` (Driver): Объект Driver для управления браузером и взаимодействия с веб-страницами.
- `editor` (AliCampaignEditor): Объект `AliCampaignEditor` для редактирования параметров кампании AliExpress.

**Методы**:
- `__init__(campaign_name: str, language: str | dict = None, currency: str = None)`: Инициализирует объект `AliCampaignGoogleSheet`, устанавливает параметры кампании, создает необходимые листы и устанавливает URL для драйвера.
- `clear()`: Очищает содержимое, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.
- `delete_products_worksheets()`: Удаляет все листы из таблицы Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.
- `set_campaign_worksheet(campaign: SimpleNamespace)`: Записывает данные кампании на лист Google Sheets.
- `set_products_worksheet(category_name: str)`: Записывает данные о продуктах из указанной категории на лист Google Sheets.
- `set_categories_worksheet(categories: SimpleNamespace)`: Записывает данные о категориях в Google Sheets.
- `get_categories()`: Получает данные из таблицы Google Sheets.
- `set_category_products(category_name: str, products: dict)`: Записывает данные о продуктах в новую таблицу Google Sheets.
- `_format_categories_worksheet(ws: Worksheet)`: Форматирует лист 'categories'.
- `_format_category_products_worksheet(ws: Worksheet)`: Форматирует лист с продуктами категории.

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

**Назначение**: Инициализирует объект `AliCampaignGoogleSheet` с указанным ID таблицы Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str | dict, optional): Язык для кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта для кампании. По умолчанию `None`.

**Как работает функция**:

1. Инициализирует родительский класс `SpreadSheet` с указанным `spreadsheet_id`.
2. Создает экземпляр класса `AliCampaignEditor` с переданными параметрами `campaign_name`, `language` и `currency`.
3. Вызывает метод `clear()` для очистки существующих данных.
4. Вызывает метод `set_campaign_worksheet()` для записи данных кампании на лист Google Sheets.
5. Вызывает метод `set_categories_worksheet()` для записи данных о категориях на лист Google Sheets.
6. Открывает URL Google Sheets в браузере, используя `driver.get_url()`.

```
A (Инициализация SpreadSheet)
│
→ B (Создание AliCampaignEditor)
│
→ C (Очистка данных)
│
→ D (Запись данных кампании)
│
→ E (Запись данных категорий)
│
→ F (Открытие URL Google Sheets)
```

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='Test Campaign', language='ru', currency='USD')
```

### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
    ...
```

**Назначение**: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.

**Как работает функция**:

1. Пытается удалить листы продуктов, вызывая метод `delete_products_worksheets()`.
2. Если возникает исключение, логирует ошибку с помощью `logger.error()`.

```
A (Попытка удаления листов продуктов)
│
→ B (Обработка исключения, если возникла ошибка)
```

**Примеры**:

```python
campaign_sheet.clear()
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
    ...
```

**Назначение**: Удаляет все листы из таблицы Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.

**Как работает функция**:

1. Определяет исключенные названия листов (`excluded_titles`).
2. Получает список всех листов в таблице, используя `self.spreadsheet.worksheets()`.
3. Итерируется по листам и удаляет каждый лист, название которого отсутствует в `excluded_titles`, с помощью `self.spreadsheet.del_worksheet_by_id()`.
4. Логирует успешное удаление каждого листа с помощью `logger.success()`.
5. Если возникает исключение, логирует ошибку с помощью `logger.error()` и вызывает исключение повторно.

```
A (Получение списка листов)
│
→ B (Итерация по листам)
│
→ C (Проверка названия листа)
│
→ D (Удаление листа, если название не исключено)
│
→ E (Логирование успешного удаления)
│
→ F (Обработка исключения, если возникла ошибка)
```

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
    ...
```

**Назначение**: Записывает данные кампании на лист Google Sheets.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании для записи.

**Как работает функция**:

1. Получает лист с именем 'campaign', используя `self.get_worksheet()`.
2. Формирует список `updates` с данными для вертикальной записи, включая название кампании, заголовок, язык, валюту и описание.
3. Итерируется по данным и добавляет операции обновления в список `updates`.
4. Выполняет пакетное обновление листа с помощью `ws.batch_update()`.
5. Логирует успешную запись данных кампании с помощью `logger.info()`.
6. Если возникает исключение, логирует ошибку с помощью `logger.error()` и вызывает исключение повторно.

```
A (Получение листа 'campaign')
│
→ B (Формирование данных для записи)
│
→ C (Итерация по данным)
│
→ D (Добавление операций обновления в список)
│
→ E (Выполнение пакетного обновления)
│
→ F (Логирование успешной записи)
│
→ G (Обработка исключения, если возникла ошибка)
```

**Примеры**:

```python
from types import SimpleNamespace
campaign_data = SimpleNamespace(name='Test Campaign', title='Test Title', language='ru', currency='USD', description='Test Description')
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

**Назначение**: Записывает данные о продуктах из указанной категории на лист Google Sheets.

**Параметры**:
- `category_name` (str): Название категории, из которой нужно получить продукты.

**Как работает функция**:

1. Получает объект категории из `self.editor.campaign.category` по имени `category_name`.
2. Получает список продуктов из объекта категории.
3. Копирует лист 'product' и переименовывает его в `category_name`, используя `self.copy_worksheet()`.
4. Формирует список `row_data` с данными о продуктах.
5. Итерируется по продуктам и добавляет данные в список `row_data`.
6. Обновляет лист Google Sheets данными из `row_data`, используя `ws.update()`.
7. Вызывает метод `self._format_category_products_worksheet()` для форматирования листа.
8. Логирует успешное обновление продуктов с помощью `logger.info()`.
9. Если возникает исключение, логирует ошибку с помощью `logger.error()` и вызывает исключение повторно.

```
A (Получение объекта категории)
│
→ B (Получение списка продуктов)
│
→ C (Копирование листа 'product')
│
→ D (Формирование данных о продуктах)
│
→ E (Итерация по продуктам)
│
→ F (Обновление листа Google Sheets)
│
→ G (Форматирование листа)
│
→ H (Логирование успешного обновления)
│
→ I (Обработка исключения, если возникла ошибка)
```

**Примеры**:

```python
campaign_sheet.set_products_worksheet(category_name='Category1')
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
    """
    ...
```

**Назначение**: Записывает данные о категориях в Google Sheets.

**Параметры**:
- `categories` (SimpleNamespace): Объект, где ключи — это категории с данными для записи.

**Как работает функция**:

1. Получает лист 'categories', используя `self.get_worksheet()`.
2. Очищает лист с помощью `ws.clear()`.
3. Получает данные о категориях из `categories.__dict__`.
4. Проверяет, что все объекты категории имеют необходимые атрибуты: 'name', 'title', 'description', 'tags', 'products_count'.
5. Формирует заголовки для таблицы.
6. Формирует данные для записи в строки.
7. Обновляет строки данных в листе.
8. Форматирует таблицу с помощью `self._format_categories_worksheet()`.
9. Логирует успешное обновление данных с помощью `logger.info()`.
10. Если возникает исключение, логирует ошибку с помощью `logger.error()` и вызывает исключение повторно.

```
A (Получение листа 'categories')
│
→ B (Очистка листа)
│
→ C (Получение данных о категориях)
│
→ D (Проверка атрибутов категорий)
│
→ E (Формирование заголовков)
│
→ F (Формирование данных для записи)
│
→ G (Обновление строк данных)
│
→ H (Форматирование таблицы)
│
→ I (Логирование успешного обновления)
│
→ J (Обработка исключения, если возникла ошибка)
```

**Примеры**:

```python
from types import SimpleNamespace
category1 = SimpleNamespace(name='Category1', title='Title1', description='Description1', tags=['tag1', 'tag2'], products_count=10)
category2 = SimpleNamespace(name='Category2', title='Title2', description='Description2', tags=['tag3', 'tag4'], products_count=20)
categories_data = SimpleNamespace(Category1=category1, Category2=category2)
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

**Назначение**: Получает данные из таблицы Google Sheets.

**Возвращает**:
- Данные из таблицы в виде списка словарей.

**Как работает функция**:

1. Получает лист с именем 'categories', используя `self.get_worksheet()`.
2. Получает все записи с листа, используя `ws.get_all_records()`.
3. Логирует успешное получение данных с помощью `logger.info()`.
4. Возвращает полученные данные.

```
A (Получение листа 'categories')
│
→ B (Получение всех записей)
│
→ C (Логирование успешного получения данных)
│
→ D (Возврат данных)
```

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
    ...
```

**Назначение**: Записывает данные о продуктах в новую таблицу Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Как работает функция**:

1. Получает объект категории из `self.editor.campaign.category` по имени `category_name`.
2. Получает список продуктов из объекта категории.
3. Копирует лист 'product' и переименовывает его в `category_name`, используя `self.copy_worksheet()`.
4. Определяет заголовки для таблицы продуктов.
5. Формирует список `row_data` с данными о продуктах.
6. Итерируется по продуктам и добавляет данные в список `row_data`.
7. Обновляет лист Google Sheets данными из `row_data`, используя `ws.update()`.
8. Вызывает метод `self._format_category_products_worksheet()` для форматирования листа.
9. Логирует успешное обновление продуктов с помощью `logger.info()`.
10. Если возникает исключение, логирует ошибку с помощью `logger.error()` и вызывает исключение повторно.

```
A (Получение объекта категории)
│
→ B (Получение списка продуктов)
│
→ C (Копирование листа 'product')
│
→ D (Определение заголовков)
│
→ E (Формирование данных о продуктах)
│
→ F (Итерация по продуктам)
│
→ G (Обновление листа Google Sheets)
│
→ H (Форматирование листа)
│
→ I (Логирование успешного обновления)
│
→ J (Обработка исключения, если возникла ошибка)
```

**Примеры**:

```python
products_data = [{'product_id': '123', 'app_sale_price': '10.00', 'original_price': '20.00', 'sale_price': '15.00', 'discount': '5.00', 'product_main_image_url': 'http://example.com/image.jpg', 'local_image_path': '/path/to/image.jpg', 'product_small_image_urls': [], 'product_video_url': 'http://example.com/video.mp4', 'local_video_path': '/path/to/video.mp4', 'first_level_category_id': '1', 'first_level_category_name': 'Category1', 'second_level_category_id': '2', 'second_level_category_name': 'Category2', 'target_sale_price': '12.00', 'target_sale_price_currency': 'USD', 'target_app_sale_price_currency': 'USD', 'target_original_price_currency': 'USD', 'original_price_currency': 'USD', 'product_title': 'Test Product', 'evaluate_rate': '5.0', 'promotion_link': 'http://example.com/promotion', 'shop_url': 'http://example.com/shop', 'shop_id': '123', 'tags': []}]
campaign_sheet.set_category_products(category_name='Category1', products=products_data)
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """ Форматирование листа 'categories'.
    @param ws Лист Google Sheets для форматирования.
    """
    ...
```

**Назначение**: Форматирует лист 'categories'.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:

1. Устанавливает ширину столбцов A, B, C, D и E.
2. Устанавливает высоту строки 1 (заголовки).
3. Определяет формат заголовков (жирный шрифт, размер 12, выравнивание по центру, серый фон).
4. Применяет формат заголовков к диапазону A1:E1.
5. Логирует успешное форматирование листа с помощью `logger.info()`.
6. Если возникает исключение, логирует ошибку с помощью `logger.error()` и вызывает исключение повторно.

```
A (Установка ширины столбцов)
│
→ B (Установка высоты строк)
│
→ C (Определение формата заголовков)
│
→ D (Применение формата к заголовкам)
│
→ E (Логирование успешного форматирования)
│
→ F (Обработка исключения, если возникла ошибка)
```

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
    ...
```

**Назначение**: Форматирует лист с продуктами категории.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:

1. Устанавливает ширину столбцов от A до Y.
2. Устанавливает высоту строки 1 (заголовки).
3. Определяет формат заголовков (жирный шрифт, размер 12, выравнивание по центру, серый фон).
4. Применяет формат заголовков к диапазону A1:Y1.
5. Логирует успешное форматирование листа с помощью `logger.info()`.
6. Если возникает исключение, логирует ошибку с помощью `logger.error()` и вызывает исключение повторно.

```
A (Установка ширины столбцов)
│
→ B (Установка высоты строк)
│
→ C (Определение формата заголовков)
│
→ D (Применение формата к заголовкам)
│
→ E (Логирование успешного форматирования)
│
→ F (Обработка исключения, если возникла ошибка)
```

**Примеры**:

```python
ws = campaign_sheet.get_worksheet('Category1')
campaign_sheet._format_category_products_worksheet(ws)