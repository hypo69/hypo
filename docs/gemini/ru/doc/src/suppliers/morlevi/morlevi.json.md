# Документация для `morlevi.json`

## Оглавление
1. [Обзор](#обзор)
2. [Основные параметры](#основные-параметры)
3. [Сценарии](#сценарии)
4. [Исключения](#исключения)

## Обзор

Файл `morlevi.json` содержит конфигурацию для парсера поставщика "morlevi". Включает в себя основные параметры поставщика, список файлов сценариев, а также правила исключений для категорий товаров.

## Основные параметры

### `supplier`
**Описание**: Название поставщика.

**Тип**: `str`

**Значение**: "morlevi"

### `supplier_id`
**Описание**: Уникальный идентификатор поставщика.

**Тип**: `str`

**Значение**: "2784"

### `supplier_prefix`
**Описание**: Префикс для идентификации товаров поставщика.

**Тип**: `str`

**Значение**: "mlv"

### `start_url`
**Описание**: URL главной страницы сайта поставщика.

**Тип**: `str`

**Значение**: "https://www.morlevi.co.il/"

### `login_url`
**Описание**: URL страницы для входа на сайт поставщика (в данном случае совпадает с главной страницей).

**Тип**: `str`

**Значение**: "https://www.morlevi.co.il/"

### `price_rule`
**Описание**: Правило для расчета цены товара.

**Тип**: `str`

**Значение**: "*1.43"

### `collect_products_from_categorypage`
**Описание**: Указывает, нужно ли собирать товары со страниц категорий.

**Тип**: `bool`

**Значение**: `false`

## Сценарии

### `scenario_files`
**Описание**: Массив файлов сценариев, которые определяют категории товаров для сбора данных.

**Тип**: `list[str]`

**Значение**: 
```
[
    { "$ref": "morlevi_categories_cases_antec.json#" },
    "morlevi_categories_storage_samsung.json",
    "morlevi_categories_storage_kingston.json",
    "morlevi_categories_video.json",
    "morlevi_categories_monitors_samsung.json",
    "morlevi_categories_monitors_lenovo.json",
    "morlevi_categories_mb_gigabyte.json",
    "morlevi_categories_cases_coolermaster.json",
    "morlevi_categories_cases_corsair.json",
    "morlevi_categories_cases_generic.json",
    "morlevi_categories_headsets.json",
    "morlevi_categories_laptops_asus.json",
    "morlevi_categories_laptops_gigabyte.json",
    "morlevi_categories_laptops_dell.json",
    "morlevi_categories_laptops_hp.json",
    "morlevi_categories_laptops_lenovo.json",
    "morlevi_categories_memory.json",
    "morlevi_categories_cpu.json",
    "morlevi_categories_cases_antec.json"
]
```

### `last_runned_scenario`
**Описание**: Имя файла последнего выполненного сценария.

**Тип**: `str`

**Значение**: "morlevi_categories_mb_gigabyte.json"

## Исключения

### `excluded`
**Описание**: Массив правил исключения для категорий товаров, сгруппированных по типам товаров.

**Тип**: `list[list[str]]`

**Значение**:
```
[
    [],
    [
        "morlevi_categories_minipc_gigabyte.json",
        "morlevi_categories_minipc_intel.json"
    ],
    [
        "morlevi_categories_video.json"
    ],
    [
        "morlevi_categories_memory_dimm_ddr4.json",
        "morlevi_categories_memory_sodimm_ddr3.json",
        "morlevi_categories_memory_sodimm_ddr4.json"
    ],
    [
        "morlevi_categories_monitors_aoc.json",
        "morlevi_categories_monitors_dell.json",
        "morlevi_categories_monitors_lenovo.json",
        "morlevi_categories_monitors_philips.json",
        "morlevi_categories_monitors_mag.json"
    ],
    [
        "morlevi_categories_psu_antec.json",
        "morlevi_categories_psu_cooler_maser.json",
        "morlevi_categories_psu_gigabyte.json",
        "morlevi_categories_psu_corsair.json"
    ],
    [
        "morlevi_categories_sound.json"
    ],
    [
        "morlevi_categories_storage_crucial.json",
        "morlevi_categories_storage_gigabyte.json",
        "morlevi_categories_storage_intel.json",
        "morlevi_categories_storage_kingston.json",
        "morlevi_categories_storage_samsung.json",
        "morlevi_categories_storage_sandisk.json",
        "morlevi_categories_storage_toshiba.json",
        "morlevi_categories_storage_wd.json"
    ],
    [
        "morlevi_categories_ups.json"
    ],
    [
        "morlevi_categories_printers.json"
    ],
    [],
    [
        "morlevi_categories_cases_zalman.json"
    ],
    [
        "morlevi_categories_keyboards_coolermaster.json",
        "morlevi_categories_keyboards_genius.json",
        "morlevi_categories_keyboards_hp.json",
        "morlevi_categories_keyboards_logitech.json",
        "morlevi_categories_keyboards_microsoft.json"
    ],
    [
        "morlevi_categories_network.json"
    ],
    [
        "morlevi_categories_printers.json"
    ]
]
```