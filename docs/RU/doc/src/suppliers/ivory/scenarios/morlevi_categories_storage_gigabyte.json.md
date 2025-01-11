# Документация для `morlevi_categories_storage_gigabyte.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Описание сценариев](#описание-сценариев)

## Обзор

Файл `morlevi_categories_storage_gigabyte.json` содержит JSON-структуру, описывающую сценарии для сбора данных о категориях товаров GIGABYTE из магазина Morlevi. Каждый сценарий определяет параметры для поиска и фильтрации товаров, такие как бренд, имя, URL для сбора данных, а также категории PrestaShop, к которым относятся товары.

## Структура файла

Файл представляет собой JSON-объект с одним основным ключом `scenarios`, значением которого является объект, содержащий набор сценариев. Каждый сценарий представлен в виде пары ключ-значение, где:

- Ключ: Строка, представляющая уникальное имя сценария (например, "internal_ssd_sata_3 120-128GB").
- Значение: Объект, содержащий данные сценария:
    - `brand` (str): Бренд товара (в данном случае всегда "GIGABYTE").
    - `name` (str): Внутреннее имя сценария, используемое для идентификации.
    - `url` (str): URL-адрес страницы с товарами на сайте Morlevi. Для некоторых категорий указаны заглушки.
    - `checkbox` (bool): Флаг, указывающий на необходимость использования чекбокса. Всегда `false`.
    - `active` (bool): Флаг, указывающий на активность сценария. Всегда `true`.
    - `condition` (str): Состояние товара, всегда "new".
    - `presta_categories` (str): Строка, содержащая идентификаторы категорий PrestaShop, разделенные запятыми.

## Описание сценариев

### `internal_ssd_sata_3 120-128GB`
**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 объемом 120-128GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_sata_3_128".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=2&p_175=822&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,134".

### `internal_ssd_sata_3 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 объемом 240-256GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_sata_3_256".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=2&p_175=823&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,135".

### `internal_ssd_sata_3 480-525GB`
**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 объемом 480-525GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_sata_3_512".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=2&p_175=826&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,136".

### `internal_ssd_sata_3 960GB-1TB`
**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 объемом 960GB-1TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_sata_3_1tb".
- `url` (str): "https://www.morlevi.co.il/Cat/50?p_315=2&p_175=829&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,137".

### `internal_ssd_sata_3 2TB`
**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 объемом 2TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_sata_3_2tb".
- `url` (str): "------------------------GIGABYTE  internal_ssd_sata_3_2tb--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,138".

### `internal_ssd_sata_3 4TB`
**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 объемом 4TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_sata_3_4tb".
- `url` (str): "------------------------GIGABYTE  internal_ssd_sata_3_4tb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,139".

### `internal_ssd_sata_3 8TB`
**Описание**: Сценарий для сбора данных о внутренних SSD SATA 3 объемом 8TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_sata_3_8tb".
- `url` (str): "------------------------GIGABYTE  internal_ssd_sata_3_8tb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,118,140".

### `internal_ssd_msata 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD mSATA объемом 240-256GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_msata_240gb".
- `url` (str): "------------------------GIGABYTE  internal_ssd_msata_240gb---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,163,164".

### `internal_ssd_m2sata 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD M.2 SATA объемом 240-256GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_m2sata_256".
- `url` (str): "------------------------GIGABYTE  internal_ssd_m2sata_256---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,149".

### `internal_ssd_m2sata 480-525GB`
**Описание**: Сценарий для сбора данных о внутренних SSD M.2 SATA объемом 480-525GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_m2sata_256".
- `url` (str): "------------------------GIGABYTE internal_ssd_m2sata_256--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,150".

### `internal_ssd_nvmi 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD NVMe объемом 240-256GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_nvme_256".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=2&p_175=823&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,119,141".

### `internal_ssd_nvmi 480-525GB`
**Описание**: Сценарий для сбора данных о внутренних SSD NVMe объемом 480-525GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_nvme_512".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=2&p_175=826&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,119,142".

### `internal_ssd_nvmi 960GB-1TB`
**Описание**: Сценарий для сбора данных о внутренних SSD NVMe объемом 960GB-1TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_nvme_1tb".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=2&p_175=829&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,119,143".

### `internal_ssd_nvmi 2TB`
**Описание**: Сценарий для сбора данных о внутренних SSD NVMe объемом 2TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_nvme_2tb".
- `url` (str): "-------------------------------GIGABYTE--internal_ssd_nvme_2tb--------------=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,119,144".

### `internal_ssd_nvmi_gen4 240-256GB`
**Описание**: Сценарий для сбора данных о внутренних SSD NVMe Gen4 объемом 240-256GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_nvmi_gen4_256".
- `url` (str): "------------------------GIGABYTE internal_ssd_nvmi_gen4_256---------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,120,141,165".

### `internal_ssd_nvmi_gen4 480-525GB`
**Описание**: Сценарий для сбора данных о внутренних SSD NVMe Gen4 объемом 480-525GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_nvmi_gen4_512".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=2&p_175=826&p_174=3352&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,120,142,168".

