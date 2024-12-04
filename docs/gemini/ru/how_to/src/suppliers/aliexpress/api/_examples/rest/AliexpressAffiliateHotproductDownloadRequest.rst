Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateHotproductDownloadRequest`, представляющий запрос для скачивания горячих продуктов из API AliExpress.  Класс наследуется от базового класса `RestApi`, обеспечивая общую функциональность для работы с REST API.  Он позволяет настраивать параметры запроса, такие как идентификатор категории, страну, язык и другие критерии.  Метод `getapiname` возвращает имя API-метода.

Шаги выполнения
-------------------------
1. **Импортирование класса `RestApi`:**  Код импортирует базовый класс `RestApi` из модуля `..base`.

2. **Определение класса `AliexpressAffiliateHotproductDownloadRequest`:** Создается класс, который наследуется от `RestApi`.

3. **Инициализация параметров запроса:** Конструктор класса инициализирует атрибуты, представляющие параметры запроса (например, `category_id`, `country`, `page_no`, `page_size` и др.).  Значения по умолчанию не заданы.

4. **Установка имени API-метода:** Метод `getapiname` возвращает строку 'aliexpress.affiliate.hotproduct.download', идентифицирующую необходимый API-метод.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateHotproductDownloadRequest

    # Создаем экземпляр класса
    request = AliexpressAffiliateHotproductDownloadRequest()

    # Устанавливаем значения параметров
    request.category_id = 123
    request.country = "US"
    request.page_no = 1
    request.page_size = 10

    # (Добавьте другие параметры, если необходимо)

    # Получаем имя API-метода
    api_name = request.getapiname()
    print(api_name)  # Выведет: aliexpress.affiliate.hotproduct.download

    # Далее можно использовать объект request для выполнения запроса к API AliExpress.
    # (Обратите внимание, что в примере отсутствует выполнение самого запроса).