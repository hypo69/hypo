Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateHotproductQueryRequest`, который представляет собой запрос к API AliExpress для получения горячих продуктов.  Класс наследуется от `RestApi` и предоставляет параметры для настройки запроса, такие как категория, цена, ключевые слова и т.д.  Метод `getapiname` возвращает имя API-метода.

Шаги выполнения
-------------------------
1. **Импортирование класса `RestApi`**: Код импортирует класс `RestApi` из модуля `..base`.
2. **Определение класса `AliexpressAffiliateHotproductQueryRequest`**: Определяется класс `AliexpressAffiliateHotproductQueryRequest`, который наследуется от `RestApi`.
3. **Инициализация параметров запроса**: Конструктор `__init__` инициализирует объект запроса, принимая домен и порт, а также устанавливая значения по умолчанию для различных параметров запроса (например, `app_signature`, `category_ids`, `delivery_days` и др.).
4. **Определение метода `getapiname`**: Этот метод возвращает строку `aliexpress.affiliate.hotproduct.query`, которая идентифицирует конкретный API-метод для запроса горячих продуктов.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateHotproductQueryRequest import AliexpressAffiliateHotproductQueryRequest

    # Создаем объект запроса, устанавливая необходимые параметры.
    request = AliexpressAffiliateHotproductQueryRequest(
        domain="api-sg.aliexpress.com",
        keywords="smartwatch"
    )

    request.category_ids = [123, 456]
    request.max_sale_price = 100
    request.page_no = 1
    request.page_size = 20


    # Отправка запроса (предполагается, что у вас есть необходимые функции для отправки запроса через RestApi).
    # Пример (замените на реальную логику отправки запроса):
    response = request.getResponse()

    # Обработка ответа (предполагается, что у вас есть функции для обработки ответа RestApi):
    result = request.parseResponse(response)
    print(result)