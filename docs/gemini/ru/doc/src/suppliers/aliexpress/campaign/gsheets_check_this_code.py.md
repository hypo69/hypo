# Модуль: Редактор рекламной кампании через Google Sheets

## Обзор

Модуль `src.suppliers.aliexpress.campaign.gsheets_check_this_code` предоставляет класс `AliCampaignGoogleSheet` для работы с Google Sheets в рамках управления рекламными кампаниями AliExpress. Он позволяет автоматизировать процесс создания, обновления и форматирования таблиц с данными о кампаниях, категориях и продуктах. Модуль интегрирован с Google Sheets API, что обеспечивает удобное взаимодействие с данными рекламных кампаний.

## Подробнее

Этот модуль является частью системы управления рекламными кампаниями AliExpress и предназначен для упрощения работы с данными, хранящимися в Google Sheets. Класс `AliCampaignGoogleSheet` предоставляет методы для очистки таблиц, удаления листов продуктов, установки данных кампании и категорий, а также для форматирования таблиц. Использование этого модуля позволяет автоматизировать рутинные задачи и повысить эффективность управления рекламными кампаниями.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс `AliCampaignGoogleSheet` предназначен для работы с Google Sheets в рамках кампаний AliExpress.

**Наследует**:

- `SpreadSheet` - класс для работы с Google Sheets API.

**Атрибуты**:

- `spreadsheet_id` (str): ID Google Sheets таблицы.
- `spreadsheet` (SpreadSheet): Экземпляр класса SpreadSheet для работы с таблицей.
- `worksheet` (Worksheet): Текущий рабочий лист Google Sheets.
- `driver` (Driver): Драйвер для управления браузером (например, Chrome) для открытия Google Sheets.
- `editor` (AliCampaignEditor): Редактор кампании AliExpress для получения данных о кампании, категориях и продуктах.

**Методы**:

- `__init__(campaign_name: str, language: str | dict = None, currency: str = None)`: Инициализация класса `AliCampaignGoogleSheet` с указанием ID таблицы Google Sheets и дополнительных параметров.
- `clear()`: Очистка содержимого Google Sheets, удаление листов продуктов и очистка данных на листах категорий и других указанных листах.
- `delete_products_worksheets()`: Удаление всех листов из Google Sheets, кроме листов `categories`, `product`, `category`, `campaign`.
- `set_campaign_worksheet(campaign: SimpleNamespace)`: Запись данных о кампании в лист Google Sheets.
- `set_products_worksheet(category_name: str)`: Запись данных о продуктах из указанной категории в лист Google Sheets.
- `set_categories_worksheet(categories: SimpleNamespace)`: Запись данных о категориях в лист Google Sheets.
- `get_categories()`: Получение данных о категориях из листа Google Sheets.
- `set_category_products(category_name: str, products: dict)`: Запись данных о продуктах категории в Google Sheets.
- `_format_categories_worksheet(ws: Worksheet)`: Форматирование листа `categories` в Google Sheets.
- `_format_category_products_worksheet(ws: Worksheet)`: Форматирование листа с продуктами категории в Google Sheets.

### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
    """ Инициализация AliCampaignGoogleSheet с указанным ID таблицы Google Sheets и дополнительными параметрами.
    Args:
        campaign_name (str): Название кампании.
        language (str | dict, optional): Язык кампании. По умолчанию None.
        currency (str, optional): Валюта кампании. По умолчанию None.

    Raises:
        Exception: Если возникает ошибка при инициализации.
    """
    ...
```

**Назначение**: Инициализация экземпляра класса `AliCampaignGoogleSheet`.

**Параметры**:

- `campaign_name` (str): Имя кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Как работает функция**:

1.  Вызывается конструктор родительского класса `SpreadSheet` с указанием `spreadsheet_id`.
2.  Инициализируется `AliCampaignEditor` с переданными параметрами кампании.
3.  Выполняется очистка Google Sheets с помощью метода `clear()`.
4.  Устанавливается рабочий лист для данных кампании с помощью `set_campaign_worksheet()`.
5.  Устанавливается рабочий лист для данных категорий с помощью `set_categories_worksheet()`.
6.  Открывается Google Sheets в браузере с использованием драйвера `webdriver`.

**ASCII flowchart**:

```
A: Инициализация AliCampaignGoogleSheet
|
B: Инициализация SpreadSheet(spreadsheet_id)
|
C: Инициализация AliCampaignEditor(campaign_name, language, currency)
|
D: clear()
|
E: set_campaign_worksheet(self.editor.campaign)
|
F: set_categories_worksheet(self.editor.campaign.category)
|
G: self.driver.get_url(f'https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}')
```

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='ru', currency='USD')
```

