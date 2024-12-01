Как использовать метод retrieve_product_details
========================================================================================

Описание
-------------------------
Метод `retrieve_product_details` позволяет получить информацию о продуктах с AliExpress. Он использует API AliExpress для получения деталей о продуктах, заданных списком ID или ссылок.  Метод принимает ID/ссылки, опционально - список требуемых полей и код страны для фильтрации.  Возвращает список объектов `model_Product`, содержащих информацию о продуктах.  Обрабатывает ошибки, связанные с запросом к API и отсутствием продуктов.  Логирует предупреждения об отсутствии продуктов.

Шаги выполнения
-------------------------
1. **Инициализация объекта `AliexpressApi`**: Создайте объект класса `AliexpressApi`, передав ему ключ API, секретный ключ, язык, валюту и, опционально, идентификатор отслеживания.  Это необходимо для аутентификации и настройки запроса.
2. **Формирование списка идентификаторов продуктов**: Сформируйте список идентификаторов продуктов (`product_ids`), которые нужно получить.  Этот список может быть строкой или списком строк.
3. **Вызов метода `retrieve_product_details`**: Вызовите метод `retrieve_product_details` объекта `AliexpressApi`, передав ему сформированный список `product_ids`, опционально список полей (`fields`) и код страны (`country`).
4. **Обработка ответа**: Метод вернёт список объектов `model_Product`. Проверьте, что список не пуст. При пустом списке, обработка ошибки выполняется внутри метода.
5. **Обработка ошибок**: Обработайте возможные исключения (`ProductsNotFoudException`, `InvalidArgumentException`, `ApiRequestException`, `ApiRequestResponseException`), которые могут быть вызваны при запросе к API.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.api import AliexpressApi
    from hypotez.src.suppliers.aliexpress.api.models import model_Language, model_Currency, model_Product
    
    # Предполагая, что у вас есть необходимые переменные
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"
    language = model_Language.RU
    currency = model_Currency.RUB
    product_ids = ["12345", "67890"]

    try:
        aliexpress_api = AliexpressApi(api_key, api_secret, language, currency)
        products = aliexpress_api.retrieve_product_details(product_ids, fields=['title', 'price'], country='RU')
        if products:
            for product in products:
                print(f"Название: {product.title}, Цена: {product.price}")
        else:
            print("Нет данных о продуктах")
    except Exception as e:
        print(f"Произошла ошибка: {e}")