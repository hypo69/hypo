Как использовать метод retrieve_product_details_as_dict
=====================================================================================

Описание
-------------------------
Метод `retrieve_product_details_as_dict` из класса `AliApi` получает подробные сведения о продуктах AliExpress по списку их идентификаторов.  Он отправляет запрос на сервер AliExpress, получая данные в формате `SimpleNamespace` и преобразует их в удобный формат словарей.

Шаги выполнения
-------------------------
1. **Получение списка идентификаторов продуктов:**  Сформировать список (`product_ids`)  уникальных идентификаторов продуктов, которые необходимо получить.
2. **Вызов метода `retrieve_product_details`:** Передать список `product_ids` в метод `retrieve_product_details` класса `AliApi`. Это отправляет запрос к API AliExpress для получения информации о продуктах.
3. **Преобразование в формат словарей:** Результат метода `retrieve_product_details` (список объектов `SimpleNamespace`) преобразуется в список словарей (`prod_details_dict`) с помощью выражения `[vars(ns) for ns in prod_details_ns]`.  Это делает данные более удобными для работы с ними.
4. **Возврат результата:**  Метод возвращает список словарей (`prod_details_dict`), содержащих данные о продуктах.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.aliapi import AliApi
    from types import SimpleNamespace
    import pprint

    # Пример списка идентификаторов продуктов
    product_ids = [12345, 67890, 11111]

    # Создаем экземпляр класса AliApi
    aliapi = AliApi()


    #  Имитация получения данных от AliExpress (замена реального запроса)
    namespace_list = [
        SimpleNamespace(product_id=12345, name="Product 1", price=10.99, description="Description 1"),
        SimpleNamespace(product_id=67890, name="Product 2", price=20.50, description="Description 2"),
        SimpleNamespace(product_id=11111, name="Product 3", price=15.00, description="Description 3")
    ]

    try:
        product_data = aliapi.retrieve_product_details_as_dict(product_ids)
        pprint.pprint(product_data)
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")