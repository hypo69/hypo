Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateCategoryGetRequest`, который наследуется от класса `RestApi`.  Этот класс предназначен для отправки запроса на получение данных о категориях для аффилиатной программы AliExpress.  Он инициализирует соединение с API AliExpress и содержит метод для получения имени API-метода.

Шаги выполнения
-------------------------
1. **Инициализация:** При создании экземпляра класса `AliexpressAffiliateCategoryGetRequest` необходимо указать домен (`domain`) и порт (`port`) API AliExpress. По умолчанию используется `api-sg.aliexpress.com` и порт `80`.
2. **Получение имени API-метода:** Метод `getapiname()` возвращает строку 'aliexpress.affiliate.category.get', которая представляет имя API-метода для запроса данных о категориях.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateCategoryGetRequest

    # Создание экземпляра класса
    api_request = AliexpressAffiliateCategoryGetRequest()

    # Получение имени API-метода
    api_name = api_request.getapiname()
    print(f"Имя API-метода: {api_name}")