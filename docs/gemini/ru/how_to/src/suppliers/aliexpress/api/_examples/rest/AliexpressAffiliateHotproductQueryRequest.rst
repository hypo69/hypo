Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateHotproductQueryRequest`, который представляет запрос к API AliExpress для получения горячих товаров.  Класс наследуется от `RestApi`, предоставляя базовые методы для работы с API.  Он инициализирует параметры запроса, такие как категория, цена, язык и т.д. и содержит метод для получения имени API.

Шаги выполнения
-------------------------
1. **Импортирование:** Модуль `RestApi` импортируется из родительского модуля `..base`.
2. **Инициализация класса:**  Создается экземпляр класса `AliexpressAffiliateHotproductQueryRequest`. При этом можно указать домен и порт API (по умолчанию "api-sg.aliexpress.com" и 80).
3. **Установка параметров:**  Класс позволяет установить различные параметры запроса, такие как `category_ids`, `keywords`, `max_sale_price`, `page_no`, и другие.  Эти параметры используются для фильтрации и сортировки результатов.
4. **Получение имени API:** Метод `getapiname` возвращает строку "aliexpress.affiliate.hotproduct.query", идентифицирующую конкретный метод API.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateHotproductQueryRequest import AliexpressAffiliateHotproductQueryRequest

    # Создание объекта запроса
    request = AliexpressAffiliateHotproductQueryRequest()

    # Установка параметров запроса
    request.category_ids = [123, 456]  # Укажите ID категорий
    request.keywords = "товары для дома"  # Ключевые слова для поиска
    request.page_no = 1
    request.page_size = 20

    # Вызов метода для получения имени API
    api_name = request.getapiname()
    print(f"Имя API: {api_name}")

    # Далее, вы можете использовать объект 'request' для отправки запроса к API AliExpress
    # используя методы родительского класса RestApi. Например, request.getResponse()