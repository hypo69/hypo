# Модуль для работы с Google Sheets для управления рекламными кампаниями AliExpress
## Обзор

Модуль `gsheet.py` предназначен для работы с Google Sheets в контексте управления рекламными кампаниями на платформе AliExpress. Он предоставляет инструменты для автоматизации процессов, связанных с созданием, редактированием и обновлением данных кампаний, категорий и продуктов непосредственно в Google Sheets.

## Подробней

Этот модуль упрощает взаимодействие с Google Sheets, позволяя программно управлять данными, используемыми в рекламных кампаниях AliExpress. Он предоставляет функциональность для очистки существующих данных, создания новых листов, записи данных о кампаниях, категориях и продуктах, а также форматирования листов для удобства восприятия.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс `AliCampaignGoogleSheet` расширяет функциональность класса `SpreadSheet` и предназначен для работы с Google Sheets, используемыми в рекламных кампаниях AliExpress. Он предоставляет методы для управления листами Google Sheets, записи данных о категориях и продуктах, а также форматирования листов.

**Наследует**:
- `SpreadSheet`: Обеспечивает базовую функциональность для работы с Google Sheets, такую как подключение к таблице, получение и обновление данных.

**Атрибуты**:
- `spreadsheet_id` (str): Идентификатор Google Sheets таблицы.
- `spreadsheet` (SpreadSheet): Экземпляр класса `SpreadSheet` для работы с Google Sheets.
- `worksheet` (Worksheet): Текущий рабочий лист Google Sheets.

**Методы**:
- `__init__`: Инициализирует объект класса `AliCampaignGoogleSheet`, устанавливая соединение с Google Sheets и инициализируя параметры кампании.
- `clear`: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на других листах.
- `delete_products_worksheets`: Удаляет все листы из Google Sheets, кроме листов с категориями и шаблоном продукта.
- `set_campaign_worksheet`: Записывает данные о кампании в лист Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в лист Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в лист Google Sheets.
- `get_categories`: Получает данные о категориях из листа Google Sheets.
- `set_category_products`: Записывает данные о продуктах категории в лист Google Sheets.
- `_format_categories_worksheet`: Форматирует лист с категориями в Google Sheets.
- `_format_category_products_worksheet`: Форматирует лист с продуктами категории в Google Sheets.

## Функции

### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None) -> None:
    """ Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
    @param campaign_name `str`: The name of the campaign.
    @param category_name `str`: The name of the category.   
    @param language `str`: The language for the campaign.
    @param currency `str`: The currency for the campaign.
    """
```

**Назначение**: Инициализирует класс `AliCampaignGoogleSheet` с указанным ID таблицы Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Как работает функция**:
1. Вызывает конструктор родительского класса `SpreadSheet`, передавая `spreadsheet_id`.
2.  <Если нужно установить рабочие листы для категорий и кампании - загружает их>

ASCII схема работы функции:
```
A[Инициализация AliCampaignGoogleSheet]
|
B[Инициализация SpreadSheet]
```

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='ru', currency='USD')
```

### `clear`

```python
def clear(self) -> None:
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
```

**Назначение**: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.

**Как работает функция**:
1. Пытается удалить листы продуктов, вызывая метод `delete_products_worksheets`.
2. В случае возникновения ошибки логирует ее.

ASCII схема работы функции:
```
A[Очистка содержимого Google Sheets]
|
B[Попытка удаления листов продуктов]
|
C[Логирование ошибки в случае неудачи]
```

**Примеры**:

```python
campaign_sheet.clear()
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self) -> None:
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
```

**Назначение**: Удаляет все листы из Google Sheets, кроме листов с названиями 'categories', 'product', 'category', 'campaign'.

**Как работает функция**:
1. Получает список всех листов в Google Sheets.
2. Перебирает листы и удаляет те, чьи названия не входят в список исключений.
3. Логирует успешное удаление каждого листа.
4. В случае возникновения ошибки логирует ее и вызывает исключение.

ASCII схема работы функции:
```
A[Удаление листов продуктов]
|
B[Получение списка листов]
|
C[Перебор листов]
|
D[Проверка на исключение]
|
E[Удаление листа (если не исключение)]
|
F[Логирование успеха]
|
G[Логирование ошибки и вызов исключения в случае неудачи]
```

**Примеры**:

```python
campaign_sheet.delete_products_worksheets()
```

### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace) -> None:
    """ Write campaign data to a Google Sheets worksheet.
    @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
    @param language `str`: Optional language parameter.
    @param currency `str`: Optional currency parameter.
    """
