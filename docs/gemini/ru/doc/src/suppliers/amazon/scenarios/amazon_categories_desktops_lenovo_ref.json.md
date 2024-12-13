# Документация для `amazon_categories_desktops_lenovo_ref.json`

## Обзор

Файл `amazon_categories_desktops_lenovo_ref.json` содержит JSON-конфигурацию для сценариев парсинга категорий настольных компьютеров Lenovo с Amazon, бывших в употреблении.  Каждый сценарий определяет условия поиска, категории для PrestaShop и правила ценообразования.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [scenarios](#scenarios)
    - [`REF lenovo DESKTOP INTEL I5`](#ref-lenovo-desktop-intel-i5)
    - [`REF lenovo DESKTOP INTEL I7`](#ref-lenovo-desktop-intel-i7)

## Структура JSON

### `scenarios`

Объект `scenarios` содержит сценарии для парсинга. Каждый сценарий представлен в виде пары ключ-значение, где ключ - это уникальное имя сценария, а значение - это объект, описывающий параметры сценария.

#### `REF lenovo DESKTOP INTEL I5`

**Описание**: Сценарий для парсинга настольных компьютеров Lenovo с процессором Intel i5, бывших в употреблении.

**Параметры**:

-   `brand` (str): Бренд товара.
-   `url` (str): URL для поиска товаров.
-   `active` (bool): Активен ли сценарий.
-  `condition` (str): Состояние товара (в данном случае, "ref" - refurbished).
-   `presta_categories` (dict): Категории для PrestaShop.
  -   `template` (dict): Шаблон категорий, где ключ "lenovo" соответствует значению "DESKTOPS INTEL I5".
-   `checkbox` (bool): Флаг для checkbox.
-  `price_rule` (int): Правило ценообразования.

#### `REF lenovo DESKTOP INTEL I7`

**Описание**: Сценарий для парсинга настольных компьютеров Lenovo с процессором Intel i7, бывших в употреблении.

**Параметры**:

-   `brand` (str): Бренд товара.
-   `url` (str): URL для поиска товаров.
-   `active` (bool): Активен ли сценарий.
-  `condition` (str): Состояние товара (в данном случае, "ref" - refurbished).
-   `presta_categories` (dict): Категории для PrestaShop.
  -   `template` (dict): Шаблон категорий, где ключ "lenovo" соответствует значению "DESKTOPS INTEL I5".
-   `checkbox` (bool): Флаг для checkbox.
-  `price_rule` (int): Правило ценообразования.