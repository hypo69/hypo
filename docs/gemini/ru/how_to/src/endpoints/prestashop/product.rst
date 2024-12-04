Как использовать класс PrestaProduct
========================================================================================

Описание
-------------------------
Класс `PrestaProduct` предоставляет методы для взаимодействия с API PrestaShop, позволяя проверять наличие товара, искать товары по фильтрам и получать информацию о товаре по его ID.  Он наследуется от класса `PrestaShop`, предоставляя базовые методы для работы с API.  Класс инициализируется данными для подключения к API.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей**: Импортируются необходимые модули, такие как `SimpleNamespace`, `typing`, `logger`, `printer`, и `PrestaShop`.

2. **Инициализация класса `PrestaProduct`**:  Создается экземпляр класса `PrestaProduct`, передавая параметры для подключения к API:
    - `credentials`: Словарь или объект `SimpleNamespace` с полями `api_domain` и `api_key`.
    - `api_domain`: Домен API.
    - `api_key`: Ключ API.

3. **Проверка параметров**: Проверяется, что `api_domain` и `api_key` заданы. Если нет, то генерируется исключение `ValueError`.

4. **Инициализация родительского класса**: Вызывается метод `__init__` родительского класса `PrestaShop` с полученными параметрами `api_domain` и `api_key`.

5. **Вызов методов класса `PrestaProduct`**: После успешной инициализации, можно использовать методы класса:
    - `check(product_reference: str)`:  Проверяет наличие товара в базе данных по заданному `product_reference` (например, SKU или MKT). Возвращает словарь с информацией о товаре, если он найден, иначе `False`.
    - `search(filter: str, value: str)`: Выполняет расширенный поиск по базе данных, используя заданные `filter` и `value`.
    - `get(id_product)`: Возвращает подробную информацию о товаре по его уникальному `id_product`.


Пример использования
-------------------------
.. code-block:: python

    from types import SimpleNamespace
    from hypotez.src.endpoints.prestashop.product import PrestaProduct
    
    # Пример данных для авторизации
    credentials = SimpleNamespace(api_domain="ваш_домен_api", api_key="ваш_ключ_api")

    try:
        # Создание экземпляра класса
        product_api = PrestaProduct(credentials=credentials)

        # Пример проверки товара по SKU
        product_info = product_api.check("12345")
        if product_info:
            pprint(product_info)  # Вывод информации о товаре
        else:
            print("Товар не найден")

        # Пример поиска товара
        search_results = product_api.search(filter="name", value="футболка")
        pprint(search_results)  # Вывод результатов поиска

        # Пример получения товара по id
        product_details = product_api.get(12345)
        pprint(product_details)

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")