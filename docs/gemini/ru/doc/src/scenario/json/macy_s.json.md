# Документация для `macy_s.json`

## Обзор

Файл `macy_s.json` содержит конфигурационные данные для сбора данных о товарах с веб-сайта поставщика "ksp". Он определяет параметры для парсинга, включая URL, правила ценообразования, количество элементов для сброса, а также списки включаемых и исключаемых файлов сценариев.

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
  "parcing method [webdriver|api]": "web",
  "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
  "collect_products_from_categorypage": false,
  "scenario_files": [
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
- **Описание**: Название поставщика.
- **Тип**: `str`
- **Значение**: `"ksp"`

### `supplier_prefix`
- **Описание**: Префикс поставщика, используемый в других частях системы.
- **Тип**: `str`
- **Значение**: `"ksp"`

### `start_url`
- **Описание**: Начальный URL для сканирования товаров.
- **Тип**: `str`
- **Значение**: `"https://www.ksp.co.il/"`

### `price_rule`
- **Описание**: Правило для обработки цены товаров.
- **Тип**: `str`
- **Значение**: `"+100"`

### `num_items_4_flush`
- **Описание**: Количество товаров, после обработки которых производится сброс данных.
- **Тип**: `int`
- **Значение**: `300`

### `if_login`
- **Описание**: Флаг, указывающий, требуется ли вход в систему.
- **Тип**: `bool`
- **Значение**: `false`

### `parcing method [webdriver|api]`
- **Описание**: Метод парсинга, используемый для сбора данных.
- **Тип**: `str`
- **Значение**: `"web"`

### `about method web scrapping [webdriver|api]`
- **Описание**: Пояснение к выбранному методу парсинга.
- **Тип**: `str`
- **Значение**: `"Если я работаю через API мне не нужен webdriver"`

### `collect_products_from_categorypage`
- **Описание**: Флаг, указывающий, нужно ли собирать продукты со страниц категорий.
- **Тип**: `bool`
- **Значение**: `false`

### `scenario_files`
- **Описание**: Список файлов сценариев, которые нужно использовать.
- **Тип**: `list`
- **Значение**: 
  ```json
    [
    "ksp_categories_consoles_microsoft.json",
    "ksp_categories_wathces_apple.json"
    ]
   ```

### `excluded`
- **Описание**: Список файлов сценариев, которые нужно исключить из обработки.
- **Тип**: `list`
- **Значение**: Список исключенных файлов в формате `JSON`.

### `last_runned_scenario`
- **Описание**: Имя последнего запущенного сценария.
- **Тип**: `str`
- **Значение**: `""`