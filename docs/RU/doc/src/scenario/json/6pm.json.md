# Документация для `hypotez/src/scenario/json/6pm.json`

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [supplier](#supplier)
    - [supplier_prefix](#supplier_prefix)
    - [start_url](#start_url)
    - [price_rule](#price_rule)
    - [if_login](#if_login)
    - [collect_products_from_categorypage](#collect_products_from_categorypage)
    - [root_category](#root_category)
    - [scenario_files](#scenario_files)
    - [excluded](#excluded)
    - [last_runned_scenario](#last_runned_scenario)

## Обзор

Данный JSON-файл содержит конфигурацию для парсера сайта 6pm.com. Он определяет основные параметры, такие как URL сайта, правила ценообразования, список сценариев и исключения. Этот файл служит для настройки процесса сбора данных о товарах с сайта 6pm.

## Структура JSON

### `supplier`

**Описание**: Название поставщика.

**Тип**: `string`

**Значение**: `"6pm"`

### `supplier_prefix`

**Описание**: Префикс поставщика, используемый для формирования идентификаторов.

**Тип**: `string`

**Значение**: `"6pm"`

### `start_url`

**Описание**: Начальный URL сайта для парсинга.

**Тип**: `string`

**Значение**: `"https://www.6pm.com/"`

### `price_rule`

**Описание**: Правило расчета цены. `+0` означает, что цена будет браться напрямую с сайта без изменений.

**Тип**: `string`

**Значение**: `"+0"`

### `if_login`

**Описание**: Флаг, указывающий, нужно ли выполнять вход на сайт. В данном случае вход не требуется.

**Тип**: `boolean`

**Значение**: `false`

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, нужно ли собирать товары непосредственно со страниц категорий. В данном случае не нужно.

**Тип**: `boolean`

**Значение**: `false`

### `root_category`

**Описание**: Идентификатор корневой категории для сбора данных.

**Тип**: `integer`

**Значение**: `3`

### `scenario_files`

**Описание**: Список файлов сценариев для парсинга. 

**Тип**: `array`

**Значение**: 
```json
[
    ".json",
    "ksp_categories_wathces_apple.json"
  ]
```

### `excluded`

**Описание**: Список файлов сценариев, которые следует исключить из обработки. Этот список включает в себя различные категории товаров, такие как колонки, телефоны, наушники, планшеты, ноутбуки, часы и т.д.

**Тип**: `array`

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

**Описание**: Имя последнего запущенного сценария. В данном случае значение пустое.

**Тип**: `string`

**Значение**: `""`