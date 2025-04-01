# Модуль для работы с Google Sheets в кампаниях AliExpress
## Обзор

Модуль `gsheet.py` предназначен для автоматизации работы с Google Sheets в рамках рекламных кампаний на AliExpress. Он включает в себя функциональность для создания, редактирования и форматирования таблиц, записи данных о категориях и продуктах, а также для управления листами Google Sheets. Модуль использует библиотеку `gspread` для взаимодействия с Google Sheets API и предоставляет удобные методы для работы с данными кампаний.

## Подробнее

Модуль `AliCampaignGoogleSheet` наследует функциональность из класса `SpreadSheet` и расширяет её, добавляя методы для работы с данными рекламных кампаний AliExpress. Он позволяет автоматизировать процесс заполнения таблиц данными о категориях и продуктах, что упрощает управление рекламными кампаниями.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress. Предоставляет методы для управления листами, записи данных о категориях и продуктах, а также для форматирования листов.

**Наследует**:
- `SpreadSheet`: Расширяет класс `SpreadSheet`, добавляя специфическую логику для работы с кампаниями AliExpress.

**Атрибуты**:
- `spreadsheet_id` (str): Идентификатор Google Sheets spreadsheet.
- `spreadsheet` (SpreadSheet): Объект SpreadSheet для работы с таблицей.
- `worksheet` (Worksheet): Текущий рабочий лист.

**Методы**:
- `__init__(campaign_name: str, language: str | dict = None, currency: str = None)`: Инициализирует класс AliCampaignGoogleSheet.
- `clear()`: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.
- `delete_products_worksheets()`: Удаляет все листы, кроме 'categories', 'product', 'category', 'campaign'.
- `set_campaign_worksheet(campaign: SimpleNamespace)`: Записывает данные кампании в лист Google Sheets.
- `set_products_worksheet(category_name: str)`: Записывает данные о продуктах в лист Google Sheets.
- `set_categories_worksheet(categories: SimpleNamespace)`: Записывает данные о категориях в лист Google Sheets.
- `get_categories()`: Получает данные о категориях из листа Google Sheets.
- `set_category_products(category_name: str, products: dict)`: Записывает данные о продуктах категории в лист Google Sheets.
- `_format_categories_worksheet(ws: Worksheet)`: Форматирует лист 'categories'.
- `_format_category_products_worksheet(ws: Worksheet)`: Форматирует лист с продуктами категории.

## Функции

### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
```

**Назначение**: Инициализирует класс `AliCampaignGoogleSheet` с указанным ID таблицы Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Как работает функция**:
1. Инициализирует класс `SpreadSheet` с использованием `spreadsheet_id` класса `AliCampaignGoogleSheet`.
2. Сохраняет параметры `campaign_name`, `language` и `currency` для дальнейшего использования.

**Примеры**:
```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale', language='ru', currency='USD')
```

### `clear`

```python
def clear(self):
```

**Назначение**: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.

**Как работает функция**:
1. Пытается удалить листы продуктов, вызывая метод `delete_products_worksheets`.
2. Ловит исключение, если происходит ошибка при очистке, и записывает сообщение об ошибке в лог.

```
Очистка Google Sheets
│
├── Удаление листов продуктов (delete_products_worksheets)
│   │
│   └── Обработка исключений (если возникли ошибки)
│
└── Запись сообщения об ошибке в лог (в случае исключения)
```

**Примеры**:
```python
campaign_sheet.clear()
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
```

**Назначение**: Удаляет все листы из таблицы Google Sheets, за исключением листов с названиями 'categories', 'product', 'category', 'campaign'.

**Как работает функция**:
1. Определяет список исключенных названий листов (`excluded_titles`).
2. Получает список всех листов в таблице Google Sheets.
3. Перебирает листы и удаляет каждый лист, название которого отсутствует в списке исключенных.
4. Ловит исключения, если происходит ошибка при удалении листов, и записывает сообщение об ошибке в лог.

```
Получение списка листов из Google Sheets
│
├── Перебор листов
│   │
│   ├── Проверка наличия имени листа в списке исключений
│   │   │
│   │   └── Удаление листа (если имя отсутствует в списке исключений)
│   │
│   └── Запись сообщения об успешном удалении в лог
│
└── Обработка исключений (если возникли ошибки при удалении листов)
    │
    └── Запись сообщения об ошибке в лог
