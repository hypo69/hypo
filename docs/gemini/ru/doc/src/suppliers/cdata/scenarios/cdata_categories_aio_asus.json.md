# Документация для `cdata_categories_aio_asus.json`

## Обзор

Этот файл содержит JSON-конфигурацию для сбора данных о категориях All-In-One компьютеров ASUS.
Каждая запись в файле представляет собой сценарий сбора данных для конкретной конфигурации ASUS AIO, включая URL, параметры фильтрации и категории PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)

## Структура JSON

Файл представляет собой JSON-объект со следующим ключом:

- `"scenarios"`: Объект, содержащий различные сценарии сбора данных.

## Сценарии

Объект `"scenarios"` содержит пары ключ-значение, где ключ — это название сценария (например, `"ASUS 15.6 - Celeron"`), а значение — это объект, описывающий настройки этого сценария. Каждый сценарий имеет следующие поля:

-   `"brand"` (str): Марка производителя (в данном случае всегда "ASUS").
-   `"url"` (str): URL-адрес страницы с фильтрами для конкретной конфигурации. Может быть URL с сайта c-data или просто строка с описанием.
-   `"checkbox"` (bool): Флаг, указывающий, нужно ли использовать чекбокс (всегда `false`).
-   `"active"` (bool): Флаг, указывающий, активен ли сценарий (всегда `true`).
-   `"condition"` (str): Условие товара (всегда `"new"`).
-   `"presta_categories"` (str): Строка, содержащая идентификаторы категорий PrestaShop, разделенные запятыми.

### Примеры сценариев:

#### `ASUS 15.6 - Celeron`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 15.6 и процессором Celeron.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"https://reseller.c-data.co.il/asus-all-in-one#/specFilters=225m!#-!4663"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,519,45,986"`

#### `ASUS 21.5 - I3`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 21.5 и процессором I3.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"--------------AIO ASUS 21.5 - I3---------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,37,45,41"`

#### `ASUS 21.5 - I5`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 21.5 и процессором I5.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"--------------AIO AIO AIO ASUS 21.5 - I5---------------2"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,38,45,41"`

#### `ASUS 21.5 - I7`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 21.5 и процессором I7.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"---------------AIO ASUS 21.5 - I7---------------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,39,45,41"`

#### `ASUS 21.5 - I9`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 21.5 и процессором I9.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"----------------AIO ASUS 21.5 - I9------------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,301,41"`
   
   
#### `ASUS 21.5 amd`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 21.5 и процессором AMD.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"----------------AIO ASUS 21.5 amd----------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,41,302"`
   
   
#### `ASUS 23.5 I3`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 23.5 и процессором I3.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"----------------AIO ASUS 23.5 I3---------------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,37,45,42"`
    
#### `ASUS 23.5 I5`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 23.5 и процессором I5.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"----------------AIO ASUS 23.5 I5----------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,38,45,42"`
    
#### `ASUS 23.5 I7`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 23.5 и процессором I7.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"https://reseller.c-data.co.il/All-In-One#/specFilters=227!#-!4635!-#!225m!#-!5510&manFilters=10"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,42,39"`
    
#### `ASUS 23.5 I9`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 23.5 и процессором I9.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"----------------AIO ASUS 23.5 I9-------------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,42,301"`
    
#### `ASUS 23.5 amd`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 23.5 и процессором AMD.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"---------------AIO ASUS 23.5 amd---------------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,42,302"`

#### `ASUS 27 I3`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 27 и процессором I3.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"---------------AIO ASUS 27 I3-----------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,37,45,43"`

#### `ASUS 23,8 I3`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 23,8 и процессором I3.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"https://reseller.c-data.co.il/asus-all-in-one#/specFilters=225!#-!5510!-#!227m!#-!4633"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,37,42,45"`

#### `ASUS 23,8 I5`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 23,8 и процессором I5.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"https://reseller.c-data.co.il/asus-all-in-one#/specFilters=225!#-!5510!-#!227m!#-!4634"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,38,42,45"`
    
#### `ASUS 23,8 I7`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 23,8 и процессором I7.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"https://reseller.c-data.co.il/asus-all-in-one#/specFilters=225!#-!5510!-#!227m!#-!4635"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,39,42,45"`
    
#### `ASUS 27 I7`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 27 и процессором I7.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"https://reseller.c-data.co.il/All-In-One#/specFilters=227!#-!4635!-#!225m!#-!5512&manFilters=10"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,43,39"`

#### `ASUS 27 I9`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 27 и процессором I9.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"-------------AIO ASUS 27 I9-------------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,43,301"`
    
#### `ASUS 27 amd`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 27 и процессором AMD.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"-------------AIO ASUS 27 amd-----------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,43,302"`

#### `ASUS 34 I3`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 34 и процессором I3.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"-------------AIO ASUS 34 I3------------------0"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,37,45,227,37"`

#### `ASUS 34 I5`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 34 и процессором I5.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"--------------AIO ASUS 34 I5------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,38,45,227,38"`

#### `ASUS 34 I7`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 34 и процессором I7.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"--------------AIO ASUS 34 I7------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,227,39"`
    
#### `ASUS 34 I9`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 34 и процессором I9.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"-------------AIO ASUS 34 I9-------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,227,301"`

#### `ASUS 34 amd`

**Описание**: Сценарий для сбора данных о All-In-One ASUS с диагональю 34 и процессором AMD.
    
**Параметры**:
    - `"brand"`: `"ASUS"`
    - `"url"`: `"------------AIO ASUS 34 amd-------------"`
    - `"checkbox"`: `false`
    - `"active"`: `true`
    - `"condition"`: `"new"`
    - `"presta_categories"`: `"35,45,227,302"`

Этот документ представляет собой структуру конфигурации для сбора данных о All-In-One компьютерах ASUS, каждый сценарий определяет конкретную модель и параметры для её сбора.