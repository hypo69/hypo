# Модуль `gsheets_check_this_code`

## Обзор

Модуль `gsheets_check_this_code` предназначен для работы с Google Sheets в контексте управления рекламными кампаниями AliExpress. Он предоставляет функциональность для чтения, записи и форматирования данных кампаний, категорий и продуктов в Google Sheets.

## Подробнее

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с Google Sheets для автоматизации управления рекламными кампаниями на AliExpress. Он использует классы `SpreadSheet` и `AliCampaignEditor` для взаимодействия с Google Sheets API и редактирования кампаний AliExpress соответственно. Модуль позволяет создавать, очищать и форматировать листы Google Sheets, а также записывать данные о кампаниях, категориях и продуктах.

## Классы

### `AliCampaignGoogleSheet`

**Описание**:
Класс `AliCampaignGoogleSheet` предназначен для работы с Google Sheets в рамках кампаний AliExpress. Он наследует класс `SpreadSheet` и предоставляет дополнительные методы для управления листами Google Sheets, записи данных о категориях и продуктах, а также форматирования листов.

**Принцип работы**:
Класс `AliCampaignGoogleSheet` инициализируется с указанием идентификатора Google Sheets, имени кампании, языка и валюты. Он использует класс `AliCampaignEditor` для управления данными кампании и предоставляет методы для очистки листов, записи данных о кампаниях, категориях и продуктах, а также форматирования листов.

**Методы**:
- `__init__`: Инициализирует объект `AliCampaignGoogleSheet`, устанавливает параметры кампании и подключается к Google Sheets.
- `clear`: Очищает содержимое листов Google Sheets, удаляя листы продуктов и очищая данные на других листах.
- `delete_products_worksheets`: Удаляет все листы из Google Sheets, кроме листов `categories`, `product`, `category` и `campaign`.
- `set_campaign_worksheet`: Записывает данные кампании в лист Google Sheets `campaign`.
- `set_products_worksheet`: Записывает данные о продуктах в лист Google Sheets, соответствующий категории.
- `set_categories_worksheet`: Записывает данные о категориях в лист Google Sheets `categories`.
- `get_categories`: Получает данные о категориях из листа Google Sheets `categories`.
- `set_category_products`: Записывает данные о продуктах категории в лист Google Sheets.
- `_format_categories_worksheet`: Форматирует лист Google Sheets `categories`.
- `_format_category_products_worksheet`: Форматирует лист Google Sheets с продуктами категории.

#### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
    """
    Args:
        campaign_name (str): Название кампании.
        language (str | dict, optional): Язык для кампании. По умолчанию `None`.
        currency (str, optional): Валюта для кампании. По умолчанию `None`.
    
    Raises:
        Exception: Если возникает ошибка при инициализации.

    """
```

**Назначение**:
Инициализирует класс `AliCampaignGoogleSheet` с указанным ID таблицы Google Sheets и дополнительными параметрами.

**Как работает функция**:

1.  Вызывает конструктор родительского класса `SpreadSheet`, передавая `spreadsheet_id`.
2.  Инициализирует редактор кампании `AliCampaignEditor` с указанным именем, языком и валютой.
3.  Вызывает метод `clear` для очистки существующих данных.
4.  Вызывает метод `set_campaign_worksheet` для записи данных кампании в соответствующий лист.
5.  Вызывает метод `set_categories_worksheet` для записи данных категорий в соответствующий лист.
6.  Открывает Google Sheets по указанному `spreadsheet_id` с помощью `driver`.

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='Test Campaign', language='ru', currency='USD')
```

#### `clear`

```python
def clear(self):
    """
    Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на других указанных листах.
    """
```

**Назначение**:
Очищает содержимое листов Google Sheets, удаляя листы продуктов и очищая данные на других указанных листах.

**Как работает функция**:

1.  Вызывает метод `delete_products_worksheets` для удаления листов продуктов.
2.  Обрабатывает возможные исключения, возникающие при очистке, и логирует ошибки.

**Примеры**:

```python
campaign_sheet.clear()
```

#### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """
    Удаляет все листы из Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.
    
    Raises:
        Exception: Если возникает ошибка при удалении листов.
    """
```

**Назначение**:
Удаляет все листы из Google Sheets, за исключением листов с названиями 'categories', 'product', 'category' и 'campaign'.

**Как работает функция**:

1.  Определяет набор `excluded_titles`, содержащий названия листов, которые не следует удалять.
2.  Получает список всех листов в Google Sheets.
3.  Итерируется по листам и удаляет те, чьи названия не входят в `excluded_titles`.
4.  Логирует успешное удаление каждого листа.
5.  Обрабатывает возможные исключения, возникающие при удалении, логирует ошибки и поднимает исключение.

**Примеры**:

```python
campaign_sheet.delete_products_worksheets()
```

#### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace):
    """
    Записывает данные кампании в лист Google Sheets 'campaign'.
    
    Args:
        campaign (SimpleNamespace | str): Объект SimpleNamespace с данными кампании для записи.
        language (str): Опциональный параметр языка.
        currency (str): Опциональный параметр валюты.
    
    Raises:
        Exception: Если возникает ошибка при записи данных кампании.
    """
```

**Назначение**:
Записывает данные кампании в лист Google Sheets с именем 'campaign'.

**Как работает функция**:

1.  Получает лист с именем 'campaign'.
2.  Подготавливает данные для записи в виде списка кортежей, содержащих ячейку, заголовок и значение.
3.  Формирует список операций обновления для пакетной записи данных в Google Sheets.
4.  Выполняет пакетное обновление листа, записывая заголовки и значения в соответствующие ячейки.
5.  Логирует успешную запись данных кампании.
6.  Обрабатывает возможные исключения, возникающие при записи, логирует ошибки и поднимает исключение.

**Примеры**:

```python
campaign_data = SimpleNamespace(name='Test Campaign', title='Test Title', language='ru', currency='USD', description='Test Description')
campaign_sheet.set_campaign_worksheet(campaign_data)
```

#### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
    """
    Записывает данные о продуктах из списка объектов SimpleNamespace в ячейки Google Sheets.
    
    Args:
        category_name (str): Название категории для получения продуктов.
    
    Raises:
        Exception: Если возникает ошибка при записи данных о продуктах.
    """
```

**Назначение**:
Записывает данные о продуктах из указанной категории в лист Google Sheets.

**Как работает функция**:

1.  Получает категорию и список продуктов из редактора кампании.
2.  Копирует лист 'product' и переименовывает его в название категории.
3.  Формирует список данных для записи в виде списка списков, где каждый внутренний список представляет строку с данными о продукте.
4.  Выполняет обновление листа, записывая данные о продуктах в соответствующие ячейки.
5.  Форматирует лист с продуктами категории.
6.  Логирует успешную запись данных о продуктах.
7.  Обрабатывает возможные исключения, возникающие при записи, логирует ошибки и поднимает исключение.

**Примеры**:

```python
campaign_sheet.set_products_worksheet(category_name='Category1')
```

#### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """
    Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    
    Args:
        categories (SimpleNamespace): Объект, где ключи — это категории с данными для записи.
    
    Raises:
        Exception: Если возникает ошибка при обновлении полей из объекта SimpleNamespace.
    """
```

**Назначение**:
Записывает данные о категориях из объекта `SimpleNamespace` в лист Google Sheets с именем 'categories'.

**Как работает функция**:

1.  Получает лист с именем 'categories'.
2.  Очищает лист перед записью данных.
3.  Получает данные о категориях из объекта `SimpleNamespace`.
4.  Проверяет, что все объекты категорий имеют необходимые атрибуты ('name', 'title', 'description', 'tags', 'products_count').
5.  Формирует заголовки таблицы.
6.  Формирует список данных для записи в виде списка списков, где каждый внутренний список представляет строку с данными о категории.
7.  Выполняет обновление листа, записывая заголовки и данные о категориях в соответствующие ячейки.
8.  Форматирует лист категорий.
9.  Логирует успешную запись данных о категориях.
10. Обрабатывает возможные исключения, возникающие при записи, логирует ошибки и поднимает исключение.

**Примеры**:

```python
categories_data = SimpleNamespace(
    Category1=SimpleNamespace(name='Name1', title='Title1', description='Description1', tags=['Tag1', 'Tag2'], products_count=10),
    Category2=SimpleNamespace(name='Name2', title='Title2', description='Description2', tags=['Tag3', 'Tag4'], products_count=20)
)
campaign_sheet.set_categories_worksheet(categories_data)
```

#### `get_categories`

```python
def get_categories(self):
    """
    Получение данных из таблицы Google Sheets.
    
    Returns:
        Данные из таблицы в виде списка словарей.
    """
```

**Назначение**:
Получает данные о категориях из листа Google Sheets с именем 'categories'.

**Как работает функция**:

1.  Получает лист с именем 'categories'.
2.  Получает все записи из листа в виде списка словарей.
3.  Логирует успешное получение данных о категориях.
4.  Возвращает полученные данные.

**Примеры**:

```python
categories = campaign_sheet.get_categories()
```

#### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict):
    """
    Запись данных о продуктах в новую таблицу Google Sheets.
    
    Args:
        category_name Название категории.
        products Словарь с данными о продуктах.
    """
```

**Назначение**:
Записывает данные о продуктах для указанной категории в новый лист Google Sheets.

**Как работает функция**:

1.  Получает категорию и список продуктов из редактора кампании.
2.  Копирует лист 'product' и переименовывает его в название категории.
3.  Определяет заголовки для таблицы продуктов.
4.  Формирует список данных для записи, преобразуя данные каждого продукта в список.
5.  Выполняет пакетное обновление листа, добавляя заголовки и данные о продуктах.
6.  Форматирует лист с продуктами категории.
7.  Логирует успешное обновление данных о продуктах.
8.  Обрабатывает возможные исключения, возникающие в процессе, и логирует ошибки.

**Примеры**:

```python
products_data = [{'product_id': '123', 'app_sale_price': '10.00', 'original_price': '12.00', 'sale_price': '11.00', 'discount': '10%', 'product_title': 'Product 1'},
                 {'product_id': '456', 'app_sale_price': '20.00', 'original_price': '24.00', 'sale_price': '22.00', 'discount': '8%', 'product_title': 'Product 2'}]
campaign_sheet.set_category_products(category_name='Category1', products=products_data)
```

#### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """
    Форматирование листа 'categories'.
    
    Args:
        ws Лист Google Sheets для форматирования.
    """
```

**Назначение**:
Форматирует лист Google Sheets с категориями, устанавливая ширину столбцов, высоту строк и форматирование заголовков.

**Как работает функция**:

1.  Устанавливает ширину столбцов A, B, C, D и E.
2.  Устанавливает высоту строки заголовков.
3.  Определяет формат для заголовков, включая жирный шрифт, размер шрифта, выравнивание и цвет фона.
4.  Применяет формат заголовков к диапазону ячеек A1:E1.
5.  Логирует успешное форматирование листа категорий.
6.  Обрабатывает возможные исключения, возникающие при форматировании, и логирует ошибки.

**Примеры**:

```python
ws = campaign_sheet.get_worksheet('categories')
campaign_sheet._format_categories_worksheet(ws)
```

#### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
    """
    Форматирование листа с продуктами категории.
    
    Args:
        ws Лист Google Sheets для форматирования.
    """
```

**Назначение**:
Форматирует лист Google Sheets с продуктами категории, устанавливая ширину столбцов, высоту строк и форматирование заголовков.

**Как работает функция**:

1.  Устанавливает ширину для столбцов от A до Y.
2.  Устанавливает высоту для первой строки (заголовков).
3.  Определяет формат для заголовков, включая жирный шрифт, размер шрифта, выравнивание и цвет фона.
4.  Применяет формат заголовков к диапазону ячеек A1:Y1.
5.  Логирует успешное форматирование листа продуктов категории.
6.  Обрабатывает возможные исключения, возникающие при форматировании, и логирует ошибки.

**Примеры**:

```python
ws = campaign_sheet.get_worksheet('Category1')
campaign_sheet._format_category_products_worksheet(ws)