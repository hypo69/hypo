Как использовать функции get_list_as_string и get_product_ids
========================================================================================

Описание
-------------------------
Функция `get_list_as_string` преобразует входное значение в строку, разделенную запятыми, если это список. В противном случае, если вход - строка, она возвращает ее. В иных случаях выбрасывает исключение `InvalidArgumentException`.  Функция `get_product_ids` преобразует входные данные в список идентификаторов продуктов, используя функцию `get_product_id`.  Она обрабатывает как строку, так и список в качестве входных данных, преобразуя строку в список, прежде чем обрабатывать каждый элемент.


Шаги выполнения
-------------------------
1. **Функция `get_list_as_string`**:
    - Проверяет, является ли входное значение `value` равным `None`. Если да, возвращает `None`.
    - Проверяет, является ли `value` строкой. Если да, возвращает строку.
    - Проверяет, является ли `value` списком. Если да, соединяет элементы списка в строку, разделяя их запятыми, и возвращает полученную строку.
    - В противном случае, выбрасывает исключение `InvalidArgumentException` с сообщением об ошибке.


2. **Функция `get_product_ids`**:
    - Проверяет, является ли входное значение `values` строкой. Если да, разбивает строку на список по разделителю запятая.
    - Проверяет, является ли `values` списком. Если нет, выбрасывает исключение `InvalidArgumentException`.
    - Инициализирует пустой список `product_ids`.
    - Проходит по каждому элементу `value` в `values`.
    - Для каждого элемента вызывает функцию `get_product_id(value)`, добавляя возвращаемый идентификатор продукта в список `product_ids`.
    - Возвращает список `product_ids`.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers.arguments import get_list_as_string, get_product_ids
    from hypotez.src.suppliers.aliexpress.api.helpers.arguments import InvalidArgumentException

    # Пример использования get_list_as_string
    list_val = ['product1', 'product2', 'product3']
    string_val = "product4,product5"
    none_val = None

    print(get_list_as_string(list_val))  # Вывод: product1,product2,product3
    print(get_list_as_string(string_val)) # Вывод: product4,product5
    print(get_list_as_string(none_val)) # Вывод: None
    try:
        print(get_list_as_string(123))
    except InvalidArgumentException as e:
        print(f"Ошибка: {e}")  # Вывод: Ошибка: Argument should be a list or string: 123


    # Пример использования get_product_ids
    product_strings = ["product1", "product2,product3"]
    product_list = ["product4", "product5"]

    product_ids = get_product_ids(product_strings)
    print(product_ids) #  (Результат зависит от реализации get_product_id, например, список чисел)

    product_ids_list = get_product_ids(product_list)
    print(product_ids_list) #  (Результат зависит от реализации get_product_id, например, список чисел)
    try:
        product_ids = get_product_ids(123)
    except InvalidArgumentException as e:
        print(f"Ошибка: {e}") # Вывод: Ошибка: Argument product_ids should be a list or string