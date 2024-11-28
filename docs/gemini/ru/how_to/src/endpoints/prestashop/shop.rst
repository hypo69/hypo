Как использовать класс PrestaShopShop
========================================================================================

Описание
-------------------------
Класс `PrestaShopShop` расширяет класс `PrestaShop` и предоставляет методы для работы с магазинами PrestaShop.  Он инициализируется параметрами, определяющими домен API и ключ API для взаимодействия с магазином.  Класс проверяет наличие необходимых параметров и выдает ошибку `ValueError`, если они не указаны.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей:**  Код импортирует необходимые модули, включая `PrestaShop`, `SimpleNamespace`, `Optional`, `header`, `gs`, `logger`, `j_loads` и другие, для работы с API Престашоп и логированием.

2. **Определение класса `PrestaShopShop`:** Создается класс `PrestaShopShop`, который наследуется от класса `PrestaShop`.

3. **Инициализация класса:** Конструктор `__init__` принимает параметры:
    - `credentials`: Словарь или объект `SimpleNamespace` с ключами `api_domain` и `api_key`.
    - `api_domain`: Домен API.
    - `api_key`: Ключ API.

4. **Обработка входных данных:** Если параметр `credentials` передан, значения `api_domain` и `api_key` из него будут взяты в приоритете, если они уже не заданы напрямую.

5. **Проверка параметров:** Проверяется, что параметры `api_domain` и `api_key` заданы. Если хотя бы один из параметров отсутствует, генерируется исключение `ValueError` с сообщением "Необходимы оба параметра: api_domain и api_key".

6. **Вызов конструктора родительского класса:**  `super().__init__(api_domain, api_key, *args, **kwards)` вызывает конструктор базового класса `PrestaShop`, передавая ему полученные значения `api_domain` и `api_key`.

Пример использования
-------------------------
.. code-block:: python

    from types import SimpleNamespace
    from hypotez.src.endpoints.prestashop.shop import PrestaShopShop

    # Пример использования с использованием словаря:
    credentials = {
        'api_domain': 'ваш_домен_api',
        'api_key': 'ваш_ключ_api'
    }

    try:
        shop_client = PrestaShopShop(credentials=credentials)
        # Теперь можно использовать методы класса PrestaShopShop,
        # например, для работы с магазином PrestaShop.
        # ...ваш код для взаимодействия с PrestaShop...
    except ValueError as e:
        print(f"Ошибка: {e}")


    # Пример использования с использованием объекта SimpleNamespace:
    credentials_ns = SimpleNamespace(api_domain='ваш_домен_api', api_key='ваш_ключ_api')
    try:
        shop_client = PrestaShopShop(credentials=credentials_ns)
        # ...ваш код для взаимодействия с PrestaShop...
    except ValueError as e:
        print(f"Ошибка: {e}")