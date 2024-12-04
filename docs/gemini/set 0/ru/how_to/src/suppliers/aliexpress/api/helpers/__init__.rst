Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код импортирует функции из модулей `requests`, `arguments`, `products` и `categories`, относящихся к API AliExpress.  Он предоставляет инструменты для работы с запросами к API, обработкой аргументов, парсингом продуктов и фильтрацией категорий.

Шаги выполнения
-------------------------
1. Импортируются функции `api_request` из модуля `requests`. Эта функция, скорее всего, отвечает за отправку HTTP-запросов к API AliExpress.
2. Импортируются функции `get_list_as_string` и `get_product_ids` из модуля `arguments`.  Эти функции, вероятно, предназначены для подготовки входных данных (списков, идентификаторов продуктов) для API-запросов.
3. Импортируется функция `parse_products` из модуля `products`.  Эта функция вероятно парсит JSON-ответ API AliExpress и преобразует его в удобный для работы формат (например, список словарей с данными о продуктах).
4. Импортируются функции `filter_parent_categories` и `filter_child_categories` из модуля `categories`. Эти функции предназначены для фильтрации категорий продуктов, возможно, на основе родительских или дочерних категорий.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers import api_request, get_product_ids, parse_products

    # Пример использования функции get_product_ids (предполагается, что есть входные данные product_ids)
    product_ids_list = [123, 456, 789]
    product_ids_string = get_product_ids(product_ids_list)  # Преобразует список в строку, подходящую для API

    # Пример использования api_request (предполагается, что есть URL и параметры запроса)
    url = "https://aliexpress.com/api/products"
    params = {"product_ids": product_ids_string, "other_params": "some_values"}
    response = api_request(url, params)

    # Пример использования parse_products (предполагается, что response - ответ от api_request)
    parsed_products = parse_products(response)

    # Пример фильтрации категорий (предполагается наличие response)
    filtered_parent_categories = filter_parent_categories(response, parent_category_id=100)

    # далее работа с результатами parsed_products и filtered_parent_categories