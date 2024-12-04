# Модуль `hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor.py`

## Обзор

Данный модуль предоставляет класс `AliCampaignEditor` для редактирования рекламных кампаний на AliExpress.  Класс наследуется от `AliPromoCampaign` и предоставляет методы для работы с продуктами и категориями кампаний, включая добавление, удаление, обновление и получение информации. Поддерживается работа с Google Sheets и JSON-файлами.

## Классы

### `AliCampaignEditor`

**Описание**: Класс для редактирования рекламных кампаний на AliExpress. Предоставляет методы для работы с продуктами и категориями.

**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр `AliCampaignEditor`.

**Параметры**:
- `campaign_name` (Optional[str]): Название кампании. По умолчанию `None`.
- `language` (Optional[str | dict]): Язык кампании. По умолчанию `'EN'`.
- `currency` (Optional[str]): Валюта кампании. По умолчанию `'USD'`.
- `campaign_file` (Optional[str | Path], optional): Путь к файлу `<lang>_<currency>.json` для загрузки данных кампании. По умолчанию `None`.

**Возвращает**:
-  Не возвращает ничего.

**Вызывает исключения**:
- `CriticalError`: Если не заданы ни `campaign_name`, ни `campaign_file`.


#### `delete_product`

**Описание**: Удаляет продукт, у которого нет аффилиатной ссылки.

**Параметры**:
- `product_id` (str): ID продукта для удаления.
- `exc_info` (bool): Включать ли информацию об исключении в логи. По умолчанию `False`.

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
- `product` (dict): Словарь с деталями продукта.


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

**Описание**: Обновляет категорию в JSON-файле.

**Параметры**:
- `json_path` (Path): Путь к JSON-файлу.
- `category` (SimpleNamespace): Объект категории для обновления.

**Возвращает**:
- bool: `True`, если обновление успешно, `False` иначе.

**Пример**:
```python
category = SimpleNamespace(name="New Category", description="Updated description")
editor = AliCampaignEditor(campaign_name="Summer Sale")
result = editor.update_category(Path("category.json"), category)
print(result)
```


#### `get_category`

**Описание**: Возвращает объект `SimpleNamespace` для заданного имени категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращает**:
- Optional[SimpleNamespace]: Объект `SimpleNamespace` категории или `None`, если не найдена.

**Пример**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
category = editor.get_category("Electronics")
print(category)
```


#### `list_categories`

**Описание**: Возвращает список имён категорий текущей кампании.

**Возвращает**:
- Optional[List[str]]: Список имён категорий или `None` при отсутствии категорий.

**Пример**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
categories = editor.list_categories
print(categories)
```


#### `get_category_products`

**Описание**: Чтение данных о товарах из JSON-файлов для конкретной категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращает**:
- Optional[List[SimpleNamespace]]: Список объектов `SimpleNamespace`, представляющих товары.

**Пример**:
```python
products = campaign.get_category_products("Electronics")
print(len(products))
```


## Функции

(Здесь могут быть описаны функции, если они присутствуют в модуле)


```