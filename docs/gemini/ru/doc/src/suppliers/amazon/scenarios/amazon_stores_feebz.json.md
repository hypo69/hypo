# Документация для `amazon_stores_feebz.json`

## Обзор

Данный файл в формате JSON содержит конфигурацию для парсинга магазина "FEEBZ" на Amazon, включая информацию о магазине и сценарии парсинга для различных категорий товаров.

## Оглавление

- [store](#store)
- [scenarios](#scenarios)
  - [ZenBook](#zenbook)
  - [ROG Gaming](#rog-gaming)
  - [TUF Gaming](#tuf-gaming)
  - [VIVOBook](#vivobook)
  - [ChromeBook](#chromebook)
  - [Asus ProArt Studiobook](#asus-proart-studiobook)
  - [Asus ProArt Desktops](#asus-proart-desktops)

## store

### Описание
Секция store содержит основные параметры магазина "FEEBZ" на Amazon.

### Параметры
*   `store_id` (str): Уникальный идентификатор магазина на Amazon.
*   `supplier_id` (int): Идентификатор поставщика.
*   `get store banners` (bool): Флаг, указывающий, нужно ли получать баннеры магазина.
*  `description` (str): Описание магазина.
*  `about` (str): Дополнительная информация о магазине.
*   `url` (str): URL-адрес страницы магазина на Amazon.
*   `shop categories page` (str): URL-адрес страницы с категориями магазина. На данный момент пустая строка.
*   `shop categories json file` (str): Путь к файлу JSON с категориями магазина. На данный момент пустая строка.

## scenarios

### Описание
Секция `scenarios` содержит набор сценариев для парсинга различных категорий товаров в магазине.

### ZenBook
#### Описание
Сценарий для парсинга товаров категории ZenBook.

#### Параметры
*   `url` (str): URL-адрес страницы категории на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*  `condition` (str): Состояние товара (новый).
*   `presta_categories` (dict): Словарь соответствия категорий PrestaShop и Amazon.
*    `checkbox` (bool): Флаг для использования чекбоксов.
*   `price_rule` (int): Правило ценообразования.

### ROG Gaming
#### Описание
Сценарий для парсинга товаров категории ROG Gaming.

#### Параметры
*   `url` (str): URL-адрес страницы категории на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*  `condition` (str): Состояние товара (новый).
*   `presta_categories` (dict): Словарь соответствия категорий PrestaShop и Amazon.
*    `checkbox` (bool): Флаг для использования чекбоксов.
*   `price_rule` (int): Правило ценообразования.

### TUF Gaming
#### Описание
Сценарий для парсинга товаров категории TUF Gaming.

#### Параметры
*   `url` (str): URL-адрес страницы категории на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*  `condition` (str): Состояние товара (новый).
*   `presta_categories` (dict): Словарь соответствия категорий PrestaShop и Amazon.
*    `checkbox` (bool): Флаг для использования чекбоксов.
*   `price_rule` (int): Правило ценообразования.

### VIVOBook
#### Описание
Сценарий для парсинга товаров категории VIVOBook.

#### Параметры
*   `url` (str): URL-адрес страницы категории на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*  `condition` (str): Состояние товара (новый).
*   `presta_categories` (dict): Словарь соответствия категорий PrestaShop и Amazon.
*    `checkbox` (bool): Флаг для использования чекбоксов.
*   `price_rule` (int): Правило ценообразования.

### ChromeBook
#### Описание
Сценарий для парсинга товаров категории ChromeBook.

#### Параметры
*   `url` (str): URL-адрес страницы категории на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*  `condition` (str): Состояние товара (новый).
*   `presta_categories` (dict): Словарь соответствия категорий PrestaShop и Amazon.
*    `checkbox` (bool): Флаг для использования чекбоксов.
*   `price_rule` (int): Правило ценообразования.

### Asus ProArt Studiobook
#### Описание
Сценарий для парсинга товаров категории Asus ProArt Studiobook.

#### Параметры
*   `url` (str): URL-адрес страницы категории на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*  `condition` (str): Состояние товара (новый).
*   `presta_categories` (dict): Словарь соответствия категорий PrestaShop и Amazon.
*    `checkbox` (bool): Флаг для использования чекбоксов.
*   `price_rule` (int): Правило ценообразования.
### Asus ProArt Desktops
#### Описание
Сценарий для парсинга товаров категории Asus ProArt Desktops.

#### Параметры
*   `url` (str): URL-адрес страницы категории на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*  `condition` (str): Состояние товара (новый).
*   `presta_categories` (dict): Словарь соответствия категорий PrestaShop и Amazon.
*    `checkbox` (bool): Флаг для использования чекбоксов.
*   `price_rule` (int): Правило ценообразования.