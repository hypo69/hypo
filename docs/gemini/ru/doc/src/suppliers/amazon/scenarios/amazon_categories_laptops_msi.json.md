# Документация для `amazon_categories_laptops_msi.json`

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
    - [store](#store)
    - [scenarios](#scenarios)

## Обзор

Файл `amazon_categories_laptops_msi.json` содержит конфигурационные данные для сбора информации о ноутбуках MSI с сайта Amazon. Он включает в себя настройки магазина и сценарии сбора данных для конкретных категорий товаров.

## Структура файла

Файл представляет собой JSON-объект, содержащий два основных раздела: `store` и `scenarios`.

### `store`

Раздел `store` содержит общие настройки магазина:

- **`store_id` (str):** Идентификатор магазина (пустая строка).
- **`supplier_id` (str):** Идентификатор поставщика (пустая строка).
- **`get store banners` (bool):** Флаг, указывающий, нужно ли получать баннеры магазина (значение `true`).
- **`description` (str):** Описание магазина ("MSI laptops").
- **`about` (str):** Дополнительная информация о магазине ("MSI laptops").
- **`url` (str):** URL-адрес страницы магазина на Amazon, где отображаются ноутбуки MSI.
- **`shop categories page` (str):** URL-адрес страницы категорий магазина (пустая строка).
- **`shop categories json file` (str):** Путь к JSON-файлу с категориями магазина (пустая строка).

### `scenarios`

Раздел `scenarios` содержит сценарии сбора данных. Каждый сценарий представлен как объект с ключом, представляющим название сценария.

#### `Apple Wathes`

- **`url` (str):** URL-адрес страницы с товарами для данного сценария (Apple Wathes).
- **`active` (bool):** Флаг, указывающий, активен ли сценарий (значение `true`).
- **`condition` (str):** Состояние товаров, отфильтрованных для данного сценария ("new").
- **`presta_categories` (dict):**  Соответствие категорий для PrestaShop. Включает в себя:
    - **`template` (dict):** Шаблон соответствия категорий, где ключи это идентификаторы категорий, а значения - это значения категории ("apple":"WATCHES").
- **`checkbox` (bool):** Флаг, указывающий, нужно ли использовать чекбоксы (значение `false`).
- **`price_rule` (int):** Правило ценообразования, которое нужно использовать (значение `1`).