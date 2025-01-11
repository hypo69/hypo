# Документация для файла `morlevi_categories_minipc_gigabyte.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [Сценарии](#сценарии)
        - [`GIGABYTE MINIPC I3 8-9th GEN`](#gigabyte-minipc-i3-8-9th-gen)
        - [`GIGABYTE MINIPC I3 10th GEN`](#gigabyte-minipc-i3-10th-gen)
        - [`GIGABYTE MINIPC I5 8-9th`](#gigabyte-minipc-i5-8-9th)
        - [`GIGABYTE MINIPC I5 10th`](#gigabyte-minipc-i5-10th)
        - [`GIGABYTE  MINIPC I7`](#gigabyte--minipc-i7)
        - [`GIGABYTE  MINIPC I9`](#gigabyte--minipc-i9)
        - [`GIGABYTE MINIPC AMD`](#gigabyte-minipc-amd)
        - [`GIGABYTE MINIPC Celeron`](#gigabyte-minipc-celeron)
        - [`GIGABYTE MINIPC Celeron 2`](#gigabyte-minipc-celeron-2)
        - [`GIGABYTE MINIPC Pentium`](#gigabyte-minipc-pentium)

## Обзор

Этот файл `morlevi_categories_minipc_gigabyte.json` содержит конфигурацию для парсинга и обработки данных о мини-ПК GIGABYTE с сайта morlevi.co.il. Он включает различные сценарии, каждый из которых определяет параметры для конкретных моделей мини-ПК, включая их URL-адреса, бренды, категории и активность.

## Структура JSON

Файл представляет собой JSON-объект со следующей структурой:
- **scenarios**: Объект, содержащий наборы сценариев для различных моделей мини-ПК GIGABYTE.

### Сценарии

Каждый сценарий представляет собой объект со следующими параметрами:
-   `brand`: (str) Бренд устройства, всегда "GIGABYTE".
-   `url`: (str) URL-адрес страницы товара на сайте morlevi.co.il.
-   `checkbox`: (bool)  Флаг для использования чекбокса.
-   `active`: (bool) Флаг активности сценария.
-   `condition`: (str) Состояние продукта, всегда "new".
-   `presta_categories`: (str) Список категорий PrestaShop.

#### `GIGABYTE MINIPC I3 8-9th GEN`

**Описание**: Сценарий для мини-ПК GIGABYTE с процессором Intel Core i3 8-го и 9-го поколения.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=1895&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,160"

#### `GIGABYTE MINIPC I3 10th GEN`

**Описание**: Сценарий для мини-ПК GIGABYTE с процессором Intel Core i3 10-го поколения.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3447&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,160"

#### `GIGABYTE MINIPC I5 8-9th`

**Описание**: Сценарий для мини-ПК GIGABYTE с процессором Intel Core i5 8-го и 9-го поколения.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "--------------------------GIGABYTE MINIPC I5 8-9th-------------------------"
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,161"

#### `GIGABYTE MINIPC I5 10th`

**Описание**: Сценарий для мини-ПК GIGABYTE с процессором Intel Core i5 10-го поколения.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3500&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,161"

#### `GIGABYTE  MINIPC I7`

**Описание**: Сценарий для мини-ПК GIGABYTE с процессором Intel Core i7.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3501&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,162"

#### `GIGABYTE  MINIPC I9`

**Описание**: Сценарий для мини-ПК GIGABYTE с процессором Intel Core i9.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "-------------GIGABYTE  MINIPC I9---------------- "
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,530"

#### `GIGABYTE MINIPC AMD`

**Описание**: Сценарий для мини-ПК GIGABYTE с процессором AMD.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "-------------GIGABYTE MINIPC AMD---------------- "
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,531"

#### `GIGABYTE MINIPC Celeron`

**Описание**: Сценарий для мини-ПК GIGABYTE с процессором Celeron.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3371&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,532"

#### `GIGABYTE MINIPC Celeron 2`

**Описание**: Альтернативный сценарий для мини-ПК GIGABYTE с процессором Celeron.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3133&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,532"

#### `GIGABYTE MINIPC Pentium`

**Описание**: Сценарий для мини-ПК GIGABYTE с процессором Pentium.

**Параметры**:
-   `brand`: "GIGABYTE"
-   `url`: "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3133&sort=datafloat2%2Cprice&keyword="
-   `checkbox`: false
-   `active`: true
-    `condition`: "new"
-   `presta_categories`: "159,532"