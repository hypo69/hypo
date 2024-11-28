Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `PrestaCustomer`, который наследуется от класса `PrestaShop` и предоставляет методы для работы с клиентами в системе управления интернет-магазином PrestaShop.  Класс позволяет добавлять, удалять, обновлять клиентов и получать информацию о клиентах.  Он также обрабатывает инициализацию с различными способами передачи параметров.

Шаги выполнения
-------------------------
1. **Импортирует необходимые модули:** Модули `sys`, `os`, `attr`, `pathlib`, `typing`, `types`, `header`, `gs`, `logger`, `jjson`, `api`, и другие, необходимые для работы с API PrestaShop и логированием.

2. **Определяет константу MODE:** Устанавливает режим работы.

3. **Определяет класс `PrestaCustomer`:** Этот класс наследуется от класса `PrestaShop`, что означает, что он использует методы и атрибуты `PrestaShop`.

4. **Определяет метод `__init__`:** Метод инициализирует объект `PrestaCustomer`. Он принимает параметры `credentials`, `api_domain`, и `api_key`.  Если `credentials` предоставлен, то значения `api_domain` и `api_key` извлекаются из него.  Если `api_domain` или `api_key` не заданы, то генерируется ошибка `ValueError`.  В противном случае, инициализируется родительский класс `PrestaShop` с заданными параметрами.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.customer import PrestaCustomer
    import os

    # Замените на ваши значения
    API_DOMAIN = os.environ.get('PRESTASHOP_API_DOMAIN')
    API_KEY = os.environ.get('PRESTASHOP_API_KEY')


    if API_DOMAIN is None or API_KEY is None:
        print("Ошибка: Не найдены переменные окружения PRESTASHOP_API_DOMAIN и/или PRESTASHOP_API_KEY")
    else:
        try:
            prestacustomer = PrestaCustomer(api_domain=API_DOMAIN, api_key=API_KEY)
            new_customer_name = 'Jane Doe'
            new_customer_email = 'janedoe@example.com'
            customer_id_to_delete = 10
            customer_id_to_update = 12
            customer_name_updated = 'Updated Jane Doe'
            customer_id_to_get = 15

            prestacustomer.add_customer_PrestaShop(new_customer_name, new_customer_email)
            prestacustomer.delete_customer_PrestaShop(customer_id_to_delete)
            prestacustomer.update_customer_PrestaShop(customer_id_to_update, customer_name_updated)
            print(prestacustomer.get_customer_details_PrestaShop(customer_id_to_get))

        except ValueError as e:
            print(f"Ошибка валидации: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")