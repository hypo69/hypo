Как использовать модуль поставщиков (suppliers)
========================================================================================

Описание
-------------------------
Этот модуль (`hypotez/src/suppliers/__init__.py`) предоставляет базовый класс `Supplier` и инструменты для работы с поставщиками.  Он определяет структуру для добавления методов, специфичных для каждого поставщика, например, Amazon, Aliexpress, Morlevi. Эти специфичные методы реализуются в отдельных файлах, соответствующих префиксу имени поставщика (например, `amazon.py`, `aliexpress.py`).  Модуль также импортирует классы `Graber`, `Context` и функцию `close_pop_up` из модуля `graber`.  Константа `MODE` определяет режим работы.

Шаги выполнения
-------------------------
1. Импортировать необходимые классы и функции из модуля:
   ```python
   from hypotez.src.suppliers.supplier import Supplier
   from hypotez.src.suppliers.graber import Graber, Context, close_pop_up
   ```
2. Создать экземпляр класса `Supplier` (или наследовать от него).
3. Импортировать методы конкретного поставщика:
   ```python
   from hypotez.src.suppliers.<supplier_prefix> import <specific_method>
   ```
   Например, для работы с Amazon:
   ```python
   from hypotez.src.suppliers.amazon import get_amazon_products
   ```
4. Вызвать метод `supplier.specific_method()` для выполнения действий, специфичных для данного поставщика.
5.  Использовать классы `Graber`, `Context` и функцию `close_pop_up` для взаимодействия с веб-драйвером.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.supplier import Supplier
    from hypotez.src.suppliers.graber import Graber, Context, close_pop_up
    from hypotez.src.suppliers.amazon import get_amazon_products

    # Предполагаем, что у вас есть необходимая инициализация веб-драйвера
    driver = Graber()
    context = Context(driver)

    # Создаем экземпляр класса Supplier, возможно с дополнительными параметрами
    supplier = Supplier(context=context)

    # Добавляем специфичный метод для Amazon
    supplier.add_method(get_amazon_products)

    # Вызываем метод для получения продуктов с Amazon
    products_data = supplier.get_amazon_products()  # Используем имя метода, добавленного в Supplier

    # ... Обработка полученных данных ...

    # Закрываем окно браузера
    close_pop_up(driver)
    driver.close()