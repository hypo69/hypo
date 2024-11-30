Как использовать метод get_parent_categories_list
========================================================================================

Описание
-------------------------
Этот метод получает список родительских категорий для заданной категории в PrestaShop. Он использует API PrestaShop для получения данных о категориях.  Метод рекурсивно вызывается, чтобы получить все родительские категории.

Шаги выполнения
-------------------------
1. **Проверка входных данных:** Проверяет, что `id_category` задан. Если нет, выводит ошибку в логгер и возвращает пустой список `parent_categories_list`.

2. **Получение данных о категории:** Использует базовый метод `get` класса `PrestaShop` для получения информации о категории с заданным `id_category`.  Запрос включает параметр `display='full'` для получения всех необходимых данных, и `io_format='JSON'` для получения данных в формате JSON.

3. **Обработка результата запроса:** Проверяет, что полученный результат не пуст. Если пуст, выводит ошибку в логгер и возвращает None.

4. **Извлечение id родительской категории:** Извлекает `id_parent` из полученного словаря `category`.

5. **Добавление родительской категории к списку:** Добавляет `id_parent` в список `parent_categories_list`.

6. **Рекурсивный вызов:** Если `id_parent` не является корневой категорией (меньше или равно 2), то метод рекурсивно вызывает сам себя с `id_parent` в качестве параметра `id_category`.

7. **Возврат списка:** Возвращает список `parent_categories_list`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.category import PrestaCategory
    # ... (код для инициализации PrestaCategory) ...
    
    api_key = "YOUR_API_KEY"
    api_domain = "YOUR_API_DOMAIN"
    credentials = {"api_domain": api_domain, "api_key": api_key}
    prestacategory = PrestaCategory(credentials=credentials)

    try:
        category_id = 123  # ID категории, для которой нужно получить родительские
        parent_categories = prestacategory.get_parent_categories_list(category_id)
        if parent_categories:
            print(f"Родительские категории для категории {category_id}: {parent_categories}")
        else:
          print("Родительские категории не найдены.")
    except ValueError as e:
        print(f"Ошибка: {e}")