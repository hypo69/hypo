# Модуль для работы с категориями PrestaShop

## Обзор

Модуль `category.py` предназначен для управления категориями в PrestaShop. Он предоставляет класс `PrestaCategory`, который позволяет получать информацию о родительских категориях. Класс наследуется от `PrestaShop`, что обеспечивает взаимодействие с API PrestaShop.

## Подробней

Этот модуль является частью системы для управления интернет-магазином на платформе PrestaShop. Он позволяет автоматизировать процесс получения иерархии категорий, что может быть полезно для навигации по сайту, формирования структуры каталога и других задач.

## Классы

### `PrestaCategory(PrestaShop)`

**Описание**: Класс для управления категориями в PrestaShop. Наследуется от класса `PrestaShop`.

**Как работает класс**:

1.  При инициализации класса `PrestaCategory` вызывается конструктор родительского класса `PrestaShop` с передачей параметров `api_key` и `api_domain`, необходимых для аутентификации и подключения к API PrestaShop.
2.  Метод `get_parent_categories_list` используется для рекурсивного получения списка родительских категорий для заданной категории.

**Методы**:

*   `__init__(self, api_key: str, api_domain: str, *args, **kwargs)`: Инициализирует объект класса `PrestaCategory`.
*   `get_parent_categories_list(self, id_category: str | int, parent_categories_list: List[int|str] = []) -> List[int]`: Получает список родительских категорий для заданной категории.

#### `__init__(self, api_key: str, api_domain: str, *args, **kwargs)`

```python
    def __init__(self, api_key:str, api_domain:str, *args, **kwargs):
        """
        Initializes a Product object.

        """

        super().__init__( api_key = api_key ,api_domain = api_domain, *args, **kwargs)
```

**Назначение**: Инициализирует объект класса `PrestaCategory`.

**Как работает функция**:
Вызывает конструктор родительского класса `PrestaShop` с передачей параметров `api_key` и `api_domain`, необходимых для аутентификации и подключения к API PrestaShop.

**Параметры**:

*   `api_key` (str): Ключ API для доступа к PrestaShop.
*   `api_domain` (str): Доменное имя PrestaShop.
*   `*args`: Произвольные позиционные аргументы.
*   `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `PrestaShopError`: Если возникает ошибка при инициализации родительского класса.

#### `get_parent_categories_list(self, id_category: str | int, parent_categories_list: List[int|str] = []) -> List[int]`

```python
    def get_parent_categories_list(self, id_category: str | int, parent_categories_list: List[int|str] = []) -> List[int]:
        """! Retrieve parent categories from PrestaShop for a given category."""
        if not id_category:
            logger.error("Missing category ID.")
            return parent_categories_list

        category = super().get('categories', resource_id=id_category, display='full', io_format='JSON')
        if not category:
            logger.error("Issue with retrieving categories.")
            return

        _parent_category = int(category['id_parent'])
        parent_categories_list.append(_parent_category)

        if _parent_category <= 2:
            return parent_categories_list
        else:
            return self.get_parent_categories_list(_parent_category, parent_categories_list)
```

**Назначение**: Получает список родительских категорий из PrestaShop для заданной категории.

**Как работает функция**:

1.  Проверяет, передан ли `id_category`. Если нет, логирует ошибку и возвращает текущий список родительских категорий.
2.  Вызывает метод `get` родительского класса `PrestaShop` для получения информации о категории по ее `id`.
3.  Если категория не найдена, логирует ошибку и возвращает `None`.
4.  Извлекает `id_parent` из полученной информации о категории и добавляет его в список родительских категорий.
5.  Если `id_parent` меньше или равен 2, возвращает список родительских категорий.
6.  В противном случае рекурсивно вызывает себя с `id_parent` в качестве аргумента для получения родительских категорий верхнего уровня.

**Параметры**:

*   `id_category` (str | int): ID категории, для которой нужно получить список родительских категорий.
*   `parent_categories_list` (List[int|str], optional): Список родительских категорий. По умолчанию `[]`.

**Возвращает**:

*   `List[int]`: Список ID родительских категорий.

**Вызывает исключения**:

*   `PrestaShopError`: Если возникает ошибка при получении информации о категории из PrestaShop.

## Функции

В данном модуле нет отдельных функций, не принадлежащих классам.