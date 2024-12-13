# Модуль `src.suppliers.bangood`

## Обзор

Модуль `src.suppliers.bangood` предназначен для сбора данных с сайта Banggood. Он включает в себя функциональность для парсинга категорий и товаров.

## Оглавление

1. [Переменные](#переменные)
2. [Импортированные модули](#импортированные-модули)
3. [Функции](#функции)

## Переменные

### `MODE`
**Описание**: Режим работы модуля.
- **Значение**: `'dev'`

## Импортированные модули
- `from .graber import Graber`: Импортирует класс `Graber` из модуля `graber`.
- `from .scenario import get_list_categories_from_site, get_list_products_in_category`: Импортирует функции `get_list_categories_from_site` и `get_list_products_in_category` из модуля `scenario`.

## Функции

### `get_list_categories_from_site`

**Описание**: Функция для получения списка категорий с сайта. Подробное описание функции смотрите в модуле `scenario`.

### `get_list_products_in_category`

**Описание**: Функция для получения списка товаров в определенной категории. Подробное описание функции смотрите в модуле `scenario`.