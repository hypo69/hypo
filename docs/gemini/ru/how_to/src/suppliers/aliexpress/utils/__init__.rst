Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот файл `hypotez/src/suppliers/aliexpress/utils/__init__.py` импортирует функции из модулей `extract_product_id`, `ensure_https` и `locales`, относящиеся к обработке данных для поставщика AliExpress.  Также он определяет константу `MODE` со значением 'dev'.

Шаги выполнения
-------------------------
1. Импортирует функцию `extract_prod_ids` из модуля `extract_product_id`. Эта функция, вероятно, отвечает за извлечение идентификаторов продуктов из данных AliExpress.
2. Импортирует функцию `ensure_https` из модуля `ensure_https`.  Эта функция, скорее всего, проверяет и преобразует ссылки,  делая их безопасными (HTTPS).
3. Импортирует переменную `locales` из модуля `locales`. Скорее всего, эта переменная содержит список или словарь доступных локалей (языков) для обработки данных AliExpress.
4. Определяет константу `MODE` со значением 'dev'. Это, вероятно, переменная, определяющая режим работы (например, 'dev' - режим разработки, 'prod' - режим производства).

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.utils import extract_prod_ids, ensure_https, locales

    # Пример использования extract_prod_ids
    product_data = '<html><body>...</body></html>' # Замените на реальные данные
    extracted_ids = extract_prod_ids(product_data)
    print(extracted_ids)

    # Пример использования ensure_https
    url = "http://example.com"
    secure_url = ensure_https(url)
    print(secure_url)

    # Пример использования locales
    available_locales = locales
    print(available_locales)

    # Пример использования MODE
    print(MODE)