```

**Примеры**:
```python
campaign_sheet.delete_products_worksheets()
```

### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace):
```

**Назначение**: Записывает данные кампании в указанный лист Google Sheets.

**Параметры**:
- `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании для записи.

**Как работает функция**:
1. Получает лист Google Sheets с именем 'campaign'.
2. Формирует список операций обновления для записи данных кампании в вертикальном формате.
3. Выполняет пакетное обновление листа Google Sheets с данными кампании.
4. Ловит исключения, если происходит ошибка при записи данных, и записывает сообщение об ошибке в лог.

```
Получение листа 'campaign' из Google Sheets
│
├── Подготовка данных для вертикальной записи
│   │
│   └── Формирование списка операций обновления
│
├── Выполнение пакетного обновления листа
│
└── Обработка исключений (если возникли ошибки при записи данных)
    │
    └── Запись сообщения об ошибке в лог
```

**Примеры**:
```python
from types import SimpleNamespace
campaign_data = SimpleNamespace(campaign_name='SummerSale', title='Hot Deals', language='ru', currency='USD', description='Amazing summer discounts!')
campaign_sheet.set_campaign_worksheet(campaign_data)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
```

**Назначение**: Записывает данные о продуктах из указанной категории в лист Google Sheets.

**Параметры**:
- `category_name` (str): Название категории, продукты которой нужно записать.

**Как работает функция**:
1. Получает категорию и список продуктов из атрибута `editor.campaign.category`.
2. Копирует лист 'product' и присваивает ему имя `category_name`.
3. Формирует список данных для записи в лист Google Sheets.
4. Обновляет лист Google Sheets данными о продуктах.
5. Форматирует лист с продуктами, вызывая метод `_format_category_products_worksheet`.
6. Ловит исключения, если происходит ошибка при записи данных, и записывает сообщение об ошибке в лог.

```
Получение категории и списка продуктов
│
├── Копирование листа 'product'
│   │
│   └── Присвоение листу имени категории
│
├── Формирование списка данных для записи
│   │
│   └── Преобразование данных о продуктах в формат строк
│
├── Обновление листа Google Sheets
│
├── Форматирование листа продуктов
│
└── Обработка исключений (если возникли ошибки при записи данных)
    │
    └── Запись сообщения об ошибке в лог
```

**Примеры**:
```python
campaign_sheet.set_products_worksheet(category_name='electronics')
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
```

**Назначение**: Записывает данные из объекта `SimpleNamespace` с категориями в ячейки Google Sheets.

**Параметры**:
- `categories` (SimpleNamespace): Объект, где ключи — это категории с данными для записи.

**Как работает функция**:
1. Получает лист Google Sheets с именем 'categories'.
2. Очищает рабочий лист перед записью данных.
3. Извлекает данные категорий из объекта `SimpleNamespace`.
4. Проверяет, что все объекты категории имеют необходимые атрибуты (`name`, `title`, `description`, `tags`, `products_count`).
5. Записывает заголовки в первую строку листа.
6. Подготавливает данные для записи, извлекая значения атрибутов из каждого объекта категории.
7. Обновляет строки данных в листе Google Sheets.
8. Вызывает метод `_format_categories_worksheet` для форматирования таблицы.
9. Ловит исключения, если происходит ошибка при обновлении данных, и записывает сообщение об ошибке в лог.

```
Получение листа 'categories' из Google Sheets
│
├── Очистка рабочего листа
│
├── Извлечение данных категорий из SimpleNamespace
│
├── Проверка наличия необходимых атрибутов у объектов категории
│
├── Запись заголовков в первую строку листа
│
├── Подготовка данных для записи (извлечение значений атрибутов)
│
├── Обновление строк данных в листе Google Sheets
│
├── Форматирование таблицы
│
└── Обработка исключений (если возникли ошибки при обновлении данных)
    │
    └── Запись сообщения об ошибке в лог
