# Документация для `ksp.json`

## Обзор

Файл `ksp.json` содержит конфигурационные данные для поставщика KSP. Он включает в себя информацию о поставщике, его URL-адресе, правилах ценообразования, списке файлов сценариев для парсинга и списке исключенных файлов.

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Параметры](#параметры)
4. [Сценарии](#сценарии)
5. [Исключения](#исключения)
6. [Последний запущенный сценарий](#последний-запущенный-сценарий)

## Структура файла

Файл представляет собой JSON-объект со следующими ключами:

- `supplier_id`: Идентификатор поставщика.
- `supplier`: Название поставщика.
- `supplier_prefix`: Префикс поставщика.
- `start_url`: Стартовый URL-адрес поставщика.
- `price_rule`: Правило ценообразования.
- `scenario_files`: Список файлов сценариев.
- `excluded`: Список исключенных файлов.
- `last_runned_scenario`: Последний запущенный файл сценария.

## Параметры

### `supplier_id`

**Описание**: Идентификатор поставщика KSP.

**Тип**: `str`

**Пример**: `"2787"`

### `supplier`

**Описание**: Название поставщика.

**Тип**: `str`

**Пример**: `"KSP"`

### `supplier_prefix`

**Описание**: Префикс поставщика, используемый в именах файлов и т.д.

**Тип**: `str`

**Пример**: `"ksp"`

### `start_url`

**Описание**: Стартовый URL-адрес веб-сайта поставщика.

**Тип**: `str`

**Пример**: `"https://www.ksp.co.il/"`

### `price_rule`

**Описание**: Правило ценообразования, применяемое к ценам поставщика.

**Тип**: `str`

**Пример**: `"+100"`

## Сценарии

### `scenario_files`

**Описание**: Список файлов сценариев JSON, используемых для парсинга данных с веб-сайта поставщика.

**Тип**: `list[str]`

**Пример**: 
```json
[
    "ksp_categories_aio_lenovo.json",
    "ksp_categories_headphones_jbl.json",
    "ksp_categories_headphones_msi.json",
    ...
]
```
## Исключения

### `excluded`
**Описание**: Список файлов сценариев JSON, которые должны быть исключены из обработки.

**Тип**: `list[str]`

**Пример**:
```json
[
    "ksp_categories_phones_xiaomi.json",
    "ksp_categories_phones_oneplus.json",
    "ksp_categories_phones_philips.json",
    ...
]
```
## Последний запущенный сценарий

### `last_runned_scenario`

**Описание**: Имя последнего запущенного файла сценария.

**Тип**: `str`

**Пример**: `"ksp_categories_phones_apple.json"`