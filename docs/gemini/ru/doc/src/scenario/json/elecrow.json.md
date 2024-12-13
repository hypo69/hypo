# Документация для `hypotez/src/scenario/json/elecrow.json`

## Обзор

Данный файл представляет собой JSON-конфигурацию для парсера, предназначенного для сбора данных с веб-сайта `elecrow.com`. Он содержит настройки, такие как базовый URL, правила ценообразования, список исключенных файлов сценариев и другие параметры.

## Содержание (TOC)

- [Обзор](#обзор)
- [Основные параметры](#основные-параметры)
- [Списки файлов](#списки-файлов)
- [Исключенные файлы](#исключенные-файлы)

## Основные параметры

### `supplier`

**Описание**: Идентификатор поставщика.

**Значение**: `"elecrow"`

### `supplier_prefix`

**Описание**: Префикс поставщика.

**Значение**: `"elecrow"`

### `start_url`

**Описание**: Начальный URL для сканирования.

**Значение**: `"https://www.elecrow.com/"`

### `price_rule`

**Описание**: Правило для корректировки цены.

**Значение**: `"+0"`

### `if_login`

**Описание**: Флаг, указывающий, требуется ли вход в систему для сбора данных.

**Значение**: `false`

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, нужно ли собирать товары со страниц категорий.

**Значение**: `false`

### `root_category`

**Описание**: Идентификатор корневой категории.

**Значение**: `3`

## Списки файлов

### `scenario_files`

**Описание**: Список файлов сценариев, которые будут использоваться.

**Значение**:
```json
[
  ".json",
  "ksp_categories_wathces_apple.json"
]
```

## Исключенные файлы

### `excluded`

**Описание**: Список файлов сценариев, которые будут исключены из обработки.
**Значение**:
```json
[
  "ksp_categories_speakers_google.json",
  "ksp_categories_speakers_jbl.json",
  "ksp_categories_phones_philips.json",
  "ksp_categories_phones_samsung.json",
  "ksp_categories_phones_google.json",
  "ksp_categories_phones_asus.json",
  "ksp_categories_phones_nokia.json",
  "ksp_categories_phones_oppo.json",
  "ksp_categories_phones_oneplus.json",
  "ksp_categories_phones_philips.json",
  "ksp_categories_phones_xiaomi.json",
  "ksp_categories_headphones_bang_olufsen.json",
  "ksp_categories_headphones_hyperx.json",
  "ksp_categories_headphones_jbl.json",
  "ksp_categories_headphones_razer.json",
  "ksp_categories_headphones_sony.json",
  "ksp_categories_headphones_xiaomi.json",
  "ksp_categories_tablets_amazon.json",
  "ksp_categories_tablets_lenovo.json",
  "ksp_categories_tablets_samsung.json",
  "ksp_categories_tablets_xiaomi.json",
  "ksp_categories_iphones.json",
  "ksp_categories_macbook.json",
  "ksp_categories_apple_wathces.json",
  "ksp_categories_ipods.json",
  "ksp_categories_ipads.json",
  "ksp_categories_imacs.json",
  "ksp_categories_consoles_microsoft.json",
  "ksp_categories_consoles_nintendo.json",
  "ksp_categories_notebooks_asus_by_model.json",
  "ksp_categories_notebooks_lenovo_by_model.json",
  "ksp_categories_notebooks_hp_by_model.json",
  "ksp_categories_notebooks_dell_by_model.json",
  "ksp_categories_notebooks_huawei_by_model.json",
  "ksp_categories_speakers_google.json",
  "ksp_categories_speakers_jbl.json",
   "ksp_categories_watches_honor.json",
   "ksp_categories_watches_lenovo.json",
    "ksp_categories_watches_garmin.json",
    "ksp_categories_watches_samsung.json",
    "ksp_categories_watches_xiaomi.json",
    "ksp_categories_watches_amazfit.json",
    "ksp_categories_streamers_google.json",
    "ksp_categories_monitors_samsung.json",
   "ksp_categories_monitors_lg.json"
]
```

### `last_runned_scenario`

**Описание**: Последний запущенный сценарий.

**Значение**: `""`