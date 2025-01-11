# Документация `morlevi_categories_storage_crucial.json`

## Обзор

Данный файл содержит JSON-конфигурацию сценариев для парсинга категорий товаров Crucial из магазина Morlevi. Каждый сценарий описывает определенную категорию товаров (например, внутренние SSD, внешние HDD и т.д.), включая их название, URL для парсинга, активность, условие и категории PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура данных](#структура-данных)
- [Сценарии](#сценарии)
  - [`internal_ssd_sata_3 120-128GB`](#internal_ssd_sata_3-120-128gb)
  - [`internal_ssd_sata_3 240-256GB`](#internal_ssd_sata_3-240-256gb)
  - [`internal_ssd_sata_3 480-525GB`](#internal_ssd_sata_3-480-525gb)
  - [`internal_ssd_sata_3 960GB-1TB`](#internal_ssd_sata_3-960gb-1tb)
  - [`internal_ssd_sata_3 2TB`](#internal_ssd_sata_3-2tb)
  - [`internal_ssd_sata_3 4TB`](#internal_ssd_sata_3-4tb)
  - [`internal_ssd_sata_3 8TB`](#internal_ssd_sata_3-8tb)
  - [`internal_ssd_msata 240-256GB`](#internal_ssd_msata-240-256gb)
  - [`internal_ssd_m2sata 240-256GB`](#internal_ssd_m2sata-240-256gb)
  - [`internal_ssd_m2sata 480-525GB`](#internal_ssd_m2sata-480-525gb)
  - [`internal_ssd_nvmi 240-256GB`](#internal_ssd_nvmi-240-256gb)
  - [`internal_ssd_nvmi 480-525GB`](#internal_ssd_nvmi-480-525gb)
  - [`internal_ssd_nvmi 960GB-1TB`](#internal_ssd_nvmi-960gb-1tb)
  - [`internal_ssd_nvmi 2TB`](#internal_ssd_nvmi-2tb)
  - [`internal_ssd_nvmi_gen4 240-256GB`](#internal_ssd_nvmi_gen4-240-256gb)
  - [`internal_ssd_nvmi_gen4 480-525GB`](#internal_ssd_nvmi_gen4-480-525gb)
  - [`internal_ssd_nvmi_gen4 960GB-1TB`](#internal_ssd_nvmi_gen4-960gb-1tb)
  - [`internal_ssd_nvmi_gen4 2TB`](#internal_ssd_nvmi_gen4-2tb)
  - [`external_ssd 500GB`](#external_ssd-500gb)
  - [`external_ssd 1TB`](#external_ssd-1tb)
  - [`external_ssd 2TB`](#external_ssd-2tb)
  - [`internal_hdd_35 1TB`](#internal_hdd_35-1tb)
  - [`internal_hdd_35 2TB`](#internal_hdd_35-2tb)
  - [`internal_hdd_35 3TB`](#internal_hdd_35-3tb)
  - [`internal_hdd_35 4TB`](#internal_hdd_35-4tb)
  - [`internal_hdd_35 6TB`](#internal_hdd_35-6tb)
  - [`internal_hdd_35 8TB`](#internal_hdd_35-8tb)
  - [`internal_hdd_35 10TB`](#internal_hdd_35-10tb)
  - [`internal_hdd_25 500GB`](#internal_hdd_25-500gb)
  - [`internal_hdd_25 1TB`](#internal_hdd_25-1tb)
  - [`external_hdd_25 1TB`](#external_hdd_25-1tb)
  - [`external_hdd_25 2TB`](#external_hdd_25-2tb)
  - [`external_hdd_25 4TB`](#external_hdd_25-4tb)
  - [`external_hdd_25 5TB`](#external_hdd_25-5tb)
  - [`external_hdd_35 4TB`](#external_hdd_35-4tb)
  - [`external_hdd_35 6TB`](#external_hdd_35-6tb)
  - [`external_hdd_35 8TB`](#external_hdd_35-8tb)
  - [`external_hdd_35 10TB`](#external_hdd_35-10tb)

## Структура данных

JSON-файл состоит из объекта с одним ключом `scenarios`, который содержит объект, в котором ключами являются идентификаторы сценариев, а значениями - объекты с параметрами для каждого сценария:

- `brand` (str): Бренд товара. В данном случае всегда `CRUCIAL`.
- `name` (str): Название сценария, которое используется для идентификации категории товара.
- `url` (str): URL-адрес страницы магазина Morlevi для парсинга товаров данной категории. Если `url` состоит из `-----------------------------------`, то парсинг данной категории не происходит.
- `checkbox` (bool): Флаг, указывающий на необходимость установки галочки (в данном случае всегда `false`).
- `active` (bool): Флаг, указывающий, активен ли данный сценарий (всегда `true`).
- `condition` (str): Состояние товара (всегда `new`).
- `presta_categories` (str): Строка с идентификаторами категорий PrestaShop, разделенными запятыми.

## Сценарии

### `internal_ssd_sata_3 120-128GB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 120-128GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_sata_3_128".
- `url` (str): "---------------------------------------------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,134".

### `internal_ssd_sata_3 240-256GB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 240-256GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_sata_3_256".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=19&p_175=823&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,135".

### `internal_ssd_sata_3 480-525GB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 480-525GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_sata_3_512".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=19&p_175=826&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,136".

### `internal_ssd_sata_3 960GB-1TB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 960GB-1TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_sata_3_1tb".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=19&p_175=829&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,137".

### `internal_ssd_sata_3 2TB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 2TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_sata_3_2tb".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=19&p_175=831&p_174=816&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,138".

### `internal_ssd_sata_3 4TB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 4TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_sata_3_4tb".
- `url` (str): "------------------------CRUCIAL  internal_ssd_sata_3_4tb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,139".

### `internal_ssd_sata_3 8TB`

**Описание**: Сценарий для внутренних SSD SATA 3 объемом 8TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_sata_3_8tb".
- `url` (str): "------------------------CRUCIAL  internal_ssd_sata_3_8tb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,140".

### `internal_ssd_msata 240-256GB`

**Описание**: Сценарий для внутренних SSD mSATA объемом 240-256GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_msata_240gb".
- `url` (str): "------------------------CRUCIAL  internal_ssd_msata_240gb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,163,164".

### `internal_ssd_m2sata 240-256GB`

**Описание**: Сценарий для внутренних SSD M.2 SATA объемом 240-256GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_m2sata_256".
- `url` (str): "------------------------CRUCIAL  internal_ssd_m2sata_256---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,149".

### `internal_ssd_m2sata 480-525GB`

**Описание**: Сценарий для внутренних SSD M.2 SATA объемом 480-525GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_m2sata_256".
- `url` (str): "------------------------CRUCIAL internal_ssd_m2sata_256--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,150".

### `internal_ssd_nvmi 240-256GB`

**Описание**: Сценарий для внутренних SSD NVMe объемом 240-256GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_nvme_256".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=19&p_175=823&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,119,141".

### `internal_ssd_nvmi 480-525GB`

**Описание**: Сценарий для внутренних SSD NVMe объемом 480-525GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_nvme_512".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=19&p_175=826&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,119,142".

### `internal_ssd_nvmi 960GB-1TB`

**Описание**: Сценарий для внутренних SSD NVMe объемом 960GB-1TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_nvme_1tb".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=19&p_175=829&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,119,143".

### `internal_ssd_nvmi 2TB`

**Описание**: Сценарий для внутренних SSD NVMe объемом 2TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_nvme_2tb".
- `url` (str): "-------------------------------CRUCIAL--internal_ssd_nvme_2tb--------------=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,119,144".

### `internal_ssd_nvmi_gen4 240-256GB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 объемом 240-256GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_nvmi_gen4_256".
- `url` (str): "------------------------CRUCIAL internal_ssd_nvmi_gen4_256---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,120,141,165".

### `internal_ssd_nvmi_gen4 480-525GB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 объемом 480-525GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_nvmi_gen4_512".
- `url` (str): "------------------------CRUCIAL internal_ssd_nvmi_gen4_512---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,120,142,168".

### `internal_ssd_nvmi_gen4 960GB-1TB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 объемом 960GB-1TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_nvmi_gen4_1tb".
- `url` (str): "-------------------------------------------------------------------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,120,143,169".

### `internal_ssd_nvmi_gen4 2TB`

**Описание**: Сценарий для внутренних SSD NVMe Gen4 объемом 2TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_nvmi_gen4_2tb".
- `url` (str): "------------------------CRUCIAL internal_ssd_nvmi_gen4_2tb--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,120,144".

### `external_ssd 500GB`

**Описание**: Сценарий для внешних SSD объемом 500GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_ssd_500GB".
- `url` (str): "------------------------CRUCIAL external_ssd 500GB--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,122,549".

### `external_ssd 1TB`

**Описание**: Сценарий для внешних SSD объемом 1TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_ssd-1TB".
- `url` (str): "------------------------CRUCIAL external_ssd 1TB--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,122,550".

### `external_ssd 2TB`

**Описание**: Сценарий для внешних SSD объемом 2TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_ssd_2TB".
- `url` (str): "------------------------CRUCIAL external_ssd 2TB--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,122,551".

### `internal_hdd_35 1TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 1TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_hdd_35-1tb".
- `url` (str): "------------------------CRUCIAL internal_hdd_35-1tb--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,177".

### `internal_hdd_35 2TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 2TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_hdd_35-2tb".
- `url` (str): "------------------------CRUCIAL internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,178".

### `internal_hdd_35 3TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 3TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_hdd_35-3tb".
- `url` (str): "------------------------CRUCIAL internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,179".

### `internal_hdd_35 4TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 4TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_hdd_35-4tb".
 - `url` (str): "------------------------CRUCIAL internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,180".

### `internal_hdd_35 6TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 6TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_hdd_35-6tb".
 - `url` (str): "------------------------CRUCIAL internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,181".

### `internal_hdd_35 8TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 8TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_hdd_35-8tb".
 - `url` (str): "------------------------CRUCIAL internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,182".

### `internal_hdd_35 10TB`

**Описание**: Сценарий для внутренних HDD 3.5" объемом 10TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_hdd_35-10tb".
 - `url` (str): "------------------------CRUCIAL internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,183".

### `internal_hdd_25 500GB`

**Описание**: Сценарий для внутренних HDD 2.5" объемом 500GB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_hdd_25_480".
 - `url` (str): "------------------------CRUCIAL internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,124,166".

### `internal_hdd_25 1TB`

**Описание**: Сценарий для внутренних HDD 2.5" объемом 1TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "internal_ssd_sata_3_1tb".
 - `url` (str): "------------------------CRUCIAL internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,124,167".

### `external_hdd_25 1TB`

**Описание**: Сценарий для внешних HDD 2.5" объемом 1TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_hdd_25-1tb".
- `url` (str): "------------------------CRUCIAL external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,125,184".

### `external_hdd_25 2TB`

**Описание**: Сценарий для внешних HDD 2.5" объемом 2TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_hdd_2tb".
- `url` (str): "------------------------CRUCIAL external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,125,185".

### `external_hdd_25 4TB`

**Описание**: Сценарий для внешних HDD 2.5" объемом 4TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_hdd_25_4tb".
- `url` (str): "------------------------CRUCIAL external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,125,186".

### `external_hdd_25 5TB`

**Описание**: Сценарий для внешних HDD 2.5" объемом 5TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_hdd_25-5tb".
- `url` (str): "------------------------CRUCIAL external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,125,187".

### `external_hdd_35 4TB`

**Описание**: Сценарий для внешних HDD 3.5" объемом 4TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_hdd_35-4tb".
- `url` (str): "------------------------CRUCIAL external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,126,184".

### `external_hdd_35 6TB`

**Описание**: Сценарий для внешних HDD 3.5" объемом 6TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_hdd_35_6tb".
- `url` (str): "------------------------CRUCIAL external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,126,185".

### `external_hdd_35 8TB`

**Описание**: Сценарий для внешних HDD 3.5" объемом 8TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_hdd_35_8tb".
- `url` (str): "------------------------CRUCIAL external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,126,186".

### `external_hdd_35 10TB`

**Описание**: Сценарий для внешних HDD 3.5" объемом 10TB.

**Параметры**:
- `brand` (str): "CRUCIAL".
- `name` (str): "external_hdd_35_10tb".
- `url` (str): "------------------------CRUCIAL external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,126,187".