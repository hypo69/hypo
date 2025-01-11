# Документация для `ksp_categories_tablets_ipads.json`

## Обзор

Файл `ksp_categories_tablets_ipads.json` содержит JSON-структуру, описывающую сценарии для парсинга категорий планшетов iPad с сайта KSP. Каждый сценарий включает информацию о бренде, URL-адресе, статусе активности и сопоставлении с категориями PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
  - [Сценарии](#сценарии)
    - [iPad Mini 2021](#ipad-mini-2021)
    - [iPad 10.2 2021](#ipad-102-2021)
    - [iPad Air 10.9 2020](#ipad-air-109-2020)
    - [iPad Air 10.9 2022](#ipad-air-109-2022)
    - [iPad Pro 11 2021](#ipad-pro-11-2021)
    - [iPad Pro 12.9 2021](#ipad-pro-129-2021)

## Структура файла

Файл состоит из одного объекта JSON с ключом `scenarios`, который содержит вложенный объект. Ключами этого вложенного объекта являются названия моделей iPad, а значениями - объекты с данными о конкретных сценариях.

### Сценарии

Каждый сценарий представлен объектом со следующими полями:

-   `brand` (str): Бренд устройства, в данном случае всегда "APPLE".
-   `url` (str): URL-адрес страницы с товарами на сайте KSP.
-   `checkbox` (bool): Флаг, указывающий на необходимость использования чекбокса (всегда `false`).
-   `active` (bool): Флаг, определяющий активность сценария (всегда `true`).
-   `condition` (str): Состояние товара, в данном случае всегда "new".
-   `presta_categories` (dict): Объект, содержащий сопоставление идентификаторов категорий PrestaShop с их названиями и описаниями.

#### `iPad Mini 2021`

**Описание**: Сценарий для парсинга категории iPad Mini 2021.

**Параметры**:
-   `brand`: "APPLE"
-   `url`: `"https://ksp.co.il/web/cat/270..245..28582"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    -   `"3508"`: `"7 - 8 INCH"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"3227"`: `"TABLETS"`
    -   `"3514"`: `"iPad Mini 2021"`
    -   `"2243"`: `"APPLE"`
    -   `"2686"`: `"Ipad"`
    -   `"2687"`: `"iPad Mini 2021"`

#### `iPad 10.2 2021`

**Описание**: Сценарий для парсинга категории iPad 10.2 2021.

**Параметры**:
-   `brand`: "APPLE"
-   `url`: `"https://ksp.co.il/web/cat/270..245..28582"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    -   `"3509"`: `"9 - 11 inch"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"3227"`: `"TABLETS"`
    -   `"3517"`: `"iPad 10.2 2021"`
    -   `"2243"`: `"APPLE"`
    -   `"2686"`: `"Ipad"`
    -   `"2689"`: `"iPad 10.2 2021"`

#### `iPad Air 10.9 2020`

**Описание**: Сценарий для парсинга категории iPad Air 10.9 2020.

**Параметры**:
-   `brand`: "APPLE"
-   `url`: `"https://ksp.co.il/web/cat/270..245..17058"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    -   `"3509"`: `"9 - 11 inch"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"3227"`: `"TABLETS"`
    -    `"3515"`: `"iPad 10.2 2021"`
    -   `"2243"`: `"APPLE"`
    -   `"2686"`: `"Ipad"`
    -   `"2688"`: `"iPad Air 10.9 2020"`

#### `iPad Air 10.9 2022`

**Описание**: Сценарий для парсинга категории iPad Air 10.9 2022.

**Параметры**:
-   `brand`: "APPLE"
-   `url`: `"https://ksp.co.il/web/cat/270..245..36222"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    -   `"3509"`: `"9 - 11 inch"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"3227"`: `"TABLETS"`
    -   `"3516"`: `"iPad Air 10.9 2022"`
    -   `"2243"`: `"APPLE"`
    -   `"2686"`: `"Ipad"`
    -   `"3519"`: `"iPad Air 10.9 2022"`

#### `iPad Pro 11 2021`

**Описание**: Сценарий для парсинга категории iPad Pro 11 2021.

**Параметры**:
-   `brand`: "APPLE"
-   `url`: `"https://ksp.co.il/web/cat/270..245..24377"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    -   `"3509"`: `"9 - 11 inch"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"3227"`: `"TABLETS"`
    -   `"3518"`: `"iPad Pro 11 2021"`
    -   `"2243"`: `"APPLE"`
    -   `"2686"`: `"Ipad"`
    -   `"2690"`: `"iPad Pro 11 2021"`

#### `iPad Pro 12.9 2021`

**Описание**: Сценарий для парсинга категории iPad Pro 12.9 2021.

**Параметры**:
-   `brand`: "APPLE"
-   `url`: `"https://ksp.co.il/web/cat/270..245..36222"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    -   `"3509"`: `"9 - 11 inch"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"3227"`: `"TABLETS"`
    -    `"3568"`: `"iPad Pro 12.9 2021"`
    -   `"2243"`: `"APPLE"`
    -   `"2686"`: `"Ipad"`
    -   `"2690"`: `"iPad Pro 11 2021"`