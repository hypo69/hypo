# AliexpressAffiliateOrderGetRequest.py

**Описание:**

Файл `AliexpressAffiliateOrderGetRequest.py` содержит класс `AliexpressAffiliateOrderGetRequest`, представляющий собой API-запрос для получения информации о заказах в программе аффилированного маркетинга AliExpress.  Класс наследуется от базового класса `RestApi`.

**Класс `AliexpressAffiliateOrderGetRequest`:**

* **`__init__(self, domain="api-sg.aliexpress.com", port=80)`:** Конструктор класса.
    * Инициализирует родительский класс `RestApi` с заданными `domain` и `port`.  По умолчанию используется `api-sg.aliexpress.com` и порт 80.
    * Инициализирует три атрибута:
        * `app_signature`: Предположительно, подпись приложения, необходимая для аутентификации.
        * `fields`: Возможно, содержит набор полей, которые нужно получить для каждого заказа.
        * `order_ids`: Список идентификаторов заказов, для которых требуется получить информацию.

* **`getapiname(self)`:** Метод, возвращающий имя API-метода.  Возвращает строку `'aliexpress.affiliate.order.get'`.  Это имя используется для вызова соответствующего API-метода на стороне сервера.


**Использование:**

Для использования класса необходимо создать его экземпляр, задать значения для `app_signature`, `fields` и `order_ids`, а затем вызвать соответствующие методы, предоставляемые базовым классом `RestApi` для выполнения запроса к API AliExpress.  Примера использования в коде нет.

**Выводы:**

Код представляет собой шаблон класса для взаимодействия с API AliExpress, необходимый для получения информации об аффилированных заказах.  Для его использования требуется заполнить атрибуты `app_signature`, `fields`, `order_ids`, и затем вызвать методы из базового класса `RestApi` для выполнения запроса к API.  Необходимо дополнить этот класс реализацией методов для заполнения параметров запроса и обработки ответа от API.