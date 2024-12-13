# Документация для файла `neimanmarcus.json`

## Обзор

Данный файл содержит конфигурацию для парсинга данных с веб-сайта Neiman Marcus. Он определяет основные параметры для работы парсера, включая поставщика, стартовый URL, правила ценообразования и другие настройки.

## Содержание

1. [Обзор](#обзор)
2. [Описание структуры JSON](#описание-структуры-json)
   - [supplier](#supplier)
   - [supplier_prefix](#supplier_prefix)
   - [start_url](#start_url)
   - [price_rule](#price_rule)
   - [num_items_4_flush](#num_items_4_flush)
   - [if_login](#if_login)
   - [parcing method [webdriver|api]](#parcing-method-webdriverapi)
   - [about method web scrapping [webdriver|api]](#about-method-web-scrapping-webdriverapi)
   - [collect_products_from_categorypage](#collect_products_from_categorypage)
   - [scenarios](#scenarios)

## Описание структуры JSON

### `supplier`

**Описание**: Идентификатор поставщика.

**Тип**: `str`

**Значение**: `"ksp"`

### `supplier_prefix`

**Описание**: Префикс поставщика.

**Тип**: `str`

**Значение**: `"ksp"`

### `start_url`

**Описание**: URL стартовой страницы веб-сайта для парсинга.

**Тип**: `str`

**Значение**: `"https://www.ksp.co.il/"`

### `price_rule`

**Описание**: Правило ценообразования для товаров.

**Тип**: `str`

**Значение**: `"+100"`

### `num_items_4_flush`

**Описание**: Количество товаров для очистки кэша.

**Тип**: `int`

**Значение**: `300`

### `if_login`

**Описание**: Флаг, указывающий, требуется ли вход на сайт.

**Тип**: `bool`

**Значение**: `false`

### `parcing method [webdriver|api]`

**Описание**: Метод парсинга данных (webdriver или API).

**Тип**: `str`

**Значение**: `"web"`

### `about method web scrapping [webdriver|api]`

**Описание**: Комментарий о методе веб-скраппинга.

**Тип**: `str`

**Значение**: `"Если я работаю через API мне не нужен webdriver"`

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, нужно ли собирать товары со страниц категорий.

**Тип**: `bool`

**Значение**: `false`

### `scenarios`

**Описание**: Объект, содержащий сценарии для парсинга.

**Тип**: `dict`

**Значение**: `{}`