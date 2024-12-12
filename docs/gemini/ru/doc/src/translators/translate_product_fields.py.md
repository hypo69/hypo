# Модуль `translate_product_fields`

## Обзор

Модуль `translate_product_fields` предназначен для управления переводами полей товаров. Он обеспечивает взаимодействие между словарем полей товара, таблицей переводов и переводчиками. Основные функции модуля включают получение переводов из таблицы PrestaShop, вставку новых переводов и перевод записей с использованием AI.

## Оглавление

- [Функции](#Функции)
    - [`get_translations_from_presta_translations_table`](#get_translations_from_presta_translations_table)
    - [`insert_new_translation_to_presta_translations_table`](#insert_new_translation_to_presta_translations_table)
    - [`translate_record`](#translate_record)

## Функции

### `get_translations_from_presta_translations_table`

**Описание**: Функция получает переводы полей товара из таблицы переводов PrestaShop.

**Параметры**:
- `product_reference` (str): Референс товара.
- `credentials` (dict): Параметры подключения к базе данных PrestaShop.
- `i18n` (str, optional): Язык перевода в формате `en_EN`, `he_HE`, `ru-RU`. По умолчанию `None`.

**Возвращает**:
- `list`: Список словарей, представляющих переводы полей товара.

### `insert_new_translation_to_presta_translations_table`

**Описание**: Функция вставляет новую запись перевода в таблицу переводов PrestaShop.

**Параметры**:
- `record` (dict): Запись с данными для вставки в таблицу переводов.
- `credentials` (dict): Параметры подключения к базе данных PrestaShop.

**Возвращает**:
- `None`

### `translate_record`

**Описание**: Функция переводит поля товара с одного языка на другой.

**Параметры**:
- `record` (dict): Запись с данными для перевода.
- `from_locale` (str): Исходный язык.
- `to_locale` (str): Язык перевода.

**Возвращает**:
- `dict`: Словарь с переведенными полями товара.