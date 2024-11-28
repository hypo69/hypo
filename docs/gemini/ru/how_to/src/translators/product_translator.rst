Как использовать функцию get_translations_from_presta_translations_table
==========================================================================================

Описание
-------------------------
Функция `get_translations_from_presta_translations_table` извлекает переводы полей товара из таблицы переводов Престашоп. Она принимает в качестве аргументов `product_reference` (идентификатор товара) и `i18n` (язык перевода).  Функция взаимодействует с базой данных, чтобы получить данные для перевода.

Шаги выполнения
-------------------------
1. Функция получает `product_reference` (идентификатор товара) и `i18n` (язык перевода).
2. Создаётся словарь `search_filter` с условием поиска по `product_reference`.
3. Используется менеджер базы данных `ProductTranslationsManager` для выбора записей, соответствующих условиям поиска.
4. Функция возвращает список (`list`) найденных переводов.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.translators.product_translator import get_translations_from_presta_translations_table

    # Идентификатор товара
    product_reference = "12345"

    # Язык перевода (например, en_EN)
    i18n = "en_EN"


    # Вызов функции для получения переводов
    translations = get_translations_from_presta_translations_table(product_reference, i18n)

    # Обработка результата (например, вывод в консоль)
    if translations:
        for translation in translations:
            print(translation)
    else:
        print(f"Нет переводов для товара с референсом {product_reference} на языке {i18n}.")