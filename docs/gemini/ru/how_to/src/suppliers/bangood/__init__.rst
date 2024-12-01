Как использовать модуль bangood
========================================================================================

Описание
-------------------------
Этот модуль предоставляет функции для работы с поставщиком Banggood.  Он содержит классы и функции для получения данных о категориях и продуктах с сайта Banggood.

Шаги выполнения
-------------------------
1. Импортируйте необходимые классы и функции:
   ```python
   from .graber import Graber
   from .scenario import get_list_categories_from_site, get_list_products_in_category
   ```

2. Инициализируйте класс `Graber`, если требуется (в зависимости от вашей задачи). Например, для получения списка категорий:
   ```python
   graber = Graber() # Если класс требует инициализации
   categories = get_list_categories_from_site() 
   ```

3. Используйте функцию `get_list_categories_from_site()` для получения списка категорий с сайта Banggood. Результатом будет список ссылок на категории.

4. Для получения списка продуктов в конкретной категории используйте функцию `get_list_products_in_category()`. Передайте ей ссылку на категорию, полученную на предыдущем шаге.
   ```python
   category_url = categories[0]  #  Взяли первую категорию из списка
   products = get_list_products_in_category(category_url)
   ```
   Функция возвращает список с информацией о продуктах.

Пример использования
-------------------------
.. code-block:: python

    from .graber import Graber
    from .scenario import get_list_categories_from_site, get_list_products_in_category
    
    # Инициализация (если требуется)
    graber = Graber()

    try:
        categories = get_list_categories_from_site()
        if categories:
            print("Получены категории:")
            for category_url in categories:
                print(f"- {category_url}")

            # Получение продуктов из первой категории
            first_category_url = categories[0]
            products = get_list_products_in_category(first_category_url)
            if products:
                print("\nПолучены продукты из первой категории:")
                for product in products:
                    print(product) #  Предполагается, что product имеет атрибуты, которые можно распечатать.
            else:
                print("Список продуктов пуст.")
        else:
            print("Список категорий пуст.")
    except Exception as e:
        print(f"Ошибка: {e}")