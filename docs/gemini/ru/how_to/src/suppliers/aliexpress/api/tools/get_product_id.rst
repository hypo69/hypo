Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Функция `get_product_id` извлекает идентификатор продукта из предоставленного текста.  Она использует функцию `extract_prod_ids` из модуля `src.suppliers.aliexpress.utils.extract_product_id`.  Если идентификатор продукта не найден, функция генерирует исключение `ProductIdNotFoundException`.  Функция возвращает строку, содержащую идентификатор продукта.  Ранее в функции был реализован поиск идентификатора продукта по образцу регулярных выражений в строке, но в текущей версии этот код удалён, и используется только функция `extract_prod_ids`.

Шаги выполнения
-------------------------
1. Функция принимает на вход строку `raw_product_id`.
2. Функция вызывает функцию `extract_prod_ids` с переданным в качестве аргумента значением `raw_product_id`.
3. Функция возвращает результат работы функции `extract_prod_ids`.
4. Если функция `extract_prod_ids` возвращает None, возникает исключение `ProductIdNotFoundException`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.tools.get_product_id import get_product_id
    from hypotez.src.suppliers.aliexpress.errors import ProductIdNotFoundException

    try:
        product_id = get_product_id("12345")
        print(f"Идентификатор продукта: {product_id}")

    except ProductIdNotFoundException as e:
        print(f"Ошибка: {e}")


    try:
        product_id = get_product_id("https://www.aliexpress.com/item/1234567890/63422123142.html")
        print(f"Идентификатор продукта: {product_id}")
    except ProductIdNotFoundException as e:
        print(f"Ошибка: {e}")