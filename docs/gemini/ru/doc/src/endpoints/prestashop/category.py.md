# Модуль `src.endpoints.prestashop.category`

## Обзор

Модуль `src.endpoints.prestashop.category` представляет собой слой между клиентскими категориями (в данном случае, PrestaShop) и поставщиками. Класс `PrestaCategory` предоставляет методы для добавления, удаления и обновления категорий, а также для получения списка родительских категорий.

## Оглавление

- [Классы](#классы)
    - [`PrestaCategory`](#PrestaCategory)
- [Функции](#функции)
    - [`__init__`](#__init__)
    - [`get_parent_categories_list`](#get_parent_categories_list)

## Классы

### `PrestaCategory`

**Описание**: Класс для работы с категориями в PrestaShop.

**Пример использования:**
```python
prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
prestacategory.add_category_PrestaShop('New Category', 'Parent Category')
prestacategory.delete_category_PrestaShop(3)
prestacategory.update_category_PrestaShop(4, 'Updated Category Name')
print(prestacategory.get_parent_categories_list_PrestaShop(5))
```

#### Методы
- [`__init__`](#__init__)
- [`get_parent_categories_list`](#get_parent_categories_list)

## Функции

### `__init__`

**Описание**: Инициализация категории PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если `api_domain` или `api_key` не переданы и не найдены в `credentials`.

### `get_parent_categories_list`

**Описание**: Извлекает из базы данных PrestaShop родительские категории для заданной категории.

**Параметры**:
- `id_category` (str | int): Категория, для которой нужно извлечь родительские категории.
- `parent_categories_list` (List[int], optional): Список родительских категорий. По умолчанию пустой список `[]`.

**Возвращает**:
- `list`: Список родительских категорий.

**Вызывает исключения**:
- `ValueError`: Если `id_category` не передан.