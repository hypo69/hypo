# Модуль translate_product_fields

## Обзор

Модуль `translate_product_fields` отвечает за управление переводами полей товаров. Он связывает словарь полей товара, таблицу переводов и переводчики.  Он предоставляет функции для получения переводов из таблицы переводов PrestaShop, вставки новых переводов и перевода записей.

## Функции

### `get_translations_from_presta_translations_table`

**Описание**: Функция извлекает переводы полей товара из таблицы переводов PrestaShop.

**Параметры**:
- `product_reference` (str): Уникальный идентификатор товара.
- `credentials` (dict): Словарь с данными для аутентификации и подключения к базе данных.
- `i18n` (str, optional): Код языка перевода (например, `en_EN`, `he_HE`, `ru-RU`). По умолчанию `None`.

**Возвращает**:
- `list`: Список словарей с результатами запроса к базе данных.  Список переводов.  Возвращает пустой список, если переводы не найдены или при ошибках.

**Вызывает исключения**:
- Возможные исключения, связанные с работой с базой данных (например, проблемы с подключением, запросом, обработкой данных).  Подробности следует уточнить в документации к `ProductTranslationsManager`.


### `insert_new_translation_to_presta_translations_table`

**Описание**: Функция добавляет новую запись перевода в таблицу переводов PrestaShop.

**Параметры**:
- `record` (dict): Словарь с данными для новой записи перевода.
- `credentials` (dict): Словарь с данными для аутентификации и подключения к базе данных.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- Возможные исключения, связанные с работой с базой данных (например, проблемы с подключением, запросом, обработкой данных).  Подробности следует уточнить в документации к `ProductTranslationsManager`.


### `translate_record`

**Описание**: Функция переводит поля товара из одного языка в другой.

**Параметры**:
- `record` (dict): Словарь с полями товара для перевода.
- `from_locale` (str): Код исходного языка.
- `to_locale` (str): Код целевого языка.

**Возвращает**:
- `dict`: Переведённый словарь с полями товара.  Возвращает `None`, если произошла ошибка при переводе.

**Вызывает исключения**:
- Возможные исключения, связанные с вызовом внешних сервисов (например, проблем с подключением, ошибками обработки текста,  ошибки вызова функции `translate`). Подробности следует уточнить в документации к `translate`.

## Заметки

- Модуль использует классы и функции из других модулей (например, `ProductTranslationsManager`, `translate`).
- Необходимо добавить подробную документацию к `ProductTranslationsManager` и `translate`.
- Требуется реализовать обработку `translated_record` внутри функции `translate_record`.
- В текущем коде отсутствуют проверки корректности входных данных и обработка ошибок. Необходимо добавить такие проверки.
- Рекомендуется использовать более описательные имена переменных (например, `product_id` вместо `product_reference`).
- Для лучшей читабельности, рекомендуется добавить комментарии в местах, где код может быть не очевиден.