Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AliexpressAffiliateLinkGenerateRequest`, который представляет собой запрос к API AliExpress для генерации аффилиатной ссылки.  Класс наследуется от базового класса `RestApi` и предоставляет методы для инициализации запроса, установки параметров и получения имени API-метода.

Шаги выполнения
-------------------------
1. **Инициализация:**  Класс `AliexpressAffiliateLinkGenerateRequest` инициализируется с помощью конструктора `__init__`.  При инициализации указывается домен (`domain`) и порт (`port`) API AliExpress.  В конструкторе также инициализируются атрибуты `app_signature`, `promotion_link_type`, `source_values`, и `tracking_id`, которые будут содержать параметры для запроса.

2. **Установка параметров:**  Атрибуты класса, такие как `app_signature`, `promotion_link_type`, `source_values` и `tracking_id`,  должны быть заполнены с конкретными значениями перед использованием запроса.  Эти параметры определяют особенности создаваемой аффилиатной ссылки.

3. **Получение имени API-метода:** Метод `getapiname()` возвращает строку 'aliexpress.affiliate.link.generate', которая идентифицирует конкретный метод API AliExpress, который нужно вызвать для генерации ссылки.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api import AliexpressAffiliateLinkGenerateRequest

    # Создаем экземпляр класса
    request = AliexpressAffiliateLinkGenerateRequest()

    # Задаем значения параметров
    request.app_signature = "ваш_ключ_приложения"
    request.promotion_link_type = "type1"
    request.source_values = {"param1": "value1", "param2": "value2"}
    request.tracking_id = 12345

    # Получаем имя API-метода
    api_name = request.getapiname()
    print(f"API метод: {api_name}")


    # Дальнейшие действия (например, отправка запроса к API с помощью метода базового класса):
    # Например, у RestApi должен быть метод send(), который отправляет запрос и обрабатывает ответ.
    # ... (ваш код для отправки запроса) ...