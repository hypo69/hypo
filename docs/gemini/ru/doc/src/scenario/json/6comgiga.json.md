# Документация для `hypotez/src/scenario/json/6comgiga.json`

## Обзор

Данный файл содержит JSON-конфигурацию для парсера, предназначенного для работы с поставщиком "6comgiga". Он определяет параметры для сбора данных, правила цен, URL-адреса и другие настройки, необходимые для работы парсера. Также файл определяет список исключений и подключаемых сценариев.

## Содержание

- [Обзор](#обзор)
- [Основные параметры](#основные-параметры)
- [Настройки каталога](#настройки-каталога)
- [Сценарии](#сценарии)
- [Исключения](#исключения)

## Основные параметры

- **`supplier`**: (str) Имя поставщика, в данном случае "6comgiga".
- **`supplier_prefix`**: (str) Префикс поставщика, используется для идентификации, в данном случае "6comgiga".
- **`start_url`**: (str) URL стартовой страницы поставщика: `https://www.6comgiga.com/`.
- **`wholesale_products_url`**: (str) URL страницы с оптовыми продуктами. В данном случае пустая строка.
- **`price_rule`**: (str) Правило для расчета цены, в данном случае "+0".
- **`num_items_4_flush`**: (int) Количество элементов для сброса кеша, в данном случае 300.
- **`if_login`**: (bool) Флаг, определяющий необходимость входа в систему. В данном случае `true`, что означает, что вход нужен.
- **`login_url`**: (str) URL страницы для входа, в данном случае пустая строка.
- **`root_category`**: (int) Идентификатор корневой категории, в данном случае 3.
-  **`collect_products_from_categorypage`**: (bool) флаг определяющий необходимость собирать товары из страницы категорий. В данном случае `false`

## Настройки каталога

- **`aliexpres_ajax_store`**: (str) URL для ajax запросов к магазину Aliexpress: `https://he.aliexpress.com/store/productGroupsAjax.htm?storeId=`.

- **`catalog_wholesale-products`**: (dict) Словарь, содержащий URL-адреса страниц оптовых товаров для разных локализаций.
    -   `ALL NOT SORTED`: (str) URL для всех не отсортированных оптовых товаров: `https://www.aliexpress.com/wholesale.html?spm=a2g0o.11810135.0.0.61b4IPjRIPjR75`.
    -   `HE`: (str) URL для оптовых товаров с локализацией HE: `https://www.he.aliexpress.com/shop categories page.html`.
    -   `RU`: (str) URL для оптовых товаров с локализацией RU: `https://www.aliexpress.com/shop categories page.html`.
    -   `EN`: (str) URL для оптовых товаров с локализацией EN: `https://www.aliexpress.com/shop categories page.html`.
    -   `FR`: (str) URL для оптовых товаров с локализацией FR: `https://fr.aliexpress.com/shop categories page.html`.

## Сценарии

- **`scenario_files`**: (list) Список подключаемых файлов сценариев в формате JSON:
    -   `aliexpress_stores_elctronic_toys.json`
    -   `aliexpress_stores_baby_clothing.json`

## Исключения

- **`excluded`**: (list) Список исключаемых файлов сценариев в формате JSON:
    -   `aliexpress_stores_battery.json`
    -   `aliexpress_stores_brands.json`
    -   `aliexpress_stores_computer_components.json`
    -   `aliexpress_stores_computer_components_fans.json`
    -   `aliexpress_stores_computers.json`
    -   `aliexpress_stores_electronics.json`
    -   `aliexpress_stores_elctronic_components_audio.json`
    -   `aliexpress_stores_elctronic_components_leds.json`
    -   `aliexpress_stores_elctronic_toys.json`
    -    `aliexpress_stores_lighting.json`
    -    `aliexpress_stores_leds.json`
    -    `aliexpress_stores_malls.json`
    -    `aliexpress_stores_memory.json`
     -  `aliexpress_stores_phones_repair_computers.json`