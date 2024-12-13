# Модуль `ali_campaign_editor.py`

## Обзор

Модуль `ali_campaign_editor.py` предоставляет функциональность для редактирования рекламных кампаний AliExpress. Он включает в себя классы и методы для управления продуктами, категориями и общими параметрами кампании.

## Оглавление

1. [Класс `AliCampaignEditor`](#класс-alicampaigneditor)
    - [Метод `__init__`](#метод-__init__)
    - [Метод `delete_product`](#метод-delete_product)
    - [Метод `update_product`](#метод-update_product)
    - [Метод `update_campaign`](#метод-update_campaign)
    - [Метод `update_category`](#метод-update_category)
    - [Метод `get_category`](#метод-get_category)
    - [Свойство `list_categories`](#свойство-list_categories)
    - [Метод `get_category_products`](#метод-get_category_products)
2. [Импорты](#импорты)
3. [Переменные модуля](#переменные-модуля)

## Класс `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предназначен для редактирования рекламных кампаний AliExpress.

### Метод `__init__`

**Описание**: Инициализирует экземпляр класса `AliCampaignEditor`.

**Параметры**:

-   `campaign_name` (str): Название кампании.
-   `language` (Optional[str | dict], optional): Язык кампании. По умолчанию `None`.
-   `currency` (Optional[str], optional): Валюта кампании. По умолчанию `None`.
  
**Примеры**:

```python
# 1. by campaign parameters
>>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
# 2. load fom file
>>> editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
```

**Вызывает исключения**:

-   `CriticalError`: Если не предоставлены ни `campaign_name`, ни `campaign_file`.

### Метод `delete_product`

**Описание**: Удаляет продукт, не имеющий партнерской ссылки.

**Параметры**:

-   `product_id` (str): ID продукта для удаления.
-   `exc_info` (bool): Включать ли информацию об исключении в логи. По умолчанию `False`.

**Пример**:

```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> editor.delete_product("12345")
```

### Метод `update_product`

**Описание**: Обновляет детали продукта в категории.

**Параметры**:

-   `category_name` (str): Название категории, где необходимо обновить продукт.
-   `lang` (str): Язык кампании.
-   `product` (dict): Словарь с данными продукта.

**Пример**:

```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
```

### Метод `update_campaign`

**Описание**: Обновляет свойства кампании, такие как `description`, `tags` и т.д.

**Пример**:

```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> editor.update_campaign()
```

### Метод `update_category`

**Описание**: Обновляет категорию в JSON-файле.

**Параметры**:

-   `json_path` (Path): Путь к JSON-файлу.
-   `category` (SimpleNamespace): Объект категории для обновления.

**Возвращает**:

-   `bool`: `True`, если обновление прошло успешно, `False` в противном случае.

**Пример**:

```python
>>> category = SimpleNamespace(name="New Category", description="Updated description")
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> result = editor.update_category(Path("category.json"), category)
>>> print(result)  # True if successful
```

### Метод `get_category`

**Описание**: Возвращает объект `SimpleNamespace` для заданной категории.

**Параметры**:

-   `category_name` (str): Название категории для получения.

**Возвращает**:

-   `Optional[SimpleNamespace]`: Объект `SimpleNamespace`, представляющий категорию, или `None`, если категория не найдена.

**Пример**:

```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> category = editor.get_category("Electronics")
>>> print(category)  # SimpleNamespace or None
```

### Свойство `list_categories`

**Описание**: Возвращает список категорий в текущей кампании.

**Возвращает**:

-   `Optional[List[str]]`: Список названий категорий или `None`, если категории не найдены.

**Пример**:

```python
>>> editor = AliCampaignEditor(campaign_name="Summer Sale")
>>> categories = editor.categories_list
>>> print(categories)  # ['Electronics', 'Fashion', 'Home']
```

### Метод `get_category_products`

**Описание**: Читает данные о товарах из JSON-файлов для конкретной категории.

**Параметры**:

-   `category_name` (str): Имя категории.

**Возвращает**:

-   `Optional[List[SimpleNamespace]]`: Список объектов `SimpleNamespace`, представляющих товары.

**Пример**:

```python
>>> products = campaign.get_category_products("Electronics")
>>> print(len(products))
15
```

## Импорты

Модуль импортирует следующие библиотеки:

-   `re`: Для работы с регулярными выражениями.
-   `shutil`: Для высокоуровневых операций с файлами.
-   `pathlib.Path`: Для работы с путями к файлам.
-   `types.SimpleNamespace`: Для создания простых объектов с атрибутами.
-   `typing.List`, `typing.Optional`: Для аннотации типов.
-   `header`: Неизвестный локальный модуль.
-   `src.gs`: Неизвестный локальный модуль.
-  `src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign`
-   `src.suppliers.aliexpress.campaign.gsheet.AliCampaignGoogleSheet`
-   `src.suppliers.aliexpress.utils`: Вспомогательные функции для работы с AliExpress.
-   `src.utils.jjson`: Функции для работы с JSON.
-   `src.utils.convertors.csv`: Функции для работы с CSV.
-   `src.utils.printer`: Функция для форматированного вывода.
-   `src.utils.file`: Функции для работы с файлами.
-   `src.logger.logger`: Модуль логирования.

## Переменные модуля

- `MODE`: Режим работы модуля. По умолчанию 'dev'.