```

**Примеры**:
```python
from types import SimpleNamespace
categories_data = SimpleNamespace(
    category1=SimpleNamespace(name='electronics', title='Electronics', description='Cool gadgets', tags=['gadgets', 'tech'], products_count=100),
    category2=SimpleNamespace(name='clothing', title='Clothing', description='Fashionable clothes', tags=['fashion', 'clothes'], products_count=50)
)
campaign_sheet.set_categories_worksheet(categories_data)
```

### `get_categories`

```python
def get_categories(self):
```

**Назначение**: Получает данные из таблицы Google Sheets.

**Возвращает**:
- Данные из таблицы в виде списка словарей.

**Как работает функция**:
1. Получает лист Google Sheets с именем 'categories'.
2. Извлекает все записи из листа в виде списка словарей.
3. Записывает сообщение об успешном извлечении данных в лог.
4. Возвращает полученные данные.

```
Получение листа 'categories' из Google Sheets
│
├── Извлечение всех записей из листа
│
├── Запись сообщения об успешном извлечении в лог
│
└── Возврат полученных данных
```

**Примеры**:
```python
categories = campaign_sheet.get_categories()
print(categories)
```

### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict):
```

**Назначение**: Записывает данные о продуктах в новую таблицу Google Sheets.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (dict): Словарь с данными о продуктах.

**Как работает функция**:
1. Получает категорию и список продуктов.
2. Копирует лист 'product' и присваивает ему имя `category_name`.
3. Определяет заголовки для таблицы продуктов.
4. Формирует список данных о продуктах для записи в таблицу.
5. Обновляет лист Google Sheets, записывая данные о продуктах.
6. Вызывает метод `_format_category_products_worksheet` для форматирования таблицы.
7. Ловит исключения, если происходит ошибка при обновлении данных, и записывает сообщение об ошибке в лог.

```
Получение категории и списка продуктов
│
├── Копирование листа 'product'
│   │
│   └── Присвоение листу имени категории
│
├── Определение заголовков таблицы
│
├── Формирование списка данных о продуктах
│
├── Обновление листа Google Sheets
│
├── Форматирование таблицы
│
└── Обработка исключений (если возникли ошибки при обновлении данных)
    │
    └── Запись сообщения об ошибке в лог
```

**Примеры**:
```python
products_data = [
    {'product_id': '123', 'app_sale_price': '20.00', 'original_price': '25.00', 'sale_price': '22.00', 'discount': '20%', 'product_title': 'Awesome Gadget'},
    {'product_id': '456', 'app_sale_price': '30.00', 'original_price': '35.00', 'sale_price': '32.00', 'discount': '15%', 'product_title': 'Cool Device'}
]
campaign_sheet.set_category_products(category_name='gadgets', products=products_data)
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
```

**Назначение**: Форматирует лист 'categories'.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:
1. Устанавливает ширину столбцов A, B, C, D и E.
2. Устанавливает высоту строки заголовков.
3. Определяет формат для заголовков, включая жирный шрифт, размер шрифта, выравнивание и цвет фона.
4. Применяет формат заголовков к диапазону ячеек A1:E1.
5. Ловит исключения, если происходит ошибка при форматировании листа, и записывает сообщение об ошибке в лог.

```
Установка ширины столбцов
│
├── Установка высоты строки заголовков
│
├── Определение формата для заголовков
│
├── Применение формата к диапазону ячеек A1:E1
│
└── Обработка исключений (если возникли ошибки при форматировании)
    │
    └── Запись сообщения об ошибке в лог
```

**Примеры**:
```python
ws = campaign_sheet.get_worksheet('categories')
campaign_sheet._format_categories_worksheet(ws)
```

### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
```

**Назначение**: Форматирует лист с продуктами категории.

**Параметры**:
- `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:
1. Устанавливает ширину столбцов от A до Y.
2. Устанавливает высоту строки заголовков.
3. Определяет формат для заголовков, включая жирный шрифт, размер шрифта, выравнивание и цвет фона.
4. Применяет формат заголовков к диапазону ячеек A1:Y1.
5. Ловит исключения, если происходит ошибка при форматировании листа, и записывает сообщение об ошибке в лог.

```
Установка ширины столбцов (A-Y)
│
├── Установка высоты строки заголовков
│
├── Определение формата для заголовков
│
├── Применение формата к диапазону ячеек A1:Y1
│
└── Обработка исключений (если возникли ошибки при форматировании)
    │
    └── Запись сообщения об ошибке в лог
```

**Примеры**:
```python
ws = campaign_sheet.get_worksheet('products')
campaign_sheet._format_category_products_worksheet(ws)