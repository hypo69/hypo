Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит функции для работы с переводами полей товаров.  Он позволяет получать переводы из таблицы переводов PrestaShop, вставлять новые переводы и переводить поля товаров с помощью стороннего API (translate).  Код взаимодействует с базой данных через `ProductTranslationsManager`, а также с модулем перевода `translate`.

Шаги выполнения
-------------------------
1. **Получение переводов из таблицы PrestaShop:**
   Функция `get_translations_from_presta_translations_table` получает переводы полей товара по заданному `product_reference` из базы данных PrestaShop. Она принимает в качестве аргументов: `product_reference` (идентификатор товара), `credentials` (данные для авторизации в базе данных) и `i18n` (код языка перевода, например, `en_EN`).
   Функция использует `ProductTranslationsManager` для выполнения запроса к базе данных с заданным фильтром (`search_filter`) и возвращает полученные переводы (`product_translations`).

2. **Вставка нового перевода в таблицу PrestaShop:**
   Функция `insert_new_translation_to_presta_translations_table` вставляет новую запись перевода в таблицу PrestaShop. Она принимает в качестве аргументов: `record` (словарь с данными для новой записи) и `credentials` (данные для авторизации).  Функция использует `ProductTranslationsManager` для добавления записи в базу.

3. **Перевод поля товара:**
   Функция `translate_record` осуществляет перевод полей товара. Она принимает в качестве аргументов: `record` (словарь с полями товара для перевода), `from_locale` (язык исходного текста) и `to_locale` (язык целевого перевода). Функция использует модуль `translate` для перевода данных. Функция предполагает, что `translate` возвращает словарь с переведенными значениями, которые необходимо далее обработать.

Пример использования
-------------------------
.. code-block:: python

    from src.translators import translate_product_fields
    from src.endpoints.PrestaShop import PrestaShop

    # Пример данных
    product_reference = "12345"
    credentials = {
        "db_host": "localhost",
        "db_user": "user",
        "db_password": "password"
        # ... другие необходимые данные для подключения к базе
    }
    i18n = "ru_RU"

    # Получение переводов
    translations = translate_product_fields.get_translations_from_presta_translations_table(product_reference, credentials, i18n)
    print(f"Переводы: {translations}")

    # Пример вставки новой записи
    new_record = {"product_reference": "67890", "name": "Новый товар", "description": "Описание"}
    translate_product_fields.insert_new_translation_to_presta_translations_table(new_record, credentials)


    # Пример перевода
    record_to_translate = {"name": "Original Name", "description": "Original Description"}
    from_locale = "en_EN"
    to_locale = "fr_FR"
    translated_record = translate_product_fields.translate_record(record_to_translate, from_locale, to_locale)
    print(f"Переведенная запись: {translated_record}")