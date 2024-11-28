Как использовать модуль endpoints
========================================================================================

Описание
-------------------------
Модуль `endpoints` предоставляет API-конечные точки для взаимодействия с различными внешними сервисами (PrestaShop, рекламные платформы, Emil, Hypo69, Kazarinov).  Каждая поддиректория (например, `prestashop`, `advertisement`) содержит API для конкретного сервиса.  Модуль структурирован для удобства интеграции и расширения.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**  Убедитесь, что все необходимые библиотеки установлены. Используйте команду `pip install -r requirements.txt`.

2. **Импорт нужного модуля:**  Импортируйте API-класс из нужной поддиректории. Например, для работы с PrestaShop:

   .. code-block:: python

       from src.endpoints.prestashop import PrestashopAPI

3. **Инициализация API-объекта:** Создайте экземпляр класса API, передавая необходимые параметры (например, логин, пароль, URL).

   .. code-block:: python

       # Пример (конкретные параметры зависят от API)
       api = PrestashopAPI(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET", base_url="YOUR_BASE_URL")

4. **Вызов методов API:**  Используйте методы API для взаимодействия с внешним сервисом.  Документация к конкретному API-модулю (например, `prestashop`) должна содержать список доступных методов и их параметры.

   .. code-block:: python

       # Пример (конкретные методы зависят от API)
       products = api.get_products()
       order = api.create_order(customer_id=123, product_id=456)


Пример использования
-------------------------
.. code-block:: python

    from src.endpoints.prestashop import PrestashopAPI

    # Замените на ваши данные
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"
    base_url = "YOUR_BASE_URL"

    try:
        api = PrestashopAPI(api_key, api_secret, base_url)
        products = api.get_products()
        for product in products:
            print(product['name'])
    except Exception as e:
        print(f"Ошибка: {e}")