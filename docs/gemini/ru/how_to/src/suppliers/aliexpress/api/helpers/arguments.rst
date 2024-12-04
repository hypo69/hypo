Как использовать этот блок кода
=========================================================================================\n

Описание
-------------------------
Модуль `arguments.py` содержит функции для обработки аргументов, связанных с продуктами AliExpress. Он преобразует входные данные в нужные форматы, проверяет их корректность и возвращает обработанные значения.  Функция `get_list_as_string` преобразует список в строку, разделенную запятыми, или возвращает строку, если входной параметр уже строка. Функция `get_product_ids` обрабатывает список или строку идентификаторов продуктов, преобразуя их в список идентификаторов, полученных с помощью функции `get_product_id`.

Шаги выполнения
-------------------------
1. **Проверка на `None`:** Функция `get_list_as_string` проверяет, является ли входной параметр `value` равным `None`. Если да, то функция возвращает `None`.
2. **Проверка типа:** Функция `get_list_as_string` проверяет, является ли входной параметр `value` строкой (`str`). Если да, то функция возвращает эту строку.
3. **Проверка типа (список):** Функция `get_list_as_string` проверяет, является ли входной параметр `value` списком (`list`). Если да, то функция объединяет элементы списка в строку, используя запятую в качестве разделителя, и возвращает эту строку.
4. **Исключение `InvalidArgumentException`:** Если ни одно из условий выше не выполняется, функция вызывает исключение `InvalidArgumentException`, передавая сообщение об ошибке с типом неверного аргумента.

5. **Проверка типа input `values`:** Функция `get_product_ids` проверяет, является ли входной параметр `values` строкой (`str`). Если да, то функция разбивает эту строку на список элементов, используя запятую в качестве разделителя.
6. **Проверка типа (список):** Функция `get_product_ids` проверяет, является ли входной параметр `values` списком (`list`). Если нет, функция вызывает исключение `InvalidArgumentException`, указывая на необходимость списка или строки в качестве входных данных.
7. **Инициализация `product_ids`:**  Создается пустой список `product_ids` для хранения результатов.
8. **Итерация по элементам списка:** Функция итерируется по каждому элементу списка `values`.
9. **Получение `product_id`:** Для каждого элемента списка, функция `get_product_id` используется для получения соответствующего идентификатора продукта.
10. **Добавление в список:** Полученный идентификатор добавляется в список `product_ids`.
11. **Возврат результата:** Функция возвращает список `product_ids`.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers.arguments import get_product_ids, get_list_as_string
    from hypotez.src.suppliers.aliexpress.api.helpers.arguments import InvalidArgumentException

    # Пример использования get_list_as_string
    result = get_list_as_string(['apple', 'banana', 'orange'])
    print(result)  # Вывод: apple,banana,orange

    result = get_list_as_string('apple')
    print(result)  # Вывод: apple

    # Пример использования get_product_ids
    product_list = ['product1', 'product2']
    product_ids = get_product_ids(product_list)
    print(product_ids)  # Вывод: список с полученными id (product1, product2)

    product_string = 'product3,product4'
    product_ids = get_product_ids(product_string)
    print(product_ids)  # Вывод: список с полученными id (product3, product4)

    try:
        product_ids = get_product_ids(123)  # Некорректный тип
    except InvalidArgumentException as e:
        print(f"Ошибка: {e}")  # Вывод: Ошибка: Argument product_ids should be a list or string