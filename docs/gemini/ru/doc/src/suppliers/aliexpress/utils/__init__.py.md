# Модуль `src.suppliers.aliexpress.utils`

## Обзор

Модуль `src.suppliers.aliexpress.utils` содержит набор утилит, используемых для работы с данными AliExpress. Включает функции для извлечения идентификаторов продуктов, обеспечения использования HTTPS и работы с локалями.

## Оглавление

- [Функции](#функции)
    - [`extract_prod_ids`](#extract_prod_ids)
    - [`ensure_https`](#ensure_https)
- [Переменные](#переменные)
    - [`locales`](#locales)

## Функции

### `extract_prod_ids`

**Описание**: Функция для извлечения идентификаторов продуктов из строк.

**Параметры**:
- Отсутствуют явные параметры.  Описание параметров и возвращаемого значения находится в `hypotez/src/suppliers/aliexpress/utils/extract_product_id.py`

**Возвращает**:
- Описание возвращаемого значения находится в `hypotez/src/suppliers/aliexpress/utils/extract_product_id.py`

### `ensure_https`

**Описание**: Функция для преобразования URL-адресов в HTTPS.

**Параметры**:
- Отсутствуют явные параметры.  Описание параметров и возвращаемого значения находится в `hypotez/src/suppliers/aliexpress/utils/ensure_https.py`

**Возвращает**:
- Описание возвращаемого значения находится в `hypotez/src/suppliers/aliexpress/utils/ensure_https.py`

## Переменные

### `locales`

**Описание**: Словарь, содержащий локали.

**Тип**: `dict`

**Пример**:
```python
{
    "ru": "ru_RU",
    "en": "en_US",
    "es": "es_ES",
    "fr": "fr_FR",
    "pt": "pt_PT",
    "de": "de_DE",
    "it": "it_IT",
    "nl": "nl_NL",
    "pl": "pl_PL",
    "tr": "tr_TR",
    "ja": "ja_JP",
    "ko": "ko_KR",
    "th": "th_TH",
    "vi": "vi_VN",
    "ar": "ar_AE",
    "he": "he_IL",
    "id": "id_ID",
    "uk": "uk_UA"
}
```