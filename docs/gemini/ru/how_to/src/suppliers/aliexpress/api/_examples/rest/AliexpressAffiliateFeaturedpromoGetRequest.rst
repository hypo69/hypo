Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateFeaturedpromoGetRequest`, который наследуется от класса `RestApi`.  Этот класс предназначен для взаимодействия с API AliExpress, конкретно для получения данных о рекомендуемых промоакциях.  Он инициализирует необходимые параметры для запроса, такие как домен и порт, и предоставляет метод для получения имени API-метода.

Шаги выполнения
-------------------------
1. **Импортирует класс `RestApi`:** Импортирует базовый класс для работы с API.
2. **Определяет класс `AliexpressAffiliateFeaturedpromoGetRequest`:** Создаёт новый класс, который наследуется от `RestApi`.
3. **Инициализирует класс:** В конструкторе (`__init__`) класса устанавливает домен и порт для подключения к API AliExpress. Также инициализирует переменные `app_signature` и `fields` для хранения соответствующих параметров.
4. **Возвращает имя API-метода:** Метод `getapiname` возвращает строку 'aliexpress.affiliate.featuredpromo.get', которая идентифицирует API-метод для получения данных о рекомендуемых промоакциях.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateFeaturedpromoGetRequest

    # Создаем экземпляр класса
    api_request = AliexpressAffiliateFeaturedpromoGetRequest()

    # (Дополнительно) Установка параметров:
    # api_request.app_signature = "ваш_ключ_приложения"
    # api_request.fields = {"param1": "value1", "param2": "value2"}

    # Получаем имя API-метода
    api_name = api_request.getapiname()
    print(f"Имя API-метода: {api_name}")