### `clear`

```python
def clear(self):
    """ Очистка содержимого Google Sheets.
    Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.

    Raises:
        Exception: Если возникает ошибка при очистке.
    """
    ...
```

**Назначение**: Очистка содержимого Google Sheets, включая удаление листов продуктов и очистку данных на листах категорий и других указанных листах.

**Как работает функция**:

1.  Вызывается метод `delete_products_worksheets()` для удаления всех листов продуктов.
2.  Обрабатываются возможные исключения при удалении листов продуктов.

**ASCII flowchart**:

```
A: clear()
|
B: try
|
C: delete_products_worksheets()
|
D: except Exception as ex
|
E: logger.error("Ошибка очистки", ex)
```

**Примеры**:

```python
campaign_sheet.clear()
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ Удаляет все листы из Google Sheets, кроме 'categories', 'product', 'category', 'campaign'.

    Raises:
        Exception: Если возникает ошибка при удалении листов.
    """
    ...
```

**Назначение**: Удаление всех листов из Google Sheets, за исключением листов с названиями 'categories', 'product', 'category', 'campaign'.

**Как работает функция**:

1.  Определяется набор исключаемых названий листов (`excluded_titles`).
2.  Получается список всех листов в Google Sheets.
3.  Перебираются листы и удаляются те, чьи названия не входят в список исключений.
4.  Логируется успешное удаление каждого листа.
5.  Обрабатываются возможные исключения при удалении листов.

**ASCII flowchart**:

```
A: delete_products_worksheets()
|
B: excluded_titles = {'categories', 'product', 'category', 'campaign'}
|
C: try
|
D: worksheets = self.spreadsheet.worksheets()
|
E: for sheet in worksheets
|
F: if sheet.title not in excluded_titles
|
G: self.spreadsheet.del_worksheet_by_id(sheet.id)
|
H: logger.success(f"Worksheet '{sheet.title}' deleted.")
|
I: except Exception as ex
|
J: logger.error("Error deleting all worksheets.", ex, exc_info=True)
|
K: raise
```

**Примеры**:

```python
campaign_sheet.delete_products_worksheets()
```

### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace):
    """ Запись данных о кампании в лист Google Sheets.
    Args:
        campaign (SimpleNamespace): SimpleNamespace объект с данными кампании для записи.
    Raises:
        Exception: Если возникает ошибка при записи данных о кампании.
    """
    ...
```

**Назначение**: Запись данных о кампании в лист Google Sheets.

**Параметры**:

- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании для записи.

**Как работает функция**:

1.  Получается рабочий лист с названием `campaign`.
2.  Формируется список операций обновления для записи данных в ячейки.
3.  Выполняется пакетное обновление ячеек рабочего листа.
4.  Логируется успешная запись данных о кампании.
5.  Обрабатываются возможные исключения при записи данных.

**ASCII flowchart**:

```
A: set_campaign_worksheet(campaign)
|
B: try
|
C: ws: Worksheet = self.get_worksheet('campaign')
|
D: updates = []
|
E: vertical_data = [('A1', 'Campaign Name', campaign.name), ...]
|
F: for cell, header, value in vertical_data
|
G: updates.append({'range': cell, 'values': [[header]]})
|
H: updates.append({'range': f'B{cell[1]}', 'values': [[str(value)]]})
|
I: if updates
|
J: ws.batch_update(updates)
|
K: logger.info("Campaign data written to 'campaign' worksheet vertically.")
|
L: except Exception as ex
|
M: logger.error("Error setting campaign worksheet.", ex, exc_info=True)
|
N: raise
```

**Примеры**:

```python
from types import SimpleNamespace
campaign_data = SimpleNamespace(name='test_campaign', title='Test Campaign', language='ru', currency='USD', description='Test description')
campaign_sheet.set_campaign_worksheet(campaign_data)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
    """ Запись данных о продуктах из списка объектов SimpleNamespace в ячейки Google Sheets.
    Args:
        category_name (str): Название категории для получения продуктов.

    Raises:
        Exception: Если возникает ошибка при записи данных о продуктах.
    """
    ...
