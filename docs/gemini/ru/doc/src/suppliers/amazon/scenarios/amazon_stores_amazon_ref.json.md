# Документация для `amazon_stores_amazon_ref.json`

## Обзор

Данный JSON-файл содержит конфигурацию для парсинга товаров с сайта Amazon Renewed. Он определяет параметры магазина, а также сценарии для различных категорий товаров, включая URL-адреса, соответствие категориям PrestaShop и правила ценообразования.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура файла](#структура-файла)
    *   [store](#store)
    *   [scenarios](#scenarios)
        *   [Oculus](#oculus)
        *   [Macbook](#macbook)
        *   [Apple Watch](#apple-watch)
        *   [SAMSUNG WATCHES](#samsung-watches)
        *   [GARMIN WATCHES](#garmin-watches)
        *   [FITBIT WATCHES](#fitbit-watches)
    

## Структура файла

### `store`

**Описание**: Секция `store` содержит общую информацию о магазине на Amazon Renewed.

**Поля**:
- `store_id` (str): Уникальный идентификатор магазина.
- `supplier_id` (int): Идентификатор поставщика.
- `get store banners` (bool): Флаг для получения баннеров магазина.
- `description` (str): Описание магазина.
- `about` (str): Дополнительная информация о магазине (пустая строка).
- `url` (str): URL-адрес магазина на Amazon Renewed.
- `shop categories page` (str): URL-адрес страницы категорий магазина (пустая строка).
- `shop categories json file` (str): Имя файла JSON с категориями магазина (пустая строка).

### `scenarios`

**Описание**: Секция `scenarios` содержит конфигурации для различных категорий товаров, которые будут обрабатываться парсером.

#### `Oculus`

**Описание**: Конфигурация для категории товаров "Oculus".

**Поля**:
- `url` (str): URL-адрес категории (пустая строка).
- `active` (str): Статус сценария, в данном случае `skip`.
- `condition` (str): Состояние товара `new`.
- `presta_categories` (dict):  Соответствие категориям PrestaShop.
    - `template` (dict): Шаблон для сопоставления категорий.
        - `oculus` (str):  Соответствие категории PrestaShop "VIRTUAL RELITY GLASSES".
- `checkbox` (bool): Флаг (false).
- `price_rule` (int): Правило ценообразования (1).

#### `Macbook`

**Описание**: Конфигурация для категории товаров "Macbook".

**Поля**:
- `url` (str): URL-адрес категории на Amazon.
- `active` (bool):  Статус сценария (true).
- `condition` (str): Состояние товара `new`.
- `presta_categories` (dict):  Соответствие категориям PrestaShop.
    - `template` (dict): Шаблон для сопоставления категорий.
        - `apple` (str): Соответствие категории PrestaShop "MACBOOK".
- `checkbox` (bool): Флаг (false).
- `price_rule` (int): Правило ценообразования (1).

#### `Apple Watch`

**Описание**: Конфигурация для категории товаров "Apple Watch".

**Поля**:
- `brand` (str): Бренд товара "APPLE".
- `url` (str): URL-адрес категории на Amazon.
- `active` (bool):  Статус сценария (true).
- `condition` (str): Состояние товара `new`.
- `presta_categories` (dict):  Соответствие категориям PrestaShop.
    - `template` (dict): Шаблон для сопоставления категорий.
        - `apple` (str): Соответствие категории PrestaShop "WATCHES".
- `checkbox` (bool): Флаг (false).
- `price_rule` (int): Правило ценообразования (1).

#### `SAMSUNG WATCHES`

**Описание**: Конфигурация для категории товаров "SAMSUNG WATCHES".

**Поля**:
- `brand` (str): Бренд товара "SAMSUNG".
- `url` (str): URL-адрес категории на Amazon.
- `active` (bool):  Статус сценария (true).
- `condition` (str): Состояние товара `new`.
- `presta_categories` (dict):  Соответствие категориям PrestaShop.
    - `template` (dict): Шаблон для сопоставления категорий.
        - `samsung` (str): Соответствие категории PrestaShop "WATCHES".
- `checkbox` (bool): Флаг (false).
- `price_rule` (int): Правило ценообразования (1).

#### `GARMIN WATCHES`

**Описание**: Конфигурация для категории товаров "GARMIN WATCHES".

**Поля**:
- `brand` (str): Бренд товара "GARMIN".
- `url` (str): URL-адрес категории на Amazon.
- `active` (bool):  Статус сценария (true).
- `condition` (str): Состояние товара `new`.
- `presta_categories` (dict):  Соответствие категориям PrestaShop.
    - `template` (dict): Шаблон для сопоставления категорий.
        - `garmin` (str): Соответствие категории PrestaShop "WATCHES".
- `checkbox` (bool): Флаг (false).
- `price_rule` (int): Правило ценообразования (1).

#### `FITBIT WATCHES`

**Описание**: Конфигурация для категории товаров "FITBIT WATCHES".

**Поля**:
- `brand` (str): Бренд товара "FITBIT".
- `url` (str): URL-адрес категории на Amazon.
- `active` (bool):  Статус сценария (true).
- `condition` (str): Состояние товара `new`.
- `presta_categories` (dict):  Соответствие категориям PrestaShop.
    - `template` (dict): Шаблон для сопоставления категорий.
        - `fitbit` (str): Соответствие категории PrestaShop "WATCHES".
- `checkbox` (bool): Флаг (false).
- `price_rule` (int): Правило ценообразования (1).