Как использовать этот блок кода
=========================================================================================\n\nОписание
-------------------------
Этот файл (`hypotez/src/suppliers/aliexpress/utils/__init__.py`) импортирует функции из других модулей, относящихся к обработке данных для поставщика AliExpress.  Он определяет константу `MODE`, которая вероятно используется для выбора режимов работы.  Этот модуль предоставляет функции для извлечения идентификаторов продуктов, перенаправления на HTTPS-соединения и управления локализацией.


Шаги выполнения
-------------------------
1. Определяет константу `MODE` со значением 'dev'.
2. Импортирует функции `extract_prod_ids`, `ensure_https` и `locales` из модулей `extract_product_id`, `ensure_https` и `locales` соответственно, которые находятся в подпапке `utils`.  Это позволяет использовать эти функции в других частях проекта.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.utils import extract_prod_ids, ensure_https, locales

    # Пример использования extract_prod_ids
    product_data = { ... } # данные о продукте
    product_ids = extract_prod_ids(product_data)
    print(product_ids)

    # Пример использования ensure_https
    url = "http://example.com"
    secured_url = ensure_https(url)
    print(secured_url)

    # Пример использования locales
    language = 'en'
    translated_text = locales.get_locale(language, 'some_key')
    print(translated_text)