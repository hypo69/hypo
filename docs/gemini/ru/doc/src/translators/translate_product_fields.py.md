# Модуль `translate_product_fields`

## Обзор

Модуль `translate_product_fields` предназначен для управления переводами полей товаров. Он обеспечивает связь между словарем полей товара, таблицей переводов и переводчиками.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
    - [`get_translations_from_presta_translations_table`](#get_translations_from_presta_translations_table)
    - [`insert_new_translation_to_presta_translations_table`](#insert_new_translation_to_presta_translations_table)
    - [`translate_record`](#translate_record)

## Функции

### `get_translations_from_presta_translations_table`

**Описание**:
Функция получает переводы полей товара из таблицы переводов PrestaShop.

**Параметры**:
- `product_reference` (str): Референс товара.
- `credentials` (dict): Параметры подключения к базе данных переводов PrestaShop.
- `i18n` (str, optional): Язык перевода в формате `en_EN`, `he_HE`, `ru-RU`. По умолчанию `None`.

**Возвращает**:
- `list`: Список словарей с переводами полей товара.

### `insert_new_translation_to_presta_translations_table`

**Описание**:
Функция добавляет новую запись перевода в таблицу переводов PrestaShop.

**Параметры**:
- `record` (dict): Словарь с данными для вставки в таблицу переводов.
- `credentials` (dict): Параметры подключения к базе данных переводов PrestaShop.

### `translate_record`

**Описание**:
Функция для перевода полей товара.

**Параметры**:
- `record` (dict): Словарь с полями товара для перевода.
- `from_locale` (str): Язык, с которого нужно перевести.
- `to_locale` (str): Язык, на который нужно перевести.

**Возвращает**:
- `dict`: Словарь с переведенными полями товара.