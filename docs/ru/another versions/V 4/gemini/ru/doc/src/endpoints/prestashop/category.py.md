# Модуль `category`

## Обзор

Модуль `category` предназначен для управления категориями в PrestaShop. Он включает в себя класс `PrestaCategory`, который позволяет получать список родительских категорий для заданной категории. Модуль использует API PrestaShop для взаимодействия с интернет-магазином.

## Подробней

Этот модуль предоставляет функциональность для получения списка родительских категорий, что может быть полезно для навигации по категориям товаров в PrestaShop. Он использует классы `PrestaShop` и `PrestaShopAsync` для взаимодействия с API PrestaShop. Класс `PrestaCategory` наследуется от `PrestaShop` и добавляет специфические методы для работы с категориями.

## Классы

### `PrestaCategory`

**Описание**: Класс для управления категориями в PrestaShop.

**Методы**:
- `__init__`: Инициализирует объект `PrestaCategory`.
- `get_parent_categories_list`: Получает список родительских категорий для заданной категории.

**Параметры**:
- `api_key` (str): Ключ API для доступа к PrestaShop.
- `api_domain` (str): Домен API PrestaShop.

#### `__init__`

**Описание**: Инициализирует объект `PrestaCategory`.

**Параметры**:
- `api_key` (str): Ключ API для доступа к PrestaShop.
- `api_domain` (str): Домен API PrestaShop.
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

#### `get_parent_categories_list`

```python
def get_parent_categories_list(self, id_category: str | int, parent_categories_list: List[int|str] = []) -> List[int]:
    """! Retrieve parent categories from PrestaShop for a given category."""
```

**Описание**: Получает список родительских категорий из PrestaShop для заданной категории.

**Параметры**:
- `id_category` (str | int): ID категории, для которой нужно получить список родительских категорий.
- `parent_categories_list` (List[int | str], optional): Список родительских категорий. По умолчанию `[]`.

**Возвращает**:
- `List[int]`: Список ID родительских категорий.

**Примеры**:
```python
# Пример использования:
api_key = 'your_api_key'
api_domain = 'your_api_domain'
category = PrestaCategory(api_key, api_domain)
parent_categories = category.get_parent_categories_list(3)
print(parent_categories)