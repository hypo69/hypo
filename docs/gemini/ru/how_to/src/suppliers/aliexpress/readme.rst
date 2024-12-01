Как использовать класс Aliexpress
========================================================================================

Описание
-------------------------
Класс `Aliexpress` предназначен для интеграции функциональности работы с AliExpress, объединяя классы `Supplier`, `AliRequests` и `AliApi`.  Он позволяет взаимодействовать с AliExpress для парсинга и использования API, предоставляя удобный интерфейс.

Шаги выполнения
-------------------------
1. **Импортируйте класс `Aliexpress`:**
   ```python
   from src.suppliers.aliexpress import Aliexpress
   ```

2. **Инициализируйте объект класса `Aliexpress`:**
    Это создаёт экземпляр класса, настраивая параметры взаимодействия с AliExpress.
    ```python
    # Варианты инициализации:
    # Без вебдрайвера
    aliexpress_instance = Aliexpress()

    # Использование вебдрайвера Chrome
    aliexpress_instance = Aliexpress('chrome')

    # Использование вебдрайвера Mozilla
    aliexpress_instance = Aliexpress('mozilla')

    # Использование вебдрайвера Edge
    aliexpress_instance = Aliexpress('edge')

    # Использование системного вебдрайвера по умолчанию
    aliexpress_instance = Aliexpress('default')

    # Настройка языка и валюты (определяется по умолчанию как {'EN': 'USD'})
    aliexpress_instance = Aliexpress(locale={'RU': 'RUB'})


    # Передача дополнительных аргументов и ключевых параметров
    aliexpress_instance = Aliexpress(param1='value1', param2=2)
    ```

3. **Используйте методы класса `Aliexpress`:**
    После инициализации вы можете обращаться к методам, предоставляемым классом.  В примерах в документации показаны базовые способы использования, например, запуск без вебдрайвера или с использованием конкретного браузера.


Пример использования
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress import Aliexpress

    # Инициализация объекта класса Aliexpress с вебдрайвером Chrome
    aliexpress = Aliexpress('chrome')


    # (Здесь должен быть код, использующий методы класса Aliexpress, например, для парсинга данных или взаимодействия с API. Пример ниже демонстрирует, как можно получить доступ к методам.)
    # Предположим, что у класса Aliexpress есть метод get_product_details
    try:
        product_data = aliexpress.get_product_details("product_url")
        print(product_data)
    except Exception as e:
        print(f"Ошибка: {e}")


    # Закрытие вебдрайвера (важно!)
    aliexpress.quit_webdriver()  # Предполагается, что метод quit_webdriver() присутствует в классе