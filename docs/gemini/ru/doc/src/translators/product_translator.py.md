# Модуль `product_translator`

## Обзор

Модуль `product_translator` предназначен для управления переводами полей товаров. Он обеспечивает связь между словарем полей товара, таблицей переводов и переводчиками.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
    - [`get_translations_from_presta_translations_table`](#get_translations_from_presta_translations_table)
    - [`insert_new_translation_to_presta_translations_table`](#insert_new_translation_to_presta_translations_table)
    - [`translate_record`](#translate_record)

## Функции

### `get_translations_from_presta_translations_table`

**Описание**: Функция возвращает список переводов полей товара из таблицы переводов.

**Параметры**:
- `product_reference` (str): Референс товара.
- `i18n` (str, optional): Локаль. По умолчанию `None`.

**Возвращает**:
- `list`: Список переводов полей товара.

### `insert_new_translation_to_presta_translations_table`

**Описание**: Функция вставляет новую запись перевода в таблицу переводов.

**Параметры**:
- `record` (dict): Словарь с данными для вставки.

**Возвращает**:
- `None`: Функция ничего не возвращает.

### `translate_record`

**Описание**: Функция для перевода полей товара с одного языка на другой.

**Параметры**:
- `record` (dict): Словарь с данными о полях товара.
- `from_locale` (str): Локаль исходного языка.
- `to_locale` (str): Локаль целевого языка.

**Возвращает**:
- `dict`: Словарь с переведенными полями товара.