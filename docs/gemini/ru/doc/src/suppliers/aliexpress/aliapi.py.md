# Модуль `aliapi.py`

## Обзор

Модуль `aliapi.py` предоставляет класс `AliApi`, который является пользовательским API для работы с AliExpress. Он расширяет функциональность базового класса `AliexpressApi` и включает методы для получения информации о продуктах, создания партнерских ссылок и управления категориями и кампаниями продуктов.

## Подробней

Модуль предназначен для упрощения взаимодействия с API AliExpress, предоставляя удобные методы для выполнения различных операций, таких как получение информации о продуктах и создание партнерских ссылок. Класс `AliApi` включает в себя функциональность для работы с категориями и кампаниями продуктов, а также методы для преобразования данных в различные форматы.

## Классы

### `AliApi`

**Описание**: Пользовательский API класс для операций с AliExpress.

**Наследует**:
- `AliexpressApi`: Расширяет базовый класс `AliexpressApi`.

**Атрибуты**:
- `manager_categories` (CategoryManager): Менеджер категорий для работы с категориями товаров.
- `manager_campaigns` (ProductCampaignsManager): Менеджер кампаний продуктов для работы с кампаниями и скидками.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliApi`.
- `retrieve_product_details_as_dict`: Получает детали продуктов в формате словаря.
- `get_affiliate_links`: Получает партнерские ссылки для указанных продуктов.

### `AliexpressApi`

**Описание**: API для работы с AliExpress.
Более подробную информацию об этом классе можно посмотреть в документации к модулю `api.py`

## Функции

### `__init__`

```python
def __init__(self, language: str = 'en', currency: str = 'usd', *args, **kwargs):
    """ Initializes an instance of the AliApi class.
    
    Args:
        language (str): The language to use for API requests. Defaults to 'en'.
        currency (str): The currency to use for API requests. Defaults to 'usd'.
    """
    credentials = gs.credentials.aliexpress
    api_key = credentials.api_key
    secret = credentials.secret
    tracking_id = credentials.tracking_id
    super().__init__(api_key, secret, language, currency, tracking_id)
    # Initialize database managers if needed
    # self.manager_categories = CategoryManager()
    # self.manager_campaigns = ProductCampaignsManager(gs.presta_credentials[0])
    ...
```

**Назначение**: Инициализирует экземпляр класса `AliApi`, устанавливая параметры языка, валюты и учетные данные для доступа к API AliExpress.

**Параметры**:
- `language` (str): Язык для API запросов. По умолчанию `'en'`.
- `currency` (str): Валюта для API запросов. По умолчанию `'usd'`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Возвращает**:
- `None`

**Как работает функция**:

1. **Извлекает учетные данные**: Функция извлекает ключ API (`api_key`), секрет (`secret`) и идентификатор отслеживания (`tracking_id`) из настроек AliExpress, хранящихся в `gs.credentials.aliexpress`.
2. **Инициализирует родительский класс**: Вызывает конструктор родительского класса `AliexpressApi` с полученными учетными данными, языком и валютой.
3. **Инициализирует менеджеры базы данных**:
   - Потенциально инициализирует менеджер категорий (`self.manager_categories`) и менеджер кампаний (`self.manager_campaigns`). В текущей версии эти строки закомментированы.

**Примеры**:

```python
# Инициализация AliApi с параметрами по умолчанию
api = AliApi()

# Инициализация AliApi с указанием языка и валюты
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
    prod_details_ns = self.retrieve_product_details(product_ids)
    prod_details_dict = [vars(ns) for ns in prod_details_ns]
    return prod_details_dict
```

**Назначение**: Получает детали продуктов, отправляя список идентификаторов продуктов в AliExpress и преобразуя полученные данные в формат словаря.

**Параметры**:
- `product_ids` (list): Список идентификаторов продуктов.

**Возвращает**:
- `dict | None`: Список данных о продуктах в виде словарей.

**Как работает функция**:

1. **Получает детали продуктов**: Вызывает метод `self.retrieve_product_details(product_ids)` для получения списка объектов `SimpleNamespace` с описаниями продуктов.
2. **Преобразует SimpleNamespace в dict**: Преобразует каждый объект `SimpleNamespace` в словарь с использованием `vars(ns)` или `ns.__dict__`.
3. **Возвращает список словарей**: Возвращает список словарей, содержащих данные о продуктах.

```
     A       B
     |       |
Получает->Преобразует SimpleNamespace в dict
данные о  |       |
продуктах |       |
     |       |
     -----C-----
           |
Возвращает список словарей
```

**Примеры**:

```python
# Пример использования retrieve_product_details_as_dict
product_ids = ['1234567890', '0987654321']
product_details = api.retrieve_product_details_as_dict(product_ids)
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
    return super().get_affiliate_links(links, link_type, **kwargs)
```

**Назначение**: Получает партнерские ссылки для указанных продуктов, используя метод из родительского класса.

**Параметры**:
- `links` (str | list): Ссылка или список ссылок на продукты, для которых нужно получить партнерские ссылки.
- `link_type` (int, optional): Тип партнерской ссылки. По умолчанию `0`.
- `**kwargs`: Дополнительные параметры, передаваемые в метод родительского класса.

**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, содержащих партнерские ссылки.

**Как работает функция**:

1. **Вызывает метод родительского класса**: Вызывает метод `super().get_affiliate_links(links, link_type, **kwargs)` для получения партнерских ссылок.
2. **Возвращает результат**: Возвращает список объектов `SimpleNamespace`, содержащих партнерские ссылки.

```
A - B
|   |
Получает->Возвращает
параметры|  партнерские
|   |  ссылки
```

**Примеры**:

```python
# Пример использования get_affiliate_links
links = ['https://aliexpress.com/item/1234567890.html', 'https://aliexpress.com/item/0987654321.html']
affiliate_links = api.get_affiliate_links(links)
if affiliate_links:
    print(affiliate_links)