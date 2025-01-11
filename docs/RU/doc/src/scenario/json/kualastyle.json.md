# Документация для `kualastyle.json`

## Обзор

Файл `kualastyle.json` содержит конфигурацию для парсера веб-сайта Kualastyle. Он определяет параметры подключения к сайту, правила парсинга, список сценариев для категорий товаров и другие настройки.

## Оглавление

- [Обзор](#обзор)
- [Параметры](#параметры)
    - [supplier](#supplier)
    - [supplier_id](#supplier_id)
    - [supplier_prefix](#supplier_prefix)
    - [start_url](#start_url)
    - [login_url](#login_url)
    - [check categories on site](#check-categories-on-site)
    - [if_login](#if_login)
    - [price_rule](#price_rule)
    - [if_list](#if_list)
    - [use_mouse](#use_mouse)
    - [mandatory](#mandatory)
    - [parcing method [webdriver|api]](#parcing-method-webdriverapi)
    - [about method web scrapping [webdriver|api]](#about-method-web-scrapping-webdriverapi)
    - [collect_products_from_categorypage](#collect_products_from_categorypage)
    - [num_items_4_flush](#num_items_4_flush)
    - [scenario_files](#scenario_files)
    - [last_runned_scenario](#last_runned_scenario)
    - [excluded](#excluded)

## Параметры

### `supplier`

**Описание**: Название поставщика.

**Тип**: `str`

**Значение**: `"kualastyle"`

### `supplier_id`

**Описание**: ID поставщика.

**Тип**: `str`

**Значение**: `"11028"`

### `supplier_prefix`

**Описание**: Префикс поставщика.

**Тип**: `str`

**Значение**: `"kualastyle"`

### `start_url`

**Описание**: Стартовый URL сайта поставщика.

**Тип**: `str`

**Значение**: `"https://kualastyle.com"`

### `login_url`

**Описание**: URL для входа на сайт поставщика.

**Тип**: `str`

**Значение**: `"https://kualastyle.com"`

### `check categories on site`

**Описание**: Флаг, указывающий, нужно ли проверять категории на сайте.

**Тип**: `bool`

**Значение**: `true`

### `if_login`

**Описание**: Флаг, указывающий, нужно ли выполнять вход на сайт.

**Тип**: `bool`

**Значение**: `true`

### `price_rule`

**Описание**: Правило расчета цены.

**Тип**: `str`

**Значение**: `"*1"`

### `if_list`

**Описание**: Условие для списка.

**Тип**: `str`

**Значение**: `"first"`

### `use_mouse`

**Описание**: Флаг, указывающий, использовать ли мышь для действий.

**Тип**: `bool`

**Значение**: `false`

### `mandatory`

**Описание**: Флаг, указывающий, является ли обязательным парсинг.

**Тип**: `bool`

**Значение**: `true`

### `parcing method [webdriver|api]`

**Описание**: Метод парсинга (webdriver или api).

**Тип**: `str`

**Значение**: `"web"`

### `about method web scrapping [webdriver|api]`

**Описание**: Комментарий о методе веб-скрейпинга.

**Тип**: `str`

**Значение**: `"Если я работаю через API мне не нужен webdriver"`

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, нужно ли собирать товары со страницы категории.

**Тип**: `bool`

**Значение**: `false`

### `num_items_4_flush`

**Описание**: Количество элементов для сброса.

**Тип**: `int`

**Значение**: `500`

### `scenario_files`

**Описание**: Список файлов сценариев для категорий.

**Тип**: `list[str]`

**Значение**:
```json
[
    "kualastyle_categories_accessories.json",
    "kualastyle_categories_appliances.json",
    "kualastyle_categories_carpets.json",
    "kualastyle_categories_children_and_youth.json",
    "kualastyle_categories_furniture.json",
    "kualastyle_categories_lighting.json",
    "kualastyle_categories_mattresses.json",
    "kualastyle_categories_mirrors.json",
    "kualastyle_categories_photos.json",
    "kualastyle_categories_textile.json"
]
```

### `last_runned_scenario`

**Описание**: Название последнего запущенного сценария.

**Тип**: `str`

**Значение**: `""`

### `excluded`

**Описание**: Список исключенных элементов.

**Тип**: `list`

**Значение**: `[]`