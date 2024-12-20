# Документация для `amazon_categories_watches_apple.json`

## Обзор

Файл `amazon_categories_watches_apple.json` содержит конфигурационные данные для парсинга и обработки товаров категории "Apple Watches" с сайта Amazon. Он включает в себя информацию о магазине, его URL, описание, а также сценарии для сбора данных о товарах, их категоризации и ценообразования.

## Оглавление
1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
   - [Раздел `store`](#раздел-store)
   - [Раздел `scenarios`](#раздел-scenarios)
      - [`Apple Wathes`](#apple-wathes)

## Структура файла

### Раздел `store`
Этот раздел содержит информацию о магазине на Amazon, для которого настраивается парсинг.

- **`store_id`**: Идентификатор магазина (в данном случае пустая строка).
- **`supplier_id`**: Идентификатор поставщика (в данном случае пустая строка).
- **`get store banners`**: Флаг, указывающий на необходимость сбора баннеров магазина (`true`).
- **`description`**: Описание магазина ("Apple Wathes").
- **`about`**: Дополнительная информация о магазине ("Macbook ref").
- **`url`**: URL магазина на Amazon.
- **`shop categories page`**: URL страницы категорий магазина (в данном случае пустая строка).
- **`shop categories json file`**: Путь к JSON файлу с категориями магазина (в данном случае пустая строка).

### Раздел `scenarios`
Этот раздел содержит сценарии парсинга товаров. В данном файле представлен один сценарий для "Apple Watches".

#### `Apple Wathes`
Этот раздел содержит настройки для парсинга товаров категории "Apple Watches".

- **`url`**: URL страницы с товарами "Apple Watches".
- **`active`**: Флаг, указывающий, активен ли сценарий (`true`).
- **`condition`**: Состояние товара ("new").
- **`presta_categories`**: Настройки категорий PrestaShop, в которые нужно отнести спарсенные товары.
  - **`template`**: Словарь, определяющий соответствие между категориями на Amazon и PrestaShop. В данном случае `{"apple": "WATCHES"}` означает, что все товары с пометкой "apple" будут отнесены к категории "WATCHES".
- **`checkbox`**: Флаг, определяющий использование чекбокса (в данном случае `false`).
- **`price_rule`**: Идентификатор ценового правила (`1`).