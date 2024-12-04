Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот модуль определяет иерархию пользовательских исключений, используемых при работе с API AliExpress.  Каждый класс исключения наследуется от базового класса `AliexpressException` и предоставляет специфическое сообщение об ошибке. Это позволяет обрабатывать различные типы ошибок API AliExpress более целенаправленно.

Шаги выполнения
-------------------------
1. **Определение исключений:** Модуль создает классы исключений:
    - `AliexpressException`: Базовый класс для всех исключений API AliExpress. Принимает строковое значение `reason` для описания ошибки.
    - `InvalidArgumentException`: Исключение для некорректных аргументов.
    - `ProductIdNotFoundException`: Исключение для случая, когда ID продукта не найден.
    - `ApiRequestException`: Исключение для ошибок запроса к API.
    - `ApiRequestResponseException`: Исключение для случаев, когда ответ API невалиден.
    - `ProductsNotFoudException`: Исключение, когда не найдено ни одного продукта.
    - `CategoriesNotFoudException`: Исключение, когда не найдено ни одной категории.
    - `InvalidTrackingIdException`: Исключение, когда идентификатор отслеживания некорректный или отсутствует.

2. **Инициализация исключений:**  При создании экземпляра исключения (например, `InvalidArgumentException`), необходимо передать описание ошибки в виде строки в конструктор `__init__`.

3. **Обработка исключений:** При возникновении исключения в коде, использующем API AliExpress, необходимо использовать `try...except` блоки для перехвата и обработки конкретных типов исключений.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.errors.exceptions import (
        AliexpressException,
        InvalidArgumentException,
        ProductIdNotFoundException,
    )

    try:
        # Ваш код, который может вызвать исключение
        result = get_product_by_id(123)  # Примерный метод
    except InvalidArgumentException as e:
        print(f"Ошибка: Неверные аргументы. Причина: {e.reason}")
    except ProductIdNotFoundException as e:
        print(f"Ошибка: Продукт с ID {e.reason} не найден")
    except AliexpressException as e:
        print(f"Произошла общая ошибка AliExpress API: {e.reason}")
    else:
        print(f"Результат: {result}")

    #Пример создания исключения
    raise InvalidArgumentException("Некорректный тип данных")