# morlevi.json

## Обзор

Файл `morlevi.json` содержит конфигурационные данные для парсера, работающего с сайтом поставщика "morlevi". Он определяет основные параметры работы парсера, такие как URL-адреса, правила ценообразования, список сценариев и исключения.

## Оглавление

- [Обзор](#обзор)
- [Основные параметры](#основные-параметры)
- [Сценарии](#сценарии)
- [Исключенные сценарии](#исключенные-сценарии)

## Основные параметры

### `supplier`

**Описание**: Имя поставщика.
**Значение**: `"morlevi"`

### `supplier_id`

**Описание**: ID поставщика.
**Значение**: `"2784"`

### `supplier_prefix`

**Описание**: Префикс поставщика.
**Значение**: `"mlv"`

### `start_url`

**Описание**: URL начальной страницы поставщика.
**Значение**: `"https://www.morlevi.co.il/"`

### `login_url`

**Описание**: URL страницы для авторизации.
**Значение**: `"https://www.morlevi.co.il/"`

### `price_rule`

**Описание**: Правило расчета цены.
**Значение**: `"*1.43"`

### `if_list`

**Описание**: Условие для списка.
**Значение**: `"first"`

### `use_mouse`

**Описание**: Флаг использования мыши.
**Значение**: `false`

### `mandatory`

**Описание**: Флаг обязательного использования.
**Значение**: `true`

### `collect_products_from_categorypage`

**Описание**: Флаг сбора товаров со страницы категории.
**Значение**: `false`

### `num_items_4_flush`

**Описание**: Количество элементов для сброса.
**Значение**: `500`

### `if_login`

**Описание**: Флаг необходимости авторизации.
**Значение**: `true`

### `parcing method [webdriver|api]`

**Описание**: Метод парсинга (webdriver или api).
**Значение**: `"web"`

### `about method web scrapping [webdriver|api]`

**Описание**: Описание метода веб-скрейпинга.
**Значение**: `"Если я работаю через API мне не нужен webdriver"`

## Сценарии

### `scenario_files`

**Описание**: Список файлов сценариев для парсинга.
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

**Описание**: Последний запущенный сценарий.
**Значение**: `"morlevi_categories_mb_gigabyte.json"`

## Исключенные сценарии

### `excluded`

**Описание**: Список исключенных сценариев, сгруппированных по категориям.

```
[
  [
  ],
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
  [
  ],
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