Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateOrderListbyindexRequest`, который наследуется от класса `RestApi`.  Этот класс предназначен для работы с API AliExpress и позволяет получать список заказов по аффилированным ссылкам.  Он инициализирует параметры запроса, необходимые для получения списка заказов (время начала и конца, размер страницы, индекс начала, статус).  Также он содержит метод `getapiname`, который возвращает имя API-метода.

Шаги выполнения
-------------------------
1. **Инициализация класса:**  Создается экземпляр класса `AliexpressAffiliateOrderListbyindexRequest`, передавая необходимые параметры, такие как домен (`domain`) и порт (`port`) API AliExpress.  Этот шаг инициализирует атрибуты класса, которые будут использоваться для формирования запроса к API.
2. **Установка параметров запроса:**  К объекту класса `AliexpressAffiliateOrderListbyindexRequest` устанавливаются параметры, такие как `start_time`, `end_time`, `page_size`, `start_query_index_id`, `status`.  Эти параметры определяют фильтры для поиска заказов.
3. **Получение имени API-метода:** Метод `getapiname()` возвращает строку 'aliexpress.affiliate.order.listbyindex', которая соответствует названию API-метода для получения списка заказов.  Эта информация используется для формирования правильного запроса.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateOrderListbyindexRequest

    # Создаем экземпляр класса, задавая параметры
    request = AliexpressAffiliateOrderListbyindexRequest()
    request.start_time = "2023-10-26"
    request.end_time = "2023-10-27"
    request.page_size = 10
    request.start_query_index_id = 1

    # Получаем имя API-метода
    api_name = request.getapiname()
    print(api_name) # Выведет: aliexpress.affiliate.order.listbyindex

    # Дальше необходимо использовать полученные данные для взаимодействия с API (например, с помощью `RestApi.execute`)