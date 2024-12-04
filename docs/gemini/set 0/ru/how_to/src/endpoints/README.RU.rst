Как использовать модуль конечных точек (endpoints)
=========================================================================================

Описание
-------------------------
Модуль `endpoints` предоставляет API для взаимодействия с различными сервисами (PrestaShop, рекламными платформами, Emil, Hypo69, Kazarinov и другими).  Каждая поддиректория (`prestashop`, `advertisement`, `emil`, `hypo69`, `kazarinov`) содержит API для взаимодействия с конкретным сервисом.

Шаги выполнения
-------------------------
1. **Установка зависимостей:** Убедитесь, что все необходимые библиотеки установлены. Для этого используйте команду:

   ```bash
   pip install -r requirements.txt
   ```

2. **Импорт необходимых модулей:** Импортируйте нужный модуль в свой код.  Например, для работы с PrestaShop:

   ```python
   from src.endpoints.prestashop import PrestashopAPI
   ```

3. **Инициализация API:** Создайте экземпляр класса API, соответствующего нужному сервису, передавая необходимые параметры (например, учетные данные).

   ```python
   # Пример инициализации API для PrestaShop
   api = PrestashopAPI(api_key='your_api_key', secret_key='your_secret_key')
   ```

4. **Вызов методов API:** Используйте методы API для выполнения операций, например, создание, чтение, обновление или удаление данных.  Обратитесь к документации конкретного модуля, чтобы узнать доступные методы и их параметры.

   ```python
   # Пример использования метода для получения списка товаров
   products = api.get_products()
   print(products)
   ```


Пример использования
-------------------------
.. code-block:: python

    from src.endpoints.prestashop import PrestashopAPI

    # Замените 'your_api_key' и 'your_secret_key' на ваши значения
    api = PrestashopAPI(api_key='your_api_key', secret_key='your_secret_key')

    try:
        # Получение списка всех товаров
        products = api.get_products()
        for product in products:
            print(product)

    except Exception as e:
        print(f"Ошибка: {e}")