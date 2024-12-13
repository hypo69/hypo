# Документация для `morlevi_categories_storage_sandisk.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сбора данных о категориях товаров SANDISK с сайта Morlevi. Он определяет различные сценарии для SSD и HDD накопителей, включая внутренние и внешние варианты, а также их различные объемы. Каждый сценарий содержит параметры для идентификации товара на сайте, URL-адрес страницы категории и соответствующие категории PrestaShop.

## Содержание

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
3.  [Описание сценариев](#описание-сценариев)
    -   [internal\_ssd\_sata\_3 120-128GB](#internal_ssd_sata_3-120-128gb)
    -   [internal\_ssd\_sata\_3 240-256GB](#internal_ssd_sata_3-240-256gb)
    -   [internal\_ssd\_sata\_3 480-525GB](#internal_ssd_sata_3-480-525gb)
    -   [internal\_ssd\_sata\_3 960GB-1TB](#internal_ssd_sata_3-960gb-1tb)
    -   [internal\_ssd\_sata\_3 2TB](#internal_ssd_sata_3-2tb)
    -   [internal\_ssd\_sata\_3 4TB](#internal_ssd_sata_3-4tb)
    -   [internal\_ssd\_sata\_3 8TB](#internal_ssd_sata_3-8tb)
    -   [internal\_ssd\_msata 240-256GB](#internal_ssd_msata-240-256gb)
    -   [internal\_ssd\_m2sata 240-256GB](#internal_ssd_m2sata-240-256gb)
    -   [internal\_ssd\_m2sata 480-525GB](#internal_ssd_m2sata-480-525gb)
    -   [internal\_ssd\_nvmi 240-256GB](#internal_ssd_nvmi-240-256gb)
    -   [internal\_ssd\_nvmi 480-525GB](#internal_ssd_nvmi-480-525gb)
    -   [internal\_ssd\_nvmi 960GB-1TB](#internal_ssd_nvmi-960gb-1tb)
    -   [internal\_ssd\_nvmi 2TB](#internal_ssd_nvmi-2tb)
    -   [internal\_ssd\_nvmi\_gen4 240-256GB](#internal_ssd_nvmi_gen4-240-256gb)
    -   [internal\_ssd\_nvmi\_gen4 480-525GB](#internal_ssd_nvmi_gen4-480-525gb)
    -   [internal\_ssd\_nvmi\_gen4 960GB-1TB](#internal_ssd_nvmi_gen4-960gb-1tb)
    -   [internal\_ssd\_nvmi\_gen4 2TB](#internal_ssd_nvmi_gen4-2tb)
    -   [external\_ssd 500GB](#external_ssd-500gb)
    -   [external\_ssd 1TB](#external_ssd-1tb)
    -   [external\_ssd 2TB](#external_ssd-2tb)
     -  [internal\_hdd\_35 1TB](#internal_hdd_35-1tb)
    -   [internal\_hdd\_35 2TB](#internal_hdd_35-2tb)
    -   [internal\_hdd\_35 3TB](#internal_hdd_35-3tb)
    -   [internal\_hdd\_35 4TB](#internal_hdd_35-4tb)
    -  [internal\_hdd\_35 6TB](#internal_hdd_35-6tb)
    -   [internal\_hdd\_35 8TB](#internal_hdd_35-8tb)
    -   [internal\_hdd\_35 10TB](#internal_hdd_35-10tb)
    -   [internal\_hdd\_25 500GB](#internal_hdd_25-500gb)
    -  [internal\_hdd\_25 1TB](#internal_hdd_25-1tb)
    -   [external\_hdd\_25 1TB](#external_hdd_25-1tb)
    -   [external\_hdd\_25 2TB](#external_hdd_25-2tb)
    -   [external\_hdd\_25 4TB](#external_hdd_25-4tb)
    -   [external\_hdd\_25 5TB](#external_hdd_25-5tb)
    -   [external\_hdd\_35 4TB](#external_hdd_35-4tb)
    -   [external\_hdd\_35 6TB](#external_hdd_35-6tb)
    -   [external\_hdd\_35 8TB](#external_hdd_35-8tb)
    -   [external\_hdd\_35 10TB](#external_hdd_35-10tb)
    
## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "<scenario_name>": {
      "brand": "<brand_name>",
      "name": "<product_name>",
      "url": "<url_address>",
      "checkbox": <boolean>,
      "active": <boolean>,
       "condition": "<product_condition>",
      "presta_categories": "<comma_separated_categories>"
    }
  }
}
```

Где:

*   `scenarios`: Основной объект, содержащий все сценарии.
*   `<scenario_name>`: Ключ, представляющий название сценария (например, `internal_ssd_sata_3 120-128GB`).
*   `brand`: Бренд продукта (в данном случае всегда "SANDISK").
*   `name`: Название продукта для внутреннего использования.
*   `url`: URL-адрес страницы категории на сайте Morlevi.
*   `checkbox`: Логическое значение, указывающее, используется ли чекбокс для выбора (всегда `false`).
*   `active`: Логическое значение, указывающее, активен ли данный сценарий (всегда `true`).
*   `condition`: Условие товара (всегда `"new"`).
*  `presta_categories`: Строка с идентификаторами категорий PrestaShop, разделенными запятыми.

## Описание сценариев

### `internal_ssd_sata_3 120-128GB`

**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 накопителях объемом 120-128GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_sata_3_128".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=23&p_175=822&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,118,134"`.
### `internal_ssd_sata_3 240-256GB`

**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 накопителях объемом 240-256GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_sata_3_256".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=23&p_175=823&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,118,135"`.

### `internal_ssd_sata_3 480-525GB`

**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 накопителях объемом 480-525GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_sata_3_512".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=23&p_175=826&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,118,136"`.

### `internal_ssd_sata_3 960GB-1TB`

**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 накопителях объемом 960GB-1TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_sata_3_1tb".
- `url` (str): "------------------------SANDISK  internal_ssd_sata_3_1tb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,118,137"`.

### `internal_ssd_sata_3 2TB`

**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 накопителях объемом 2TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_sata_3_2tb".
- `url` (str): "------------------------SANDISK  internal_ssd_sata_3_2tb--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,118,138"`.

### `internal_ssd_sata_3 4TB`

**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 накопителях объемом 4TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_sata_3_4tb".
- `url` (str): "------------------------SANDISK  internal_ssd_sata_3_4tb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,118,139"`.

### `internal_ssd_sata_3 8TB`

**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 накопителях объемом 8TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_sata_3_8tb".
- `url` (str): "------------------------SANDISK  internal_ssd_sata_3_8tb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,118,140"`.

### `internal_ssd_msata 240-256GB`

**Описание**: Сценарий для сбора данных о внутренних SSD mSATA накопителях объемом 240-256GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_msata_240gb".
- `url` (str): "------------------------SANDISK  internal_ssd_msata_240gb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,163,164"`.

### `internal_ssd_m2sata 240-256GB`

**Описание**: Сценарий для сбора данных о внутренних SSD M.2 SATA накопителях объемом 240-256GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_m2sata_256".
- `url` (str): "------------------------SANDISK  internal_ssd_m2sata_256---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,149"`.

### `internal_ssd_m2sata 480-525GB`

**Описание**: Сценарий для сбора данных о внутренних SSD M.2 SATA накопителях объемом 480-525GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_m2sata_256".
- `url` (str): "------------------------SANDISK internal_ssd_m2sata_256--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,150"`.

### `internal_ssd_nvmi 240-256GB`

**Описание**: Сценарий для сбора данных о внутренних SSD NVMe накопителях объемом 240-256GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_nvme_256".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=23&p_175=823&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,119,141"`.

### `internal_ssd_nvmi 480-525GB`

**Описание**: Сценарий для сбора данных о внутренних SSD NVMe накопителях объемом 480-525GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_nvme_512".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=23&p_175=826&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,119,142"`.

### `internal_ssd_nvmi 960GB-1TB`

**Описание**: Сценарий для сбора данных о внутренних SSD NVMe накопителях объемом 960GB-1TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_nvme_1tb".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=23&p_175=829&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,119,143"`.

### `internal_ssd_nvmi 2TB`

**Описание**: Сценарий для сбора данных о внутренних SSD NVMe накопителях объемом 2TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_nvme_2tb".
- `url` (str): "------------------------SANDISK internal_ssd_nvme_2tb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,119,144"`.

### `internal_ssd_nvmi_gen4 240-256GB`

**Описание**: Сценарий для сбора данных о внутренних SSD NVMe Gen4 накопителях объемом 240-256GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_nvmi_gen4_256".
- `url` (str): "------------------------SANDISK internal_ssd_nvmi_gen4_256---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,120,141,165"`.

### `internal_ssd_nvmi_gen4 480-525GB`

**Описание**: Сценарий для сбора данных о внутренних SSD NVMe Gen4 накопителях объемом 480-525GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_nvmi_gen4_512".
- `url` (str): "------------------------SANDISK internal_ssd_nvmi_gen4_512---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,120,142,168"`.

### `internal_ssd_nvmi_gen4 960GB-1TB`

**Описание**: Сценарий для сбора данных о внутренних SSD NVMe Gen4 накопителях объемом 960GB-1TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_nvmi_gen4_1tb".
- `url` (str): "------------------------SANDISK internal_ssd_nvmi_gen4_1tb--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,120,143,169"`.

### `internal_ssd_nvmi_gen4 2TB`

**Описание**: Сценарий для сбора данных о внутренних SSD NVMe Gen4 накопителях объемом 2TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_nvmi_gen4_2tb".
- `url` (str): "------------------------SANDISK internal_ssd_nvmi_gen4_2tb--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,120,144"`.

### `external_ssd 500GB`

**Описание**: Сценарий для сбора данных о внешних SSD накопителях объемом 500GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_ssd_500GB".
- `url` (str): "------------------------SANDISK external_ssd 500GB--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,122,549"`.

### `external_ssd 1TB`

**Описание**: Сценарий для сбора данных о внешних SSD накопителях объемом 1TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_ssd-1TB".
- `url` (str): "------------------------SANDISK external_ssd 1TB--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,122,550"`.

### `external_ssd 2TB`

**Описание**: Сценарий для сбора данных о внешних SSD накопителях объемом 2TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_ssd_2TB".
- `url` (str): "------------------------SANDISK external_ssd 2TB--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,122,551"`.
### `internal_hdd_35 1TB`

**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" накопителях объемом 1TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_hdd_35-1tb".
- `url` (str): "------------------------SANDISK internal_hdd_35-1tb--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,123,177"`.

### `internal_hdd_35 2TB`

**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" накопителях объемом 2TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_hdd_35-2tb".
- `url` (str): "------------------------SANDISK internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,123,178"`.

### `internal_hdd_35 3TB`

**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" накопителях объемом 3TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_hdd_35-3tb".
- `url` (str): "------------------------SANDISK internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,123,179"`.

### `internal_hdd_35 4TB`

**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" накопителях объемом 4TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_hdd_35-4tb".
- `url` (str): "------------------------SANDISK internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,123,180"`.
### `internal_hdd_35 6TB`

**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" накопителях объемом 6TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_hdd_35-6tb".
- `url` (str): "------------------------SANDISK internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,123,181"`.

### `internal_hdd_35 8TB`

**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" накопителях объемом 8TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_hdd_35-8tb".
- `url` (str): "------------------------SANDISK internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,123,182"`.

### `internal_hdd_35 10TB`

**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" накопителях объемом 10TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_hdd_35-10tb".
- `url` (str): "------------------------SANDISK internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,123,183"`.

### `internal_hdd_25 500GB`

**Описание**: Сценарий для сбора данных о внутренних HDD 2.5" накопителях объемом 500GB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_hdd_25_480".
- `url` (str): "------------------------SANDISK internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,124,166"`.
### `internal_hdd_25 1TB`

**Описание**: Сценарий для сбора данных о внутренних HDD 2.5" накопителях объемом 1TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "internal_ssd_sata_3_1tb".
- `url` (str): "------------------------SANDISK internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,124,167"`.

### `external_hdd_25 1TB`

**Описание**: Сценарий для сбора данных о внешних HDD 2.5" накопителях объемом 1TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_hdd_25-1tb".
- `url` (str): "------------------------SANDISK external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,125,184"`.

### `external_hdd_25 2TB`

**Описание**: Сценарий для сбора данных о внешних HDD 2.5" накопителях объемом 2TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_hdd_2tb".
- `url` (str): "------------------------SANDISK external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,125,185"`.

### `external_hdd_25 4TB`

**Описание**: Сценарий для сбора данных о внешних HDD 2.5" накопителях объемом 4TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_hdd_25_4tb".
- `url` (str): "------------------------SANDISK external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,125,186"`.

### `external_hdd_25 5TB`

**Описание**: Сценарий для сбора данных о внешних HDD 2.5" накопителях объемом 5TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_hdd_25-5tb".
- `url` (str): "------------------------SANDISK external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,125,187"`.

### `external_hdd_35 4TB`

**Описание**: Сценарий для сбора данных о внешних HDD 3.5" накопителях объемом 4TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_hdd_35-4tb".
- `url` (str): "------------------------SANDISK external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,126,184"`.

### `external_hdd_35 6TB`

**Описание**: Сценарий для сбора данных о внешних HDD 3.5" накопителях объемом 6TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_hdd_35_6tb".
- `url` (str): "------------------------SANDISK external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,126,185"`.

### `external_hdd_35 8TB`

**Описание**: Сценарий для сбора данных о внешних HDD 3.5" накопителях объемом 8TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_hdd_35_8tb".
- `url` (str): "------------------------SANDISK external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"117,126,186"`.

### `external_hdd_35 10TB`

**Описание**: Сценарий для сбора данных о внешних HDD 3.5" накопителях объемом 10TB от SANDISK.

**Параметры**:
- `brand` (str): "SANDISK".
- `name` (str): "external_hdd_35_10tb".
- `url` (