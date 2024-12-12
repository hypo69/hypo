# Модуль `product_translator`

## Обзор

Модуль `product_translator` предназначен для управления переводами товаров. Он обеспечивает связь между словарем полей товара, таблицей переводов и переводчиками. Модуль позволяет получать, добавлять и переводить данные о товарах.

## Содержание

- [Функции](#Функции)
    - [`get_translations_from_presta_translations_table`](#get_translations_from_presta_translations_table)
    - [`insert_new_translation_to_presta_translations_table`](#insert_new_translation_to_presta_translations_table)
    - [`translate_record`](#translate_record)

## Функции

### `get_translations_from_presta_translations_table`

**Описание**: Функция возвращает список переводов полей товара из таблицы `product_translations`.

**Параметры**:
- `product_reference` (str): Артикул товара, для которого нужно получить переводы.
- `i18n` (str, optional): Локаль, для которой нужно получить переводы. По умолчанию `None`.

**Возвращает**:
- `list`: Список словарей с переводами, найденных в таблице.

### `insert_new_translation_to_presta_translations_table`

**Описание**: Функция для вставки новой записи перевода в таблицу `product_translations`.

**Параметры**:
- `record` (dict): Словарь с данными для вставки.

**Возвращает**:
- `None`

### `translate_record`

**Описание**: Функция для перевода полей товара.

**Параметры**:
- `record` (dict): Словарь с данными для перевода.
- `from_locale` (str): Исходная локаль.
- `to_locale` (str): Локаль, на которую нужно перевести.

**Возвращает**:
- `dict`: Словарь с переведенными данными.