# Документация для `morlevi_categories_storage_toshiba.json`

## Обзор
Файл `morlevi_categories_storage_toshiba.json` содержит JSON-структуру, описывающую сценарии для различных категорий устройств хранения данных от производителя TOSHIBA. Каждый сценарий определяет параметры продукта, такие как бренд, имя, URL, активность, состояние и категории PrestaShop.

## Оглавление
1. [Структура файла](#Структура-файла)
2. [Описание сценариев](#Описание-сценариев)
    - [`internal_ssd_sata_3 120-128GB`](#internal_ssd_sata_3-120-128GB)
    - [`internal_ssd_sata_3 240-256GB`](#internal_ssd_sata_3-240-256GB)
    - [`internal_ssd_sata_3 480-525GB`](#internal_ssd_sata_3-480-525GB)
    - [`internal_ssd_sata_3 960GB-1TB`](#internal_ssd_sata_3-960GB-1TB)
    - [`internal_ssd_sata_3 2TB`](#internal_ssd_sata_3-2TB)
    - [`internal_ssd_sata_3 4TB`](#internal_ssd_sata_3-4TB)
    - [`internal_ssd_sata_3 8TB`](#internal_ssd_sata_3-8TB)
    - [`internal_ssd_msata 240-256GB`](#internal_ssd_msata-240-256GB)
    - [`internal_ssd_m2sata 240-256GB`](#internal_ssd_m2sata-240-256GB)
    - [`internal_ssd_m2sata 480-525GB`](#internal_ssd_m2sata-480-525GB)
    - [`internal_ssd_nvmi 240-256GB`](#internal_ssd_nvmi-240-256GB)
    - [`internal_ssd_nvmi 480-525GB`](#internal_ssd_nvmi-480-525GB)
    - [`internal_ssd_nvmi 960GB-1TB`](#internal_ssd_nvmi-960GB-1TB)
    - [`internal_ssd_nvmi 2TB`](#internal_ssd_nvmi-2TB)
    - [`internal_ssd_nvmi_gen4 240-256GB`](#internal_ssd_nvmi_gen4-240-256GB)
    - [`internal_ssd_nvmi_gen4 480-525GB`](#internal_ssd_nvmi_gen4-480-525GB)
    - [`internal_ssd_nvmi_gen4 960GB-1TB`](#internal_ssd_nvmi_gen4-960GB-1TB)
    - [`internal_ssd_nvmi_gen4 2TB`](#internal_ssd_nvmi_gen4-2TB)
    - [`external_ssd 500GB`](#external_ssd-500GB)
    - [`external_ssd 1TB`](#external_ssd-1TB)
    - [`external_ssd 2TB`](#external_ssd-2TB)
    - [`internal_hdd_35 1TB`](#internal_hdd_35-1TB)
    - [`internal_hdd_35 2TB`](#internal_hdd_35-2TB)
    - [`internal_hdd_35 3TB`](#internal_hdd_35-3TB)
    - [`internal_hdd_35 4TB`](#internal_hdd_35-4TB)
    - [`internal_hdd_35 6TB`](#internal_hdd_35-6TB)
    - [`internal_hdd_35 8TB`](#internal_hdd_35-8TB)
    - [`TOSHIBA internal_hdd_35 10TB`](#TOSHIBA-internal_hdd_35-10TB)
    - [`internal_hdd_35 18TB`](#internal_hdd_35-18TB)
    - [`internal_hdd_25 500GB`](#internal_hdd_25-500GB)
    - [`internal_hdd_25 1TB`](#internal_hdd_25-1TB)
    - [`external_hdd_25 1TB`](#external_hdd_25-1TB)
    - [`external_hdd_25 2TB`](#external_hdd_25-2TB)
    - [`external_hdd_25 4TB`](#external_hdd_25-4TB)
    - [`external_hdd_25 5TB`](#external_hdd_25-5TB)
    - [`external_hdd_35 4TB`](#external_hdd_35-4TB)
    - [`external_hdd_35 6TB`](#external_hdd_35-6TB)
    - [`external_hdd_35 8TB`](#external_hdd_35-8TB)
    - [`external_hdd_35 10TB`](#external_hdd_35-10TB)

## Структура файла

Файл представляет собой JSON-объект со следующим строением:
```json
{
  "scenarios": {
    "scenario_name_1": {
      "brand": "TOSHIBA",
      "name": "product_name_1",
      "url": "product_url_1",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": "category_ids_1"
    },
      "scenario_name_2": {
      "brand": "TOSHIBA",
      "name": "product_name_2",
      "url": "product_url_2",
      "checkbox": false,
      "active": true,
      "condition": "new",
       "presta_categories": "category_ids_2"
    },
    ...
  }
}
```

Где:
- `"scenarios"`: Объект, содержащий все сценарии.
- `"scenario_name"`: Ключ, представляющий собой уникальное имя сценария (например, `"internal_ssd_sata_3 120-128GB"`).
- `"brand"`: Строка, указывающая бренд продукта (всегда `"TOSHIBA"`).
- `"name"`: Строка, представляющая собой внутреннее имя продукта.
- `"url"`: Строка, содержащая URL-адрес продукта (заполнитель или URL).
- `"checkbox"`: Логическое значение, указывающее состояние чекбокса (всегда `false`).
- `"active"`: Логическое значение, указывающее, активен ли сценарий (всегда `true`).
- `"condition"`: Строка, указывающая состояние продукта (всегда `"new"`).
- `"presta_categories"`: Строка, содержащая идентификаторы категорий PrestaShop, разделенные запятыми.

## Описание сценариев

### `internal_ssd_sata_3 120-128GB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 120-128GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_sata_3_128`.
- `url` (str):  `---------------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,118,134`.

### `internal_ssd_sata_3 240-256GB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 240-256GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_sata_3_256`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,118,135`.

### `internal_ssd_sata_3 480-525GB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 480-525GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_sata_3_512`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,118,136`.

### `internal_ssd_sata_3 960GB-1TB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 960GB-1TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_sata_3_1tb`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,118,137`.

### `internal_ssd_sata_3 2TB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 2TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_sata_3_2tb`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,118,138`.

### `internal_ssd_sata_3 4TB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 4TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_sata_3_4tb`.
- `url` (str):  `------------------------TOSHIBA  internal_ssd_sata_3_4tb---------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,118,139`.

### `internal_ssd_sata_3 8TB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 8TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_sata_3_8tb`.
- `url` (str):  `------------------------TOSHIBA  internal_ssd_sata_3_8tb---------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,118,140`.

### `internal_ssd_msata 240-256GB`

**Описание**: Сценарий для внутренних SSD mSATA объемом 240-256GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_msata_240gb`.
- `url` (str):  `------------------------TOSHIBA  internal_ssd_msata_240gb---------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,163,164`.

### `internal_ssd_m2sata 240-256GB`

**Описание**: Сценарий для внутренних SSD M.2 SATA объемом 240-256GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_m2sata_256`.
- `url` (str):  `------------------------TOSHIBA  internal_ssd_m2sata_256---------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,149`.

### `internal_ssd_m2sata 480-525GB`

**Описание**: Сценарий для внутренних SSD M.2 SATA объемом 480-525GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_m2sata_256`.
- `url` (str):  `------------------------TOSHIBA internal_ssd_m2sata_256--------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,150`.

### `internal_ssd_nvmi 240-256GB`

**Описание**: Сценарий для внутренних SSD NVMe объемом 240-256GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_nvme_256`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,119,141`.

### `internal_ssd_nvmi 480-525GB`

**Описание**: Сценарий для внутренних SSD NVMe объемом 480-525GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_nvme_512`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,119,142`.

### `internal_ssd_nvmi 960GB-1TB`

**Описание**: Сценарий для внутренних SSD NVMe объемом 960GB-1TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_nvme_1tb`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,119,143`.

### `internal_ssd_nvmi 2TB`

**Описание**: Сценарий для внутренних SSD NVMe объемом 2TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_nvme_2tb`.
- `url` (str):  `-------------------------------TOSHIBA--internal_ssd_nvme_2tb--------------=`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,119,144`.

### `internal_ssd_nvmi_gen4 240-256GB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 объемом 240-256GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_nvmi_gen4_256`.
- `url` (str):  `------------------------TOSHIBA internal_ssd_nvmi_gen4_256---------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,120,141,165`.

### `internal_ssd_nvmi_gen4 480-525GB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 объемом 480-525GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_nvmi_gen4_512`.
- `url` (str):  `------------------------TOSHIBA internal_ssd_nvmi_gen4_512---------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,120,142,168`.

### `internal_ssd_nvmi_gen4 960GB-1TB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 объемом 960GB-1TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_nvmi_gen4_1tb`.
- `url` (str):  `-------------------------------------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,120,143,169`.

### `internal_ssd_nvmi_gen4 2TB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 объемом 2TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_nvmi_gen4_2tb`.
- `url` (str):  `------------------------TOSHIBA internal_ssd_nvmi_gen4_2tb--------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,120,144`.

### `external_ssd 500GB`

**Описание**: Сценарий для внешних SSD объемом 500GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_ssd_500GB`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,122,549`.

### `external_ssd 1TB`

**Описание**: Сценарий для внешних SSD объемом 1TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_ssd-1TB`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,122,550`.

### `external_ssd 2TB`

**Описание**: Сценарий для внешних SSD объемом 2TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_ssd_2TB`.
- `url` (str):  `--------------------------------------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,122,551`.

### `internal_hdd_35 1TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 1TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_hdd_35-1tb`.
- `url` (str):  `https://www.morlevi.co.il/Cat/49?p_315=35&p_177=839&sort=datafloat2%2Cprice&keyword=`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,123,177`.

### `internal_hdd_35 2TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 2TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_hdd_35-2tb`.
- `url` (str):  `https://www.morlevi.co.il/Cat/49?p_315=35&p_177=840&sort=datafloat2%2Cprice&keyword=`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,123,178`.

### `internal_hdd_35 3TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 3TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_hdd_35-3tb`.
- `url` (str):  `https://www.morlevi.co.il/Cat/49?p_315=35&p_177=841&sort=datafloat2%2Cprice&keyword=`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,123,179`.

### `internal_hdd_35 4TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 4TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_hdd_35-4tb`.
- `url` (str):  `https://www.morlevi.co.il/Cat/49?p_315=35&p_177=842&sort=datafloat2%2Cprice&keyword=`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,123,180`.

### `internal_hdd_35 6TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 6TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_hdd_35-6tb`.
- `url` (str):  `https://www.morlevi.co.il/Cat/49?p_315=35&p_177=843&sort=datafloat2%2Cprice&keyword=`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,123,181`.

### `internal_hdd_35 8TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 8TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_hdd_35-8tb`.
- `url` (str):  `https://www.morlevi.co.il/Cat/49?p_315=35&p_177=844&sort=datafloat2%2Cprice&keyword=`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,123,182`.

### `TOSHIBA internal_hdd_35 10TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 10TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_hdd_35-10tb`.
- `url` (str):  `----------------------------TOSHIBA internal_hdd_35 10TB--------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,123,183`.

### `internal_hdd_35 18TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 18TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_hdd_35-10tb`.
- `url` (str):  `----------------------------TOSHIBA internal_hdd_35 18TB--------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,123,552`.

### `internal_hdd_25 500GB`

**Описание**: Сценарий для внутренних HDD 2.5" объемом 500GB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_hdd_25_480`.
- `url` (str):  `----------------------------TOSHIBA internal_hdd_25 500GB --------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,124,166`.

### `internal_hdd_25 1TB`

**Описание**: Сценарий для внутренних HDD 2.5" объемом 1TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `internal_ssd_sata_3_1tb`.
- `url` (str):  `----------------------------TOSHIBA internal_hdd_25 1T --------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,124,167`.

### `external_hdd_25 1TB`

**Описание**: Сценарий для внешних HDD 2.5" объемом 1TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_hdd_25-1tb`.
- `url` (str):  `----------------------------TOSHIBA external_hdd_25 1t --------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,125,184`.

### `external_hdd_25 2TB`

**Описание**: Сценарий для внешних HDD 2.5" объемом 2TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_hdd_2tb`.
- `url` (str):  `----------------------------TOSHIBA external_hdd_25 2t --------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,125,185`.

### `external_hdd_25 4TB`

**Описание**: Сценарий для внешних HDD 2.5" объемом 4TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_hdd_25_4tb`.
 - `url` (str):  `----------------------------TOSHIBA external_hdd_25 4t --------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,125,186`.

### `external_hdd_25 5TB`

**Описание**: Сценарий для внешних HDD 2.5" объемом 5TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_hdd_25-5tb`.
- `url` (str):  `----------------------------TOSHIBA external_hdd_25 5t --------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,125,187`.

### `external_hdd_35 4TB`

**Описание**: Сценарий для внешних HDD 3.5" объемом 4TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_hdd_35-4tb`.
- `url` (str):  `------------------------TOSHIBA external_hdd_35--------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,126,184`.

### `external_hdd_35 6TB`

**Описание**: Сценарий для внешних HDD 3.5" объемом 6TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_hdd_35_6tb`.
- `url` (str):  `------------------------TOSHIBA external_hdd_35--------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,126,185`.

### `external_hdd_35 8TB`

**Описание**: Сценарий для внешних HDD 3.5" объемом 8TB от Toshiba.

**Параметры**:
- `brand` (str):  `TOSHIBA`.
- `name` (str):  `external_hdd_35_8tb`.
- `url` (str):  `------------------------TOSHIBA external_hdd_35--------------------------`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (str): `117,126,186