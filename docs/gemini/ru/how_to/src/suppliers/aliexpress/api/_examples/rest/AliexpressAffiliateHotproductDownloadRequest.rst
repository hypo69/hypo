Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateHotproductDownloadRequest`, который представляет собой запрос к API AliExpress для скачивания горячих продуктов. Класс наследуется от `RestApi`, предоставляя базовый функционал для работы с API.  Он инициализирует параметры запроса, такие как домен, ID категории, страну и т.д., и определяет имя API-метода.

Шаги выполнения
-------------------------
1. **Импортирует необходимый класс:** `RestApi` импортируется из модуля `..base`.
2. **Инициализирует класс:** Создаёт экземпляр класса `AliexpressAffiliateHotproductDownloadRequest`, передавая необходимые параметры, такие как домен ("api-sg.aliexpress.com") и порт (80).
3. **Устанавливает параметры запроса:**  Класс инициализирует переменные для хранения различных параметров, необходимых для запроса (например, `category_id`, `country`, `fields` и т.д.)
4. **Определяет имя API-метода:** Метод `getapiname` возвращает строку 'aliexpress.affiliate.hotproduct.download', которая используется для вызова соответствующего API-метода.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateHotproductDownloadRequest

    # Создаем экземпляр класса, устанавливая необходимые параметры
    request = AliexpressAffiliateHotproductDownloadRequest(
        domain="api-sg.aliexpress.com",
        # ... добавьте другие параметры, такие как category_id, country, etc.
    )

    request.category_id = 123
    request.country = "US"
    # ... задаем другие параметры


    #  (В реальном приложении здесь должен быть вызов метода для отправки запроса к API)
    #  Например, если у класса RestApi есть метод для отправки, то его вызов был бы здесь.

    # Пример:
    # api_response = request.send_request()
    # print(api_response)