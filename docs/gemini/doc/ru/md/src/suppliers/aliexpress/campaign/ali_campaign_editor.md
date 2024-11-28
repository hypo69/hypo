# Модуль `hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor.py`

## Обзор

Данный модуль предоставляет класс `AliCampaignEditor` для редактирования рекламных кампаний на AliExpress. Он наследуется от класса `AliPromoCampaign` и предоставляет методы для управления продуктами и категориями кампании.  Модуль использует Google Sheets для работы с данными кампаний (через класс `AliCampaignGoogleSheet`) и предоставляет функции для обработки файлов JSON, CSV, и текстовых файлов.  Модуль также обеспечивает обработку ошибок и логирование с использованием `logger`.

## Оглавление

- [Модуль `ali_campaign_editor`](#модуль-ali-campaign-editor)
- [Класс `AliCampaignEditor`](#класс-alicampaigneditor)
    - [Метод `__init__`](#метод-init)
    - [Метод `delete_product`](#метод-delete-product)
    - [Метод `update_product`](#метод-update-product)
    - [Метод `update_campaign`](#метод-update-campaign)
    - [Метод `update_category`](#метод-update-category)
    - [Метод `get_category`](#метод-get-category)
    - [Свойство `list_categories`](#свойство-list-categories)
    - [Метод `get_category_products`](#метод-get-category-products)

## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предназначен для редактирования рекламных кампаний AliExpress. Он расширяет функциональность класса `AliPromoCampaign`.

**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр класса `AliCampaignEditor`.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (Optional[str | dict], optional): Язык кампании. По умолчанию "EN".
- `currency` (Optional[str], optional): Валюта кампании. По умолчанию "USD".
- `campaign_file` (Optional[str | Path], optional): Путь к файлу JSON с настройками кампании. По умолчанию `None`.


**Возвращает**:
- Нет.


**Возможные исключения**:
- `CriticalError`: Если не задано ни `campaign_name`, ни `campaign_file`.

#### `delete_product`

**Описание**: Удаляет продукт из кампании, если у него нет партнерской ссылки.

**Параметры**:
- `product_id` (str): Идентификатор продукта.
- `exc_info` (bool, optional):  Включать ли информацию об ошибке в лог. По умолчанию `False`.


**Пример**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.delete_product("12345")
```

#### `update_product`

**Описание**: Обновляет данные продукта в категории.

**Параметры**:
- `category_name` (str): Название категории.
- `lang` (str): Язык кампании.
- `product` (dict): Словарь с данными продукта.


**Пример**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
```

#### `update_campaign`

**Описание**: Обновляет свойства кампании (описание, теги и т.д.).

**Пример**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_campaign()
```

#### `update_category`

**Описание**: Обновляет категорию в файле JSON.

**Параметры**:
- `json_path` (Path): Путь к файлу JSON.
- `category` (SimpleNamespace): Объект SimpleNamespace с обновленными данными категории.


**Возвращает**:
- bool: `True`, если обновление прошло успешно, `False` иначе.

**Пример**:

```python
category = SimpleNamespace(name="New Category", description="Updated description")
editor = AliCampaignEditor(campaign_name="Summer Sale")
result = editor.update_category(Path("category.json"), category)
print(result)
```

#### `get_category`

**Описание**: Возвращает объект `SimpleNamespace` для заданной категории.

**Параметры**:
- `category_name` (str): Имя категории.


**Возвращает**:
- Optional[SimpleNamespace]: Объект `SimpleNamespace`, представляющий категорию, или `None`, если категория не найдена.

**Пример**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
category = editor.get_category("Electronics")
print(category)
```


#### `list_categories`

**Описание**: Возвращает список имен категорий текущей кампании.

**Возвращает**:
- Optional[List[str]]: Список имен категорий, или `None`, если нет категорий.

**Пример**:

```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
categories = editor.list_categories
print(categories)
```


#### `get_category_products`

**Описание**: Возвращает список товаров для заданной категории из JSON файлов.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращает**:
- Optional[List[SimpleNamespace]]: Список объектов SimpleNamespace, представляющих товары, или `None`, если файлы не найдены.

**Пример**:


```python
products = campaign.get_category_products("Electronics")
print(len(products))
```


```