# Конфигурация поставщика Amazon

## Обзор

Этот файл JSON содержит конфигурационные параметры для поставщика Amazon. Он определяет основные настройки для сбора данных, включая начальный URL, правила ценообразования, логин, языковые настройки, а также список сценариев и исключений.

## Оглавление
1. [Обзор](#обзор)
2. [Основные параметры](#основные-параметры)
3. [Настройки логина](#настройки-логина)
4. [Настройки сбора данных](#настройки-сбора-данных)
5. [Сценарии и исключения](#сценарии-и-исключения)
6. [Последний запущенный сценарий](#последний-запущенный-сценарий)

## Основные параметры

### `supplier`
- **Описание**: Название поставщика.
- **Тип**: `str`
- **Значение**: `"amazon"`

### `supplier_id`
- **Описание**: Идентификатор поставщика.
- **Тип**: `str`
- **Значение**: `"2800"`

### `supplier_prefix`
- **Описание**: Префикс поставщика.
- **Тип**: `str`
- **Значение**: `"amazon"`

### `start_url`
- **Описание**: Начальный URL для парсинга.
- **Тип**: `str`
- **Значение**: `"https://www.amazon.com/"`

### `price_rule`
- **Описание**: Правило ценообразования.
- **Тип**: `str`
- **Значение**: `"+0"`

### `if_list`
- **Описание**: Условие для обработки списков.
- **Тип**: `str`
- **Значение**: `"first"`

### `use_mouse`
- **Описание**: Флаг использования мыши.
- **Тип**: `bool`
- **Значение**: `false`

### `mandatory`
- **Описание**: Флаг обязательного использования.
- **Тип**: `bool`
- **Значение**: `true`

## Настройки логина

### `if_login`
- **Описание**: Флаг необходимости логина.
- **Тип**: `bool`
- **Значение**: `false`

### `login_url`
- **Описание**: URL для логина.
- **Тип**: `str`
- **Значение**: `"https://amazon.com"`

## Настройки сбора данных

### `lang`
- **Описание**: Язык сайта.
- **Тип**: `str`
- **Значение**: `"EN"`

### `check categories on site`
- **Описание**: Флаг проверки категорий на сайте.
- **Тип**: `bool`
- **Значение**: `false`

### `parsing via api`
- **Описание**: Флаг использования API для парсинга.
- **Тип**: `bool`
- **Значение**: `false`

### `collect_products_from_categorypage`
- **Описание**: Флаг сбора продуктов со страницы категории.
- **Тип**: `bool`
- **Значение**: `false`

## Сценарии и исключения

### `scenario_files`
- **Описание**: Список файлов сценариев.
- **Тип**: `list`
- **Значение**:
  ```json
    ["amazon_categories_murano_glass.json"]
  ```

### `excluded`
- **Описание**: Список исключенных файлов.
- **Тип**: `list`
- **Значение**:
  ```json
  [
    "amazon_categories_lighting.json",
    "amazon_categories_shelves.json",
    "amazon_categories_consoles.json",
    "amazon_categories_office_chairs.json",
    "amazon_categories_ottomans.json",
    "amazon_categories_desktops_dell_ref.json",
    "amazon_categories_videocards.json",
    "amazon_categories_copmuter_cooling_corsair_new.json",
    "amazon_categories_desktops_dell_ref.json",
    "amazon_categories_desktops_hp_used.json",
    "amazon_categories_desktops_lenovo_new.json",
    "amazon_categories_desktops_lenovo_ref.json",
    "amazon_categories_desktops_lenovo_used.json",
    "amazon_categories_laptops_acer.json",
    "amazon_categories_laptops_asus.json",
    "amazon_stores_tech_pirate.json",
    "amazon_stores_amazon_ref.json",
    "amazon_stores_asus.json",
    "amazon_stores_feebz.json",
    "amazon_stores_lenovo.json",
    "amazon_categories_laptops_lenovo.json",
    "amazon_categories_watches_apple.json",
    "amazon_categories_laptops_macbook.json.json"
  ]
  ```

## Последний запущенный сценарий

### `last_runned_scenario`
- **Описание**: Имя последнего запущенного сценария.
- **Тип**: `str`
- **Значение**: `""`

### `last_runned_scenario_filename`
- **Описание**: Имя файла последнего запущенного сценария.
- **Тип**: `str`
- **Значение**: `""`