# Модуль `aliapi`

## Обзор

Модуль `aliapi` предоставляет класс `AliApi`, который является пользовательским API для выполнения операций с AliExpress. Он расширяет функциональность базового класса `AliexpressApi` и включает методы для получения информации о продуктах, создания партнерских ссылок и управления категориями и кампаниями продуктов.

## Подробней

Этот модуль предназначен для интеграции с AliExpress API, позволяя получать данные о продуктах, управлять категориями и кампаниями, а также генерировать партнерские ссылки. Класс `AliApi` предоставляет удобные методы для работы с API AliExpress, такие как `retrieve_product_details_as_dict` для получения информации о продуктах в формате словаря и `get_affiliate_links` для создания партнерских ссылок. Модуль использует другие модули проекта, такие как `gs`, `j_loads_ns`, `j_loads`, `j_dumps`, `json2csv`, `logger`, `AliexpressApi`, `AliexpressCategory` и `ProductCampaignsManager`, для выполнения различных задач, таких как загрузка настроек, преобразование данных, логирование и взаимодействие с базой данных.

## Классы

### `AliApi`

**Описание**: Пользовательский класс API для операций с AliExpress.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliApi`.
- `retrieve_product_details_as_dict`: Получает детали продукта в виде словаря.
- `get_affiliate_links`: Получает партнерские ссылки для указанных продуктов.

**Параметры**:
- `language` (str): Язык для API запросов. По умолчанию 'en'.
- `currency` (str): Валюта для API запросов. По умолчанию 'usd'.

**Примеры**
```python
# Пример инициализации класса AliApi
ali_api = AliApi(language='ru', currency='rub')

# Пример получения деталей продукта в виде словаря
product_ids = ['1234567890', '0987654321']
product_details = ali_api.retrieve_product_details_as_dict(product_ids)
if product_details:
    print(product_details)

# Пример получения партнерских ссылок
links = ['https://aliexpress.com/item/1234567890.html', 'https://aliexpress.com/item/0987654321.html']
affiliate_links = ali_api.get_affiliate_links(links)
if affiliate_links:
    print(affiliate_links)
```

## Функции

### `__init__`

```python
def __init__(self, language: str = 'en', currency: str = 'usd', *args, **kwargs):
    """ Initializes an instance of the AliApi class.
    
    Args:
        language (str): The language to use for API requests. Defaults to 'en'.
        currency (str): The currency to use for API requests. Defaults to 'usd'.
    """
```

**Описание**: Инициализирует экземпляр класса `AliApi`.

**Параметры**:
- `language` (str): Язык для API запросов. По умолчанию 'en'.
- `currency` (str): Валюта для API запросов. По умолчанию 'usd'.

**Примеры**:
```python
# Пример инициализации класса AliApi
ali_api = AliApi(language='ru', currency='rub')
```

### `retrieve_product_details_as_dict`

```python
def retrieve_product_details_as_dict(self, product_ids: list) -> dict | dict | None:
    """ Sends a list of product IDs to AliExpress and receives a list of SimpleNamespace objects with product descriptions.
    
    Args:
        product_ids (list): List of product IDs.
    
    Returns:
        dict | None: List of product data as dictionaries.
    
    Example:
        # Convert from SimpleNamespace format to dict
        namespace_list = [
            SimpleNamespace(a=1, b=2, c=3),
            SimpleNamespace(d=4, e=5, f=6),
            SimpleNamespace(g=7, h=8, i=9)
        ]
        
        # Convert each SimpleNamespace object to a dictionary
        dict_list = [vars(ns) for ns in namespace_list]
        
        # Alternatively, use the __dict__ method:
        dict_list = [ns.__dict__ for ns in namespace_list]
        
        # Print the list of dictionaries
        print(dict_list)
    """
```

**Описание**: Отправляет список ID продуктов в AliExpress и получает список объектов `SimpleNamespace` с описаниями продуктов.

**Параметры**:
- `product_ids` (list): Список ID продуктов.

**Возвращает**:
- `dict | None`: Список данных о продуктах в виде словарей.

**Примеры**:
```python
# Пример получения деталей продукта в виде словаря
product_ids = ['1234567890', '0987654321']
ali_api = AliApi()
product_details = ali_api.retrieve_product_details_as_dict(product_ids)
if product_details:
    print(product_details)
```

### `get_affiliate_links`

```python
def get_affiliate_links(self, links: str | list, link_type: int = 0, **kwargs) -> List[SimpleNamespace]:
    """ 
    Retrieves affiliate links for the specified products.
    
    Args:
        links (str | list): The product links to be processed.
        link_type (int, optional): The type of affiliate link to be generated. Defaults to 0.
    
    Returns:
        List[SimpleNamespace]: A list of SimpleNamespace objects containing affiliate links.
    """
```

**Описание**: Получает партнерские ссылки для указанных продуктов.

**Параметры**:
- `links` (str | list): Ссылки на продукты для обработки.
- `link_type` (int, optional): Тип партнерской ссылки для генерации. По умолчанию 0.

**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, содержащих партнерские ссылки.

**Примеры**:
```python
# Пример получения партнерских ссылок
links = ['https://aliexpress.com/item/1234567890.html', 'https://aliexpress.com/item/0987654321.html']
ali_api = AliApi()
affiliate_links = ali_api.get_affiliate_links(links)
if affiliate_links:
    print(affiliate_links)