```

**Назначение**: Записывает данные о кампании в лист Google Sheets с именем 'campaign'.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании.

**Как работает функция**:
1. Получает рабочий лист с именем 'campaign'.
2. Подготавливает данные для записи в вертикальном формате.
3. Обновляет ячейки листа данными из объекта `campaign`.
4. Логирует успешную запись данных.
5. В случае возникновения ошибки логирует ее и вызывает исключение.

ASCII схема работы функции:
```
A[Запись данных кампании в Google Sheets]
|
B[Получение рабочего листа 'campaign']
|
C[Подготовка данных для записи]
|
D[Обновление ячеек листа]
|
E[Логирование успеха]
|
F[Логирование ошибки и вызов исключения в случае неудачи]
```

**Примеры**:

```python
from types import SimpleNamespace
campaign_data = SimpleNamespace(campaign_name='test_campaign', title='Test Campaign', language='ru', currency='USD', description='Test description')
campaign_sheet.set_campaign_worksheet(campaign_data)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str) -> None:
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
```

**Назначение**: Записывает данные о продуктах из указанной категории в лист Google Sheets.

**Параметры**:
- `category_name` (str): Название категории, продукты из которой нужно записать в лист.

**Как работает функция**:
1. Копирует лист 'product' и присваивает ему имя категории.
2. Получает данные о продуктах из категории.
3. Формирует данные для записи в строки листа.
4. Обновляет лист данными о продуктах.
5. Форматирует лист с продуктами.
6. Логирует успешную запись данных.
7. В случае возникновения ошибки логирует ее и вызывает исключение.

ASCII схема работы функции:
```
A[Запись данных о продуктах в Google Sheets]
|
B[Копирование листа 'product']
|
C[Получение данных о продуктах]
|
D[Формирование данных для записи]
|
E[Обновление листа данными]
|
F[Форматирование листа]
|
G[Логирование успеха]
|
H[Логирование ошибки и вызов исключения в случае неудачи]
```

**Примеры**:

```python
campaign_sheet.set_products_worksheet(category_name='test_category')
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace) -> None:
    """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
    """
```

**Назначение**: Записывает данные о категориях из объекта SimpleNamespace в лист Google Sheets.

**Параметры**:
- `categories` (SimpleNamespace): Объект SimpleNamespace, содержащий данные о категориях.

**Как работает функция**:
1. Получает рабочий лист с именем 'categories'.
2. Очищает рабочий лист.
3. Получает данные о категориях из объекта `categories`.
4. Проверяет наличие необходимых атрибутов у объектов категорий.
5. Формирует заголовки таблицы.
6. Формирует данные для записи в строки листа.
7. Обновляет лист данными о категориях.
8. Форматирует лист с категориями.
9. Логирует успешную запись данных.
10. В случае возникновения ошибки логирует ее и вызывает исключение.

ASCII схема работы функции:
```
A[Запись данных о категориях в Google Sheets]
|
B[Получение рабочего листа 'categories']
|
C[Очистка рабочего листа]
|
D[Получение данных о категориях]
|
E[Проверка атрибутов категорий]
|
F[Формирование заголовков таблицы]
|
G[Формирование данных для записи]
|
H[Обновление листа данными]
|
I[Форматирование листа]
|
J[Логирование успеха]
|
K[Логирование ошибки и вызов исключения в случае неудачи]
```

**Примеры**:

```python
from types import SimpleNamespace
category1 = SimpleNamespace(name='cat1', title='Category 1', description='Description 1', tags=['tag1', 'tag2'], products_count=10)
category2 = SimpleNamespace(name='cat2', title='Category 2', description='Description 2', tags=['tag3', 'tag4'], products_count=20)
categories_data = SimpleNamespace(cat1=category1, cat2=category2)
campaign_sheet.set_categories_worksheet(categories_data)
```

### `get_categories`

```python
def get_categories(self) -> list[dict[Any, Any]]:
    """ Получение данных из таблицы Google Sheets.
    @return Данные из таблицы в виде списка словарей.
    """
```

**Назначение**: Получает данные о категориях из листа Google Sheets с именем 'categories'.

**Возвращает**:
- `list[dict[Any, Any]]`: Данные из таблицы в виде списка словарей.

**Как работает функция**:
1. Получает рабочий лист с именем 'categories'.
2. Получает все записи с листа.
3. Логирует успешное получение данных.
4. Возвращает полученные данные.

ASCII схема работы функции:
```
A[Получение данных о категориях из Google Sheets]
|
B[Получение рабочего листа 'categories']
|
C[Получение всех записей с листа]
|
D[Логирование успеха]
|
E[Возврат данных]
```

**Примеры**:

```python
categories = campaign_sheet.get_categories()
print(categories)
```

### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict) -> None:
    """ Запись данных о продуктах в новую таблицу Google Sheets.
    @param category_name Название категории.
    @param products Словарь с данными о продуктах.
    """
```

