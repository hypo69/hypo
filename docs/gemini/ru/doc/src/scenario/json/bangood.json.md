# bangood.json

## Обзор

Данный файл содержит JSON-конфигурацию для парсинга данных с сайта Banggood. Он определяет параметры поставщика, начальный URL, правила ценообразования, и другие настройки для сбора информации о товарах.

## Оглавление

- [Описание](#описание)
- [Структура файла](#структура-файла)
  - [`supplier`](#supplier)
  - [`supplier_prefix`](#supplier_prefix)
  - [`start_url`](#start_url)
  - [`price_rule`](#price_rule)
  - [`num_items_4_flush`](#num_items_4_flush)
  - [`if_login`](#if_login)
  - [`parcing method [webdriver|api]`](#parcing-method-webdriverapi)
  - [`about method web scrapping [webdriver|api]`](#about-method-web-scrapping-webdriverapi)
  - [`collect_products_from_categorypage`](#collect_products_from_categorypage)
  - [`scenario_files`](#scenario_files)
  - [`excluded`](#excluded)
  - [`last_runned_scenario`](#last_runned_scenario)

## Описание

Этот файл конфигурации используется для настройки процесса сбора данных с веб-сайта Banggood. Он содержит информацию о поставщике, начальном URL для парсинга, правилах расчета цен, а также список исключенных категорий товаров и сценариев.

## Структура файла

### `supplier`

**Описание**: Идентификатор поставщика.

**Тип**: `str`

**Значение**: `"ksp"`

### `supplier_prefix`

**Описание**: Префикс поставщика.

**Тип**: `str`

**Значение**: `"ksp"`

### `start_url`

**Описание**: Начальный URL для парсинга.

**Тип**: `str`

**Значение**: `"https://www.banggood.com/search/rc-drones.html?last_spm=1a981.SearchResultPage.0001393399.00012138459.bc2a93ecdf3644b08e434b1e6b3f5d05"`

### `price_rule`

**Описание**: Правило для расчета цены.

**Тип**: `str`

**Значение**: `"+100"`

### `num_items_4_flush`

**Описание**: Количество товаров для сброса данных.

**Тип**: `int`

**Значение**: `300`

### `if_login`

**Описание**: Флаг, указывающий, требуется ли вход на сайт.

**Тип**: `bool`

**Значение**: `false`

### `parcing method [webdriver|api]`

**Описание**: Метод парсинга данных (webdriver или api).

**Тип**: `str`

**Значение**: `"web"`

### `about method web scrapping [webdriver|api]`

**Описание**: Информация о методе веб-скрепинга.

**Тип**: `str`

**Значение**: `"Если я работаю через API мне не нужен webdriver"`

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, нужно ли собирать товары со страницы категории.

**Тип**: `bool`

**Значение**: `false`

### `scenario_files`

**Описание**: Список файлов сценариев для парсинга.

**Тип**: `list`

**Значение**: 
```json
[
    "ksp_categories_consoles_microsoft.json",
    "ksp_categories_wathces_apple.json"
]
```

### `excluded`

**Описание**: Список исключенных категорий товаров.

**Тип**: `list`

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

**Тип**: `str`

**Значение**: `""`