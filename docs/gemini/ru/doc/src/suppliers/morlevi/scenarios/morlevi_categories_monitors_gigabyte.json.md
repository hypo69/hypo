# Документация для `morlevi_categories_monitors_gigabyte.json`

## Обзор

Этот файл содержит JSON-конфигурацию сценариев для парсинга мониторов бренда GIGABYTE с веб-сайта поставщика Morlevi. Каждый сценарий включает информацию о URL, чекбоксе, статусе активности и условиях, а также список категорий PrestaShop.

## Содержание

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
    *   [Ключ `scenarios`](#ключ-scenarios)
3.  [Сценарии](#сценарии)
    *   [GIGABYTE 22](#gigabyte-22)
    *   [GIGABYTE 24-25](#gigabyte-24-25)
    *   [GIGABYTE 27-29](#gigabyte-27-29)
    *   [GIGABYTE 32](#gigabyte-32)
    *   [GIGABYTE 34](#gigabyte-34)
    *   [GIGABYTE 49](#gigabyte-49)

## Структура JSON

JSON-файл состоит из одного основного ключа `scenarios`, содержащего в себе объекты, описывающие отдельные сценарии парсинга.

### Ключ `scenarios`
  Представляет собой словарь, где каждый ключ - это название сценария, а значение - это словарь с настройками для этого сценария.

## Сценарии

Каждый сценарий представляет собой словарь со следующими ключами:

-   `brand` (str): Название бренда монитора.
-   `url` (str): URL для парсинга.
-   `checkbox` (bool): Значение чекбокса.
-  `active` (bool): Статус активности сценария.
- `condition` (str): Условие товара (в данном случае `new`).
- `presta_categories` (str): Список категорий PrestaShop, разделенных запятыми.

### GIGABYTE 22

   **Описание**: Сценарий для парсинга мониторов GIGABYTE с диагональю 22 дюйма.

   **Параметры**:
   - `brand` (str): "GIGABYTE"
   - `url` (str): "----------------------------------GIGABYTE 22---------------------------------------"
   - `checkbox` (bool): false
   - `active` (bool): true
   - `condition` (str): "new"
   - `presta_categories` (str): "127,128,980"

### GIGABYTE 24-25

   **Описание**: Сценарий для парсинга мониторов GIGABYTE с диагональю 24-25 дюймов.

   **Параметры**:
   - `brand` (str): "GIGABYTE"
   - `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1807&sort=datafloat2%2Cprice&keyword="
   - `checkbox` (bool): false
   - `active` (bool): true
   - `condition` (str): "new"
   - `presta_categories` (str): "127,129,980"

### GIGABYTE 27-29

   **Описание**: Сценарий для парсинга мониторов GIGABYTE с диагональю 27-29 дюймов.

   **Параметры**:
   - `brand` (str): "GIGABYTE"
   - `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1808&sort=datafloat2%2Cprice&keyword="
   - `checkbox` (bool): false
   - `active` (bool): true
    - `condition` (str): "new"
   - `presta_categories` (str): "127,130,980"

### GIGABYTE 32

   **Описание**: Сценарий для парсинга мониторов GIGABYTE с диагональю 32 дюйма.

   **Параметры**:
   - `brand` (str): "GIGABYTE"
   - `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1809&sort=datafloat2%2Cprice&keyword="
   - `checkbox` (bool): false
   - `active` (bool): true
    - `condition` (str): "new"
   - `presta_categories` (str): "127,131,980"

### GIGABYTE 34

   **Описание**: Сценарий для парсинга мониторов GIGABYTE с диагональю 34 дюйма.

   **Параметры**:
   - `brand` (str): "GIGABYTE"
   - `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1810&sort=datafloat2%2Cprice&keyword="
   - `checkbox` (bool): false
   - `active` (bool): true
   - `condition` (str): "new"
   - `presta_categories` (str): "127,132,980"

### GIGABYTE 49

   **Описание**: Сценарий для парсинга мониторов GIGABYTE с диагональю 49 дюймов.

   **Параметры**:
   - `brand` (str): "GIGABYTE"
   - `url` (str): "-----------------------------  GIGABYTE 49 ---------------------------------"
   - `checkbox` (bool): false
   - `active` (bool): true
   - `condition` (str): "new"
   - `presta_categories` (str): "127,133,980"