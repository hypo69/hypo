# Документация для `morlevi_categories_cases_antec.json`

## Обзор

Данный файл `morlevi_categories_cases_antec.json` содержит конфигурационные данные для сбора информации о категориях компьютерных корпусов Antec с сайта morlevi.co.il. Файл определяет настройки магазина, а также различные сценарии для определенных типов корпусов Antec.

## Содержание

1.  [Описание магазина](#описание-магазина)
2.  [Сценарии](#сценарии)
    - [ANTEC MID TOWER](#antec-mid-tower)
    - [ANTEC FULL TOWER](#antec-full-tower)
    - [ANTEC MINI TOWER](#antec-mini-tower)
    - [ANTEC gaming MID TOWER](#antec-gaming-mid-tower)
    - [ANTEC gaming full tower](#antec-gaming-full-tower)
    - [ANTEC mini itx](#antec-mini-itx)

## Описание магазина

Данный раздел описывает общие настройки для магазина, с которого производится сбор данных.

**Описание**: Конфигурация магазина для компьютерных корпусов Antec.

**Параметры**:

-   `description` (str): Описание категории товаров магазина - "Antec Computer Cases".
-   `about` (str): Пустая строка.
-   `category ID on site` (str): Пустая строка, ID категории на сайте не указан.
-   `category ID in PRESTAHOP db` (str): Пустая строка, ID категории в БД PrestaShop не указан.
-   `brand` (list[str]): Список брендов, в данном случае только "ANTEC".
-   `url` (str): URL-адрес страницы категории на сайте "https://www.morlevi.co.il/Cat/95?p_315=12&sort=datafloat2%2Cprice&keyword=".
-   `get store banners` (bool): Указывает, нужно ли получать баннеры магазина - `true`.

## Сценарии

Данный раздел описывает различные сценарии для сбора данных, связанные с различными типами компьютерных корпусов Antec.

### ANTEC MID TOWER

**Описание**: Сценарий для сбора данных о корпусах Antec типа MID TOWER.

**Параметры**:
-   `brand` (str): Бренд - "ANTEC".
-   `template` (str): Пустая строка, шаблон не определен.
-   `url` (str): URL-адрес для сбора данных "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=540&sort=datafloat2%2Cprice&keyword=".
-   `checkbox` (bool): Флаг чекбокса - `false`.
-   `active` (bool): Флаг активности сценария - `true`.
-  `condition` (str): Состояние товара - "new".
-   `presta_categories` (dict): Категории PrestaShop, в которых размещаются товары.
    -   `template` (dict): Шаблон категорий, где "antec" соответствует "MID TOWER".

### ANTEC FULL TOWER

**Описание**: Сценарий для сбора данных о корпусах Antec типа FULL TOWER.

**Параметры**:
-   `brand` (str): Бренд - "ANTEC".
-  `url` (str): URL-адрес, указанный как "----------------------------ANTEC FULL TOWER--------------------------------"
-   `checkbox` (bool): Флаг чекбокса - `false`.
-   `active` (bool): Флаг активности сценария - `true`.
-   `condition` (str): Состояние товара - "new".
-   `presta_categories` (dict): Категории PrestaShop, в которых размещаются товары.
    -   `template` (dict): Шаблон категорий, где "antec" соответствует "FULL TOWER".

### ANTEC MINI TOWER

**Описание**: Сценарий для сбора данных о корпусах Antec типа MINI TOWER.

**Параметры**:
-   `brand` (str): Бренд - "ANTEC".
-   `template` (str): Пустая строка, шаблон не определен.
-   `url` (str): URL-адрес для сбора данных "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=542&sort=datafloat2%2Cprice&keyword=".
-   `checkbox` (bool): Флаг чекбокса - `false`.
-   `active` (bool): Флаг активности сценария - `true`.
-  `condition` (str): Состояние товара - "new".
-   `presta_categories` (dict): Категории PrestaShop, в которых размещаются товары.
    -   `template` (dict): Шаблон категорий, где "antec" соответствует "MINI TOWER".

### ANTEC gaming MID TOWER

**Описание**: Сценарий для сбора данных о игровых корпусах Antec типа MID TOWER.

**Параметры**:
-   `brand` (str): Бренд - "ANTEC".
-   `template` (str): Пустая строка, шаблон не определен.
-   `url` (str): URL-адрес для сбора данных "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=545&sort=datafloat2%2Cprice&keyword=".
-   `checkbox` (bool): Флаг чекбокса - `false`.
-   `active` (bool): Флаг активности сценария - `true`.
-   `condition` (str): Состояние товара - "new".
-   `presta_categories` (dict): Категории PrestaShop, в которых размещаются товары.
    -   `template` (dict): Шаблон категорий, где "antec" соответствует "MINI TOWER".

### ANTEC gaming full tower

**Описание**: Сценарий для сбора данных о игровых корпусах Antec типа FULL TOWER.

**Параметры**:
-   `brand` (str): Бренд - "ANTEC".
-  `template` (str): Пустая строка, шаблон не определен.
-  `url` (str): URL-адрес, указанный как "----------------------------ANTEC gaming full TOWER--------------------------------"
-   `checkbox` (bool): Флаг чекбокса - `false`.
-   `active` (bool): Флаг активности сценария - `true`.
-  `condition` (str): Состояние товара - "new".
-   `presta_categories` (dict): Категории PrestaShop, в которых размещаются товары.
    -   `template` (dict): Шаблон категорий, где "antec" соответствует "MINI TOWER".

### ANTEC mini itx

**Описание**: Сценарий для сбора данных о корпусах Antec типа MINI ITX.

**Параметры**:
-   `brand` (str): Бренд - "ANTEC".
-   `template` (str): Пустая строка, шаблон не определен.
-   `url` (str): URL-адрес, указанный как "----------------------------ANTEC mini itxR--------------------------------"
-   `checkbox` (bool): Флаг чекбокса - `false`.
-   `active` (bool): Флаг активности сценария - `true`.
-  `condition` (str): Состояние товара - "new".
-   `presta_categories` (dict): Категории PrestaShop, в которых размещаются товары.
    -   `template` (dict): Шаблон категорий, где "antec" соответствует "MINI ITX".