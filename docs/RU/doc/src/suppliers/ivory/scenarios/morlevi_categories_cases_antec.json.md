# Документация для `morlevi_categories_cases_antec.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Раздел `store`](#раздел-store)
4. [Раздел `scenarios`](#раздел-scenarios)
    - [Сценарий `ANTEC MID TOWER`](#сценарий-antec-mid-tower)
    - [Сценарий `ANTEC FULL TOWER`](#сценарий-antec-full-tower)
    - [Сценарий `ANTEC MINI TOWER`](#сценарий-antec-mini-tower)
    - [Сценарий `ANTEC gaming MID TOWER`](#сценарий-antec-gaming-mid-tower)
    - [Сценарий `ANTEC gaming full tower`](#сценарий-antec-gaming-full-tower)
    - [Сценарий `ANTEC mini itx`](#сценарий-antec-mini-itx)

## Обзор

Файл `morlevi_categories_cases_antec.json` содержит конфигурационные данные для парсинга и обработки категорий товаров, связанных с компьютерными корпусами бренда Antec на сайте morlevi.co.il. Он определяет основные настройки магазина и сценарии для различных типов корпусов Antec.

## Структура файла

Файл представляет собой JSON-объект с двумя основными разделами: `store` и `scenarios`.

## Раздел `store`

Раздел `store` содержит общие сведения о магазине и параметрах парсинга.

-   `description`: (string) Описание категории товаров, в данном случае "Antec Computer Cases".
-   `about`: (string) Дополнительная информация о категории (в данном случае пустая строка).
-   `category ID on site`: (string) Идентификатор категории на сайте (в данном случае пустая строка).
-   `category ID in PRESTAHOP db`: (string) Идентификатор категории в базе данных PrestaShop (в данном случае пустая строка).
-   `brand`: (list) Список брендов, для которых производится парсинг, в данном случае `["ANTEC"]`.
-   `url`: (string) URL-адрес страницы каталога товаров на сайте morlevi.co.il.
-   `get store banners`: (boolean) Указывает, нужно ли собирать баннеры магазина.

## Раздел `scenarios`

Раздел `scenarios` содержит набор сценариев для обработки конкретных категорий товаров Antec. Каждый сценарий представляет собой объект со следующими полями:

-   `brand`: (string) Бренд товара.
-   `template`: (string) Шаблон для парсинга (может быть пустой строкой).
-   `url`: (string) URL-адрес страницы с товарами.
-   `checkbox`: (boolean) Флаг для использования чекбоксов (в данном случае всегда `false`).
-   `active`: (boolean) Флаг для активации сценария (в данном случае всегда `true`).
-   `condition`: (string) Состояние товара (в данном случае всегда `"new"`).
-   `presta_categories`: (object) Объект с настройками категорий PrestaShop.

    -   `template`: (object) Объект с шаблонами категорий, где ключ — это внутренний идентификатор бренда (например, "antec"), а значение — название категории в PrestaShop.

### Сценарий `ANTEC MID TOWER`

**Описание**: Сценарий для парсинга корпусов Antec типа Mid Tower.

**Параметры:**
-   `brand`: "ANTEC"
-   `template`: ""
-   `url`: "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=540&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-   `condition`: "new"
-   `presta_categories`:
    -   `template`:
        -   `antec`: "MID TOWER"

### Сценарий `ANTEC FULL TOWER`

**Описание**: Сценарий для парсинга корпусов Antec типа Full Tower.

**Параметры:**
-   `brand`: "ANTEC"
-   `url`: "----------------------------ANTEC FULL TOWER--------------------------------"
-   `checkbox`: false
-   `active`: true
-   `condition`: "new"
-   `presta_categories`:
    -   `template`:
        -   `antec`: "FULL TOWER"

### Сценарий `ANTEC MINI TOWER`

**Описание**: Сценарий для парсинга корпусов Antec типа Mini Tower.

**Параметры:**
-   `brand`: "ANTEC"
-   `template`: ""
-   `url`: "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=542&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-   `condition`: "new"
-   `presta_categories`:
    -   `template`:
        -   `antec`: "MINI TOWER"

### Сценарий `ANTEC gaming MID TOWER`

**Описание**: Сценарий для парсинга игровых корпусов Antec типа Mid Tower.

**Параметры:**
-   `brand`: "ANTEC"
-   `template`: ""
-  `url`: "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=545&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-   `condition`: "new"
-   `presta_categories`:
    -   `template`:
        -   `antec`: "MINI TOWER"

### Сценарий `ANTEC gaming full tower`

**Описание**: Сценарий для парсинга игровых корпусов Antec типа Full Tower.

**Параметры:**
-   `brand`: "ANTEC"
-   `template`: ""
-   `url`: "----------------------------ANTEC gaming full TOWER--------------------------------"
-   `checkbox`: false
-   `active`: true
-   `condition`: "new"
-   `presta_categories`:
    -   `template`:
        -   `antec`: "MINI TOWER"

### Сценарий `ANTEC mini itx`

**Описание**: Сценарий для парсинга корпусов Antec типа Mini ITX.

**Параметры:**
-   `brand`: "ANTEC"
-   `template`: ""
-   `url`: "----------------------------ANTEC mini itxR--------------------------------"
-   `checkbox`: false
-   `active`: true
-   `condition`: "new"
-   `presta_categories`:
    -   `template`:
        -   `antec`: "MINI ITX"