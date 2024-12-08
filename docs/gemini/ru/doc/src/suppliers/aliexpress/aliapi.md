# Модуль `hypotez/src/suppliers/aliexpress/aliapi.py`

## Обзор

Этот модуль предоставляет класс `AliApi` для работы с API AliExpress. Он расширяет базовый класс `AliexpressApi` и добавляет дополнительные функции для работы с продуктами, категориями и рекламными кампаниями. Модуль использует библиотеки `requests`, `json`, `asyncio`, `pathlib` и другие для обработки данных и взаимодействия с API.  Он также взаимодействует с базами данных для хранения и управления данными.

## Классы

### `AliApi`

**Описание**: Расширенный класс для работы с API AliExpress.  Предназначен для взаимодействия с API, работы с продуктами, категориями и рекламными кампаниями.

**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр класса `AliApi`.

**Параметры**:
- `language` (str): Язык для запросов API. По умолчанию 'en'.
- `currency` (str): Валюта для запросов API. По умолчанию 'usd'.

**Возвращает**:
- `None`

#### `retrieve_product_details_as_dict`

**Описание**: Отправляет список идентификаторов продуктов в API AliExpress и получает список объектов `SimpleNamespace` с описанием продуктов, преобразует их в список словарей.

**Параметры**:
- `product_ids` (list): Список идентификаторов продуктов.

**Возвращает**:
- `dict | None`: Список данных о продуктах в формате словарей. Возвращает `None`, если произошла ошибка.

**Пример**:
```python
# Пример использования, см.  внутри документации для `retrieve_product_details_as_dict`
```

#### `get_affiliate_links`

**Описание**: Возвращает аффилированные ссылки для указанных продуктов.

**Параметры**:
- `links` (str | list): Ссылка на продукт или список ссылок.
- `link_type` (int, optional): Тип аффилированной ссылки. По умолчанию 0.


**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace` с аффилированными ссылками.


**Примечания**:  Метод использует `super().get_affiliate_links()` для вызова базового метода.  Более подробная документация для базового метода должна быть доступна в `AliexpressApi`.


##  Атрибуты

**Описание**:  Указанные атрибуты используются для взаимодействия с базами данных.

- `manager_categories`: Объект `CategoryManager`.
- `manager_campaigns`: Объект `ProductCampaignsManager`.


##  Модули и импорты

- `re`, `json`, `asyncio`, `pathlib`, `List`, `Dict`, `SimpleNamespace`, `get`, `post` (из `requests`)
- `gs`, `j_loads_ns`, `j_loads`, `j_dumps`, `pprint` (из `src.utils.jjson`, `src.utils.printer`)
- `json2csv` (из `src.utils.convertors.json`)
- `logger` (из `src.logger`)
- `AliexpressApi`, `AliexpressCategory`, `CategoryManager`, `ProductCampaignsManager` (из других модулей)


##  Примечания

- Модуль использует `gs.credentials.aliexpress` для получения API-ключей.
- Документация для `AliexpressApi` и других связанных модулей предполагается доступной.
- Код содержит комментарии, поясняющие использование некоторых функций, и примеры.