```

**Назначение**: Запись данных о продуктах из указанной категории в лист Google Sheets.

**Параметры**:

- `category_name` (str): Название категории для получения продуктов.

**Как работает функция**:

1.  Получается объект категории из `self.editor.campaign.category`.
2.  Получается список продуктов из объекта категории.
3.  Создается копия листа `product` с новым именем `category_name`.
4.  Формируются данные для записи в строки Google Sheets на основе данных продуктов.
5.  Выполняется обновление строк в Google Sheets.
6.  Вызывается метод `_format_category_products_worksheet` для форматирования листа.
7.  Логируется успешное обновление данных о продуктах.
8.  Обрабатываются возможные исключения при записи данных.

**ASCII flowchart**:

```
A: set_products_worksheet(category_name)
|
B: if category_name
|
C: category: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
|
D: products: list[SimpleNamespace] = category.products
|
E: else
|
F: logger.warning("No products found for category.")
|
G: return
|
H: ws = self.copy_worksheet('product', category_name)
|
I: try
|
J: row_data = []
|
K: for product in products
|
L: _ = product.__dict__
|
M: row_data.append([str(_.get('product_id')), ...])
|
N: for index, row in enumerate(row_data, start=2)
|
O: ws.update(f'A{index}:Y{index}', [row])
|
P: logger.info(f"Products {str(_.get('product_id'))} updated .")
|
Q: self._format_category_products_worksheet(ws)
|
R: logger.info("Products updated in worksheet.")
|
S: except Exception as ex
|
T: logger.error("Error setting products worksheet.", ex, exc_info=True)
|
U: raise
```

**Примеры**:

```python
campaign_sheet.set_products_worksheet(category_name='some_category')
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    Args:
        categories (SimpleNamespace): Объект, где ключи — это категории с данными для записи.

    Raises:
        Exception: Если возникает ошибка при обновлении полей из объекта SimpleNamespace.
    """
    ...
```

**Назначение**: Запись данных о категориях в лист Google Sheets.

**Параметры**:

- `categories` (SimpleNamespace): Объект SimpleNamespace, содержащий данные о категориях.

**Как работает функция**:

1.  Получается рабочий лист с названием `categories`.
2.  Очищается рабочий лист.
3.  Получаются данные о категориях из объекта `categories`.
4.  Проверяется наличие необходимых атрибутов у объектов категорий.
5.  Формируются заголовки и строки данных для записи в Google Sheets.
6.  Выполняется обновление данных в Google Sheets.
7.  Вызывается метод `_format_categories_worksheet` для форматирования листа.
8.  Логируется успешное обновление данных о категориях.
9.  Обрабатываются возможные исключения при записи данных.

**ASCII flowchart**:

```
A: set_categories_worksheet(categories)
|
B: ws: Worksheet = self.get_worksheet('categories')
|
C: ws.clear()
|
D: try
|
E: category_data = categories.__dict__
|
F: required_attrs = ['name', 'title', 'description', 'tags', 'products_count']
|
G: if all(all(hasattr(category, attr) for attr in required_attrs) for category in category_data.values())
|
H: headers = ['Name', 'Title', 'Description', 'Tags', 'Products Count']
|
I: ws.update('A1:E1', [headers])
|
J: rows = []
|
K: for category in category_data.values()
|
L: row_data = [category.name, category.title, category.description, ', '.join(category.tags), category.products_count]
|
M: rows.append(row_data)
|
N: ws.update(f'A2:E{1 + len(rows)}', rows)
|
O: self._format_categories_worksheet(ws)
|
P: logger.info("Category fields updated from SimpleNamespace object.")
|
Q: else
|
R: logger.warning("One or more category objects do not contain all required attributes.")
|
S: except Exception as ex
|
T: logger.error("Error updating fields from SimpleNamespace object.", ex, exc_info=True)
|
U: raise
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
def get_categories(self):
    """ Получение данных из таблицы Google Sheets.
    Returns:
        Данные из таблицы в виде списка словарей.
    """
    ...
```

**Назначение**: Получение данных о категориях из листа Google Sheets.

**Возвращает**:

- `list[dict]`: Данные из таблицы в виде списка словарей.

**Как работает функция**:

1.  Получается рабочий лист с названием `categories`.
2.  Получаются все записи из рабочего листа в виде списка словарей.
3.  Логируется успешное получение данных о категориях.
4.  Возвращаются полученные данные.

**ASCII flowchart**:

```
A: get_categories()
|
B: ws = self.get_worksheet('categories')
|
C: data = ws.get_all_records()
|
D: logger.info("Categories data retrieved from worksheet.")
|
E: return data
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
    Args:
        category_name Название категории.
        products Словарь с данными о продуктах.
    """
    ...
