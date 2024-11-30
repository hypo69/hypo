Как использовать функцию translate_presta_fields_dict
========================================================================================

Описание
-------------------------
Функция `translate_presta_fields_dict` переводит мультиязычные поля товара, представленные в словаре `presta_fields_dict`, в соответствии со схемой языков клиента `client_langs_schema`.  Она обновляет идентификаторы языков в словаре `presta_fields_dict` на соответствующие идентификаторы из схемы `client_langs_schema` используя язык страницы `page_lang`. Если перевода в базе данных нет, функция создает новый перевод.

Шаги выполнения
-------------------------
1. Функция сначала вызывает функцию `rearrange_language_keys`, которая обновляет идентификаторы языков в словаре `presta_fields_dict` в соответствии с языком страницы `page_lang` и схемой `client_langs_schema`.
2. Функция получает из базы данных переводы для товара, используя его `reference` в `get_translations_from_presta_translations_table`.
3. Если переводы не найдены или их недостаточно, функция создает новый перевод, используя класс `record` и функцию `insert_new_translation_to_presta_translations_table`.
4. Функция итерируется по схеме языков `client_langs_schema` и переводит поля товара, используя переводы из базы данных.
5. Для каждого перевода из базы данных, если код языка из схемы `client_langs_schema` совпадает с локалью перевода, поля `presta_fields_dict` обновляются соответствующим переводом и идентификатором языка из схемы `client_langs_schema`.
6. Возвращает обновлённый словарь `presta_fields_dict`.

Пример использования
-------------------------
.. code-block:: python

    import json

    # Пример данных
    client_langs_schema = [
        {'id': 1, 'iso_code': 'en', 'locale': 'en-US', 'language_code': 'en-us'},
        {'id': 2, 'iso_code': 'ru', 'locale': 'ru-RU', 'language_code': 'ru-ru'}
    ]

    presta_fields_dict = {
        'reference': '12345',
        'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]},
        'description': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Description'}]}
    }
    
    page_lang = 'en-US'

    # Использование функции
    translated_dict = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)

    # Вывод результата
    print(json.dumps(translated_dict, indent=4, ensure_ascii=False))
```
**Примечание:**  В примере использования предполагается, что функции `rearrange_language_keys`, `get_translations_from_presta_translations_table`, `insert_new_translation_to_presta_translations_table`, и класс `record`  определены в других частях кода.  Также,  важно учесть, что для корректной работы функция `translate_presta_fields_dict` требует наличия  входных параметров `presta_fields_dict`, `client_langs_schema`, и `page_lang`.  Обратите внимание на возможные исключения, обработанные в коде `try...except`, и на необходимость логгирования ошибок.