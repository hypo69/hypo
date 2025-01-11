# Документация для `morlevi_categories_storage_wd.json`

## Обзор

Файл `morlevi_categories_storage_wd.json` содержит конфигурационные данные для определения соответствия между категориями товаров Western Digital и категориями в PrestaShop. Данные включают информацию о различных типах накопителей (SSD, HDD), их форм-факторах и объёмах, а также ссылки на соответствующие страницы на сайте поставщика.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура файла](#структура-файла)
3.  [Описание полей](#описание-полей)
4.  [Сценарии](#сценарии)

## Структура файла

Файл представляет собой JSON-объект, содержащий единственный ключ `scenarios`, значением которого является объект, содержащий наборы данных для каждого типа продукта. Каждый ключ этого объекта представляет собой сценарий для конкретного типа товара и содержит следующую структуру:

```json
{
    "scenarios": {
        "scenario_name": {
            "brand": "brand_name",
            "name": "product_name",
            "url": "product_url",
            "checkbox": false,
            "active": true,
            "condition": "product_condition",
            "presta_categories": "comma_separated_category_ids"
        }
    }
}
```

## Описание полей

-   `brand` (str): Название бренда продукта, в данном случае всегда "WESTERN DIGITAL".
-   `name` (str): Уникальное имя товара для внутреннего использования.
-   `url` (str): URL-адрес страницы товара на сайте поставщика.
-   `checkbox` (bool): Логический флаг, по умолчанию `false`.
-   `active` (bool): Логический флаг, указывающий, активен ли сценарий. Всегда `true`.
-   `condition` (str): Состояние товара, в данном случае всегда `"new"`.
-   `presta_categories` (str): Строка, содержащая ID категорий PrestaShop, разделенные запятыми, к которым относится товар.

## Сценарии

### `WESTERN DIGITAL internal_ssd_sata_3 120-128GB`

**Описание**: Сценарий для внутренних SSD накопителей SATA3 объемом 120-128GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_128"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3 120-128GB--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,134"

### `internal_ssd_sata_3 240-256GB`

**Описание**: Сценарий для внутренних SSD накопителей SATA3 объемом 240-256GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_256"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3240-256GB--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,135"

### `internal_ssd_sata_3 480-525GB`

**Описание**: Сценарий для внутренних SSD накопителей SATA3 объемом 480-525GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_512"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3 480-525--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,136"

### `internal_ssd_sata_3 960GB-1TB`

**Описание**: Сценарий для внутренних SSD накопителей SATA3 объемом 960GB-1TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_1tb"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3 960GB--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,137"

### `internal_ssd_sata_3 2TB`

**Описание**: Сценарий для внутренних SSD накопителей SATA3 объемом 2TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_2tb"
- `url`: "-------------------------------------WESTERN DIGITAL internal_ssd_sata_3 2TB--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,138"

### `internal_ssd_sata_3 4TB`

**Описание**: Сценарий для внутренних SSD накопителей SATA3 объемом 4TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_4tb"
- `url`: "------------------------WESTERN DIGITAL  internal_ssd_sata_3_4tb---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,139"

### `internal_ssd_sata_3 8TB`

**Описание**: Сценарий для внутренних SSD накопителей SATA3 объемом 8TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_8tb"
- `url`: "------------------------WESTERN DIGITAL  internal_ssd_sata_3_8tb---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,118,140"

### `internal_ssd_msata 240-256GB`

**Описание**: Сценарий для внутренних mSATA SSD накопителей объемом 240-256GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_msata_240gb"
- `url`: "------------------------WESTERN DIGITAL  internal_ssd_msata_240gb---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,163,164"

### `internal_ssd_m2sata 240-256GB`

**Описание**: Сценарий для внутренних M.2 SATA SSD накопителей объемом 240-256GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_m2sata_256"
- `url`: "------------------------WESTERN DIGITAL  internal_ssd_m2sata_256---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,149"

### `internal_ssd_m2sata 480-525GB`

**Описание**: Сценарий для внутренних M.2 SATA SSD накопителей объемом 480-525GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_m2sata_256"
- `url`: "------------------------WESTERN DIGITAL internal_ssd_m2sata_256--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,150"

### `internal_ssd_nvmi 240-256GB`

**Описание**: Сценарий для внутренних NVMe SSD накопителей объемом 240-256GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvme_256"
- `url`: "https://www.morlevi.co.il/Cat/51?p_315=4&p_175=823&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,119,141"

### `internal_ssd_nvmi 480-525GB`

**Описание**: Сценарий для внутренних NVMe SSD накопителей объемом 480-525GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvme_512"
- `url`: "https://www.morlevi.co.il/Cat/51?p_315=4&p_175=826&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,119,142"

### `internal_ssd_nvmi 960GB-1TB`

**Описание**: Сценарий для внутренних NVMe SSD накопителей объемом 960GB-1TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvme_1tb"
- `url`: "https://www.morlevi.co.il/Cat/51?p_315=4&p_175=829&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,119,143"

### `internal_ssd_nvmi 2TB`

**Описание**: Сценарий для внутренних NVMe SSD накопителей объемом 2TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvme_2tb"
- `url`: "-------------------------------WESTERN DIGITAL--internal_ssd_nvme_2tb--------------="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,119,144"

### `internal_ssd_nvmi_gen4 240-256GB`

**Описание**: Сценарий для внутренних NVMe Gen4 SSD накопителей объемом 240-256GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvmi_gen4_256"
- `url`: "------------------------WESTERN DIGITAL internal_ssd_nvmi_gen4_256---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,120,141,165"

### `internal_ssd_nvmi_gen4 480-525GB`

**Описание**: Сценарий для внутренних NVMe Gen4 SSD накопителей объемом 480-525GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvmi_gen4_512"
- `url`: "------------------------WESTERN DIGITAL internal_ssd_nvmi_gen4_512---------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,120,142,168"

### `internal_ssd_nvmi_gen4 960GB-1TB`

**Описание**: Сценарий для внутренних NVMe Gen4 SSD накопителей объемом 960GB-1TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvmi_gen4_1tb"
- `url`: "https://www.morlevi.co.il/Cat/51?p_315=4&p_175=829&p_174=820&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,120,143,169"

### `internal_ssd_nvmi_gen4 2TB`

**Описание**: Сценарий для внутренних NVMe Gen4 SSD накопителей объемом 2TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_nvmi_gen4_2tb"
- `url`: "------------------------WESTERN DIGITAL internal_ssd_nvmi_gen4_2tb--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,120,144"

### `external_ssd 500GB`

**Описание**: Сценарий для внешних SSD накопителей объемом 500GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_ssd_500GB"
- `url`: "https://www.morlevi.co.il/Cat/175?p_315=4&p_177=838&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,122,549"

### `external_ssd 500`

**Описание**: Сценарий для внешних SSD накопителей объемом 1TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_ssd-1TB"
- `url`: "https://www.morlevi.co.il/Cat/175?p_315=4&p_177=838&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,122,550"

### `external_ssd 1TB`

**Описание**: Сценарий для внешних SSD накопителей объемом 1TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_ssd-1TB"
- `url`: "https://www.morlevi.co.il/Cat/175?p_315=4&p_177=839&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,122,550"

### `external_ssd 2TB`

**Описание**: Сценарий для внешних SSD накопителей объемом 2TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_ssd_2TB"
- `url`: "https://www.morlevi.co.il/Cat/175?p_315=4&p_177=840&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,122,551"

### `internal_hdd_35 1TB`

**Описание**: Сценарий для внутренних HDD 3.5" накопителей объемом 1TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-1tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=839&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,177"

### `internal_hdd_35 2TB`

**Описание**: Сценарий для внутренних HDD 3.5" накопителей объемом 2TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-2tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=840&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,178"

### `internal_hdd_35 3TB`

**Описание**: Сценарий для внутренних HDD 3.5" накопителей объемом 3TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-3tb"
- `url`: "------------------------WESTERN DIGITAL internal_hdd--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,179"

### `internal_hdd_35 4TB`

**Описание**: Сценарий для внутренних HDD 3.5" накопителей объемом 4TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-4tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=842&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,180"

### `internal_hdd_35 6TB`

**Описание**: Сценарий для внутренних HDD 3.5" накопителей объемом 6TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-6tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=843&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,181"

### `internal_hdd_35 8TB`

**Описание**: Сценарий для внутренних HDD 3.5" накопителей объемом 8TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-8tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=844&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,182"

### `internal_hdd_35 10TB`

**Описание**: Сценарий для внутренних HDD 3.5" накопителей объемом 10TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-10tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=845&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,183"

### `internal_hdd_35 18TB`

**Описание**: Сценарий для внутренних HDD 3.5" накопителей объемом 18TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_35-10tb"
- `url`: "https://www.morlevi.co.il/Cat/49?p_315=4&p_177=3614&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,123,552"

### `internal_hdd_25 500GB`

**Описание**: Сценарий для внутренних HDD 2.5" накопителей объемом 500GB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_hdd_25_480"
- `url`: "-------------------------------------------------------------------------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,124,166"

### `internal_hdd_25 1TB`

**Описание**: Сценарий для внутренних HDD 2.5" накопителей объемом 1TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "internal_ssd_sata_3_1tb"
- `url`: "https://www.morlevi.co.il/Cat/187?p_315=4&p_177=839&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,124,167"

### `external_hdd_25 1TB`

**Описание**: Сценарий для внешних HDD 2.5" накопителей объемом 1TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_25-1tb"
- `url`: "https://www.morlevi.co.il/Cat/177?p_315=4&p_177=839&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,125,184"

### `external_hdd_25 2TB`

**Описание**: Сценарий для внешних HDD 2.5" накопителей объемом 2TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_2tb"
- `url`: "https://www.morlevi.co.il/Cat/177?p_315=4&p_177=840&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,125,185"

### `external_hdd_25 4TB`

**Описание**: Сценарий для внешних HDD 2.5" накопителей объемом 4TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_25_4tb"
- `url`: "https://www.morlevi.co.il/Cat/177?p_315=4&p_177=842&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,125,186"

### `external_hdd_25 5TB`

**Описание**: Сценарий для внешних HDD 2.5" накопителей объемом 5TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_25-5tb"
- `url`: "https://www.morlevi.co.il/Cat/177?p_315=4&p_177=3594&sort=datafloat2%2Cprice&keyword="
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,125,187"

### `external_hdd_35 4TB`

**Описание**: Сценарий для внешних HDD 3.5" накопителей объемом 4TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_35-4tb"
- `url`: "------------------------WESTERN DIGITAL external_hdd_35--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,126,184"

### `external_hdd_35 6TB`

**Описание**: Сценарий для внешних HDD 3.5" накопителей объемом 6TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_35_6tb"
- `url`: "------------------------WESTERN DIGITAL external_hdd_35--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,126,185"

### `external_hdd_35 8TB`

**Описание**: Сценарий для внешних HDD 3.5" накопителей объемом 8TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_35_8tb"
- `url`: "------------------------WESTERN DIGITAL external_hdd_35--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,126,186"

### `external_hdd_35 10TB`

**Описание**: Сценарий для внешних HDD 3.5" накопителей объемом 10TB.

**Поля**:
- `brand`: "WESTERN DIGITAL"
- `name`: "external_hdd_35_10tb"
- `url`: "------------------------WESTERN DIGITAL external_hdd_35--------------------------"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "117,126,187"