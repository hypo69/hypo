# Модуль `translate_product_fields`

## Обзор

Модуль `translate_product_fields` предназначен для управления переводами полей товара. Он обеспечивает связь между словарем полей товара, таблицей переводов и переводчиками.

## Оглавление

1.  [Функции](#Функции)
    *   [`get_translations_from_presta_translations_table`](#get_translations_from_presta_translations_table)
    *   [`insert_new_translation_to_presta_translations_table`](#insert_new_translation_to_presta_translations_table)
    *   [`translate_record`](#translate_record)

## Функции

### `get_translations_from_presta_translations_table`

**Описание**:
Функция получает переводы полей товара из таблицы переводов PrestaShop на основе артикула товара.

**Параметры**:
-   `product_reference` (str): Артикул товара, для которого требуется получить переводы.
-   `credentials` (dict): Словарь с параметрами подключения к базе данных PrestaShop.
-  `i18n` (str, optional): Язык перевода в формате en_EN, he_HE, ru-RU. По умолчанию `None`.

**Возвращает**:
- `list`: Список словарей, содержащих переводы полей товара.

### `insert_new_translation_to_presta_translations_table`

**Описание**:
Функция добавляет новую запись перевода в таблицу переводов PrestaShop.

**Параметры**:
-   `record` (dict): Словарь с данными для вставки в таблицу переводов.
-   `credentials` (dict): Словарь с параметрами подключения к базе данных PrestaShop.

**Возвращает**:
    - `None`

### `translate_record`

**Описание**:
Функция для перевода полей товара. Использует внешнюю функцию `translate` для выполнения перевода.

**Параметры**:
-   `record` (dict): Словарь с данными для перевода.
-   `from_locale` (str): Исходный язык перевода.
-   `to_locale` (str): Целевой язык перевода.

**Возвращает**:
-   `dict`: Словарь с переведенными данными.