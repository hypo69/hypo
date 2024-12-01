Как использовать модуль hypotez/src/suppliers/aliexpress/api/helpers
=====================================================================================

Описание
-------------------------
Данный модуль `hypotez/src/suppliers/aliexpress/api/helpers` предоставляет набор функций для работы с API AliExpress. Он содержит функции для отправки запросов, обработки аргументов, парсинга данных о продуктах и фильтрации категорий.

Шаги выполнения
-------------------------
Модуль экспортирует несколько функций:

1. `api_request`: Функция для отправки запросов к API AliExpress.  Она принимает URL, параметры и тип запроса (GET/POST).  Возвращает результат запроса или ошибку.
2. `get_list_as_string`: Преобразует список в строку, подходящую для использования в запросах API (например, для списка идентификаторов продуктов).
3. `get_product_ids`: Извлекает список идентификаторов продуктов из входных данных.
4. `parse_products`: Парсит данные о продуктах, полученные из ответа API, в удобный формат.
5. `filter_parent_categories`: Фильтрует список категорий, оставляя только родительские категории.
6. `filter_child_categories`: Фильтрует список категорий, оставляя только дочерние категории.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers import api_request, get_product_ids, parse_products

    # Пример использования функции get_product_ids:
    product_ids = get_product_ids({'products': [123, 456, 789]})  # предполагается, что входные данные - словарь
    print(f"Идентификаторы продуктов: {product_ids}")

    # Пример использования функции api_request:
    url = "https://aliexpress-api.com/products"
    params = {"ids": product_ids}
    try:
        response = api_request(url, params, method='GET')
        parsed_data = parse_products(response.json())  # предполагается, что функция parse_products обрабатывает JSON
        print(parsed_data)

    except Exception as e:
        print(f"Ошибка при запросе: {e}")

    #Пример использования filter_parent_categories:
    categories = [{"id": 1, "parent_id": None}, {"id": 2, "parent_id": 1}, {"id": 3, "parent_id": 2}]
    parent_categories = filter_parent_categories(categories)
    print(f"Родительские категории: {parent_categories}")

    #Пример использования filter_child_categories:
    child_categories = filter_child_categories(categories)
    print(f"Дочерние категории: {child_categories}")