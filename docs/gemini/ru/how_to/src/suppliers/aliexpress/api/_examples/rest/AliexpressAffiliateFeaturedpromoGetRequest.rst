Как использовать этот блок кода
=========================================================================================\n\nОписание
-------------------------
Этот код определяет класс `AliexpressAffiliateFeaturedpromoGetRequest`, который наследуется от класса `RestApi`. Он предназначен для запроса данных о промоакциях на AliExpress через API.  Класс предоставляет методы для инициализации соединения и получения имени API-метода.

Шаги выполнения
-------------------------
1. Импортирует класс `RestApi` из модуля `..base`.
2. Определяет класс `AliexpressAffiliateFeaturedpromoGetRequest`, который наследуется от `RestApi`.
3. В конструкторе `__init__` инициализирует соединение с API, принимая `domain` (по умолчанию "api-sg.aliexpress.com") и `port` (по умолчанию 80).
4. Инициализирует атрибуты `app_signature` и `fields` со значениями `None`.  Эти атрибуты, вероятно, будут использованы для дополнительной настройки запроса.
5. Определяет метод `getapiname`, который возвращает имя API-метода: `aliexpress.affiliate.featuredpromo.get`.  Это имя используется для идентификации конкретного API-запроса.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateFeaturedpromoGetRequest

    # Создаем экземпляр класса, указывая желаемый домен
    api_request = AliexpressAffiliateFeaturedpromoGetRequest(domain="api-us.aliexpress.com")

    # Получаем имя API-метода
    api_name = api_request.getapiname()
    print(f"Имя API-метода: {api_name}")