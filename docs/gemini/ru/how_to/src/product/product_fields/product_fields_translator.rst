Как использовать функцию translate_presta_fields_dict
========================================================================================

Описание
-------------------------
Функция `translate_presta_fields_dict` переводит мультиязычные поля товара, содержащиеся в словаре `presta_fields_dict`, в соответствии со схемой языков клиента `client_langs_schema`.  Она обновляет атрибут `id` для языковых полей, используя идентификаторы из `client_langs_schema`  соответствующий языку страницы `page_lang`. Если перевод не найден, функция добавляет новый перевод в базу данных.

Шаги выполнения
-------------------------
1. **Переупорядочивает языковые ключи.** Функция вызывает `rearrange_language_keys` для предварительной обработки словаря `presta_fields_dict`. Это подготавливает данные для последующего перевода.
2. **Получает переводы из базы данных.** Функция ищет существующие переводы для товара, используя `get_translations_from_presta_translations_table` с идентификатором товара из поля `reference` в `presta_fields_dict`.
3. **Обрабатывает отсутствие переводов.** Если переводы не найдены или база данных пуста, функция создает новый перевод с помощью `insert_new_translation_to_presta_translations_table`. Она создает запись, используя поля из входного словаря `presta_fields_dict`.
4. **Циклически проходит по схеме языков клиента.** Функция итерирует по списку `client_langs_schema`.
5. **Находит переводы в базе данных.** Внутри цикла, она итерирует по списку `enabled_product_translations`.
6. **Проверяет соответствие языков.**  Если `iso_code` языка из `client_langs_schema` содержится в `locale` перевода из базы данных, функция обновляет значение поля в `presta_fields_dict`.  Ключ поля берется из входного словаря.  Значение поля устанавливается в словарь с языком и id в соответствии со схемой.
7. **Обработка ошибок.** Если возникает ошибка при обработке перевода, функция записывает сообщение об ошибке в лог с помощью `logger.error`.
8. **Возвращает обновлённый словарь.** В результате функция возвращает словарь `presta_fields_dict` с обновлёнными переводами.


Пример использования
-------------------------
.. code-block:: python

    import json

    # Пример данных
    presta_fields_dict = {"reference": "12345", "name": {"language": [{"attrs": {"id": "2"}, "value": "Product Name"}]}, "description": {"language": [{"attrs": {"id": "2"}, "value": "Product Description"}]}}
    client_langs_schema = [{"id": 1, "locale": "en-US", "iso_code": "en"}, {"id": 2, "locale": "ru-RU", "iso_code": "ru"}]
    page_lang = "ru-RU"

    # Предположим, что get_translations_from_presta_translations_table и insert_new_translation_to_presta_translations_table определены в других частях кода
    # ... (определения функций) ...

    translated_dict = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)

    print(json.dumps(translated_dict, indent=2))