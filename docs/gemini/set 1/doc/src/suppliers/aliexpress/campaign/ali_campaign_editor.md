# Модуль `hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor.py`

## Обзор

Этот модуль предоставляет редактор для рекламных кампаний на AliExpress. Он позволяет добавлять, удалять и обновлять товары в кампаниях, а также работать с категориями. Модуль использует данные в формате JSON и взаимодействует с Google Sheets (через `AliCampaignGoogleSheet`).

## Оглавление

* [Классы](#классы)
* [Функции](#функции)


## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предоставляет методы для управления рекламными кампаниями на AliExpress. Наследуется от класса `AliPromoCampaign`.

**Методы**:

* `__init__`: Инициализирует объект `AliCampaignEditor`.
* `delete_product`: Удаляет продукт из кампании, если он не содержит аффилиатную ссылку.
* `update_product`: Обновляет данные продукта в категории.
* `update_campaign`: Обновляет свойства кампании (описание, тэги и т.д.).
* `update_category`: Обновляет данные категории в JSON файле.
* `get_category`: Возвращает объект `SimpleNamespace` для заданной категории.
* `list_categories`: Возвращает список всех категорий в кампании.
* `get_category_products`: Возвращает список продуктов для заданной категории из JSON файлов.


**Параметры конструктора (`__init__`)**:

- `campaign_name` (str): Название кампании.
- `language` (Optional[str | dict], optional): Язык кампании. По умолчанию "EN".
- `currency` (Optional[str], optional): Валюта кампании. По умолчанию "USD".
- `campaign_file` (Optional[str | Path], optional): Путь к файлу кампании. По умолчанию `None`.

**Возвращаемые значения**:


**Исключения**:

- `CriticalError`: Если не указаны ни `campaign_name`, ни `campaign_file`.


## Функции

(Нет функций в данном модуле)


## Подробные описания методов

### `AliCampaignEditor.__init__`

**Описание**: Инициализирует объект `AliCampaignEditor` с параметрами кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (Optional[str | dict], optional): Язык кампании (по умолчанию "EN").
- `currency` (Optional[str], optional): Валюта кампании (по умолчанию "USD").
- `campaign_file` (Optional[str | Path], optional): Путь к файлу кампании в формате JSON.

**Возвращаемые значения**:
- Не возвращает значение.

**Исключения**:
- `CriticalError`: Если не указаны ни `campaign_name`, ни `campaign_file`.

### `AliCampaignEditor.delete_product`

**Описание**: Удаляет продукт из списка продуктов, если он не содержит аффилиатную ссылку.

**Параметры**:
- `product_id` (str): ID продукта.
- `exc_info` (bool, optional): Включать ли информацию об исключении в лог. По умолчанию `False`.

**Возвращаемые значения**:
- Не возвращает значение.

**Исключения**:
- `FileNotFoundError`: Если файл продукта не найден.
- `Exception`: Общее исключение при операциях с файлами.


### `AliCampaignEditor.update_product`

**Описание**: Обновляет данные продукта в категории.

**Параметры**:
- `category_name` (str): Название категории.
- `lang` (str): Язык кампании.
- `product` (dict): Словарь с данными продукта.

**Возвращаемые значения**:
- Не возвращает значение.

**Исключения**:
- Нет описанных исключений.

### `AliCampaignEditor.update_category`

**Описание**: Обновляет данные категории в JSON файле.

**Параметры**:
- `json_path` (Path): Путь к JSON файлу.
- `category` (SimpleNamespace): Объект категории для обновления.

**Возвращаемые значения**:
- bool: `True`, если обновление успешно, `False` в противном случае.

**Исключения**:
- `Exception`: Общее исключение при работе с JSON.


###  `AliCampaignEditor.get_category`

**Описание**: Возвращает объект `SimpleNamespace` для заданной категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращаемые значения**:
- Optional[SimpleNamespace]: Объект `SimpleNamespace` или `None`, если категория не найдена.

**Исключения**:
- `Exception`: Общее исключение.


### `AliCampaignEditor.list_categories`

**Описание**: Возвращает список всех категорий в кампании.

**Параметры**:
- Нет параметров.

**Возвращаемые значения**:
- Optional[List[str]]: Список имен категорий или `None`, если категории не найдены.

**Исключения**:
- `Exception`: Общее исключение.

### `AliCampaignEditor.get_category_products`

**Описание**: Чтение данных о товарах из JSON файлов для конкретной категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращаемые значения**:
- Optional[List[SimpleNamespace]]: Список объектов `SimpleNamespace`, представляющих товары.

**Исключения**:
- `Exception`: Общее исключение.