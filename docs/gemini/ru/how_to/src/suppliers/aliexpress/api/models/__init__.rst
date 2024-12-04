Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот модуль (`hypotez/src/suppliers/aliexpress/api/models/__init__.py`) содержит импорты, определяющие различные модели данных, связанные с API AliExpress. Он предоставляет доступ к классам, представляющим языки, валюты, параметры запроса для продуктов, ссылки на партнёрские программы, информацию о популярных продуктах, сами продукты и категории.

Шаги выполнения
-------------------------
1. Модуль импортирует классы из других файлов внутри папки `models`, например, `languages`, `currencies`, `request_parameters`, `affiliate_link`, `hotproducts`, `product`, `category`, и `ChildCategory`.
2. Импортированные классы представляют собой определения различных типов данных, необходимых для работы с API AliExpress.
3. Модуль экспортирует эти классы, делая их доступными для использования в других частях приложения.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models import Product, Language, Currency

    # Пример использования классов
    my_product = Product(id=123, title="Example Product", price=19.99, currency=Currency.USD)
    my_language = Language(code="en", name="English")

    print(my_product.title)
    print(my_language.name)