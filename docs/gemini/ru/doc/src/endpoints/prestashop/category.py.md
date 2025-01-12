# Модуль `category.py`

## Обзор

Модуль предоставляет классы `PrestaCategory` и `PrestaCategoryAsync` для управления категориями в PrestaShop.
`PrestaCategory` использует синхронные запросы, а `PrestaCategoryAsync` использует асинхронные запросы.

## Оглавление

1. [Класс `PrestaCategory`](#класс-prestacategory)
   - [Метод `__init__`](#метод-__init__)
   - [Метод `get_parent_categories_list`](#метод-get_parent_categories_list)
2. [Класс `PrestaCategoryAsync`](#класс-prestacategoryasync)
   - [Метод `__init__`](#метод-__init__-1)
   - [Метод `get_parent_categories_list`](#метод-get_parent_categories_list-1)

## Классы

### `PrestaCategory`

**Описание**: Класс для управления категориями в PrestaShop с использованием синхронных запросов.

**Методы**:

#### `__init__`

**Описание**: Инициализирует класс `PrestaCategory`.

**Параметры**:

- `credentials` (Optional[Union[dict, SimpleNamespace]], optional): Словарь или SimpleNamespace с учетными данными (api_domain, api_key). По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:

- `ValueError`: Если `api_domain` или `api_key` не предоставлены.

#### `get_parent_categories_list`

**Описание**: Получает список родительских категорий для заданной категории.

**Параметры**:

- `id_category` (Union[str, int]): Идентификатор категории.
- `parent_categories_list` (List[int], optional): Список родительских категорий. По умолчанию `[]`.

**Возвращает**:

- `List[int]`: Список идентификаторов родительских категорий. Возвращает пустой список, если `id_category` не указан или произошла ошибка при получении категорий.

### `PrestaCategoryAsync`

**Описание**: Класс для управления категориями в PrestaShop с использованием асинхронных запросов.

**Методы**:

#### `__init__`

**Описание**: Инициализирует класс `PrestaCategoryAsync`.

**Параметры**:

- `credentials` (Optional[Union[dict, SimpleNamespace]], optional): Словарь или SimpleNamespace с учетными данными (api_domain, api_key). По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:

- `ValueError`: Если `api_domain` или `api_key` не предоставлены.

#### `get_parent_categories_list`

**Описание**: Асинхронно получает список родительских категорий для заданной категории.

**Параметры**:

- `id_category` (Union[str, int]): Идентификатор категории.
- `parent_categories_list` (List[int], optional): Список родительских категорий. По умолчанию `[]`.

**Возвращает**:

- `List[int]`: Список идентификаторов родительских категорий. Возвращает пустой список, если `id_category` не указан или произошла ошибка при получении категорий.