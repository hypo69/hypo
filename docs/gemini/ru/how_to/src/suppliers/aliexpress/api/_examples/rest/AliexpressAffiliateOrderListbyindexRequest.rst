Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateOrderListbyindexRequest`, который представляет собой запрос к API AliExpress для получения списка заказов по аффилированным ссылкам.  Он наследуется от базового класса `RestApi` и предоставляет атрибуты для настройки параметров запроса (например, временные рамки, размер страницы, статус заказа). Метод `getapiname` возвращает имя API-метода.


Шаги выполнения
-------------------------
1. Импортирует класс `RestApi` из модуля `..base`.
2. Определяет класс `AliexpressAffiliateOrderListbyindexRequest`, который наследуется от `RestApi`.
3. В конструкторе `__init__` инициализирует параметры запроса:
    - `domain`:  устанавливает доменное имя API (по умолчанию `api-sg.aliexpress.com`).
    - `port`: устанавливает порт API (по умолчанию `80`).
    - `app_signature`, `end_time`, `fields`, `page_size`, `start_query_index_id`, `start_time`, `status`:  инициализирует атрибуты для указания параметров запроса (например, подписи приложения, временные рамки, поля, размер страницы и т.д.).  Эти параметры могут быть изменены перед использованием запроса.
4. Определяет метод `getapiname`, который возвращает имя API-метода (`aliexpress.affiliate.order.listbyindex`).  Этот метод необходим для идентификации запроса в API.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateOrderListbyindexRequest import AliexpressAffiliateOrderListbyindexRequest

    # Создаем экземпляр класса запроса
    request = AliexpressAffiliateOrderListbyindexRequest(
        domain="your-aliexpress-domain.com",  # Укажите ваш домен
        port=8080  # Укажите порт
    )

    # Устанавливаем параметры запроса
    request.app_signature = "your_app_signature"
    request.start_time = "2023-10-26"
    request.end_time = "2023-10-27"
    request.page_size = 100
    request.status = "paid"  # Например, статус заказа


    # Далее нужно вызвать метод для отправки запроса к API (который отсутствует в данном коде)
    # Например,  result = request.execute() или аналогичный метод.
    # Обратите внимание, что  request.execute()  необходимо реализовать в другом месте вашего кода
    # для выполнения фактического запроса к API.