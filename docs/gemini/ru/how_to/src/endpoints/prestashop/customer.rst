Как использовать класс PrestaCustomer
========================================================================================

Описание
-------------------------
Класс `PrestaCustomer` предоставляет методы для взаимодействия с клиентами в системе PrestaShop через API. Он наследуется от класса `PrestaShop`, предоставляя базовые функции работы с API.  Класс позволяет добавлять, удалять, обновлять клиентов и получать их детали.  Он также обрабатывает валидацию входных данных и выдает исключения при проблемах.

Шаги выполнения
-------------------------
1. **Инициализация:**  Создается экземпляр класса `PrestaCustomer`, передавая необходимые параметры:
    - `credentials`: Словарь или объект `SimpleNamespace`, содержащий `api_domain` и `api_key`.
    - `api_domain`: Домен API PrestaShop.
    - `api_key`: Ключ API PrestaShop.

    Если `credentials` не передан, необходимо передать `api_domain` и `api_key` напрямую.

2. **Проверка валидности входных данных:**  Метод `__init__` проверяет, что `api_domain` и `api_key`  переданы.  Если хотя бы один параметр отсутствует, генерируется исключение `ValueError`.

3. **Использование методов:** После успешной инициализации, можно использовать методы класса для работы с клиентами:
    - `add_customer_PrestaShop(name, email)`: Добавляет нового клиента с заданным именем и email.
    - `delete_customer_PrestaShop(id)`: Удаляет клиента по его идентификатору.
    - `update_customer_PrestaShop(id, new_name)`: Обновляет имя клиента по его идентификатору.
    - `get_customer_details_PrestaShop(id)`: Возвращает детали клиента по его идентификатору.

4. **Обработка возможных ошибок:**  Класс использует  класс `PrestaShopException` для обработки ошибок, которые могут возникнуть при взаимодействии с API PrestaShop.  В случае возникновения ошибки, будет выброшено соответствующее исключение.


Пример использования
-------------------------
.. code-block:: python

    from types import SimpleNamespace
    import os
    
    # Замените на ваши реальные значения
    API_DOMAIN = os.environ.get('API_DOMAIN')
    API_KEY = os.environ.get('API_KEY')

    credentials = SimpleNamespace(api_domain=API_DOMAIN, api_key=API_KEY)

    try:
        prestacustomer = PrestaCustomer(credentials=credentials)
        # Добавление клиента
        prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
        # Получение деталей клиента
        customer_details = prestacustomer.get_customer_details_PrestaShop(1)
        print(customer_details)
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    except PrestaShopException as e:
        print(f"Ошибка взаимодействия с API: {e}")