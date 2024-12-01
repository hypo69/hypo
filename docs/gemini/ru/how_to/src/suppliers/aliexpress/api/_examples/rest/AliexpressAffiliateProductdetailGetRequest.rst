Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateProductdetailGetRequest`, представляющий собой запрос к API AliExpress для получения подробной информации о продукте.  Класс наследуется от базового класса `RestApi` и предоставляет методы для инициализации запроса и получения имени API.  Он позволяет настраивать параметры запроса, такие как идентификаторы продуктов, валюту и язык.

Шаги выполнения
-------------------------
1. **Импортирование класса `RestApi`**: Код импортирует базовый класс `RestApi` из модуля `..base`.

2. **Инициализация класса `AliexpressAffiliateProductdetailGetRequest`**:  Создается экземпляр класса `AliexpressAffiliateProductdetailGetRequest`, принимая в качестве аргументов домен API (`api-sg.aliexpress.com`) и порт (80). Базовый класс `RestApi` также инициализируется в этом шаге.

3. **Настройка параметров запроса**: Класс предоставляет атрибуты для настройки параметров запроса:
    - `app_signature`: Подпись приложения.
    - `country`: Страна.
    - `fields`: Список полей для возврата.
    - `product_ids`: Список идентификаторов продуктов.
    - `target_currency`: Целевая валюта.
    - `target_language`: Целевой язык.
    - `tracking_id`: Идентификатор отслеживания.
    Можно задавать значения этих параметров при создании экземпляра класса или позже.


4. **Получение имени API**: Метод `getapiname()` возвращает строку 'aliexpress.affiliate.productdetail.get', которая представляет имя API-метода для запроса деталей продукта.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateProductdetailGetRequest import AliexpressAffiliateProductdetailGetRequest

    # Создание экземпляра класса с настройкой параметров
    request = AliexpressAffiliateProductdetailGetRequest(domain="api-sg.aliexpress.com", port=80)
    request.product_ids = [123, 456]  # Устанавливаем идентификаторы продуктов
    request.target_currency = "USD"  # Устанавливаем валюту
    request.target_language = "en"  # Устанавливаем язык

    # Получение имени API
    api_name = request.getapiname()
    print(f"Имя API: {api_name}")

    # Дальнейшие действия с запросом (например, отправка запроса и обработка ответа) 
    #  (в примере показан только метод получения имени).