Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `PrestaShopShop`, наследуемый от класса `PrestaShop`.  Он предназначен для работы с магазинами PrestaShop и инициализирует соединение с API PrestaShop.  Класс проверяет наличие необходимых параметров для подключения (api_domain, api_key) и выбрасывает исключение `ValueError`, если они отсутствуют.

Шаги выполнения
-------------------------
1. Импортирует необходимые модули: `SimpleNamespace`, `Optional`, `header`, `gs`, `logger`, `j_loads`, `PrestaShop`, `PrestaShopException`, `Path`, `attr`, `sys`, `os`.
2. Определяет класс `PrestaShopShop`, наследующийся от `PrestaShop`.
3. Определяет конструктор `__init__` класса `PrestaShopShop`.
4. Если `credentials` (словарь или `SimpleNamespace`) переданы, то извлекает значения `api_domain` и `api_key` из `credentials`, используя метод `get()`. Это позволяет использовать `credentials` в качестве источника параметров подключения.
5. Проверяет, что `api_domain` и `api_key` не пусты. Если они отсутствуют, выбрасывается исключение `ValueError`.
6. Вызывает конструктор родительского класса `PrestaShop` с полученными значениями `api_domain` и `api_key`. Это устанавливает соединение с API PrestaShop.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.shop import PrestaShopShop
    from types import SimpleNamespace
    
    # Пример использования credentials в виде SimpleNamespace
    credentials = SimpleNamespace(api_domain="ваш_домен", api_key="ваш_ключ")
    
    try:
        shop_client = PrestaShopShop(credentials=credentials)
        # Далее можно использовать shop_client для взаимодействия с API PrestaShop
        # Например, shop_client.get_products()
    except ValueError as e:
        print(f"Ошибка: {e}")
        
    # Пример без использования credentials, передавая параметры напрямую
    try:
      shop_client2 = PrestaShopShop(api_domain="ваш_домен", api_key="ваш_ключ")
    except ValueError as e:
      print(f"Ошибка: {e}")