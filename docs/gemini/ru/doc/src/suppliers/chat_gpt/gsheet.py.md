# Модуль `gsheet.py`

## Обзор

Модуль `gsheet.py` представляет собой класс `GptGs`, который расширяет функциональность класса `SpreadSheet` для управления Google Sheets в контексте кампаний AliExpress. Этот модуль позволяет читать, записывать и форматировать данные кампаний, категорий и продуктов в Google Sheets.

## Оглавление

- [Классы](#классы)
  - [`GptGs`](#gptgs)
- [Функции](#функции)
  - [`__init__`](#__init__)
  - [`clear`](#clear)
  - [`update_chat_worksheet`](#update_chat_worksheet)
  - [`get_campaign_worksheet`](#get_campaign_worksheet)
  - [`set_category_worksheet`](#set_category_worksheet)
  - [`get_category_worksheet`](#get_category_worksheet)
  - [`set_categories_worksheet`](#set_categories_worksheet)
  - [`get_categories_worksheet`](#get_categories_worksheet)
  - [`set_product_worksheet`](#set_product_worksheet)
  - [`get_product_worksheet`](#get_product_worksheet)
  - [`set_products_worksheet`](#set_products_worksheet)
  - [`delete_products_worksheets`](#delete_products_worksheets)
  - [`save_categories_from_worksheet`](#save_categories_from_worksheet)
  - [`save_campaign_from_worksheet`](#save_campaign_from_worksheet)

## Классы

### `GptGs`

**Описание**: Класс для управления Google Sheets в контексте кампаний AliExpress.

**Наследует**:
- `SpreadSheet`

**Методы**:
- [`__init__`](#__init__): Инициализирует класс `GptGs`.
- [`clear`](#clear): Очищает содержимое Google Sheets.
- [`update_chat_worksheet`](#update_chat_worksheet): Записывает данные чата в Google Sheets.
- [`get_campaign_worksheet`](#get_campaign_worksheet): Читает данные кампании из Google Sheets.
- [`set_category_worksheet`](#set_category_worksheet): Записывает данные категории в Google Sheets.
- [`get_category_worksheet`](#get_category_worksheet): Читает данные категории из Google Sheets.
- [`set_categories_worksheet`](#set_categories_worksheet): Записывает данные категорий в Google Sheets.
- [`get_categories_worksheet`](#get_categories_worksheet): Читает данные категорий из Google Sheets.
- [`set_product_worksheet`](#set_product_worksheet): Записывает данные продукта в Google Sheets.
- [`get_product_worksheet`](#get_product_worksheet): Читает данные продукта из Google Sheets.
- [`set_products_worksheet`](#set_products_worksheet): Записывает данные продуктов в Google Sheets.
- [`delete_products_worksheets`](#delete_products_worksheets): Удаляет листы продуктов из Google Sheets.
- [`save_categories_from_worksheet`](#save_categories_from_worksheet): Сохраняет данные категорий из Google Sheets.
- [`save_campaign_from_worksheet`](#save_campaign_from_worksheet): Сохраняет данные кампании из Google Sheets.

## Функции

### `__init__`

**Описание**: Инициализирует класс `GptGs` с указанным ID Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `category_name` (str): Имя категории.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.

**Возвращает**:
- `None`

### `clear`

**Описание**: Очищает содержимое Google Sheets, удаляя листы продуктов и данные категорий и кампаний.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при очистке.

### `update_chat_worksheet`

**Описание**: Записывает данные чата в указанный лист Google Sheets.

**Параметры**:
- `data` (SimpleNamespace | dict | list): Данные для записи в виде объекта `SimpleNamespace`, словаря или списка.
- `conversation_name` (str): Название листа, куда нужно записать данные.
- `language` (str, optional): Необязательный параметр языка. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при записи данных.

### `get_campaign_worksheet`

**Описание**: Читает данные кампании из листа 'campaign' Google Sheets.

**Параметры**:
- `None`

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с данными кампании.

**Вызывает исключения**:
- `ValueError`: Если лист 'campaign' не найден.
- `Exception`: Если происходит ошибка при чтении данных.

### `set_category_worksheet`

**Описание**: Записывает данные категории из объекта `SimpleNamespace` в Google Sheets вертикально.

**Параметры**:
- `category` (SimpleNamespace | str): Объект `SimpleNamespace` с данными категории или имя категории.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `TypeError`: Если `category` не является `SimpleNamespace`.
- `Exception`: Если происходит ошибка при записи данных.

### `get_category_worksheet`

**Описание**: Читает данные категории из листа 'category' Google Sheets.

**Параметры**:
- `None`

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с данными категории.

**Вызывает исключения**:
- `ValueError`: Если лист 'category' не найден.
- `Exception`: Если происходит ошибка при чтении данных.

### `set_categories_worksheet`

**Описание**: Записывает данные из объекта `SimpleNamespace` в Google Sheets на лист 'categories'.

**Параметры**:
- `categories` (SimpleNamespace): Объект `SimpleNamespace`, содержащий данные категорий.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при записи данных.

### `get_categories_worksheet`

**Описание**: Читает данные из листа 'categories' Google Sheets, начиная со второй строки, и возвращает их в виде списка списков.

**Параметры**:
- `None`

**Возвращает**:
- `List[List[str]]`: Список списков строк, представляющих данные категорий.

**Вызывает исключения**:
- `ValueError`: Если лист 'categories' не найден.
- `Exception`: Если происходит ошибка при чтении данных.

### `set_product_worksheet`

**Описание**: Записывает данные продукта в новый лист Google Sheets, копируя шаблон 'product_template'.

**Параметры**:
- `product` (SimpleNamespace | str): Объект `SimpleNamespace` с данными продукта или имя продукта.
- `category_name` (str): Имя категории, которой принадлежит продукт.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при записи данных.

### `get_product_worksheet`

**Описание**: Читает данные продукта из листа 'products' Google Sheets.

**Параметры**:
- `None`

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с данными продукта.

**Вызывает исключения**:
- `ValueError`: Если лист 'products' не найден.
- `Exception`: Если происходит ошибка при чтении данных.

### `set_products_worksheet`

**Описание**: Записывает данные списка объектов `SimpleNamespace` в Google Sheets на лист с именем категории.

**Параметры**:
- `category_name` (str): Название категории.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при записи данных.

### `delete_products_worksheets`

**Описание**: Удаляет все листы Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при удалении листов.

### `save_categories_from_worksheet`

**Описание**: Сохраняет данные категорий, отредактированные в Google Sheets, и обновляет их в объекте кампании.

**Параметры**:
- `update` (bool, optional): Флаг для обновления данных кампании. По умолчанию `False`.

**Возвращает**:
- `None`

### `save_campaign_from_worksheet`

**Описание**: Сохраняет данные рекламной кампании из Google Sheets и обновляет объект кампании.

**Параметры**:
- `None`

**Возвращает**:
- `None`