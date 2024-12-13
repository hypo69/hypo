# Документация для `ksp_categories_headphones_msi.json`

## Обзор

Этот файл содержит JSON-конфигурацию сценариев для парсинга категорий наушников бренда MSI с сайта KSP. Включает сценарии для наушников типа "In-ear Bud" и "Overear", определяя соответствующие URL, условия, и шаблоны категорий для PrestaShop.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
   - [In-ear Bud](#in-ear-bud)
   - [Overear](#overear)
  
## Структура JSON

JSON-файл имеет следующую структуру:

-   `scenarios`: Основной объект, содержащий все сценарии.
    -   Каждый сценарий представляет собой объект, ключом которого является название сценария.
    -   Внутри каждого сценария находятся параметры:
        -   `brand` (str): Бренд продукта.
        -   `url` (str): URL-адрес категории на сайте KSP.
        -   `checkbox` (bool): Флаг для включения/выключения сценария (здесь `false`).
        -   `active` (bool): Флаг для активации сценария (здесь `true`).
        - `condition` (str): Состояние продукта.
        -  `presta_categories` (dict): Объект, содержащий шаблоны для категорий PrestaShop.
            -`template`(dict): Объект, содержащий шаблоны.
               -  ключ "msi"(str): шаблон для PrestaShop

## Сценарии

### `In-ear Bud`

**Описание**: Сценарий для парсинга наушников типа "In-ear Bud" бренда MSI.

**Параметры**:

-   `brand` (str): `MSI`.
-   `url` (str): `https://ksp.co.il/web/cat/242..47..1250`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-  `condition` (str): `new`.
-   `presta_categories` (dict): 
    - `template` (dict):
        - `msi` (str): `HEADPHONES BT In-ear Bud`.

### `Overear`

**Описание**: Сценарий для парсинга наушников типа "Overear" бренда MSI.

**Параметры**:

-   `brand` (str): `MSI`.
-   `url` (str): `https://ksp.co.il/web/cat/242..1252..47`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-  `condition` (str): `new`.
-   `presta_categories` (dict):
    - `template` (dict):
        - `msi` (str): `HEADPHONES Overear`.