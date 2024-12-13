# Документация для `morlevi_categories_storage_sandisk.json`

## Обзор

Этот файл содержит JSON-конфигурацию для сбора данных о категориях товаров Sandisk на сайте Morlevi. Он определяет различные сценарии для SSD (внутренних и внешних), HDD (внутренних и внешних) с разными объемами памяти и интерфейсами, а также связывает их с соответствующими категориями PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Сценарии](#сценарии)
    - [internal_ssd_sata_3 120-128GB](#internal_ssd_sata_3-120-128gb)
    - [internal_ssd_sata_3 240-256GB](#internal_ssd_sata_3-240-256gb)
    - [internal_ssd_sata_3 480-525GB](#internal_ssd_sata_3-480-525gb)
    - [internal_ssd_sata_3 960GB-1TB](#internal_ssd_sata_3-960gb-1tb)
    - [internal_ssd_sata_3 2TB](#internal_ssd_sata_3-2tb)
    - [internal_ssd_sata_3 4TB](#internal_ssd_sata_3-4tb)
    - [internal_ssd_sata_3 8TB](#internal_ssd_sata_3-8tb)
    - [internal_ssd_msata 240-256GB](#internal_ssd_msata-240-256gb)
    - [internal_ssd_m2sata 240-256GB](#internal_ssd_m2sata-240-256gb)
     - [internal_ssd_m2sata 480-525GB](#internal_ssd_m2sata-480-525gb)
    - [internal_ssd_nvmi 240-256GB](#internal_ssd_nvmi-240-256gb)
    - [internal_ssd_nvmi 480-525GB](#internal_ssd_nvmi-480-525gb)
    - [internal_ssd_nvmi 960GB-1TB](#internal_ssd_nvmi-960gb-1tb)
    - [internal_ssd_nvmi 2TB](#internal_ssd_nvmi-2tb)
    - [internal_ssd_nvmi_gen4 240-256GB](#internal_ssd_nvmi_gen4-240-256gb)
    - [internal_ssd_nvmi_gen4 480-525GB](#internal_ssd_nvmi_gen4-480-525gb)
    - [internal_ssd_nvmi_gen4 960GB-1TB](#internal_ssd_nvmi_gen4-960gb-1tb)
    - [internal_ssd_nvmi_gen4 2TB](#internal_ssd_nvmi_gen4-2tb)
    - [external_ssd 500GB](#external_ssd-500gb)
    - [external_ssd 1TB](#external_ssd-1tb)
    - [external_ssd 2TB](#external_ssd-2tb)
    - [internal_hdd_35 1TB](#internal_hdd_35-1tb)
    - [internal_hdd_35 2TB](#internal_hdd_35-2tb)
     - [internal_hdd_35 3TB](#internal_hdd_35-3tb)
      - [internal_hdd_35 4TB](#internal_hdd_35-4tb)
    - [internal_hdd_35 6TB](#internal_hdd_35-6tb)
    - [internal_hdd_35 8TB](#internal_hdd_35-8tb)
    - [internal_hdd_35 10TB](#internal_hdd_35-10tb)
     - [internal_hdd_25 500GB](#internal_hdd_25-500gb)
     - [internal_hdd_25 1TB](#internal_hdd_25-1tb)
    - [external_hdd_25 1TB](#external_hdd_25-1tb)
    - [external_hdd_25 2TB](#external_hdd_25-2tb)
    - [external_hdd_25 4TB](#external_hdd_25-4tb)
    - [external_hdd_25 5TB](#external_hdd_25-5tb)
    - [external_hdd_35 4TB](#external_hdd_35-4tb)
    - [external_hdd_35 6TB](#external_hdd_35-6tb)
    - [external_hdd_35 8TB](#external_hdd_35-8tb)
    - [external_hdd_35 10TB](#external_hdd_35-10tb)


## Структура JSON

Файл JSON содержит корневой объект с ключом `"scenarios"`, который содержит вложенные объекты. Каждый из этих вложенных объектов представляет собой сценарий для определенной категории товаров.

Каждый сценарий имеет следующие ключи:

- `"brand"` (str): Бренд товара.
- `"name"` (str): Внутреннее имя сценария.
- `"url"` (str): URL-адрес страницы категории на сайте Morlevi, с которой будут собираться данные. Если URL не задан явно, прописывается  `------------------------<описание>---------------------------`
- `"checkbox"` (bool):  Флаг, указывающий на то, нужно ли использовать чекбокс при сборе данных.
- `"active"` (bool): Флаг, указывающий на активность сценария.
-  `"condition"` (str):  Состояние товара  (new/used).
-  `"presta_categories"` (str):  Список категорий PrestaShop, к которым относится товар, разделенный запятыми.

## Сценарии

### `internal_ssd_sata_3 120-128GB`
**Описание**:  Сценарий для сбора данных о внутренних SSD накопителях SATA 3 с объемом памяти 120-128GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_sata_3_128"
- `"url"`: "https://www.morlevi.co.il/Cat/50?p_315=23&p_175=822&sort=datafloat2%2Cprice&keyword="
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,118,134"

### `internal_ssd_sata_3 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях SATA 3 с объемом памяти 240-256GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_sata_3_256"
- `"url"`: "https://www.morlevi.co.il/Cat/50?p_315=23&p_175=823&sort=datafloat2%2Cprice&keyword="
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,118,135"

### `internal_ssd_sata_3 480-525GB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях SATA 3 с объемом памяти 480-525GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_sata_3_512"
- `"url"`: "https://www.morlevi.co.il/Cat/50?p_315=23&p_175=826&sort=datafloat2%2Cprice&keyword="
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,118,136"

### `internal_ssd_sata_3 960GB-1TB`
**Описание**:  Сценарий для сбора данных о внутренних SSD накопителях SATA 3 с объемом памяти 960GB-1TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_sata_3_1tb"
- `"url"`: "------------------------SANDISK  internal_ssd_sata_3_1tb---------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,118,137"

### `internal_ssd_sata_3 2TB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях SATA 3 с объемом памяти 2TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_sata_3_2tb"
- `"url"`: "------------------------SANDISK  internal_ssd_sata_3_2tb--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,118,138"

### `internal_ssd_sata_3 4TB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях SATA 3 с объемом памяти 4TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_sata_3_4tb"
- `"url"`: "------------------------SANDISK  internal_ssd_sata_3_4tb---------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,118,139"

### `internal_ssd_sata_3 8TB`
**Описание**:  Сценарий для сбора данных о внутренних SSD накопителях SATA 3 с объемом памяти 8TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_sata_3_8tb"
- `"url"`: "------------------------SANDISK  internal_ssd_sata_3_8tb---------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,118,140"

### `internal_ssd_msata 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях mSATA с объемом памяти 240-256GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_msata_240gb"
- `"url"`: "------------------------SANDISK  internal_ssd_msata_240gb---------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,163,164"

### `internal_ssd_m2sata 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях M.2 SATA с объемом памяти 240-256GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_m2sata_256"
- `"url"`: "------------------------SANDISK  internal_ssd_m2sata_256---------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,149"

### `internal_ssd_m2sata 480-525GB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях M.2 SATA с объемом памяти 480-525GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_m2sata_256"
- `"url"`: "------------------------SANDISK internal_ssd_m2sata_256--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,150"

### `internal_ssd_nvmi 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях NVMe с объемом памяти 240-256GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_nvme_256"
- `"url"`: "https://www.morlevi.co.il/Cat/51?p_315=23&p_175=823&sort=datafloat2%2Cprice&keyword="
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,119,141"

### `internal_ssd_nvmi 480-525GB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях NVMe с объемом памяти 480-525GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_nvme_512"
- `"url"`: "https://www.morlevi.co.il/Cat/51?p_315=23&p_175=826&sort=datafloat2%2Cprice&keyword="
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,119,142"

### `internal_ssd_nvmi 960GB-1TB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях NVMe с объемом памяти 960GB-1TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_nvme_1tb"
- `"url"`: "https://www.morlevi.co.il/Cat/51?p_315=23&p_175=829&sort=datafloat2%2Cprice&keyword="
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,119,143"

### `internal_ssd_nvmi 2TB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях NVMe с объемом памяти 2TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_nvme_2tb"
- `"url"`: "------------------------SANDISK internal_ssd_nvme_2tb---------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,119,144"

### `internal_ssd_nvmi_gen4 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях NVMe Gen4 с объемом памяти 240-256GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_nvmi_gen4_256"
- `"url"`: "------------------------SANDISK internal_ssd_nvmi_gen4_256---------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,120,141,165"

### `internal_ssd_nvmi_gen4 480-525GB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях NVMe Gen4 с объемом памяти 480-525GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_nvmi_gen4_512"
- `"url"`: "------------------------SANDISK internal_ssd_nvmi_gen4_512---------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,120,142,168"

### `internal_ssd_nvmi_gen4 960GB-1TB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях NVMe Gen4 с объемом памяти 960GB-1TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_nvmi_gen4_1tb"
- `"url"`: "------------------------SANDISK internal_ssd_nvmi_gen4_1tb--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,120,143,169"

### `internal_ssd_nvmi_gen4 2TB`
**Описание**: Сценарий для сбора данных о внутренних SSD накопителях NVMe Gen4 с объемом памяти 2TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_nvmi_gen4_2tb"
- `"url"`: "------------------------SANDISK internal_ssd_nvmi_gen4_2tb--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,120,144"

### `external_ssd 500GB`
**Описание**: Сценарий для сбора данных о внешних SSD накопителях с объемом памяти 500GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_ssd_500GB"
- `"url"`: "------------------------SANDISK external_ssd 500GB--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,122,549"

### `external_ssd 1TB`
**Описание**: Сценарий для сбора данных о внешних SSD накопителях с объемом памяти 1TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_ssd-1TB"
- `"url"`: "------------------------SANDISK external_ssd 1TB--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,122,550"

### `external_ssd 2TB`
**Описание**: Сценарий для сбора данных о внешних SSD накопителях с объемом памяти 2TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_ssd_2TB"
- `"url"`: "------------------------SANDISK external_ssd 2TB--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,122,551"

### `internal_hdd_35 1TB`
**Описание**: Сценарий для сбора данных о внутренних HDD накопителях 3.5" с объемом памяти 1TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_hdd_35-1tb"
- `"url"`: "------------------------SANDISK internal_hdd_35-1tb--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,123,177"

### `internal_hdd_35 2TB`
**Описание**: Сценарий для сбора данных о внутренних HDD накопителях 3.5" с объемом памяти 2TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_hdd_35-2tb"
- `"url"`: "------------------------SANDISK internal_hdd--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,123,178"

### `internal_hdd_35 3TB`
**Описание**: Сценарий для сбора данных о внутренних HDD накопителях 3.5" с объемом памяти 3TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_hdd_35-3tb"
- `"url"`: "------------------------SANDISK internal_hdd--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,123,179"

### `internal_hdd_35 4TB`
**Описание**: Сценарий для сбора данных о внутренних HDD накопителях 3.5" с объемом памяти 4TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_hdd_35-4tb"
- `"url"`: "------------------------SANDISK internal_hdd--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,123,180"

### `internal_hdd_35 6TB`
**Описание**: Сценарий для сбора данных о внутренних HDD накопителях 3.5" с объемом памяти 6TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_hdd_35-6tb"
- `"url"`: "------------------------SANDISK internal_hdd--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,123,181"

### `internal_hdd_35 8TB`
**Описание**: Сценарий для сбора данных о внутренних HDD накопителях 3.5" с объемом памяти 8TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_hdd_35-8tb"
- `"url"`: "------------------------SANDISK internal_hdd--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,123,182"

### `internal_hdd_35 10TB`
**Описание**: Сценарий для сбора данных о внутренних HDD накопителях 3.5" с объемом памяти 10TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_hdd_35-10tb"
- `"url"`: "------------------------SANDISK internal_hdd--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,123,183"

### `internal_hdd_25 500GB`
**Описание**: Сценарий для сбора данных о внутренних HDD накопителях 2.5" с объемом памяти 500GB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_hdd_25_480"
- `"url"`: "------------------------SANDISK internal_hdd--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,124,166"

### `internal_hdd_25 1TB`
**Описание**: Сценарий для сбора данных о внутренних HDD накопителях 2.5" с объемом памяти 1TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "internal_ssd_sata_3_1tb"
- `"url"`: "------------------------SANDISK internal_hdd--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,124,167"

### `external_hdd_25 1TB`
**Описание**: Сценарий для сбора данных о внешних HDD накопителях 2.5" с объемом памяти 1TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_hdd_25-1tb"
- `"url"`: "------------------------SANDISK external_hdd_25--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,125,184"

### `external_hdd_25 2TB`
**Описание**: Сценарий для сбора данных о внешних HDD накопителях 2.5" с объемом памяти 2TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_hdd_2tb"
- `"url"`: "------------------------SANDISK external_hdd_25--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,125,185"

### `external_hdd_25 4TB`
**Описание**: Сценарий для сбора данных о внешних HDD накопителях 2.5" с объемом памяти 4TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_hdd_25_4tb"
- `"url"`: "------------------------SANDISK external_hdd_25--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,125,186"

### `external_hdd_25 5TB`
**Описание**: Сценарий для сбора данных о внешних HDD накопителях 2.5" с объемом памяти 5TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_hdd_25-5tb"
- `"url"`: "------------------------SANDISK external_hdd_25--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,125,187"

### `external_hdd_35 4TB`
**Описание**: Сценарий для сбора данных о внешних HDD накопителях 3.5" с объемом памяти 4TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_hdd_35-4tb"
- `"url"`: "------------------------SANDISK external_hdd_35--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,126,184"

### `external_hdd_35 6TB`
**Описание**: Сценарий для сбора данных о внешних HDD накопителях 3.5" с объемом памяти 6TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_hdd_35_6tb"
- `"url"`: "------------------------SANDISK external_hdd_35--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,126,185"

### `external_hdd_35 8TB`
**Описание**: Сценарий для сбора данных о внешних HDD накопителях 3.5" с объемом памяти 8TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_hdd_35_8tb"
- `"url"`: "------------------------SANDISK external_hdd_35--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,126,186"

### `external_hdd_35 10TB`
**Описание**: Сценарий для сбора данных о внешних HDD накопителях 3.5" с объемом памяти 10TB.
**Параметры**:
- `"brand"`: "SANDISK"
- `"name"`: "external_hdd_35_10tb"
- `"url"`: "------------------------SANDISK external_hdd_35--------------------------"
- `"checkbox"`: false
- `"active"`: true
- `"condition"`: "new"
- `"presta_categories"`: "117,126,187"