# Документация для `morlevi_categories_storage_wd.json`

## Обзор

Данный файл содержит JSON-структуру, описывающую сценарии для категорий товаров поставщика "WESTERN DIGITAL". Каждый сценарий включает информацию о бренде, имени, URL, состоянии активации и соответствующих категориях PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Сценарии](#сценарии)
  - [WESTERN DIGITAL internal_ssd_sata_3 120-128GB](#western-digital-internal_ssd_sata_3-120-128gb)
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
  - [external_ssd 500](#external_ssd-500)
  - [external_ssd 1TB](#external_ssd-1tb)
  - [external_ssd 2TB](#external_ssd-2tb)
  - [internal_hdd_35 1TB](#internal_hdd_35-1tb)
  - [internal_hdd_35 2TB](#internal_hdd_35-2tb)
  - [internal_hdd_35 3TB](#internal_hdd_35-3tb)
  - [internal_hdd_35 4TB](#internal_hdd_35-4tb)
  - [internal_hdd_35 6TB](#internal_hdd_35-6tb)
  - [internal_hdd_35 8TB](#internal_hdd_35-8tb)
  - [internal_hdd_35 10TB](#internal_hdd_35-10tb)
  - [internal_hdd_35 18TB](#internal_hdd_35-18tb)
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

Файл имеет следующую структуру:

```json
{
  "scenarios": {
    "scenario_name": {
      "brand": "string",
      "name": "string",
      "url": "string",
      "checkbox": "boolean",
      "active": "boolean",
      "condition": "string",
      "presta_categories": "string"
    }
   }
}
```

Где:

-   `scenarios`: Объект, содержащий все сценарии.
-   `scenario_name`: Ключ, представляющий название конкретного сценария.
-   `brand`: Бренд товара (в данном случае всегда "WESTERN DIGITAL").
-   `name`: Имя товара для внутреннего использования.
-   `url`: URL-адрес, связанный с товаром.
-   `checkbox`: Логическое значение, указывающее, установлен ли флажок (не используется в текущей реализации).
-   `active`: Логическое значение, определяющее, активен ли сценарий.
-    `condition`: Состояние товара, например, "new".
-   `presta_categories`: Строка, содержащая идентификаторы категорий PrestaShop, разделенные запятыми.

## Сценарии

### `WESTERN DIGITAL internal_ssd_sata_3 120-128GB`

**Описание**: Сценарий для внутренних SSD SATA 3 дисков ёмкостью 120-128GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_128"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3 120-128GB--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,134"

### `internal_ssd_sata_3 240-256GB`

**Описание**: Сценарий для внутренних SSD SATA 3 дисков ёмкостью 240-256GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_256"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3240-256GB--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,135"

### `internal_ssd_sata_3 480-525GB`

**Описание**: Сценарий для внутренних SSD SATA 3 дисков ёмкостью 480-525GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_512"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3 480-525--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,136"

### `internal_ssd_sata_3 960GB-1TB`

**Описание**: Сценарий для внутренних SSD SATA 3 дисков ёмкостью 960GB-1TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_1tb"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3 960GB--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,137"

### `internal_ssd_sata_3 2TB`

**Описание**: Сценарий для внутренних SSD SATA 3 дисков ёмкостью 2TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_2tb"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3 2TB--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,138"

### `internal_ssd_sata_3 4TB`

**Описание**: Сценарий для внутренних SSD SATA 3 дисков ёмкостью 4TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_4tb"
- `url`: "------------------------WESTERN DIGITAL  internal_ssd_sata_3_4tb---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,139"

### `internal_ssd_sata_3 8TB`

**Описание**: Сценарий для внутренних SSD SATA 3 дисков ёмкостью 8TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_8tb"
- `url`: "------------------------WESTERN DIGITAL  internal_ssd_sata_3_8tb---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,140"

### `internal_ssd_msata 240-256GB`

**Описание**: Сценарий для внутренних SSD mSATA дисков ёмкостью 240-256GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_msata_240gb"
- `url`: "------------------------WESTERN DIGITAL  internal_ssd_msata_240gb---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,163,164"

### `internal_ssd_m2sata 240-256GB`

**Описание**: Сценарий для внутренних SSD M.2 SATA дисков ёмкостью 240-256GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_m2sata_256"
- `url`: "------------------------WESTERN DIGITAL  internal_ssd_m2sata_256---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,149"

### `internal_ssd_m2sata 480-525GB`

**Описание**: Сценарий для внутренних SSD M.2 SATA дисков ёмкостью 480-525GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_m2sata_256"
- `url`: "------------------------WESTERN DIGITAL internal_ssd_m2sata_256--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,150"

### `internal_ssd_nvmi 240-256GB`

**Описание**: Сценарий для внутренних SSD NVMe дисков ёмкостью 240-256GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvme_256"
- `url`: "https://www.morlevi.co.il/Cat/51?p_315=4&p_175=823&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,119,141"

### `internal_ssd_nvmi 480-525GB`

**Описание**: Сценарий для внутренних SSD NVMe дисков ёмкостью 480-525GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvme_512"
- `url`: "https://www.morlevi.co.il/Cat/51?p_315=4&p_175=826&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,119,142"

### `internal_ssd_nvmi 960GB-1TB`

**Описание**: Сценарий для внутренних SSD NVMe дисков ёмкостью 960GB-1TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvme_1tb"
- `url`: "https://www.morlevi.co.il/Cat/51?p_315=4&p_175=829&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,119,143"

### `internal_ssd_nvmi 2TB`

**Описание**: Сценарий для внутренних SSD NVMe дисков ёмкостью 2TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvme_2tb"
- `url`: "-------------------------------WESTERN DIGITAL--internal_ssd_nvme_2tb--------------="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,119,144"

### `internal_ssd_nvmi_gen4 240-256GB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 дисков ёмкостью 240-256GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvmi_gen4_256"
- `url`: "------------------------WESTERN DIGITAL internal_ssd_nvmi_gen4_256---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,120,141,165"

### `internal_ssd_nvmi_gen4 480-525GB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 дисков ёмкостью 480-525GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvmi_gen4_512"
- `url`: "------------------------WESTERN DIGITAL internal_ssd_nvmi_gen4_512---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,120,142,168"

### `internal_ssd_nvmi_gen4 960GB-1TB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 дисков ёмкостью 960GB-1TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvmi_gen4_1tb"
- `url`: "https://www.morlevi.co.il/Cat/51?p_315=4&p_175=829&p_174=820&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,120,143,169"

### `internal_ssd_nvmi_gen4 2TB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 дисков ёмкостью 2TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvmi_gen4_2tb"
- `url`: "------------------------WESTERN DIGITAL internal_ssd_nvmi_gen4_2tb--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,120,144"

### `external_ssd 500GB`

**Описание**: Сценарий для внешних SSD дисков ёмкостью 500GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_ssd_500GB"
- `url`: "https://www.morlevi.co.il/Cat/175?p_315=4&p_177=838&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,122,549"

### `external_ssd 500`

**Описание**: Сценарий для внешних SSD дисков ёмкостью 1TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_ssd-1TB"
- `url`: "https://www.morlevi.co.il/Cat/175?p_315=4&p_177=838&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,122,550"

### `external_ssd 1TB`

**Описание**: Сценарий для внешних SSD дисков ёмкостью 1TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_ssd-1TB"
- `url`: "https://www.morlevi.co.il/Cat/175?p_315=4&p_177=839&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,122,550"

### `external_ssd 2TB`

**Описание**: Сценарий для внешних SSD дисков ёмкостью 2TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_ssd_2TB"
- `url`: "https://www.morlevi.co.il/Cat/175?p_315=4&p_177=840&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,122,551"

### `internal_hdd_35 1TB`

**Описание**: Сценарий для внутренних HDD 3.5" дисков ёмкостью 1TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-1tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=839&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,177"

### `internal_hdd_35 2TB`

**Описание**: Сценарий для внутренних HDD 3.5" дисков ёмкостью 2TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-2tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=840&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,178"

### `internal_hdd_35 3TB`

**Описание**: Сценарий для внутренних HDD 3.5" дисков ёмкостью 3TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-3tb"
- `url`: "------------------------WESTERN DIGITAL internal_hdd--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,179"

### `internal_hdd_35 4TB`

**Описание**: Сценарий для внутренних HDD 3.5" дисков ёмкостью 4TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-4tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=842&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,180"

### `internal_hdd_35 6TB`

**Описание**: Сценарий для внутренних HDD 3.5" дисков ёмкостью 6TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-6tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=843&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,181"

### `internal_hdd_35 8TB`

**Описание**: Сценарий для внутренних HDD 3.5" дисков ёмкостью 8TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-8tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=844&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,182"

### `internal_hdd_35 10TB`

**Описание**: Сценарий для внутренних HDD 3.5" дисков ёмкостью 10TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-10tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=845&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,183"

### `internal_hdd_35 18TB`

**Описание**: Сценарий для внутренних HDD 3.5" дисков ёмкостью 18TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-10tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=3614&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,552"

### `internal_hdd_25 500GB`

**Описание**: Сценарий для внутренних HDD 2.5" дисков ёмкостью 500GB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_25_480"
- `url`: "-------------------------------------------------------------------------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,124,166"

### `internal_hdd_25 1TB`

**Описание**: Сценарий для внутренних HDD 2.5" дисков ёмкостью 1TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_1tb"
- `url`: "https://www.morlevi.co.il/Cat/187?p_315=4&p_177=839&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,124,167"

### `external_hdd_25 1TB`

**Описание**: Сценарий для внешних HDD 2.5" дисков ёмкостью 1TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_25-1tb"
- `url`: "https://www.morlevi.co.il/Cat/177?p_315=4&p_177=839&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,125,184"

### `external_hdd_25 2TB`

**Описание**: Сценарий для внешних HDD 2.5" дисков ёмкостью 2TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_2tb"
- `url`: "https://www.morlevi.co.il/Cat/177?p_315=4&p_177=840&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,125,185"

### `external_hdd_25 4TB`

**Описание**: Сценарий для внешних HDD 2.5" дисков ёмкостью 4TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_25_4tb"
- `url`: "https://www.morlevi.co.il/Cat/177?p_315=4&p_177=842&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,125,186"

### `external_hdd_25 5TB`

**Описание**: Сценарий для внешних HDD 2.5" дисков ёмкостью 5TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_25-5tb"
- `url`: "https://www.morlevi.co.il/Cat/177?p_315=4&p_177=3594&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,125,187"

### `external_hdd_35 4TB`

**Описание**: Сценарий для внешних HDD 3.5" дисков ёмкостью 4TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_35-4tb"
- `url`: "------------------------WESTERN DIGITAL external_hdd_35--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,126,184"

### `external_hdd_35 6TB`

**Описание**: Сценарий для внешних HDD 3.5" дисков ёмкостью 6TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_35_6tb"
- `url`: "------------------------WESTERN DIGITAL external_hdd_35--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,126,185"

### `external_hdd_35 8TB`

**Описание**: Сценарий для внешних HDD 3.5" дисков ёмкостью 8TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_35_8tb"
- `url`: "------------------------WESTERN DIGITAL external_hdd_35--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,126,186"

### `external_hdd_35 10TB`

**Описание**: Сценарий для внешних HDD 3.5" дисков ёмкостью 10TB.

**Параметры**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_35_10tb"
- `url`: "------------------------WESTERN DIGITAL external_hdd_35--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,126,187"