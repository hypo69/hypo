# Документация для `amazon_categories_laptops_asus.json`

## Обзор

Данный JSON-файл содержит конфигурацию для парсинга и категоризации ноутбуков ASUS с Amazon. Он определяет настройки магазина и сценарии для конкретных категорий товаров.

## Содержание

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
  - [Раздел "store"](#раздел-store)
  - [Раздел "scenarios"](#раздел-scenarios)
    - [Сценарий "ASUS INTEL CELERON"](#сценарий-asus-intel-celeron)

## Структура файла

### Раздел "store"

Этот раздел содержит общие настройки магазина на Amazon, с которого будет производиться сбор данных.

- **`store_id`** (string): Идентификатор магазина (в текущей конфигурации пустой).
- **`supplier_id`** (string): Идентификатор поставщика (в текущей конфигурации пустой).
- **`get store banners`** (boolean): Флаг, указывающий, нужно ли собирать баннеры магазина. Установлен в `true`.
- **`description`** (string): Описание магазина. В данном случае `"ASUS laptops"`.
- **`about`** (string): Дополнительная информация о магазине. В данном случае `"ASUS laptops"`.
- **`url`** (string): URL главной страницы магазина на Amazon.
- **`shop categories page`** (string): URL страницы с категориями магазина (в текущей конфигурации пустой).
- **`shop categories json file`** (string): Путь к JSON-файлу с категориями магазина (в текущей конфигурации пустой).

### Раздел "scenarios"

Этот раздел содержит сценарии для различных категорий товаров, которые будут парситься.

#### Сценарий "ASUS INTEL CELERON"

Этот сценарий описывает настройки для парсинга ноутбуков ASUS с процессором Intel Celeron.

- **`brand`** (string): Бренд товара, который будет использоваться для фильтрации. Указан `"DELL"`, что может быть ошибкой, так как в названии сценария указан ASUS.
- **`url`** (string): URL страницы на Amazon с соответствующей категорией товаров.
- **`active`** (boolean): Флаг, указывающий, активен ли данный сценарий. Установлен в `true`.
- **`condition`** (string): Состояние товара. Установлено в `"new"`.
- **`presta_categories`** (dict): Соответствие между категориями из Amazon и PrestaShop.
  - **`template`** (dict): Шаблон для категорий. Ключ `"asus"` соответствует значению `"LAPTOPS INTEL CELERON"`.
- **`checkbox`** (boolean): Флаг, указывающий, нужно ли использовать чекбокс для выбора товаров. Установлен в `false`.
- **`price_rule`** (integer): Номер правила для расчета цены. Установлен в `1`.