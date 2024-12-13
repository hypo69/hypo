# Документация для `morlevi_categories_mb_gigabyte.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
    - [GIGABYTE INTEL LGA1700 12 Gen Z690](#gigabyte-intel-lga1700-12-gen-z690)
    - [GIGABYTE INTEL LGA1700 12 Gen B660](#gigabyte-intel-lga1700-12-gen-b660)
    - [GIGABYTE INTEL LGA1700 12 H610](#gigabyte-intel-lga1700-12-h610)
    - [GIGABYTE INTEL LGA1200 H510](#gigabyte-intel-lga1200-h510)
    - [GIGABYTE INTEL LGA1200 B560](#gigabyte-intel-lga1200-b560)
    - [GIGABYTE INTEL LGA1200 Z590](#gigabyte-intel-lga1200-z590)
    - [GIGABYTE INTEL LGA1200 H410 GEN10](#gigabyte-intel-lga1200-h410-gen10)
    - [GIGABYTE INTEL LGA1200 H470 GEN10](#gigabyte-intel-lga1200-h470-gen10)
    - [GIGABYTE INTEL LGA2066 X299](#gigabyte-intel-lga2066-x299)
    - [GIGABYTE AMD AM4+ A520](#gigabyte-amd-am4-a520)
    - [GIGABYTE AMD AM4+ B450](#gigabyte-amd-am4-b450)
    - [GIGABYTE AMD AM4+ B550](#gigabyte-amd-am4-b550)
    - [GIGABYTE AMD AM4+ X570/X570S](#gigabyte-amd-am4-x570x570s)
    - [GIGABYTE AMD Threadripper TRX40](#gigabyte-amd-threadripper-trx40)
    - [GIGABYTE AMD Threadripper X399](#gigabyte-amd-threadripper-x399)
    - [GIGABYTE AMD Threadripper WRX80](#gigabyte-amd-threadripper-wrx80)

## Обзор

Файл `morlevi_categories_mb_gigabyte.json` содержит конфигурационные данные для определения категорий материнских плат Gigabyte на сайте Morlevi. Он определяет соответствие между названиями категорий на сайте Morlevi и категориями в PrestaShop.

## Структура файла

Файл представляет собой JSON-объект, содержащий единственный ключ `scenarios`, значением которого является объект, описывающий различные сценарии для материнских плат Gigabyte. Каждый сценарий имеет следующие ключи:

-   `brand`: Строка, представляющая бренд материнской платы. В данном случае всегда `GIGABYTE`.
-   `url`: Строка, представляющая URL-адрес категории материнских плат на сайте Morlevi.
-   `checkbox`: Логическое значение, определяющее, отображается ли чекбокс для этой категории. Всегда `false`.
-   `active`: Логическое значение, указывающее, активна ли категория. Всегда `true`.
-   `condition`: Строка, определяющая состояние товара. Всегда `new`.
-   `presta_categories`: Объект, содержащий информацию о соответствии с категориями в PrestaShop.
    -   `template`: Объект, содержащий соответствие между ключом `gigabyte` и категорией PrestaShop.
-   `price_rule`: Целое число, определяющее правило ценообразования для этой категории. Присутствует не во всех сценариях.

## Сценарии

### `GIGABYTE INTEL LGA1700 12 Gen Z690`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом Intel LGA1700 и чипсетом Z690.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/378`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "Intel Z690" }`
-   `price_rule`: `1`

### `GIGABYTE INTEL LGA1700 12 Gen B660`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом Intel LGA1700 и чипсетом B660.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/388`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "Intel B660" }`

### `GIGABYTE INTEL LGA1700 12 H610`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом Intel LGA1700 и чипсетом H610.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/389`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "Intel H610" }`

### `GIGABYTE INTEL LGA1200 H510`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом Intel LGA1200 и чипсетом H510.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/364`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "Intel H610" }`

### `GIGABYTE INTEL LGA1200 B560`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом Intel LGA1200 и чипсетом B560.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/365`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-    `presta_categories`:
    -   `template`: `{ "gigabyte": "Intel B560" }`

### `GIGABYTE INTEL LGA1200 Z590`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом Intel LGA1200 и чипсетом Z590.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/360`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-    `presta_categories`:
    -   `template`: `{ "gigabyte": "Intel B560" }`

### `GIGABYTE INTEL LGA1200 H410 GEN10`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом Intel LGA1200 и чипсетом H410.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/343`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "Intel H410" }`

### `GIGABYTE INTEL LGA1200 H470 GEN10`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом Intel LGA1200 и чипсетом H470.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/343`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "Intel H470" }`

### `GIGABYTE INTEL LGA2066 X299`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом Intel LGA2066 и чипсетом X299.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/28?p_95=411`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "Intel X299" }`

### `GIGABYTE AMD AM4+ A520`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом AMD AM4+ и чипсетом A520.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/350`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "AMD A520" }`

### `GIGABYTE AMD AM4+ B450`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом AMD AM4+ и чипсетом B450.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/311`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "AMD B450" }`

### `GIGABYTE AMD AM4+ B550`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом AMD AM4+ и чипсетом B550.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/340`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "AMD B550" }`

### `GIGABYTE AMD AM4+ X570/X570S`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом AMD AM4+ и чипсетом X570/X570S.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/22?p_95=4022&p_95=3225`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "AMD X570" }`

### `GIGABYTE AMD Threadripper TRX40`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом AMD Threadripper и чипсетом TRX40.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/349`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "AMD TRX40" }`

### `GIGABYTE AMD Threadripper X399`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом AMD Threadripper и чипсетом X399.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/353`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "AMD X399" }`

### `GIGABYTE AMD Threadripper WRX80`

**Описание**: Конфигурация для материнских плат Gigabyte с сокетом AMD Threadripper и чипсетом WRX80.

**Параметры**:

-   `brand`: `GIGABYTE`
-   `url`: `https://www.morlevi.co.il/Cat/366`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `new`
-   `presta_categories`:
    -   `template`: `{ "gigabyte": "AMD WRX80" }`