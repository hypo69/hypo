# Документация для `ksp.json`

## Обзор

Файл `ksp.json` содержит конфигурацию для сбора данных о товарах с сайта KSP. Он определяет основные параметры, такие как ID поставщика, URL, правила ценообразования, а также список сценариев для парсинга категорий товаров. Также включает в себя список исключений, сценарии которые не должны запускаться.

## Оглавление

1. [Обзор](#обзор)
2. [Основные параметры](#основные-параметры)
3. [Сценарии парсинга](#сценарии-парсинга)
4. [Исключенные сценарии](#исключенные-сценарии)
5. [Последний запущенный сценарий](#последний-запущенный-сценарий)

## Основные параметры

### `supplier_id`
- **Описание**: Идентификатор поставщика.
- **Тип**: `str`
- **Значение**: `"2787"`

### `supplier`
- **Описание**: Название поставщика.
- **Тип**: `str`
- **Значение**: `"KSP"`

### `supplier_prefix`
- **Описание**: Префикс поставщика.
- **Тип**: `str`
- **Значение**: `"ksp"`

### `start_url`
- **Описание**: Начальный URL для парсинга.
- **Тип**: `str`
- **Значение**: `"https://www.ksp.co.il/"`

### `price_rule`
- **Описание**: Правило ценообразования.
- **Тип**: `str`
- **Значение**: `"+100"`

### `if_list`
- **Описание**: Условие работы со списком.
- **Тип**: `str`
- **Значение**: `"first"`

### `use_mouse`
- **Описание**: Использовать мышь при парсинге.
- **Тип**: `bool`
- **Значение**: `false`

### `mandatory`
- **Описание**: Является ли парсинг обязательным.
- **Тип**: `bool`
- **Значение**: `true`

### `num_items_4_flush`
- **Описание**: Количество элементов для сброса.
- **Тип**: `int`
- **Значение**: `300`

### `if_login`
- **Описание**: Требуется ли вход в систему.
- **Тип**: `bool`
- **Значение**: `false`

### `parcing method [webdriver|api]`
- **Описание**: Метод парсинга.
- **Тип**: `str`
- **Значение**: `"web"`

### `about method web scrapping [webdriver|api]`
- **Описание**: Описание метода веб-скрапинга.
- **Тип**: `str`
- **Значение**: `"Если я работаю через API мне не нужен webdriver"`

### `collect_products_from_categorypage`
- **Описание**: Собирать ли продукты со страницы категории.
- **Тип**: `bool`
- **Значение**: `false`

## Сценарии парсинга

### `scenario_files`
- **Описание**: Список файлов сценариев для парсинга.
- **Тип**: `list`
- **Значение**: 
```
[
    "ksp_categories_aio_lenovo.json",
    "ksp_categories_headphones_jbl.json",
    "ksp_categories_headphones_msi.json",
    "ksp_categories_headphones_razer.json",
    "ksp_categories_headphones_sony.json",
    "ksp_categories_headphones_xiaomi.json",
    "ksp_categories_monitors_lenovo.json",
    "ksp_categories_monitors_lg.json",
    "ksp_categories_monitors_samsung.json",
    "ksp_categories_motherboards_msi.json",
    "ksp_categories_phones_apple.json",
    "ksp_categories_phones_asus.json",
    "ksp_categories_phones_google.json",
    "ksp_categories_phones_nokia.json",
    "ksp_categories_phones_oneplus.json",
    "ksp_categories_phones_samsung.json",
    "ksp_categories_aio_imacs.json",
    "ksp_categories_consoles_microsoft.json",
    "ksp_categories_consoles_nintendo.json",
    "ksp_categories_headphones_bang_olufsen.json",
    "ksp_categories_headphones_hyperx.json",
    "ksp_categories_headphones_ipods.json",
    "ksp_categories_notebooks_hp_by_model.json",
    "ksp_categories_phones_oppo.json",
     "ksp_categories_notebooks_dell_by_model.json"
]
```

## Исключенные сценарии

### `excluded`
- **Описание**: Список исключенных файлов сценариев.
- **Тип**: `list`
- **Значение**: 
```
[
  "ksp_categories_phones_xiaomi.json",
  "ksp_categories_phones_oneplus.json",
  "ksp_categories_phones_philips.json",
  "ksp_categories_phones_samsung.json",
  "ksp_categories_phones_xiaomi.json",
  "ksp_categories_monitors_samsung.json",
  "ksp_categories_tablets_ipads.json",
  "ksp_categories_tablets_amazon.json",
  "ksp_categories_tablets_lenovo.json",
  "ksp_categories_tablets_samsung.json",
  "ksp_categories_tablets_xiaomi.json",
  "ksp_categories_streamers_google.json",
  "ksp_categories_motherboards_msi.json",
  "ksp_categories_speakers_google.json",
  "ksp_categories_speakers_jbl.json",
  "ksp_categories_phones_apple.json",
  "ksp_categories_phones_asus.json",
  "ksp_categories_phones_google.json",
  "ksp_categories_phones_nokia.json",
  "ksp_categories_phones_oneplus.json",
  "ksp_categories_phones_oppo.json",
  "ksp_categories_phones_philips.json",
  "ksp_categories_phones_samsung.json",
  "ksp_categories_phones_xiaomi.json",
  "ksp_categories_watches_honor.json",
  "ksp_categories_watches_lenovo.json",
  "ksp_categories_watches_garmin.json",
  "ksp_categories_watches_samsung.json",
  "ksp_categories_watches_xiaomi.json",
  "ksp_categories_watches_amazfit.json",
  "ksp_categories_wathces_apple.json",
  "ksp_categories_notebooks_macbook.json",
  "ksp_categories_notebooks_asus_by_model.json",
  "ksp_categories_notebooks_lenovo_by_model.json",
  "ksp_categories_notebooks_huawei_by_model.json",
  "ksp_categories_monitors_lg.json",
  "ksp_categories_monitors_lenovo.json",
  "ksp_categories_monitors_samsung.json",
  "ksp_categories_tablets_ipads.json",
  "ksp_categories_tablets_amazon.json",
  "ksp_categories_tablets_lenovo.json",
  "ksp_categories_tablets_samsung.json",
  "ksp_categories_tablets_xiaomi.json",
  "ksp_categories_streamers_google.json",
   "ksp_categories_aio_imacs.json.json",
    "ksp_categories_aio_lenovo.json.json",
  "ksp_categories_motherboards_msi.json",
  "ksp_categories_speakers_google.json",
  "ksp_categories_speakers_jbl.json",
  "ksp_categories_headphones_bang_olufsen.json",
  "ksp_categories_headphones_hyperx.json",
  "ksp_categories_headphones_ipods.json",
  "ksp_categories_headphones_jbl.json",
  "ksp_categories_headphones_msi.json",
  "ksp_categories_headphones_razer.json",
  "ksp_categories_headphones_sony.json",
  "ksp_categories_headphones_xiaomi.json",
  "ksp_categories_phones_apple.json",
  "ksp_categories_phones_asus.json",
  "ksp_categories_phones_google.json",
  "ksp_categories_phones_nokia.json",
  "ksp_categories_phones_oneplus.json",
  "ksp_categories_phones_oppo.json",
  "ksp_categories_phones_philips.json",
  "ksp_categories_phones_samsung.json",
  "ksp_categories_phones_xiaomi.json",
  "ksp_categories_watches_honor.json",
  "ksp_categories_watches_lenovo.json",
  "ksp_categories_watches_garmin.json",
  "ksp_categories_watches_samsung.json",
  "ksp_categories_watches_xiaomi.json",
  "ksp_categories_watches_amazfit.json",
  "ksp_categories_wathces_apple.json",
  "ksp_categories_consoles_microsoft.json",
  "ksp_categories_consoles_nintendo.json",
  "ksp_categories_notebooks_asus_by_model.json",
  "ksp_categories_notebooks_macbook.json",
  "ksp_categories_notebooks_asus_by_model.json",
  "ksp_categories_notebooks_lenovo_by_model.json",
  "ksp_categories_notebooks_hp_by_model.json",
  "ksp_categories_notebooks_dell_by_model.json",
  "ksp_categories_notebooks_huawei_by_model.json"
]
```

## Последний запущенный сценарий

### `last_runned_scenario`
- **Описание**: Последний запущенный файл сценария.
- **Тип**: `str`
- **Значение**: `"ksp_categories_phones_apple.json"`