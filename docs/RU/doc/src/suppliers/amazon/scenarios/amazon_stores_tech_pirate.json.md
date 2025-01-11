# Документация для `amazon_stores_tech_pirate.json`

## Обзор

Этот файл `amazon_stores_tech_pirate.json` содержит конфигурацию для парсинга товаров из магазина Amazon "Tech Pirate". Он определяет настройки магазина, включая его идентификатор, идентификатор поставщика, описание, URL-адрес и настройки для различных сценариев, таких как "Apple iPad" и "Microsoft Surface".

## Содержание

1.  [Обзор](#обзор)
2.  [Структура файла](#структура-файла)
3.  [Раздел `store`](#раздел-store)
4.  [Раздел `scenarios`](#раздел-scenarios)
    - [Сценарий `Apple iPad`](#сценарий-apple-ipad)
    - [Сценарий `Microsoft Surface`](#сценарий-microsoft-surface)

## Структура файла

Файл имеет структуру JSON, которая содержит два основных раздела: `store` и `scenarios`.

## Раздел `store`

Раздел `store` содержит общую информацию о магазине.

**Описание полей:**

-   `store_id` (str): Идентификатор магазина на Amazon. В данном случае `ATVPDKIKX0DER`.
-   `supplier_id` (int): Идентификатор поставщика, `4534`.
-   `get store banners` (bool): Флаг, указывающий, нужно ли получать баннеры магазина. Установлен в `true`.
-   `description` (str): Описание магазина, `"refirnished apple ipad and Microsoft Surface"`.
-   `about` (str): Информация о магазине, `"OCULUS"`.
-   `url` (str): URL-адрес магазина на Amazon, `"https://www.amazon.com/s?me=A3MMFG4QMDSOPQ&marketplaceID=ATVPDKIKX0DER"`.
-  `shop categories page` (str): URL-адрес страницы с категориями магазина. В данном случае пустая строка `""`.
- `shop categories json file` (str): Путь к JSON-файлу, содержащему категории магазина. В данном случае пустая строка `""`.

## Раздел `scenarios`

Раздел `scenarios` содержит настройки для различных сценариев парсинга товаров. Каждый сценарий имеет свое имя и настройки.

### Сценарий `Apple iPad`

**Описание полей:**

-   `url` (str): URL-адрес страницы с товарами Apple iPad, `"https://www.amazon.com/s?i=merchant-items&me=A3MMFG4QMDSOPQ&rh=p_4%3AApple&dc&ds=v1%3AZR3ViI9gYZ%2FaTgCS2hbcRqqmXZIvuJ1OuWNjXLgyMeA&marketplaceID=ATVPDKIKX0DER&qid=1671321429&ref=sr_nr_p_4_1"`.
-   `active` (bool): Флаг, указывающий, активен ли сценарий. Установлен в `true`.
-   `condition` (str): Состояние товаров, `"new"`.
-    `presta_categories` (dict): Словарь, связывающий категории Amazon с категориями PrestaShop.
    - `template` (dict): Словарь соответствий, `{ "apple": "iPad" }`.
-   `checkbox` (bool): Флаг для чекбокса. Установлен в `false`.
-   `price_rule` (int): Правило ценообразования, `1`.

### Сценарий `Microsoft Surface`

**Описание полей:**

-   `url` (str): URL-адрес страницы с товарами Microsoft Surface, `"https://www.amazon.com/s?i=merchant-items&me=A3MMFG4QMDSOPQ&rh=p_4%3AMicrosoft&dc&ds=v1%3AZamybgWSUuxayvxDLutGT0IMf5bIa4O%2Fi7cOvvZyJYw&marketplaceID=ATVPDKIKX0DER&qid=1671322146&ref=sr_nr_p_4_2"`.
-   `active` (bool): Флаг, указывающий, активен ли сценарий. Установлен в `true`.
-   `condition` (str): Состояние товаров, `"new"`.
-    `presta_categories` (dict): Словарь, связывающий категории Amazon с категориями PrestaShop.
    - `template` (dict): Словарь соответствий, `{ "microsoft": "SURFACE" }`.
-   `checkbox` (bool): Флаг для чекбокса. Установлен в `false`.
-   `price_rule` (int): Правило ценообразования, `1`.