# Модуль `aliapi.py`

## Обзор

Модуль `aliapi.py` предоставляет класс `AliApi`, который является пользовательским API для работы с AliExpress. Он расширяет функциональность базового класса `AliexpressApi` и предоставляет методы для получения информации о продуктах, создания партнерских ссылок и управления категориями и кампаниями продуктов.

## Подробней

Модуль предназначен для интеграции с AliExpress и позволяет автоматизировать получение данных о товарах, категориях и акциях. Класс `AliApi` использует API ключи, секреты и идентификаторы отслеживания для аутентификации и взаимодействия с AliExpress. Он также содержит методы для преобразования данных из формата `SimpleNamespace` в `dict`. Модуль активно использует логирование для отслеживания ошибок и действий.

## Классы

### `AliApi`

**Описание**: Пользовательский класс API для операций с AliExpress.

**Наследует**: `AliexpressApi`

**Аттрибуты**:
- `manager_categories` (CategoryManager): Менеджер категорий AliExpress.
- `manager_campaigns` (ProductCampaignsManager): Менеджер кампаний продуктов.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliApi`.
- `retrieve_product_details_as_dict`: Получает детали продукта в виде словаря.
- `get_affiliate_links`: Получает партнерские ссылки для указанных продуктов.

### `__init__`

```python
def __init__(self, language: str = 'en', currency: str = 'usd', *args, **kwargs):
    """ Initializes an instance of the AliApi class.
    
    Args:
        language (str): The language to use for API requests. Defaults to 'en'.
        currency (str): The currency to use for API requests. Defaults to 'usd'.
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `AliApi`.

**Параметры**:
- `language` (str): Язык для API запросов. По умолчанию 'en'.
- `currency` (str): Валюта для API запросов. По умолчанию 'usd'.
- `*args`: Произвольные позиционные аргументы, передаваемые в родительский класс.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в родительский класс.

**Как работает функция**:
1. Извлекает учетные данные AliExpress (api_key, secret, tracking_id) из глобальных настроек (`gs.credentials.aliexpress`).
2. Инициализирует родительский класс `AliexpressApi` с полученными учетными данными, языком и валютой.
3. Закомментировано: Инициализирует менеджеры базы данных категорий и кампаний продуктов.

**Примеры**:
```python
# Создание экземпляра класса AliApi с параметрами по умолчанию
api = AliApi()

# Создание экземпляра класса AliApi с указанием языка и валюты
api = AliApi(language='ru', currency='rub')
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

**Назначение**: Получает детали продукта в виде словаря.

**Параметры**:
- `product_ids` (list): Список идентификаторов продуктов.

**Возвращает**:
- `dict | None`: Список данных о продуктах в виде словарей.

**Как работает функция**:
1. Вызывает метод `retrieve_product_details` родительского класса `AliexpressApi` для получения деталей продукта в формате `SimpleNamespace`.
2. Преобразует каждый объект `SimpleNamespace` в словаре с использованием `vars(ns)` или `ns.__dict__`.
3. Возвращает список словарей с деталями продуктов.

```
      A
      |
  Получение деталей в формате SimpleNamespace
      |
      B
      |
  Преобразование SimpleNamespace в dict
      |
      C
```

**Примеры**:
```python
# Пример использования функции
product_ids = ['1234567890', '0987654321']
product_details = api.retrieve_product_details_as_dict(product_ids)
if product_details:
    for product in product_details:
        print(product['title'])
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

**Назначение**: Получает партнерские ссылки для указанных продуктов.

**Параметры**:
- `links` (str | list): Ссылка или список ссылок на продукты.
- `link_type` (int, optional): Тип партнерской ссылки. По умолчанию 0.
- `**kwargs`: Дополнительные параметры, передаваемые в родительский класс.

**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, содержащих партнерские ссылки.

**Как работает функция**:
1. Вызывает метод `get_affiliate_links` родительского класса `AliexpressApi` с переданными параметрами.
2. Возвращает список объектов `SimpleNamespace`, содержащих партнерские ссылки.

```
      A
      |
  Получение партнерских ссылок от AliexpressApi
      |
      B
```

**Примеры**:
```python
# Пример использования функции
links = ['https://aliexpress.com/item/1234567890.html', 'https://aliexpress.com/item/0987654321.html']
affiliate_links = api.get_affiliate_links(links)
for link in affiliate_links:
    print(link.affiliate_link)