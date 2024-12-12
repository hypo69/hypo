# Модуль `category.py`

## Обзор

Модуль `category.py` предоставляет класс `PrestaCategory`, который обеспечивает взаимодействие с категориями PrestaShop. Он позволяет добавлять, удалять, обновлять категории, а также получать список родительских категорий для заданной категории. Класс предназначен для работы с API PrestaShop и обеспечивает абстракцию от деталей запросов.

## Оглавление

1. [Классы](#классы)
    - [`PrestaCategory`](#prestacategory)
2. [Функции](#функции)
    - [`__init__`](#__init__)
    - [`get_parent_categories_list`](#get_parent_categories_list)

## Классы

### `PrestaCategory`

**Описание**: Класс для работы с категориями в PrestaShop. Предоставляет методы для добавления, удаления, обновления категорий, а также получения списка родительских категорий.

**Пример использования**:

```python
    prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
    prestacategory.add_category_PrestaShop('New Category', 'Parent Category')
    prestacategory.delete_category_PrestaShop(3)
    prestacategory.update_category_PrestaShop(4, 'Updated Category Name')
    print(prestacategory.get_parent_categories_list_PrestaShop(5))
```

**Методы**:

- [`__init__`](#__init__): Инициализирует экземпляр класса `PrestaCategory`.
- [`get_parent_categories_list`](#get_parent_categories_list): Получает список родительских категорий для заданной категории.

## Функции

### `__init__`

**Описание**: Инициализирует экземпляр класса `PrestaCategory`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`:  Произвольные позиционные аргументы, передаваемые в родительский класс.
- `**kwards`: Произвольные именованные аргументы, передаваемые в родительский класс.

**Вызывает исключения**:

- `ValueError`: Если не предоставлены `api_domain` или `api_key`.

### `get_parent_categories_list`

**Описание**: Получает список родительских категорий для заданной категории. Функция рекурсивно обходит родительские категории, пока не достигнет корневой категории (с ID = 2).

**Параметры**:

- `id_category` (str | int): ID категории, для которой нужно получить список родительских категорий.
- `parent_categories_list` (List[int], optional): Список, в который добавляются ID родительских категорий. По умолчанию пустой список `[]`.

**Возвращает**:

- `list`: Список ID родительских категорий. Возвращает пустой список, если `id_category` не указан или произошла ошибка при получении категории.

**Вызывает исключения**:
- `None`: Если что-то не так с категориями, или `category` is None.