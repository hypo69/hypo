# Документация для `morlevi_categories_storage_crucial.json`

## Обзор
Файл `morlevi_categories_storage_crucial.json` содержит JSON-структуру, описывающую различные категории товаров (накопителей) бренда CRUCIAL, используемые для парсинга. Каждая категория имеет уникальное имя, URL для парсинга, настройки активности и соответствие категориям в PrestaShop.

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание полей](#описание-полей)
4. [Примеры категорий](#примеры-категорий)

## Структура JSON
JSON-файл содержит один главный объект `scenarios`, внутри которого находятся объекты, представляющие собой отдельные категории товаров.

```json
{
  "scenarios": {
    "category_name_1": {
      "brand": "CRUCIAL",
      "name": "product_name_1",
      "url": "product_url_1",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "category_ids_1"
     },
    "category_name_2": {
        "brand": "CRUCIAL",
        "name": "product_name_2",
        "url": "product_url_2",
        "checkbox": false,
        "active": true,
         "condition":"new",
        "presta_categories": "category_ids_2"
    },
    ...
   }
}
```

## Описание полей

Каждый объект категории внутри `scenarios` имеет следующие поля:

- `brand` (str): Бренд товара, всегда "CRUCIAL" в данном файле.
- `name` (str): Внутреннее имя товара, используемое для идентификации.
- `url` (str): URL-адрес страницы товара на сайте поставщика (Morlevi). Если URL не требуется, может быть указана строка-заполнитель, например,  "------------------------CRUCIAL internal_hdd--------------------------".
- `checkbox` (bool): Флаг, указывающий, нужно ли использовать чекбокс для данной категории (всегда `false` в данном файле).
- `active` (bool): Флаг, указывающий, активна ли категория для парсинга (всегда `true` в данном файле).
- `condition` (str): Состояние товара, всегда "new" в данном файле.
- `presta_categories` (str): Строка, содержащая ID категорий в PrestaShop, разделенных запятыми.

## Примеры категорий

### Внутренние SSD SATA 3
```json
"internal_ssd_sata_3 120-128GB": {
    "brand": "CRUCIAL",
    "name": "internal_ssd_sata_3_128",
    "url": "---------------------------------------------------------------",
    "checkbox": false,
    "active": true,
    "condition":"new",
    "presta_categories": "117,118,134"
}
```
**Описание**: Описывает внутренний SSD SATA 3 объемом 120-128GB. Указывает URL-заглушку,  активность и соответствующие категории в PrestaShop.

### Внутренние SSD NVMe
```json
"internal_ssd_nvmi 240-256GB": {
    "brand": "CRUCIAL",
    "name": "internal_ssd_nvme_256",
    "url": "https://www.morlevi.co.il/Cat/51?p_315=19&p_175=823&sort=datafloat2%2Cprice&keyword=",
    "checkbox": false,
    "active": true,
    "condition":"new",
    "presta_categories": "117,119,141"
}
```
**Описание**: Описывает внутренний SSD NVMe объемом 240-256GB. Содержит URL-адрес для парсинга, флаг активности и список категорий PrestaShop.

### Внешние HDD 2.5"
```json
"external_hdd_25 1TB": {
    "brand": "CRUCIAL",
    "name": "external_hdd_25-1tb",
    "url": "------------------------CRUCIAL external_hdd_25--------------------------",
    "checkbox": false,
    "active": true,
    "condition":"new",
    "presta_categories": "117,125,184"
}
```
**Описание**: Описывает внешний HDD 2.5" объемом 1TB. URL-заглушка, флаг активности и категории PrestaShop.