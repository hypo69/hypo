Как использовать функцию get_translations_from_presta_translations_table
=====================================================================

Описание
-------------------------
Функция `get_translations_from_presta_translations_table` извлекает данные о переводах для определенного товара из таблицы переводов PrestaShop.  Она принимает референс товара и локаль (язык), и возвращает список словарей с переводами для указанных полей товара.

Шаги выполнения
-------------------------
1. **Получение референса товара и локали:** Функция принимает в качестве аргументов строку `product_reference`, представляющую собой уникальный идентификатор товара, и строку `i18n` - код языка (например, `en_EN`, `ru-RU`).

2. **Создание фильтра поиска:** Создается словарь `search_filter` для поиска в базе данных.  Ключ этого словаря - `product_reference`, а значение - полученный `product_reference`.

3. **Выполнение запроса к базе данных:**  Функция `translations_manager.select_record(**search_filter)` выполняет запрос к базе данных, используя предоставленный `search_filter`.  Это предполагает наличие менеджера базы данных (`ProductTranslationsManager`), который отвечает за взаимодействие с таблицей переводов.

4. **Возвращение результатов:** Функция возвращает список словарей `product_translations`, содержащих данные о переводах.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.translators.product_translator import get_translations_from_presta_translations_table

    # Предполагается, что у вас есть объект ProductTranslationsManager (например, полученный через connect_db_and_create_manager)
    # и credentials - данные для подключения к базе данных.

    product_reference = "12345"
    i18n = "ru_RU"

    translations = get_translations_from_presta_translations_table(product_reference, i18n)

    # Далее можно обработать полученные переводы, например, вывести их на экран:
    if translations:
        for translation in translations:
            print(translation)
    else:
        print(f"Нет переводов для товара с референсом {product_reference} на языке {i18n}")