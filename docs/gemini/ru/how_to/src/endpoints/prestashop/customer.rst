Как использовать класс PrestaCustomer
=========================================================================================

Описание
-------------------------
Класс `PrestaCustomer` предоставляет методы для взаимодействия с клиентами в системе управления интернет-магазином PrestaShop. Он наследуется от класса `PrestaShop`, предоставляя базовые функции API.  Класс позволяет добавлять, удалять, обновлять и получать информацию о клиентах.  Инициализация требует параметров `api_domain` и `api_key`, которые могут быть переданы как через отдельные аргументы, так и в виде словаря или объекта `SimpleNamespace`.


Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей:**  Код импортирует необходимые библиотеки, включая `attr`, `pathlib`, `typing`, `SimpleNamespace`, `header`, `gs`, `logger`, `j_loads`, `PrestaShop`,  и другие, необходимые для работы с API PrestaShop и логирования.

2. **Определение класса `PrestaCustomer`:**  Класс наследуется от `PrestaShop`. Он содержит конструктор `__init__`, который инициализирует необходимые параметры.

3. **Обработка входных данных:**  Конструктор проверяет, были ли переданы `credentials`. Если да, то извлекает значения `api_domain` и `api_key` из `credentials`.

4. **Проверка параметров:** Если `api_domain` или `api_key` не были заданы, то генерируется исключение `ValueError` с сообщением об обязательности указания обоих параметров.

5. **Вызов конструктора родительского класса:**  `super().__init__(api_domain, api_key, *args, **kwards)` вызывает конструктор родительского класса `PrestaShop`, передавая необходимые параметры.

6. **Методы для работы с клиентами:**  Класс `PrestaCustomer` содержит методы для добавления (`add_customer_PrestaShop`), удаления (`delete_customer_PrestaShop`), обновления (`update_customer_PrestaShop`) и получения данных (`get_customer_details_PrestaShop`) клиентов.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.customer import PrestaCustomer
    import os

    # Замените на ваши данные
    API_DOMAIN = os.environ.get("API_DOMAIN")
    API_KEY = os.environ.get("API_KEY")

    if not API_DOMAIN or not API_KEY:
        raise ValueError("Необходимо указать API_DOMAIN и API_KEY")
        
    credentials = {"api_domain": API_DOMAIN, "api_key": API_KEY}
    prestacustomer = PrestaCustomer(credentials=credentials)
    
    try:
        # Добавление нового клиента
        result = prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
        print(f"Результат добавления: {result}")


        # Удаление клиента
        result = prestacustomer.delete_customer_PrestaShop(123) # Замените 123 на ID клиента
        print(f"Результат удаления: {result}")


        # Обновление клиента
        result = prestacustomer.update_customer_PrestaShop(123, 'Updated Customer Name')
        print(f"Результат обновления: {result}")

        # Получение данных о клиенте
        result = prestacustomer.get_customer_details_PrestaShop(123)
        print(f"Подробности о клиенте: {result}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")