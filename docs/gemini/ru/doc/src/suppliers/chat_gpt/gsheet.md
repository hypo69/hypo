# Модуль `hypotez/src/suppliers/chat_gpt/gsheet.py`

## Обзор

Модуль `gsheet.py` предоставляет класс `GptGs`, наследующий от `SpreadSheet`, для управления Google Таблицами в контексте кампаний AliExpress.  Класс позволяет читать, записывать и обновлять данные о категориях, кампаниях и продуктах в Google Таблицах.  Реализованы методы для очистки, обновления, чтения и записи данных в различные листы таблицы.

## Классы

### `GptGs`

**Описание**: Класс `GptGs` предназначен для работы с Google Таблицами, предоставляя методы для управления данными кампаний AliExpress. Наследуется от `SpreadSheet`,  позволяя взаимодействовать с таблицей и её листами.

**Методы**:

- `__init__(self, campaign_name: str = None, category_name: str = None, language: str = None, currency: str = None)`: Инициализирует объект `GptGs` с указанием идентификатора Google Таблицы и опциональными параметрами кампании.
- `clear(self)`: Очищает содержимое таблицы, удаляя листы продуктов и очищая данные на листах категорий и кампании.
- `update_chat_worksheet(self, data: SimpleNamespace|dict|list, conversation_name:str, language: str = None)`: Записывает данные кампании в Google Таблицу на указанный лист.
- `get_campaign_worksheet(self) -> SimpleNamespace`: Читает данные о кампании из листа 'campaign'.
- `set_category_worksheet(self, category: SimpleNamespace | str)`: Записывает данные категории в таблицу вертикально в лист 'category'.
- `get_category_worksheet(self) -> SimpleNamespace`: Читает данные о категории из листа 'category'.
- `set_categories_worksheet(self, categories: SimpleNamespace)`: Записывает данные о списка категорий в лист 'categories'.
- `get_categories_worksheet(self) -> List[List[str]]`: Читает данные из колонок A-E листа 'categories', начиная со второй строки.
- `set_product_worksheet(self, product: SimpleNamespace | str, category_name: str)`: Записывает данные продукта в новый лист Google Таблицы, скопированный из 'product_template'.
- `get_product_worksheet(self) -> SimpleNamespace`: Читает данные продукта из листа 'products'.
- `set_products_worksheet(self, category_name: str)`: Записывает данные о продуктах на лист, соответствующий переданной категории.
- `delete_products_worksheets(self)`: Удаляет все листы Google Таблицы, кроме 'categories' и 'product_template'.
- `save_categories_from_worksheet(self, update: bool = False)`: Сохраняет данные, отредактированные в Google Таблице, в атрибуте `campaign.category`.
- `save_campaign_from_worksheet(self)`: Сохраняет данные о кампании из Google Таблицы в атрибуте `self.campaign`.


**Параметры**:

- `campaign_name` (str, optional): Имя кампании. По умолчанию `None`.
- `category_name` (str, optional): Имя категории. По умолчанию `None`.
- `language` (str, optional): Язык кампании. По умолчанию `None`.
- `currency` (str, optional): Валюта кампании. По умолчанию `None`.
- `data` (SimpleNamespace|dict|list): Данные кампании для записи.
- `conversation_name` (str): Имя листа.
- `language` (str, optional): Язык. По умолчанию `None`.
- `category` (SimpleNamespace | str): Объект `SimpleNamespace` с данными категории.
- `categories` (SimpleNamespace): Объект `SimpleNamespace` с данными списком категорий.
- `product` (SimpleNamespace | str): Объект `SimpleNamespace` с данными продукта.
- `category_name` (str): Название категории.
- `ns_list` (List[SimpleNamespace]|SimpleNamespace): Список объектов `SimpleNamespace` с данными.


**Возвращает**:

- `None` (для большинства методов).
- `SimpleNamespace`: Объект с данными о кампании/категории/продукте.
- `List[List[str]]`: Список строк с данными из листа 'categories'.


**Вызывает исключения**:

- `ValueError`: Если лист не найден или при других ошибках валидации.
- `TypeError`: Если неверный тип данных передан в метод.
- `Exception`: В случае возникновения ошибок при работе с Google Таблицами.


## Функции

(Нет функций в данном модуле)


## Константные значения


```