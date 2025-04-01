# Модуль `src.endpoints.prestashop.category`

## Обзор

Модуль предназначен для управления категориями в PrestaShop. Он содержит класс `PrestaCategory`, который позволяет получать информацию о родительских категориях.

## Подробнее

Этот модуль предоставляет функциональность для взаимодействия с API PrestaShop для управления категориями товаров. Класс `PrestaCategory` расширяет класс `PrestaShop` и реализует методы для получения списка родительских категорий для заданной категории. Этот модуль полезен для навигации по иерархии категорий в PrestaShop и получения информации об их структуре.

## Классы

### `PrestaCategory`

**Описание**: Класс для управления категориями в PrestaShop.

**Наследует**:
- `PrestaShop`: Класс `PrestaCategory` наследует функциональность для взаимодействия с API PrestaShop.

**Атрибуты**:
- `api_key` (str): Ключ API для доступа к PrestaShop.
- `api_domain` (str): Доменное имя PrestaShop.

**Методы**:
- `get_parent_categories_list()`: Получает список родительских категорий для заданной категории.

### `__init__`

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

**Возвращает**:
- `None`

**Как работает функция**:
1. Вызывает конструктор родительского класса `PrestaShop` для инициализации общих параметров API.

**Примеры**:
```python
category = PrestaCategory(api_key='your_api_key', api_domain='your_domain')
```

### `get_parent_categories_list`

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

**Назначение**: Получает список родительских категорий из PrestaShop для заданной категории.

**Параметры**:
- `id_category` (str | int): ID категории, для которой нужно получить родительские категории.
- `parent_categories_list` (Optional[List[int | str]], optional): Список родительских категорий. По умолчанию `None`.

**Возвращает**:
- `List[int | str]`: Список ID родительских категорий.

**Вызывает исключения**:
- `ValueError`: Если отсутствует ID категории.
- `Exception`: Если возникает ошибка при получении данных о категории.

**Как работает функция**:
1. Проверяет, передан ли `id_category`. Если нет, то логирует ошибку и возвращает пустой список или переданный `parent_categories_list`.
2. Получает информацию о категории из PrestaShop, используя метод `super().get()`.
3. Если информация о категории не получена, логирует ошибку и возвращает пустой список или переданный `parent_categories_list`.
4. Извлекает `id_parent` из полученной информации о категории.
5. Добавляет `id_parent` в список `parent_categories_list`.
6. Если `id_parent` меньше или равен 2, возвращает `parent_categories_list`.
7. В противном случае рекурсивно вызывает `get_parent_categories_list()` с `id_parent` в качестве `id_category`.

```
A: Проверка наличия id_category
|
B: Получение информации о категории из PrestaShop
|
C: Извлечение id_parent из информации о категории
|
D: Добавление id_parent в parent_categories_list
|
E: Проверка id_parent <= 2
|
F: Возврат parent_categories_list
```

**Примеры**:
```python
category = PrestaCategory(api_key='your_api_key', api_domain='your_domain')
parent_categories = category.get_parent_categories_list(id_category='10')
print(parent_categories)
# [2, 10]
```
```python
category = PrestaCategory(api_key='your_api_key', api_domain='your_domain')
parent_categories = category.get_parent_categories_list(id_category=10)
print(parent_categories)
# [2, 10]
```
```python
category = PrestaCategory(api_key='your_api_key', api_domain='your_domain')
parent_categories = category.get_parent_categories_list(id_category='10', parent_categories_list=[1,2,3])
print(parent_categories)
# [1, 2, 3, 2, 10]