**Назначение**: Записывает данные о продуктах в новый лист Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Как работает функция**:
1. Копирует лист 'product' и присваивает ему имя категории.
2. Формирует заголовки для таблицы.
3. Формирует данные для записи в строки листа на основе предоставленных данных о продуктах.
4. Обновляет лист данными о продуктах.
5. Форматирует лист с продуктами.
6. Логирует успешную запись данных.
7. В случае возникновения ошибки логирует ее и вызывает исключение.

ASCII схема работы функции:
```
A[Запись данных о продуктах в Google Sheets]
|
B[Копирование листа 'product']
|
C[Формирование заголовков таблицы]
|
D[Формирование данных для записи]
|
E[Обновление листа данными]
|
F[Форматирование листа]
|
G[Логирование успеха]
|
H[Логирование ошибки и вызов исключения в случае неудачи]
```

**Примеры**:

```python
products_data = [
    {'product_id': '1', 'app_sale_price': '10.00', 'original_price': '12.00', 'sale_price': '11.00', 'discount': '10%',
     'product_main_image_url': 'url1', 'local_image_path': 'path1', 'product_small_image_urls': [],
     'product_video_url': 'url2', 'local_video_path': 'path2', 'first_level_category_id': '100',
     'first_level_category_name': 'Category1', 'second_level_category_id': '200', 'second_level_category_name': 'Category2',
     'target_sale_price': '9.00', 'target_sale_price_currency': 'USD', 'target_app_sale_price_currency': 'USD',
     'target_original_price_currency': 'USD', 'original_price_currency': 'USD', 'product_title': 'Product 1',
     'evaluate_rate': '4.5', 'promotion_link': 'link1', 'shop_url': 'shop1', 'shop_id': 'shop_id_1', 'tags': []},
    {'product_id': '2', 'app_sale_price': '20.00', 'original_price': '24.00', 'sale_price': '22.00', 'discount': '20%',
     'product_main_image_url': 'url3', 'local_image_path': 'path3', 'product_small_image_urls': [],
     'product_video_url': 'url4', 'local_video_path': 'path4', 'first_level_category_id': '300',
     'first_level_category_name': 'Category3', 'second_level_category_id': '400', 'second_level_category_name': 'Category4',
     'target_sale_price': '18.00', 'target_sale_price_currency': 'EUR', 'target_app_sale_price_currency': 'EUR',
     'target_original_price_currency': 'EUR', 'original_price_currency': 'EUR', 'product_title': 'Product 2',
     'evaluate_rate': '4.8', 'promotion_link': 'link2', 'shop_url': 'shop2', 'shop_id': 'shop_id_2', 'tags': []}
]
campaign_sheet.set_category_products(category_name='test_category', products=products_data)
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet) -> None:
    """ Форматирование листа 'categories'.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Назначение**: Форматирует лист Google Sheets с категориями.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:
1. Устанавливает ширину столбцов.
2. Устанавливает высоту строк.
3. Форматирует заголовки.
4. Логирует успешное форматирование.
5. В случае возникновения ошибки логирует ее и вызывает исключение.

ASCII схема работы функции:
```
A[Форматирование листа 'categories']
|
B[Установка ширины столбцов]
|
C[Установка высоты строк]
|
D[Форматирование заголовков]
|
E[Логирование успеха]
|
F[Логирование ошибки и вызов исключения в случае неудачи]
```

**Примеры**:

```python
ws = campaign_sheet.get_worksheet('categories')
campaign_sheet._format_categories_worksheet(ws)
```

### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet) -> None:
    """ Форматирование листа с продуктами категории.
    @param ws Лист Google Sheets для форматирования.
    """
```

**Назначение**: Форматирует лист Google Sheets с продуктами категории.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:
1. Устанавливает ширину столбцов.
2. Устанавливает высоту строк.
3. Форматирует заголовки.
4. Логирует успешное форматирование.
5. В случае возникновения ошибки логирует ее и вызывает исключение.

ASCII схема работы функции:
```
A[Форматирование листа с продуктами категории]
|
B[Установка ширины столбцов]
|
C[Установка высоты строк]
|
D[Форматирование заголовков]
|
E[Логирование успеха]
|
F[Логирование ошибки и вызов исключения в случае неудачи]
```

**Примеры**:

```python
ws = campaign_sheet.get_worksheet('test_category')
campaign_sheet._format_category_products_worksheet(ws)