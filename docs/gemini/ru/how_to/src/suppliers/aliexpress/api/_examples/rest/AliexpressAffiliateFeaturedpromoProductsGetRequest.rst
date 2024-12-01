Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, представляющий запрос к API AliExpress для получения данных о промо-продуктах.  Класс наследуется от базового класса `RestApi`, что указывает на использование REST API.  Он инициализирует параметры запроса, такие как идентификатор категории, страну, поля, номера страниц, даты начала и окончания промоакции, имя акции, сортировку, валюту и язык.  Также он определяет имя API-метода (`aliexpress.affiliate.featuredpromo.products.get`).

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей**: Код импортирует класс `RestApi` из модуля `..base`.
2. **Инициализация класса `AliexpressAffiliateFeaturedpromoProductsGetRequest`**:  Создается экземпляр класса, принимая в качестве аргументов домен (`domain`) и порт (`port`) API AliExpress.
3. **Установка параметров запроса**:  Класс позволяет задать различные параметры запроса, такие как `category_id`, `country`, `fields`, `page_no`, `page_size` и другие.  Эти параметры будут использоваться при формировании запроса к API.
4. **Получение имени API-метода**: Метод `getapiname` возвращает строку, представляющую имя метода API, который будет использован для запроса (`aliexpress.affiliate.featuredpromo.products.get`).

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateFeaturedpromoProductsGetRequest

    # Создаем экземпляр класса, устанавливая необходимые параметры
    request = AliexpressAffiliateFeaturedpromoProductsGetRequest(
        domain="api-sg.aliexpress.com",
        port=80,
        category_id=123,
        country="US",
        page_no=1,
        page_size=10,
    )

    # Получаем имя API-метода
    api_name = request.getapiname()
    print(f"Имя API-метода: {api_name}")

    # Дальнейшие действия (например, отправка запроса к API и обработка ответа)
    # ...