# Модуль `src.endpoints.prestashop.category`

## Обзор

Модуль `src.endpoints.prestashop.category` предназначен для управления категориями в PrestaShop. Он содержит класс `PrestaCategory`, который упрощает получение информации о родительских категориях.

## Подробнее

Модуль предоставляет функциональность для взаимодействия с API PrestaShop для получения иерархии категорий. Класс `PrestaCategory` наследуется от `PrestaShop` и использует его методы для выполнения запросов к API. Этот модуль позволяет разработчикам легко интегрировать функции управления категориями в свои приложения PrestaShop.

## Классы

### `PrestaCategory`

**Описание**: Класс `PrestaCategory` предназначен для управления категориями в PrestaShop. Он позволяет получать список родительских категорий для заданной категории.

**Наследует**:
- `PrestaShop`: Класс `PrestaCategory` наследует функциональность для работы с API PrestaShop.

**Атрибуты**:
- `api_key` (str): Ключ API для доступа к PrestaShop.
- `api_domain` (str): Доменное имя PrestaShop.

**Методы**:
- `get_parent_categories_list()`: Получает список родительских категорий для заданной категории.

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
1. Вызывает конструктор родительского класса `PrestaShop` с переданными аргументами.

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

**Назначение**: Получает список родительских категорий для заданной категории из PrestaShop.

**Параметры**:
- `id_category` (str | int): ID категории, для которой нужно получить родительские категории.
- `parent_categories_list` (Optional[List[int | str]], optional): Список родительских категорий. По умолчанию `None`.

**Возвращает**:
- `List[int | str]`: Список ID родительских категорий.

**Вызывает исключения**:
- `ValueError`: Если отсутствует ID категории.
- `Exception`: Если возникает ошибка при получении данных о категории.

**Как работает функция**:

1. **Проверка наличия ID категории**:
   - Если `id_category` отсутствует, функция логирует ошибку и возвращает текущий (или пустой) список родительских категорий.
2. **Получение информации о категории**:
   - Использует метод `get` родительского класса `PrestaShop` для получения информации о категории по её ID.
   - Если информация о категории не найдена, функция логирует ошибку и возвращает текущий (или пустой) список родительских категорий.
3. **Извлечение ID родительской категории**:
   - Извлекает `id_parent` из полученной информации о категории.
4. **Добавление родительской категории в список**:
   - Добавляет ID родительской категории в список `parent_categories_list`.
5. **Рекурсивный вызов**:
   - Если ID родительской категории больше 2, функция рекурсивно вызывает себя с ID родительской категории для получения списка её родительских категорий.
   - Если ID родительской категории меньше или равен 2, функция возвращает полученный список родительских категорий.

**ASCII flowchart**:

```
A [Проверка наличия ID категории]
│
├── Нет ID -> B [Логирование ошибки и возврат списка]
│
└── ID есть -> C [Получение информации о категории]
    │
    ├── Нет информации -> D [Логирование ошибки и возврат списка]
    │
    └── Информация есть -> E [Извлечение ID родительской категории]
        │
        F [Добавление родительской категории в список]
        │
        G [Проверка ID родительской категории (<= 2?)]
        │
        ├── Да -> H [Возврат списка]
        │
        └── Нет -> I [Рекурсивный вызов функции с ID родительской категории]
```

**Примеры**:

```python
category = PrestaCategory(api_key='your_api_key', api_domain='your_domain')
parent_categories = category.get_parent_categories_list(id_category='10')
print(parent_categories)
# [2, 10]

parent_categories = category.get_parent_categories_list(id_category=15, parent_categories_list=[1, 2])
print(parent_categories)
# [1, 2, 2, 15]