# Модуль `hypotez/src/endpoints/prestashop/category.py`

## Обзор

Модуль `hypotez/src/endpoints/prestashop/category.py` предоставляет класс `PrestaCategory` для взаимодействия с категориями в системе PrestaShop. Класс предоставляет методы для добавления, удаления, обновления категорий, а также получения списка родительских категорий для заданной категории.  Модуль реализует взаимодействие с API PrestaShop для работы с категориями.  Документация описывает функциональность класса `PrestaCategory`, включая методы и их параметры.

## Оглавление

- [Модуль `hypotez/src/endpoints/prestashop/category.py`](#модуль-hypotezsrcendpointsprestashopcategorypy)
- [Обзор](#обзор)
- [Класс `PrestaCategory`](#класс-prestacategory)
    - [`__init__`](#init)
    - [`get_parent_categories_list`](#get-parent-categories-list)


## Класс `PrestaCategory`

### Описание

Класс `PrestaCategory` наследуется от `PrestaShop` и предоставляет методы для работы с категориями PrestaShop.


### `__init__`

**Описание**: Инициализирует объект `PrestaCategory`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.


**Возвращает**:
-  Не имеет возвращаемого значения.

**Возможные исключения**:
- `ValueError`: Если не указаны `api_domain` и `api_key`.



### `get_parent_categories_list`

**Описание**: Получает список родительских категорий для заданной категории по её ID.

**Параметры**:
- `id_category` (str | int): ID категории, для которой нужно получить список родительских категорий.
- `parent_categories_list` (List[int], optional): Список родительских категорий (используется для рекурсивного вызова). По умолчанию пустой список.


**Возвращает**:
- list: Список ID родительских категорий. Возвращает пустой список, если `id_category` не задан или категория не найдена.

**Возможные исключения**:
- `ValueError`: Если передан некорректный `id_category`.
- Другие исключения, возникающие при взаимодействии с API PrestaShop.

**Детали**:
- Функция реализует рекурсивный вызов для получения всех родительских категорий.
- Базовый случай рекурсии – когда `id_category` соответствует корневой категории (`id_category` <= 2).
- Логика получения родительских категорий реализована через API PrestaShop.
- Функция использует `logger` для вывода диагностической информации и обработки ошибок.


```