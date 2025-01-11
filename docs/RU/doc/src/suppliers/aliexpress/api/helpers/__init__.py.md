# Модуль `hypotez/src/suppliers/aliexpress/api/helpers/__init__.py`

## Обзор

Модуль `__init__.py` пакета `hypotez/src/suppliers/aliexpress/api/helpers`  инициализирует и предоставляет доступ к различным вспомогательным функциям и модулям, используемым для работы с API AliExpress. Модуль импортирует и делает доступными функции для формирования запросов к API, обработки аргументов, парсинга продуктов и фильтрации категорий.

## Оглавление

1.  [Обзор](#обзор)
2.  [Импортируемые модули и функции](#импортируемые-модули-и-функции)

## Импортируемые модули и функции

В данном модуле импортируются следующие функции и модули:

-   `api_request` из `hypotez/src/suppliers/aliexpress/api/helpers/requests.py`: Функция для отправки запросов к API AliExpress.
-   `get_list_as_string`, `get_product_ids` из `hypotez/src/suppliers/aliexpress/api/helpers/arguments.py`: Функции для обработки аргументов запросов.
-   `parse_products` из `hypotez/src/suppliers/aliexpress/api/helpers/products.py`: Функция для парсинга данных о продуктах.
-   `filter_parent_categories`, `filter_child_categories` из `hypotez/src/suppliers/aliexpress/api/helpers/categories.py`: Функции для фильтрации категорий.