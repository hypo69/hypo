# Модуль hypotez/src/endpoints/prestashop/category.py

## Обзор

Модуль `hypotez/src/endpoints/prestashop/category.py` предоставляет класс `PrestaCategory` для взаимодействия с категориями в системе PrestaShop. Класс обеспечивает методы для добавления, удаления, обновления категорий, а также получения списка родительских категорий для заданной категории.  Он взаимодействует с API PrestaShop, используя для этого `requests`. Модуль обрабатывает и валидирует данные, полученные от API.

## Оглавление

- [Классы](#классы)
    - [PrestaCategory](#presta-category)
        - [__init__](#init)
        - [get_parent_categories_list](#get-parent-categories-list)


## Классы

### `PrestaCategory`

**Описание**:  Класс для работы с категориями в системе PrestaShop.  Предоставляет методы для взаимодействия с API, включая добавление, удаление, обновление категорий и получение родительских категорий.

**Пример использования**:

```python
prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
prestacategory.add_category_PrestaShop('New Category', 'Parent Category')
prestacategory.delete_category_PrestaShop(3)
prestacategory.update_category_PrestaShop(4, 'Updated Category Name')
print(prestacategory.get_parent_categories_list_PrestaShop(5))
```

#### `__init__`

**Описание**: Инициализация объекта `PrestaCategory`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  Не возвращает ничего.

**Вызывает исключения**:

- `ValueError`: Если не указаны `api_domain` и `api_key`.



#### `get_parent_categories_list`

**Описание**: Получает список родительских категорий для заданной категории.

**Параметры**:

- `id_category` (str | int): Идентификатор категории, для которой необходимо получить родительские категории.
- `parent_categories_list` (List[int], optional): Список родительских категорий. По умолчанию пустой список.

**Возвращает**:
- `list`: Список идентификаторов родительских категорий. Возвращает `parent_categories_list` если id_category пустое.

**Вызывает исключения**:
- `logger.error`:  Выводит ошибки, если id_category отсутствует или данные некорректны.  В этом случае возвращает пустой список.


**Подробности**:  Функция рекурсивно обходит родительские категории, пока не достигнет корневой категории (id_parent <= 2).  Обработка ошибок (нет категории, некорректные данные) реализована.


```


```