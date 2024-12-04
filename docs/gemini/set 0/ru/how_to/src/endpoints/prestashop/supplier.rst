Как использовать класс PrestaSupplier
========================================================================================

Описание
-------------------------
Класс `PrestaSupplier` предназначен для работы с поставщиками в системе PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API.  Класс инициализируется данными для доступа к API, такими как домен и ключ.  Если данные передаются в виде словаря или объекта `SimpleNamespace`, то значения `api_domain` и `api_key` из него будут использованы в качестве параметров инициализации. Если эти параметры не предоставлены явно, то возникает ошибка.

Шаги выполнения
-------------------------
1. Импортировать необходимые модули: `SimpleNamespace`, `Optional`, `header`, `gs`, `logger`, `j_loads`, `PrestaShop` из соответствующих модулей.

2. Создать экземпляр класса `PrestaSupplier`.  При создании экземпляра можно передать параметры инициализации:
    - `credentials`: Словарь или объект `SimpleNamespace` содержащий `api_domain` и `api_key`.
    - `api_domain`: Домен API PrestaShop.
    - `api_key`: Ключ API PrestaShop.
    Если `credentials` предоставлен, то значения `api_domain` и `api_key` из него будут использованы.

3. Проверить корректность параметров.  Если `api_domain` или `api_key` не заданы, вызовется исключение `ValueError` с сообщением "Необходимы оба параметра: api_domain и api_key".

4. Инициализировать родительский класс `PrestaShop`, передавая полученные `api_domain` и `api_key`.

Пример использования
-------------------------
.. code-block:: python

    from types import SimpleNamespace
    from hypotez.src.endpoints.prestashop.supplier import PrestaSupplier
    
    # Пример 1: передача параметров через credentials
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    supplier = PrestaSupplier(credentials=credentials)
    
    # Пример 2: передача параметров напрямую
    supplier2 = PrestaSupplier(api_domain='your_api_domain', api_key='your_api_key')
    
    # Обратите внимание, что далее нужно использовать методы, определенные в родительском классе PrestaShop.
    # Например, чтобы получить данные, нужно использовать методы этого класса
    # try:
    #     response = supplier.get_products()
    #     print(response.json())  # Обработка ответа
    # except Exception as e:
    #     print(f"Ошибка: {e}")