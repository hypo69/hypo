# Документация для `ebay_stores_mmhfcom.json`

## Обзор

Данный файл содержит конфигурацию для магазина eBay с идентификатором `mmhfcom`. Он включает информацию о магазине, а также настройки для различных сценариев импорта товаров. Файл структурирован в формате JSON и определяет параметры для сбора данных и категоризации товаров из магазина eBay.

## Содержание (TOC)

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
    -   [Секция `store`](#секция-store)
    -   [Секция `scenarios`](#секция-scenarios)
        -   [Сценарий `motor parts`](#сценарий-motor-parts)
        -   [Сценарий `industrial`](#сценарий-industrial)
        -   [Сценарий `industrial 2`](#сценарий-industrial-2)
        -   [Сценарий `health`](#сценарий-health)

## Структура JSON

### Секция `store`

Секция `store` содержит общую информацию о магазине eBay.

**Описание**: Конфигурация магазина eBay.

**Поля**:
*   `store_id` (str): Идентификатор магазина на eBay (`thegasketsman75`).
*   `supplier_id` (int): Идентификатор поставщика (`4534`).
*   `get store banners` (bool): Флаг, указывающий на необходимость сбора баннеров магазина (`true`).
*   `description` (str): Описание магазина (`thegasketsman75 Gasket KIT`).
*   `about` (str): Дополнительная информация о магазине (пустая строка).
*   `url` (str): URL-адрес магазина (`https://www.ebay.com/str/mmhfcom`).
*   `shop categories page` (str): URL-адрес страницы категорий магазина (пустая строка).
*   `shop categories json file` (str): Путь к файлу JSON с категориями магазина (пустая строка).

### Секция `scenarios`

Секция `scenarios` содержит настройки для различных сценариев импорта товаров.

**Описание**: Настройки сценариев импорта товаров.

#### Сценарий `motor parts`

**Описание**: Настройки для импорта товаров из категории "Автозапчасти".

**Поля**:
*   `url` (str): URL-адрес категории "Автозапчасти" (`https://www.ebay.com/str/mmhfcom/eBay-Motors/_i.html?_sacat=6000`).
*   `active` (bool): Флаг, указывающий на активность сценария (`true`).
*   `condition` (str): Состояние товаров (`new`).
*   `presta_categories` (dict): Настройки категорий PrestaShop.
    *   `template` (dict): Шаблон сопоставления категорий.
        *   `automotive parts` (str): Соответствующая категория в PrestaShop (`PARTS UNSORTED`).
*   `checkbox` (bool): Флаг для использования чекбокса (не используется в данном контексте) (`false`).
*   `price_rule` (int): Правило ценообразования (`1`).

#### Сценарий `industrial`

**Описание**: Настройки для импорта товаров из категории "Бизнес и промышленность".

**Поля**:
*   `url` (str): URL-адрес категории "Бизнес и промышленность" (`https://www.ebay.com/str/mmhfcom/Business-Industrial/_i.html?_sacat=12576`).
*   `active` (bool): Флаг, указывающий на активность сценария (`true`).
*   `condition` (str): Состояние товаров (`new`).
*   `presta_categories` (dict): Настройки категорий PrestaShop.
    *   `template` (dict): Шаблон сопоставления категорий.
        *   `desktop_hardware` (str): Соответствующая категория в PrestaShop (`UNSORTED`).
*   `checkbox` (bool): Флаг для использования чекбокса (не используется в данном контексте) (`false`).
*   `price_rule` (int): Правило ценообразования (`1`).

#### Сценарий `industrial 2`

**Описание**: Настройки для импорта товаров из категории "Электроника".

**Поля**:
*   `url` (str): URL-адрес категории "Электроника" (`https://www.ebay.com/str/mmhfcom/Consumer-Electronics/_i.html?_sacat=293`).
*   `active` (bool): Флаг, указывающий на активность сценария (`true`).
*   `condition` (str): Состояние товаров (`new`).
*   `presta_categories` (dict): Настройки категорий PrestaShop.
    *   `template` (dict): Шаблон сопоставления категорий.
        *   `desktop_hardware` (str): Соответствующая категория в PrestaShop (`UNSORTED`).
*   `checkbox` (bool): Флаг для использования чекбокса (не используется в данном контексте) (`false`).
*   `price_rule` (int): Правило ценообразования (`1`).

#### Сценарий `health`

**Описание**: Настройки для импорта товаров из категории "Здоровье и красота".

**Поля**:
*   `url` (str): URL-адрес категории "Здоровье и красота" (`https://www.ebay.com/str/mmhfcom/Health-Beauty/_i.html?_sacat=26395`).
*   `active` (bool): Флаг, указывающий на активность сценария (`true`).
*   `condition` (str): Состояние товаров (`new`).
*   `presta_categories` (dict): Настройки категорий PrestaShop.
    *   `template` (dict): Шаблон сопоставления категорий.
        *   `desktop_hardware` (str): Соответствующая категория в PrestaShop (`UNSORTED`).
*   `checkbox` (bool): Флаг для использования чекбокса (не используется в данном контексте) (`false`).
*   `price_rule` (int): Правило ценообразования (`1`).