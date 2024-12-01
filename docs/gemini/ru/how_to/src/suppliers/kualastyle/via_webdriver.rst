Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Функция `get_list_products_in_category` извлекает список ссылок на продукты, находящиеся на странице категории. Она использует драйвер веб-драйвера для взаимодействия с сайтом и находит ссылки на продукты, используя локаторы.

Шаги выполнения
-------------------------
1. Функция принимает в качестве аргумента объект `s`, содержащий информацию о поставщике, включая веб-драйвер (`s.driver`) и локаторы (`s.locators`).
2. Получает локаторы элементов на странице категории (`l = s.locators.get('category')`).
3. Прокручивает страницу вниз (`d.scroll(scroll_count = 10, direction = "forward")`). Это необходимо, если ссылки на продукты находятся ниже видимой области страницы.
4. Выполняет поиск ссылок на продукты, используя `d.execute_locator` с локаторами (`l['product_links']`).
5. Возвращает список ссылок на продукты (`list_products_in_category`).

Пример использования
-------------------------
.. code-block:: python

    # Предполагается, что у вас есть объект "supplier_object" с необходимыми атрибутами.
    from src.suppliers.kualastyle import via_webdriver # or import the specific file
    import src.suppliers.kualastyle as supplier
    
    supplier_object = supplier.Supplier(...)  # Замените ... на инициализацию вашего объекта
    
    try:
        product_links = via_webdriver.get_list_products_in_category(supplier_object)
        if product_links:
            for link in product_links:
                print(link)
        else:
            print("Список ссылок на продукты пуст или не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")