# Документация для файла `grandadvance.json`

## Обзор

Файл `grandadvance.json` содержит конфигурационные данные для поставщика "grandadvance". Он определяет параметры, необходимые для сбора данных о товарах с сайта поставщика, включая URL-адреса, правила ценообразования и настройки входа.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [Поля верхнего уровня](#поля-верхнего-уровня)
        - [`supplier`](#supplier)
        - [`supplier_id`](#supplier_id)
        - [`supplier_prefix`](#supplier_prefix)
        - [`start_url`](#start_url)
        - [`price_rule`](#price_rule)
        - [`if_login`](#if_login)
        - [`login_url`](#login_url)
        - [`root_category`](#root_category)
        - [`collect_products_from_categorypage`](#collect_products_from_categorypage)
        - [`scenario_files`](#scenario_files)
        - [`out`](#out)
        - [`last_runned_scenario`](#last_runned_scenario)
        - [`locator_description`](#locator_description)
        - [`scenario_interrupted`](#scenario_interrupted)

## Структура JSON

### Поля верхнего уровня

#### `supplier`
- **Описание**: Название поставщика.
- **Тип**: `str`
- **Значение**: `"grandadvance"`

#### `supplier_id`
- **Описание**: Идентификатор поставщика.
- **Тип**: `str`
- **Значение**: `"2789"`

#### `supplier_prefix`
- **Описание**: Префикс поставщика.
- **Тип**: `str`
- **Значение**: `"grandadvance"`

#### `start_url`
- **Описание**: Начальный URL-адрес сайта поставщика.
- **Тип**: `str`
- **Значение**: `"https://www.grandadvance.co.il/"`

#### `price_rule`
- **Описание**: Правило для расчета цены.
- **Тип**: `str`
- **Значение**: `"+0"`

#### `if_login`
- **Описание**: Указывает, требуется ли вход для доступа к данным.
- **Тип**: `bool`
- **Значение**: `false`

#### `login_url`
- **Описание**: URL-адрес страницы входа.
- **Тип**: `str`
- **Значение**: `"https://www.login.grandadvance.co.il"`

#### `root_category`
- **Описание**: Идентификатор корневой категории.
- **Тип**: `int`
- **Значение**: `3`

#### `collect_products_from_categorypage`
- **Описание**: Указывает, нужно ли собирать товары со страницы категории.
- **Тип**: `bool`
- **Значение**: `true`

#### `scenario_files`
- **Описание**: Список файлов сценариев (в данном случае пустой).
- **Тип**: `list`
- **Значение**: `[]`

#### `out`
- **Описание**: Список для вывода (в данном случае пустой).
- **Тип**: `list`
- **Значение**: `[]`

#### `last_runned_scenario`
- **Описание**: Название последнего запущенного сценария.
- **Тип**: `str`
- **Значение**: `""`

#### `locator_description`
- **Описание**: Описание локатора.
- **Тип**: `str`
- **Значение**: `""`

#### `scenario_interrupted`
- **Описание**: Указывает, был ли прерван сценарий.
- **Тип**: `str`
- **Значение**: `""`