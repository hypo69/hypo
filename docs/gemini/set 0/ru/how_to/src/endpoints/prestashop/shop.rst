Как использовать класс PrestaShopShop
========================================================================================

Описание
-------------------------
Класс `PrestaShopShop` предоставляет методы для взаимодействия с магазинами PrestaShop. Он расширяет базовый класс `PrestaShop`, добавляя специфические методы для работы с магазинами.  Класс инициализируется с параметрами доступа к API, такими как домен и ключ API.  Он проверяет наличие необходимых параметров и, при их отсутствии, генерирует ошибку.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей**:  Код импортирует необходимые модули, такие как `SimpleNamespace`, `Optional`, `PrestaShop`,  `PrestaShopException`, и другие вспомогательные модули.


2. **Инициализация класса `PrestaShopShop`**:  Класс `PrestaShopShop` принимает параметры для инициализации:
   - `credentials`: Словарь или объект `SimpleNamespace`, содержащий параметры доступа (`api_domain`, `api_key`).
   - `api_domain`: Домен API.
   - `api_key`: Ключ API.

   Если параметр `credentials` передан, значения `api_domain` и `api_key` берутся из него.

3. **Проверка обязательных параметров**:  Код проверяет, что оба параметра `api_domain` и `api_key` установлены. Если нет, генерируется исключение `ValueError`.

4. **Вызов конструктора родительского класса**:  Если проверка пройдена, инициализируется родительский класс `PrestaShop`, передавая в него значения `api_domain` и `api_key`.


Пример использования
-------------------------
.. code-block:: python

    from types import SimpleNamespace
    from hypotez.src.endpoints.prestashop.shop import PrestaShopShop
    
    # Пример использования с dict
    credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
    shop = PrestaShopShop(credentials=credentials)

    # Пример использования с SimpleNamespace
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    shop = PrestaShopShop(credentials=credentials)

    # Обратите внимание, что вы должны заменить 'your_api_domain' и 'your_api_key' на свои реальные данные.
    
    try:
        # Теперь вы можете использовать методы класса PrestaShopShop, например, для запросов к API магазина.
        # ... ваш код для работы с API PrestaShop ...
    except ValueError as e:
        print(f"Ошибка: {e}")