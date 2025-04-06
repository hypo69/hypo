# Модуль для управления категориями в PrestaShop

## Обзор

Модуль `src.endpoints.prestashop.category` предназначен для управления категориями товаров в интернет-магазине, работающем на платформе PrestaShop. Он содержит класс `PrestaCategory`, который позволяет получать информацию о родительских категориях для заданной категории.

## Подробнее

Модуль предоставляет функциональность для взаимодействия с API PrestaShop для получения данных о категориях. Он использует класс `PrestaCategory`, который наследуется от `PrestaShop`, для выполнения запросов к API и обработки ответов. Основная задача модуля - рекурсивно получать список всех родительских категорий для заданной категории, начиная с указанного идентификатора категории и двигаясь вверх по дереву категорий до корневой категории.

## Классы

### `PrestaCategory`

**Описание**: Класс `PrestaCategory` предназначен для управления категориями в PrestaShop.

**Наследует**:
- `PrestaShop`: `PrestaCategory` наследует функциональность для взаимодействия с API PrestaShop из класса `PrestaShop`.

**Атрибуты**:
- Нет дополнительных атрибутов, кроме унаследованных от `PrestaShop`.

**Методы**:
- `__init__`: Инициализирует объект `PrestaCategory`, вызывая конструктор родительского класса `PrestaShop` с передачей ключа API и доменного имени PrestaShop.
- `get_parent_categories_list`: Получает список родительских категорий для заданной категории.

#### `__init__`

```python
def __init__(self, api_key: str, api_domain: str, *args, **kwargs) -> None:
    """Initializes a Product object.

    Args:
        api_key (str): Ключ API для доступа к PrestaShop.
        api_domain (str): Доменное имя PrestaShop.

    Returns:
        None

    Example:
        >>> category = PrestaCategory(api_key=\'your_api_key\', api_domain=\'your_domain\')
    """
    ...
```

**Назначение**: Инициализирует объект `PrestaCategory`.

**Параметры**:
- `api_key` (str): Ключ API для доступа к PrestaShop.
- `api_domain` (str): Доменное имя PrestaShop.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Возвращает**:
- `None`

**Как работает функция**:
1. Вызывает конструктор родительского класса `PrestaShop` с переданными параметрами `api_key` и `api_domain`, а также любыми дополнительными позиционными и именованными аргументами.

#### `get_parent_categories_list`

```python
def get_parent_categories_list(
    self, id_category: str | int, parent_categories_list: Optional[List[int | str]] = None
) -> List[int | str]:
    """Retrieve parent categories from PrestaShop for a given category.

    Args:
        id_category (str | int): ID категории, для которой нужно получить родительские категории.
        parent_categories_list (Optional[List[int | str]], optional): Список родительских категорий. Defaults to None.

    Returns:
        List[int | str]: Список ID родительских категорий.

    Raises:
        ValueError: Если отсутствует ID категории.
        Exception: Если возникает ошибка при получении данных о категории.

    Example:
        >>> category = PrestaCategory(api_key=\'your_api_key\', api_domain=\'your_domain\')
        >>> parent_categories = category.get_parent_categories_list(id_category=\'10\')
        >>> print(parent_categories)
        [2, 10]
    """
    ...
```

**Назначение**: Получает список родительских категорий для заданной категории.

**Параметры**:
- `id_category` (str | int): ID категории, для которой нужно получить родительские категории.
- `parent_categories_list` (Optional[List[int | str]], optional): Список родительских категорий. По умолчанию `None`.

**Возвращает**:
- `List[int | str]`: Список ID родительских категорий.

**Вызывает исключения**:
- `ValueError`: Если отсутствует ID категории.
- `Exception`: Если возникает ошибка при получении данных о категории.

**Как работает функция**:

     A - Проверка наличия ID категории
     │
     ├── Если ID категории отсутствует --> Возврат `parent_categories_list` или пустой список
     │
     B - Получение данных о категории из API PrestaShop
     │
     ├── Если данные о категории отсутствуют --> Возврат `parent_categories_list` или пустой список
     │
     C - Извлечение ID родительской категории
     │
     D - Добавление ID родительской категории в список
     │
     E - Проверка, является ли родительская категория корневой (ID <= 2)
     │
     ├── Если категория корневая --> Возврат `parent_categories_list`
     │
     └── Если категория не корневая --> Рекурсивный вызов `get_parent_categories_list` для родительской категории
     │
     F - Возврат списка родительских категорий

**Примеры**:
```python
>>> category = PrestaCategory(api_key='your_api_key', api_domain='your_domain')
>>> parent_categories = category.get_parent_categories_list(id_category='10')
>>> print(parent_categories)
[2, 10]
```
```python
>>> category = PrestaCategory(api_key='your_api_key', api_domain='your_domain')
>>> parent_categories = category.get_parent_categories_list(id_category=15, parent_categories_list=[5])
>>> print(parent_categories)
[5, 2, 15]
```