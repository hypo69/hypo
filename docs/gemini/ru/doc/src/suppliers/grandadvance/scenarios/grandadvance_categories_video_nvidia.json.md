# Документация для `grandadvance_categories_video_nvidia.json`

## Обзор

Файл `grandadvance_categories_video_nvidia.json` содержит JSON-объект с конфигурацией для категорий видеокарт NVIDIA от поставщика Grand Advance. Каждая запись представляет собой бренд видеокарт с настройками для сбора данных.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [MSI](#msi)
  - [GIGABYTE](#gigabyte)
  - [PNY](#pny)

## Структура JSON

### MSI

**Описание**: Конфигурация для видеокарт MSI.

**Свойства**:
- `brand` (str): Название бренда "MSI".
- `url` (str): URL для получения списка товаров MSI на сайте Grand Advance.
- `checkbox` (bool): Флаг, указывающий, выбран ли этот бренд.
- `active` (bool): Флаг, указывающий, является ли этот бренд активным.
- `condition` (str): Состояние товара (в данном случае "new").
- `presta_categories` (str): Идентификаторы категорий PrestaShop, к которым относятся товары этого бренда.

**Пример**:
```json
{
    "brand": "MSI",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=69",
    "checkbox": false,
    "active": true,
    "condition":"new",
    "presta_categories": "108,109"
}
```

### GIGABYTE

**Описание**: Конфигурация для видеокарт GIGABYTE.

**Свойства**:
- `brand` (str): Название бренда "GIGABYTE".
- `url` (str): URL для получения списка товаров GIGABYTE на сайте Grand Advance.
- `checkbox` (bool): Флаг, указывающий, выбран ли этот бренд.
- `active` (bool): Флаг, указывающий, является ли этот бренд активным.
- `condition` (str): Состояние товара (в данном случае "new").
- `presta_categories` (str): Идентификаторы категорий PrestaShop, к которым относятся товары этого бренда.

**Пример**:
```json
{
    "brand": "GIGABYTE",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=25",
    "checkbox": false,
    "active": true,
    "condition":"new",
    "presta_categories": "108,109"
}
```

### PNY

**Описание**: Конфигурация для видеокарт PNY.

**Свойства**:
- `brand` (str): Название бренда "PNY".
- `url` (str): URL для получения списка товаров PNY на сайте Grand Advance.
- `checkbox` (bool): Флаг, указывающий, выбран ли этот бренд.
- `active` (bool): Флаг, указывающий, является ли этот бренд активным.
- `condition` (str): Состояние товара (в данном случае "new").
- `presta_categories` (str): Идентификаторы категорий PrestaShop, к которым относятся товары этого бренда.

**Пример**:
```json
{
    "brand": "PNY",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=27",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "108,111"
}
```