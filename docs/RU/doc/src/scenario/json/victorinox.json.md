# Документация для `hypotez/src/scenario/json/victorinox.json`

## Обзор

Этот файл содержит JSON-конфигурацию для сбора данных с сайта поставщика "ksp". Он определяет параметры для сканирования сайта, правила ценообразования, список сценариев и исключений.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание полей](#описание-полей)

## Структура JSON

```json
{
  "supplier": "ksp",
  "supplier_prefix": "ksp",
  "start_url": "https://www.ksp.co.il/",
  "price_rule": "+100",
  "num_items_4_flush": 300,
  "if_login": false,
  "collect_products_from_categorypage": false,
  "scenarios": [
      "ksp_categories_consoles_microsoft.json",
      "ksp_categories_wathces_apple.json"
  ],
  "excluded": [
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
  ],
  "last_runned_scenario": ""
}
```

## Описание полей

### `supplier`

**Описание**: Идентификатор поставщика.
**Тип**: `string`
**Значение**: `"ksp"`

### `supplier_prefix`

**Описание**: Префикс для идентификации товаров данного поставщика.
**Тип**: `string`
**Значение**: `"ksp"`

### `start_url`

**Описание**: URL начальной страницы сайта поставщика.
**Тип**: `string`
**Значение**: `"https://www.ksp.co.il/"`

### `price_rule`

**Описание**: Правило ценообразования, используемое для корректировки цен.
**Тип**: `string`
**Значение**: `"+100"` (означает увеличение цены на 100)

### `num_items_4_flush`

**Описание**: Количество товаров для сброса кэша.
**Тип**: `integer`
**Значение**: `300`

### `if_login`

**Описание**: Флаг, указывающий, требуется ли вход на сайт поставщика.
**Тип**: `boolean`
**Значение**: `false`

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, нужно ли собирать товары непосредственно со страниц категорий.
**Тип**: `boolean`
**Значение**: `false`

### `scenarios`

**Описание**: Массив JSON-файлов, содержащих сценарии для сканирования.
**Тип**: `array`
**Значение**:
```json
[
    "ksp_categories_consoles_microsoft.json",
    "ksp_categories_wathces_apple.json"
]
```

### `excluded`

**Описание**: Массив JSON-файлов, представляющих исключения для сканирования.
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

**Описание**: Содержит имя последнего запущенного сценария.
**Тип**: `string`
**Значение**: `""`