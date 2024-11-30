Как использовать функцию `get_translations_from_presta_translations_table`
===========================================================================

Описание
-------------------------
Функция `get_translations_from_presta_translations_table` извлекает данные о переводах товара из таблицы переводов PrestaShop. Она принимает референс товара и код языка и возвращает список найденных записей.

Шаги выполнения
-------------------------
1. **Принимает параметры:** Функция получает в качестве входных данных `product_reference` (идентификатор товара) и `i18n` (код языка в формате `en_EN`, `ru-RU`, `he_HE` и т.д.).

2. **Создает фильтр поиска:**  Используя объект `ProductTranslationsManager`, формируется словарь `search_filter` для поиска в таблице.  Этот словарь содержит условие поиска по `product_reference`.

3. **Выполняет запрос:**  Объект `translations_manager` выполняет запрос к базе данных, используя сформированный `search_filter`.

4. **Возвращает результат:** Функция возвращает список `product_translations` с результатами поиска. Этот список содержит все найденные записи, соответствующие заданному `product_reference`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.translators.product_translator import get_translations_from_presta_translations_table

    # Идентификатор товара
    product_reference = "12345"

    # Код языка (например, ru-RU)
    i18n = "ru-RU"

    # Вызов функции для получения переводов
    translations = get_translations_from_presta_translations_table(product_reference, i18n)

    # Обработка полученных переводов (например, печать)
    if translations:
        for translation in translations:
            print(translation)
    else:
        print("Переводы для данного товара не найдены.")