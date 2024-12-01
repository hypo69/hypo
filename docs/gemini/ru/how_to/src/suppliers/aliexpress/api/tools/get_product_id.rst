Как использовать этот блок кода
=========================================================================================\n

Описание
-------------------------
Этот код определяет функцию `get_product_id`, которая извлекает идентификатор продукта из заданного текстового входного значения.  Функция использует функцию `extract_prod_ids` из модуля `src.suppliers.aliexpress.utils.extract_product_id` для извлечения ID. Если идентификатор продукта не найден, генерируется исключение `ProductIdNotFoundException`.  Исходный код также содержал неиспользуемый код для поиска ID по регулярному выражению, который теперь удален.

Шаги выполнения
-------------------------
1. Функция `get_product_id` принимает строку `raw_product_id` в качестве входного параметра.
2. Она вызывает функцию `extract_prod_ids` с переданным `raw_product_id` в качестве аргумента.
3. Функция `extract_prod_ids` обрабатывает входную строку, предполагая, что она содержит искомый идентификатор продукта и возвращает его в виде строки.
4. Результат (идентификатор продукта) возвращается из функции `get_product_id`.
5. Если `extract_prod_ids` не находит идентификатор, генерируется исключение `ProductIdNotFoundException` с сообщением об ошибке, содержащим исходный `raw_product_id`.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.tools.get_product_id import get_product_id
    from hypotez.src.suppliers.aliexpress.errors import ProductIdNotFoundException

    try:
        product_id = get_product_id("some_valid_product_id")
        print(f"Найденный идентификатор продукта: {product_id}")
    except ProductIdNotFoundException as e:
        print(f"Ошибка: {e}")

    try:
        product_id = get_product_id("неверный_id_продукта")
        print(f"Найденный идентификатор продукта: {product_id}")
    except ProductIdNotFoundException as e:
        print(f"Ошибка: {e}")