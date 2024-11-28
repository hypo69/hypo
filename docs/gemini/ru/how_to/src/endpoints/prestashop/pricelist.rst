Как использовать класс PriceListRequester
========================================================================================

Описание
-------------------------
Класс `PriceListRequester` предназначен для запроса списка цен товаров из Престашоп API. Он наследуется от класса `PrestaShop` и предоставляет методы для запроса цен, обновления источника данных и изменения цены товара.  Класс `PriceListRequester` инициализируется учетными данными API (домен и ключ).

Шаги выполнения
-------------------------
1. **Инициализация:** Создайте экземпляр класса `PriceListRequester`, передавая ему словарь `api_credentials` с ключами `api_domain` и `api_key`.

2. **Запрос цен:**  Используйте метод `request_prices`, передавая список товаров (`products`). Метод должен вернуть словарь, где ключи - это названия товаров, а значения - соответствующие цены.  Этот метод **отправляет запрос** на сервер Престашоп API.

3. **Обновление источника данных:** Используйте метод `update_source`, передавая новый источник данных (`new_source`) для запроса цен.

4. **Изменение цены товара:** Метод `modify_product_price` позволяет **изменить** цену товара (`product`) на новую цену (`new_price`) в источнике данных.

Пример использования
-------------------------
.. code-block:: python

    import json
    from hypotez.src.endpoints.prestashop.pricelist import PriceListRequester

    # Учетные данные для Престашоп API
    api_credentials = {
        'api_domain': 'ваш_домен_престашоп',
        'api_key': 'ваш_ключ_престашоп'
    }

    # Список товаров
    products = ['product1', 'product2']

    # Создание экземпляра класса
    requester = PriceListRequester(api_credentials)

    # Запрос цен
    try:
        prices = requester.request_prices(products)
        print(json.dumps(prices, indent=2))
    except Exception as e:
        print(f"Ошибка при запросе цен: {e}")

    # Пример обновления источника данных
    new_source = 'новый_источник'
    requester.update_source(new_source)

    # Пример изменения цены товара
    product_to_modify = 'product1'
    new_price = 15.99
    requester.modify_product_price(product_to_modify, new_price)