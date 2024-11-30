Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит функции для работы с переводами полей товаров.  Функции позволяют получить переводы из таблицы переводов PrestaShop, вставить новые переводы и перевести поля товара с одного языка на другой.

Шаги выполнения
-------------------------
1. **Получение переводов из таблицы переводов PrestaShop:**
   Функция `get_translations_from_presta_translations_table` получает переводы полей товара из таблицы переводов PrestaShop.

   - Она принимает в качестве аргументов:
     - `product_reference`: Уникальный идентификатор товара.
     - `credentials`: Словарь с данными для подключения к базе данных переводов.
     - `i18n`: Код языка в формате `en_EN`, `he_HE`, `ru-RU`.  Если не указан, используется значение по умолчанию.
   - Функция использует менеджер `ProductTranslationsManager` для выполнения запроса к базе данных.
   - Фильтрует результаты, используя `search_filter` с `product_reference`.
   - Возвращает список словарей `product_translations` с переводами.

2. **Вставка нового перевода в таблицу переводов PrestaShop:**
   Функция `insert_new_translation_to_presta_translations_table` добавляет новую запись перевода в таблицу.

   - Принимает в качестве аргументов:
     - `record`: Словарь с данными нового перевода.
     - `credentials`: Словарь с данными для подключения к базе данных.
   - Использует менеджер `ProductTranslationsManager` для добавления записи.

3. **Перевод полей товара:**
   Функция `translate_record` переводит поля товара с одного языка на другой.

   - Принимает в качестве аргументов:
     - `record`: Словарь с данными товара для перевода.
     - `from_locale`: Код исходного языка.
     - `to_locale`: Код языка перевода.
   - Использует функцию `translate` из модуля `src.ai` для перевода.
   - Обрабатывает переведённые данные.
   - Возвращает словарь `translated_record` с переведёнными полями.


Пример использования
-------------------------
.. code-block:: python

    from src.translators import translate_product_fields

    # Предполагаемые данные
    product_reference = "PRODUCT123"
    credentials = {"host": "localhost", "user": "user", "password": "password"}
    i18n = "en_EN"
    
    # Получение переводов
    translations = translate_product_fields.get_translations_from_presta_translations_table(
        product_reference, credentials, i18n
    )
    print(f"Полученные переводы: {translations}")
    
    # Пример вставки (предполагается, что record содержит данные для вставки)
    new_record = {"product_reference": "PRODUCT456", "field1": "Value1", "field2": "Value2", "i18n": "fr_FR"}
    translate_product_fields.insert_new_translation_to_presta_translations_table(new_record, credentials)

    # Пример перевода (предполагается, что record содержит данные для перевода и от translate импортированно)
    record_to_translate = {"name": "Original Name", "description": "Original description", "i18n": "en_EN"}
    translated_record = translate_product_fields.translate_record(record_to_translate, "en_EN", "ru_RU")
    print(f"Переведенная запись: {translated_record}")