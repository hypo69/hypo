# Модуль `ali_campaign_editor.py`

## Обзор

Модуль предоставляет редактор для управления рекламными кампаниями AliExpress. Он позволяет создавать, обновлять и удалять товары и категории в рамках кампании. Модуль поддерживает работу с JSON файлами, хранящими информацию о товарах и категориях, а также обеспечивает взаимодействие с Google Sheets для синхронизации данных.

## Оглавление

1.  [Класс `AliCampaignEditor`](#класс-alicampaigneditor)
    *   [Метод `__init__`](#__init__)
    *   [Метод `delete_product`](#delete_product)
    *   [Метод `update_product`](#update_product)
    *   [Метод `update_campaign`](#update_campaign)
    *   [Метод `update_category`](#update_category)
    *   [Метод `get_category`](#get_category)
    *   [Свойство `list_categories`](#list_categories)
    *   [Метод `get_category_products`](#get_category_products)

## Классы

### `AliCampaignEditor`

**Описание**: Редактор для управления рекламными кампаниями. Позволяет создавать, обновлять и удалять товары и категории в рамках кампании.

#### `__init__`

**Описание**: Инициализирует объект `AliCampaignEditor` с заданными параметрами.

**Параметры**:

*   `campaign_name` (str): Название кампании.
*   `language` (Optional[str | dict], optional): Язык кампании. По умолчанию `None`.
*   `currency` (Optional[str], optional): Валюта кампании. По умолчанию `None`.

**Вызывает исключения**:

*   `CriticalError`: Если не предоставлен ни `campaign_name`, ни `campaign_file`.

#### `delete_product`

**Описание**: Удаляет продукт, у которого нет партнерской ссылки.

**Параметры**:

*   `product_id` (str): Идентификатор продукта для удаления.
*   `exc_info` (bool, optional): Включать ли информацию об исключениях в логи. По умолчанию `False`.

#### `update_product`

**Описание**: Обновляет детали продукта в пределах категории.

**Параметры**:

*   `category_name` (str): Название категории, в которой нужно обновить продукт.
*   `lang` (str): Язык кампании.
*   `product` (dict): Словарь, содержащий детали продукта.

#### `update_campaign`

**Описание**: Обновляет свойства кампании, такие как `description` и `tags`.

#### `update_category`

**Описание**: Обновляет категорию в JSON файле.

**Параметры**:

*   `json_path` (Path): Путь к JSON файлу.
*   `category` (SimpleNamespace): Объект категории для обновления.

**Возвращает**:

*   `bool`: `True`, если обновление успешно, `False` в противном случае.

#### `get_category`

**Описание**: Возвращает объект `SimpleNamespace` для заданного имени категории.

**Параметры**:

*   `category_name` (str): Имя категории для получения.

**Возвращает**:

*   `Optional[SimpleNamespace]`: Объект `SimpleNamespace`, представляющий категорию, или `None`, если категория не найдена.

#### `list_categories`

**Описание**: Возвращает список категорий текущей кампании.

**Возвращает**:

*   `Optional[List[str]]`: Список имен категорий или `None`, если категории не найдены.

#### `get_category_products`

**Описание**: Читает данные о товарах из JSON-файлов для конкретной категории.

**Параметры**:

*   `category_name` (str): Имя категории.

**Возвращает**:

*   `Optional[List[SimpleNamespace]]`: Список объектов `SimpleNamespace`, представляющих товары.