# Модуль для работы с API AliExpress
## Обзор

Модуль `aliapi.py` предоставляет класс `AliApi`, который является расширением класса `AliexpressApi` и предназначен для взаимодействия с API AliExpress. Он включает в себя методы для получения информации о товарах, категориях и акциях, а также для генерации партнерских ссылок. Модуль использует менеджеры баз данных для работы с категориями и акциями товаров.

## Подробней

Модуль предназначен для упрощения работы с API AliExpress, предоставляя удобные методы для выполнения различных операций, таких как получение информации о товарах, получение партнерских ссылок и управление категориями и акциями товаров. Класс `AliApi` инкапсулирует логику взаимодействия с API AliExpress и предоставляет интерфейс для выполнения основных операций.

## Классы

### `AliApi`

**Описание**:
Класс `AliApi` является кастомным классом API для операций с AliExpress.

**Принцип работы**:
Класс наследует функциональность от класса `AliexpressApi` и добавляет собственные методы для работы с API AliExpress. Он использует менеджеры баз данных `CategoryManager` и `ProductCampaignsManager` для управления категориями и акциями товаров.

**Наследует**:
- `AliexpressApi`: Класс, предоставляющий базовую функциональность для взаимодействия с API AliExpress.

**Аттрибуты**:
- `manager_categories` (CategoryManager): Менеджер для работы с категориями товаров AliExpress.
- `manager_campaigns` (ProductCampaignsManager): Менеджер для работы с акциями товаров AliExpress.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliApi`.
- `retrieve_product_details_as_dict`: Получает детали продуктов в виде словаря.
- `get_affiliate_links`: Получает партнерские ссылки для указанных продуктов.

### `__init__`

```python
def __init__(self, language: str = 'en', currency: str = 'usd', *args, **kwargs):
    """ Инициализирует экземпляр класса AliApi.

    Args:
        language (str): Язык для использования в API запросах. По умолчанию 'en'.
        currency (str): Валюта для использования в API запросах. По умолчанию 'usd'.
    """
```

**Назначение**:
Инициализация экземпляра класса `AliApi` с указанием языка и валюты.

**Параметры**:
- `language` (str): Язык для API-запросов (по умолчанию 'en').
- `currency` (str): Валюта для API-запросов (по умолчанию 'usd').
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Как работает функция**:

1. **Извлечение учетных данных:** Извлекает учетные данные (api_key, secret, tracking_id) для доступа к API AliExpress из глобальных настроек `gs.credentials.aliexpress`.
2. **Инициализация родительского класса:** Вызывает конструктор родительского класса `AliexpressApi` с переданными учетными данными, языком и валютой.
3. **Инициализация менеджеров баз данных (закомментировано):** Инициализирует менеджеры баз данных `CategoryManager` и `ProductCampaignsManager`. Эта часть кода закомментирована, но предполагает создание экземпляров этих менеджеров для дальнейшей работы с категориями и акциями товаров.

**Примеры**:

```python
from src.suppliers.aliexpress.aliapi import AliApi

# Инициализация экземпляра класса AliApi с параметрами по умолчанию
api = AliApi()

# Инициализация экземпляра класса AliApi с указанием языка и валюты
api_ru = AliApi(language='ru', currency='rub')
```

### `retrieve_product_details_as_dict`

```python
def retrieve_product_details_as_dict(self, product_ids: list) -> dict | dict | None:
    """ Отправляет список идентификаторов продуктов в AliExpress и получает список объектов SimpleNamespace с описаниями продуктов.

    Args:
        product_ids (list): Список идентификаторов продуктов.

    Returns:
        dict | None: Список данных о продуктах в виде словарей.

    Example:
        # Преобразование из формата SimpleNamespace в dict
        namespace_list = [
            SimpleNamespace(a=1, b=2, c=3),
            SimpleNamespace(d=4, e=5, f=6),
            SimpleNamespace(g=7, h=8, i=9)
        ]

        # Преобразование каждого объекта SimpleNamespace в словарь
        dict_list = [vars(ns) for ns in namespace_list]

        # Альтернативно, использование метода __dict__:
        dict_list = [ns.__dict__ for ns in namespace_list]

        # Вывод списка словарей
        print(dict_list)
    """
```

**Назначение**:
Получение детальной информации о продуктах AliExpress по их идентификаторам и представление этих данных в виде списка словарей.

**Параметры**:
- `product_ids` (list): Список идентификаторов продуктов, для которых требуется получить информацию.

**Возвращает**:
- `dict | None`: Список словарей, содержащих детальную информацию о продуктах. Возвращает `None`, если произошла ошибка при получении данных.

**Как работает функция**:

1. **Получение данных о продуктах в формате SimpleNamespace:** Вызывает метод `retrieve_product_details` (из родительского класса `AliexpressApi`), чтобы получить детальную информацию о продуктах в формате `SimpleNamespace`.
2. **Преобразование SimpleNamespace в словарь:** Преобразует каждый объект `SimpleNamespace` в словаре в список словарей.
3. **Возврат результата:** Возвращает список словарей, содержащих информацию о продуктах.

**Примеры**:

```python
from src.suppliers.aliexpress.aliapi import AliApi

# Создание экземпляра класса AliApi
api = AliApi()

# Список идентификаторов продуктов
product_ids = ['1234567890', '0987654321']

# Получение информации о продуктах в виде списка словарей
product_details = api.retrieve_product_details_as_dict(product_ids)

# Вывод информации о продуктах
if product_details:
    for product in product_details:
        print(product)
```

### `get_affiliate_links`

```python
def get_affiliate_links(self, links: str | list, link_type: int = 0, **kwargs) -> List[SimpleNamespace]:
    """
    Получает партнерские ссылки для указанных продуктов.

    Args:
        links (str | list): Ссылки на продукты, для которых требуется получить партнерские ссылки.
        link_type (int, optional): Тип партнерской ссылки, которую требуется сгенерировать. По умолчанию 0.

    Returns:
        List[SimpleNamespace]: Список объектов SimpleNamespace, содержащих партнерские ссылки.
    """
```

**Назначение**:
Получение партнерских ссылок для заданных товаров на AliExpress.

**Параметры**:
- `links` (str | list): Ссылка или список ссылок на товары, для которых необходимо получить партнерские ссылки.
- `link_type` (int, optional): Тип партнерской ссылки (по умолчанию 0).
- `**kwargs`: Дополнительные параметры, передаваемые в метод `get_affiliate_links` родительского класса.

**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, каждый из которых содержит информацию о партнерской ссылке.

**Как работает функция**:

1. **Вызов метода родительского класса:** Вызывает метод `get_affiliate_links` родительского класса (`AliexpressApi`) с переданными параметрами.
2. **Возврат результата:** Возвращает результат, полученный от метода родительского класса, который представляет собой список объектов `SimpleNamespace`, содержащих партнерские ссылки.

**Примеры**:

```python
from src.suppliers.aliexpress.aliapi import AliApi

# Создание экземпляра класса AliApi
api = AliApi()

# Ссылка на товар
product_link = 'https://aliexpress.com/item/1234567890.html'

# Получение партнерской ссылки
affiliate_links = api.get_affiliate_links(product_link)

# Вывод партнерской ссылки
if affiliate_links:
    for link in affiliate_links:
        print(link)

# Список ссылок на товары
product_links = ['https://aliexpress.com/item/1234567890.html', 'https://aliexpress.com/item/0987654321.html']

# Получение партнерских ссылок для списка товаров
affiliate_links = api.get_affiliate_links(product_links)

# Вывод партнерских ссылок
if affiliate_links:
    for link in affiliate_links:
        print(link)