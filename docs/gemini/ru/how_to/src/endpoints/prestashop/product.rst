Как использовать класс PrestaProduct
========================================================================================

Описание
-------------------------
Этот класс предоставляет методы для работы с товарами в системе PrestaShop через API.  Он наследуется от класса `PrestaShop`, предоставляя общие методы для взаимодействия с API.  Класс содержит методы для проверки наличия товара по артикулу, расширенного поиска и получения информации о товаре по ID.  Он также включает инициализацию с параметрами для подключения к API.

Шаги выполнения
-------------------------
1. **Инициализация:** Создайте экземпляр класса `PrestaProduct`, передав необходимые данные для подключения к API.  Это могут быть `credentials` (словарь или `SimpleNamespace` с `api_domain` и `api_key`), или `api_domain` и `api_key` напрямую.  Если `credentials` переданы, `api_domain` и `api_key` из него будут взяты по умолчанию.

2. **Проверка наличия товара (check):**  Вызовите метод `check(product_reference: str)`, передав в качестве аргумента `product_reference` (SKU или MKT товара).  Метод вернет словарь с информацией о товаре, если он найден, иначе вернёт `False`.

3. **Расширенный поиск (search):** Вызовите метод `search(filter: str, value: str)`, передав `filter` (например, `name`, `reference`) и `value` (значение для фильтра). Метод выполнит поиск и вернет результат.

4. **Получение информации о товаре по ID (get):** Вызовите метод `get(id_product)`, передав `id_product` (ID товара). Метод вернет словарь с информацией о товаре.

5. **Обработка исключений:**  Код содержит проверку на наличие `api_domain` и `api_key`. Если они не предоставлены, будет выброшено исключение `ValueError`. Обработайте это исключение, чтобы избежать сбоев программы.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.product import PrestaProduct
    from types import SimpleNamespace

    # Инициализация с использованием credentials
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    product_api = PrestaProduct(credentials=credentials)

    # Проверка наличия товара
    product_data = product_api.check('12345')
    if product_data:
        pprint(product_data)
    else:
        print("Товар не найден.")

    # Расширенный поиск
    search_results = product_api.search('name', 'футболка')
    pprint(search_results)


    # Получение товара по ID
    product_by_id = product_api.get(10)
    pprint(product_by_id)

    # Инициализация с передачей api_domain и api_key напрямую
    product_api2 = PrestaProduct(api_domain='your_api_domain', api_key='your_api_key')