Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateOrderListRequest`, который наследуется от класса `RestApi`.  Этот класс предназначен для создания запросов к API AliExpress для получения списка заказов партнера.  Он инициализирует необходимые параметры для запроса и предоставляет метод для получения имени API-метода.

Шаги выполнения
-------------------------
1. **Импорт класса `RestApi`**: Код импортирует базовый класс `RestApi` из модуля `..base`.
2. **Определение класса `AliexpressAffiliateOrderListRequest`**:  Создается класс, который расширяет функциональность `RestApi`.
3. **Инициализация параметров**: Конструктор `__init__` класса устанавливает необходимые параметры для запроса:
    - `domain`: домен API (по умолчанию `api-sg.aliexpress.com`).
    - `port`: порт API (по умолчанию `80`).
    - `app_signature`: подпись приложения.
    - `end_time`: конечная дата.
    - `fields`: поля.
    - `locale_site`: локаль сайта.
    - `page_no`: номер страницы.
    - `page_size`: размер страницы.
    - `start_time`: начальная дата.
    - `status`: статус заказа.
4. **Получение имени API-метода**: Метод `getapiname` возвращает строку `aliexpress.affiliate.order.list`, которая идентифицирует нужный метод API.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateOrderListRequest import AliexpressAffiliateOrderListRequest

    # Создание экземпляра класса
    request = AliexpressAffiliateOrderListRequest()

    # Установка значений параметров
    request.app_signature = "ваш_ключ_приложения"
    request.start_time = "2023-10-26"
    request.end_time = "2023-10-27"
    request.page_no = 1
    request.page_size = 10

    # Вызов метода для получения имени API
    api_name = request.getapiname()
    print(f"Имя API: {api_name}")

    # Далее, вы должны использовать полученные данные (request)
    # для формирования и отправки запроса к API AliExpress
    # с помощью методов класса RestApi, который импортирован,
    # но не продемонстрирован в этом примере.