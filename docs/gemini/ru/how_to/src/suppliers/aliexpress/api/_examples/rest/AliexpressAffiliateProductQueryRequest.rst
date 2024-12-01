Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateProductQueryRequest`, который представляет запрос к API AliExpress для получения информации о продуктах. Класс наследуется от класса `RestApi`, предоставляя базовые методы для работы с API.  Он инициализирует параметры запроса, такие как `app_signature`, `category_ids` и другие, позволяющие фильтровать и сортировать результаты.  Метод `getapiname` возвращает имя API-метода для запроса.

Шаги выполнения
-------------------------
1. **Импортирование класса `RestApi`**: Код импортирует класс `RestApi` из модуля `..base`.
2. **Определение класса `AliexpressAffiliateProductQueryRequest`**: Определяется класс, который наследуется от `RestApi`.
3. **Инициализация параметров запроса**:  Конструктор класса инициализирует различные параметры запроса (например, `app_signature`, `category_ids`, `delivery_days` и т.д.).  Это позволяет пользователю задавать параметры для поиска.
4. **Указание имени API-метода**: Метод `getapiname` возвращает строку 'aliexpress.affiliate.product.query', которая идентифицирует конкретный метод API AliExpress.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateProductQueryRequest

    # Создаем экземпляр класса, задавая параметры запроса.
    query_request = AliexpressAffiliateProductQueryRequest(
        domain="api-sg.aliexpress.com",
        category_ids=["123", "456"]  # Пример категорий
    )

    # Получение имени API-метода
    api_name = query_request.getapiname()
    print(f"Идентификатор API метода: {api_name}")