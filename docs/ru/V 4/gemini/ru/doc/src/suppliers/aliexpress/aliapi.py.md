# Модуль `aliapi.py`

## Обзор

Модуль `aliapi.py` предоставляет класс `AliApi`, который является расширением класса `AliexpressApi` и предназначен для взаимодействия с API AliExpress. Этот модуль включает функциональность для получения информации о продуктах, создания партнерских ссылок, а также управления категориями и кампаниями продуктов через базу данных.

## Подробней

Модуль `aliapi.py` является частью проекта `hypotez` и служит для упрощения работы с API AliExpress. Он предоставляет удобные методы для получения информации о продуктах, создания партнерских ссылок и управления данными, связанными с категориями и кампаниями продуктов. `AliApi` наследуется от `AliexpressApi` и добавляет дополнительную функциональность, специфичную для нужд проекта `hypotez`.

## Классы

### `AliApi`

**Описание**:
Класс `AliApi` предназначен для работы с API AliExpress, включая получение информации о продуктах и создание партнерских ссылок.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliApi`.
- `retrieve_product_details_as_dict`: Получает детали продуктов в виде словаря.
- `get_affiliate_links`: Получает партнерские ссылки для указанных продуктов.

#### `__init__`

```python
def __init__(self, language: str = 'en', currency: str = 'usd', *args, **kwargs):
    """ Initializes an instance of the AliApi class.
    
    Args:
        language (str): The language to use for API requests. Defaults to 'en'.
        currency (str): The currency to use for API requests. Defaults to 'usd'.
    """
    ...
```

**Описание**:
Инициализирует экземпляр класса `AliApi`, устанавливая язык и валюту для API запросов, а также инициализирует менеджеры категорий и кампаний продуктов.

**Параметры**:
- `language` (str): Язык для API запросов. По умолчанию `'en'`.
- `currency` (str): Валюта для API запросов. По умолчанию `'usd'`.
- `*args`: Дополнительные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwargs`: Дополнительные именованные аргументы, передаваемые в конструктор родительского класса.

**Примеры**:

```python
api = AliApi(language='ru', currency='rub')
```

#### `retrieve_product_details_as_dict`

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
    ...
```

**Описание**:
Отправляет список идентификаторов продуктов в AliExpress и получает список объектов `SimpleNamespace` с описаниями продуктов, преобразованными в словари.

**Параметры**:
- `product_ids` (list): Список идентификаторов продуктов.

**Возвращает**:
- `dict | None`: Список данных о продуктах в виде словарей.

**Примеры**:

```python
product_ids = ['1234567890', '0987654321']
product_details = api.retrieve_product_details_as_dict(product_ids)
if product_details:
    print(product_details)
```

#### `get_affiliate_links`

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
    ...
```

**Описание**:
Получает партнерские ссылки для указанных продуктов.

**Параметры**:
- `links` (str | list): Ссылка или список ссылок на продукты.
- `link_type` (int, optional): Тип партнерской ссылки. По умолчанию `0`.
- `**kwargs`: Дополнительные параметры, передаваемые в метод `get_affiliate_links` родительского класса.

**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, содержащих партнерские ссылки.

**Примеры**:

```python
links = ['https://aliexpress.com/item/1234567890.html', 'https://aliexpress.com/item/0987654321.html']
affiliate_links = api.get_affiliate_links(links)
if affiliate_links:
    print(affiliate_links)
```