# Модуль `hypotez/src/suppliers/bangood/__init__.py`

## Обзор

Этот модуль предоставляет функции и классы для работы с поставщиком Banggood.  Он содержит интерфейс для извлечения данных о категориях и продуктах с сайта Banggood.

## Оглавление

- [Модуль `hypotez/src/suppliers/bangood/__init__.py`](#модуль-hypotezsrcsuppliersbangoodinitpy)
- [Переменная `MODE`](#переменная-mode)
- [Класс `Graber`](#класс-graber)
- [Функция `get_list_categories_from_site`](#функция-get_list_categories_from_site)
- [Функция `get_list_products_in_category`](#функция-get_list_products_in_category)


## Переменная `MODE`

```python

```

**Описание**:  Указывает режим работы модуля (например, 'dev', 'prod'). По умолчанию установлен в 'dev'.


## Класс `Graber`

```python
from .graber import Graber
```

**Описание**: Класс `Graber` предоставляет методы для извлечения данных с сайта.  Подразумевает, что реализация методов в файле `graber.py` содержит логику взаимодействия с API Banggood.


## Функция `get_list_categories_from_site`

```python
from .scenario import get_list_categories_from_site
```

**Описание**: Возвращает список категорий с сайта Banggood.


**Возвращает**:
- `list`: Список словарей, где каждый словарь представляет категорию (имя, ID и т.д.).


## Функция `get_list_products_in_category`

```python
from .scenario import get_list_products_in_category
```

**Описание**: Возвращает список продуктов в заданной категории.


**Параметры**:
- `category_id` (int): Идентификатор категории.


**Возвращает**:
- `list`: Список словарей, где каждый словарь представляет продукт (имя, цена, ID и т.д.).