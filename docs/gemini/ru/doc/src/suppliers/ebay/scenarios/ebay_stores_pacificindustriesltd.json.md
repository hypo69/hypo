# Документация для `ebay_stores_pacificindustriesltd.json`

## Оглавление
- [Обзор](#обзор)
- [Структура файла](#структура-файла)
  - [Раздел `store`](#раздел-store)
  - [Раздел `scenarios`](#раздел-scenarios)

## Обзор

Данный файл `ebay_stores_pacificindustriesltd.json` содержит конфигурационные данные для магазина eBay под названием "ASUS Official store", управляемого поставщиком с идентификатором 4534. Файл определяет параметры магазина и сценарии для парсинга определенных категорий товаров, таких как "Google Nest".

## Структура файла

Файл состоит из двух основных разделов: `store` и `scenarios`.

### Раздел `store`

Раздел `store` содержит информацию о магазине на eBay.

**Описание**: Настройки магазина на eBay.

**Параметры**:
- `store_id` (str): Уникальный идентификатор магазина.
- `supplier_id` (int): Идентификатор поставщика магазина.
- `get store banners` (bool): Флаг, указывающий на необходимость получения баннеров магазина.
- `description` (str): Описание магазина.
- `about` (str): Дополнительная информация о магазине.
- `url` (str): URL-адрес магазина на eBay.
- `shop categories page` (str): URL-адрес страницы категорий магазина.
- `shop categories json file` (str): Путь к файлу JSON со списком категорий магазина.

### Раздел `scenarios`

Раздел `scenarios` определяет сценарии для парсинга конкретных категорий товаров в магазине.

**Описание**: Настройки сценариев парсинга категорий товаров.

####  `Google Nest`

**Описание**: Сценарий для парсинга товаров из категории "Google Nest".

**Параметры**:
- `url` (str): URL-адрес категории товаров на eBay.
- `active` (bool): Флаг, указывающий на активность сценария.
- `condition` (str): Условие товара, которое нужно парсить (например, "new").
- `presta_categories` (dict): Настройки категорий для PrestaShop.
    - `template` (dict): Шаблон категорий.
         - `google` (str): Имя категории (например, "NEST").
- `checkbox` (bool): Флаг, относящийся к checkbox.
- `price_rule` (int): Правило для определения цены.