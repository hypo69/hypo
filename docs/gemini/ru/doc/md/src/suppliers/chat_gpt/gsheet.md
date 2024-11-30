# Модуль hypotez/src/suppliers/chat_gpt/gsheet.py

## Обзор

Модуль `gsheet.py` предоставляет класс `GptGs` для управления Google Таблицами в контексте кампаний AliExpress.  Класс наследуется от `SpreadSheet` и предоставляет методы для чтения, записи и обновления данных о категориях, продуктах и кампаниях в Google Таблицах.  Он также включает функциональность для удаления ненужных листов.


## Классы

### `GptGs`

**Описание**: Класс для работы с Google Таблицами в контексте кампаний AliExpress.  Наследуется от `SpreadSheet` и предоставляет методы для управления данными кампаний, категорий и продуктов в Google Таблицах.

**Методы**:

- `__init__(self, campaign_name: str, category_name: str, language: str = None, currency: str = None)`:
    **Описание**: Инициализирует объект `GptGs`, принимая ID таблицы Google и необязательные параметры кампании.
    **Параметры**:
        - `campaign_name` (str): Название кампании.
        - `category_name` (str): Название категории.
        - `language` (str, необязательно): Язык кампании.
        - `currency` (str, необязательно): Валюта кампании.
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `Exception`: В случае возникновения ошибки при инициализации.

- `clear(self)`:
    **Описание**: Очищает содержимое таблицы, удаляя листы продуктов и очищая листы категорий и кампании.
    **Параметры**:
        - Нет
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `Exception`: В случае возникновения ошибки при очистке.


- `update_chat_worksheet(self, data: SimpleNamespace | dict | list, conversation_name: str, language: str = None)`:
    **Описание**: Записывает данные кампании в лист Google Таблицы.
    **Параметры**:
        - `data` (SimpleNamespace | dict | list): Данные кампании в формате SimpleNamespace, словаря или списка.
        - `conversation_name` (str): Имя листа для записи данных.
        - `language` (str, необязательно): Язык кампании.
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `Exception`: В случае возникновения ошибки при записи данных.


- `get_campaign_worksheet(self) -> SimpleNamespace`:
    **Описание**: Читает данные кампании из листа 'campaign' Google Таблицы.
    **Параметры**:
        - Нет
    **Возвращает**:
        - SimpleNamespace: Объект SimpleNamespace с данными кампании.
    **Вызывает исключения**:
        - `ValueError`: Если лист 'campaign' не найден.
        - `Exception`: В случае возникновения других ошибок при чтении.


- `set_category_worksheet(self, category: SimpleNamespace | str)`:
    **Описание**: Записывает данные категории в лист 'category' Google Таблицы.
    **Параметры**:
        - `category` (SimpleNamespace): Объект SimpleNamespace с данными категории.
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `TypeError`: Если параметр `category` не является `SimpleNamespace`.
        - `Exception`: В случае других ошибок при записи.


- `get_category_worksheet(self) -> SimpleNamespace`:
    **Описание**: Читает данные категории из листа 'category' Google Таблицы.
    **Параметры**:
        - Нет
    **Возвращает**:
        - SimpleNamespace: Объект SimpleNamespace с данными категории.
    **Вызывает исключения**:
        - `ValueError`: Если лист 'category' не найден.
        - `Exception`: В случае возникновения других ошибок при чтении.


- `set_categories_worksheet(self, categories: SimpleNamespace)`:
    **Описание**: Записывает данные списка категорий в лист 'categories' Google Таблицы.
    **Параметры**:
        - `categories` (SimpleNamespace): Объект SimpleNamespace содержащий список категорий.
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `Exception`: В случае возникновения ошибок при записи.


- `get_categories_worksheet(self) -> List[List[str]]`:
    **Описание**: Читает данные из колонок A-E листа 'categories' Google Таблицы, начиная со второй строки.
    **Параметры**:
        - Нет
    **Возвращает**:
        - List[List[str]]: Данные из таблицы в формате списка списков.
    **Вызывает исключения**:
        - `ValueError`: Если лист 'categories' не найден.
        - `Exception`: В случае возникновения других ошибок при чтении.


- `set_product_worksheet(self, product: SimpleNamespace | str, category_name: str)`:
    **Описание**: Записывает данные продукта в новый лист Google Таблицы, используя шаблон 'product_template'.
    **Параметры**:
        - `product` (SimpleNamespace): Объект SimpleNamespace с данными продукта.
        - `category_name` (str): Имя категории.
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `Exception`: В случае возникновения ошибки при записи.


- `get_product_worksheet(self) -> SimpleNamespace`:
    **Описание**: Читает данные продукта из листа 'products' Google Таблицы.
    **Параметры**:
        - Нет
    **Возвращает**:
        - SimpleNamespace: Объект SimpleNamespace с данными продукта.
    **Вызывает исключения**:
        - `ValueError`: Если лист 'products' не найден.
        - `Exception`: В случае возникновения других ошибок при чтении.


- `set_products_worksheet(self, category_name: str)`:
    **Описание**: Записывает данные продуктов в лист Google Таблицы, связанный с категорией.
    **Параметры**:
        - `category_name` (str): Имя категории.
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `Exception`: В случае возникновения ошибки при записи данных продуктов.


- `delete_products_worksheets(self)`:
    **Описание**: Удаляет все листы из таблицы Google, кроме 'categories' и 'product_template'.
    **Параметры**:
        - Нет
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `Exception`: В случае возникновения ошибок при удалении листов.


- `save_categories_from_worksheet(self, update: bool = False)`:
    **Описание**: Сохраняет отредактированные категории из Google Таблицы.
    **Параметры**:
        - `update` (bool, необязательно): Флаг обновления данных кампании. По умолчанию `False`.
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `Exception`: В случае возникновения ошибки при сохранении.


- `save_campaign_from_worksheet(self)`:
    **Описание**: Сохраняет данные рекламной кампании из Google Таблицы.
    **Параметры**:
        - Нет
    **Возвращает**:
        - None
    **Вызывает исключения**:
        - `Exception`: В случае возникновения ошибок при сохранении.


## Функции

(Нет функций в модуле)

## Дополнительные примечания:

* Модуль использует библиотеку `gspread`.
* Класс `GptGs` наследует методы от класса `SpreadSheet`.
* Используется `SimpleNamespace` для работы с данными.
* Исключения обрабатываются с использованием `try...except` блоков и логирования ошибок.