### `internal_ssd_nvmi_gen4 960GB-1TB`
**Описание**: Сценарий для сбора данных о внутренних SSD NVMe Gen4 объемом 960GB-1TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_nvmi_gen4_1tb".
- `url` (str): "https://www.morlevi.co.il/Cat/51?p_315=2&p_175=829&p_174=3234&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,120,143,169".

### `internal_ssd_nvmi_gen4 2TB`
**Описание**: Сценарий для сбора данных о внутренних SSD NVMe Gen4 объемом 2TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_nvmi_gen4_2tb".
- `url` (str): "https://www.morlevi.co.il/Cat/172?p_315=2&p_175=831&p_174=3234&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,120,144".

### `external_ssd 500GB`
**Описание**: Сценарий для сбора данных о внешних SSD объемом 500GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_ssd_500GB".
- `url` (str): "------------------------GIGABYTE external_ssd 500GB--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,122,549".

### `external_ssd 1TB`
**Описание**: Сценарий для сбора данных о внешних SSD объемом 1TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_ssd-1TB".
- `url` (str): "------------------------GIGABYTE external_ssd 1TB--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,122,550".

### `external_ssd 2TB`
**Описание**: Сценарий для сбора данных о внешних SSD объемом 2TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_ssd_2TB".
- `url` (str): "------------------------GIGABYTE external_ssd 2TB--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,122,551".

### `internal_hdd_35 1TB`
**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" объемом 1TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_hdd_35-1tb".
- `url` (str): "------------------------GIGABYTE internal_hdd_35-1tb--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,177".

### `internal_hdd_35 2TB`
**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" объемом 2TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_hdd_35-2tb".
- `url` (str): "------------------------GIGABYTE internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,178".

### `internal_hdd_35 3TB`
**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" объемом 3TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_hdd_35-3tb".
- `url` (str): "------------------------GIGABYTE internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,179".

### `internal_hdd_35 4TB`
**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" объемом 4TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_hdd_35-4tb".
- `url` (str): "------------------------GIGABYTE internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,180".

### `internal_hdd_35 6TB`
**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" объемом 6TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_hdd_35-6tb".
- `url` (str): "------------------------GIGABYTE internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,181".

### `internal_hdd_35 8TB`
**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" объемом 8TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_hdd_35-8tb".
- `url` (str): "------------------------GIGABYTE internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,182".

### `internal_hdd_35 10TB`
**Описание**: Сценарий для сбора данных о внутренних HDD 3.5" объемом 10TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_hdd_35-10tb".
- `url` (str): "------------------------GIGABYTE internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,123,183".

### `internal_hdd_25 500GB`
**Описание**: Сценарий для сбора данных о внутренних HDD 2.5" объемом 500GB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_hdd_25_480".
- `url` (str): "------------------------GIGABYTE internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,124,166".

### `internal_hdd_25 1TB`
**Описание**: Сценарий для сбора данных о внутренних HDD 2.5" объемом 1TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "internal_ssd_sata_3_1tb".
- `url` (str): "------------------------GIGABYTE internal_hdd--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,124,167".

### `external_hdd_25 1TB`
**Описание**: Сценарий для сбора данных о внешних HDD 2.5" объемом 1TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_hdd_25-1tb".
- `url` (str): "------------------------GIGABYTE external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,125,184".

### `external_hdd_25 2TB`
**Описание**: Сценарий для сбора данных о внешних HDD 2.5" объемом 2TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_hdd_2tb".
- `url` (str): "------------------------GIGABYTE external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,125,185".

### `external_hdd_25 4TB`
**Описание**: Сценарий для сбора данных о внешних HDD 2.5" объемом 4TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_hdd_25_4tb".
- `url` (str): "------------------------GIGABYTE external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,125,186".

### `external_hdd_25 5TB`
**Описание**: Сценарий для сбора данных о внешних HDD 2.5" объемом 5TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_hdd_25-5tb".
- `url` (str): "------------------------GIGABYTE external_hdd_25--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,125,187".

### `external_hdd_35 4TB`
**Описание**: Сценарий для сбора данных о внешних HDD 3.5" объемом 4TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_hdd_35-4tb".
- `url` (str): "------------------------GIGABYTE external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,126,184".

### `external_hdd_35 6TB`
**Описание**: Сценарий для сбора данных о внешних HDD 3.5" объемом 6TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_hdd_35_6tb".
- `url` (str): "------------------------GIGABYTE external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,126,185".

### `external_hdd_35 8TB`
**Описание**: Сценарий для сбора данных о внешних HDD 3.5" объемом 8TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_hdd_35_8tb".
- `url` (str): "------------------------GIGABYTE external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,126,186".

### `external_hdd_35 10TB`
**Описание**: Сценарий для сбора данных о внешних HDD 3.5" объемом 10TB от GIGABYTE.
**Параметры**:
- `brand` (str): "GIGABYTE".
- `name` (str): "external_hdd_35_10tb".
- `url` (str): "------------------------GIGABYTE external_hdd_35--------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "117,126,187".