# Модуль hypotez/src/suppliers/bangood/__init__.py

## Обзор

Этот модуль предоставляет функции и классы для работы с поставщиком Bangood. Он содержит класс `Graber` для извлечения данных и функции для получения списка категорий и продуктов.

## Оглавление

* [Модуль hypotez/src/suppliers/bangood/__init__.py](#модуль-hypotezsrcsuppliersbangoodinitpy)
    * [Переменная MODE](#переменная-mode)
    * [Класс Graber](#класс-graber)
    * [Функция get\_list\_categories\_from\_site](#функция-get_list_categories_from_site)
    * [Функция get\_list\_products\_in\_category](#функция-get_list_products_in_category)


## Переменная MODE

```python
MODE = 'dev'
```

**Описание**: Переменная, определяющая режим работы модуля. В данном случае, значение `'dev'` указывает на режим разработки.


## Класс Graber

```python
from .graber import Graber
```

**Описание**: Класс для извлечения данных с сайта Bangood. Подробное описание методов класса находится в файле `graber.py`.


## Функция get_list_categories_from_site

```python
from .scenario import get_list_categories_from_site
```

**Описание**: Возвращает список категорий с сайта Bangood.

**Возвращает**:
* `list`: Список словарей, где каждый словарь представляет категорию и содержит информацию о ней.


## Функция get_list_products_in_category

```python
from .scenario import get_list_products_in_category
```

**Описание**: Возвращает список продуктов из заданной категории на Bangood.

**Параметры**:
* `category_id` (int): ID категории для получения продуктов.

**Возвращает**:
* `list`: Список словарей, где каждый словарь представляет продукт и содержит информацию о нем.

**Вызывает исключения**:
* `ValueError`: Если передан некорректный `category_id`.