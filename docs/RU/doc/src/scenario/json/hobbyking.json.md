# Конфигурация сценария для KSP

## Обзор

Этот JSON-файл содержит конфигурацию для сценариев сбора данных с сайта KSP. Он определяет основные параметры, такие как поставщик, начальный URL, правила ценообразования, а также список сценариев для запуска и исключенные сценарии.

## Содержание

- [Обзор](#обзор)
- [Основные параметры](#основные-параметры)
- [Сценарии](#сценарии)
- [Исключенные сценарии](#исключенные-сценарии)

## Основные параметры

### `supplier`

**Описание**: Идентификатор поставщика, в данном случае "ksp".

### `supplier_prefix`

**Описание**: Префикс поставщика, также "ksp".

### `start_url`

**Описание**: Начальный URL сайта KSP: `https://www.ksp.co.il/`.

### `price_rule`

**Описание**: Правило ценообразования, которое применяется к ценам товаров. В данном случае "+100".

### `num_items_4_flush`

**Описание**: Количество товаров для сброса данных, в данном случае 300.

### `if_login`

**Описание**: Флаг, указывающий, требуется ли вход в систему. В данном случае `false`.

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, нужно ли собирать продукты со страницы категории. В данном случае `false`.

## Сценарии

### `scenarios`

**Описание**: Список сценариев для выполнения.

- `ksp_categories_consoles_microsoft.json`: Сценарий для сбора данных о консолях Microsoft.
- `ksp_categories_wathces_apple.json`: Сценарий для сбора данных о часах Apple.

## Исключенные сценарии

### `excluded`

**Описание**: Список исключенных сценариев, которые не будут выполняться.

- `ksp_categories_speakers_google.json`: Исключенный сценарий для колонок Google.
- `ksp_categories_speakers_jbl.json`: Исключенный сценарий для колонок JBL.
- `ksp_categories_phones_philips.json`: Исключенный сценарий для телефонов Philips.
- `ksp_categories_phones_samsung.json`: Исключенный сценарий для телефонов Samsung.
- `ksp_categories_phones_google.json`: Исключенный сценарий для телефонов Google.
- `ksp_categories_phones_asus.json`: Исключенный сценарий для телефонов Asus.
- `ksp_categories_phones_nokia.json`: Исключенный сценарий для телефонов Nokia.
- `ksp_categories_phones_oppo.json`: Исключенный сценарий для телефонов Oppo.
- `ksp_categories_phones_oneplus.json`: Исключенный сценарий для телефонов OnePlus.
- `ksp_categories_phones_philips.json`: Исключенный сценарий для телефонов Philips.
- `ksp_categories_phones_xiaomi.json`: Исключенный сценарий для телефонов Xiaomi.
- `ksp_categories_headphones_bang_olufsen.json`: Исключенный сценарий для наушников Bang & Olufsen.
- `ksp_categories_headphones_hyperx.json`: Исключенный сценарий для наушников HyperX.
- `ksp_categories_headphones_jbl.json`: Исключенный сценарий для наушников JBL.
- `ksp_categories_headphones_razer.json`: Исключенный сценарий для наушников Razer.
- `ksp_categories_headphones_sony.json`: Исключенный сценарий для наушников Sony.
- `ksp_categories_headphones_xiaomi.json`: Исключенный сценарий для наушников Xiaomi.
- `ksp_categories_tablets_amazon.json`: Исключенный сценарий для планшетов Amazon.
- `ksp_categories_tablets_lenovo.json`: Исключенный сценарий для планшетов Lenovo.
- `ksp_categories_tablets_samsung.json`: Исключенный сценарий для планшетов Samsung.
- `ksp_categories_tablets_xiaomi.json`: Исключенный сценарий для планшетов Xiaomi.
- `ksp_categories_iphones.json`: Исключенный сценарий для iPhone.
- `ksp_categories_macbook.json`: Исключенный сценарий для MacBook.
- `ksp_categories_apple_wathces.json`: Исключенный сценарий для Apple Watch.
- `ksp_categories_ipods.json`: Исключенный сценарий для iPod.
- `ksp_categories_ipads.json`: Исключенный сценарий для iPad.
- `ksp_categories_imacs.json`: Исключенный сценарий для iMac.
- `ksp_categories_consoles_microsoft.json`: Исключенный сценарий для консолей Microsoft.
- `ksp_categories_consoles_nintendo.json`: Исключенный сценарий для консолей Nintendo.
- `ksp_categories_notebooks_asus_by_model.json`: Исключенный сценарий для ноутбуков Asus по моделям.
- `ksp_categories_notebooks_lenovo_by_model.json`: Исключенный сценарий для ноутбуков Lenovo по моделям.
- `ksp_categories_notebooks_hp_by_model.json`: Исключенный сценарий для ноутбуков HP по моделям.
- `ksp_categories_notebooks_dell_by_model.json`: Исключенный сценарий для ноутбуков Dell по моделям.
- `ksp_categories_notebooks_huawei_by_model.json`: Исключенный сценарий для ноутбуков Huawei по моделям.
- `ksp_categories_speakers_google.json`: Исключенный сценарий для колонок Google.
- `ksp_categories_speakers_jbl.json`: Исключенный сценарий для колонок JBL.
- `ksp_categories_watches_honor.json`: Исключенный сценарий для часов Honor.
- `ksp_categories_watches_lenovo.json`: Исключенный сценарий для часов Lenovo.
- `ksp_categories_watches_garmin.json`: Исключенный сценарий для часов Garmin.
- `ksp_categories_watches_samsung.json`: Исключенный сценарий для часов Samsung.
- `ksp_categories_watches_xiaomi.json`: Исключенный сценарий для часов Xiaomi.
- `ksp_categories_watches_amazfit.json`: Исключенный сценарий для часов Amazfit.
- `ksp_categories_streamers_google.json`: Исключенный сценарий для стримеров Google.
- `ksp_categories_monitors_samsung.json`: Исключенный сценарий для мониторов Samsung.
- `ksp_categories_monitors_lg.json`: Исключенный сценарий для мониторов LG.

### `last_runned_scenario`

**Описание**: Последний запущенный сценарий, в данном случае пустая строка.