```

**Назначение**: Запись данных о продуктах в новую таблицу Google Sheets.

**Параметры**:

- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Как работает функция**:

1.  Получается объект категории из `self.editor.campaign.category`.
2.  Получается список продуктов из объекта категории.
3.  Создается копия листа `product` с новым именем `category_name`.
4.  Определяются заголовки для таблицы продуктов.
5.  Формируются данные для записи в строки Google Sheets на основе данных продуктов.
6.  Выполняется обновление строк в Google Sheets.
7.  Вызывается метод `_format_category_products_worksheet` для форматирования листа.
8.  Логируется успешное обновление данных о продуктах.
9.  Обрабатываются возможные исключения при записи данных.

**ASCII flowchart**:

```
A: set_category_products(category_name, products)
|
B: if category_name
|
C: category_ns: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
|
D: products_ns: list[SimpleNamespace] = category_ns.products
|
E: else
|
F: logger.warning("No products found for category.")
|
G: return
|
H: ws = self.copy_worksheet('product', category_name)
|
I: try
|
J: headers = ['product_id', ...]
|
K: updates = [{'range': 'A1:Y1', 'values': [headers]}]
|
L: row_data = []
|
M: for product in products
|
N: _ = product.__dict__
|
O: row_data.append([str(_.get('product_id')), ...])
|
P: for index, row in enumerate(row_data, start=2)
|
Q: ws.update(f'A{index}:Y{index}', [row])
|
R: logger.info(f"Products {str(_.get('product_id'))} updated .")
|
S: self._format_category_products_worksheet(ws)
|
T: logger.info("Products updated in worksheet.")
|
U: except Exception as ex
|
V: logger.error("Error updating products in worksheet.", ex, exc_info=True)
|
W: raise
```

**Примеры**:

```python
campaign_sheet.set_category_products(category_name='some_category', products=[{'product_id': 1, 'app_sale_price': 10.0}])
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """ Форматирование листа 'categories'.
    Args:
        ws Лист Google Sheets для форматирования.
    """
    ...
```

**Назначение**: Форматирование листа `categories` в Google Sheets.

**Параметры**:

- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:

1.  Устанавливается ширина столбцов.
2.  Устанавливается высота строк.
3.  Форматируются заголовки (жирный шрифт, выравнивание, цвет фона).
4.  Логируется успешное форматирование листа.
5.  Обрабатываются возможные исключения при форматировании.

**ASCII flowchart**:

```
A: _format_categories_worksheet(ws)
|
B: try
|
C: set_column_width(ws, 'A:A', 150)
|
D: set_column_width(ws, 'B:B', 200)
|
E: set_column_width(ws, 'C:C', 300)
|
F: set_column_width(ws, 'D:D', 200)
|
G: set_column_width(ws, 'E:E', 150)
|
H: set_row_height(ws, '1:1', 40)
|
I: header_format = cellFormat(textFormat=textFormat(bold=True, fontSize=12), horizontalAlignment='CENTER', verticalAlignment='MIDDLE', backgroundColor=Color(0.8, 0.8, 0.8))
|
J: format_cell_range(ws, 'A1:E1', header_format)
|
K: logger.info("Categories worksheet formatted.")
|
L: except Exception as ex
|
M: logger.error("Error formatting categories worksheet.", ex, exc_info=True)
|
N: raise
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
    Args:
        ws Лист Google Sheets для форматирования.
    """
    ...
```

**Назначение**: Форматирование листа с продуктами категории в Google Sheets.

**Параметры**:

- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:

1.  Устанавливается ширина столбцов.
2.  Устанавливается высота строк.
3.  Форматируются заголовки (жирный шрифт, выравнивание, цвет фона).
4.  Логируется успешное форматирование листа.
5.  Обрабатываются возможные исключения при форматировании.

**ASCII flowchart**:

```
A: _format_category_products_worksheet(ws)
|
B: try
|
C: set_column_width(ws, 'A:A', 250)
|
D: set_column_width(ws, 'B:B', 220)
|
...
|
Y: set_column_width(ws, 'Y:Y', 200)
|
Z: set_row_height(ws, '1:1', 40)
|
AA: header_format = cellFormat(textFormat=textFormat(bold=True, fontSize=12), horizontalAlignment='CENTER', verticalAlignment='TOP', backgroundColor=Color(0.8, 0.8, 0.8))
|
BB: format_cell_range(ws, 'A1:Y1', header_format)
|
CC: logger.info("Category products worksheet formatted.")
|
DD: except Exception as ex
|
EE: logger.error("Error formatting category products worksheet.", ex, exc_info=True)
|
FF: raise
```

**Примеры**:

```python
ws = campaign_sheet.get_worksheet('some_category')
campaign_sheet._format_category_products_worksheet(ws)
```