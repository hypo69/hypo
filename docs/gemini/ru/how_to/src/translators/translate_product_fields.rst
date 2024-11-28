Как использовать этот блок кода
========================================================================================

Описание
-------------------------
Этот код содержит функции для работы с переводами полей товаров.  Он взаимодействует с базой данных PrestaShop,  выполняя поиск, добавление и перевод записей о переводах.

Шаги выполнения
-------------------------
1. **`get_translations_from_presta_translations_table(product_reference, credentials, i18n)`:**
    - Принимает `product_reference` (идентификатор товара), `credentials` (данные для подключения к базе данных) и `i18n` (код языка перевода).
    - Создаёт объект `ProductTranslationsManager` для работы с базой данных, используя переданные `credentials`.
    - Устанавливает фильтр поиска `search_filter` для товара по `product_reference`.
    - Выполняет запрос `select_record` в базе данных с использованием `search_filter`.
    - Возвращает список `product_translations` (переводы) найденных в базе данных.

2. **`insert_new_translation_to_presta_translations_table(record, credentials)`:**
    - Принимает `record` (запись с данными для перевода) и `credentials` (данные для подключения).
    - Создаёт объект `ProductTranslationsManager` для работы с базой данных, используя переданные `credentials`.
    - Выполняет добавление записи в базу данных с помощью метода `insert_record`, используя переданный `record`.

3. **`translate_record(record: dict, from_locale: str, to_locale: str) -> dict`:**
    - Принимает `record` (запись для перевода), `from_locale` (исходный язык) и `to_locale` (целевой язык).
    - Использует функцию `translate` из модуля `src.ai` для перевода `record`.
    - Обрабатывает переведенную запись `translated_record` (дополнительно).
    - Возвращает переведенную запись `translated_record`.


Пример использования
-------------------------
.. code-block:: python

    import json
    from src.translators import translate_product_fields
    from src.endpoints.PrestaShop import PrestaShop

    # Пример данных
    product_reference = "product_123"
    credentials = {
        'host': 'your_host',
        'username': 'your_username',
        'password': 'your_password',
        # ... другие данные для подключения
    }
    i18n = "ru-RU"

    # Получаем переводы
    translations = translate_product_fields.get_translations_from_presta_translations_table(product_reference, credentials, i18n)

    if translations:
        print(f"Найденные переводы: {json.dumps(translations, indent=2)}")

    # Пример создания новой записи для перевода
    new_record = {
        'product_reference': 'new_product_456',
        'field1': 'value1',
        'field2': 'value2',
        'i18n': 'en-US'
    }
    translate_product_fields.insert_new_translation_to_presta_translations_table(new_record, credentials)


    # Пример перевода
    record_to_translate = {'text': 'This is a test'}
    from_locale = 'en-US'
    to_locale = 'ru-RU'
    translated_record = translate_product_fields.translate_record(record_to_translate, from_locale, to_locale)
    print(f"Переведенная запись: {translated_record}")