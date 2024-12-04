Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `PriceListRequester`, который наследуется от класса `PrestaShop` и предназначен для запроса списка цен товаров из Престашоп API. Класс содержит методы для инициализации, запроса цен, обновления источника данных и изменения цены товара.  Класс `PriceListRequester` взаимодействует с внешним источником данных (API) для получения и изменения цен товаров.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует необходимые модули, включая `sys`, `os`, `attr`, `pathlib`, `typing`, `header`, `gs`, `logger`, `jjson`, `PrestaShop`, и `SimpleNamespace`.  Эти импорты необходимы для работы кода.

2. **Определение класса `PriceListRequester`:**  Класс наследуется от `PrestaShop`, что указывает на то, что он использует методы и атрибуты из этого класса.

3. **Инициализация объекта:** Метод `__init__` принимает словарь `api_credentials` с учетными данными API, включая `api_domain` и `api_key`, и инициализирует экземпляр класса `PrestaShop` с этими данными.

4. **Запрос цен товаров:** Метод `request_prices` принимает список товаров `products` и отправляет запрос в API для получения цен на эти товары.  Важно, что в текущем коде реализация запроса отсутствует.  В этом месте необходимо реализовать логику запроса к API Престашоп.

5. **Обновление источника данных:** Метод `update_source` принимает новый источник данных `new_source` и обновляет внутреннее значение `self.source`.  Это используется для переключения на другой API или источник информации, если это необходимо.

6. **Изменение цены товара:** Метод `modify_product_price` принимает название товара `product` и новую цену `new_price` и отправляет запрос для изменения цены товара в источнике данных.  Аналогично методу `request_prices`, в текущем коде реализация запроса отсутствует.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.pricelist import PriceListRequester
    import os

    # Укажите путь к файлу с учетными данными (например, json)
    credentials_file = os.path.join('credentials.json')

    try:
        with open(credentials_file, 'r') as f:
            api_credentials = j_loads(f.read()) # Предполагается, что j_loads из jjson модуля
    except FileNotFoundError:
        print(f"Ошибка: файл {credentials_file} не найден.")
        exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    products_to_get = ['product1', 'product2']

    requester = PriceListRequester(api_credentials)
    prices = requester.request_prices(products_to_get)

    if prices:
        print("Полученные цены:")
        for product, price in prices.items():
            print(f"Цена товара {product}: {price}")
    else:
        print("Ошибка при получении цен.")

    # пример изменения цены
    product_to_change = 'product1'
    new_price = 12.99
    requester.modify_product_price(product_to_change, new_price)
    print(f"Цена товара {product_to_change} изменена на {new_price}")