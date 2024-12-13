# Документация для `bangood.json`

## Обзор

Файл `bangood.json` содержит конфигурационные данные для парсинга данных с сайта Banggood. Он определяет поставщика, префикс, начальный URL, правила ценообразования и другие параметры, необходимые для работы парсера. Файл также содержит списки сценариев и исключений для различных категорий товаров.

## Содержание

1. [Обзор](#обзор)
2. [Основные параметры](#основные-параметры)
3. [Сценарии и исключения](#сценарии-и-исключения)
4. [Дополнительные параметры](#дополнительные-параметры)
   

## Основные параметры

### `supplier`

**Описание**: Название поставщика.

**Тип данных**: `str`

**Значение**: `"ksp"`

### `supplier_prefix`

**Описание**: Префикс для поставщика.

**Тип данных**: `str`

**Значение**: `"ksp"`

### `start_url`

**Описание**: Начальный URL для парсинга.

**Тип данных**: `str`

**Значение**: `"https://www.banggood.com/search/rc-drones.html?last_spm=1a981.SearchResultPage.0001393399.00012138459.bc2a93ecdf3644b08e434b1e6b3f5d05"`

### `price_rule`

**Описание**: Правило ценообразования.

**Тип данных**: `str`

**Значение**: `"+100"`

### `num_items_4_flush`

**Описание**: Количество товаров для сброса.

**Тип данных**: `int`

**Значение**: `300`

### `if_login`

**Описание**: Флаг, указывающий, требуется ли вход в систему.

**Тип данных**: `bool`

**Значение**: `false`

## Сценарии и исключения

### `scenario_files`

**Описание**: Список файлов сценариев.

**Тип данных**: `list[str]`

**Значение**: 
```json
[
    "ksp_categories_consoles_microsoft.json",
    "ksp_categories_wathces_apple.json"
]
```

### `excluded`

**Описание**: Список исключенных файлов сценариев.

**Тип данных**: `list[str]`

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
## Дополнительные параметры

### `parcing method [webdriver|api]`
**Описание**: Метод парсинга.
**Тип данных**: `str`
**Значение**: `"web"`

### `about method web scrapping [webdriver|api]`
**Описание**: Описание метода веб-скраппинга.
**Тип данных**: `str`
**Значение**: `"Если я работаю через API мне не нужен webdriver"`
### `collect_products_from_categorypage`
**Описание**: Флаг для сбора продуктов со страниц категорий.
**Тип данных**: `bool`
**Значение**: `false`
### `last_runned_scenario`

**Описание**: Последний запущенный сценарий.

**Тип данных**: `str`

**Значение**: `""`