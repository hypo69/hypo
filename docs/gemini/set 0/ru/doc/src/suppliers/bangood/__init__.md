# Модуль hypotez/src/suppliers/bangood/__init__.py

## Обзор

Этот модуль предоставляет функции и классы для работы с поставщиком Bangood. Он содержит классы для сбора данных и функции для получения списков категорий и продуктов.

## Содержание

### Модульные переменные

* **`MODE` (str):**  Устанавливает режим работы, например, 'dev' или 'prod'. Значение по умолчанию 'dev'.

### Импорты

* **`Graber`**:  Класс для сбора данных с Bangood.  ([подробнее](#graber)).
* **`get_list_categories_from_site`**: Функция для получения списка категорий с сайта. ([подробнее](#get_list_categories_from_site)).
* **`get_list_products_in_category`**: Функция для получения списка продуктов в заданной категории. ([подробнее](#get_list_products_in_category)).

## Классы

### `Graber`

**Описание**: Класс для сбора данных с Bangood.

**Методы**
(Подробное описание методов `Graber` находится в файле `hypotez/src/suppliers/bangood/graber.py`)

## Функции

### `get_list_categories_from_site`

**Описание**: Возвращает список категорий с сайта Bangood.

**Возвращает**:
- `list[str]`: Список строк, представляющих названия категорий.


### `get_list_products_in_category`

**Описание**: Возвращает список продуктов, находящихся в указанной категории.


**Параметры**:
- `category_id` (str): Идентификатор категории.


**Возвращает**:
- `list`: Список словарей, каждый из которых описывает продукт.


**Примечания**: Более подробные детали реализации функций и классов, включая потенциальные исключения и возврат значений, находятся в соответствующих файлах.