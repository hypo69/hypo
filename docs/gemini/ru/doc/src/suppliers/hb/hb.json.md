# Документация для `hb.json`

## Обзор

Файл `hb.json` содержит конфигурационные данные для поставщика "HB Dead Sea Cosmetics". Он определяет различные параметры, такие как ID поставщика, префикс, список активных клиентов, начальный URL, правила ценообразования, сценарии сбора данных, а также список исключений. Этот файл используется для настройки процесса сбора данных и управления им.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
   - [supplier](#supplier)
   - [supplier_id](#supplier_id)
   - [supplier_prefix](#supplier_prefix)
   - [active_clients_list](#active_clients_list)
   - [start_url](#start_url)
   - [price_rule](#price_rule)
   - [if_list](#if_list)
   - [use_mouse](#use_mouse)
    - [mandatory](#mandatory)
   - [if_login](#if_login)
   - [login_url](#login_url)
   - [lang](#lang)
   - [id_category_default](#id_category_default)
   - [compare_categorie_dict](#compare_categorie_dict)
   - [collect_products_from_categorypage](#collect_products_from_categorypage)
   - [scenario_files](#scenario_files)
   - [excluded](#excluded)
   - [last_runned_scenario](#last_runned_scenario)
   - [scenario_interrupted](#scenario_interrupted)
   - [last_runned_scenario_filename](#last_runned_scenario_filename)
     - [just_runned_scenario_filename](#just_runned_scenario_filename)
   - [interrupted_scenario](#interrupted_scenario)

## Структура JSON

### `supplier`

**Описание**: Название поставщика.
**Тип**: `str`
**Пример**: `"HB Dead Sea Cosmetics"`

### `supplier_id`

**Описание**: Уникальный идентификатор поставщика.
**Тип**: `str`
**Пример**: `"11267"`

### `supplier_prefix`

**Описание**: Префикс поставщика, используемый в идентификаторах продуктов.
**Тип**: `str`
**Пример**: `"hb"`

### `active_clients_list`

**Описание**: Список доменов активных клиентов.
**Тип**: `list[str]`
**Пример**: `["emil-design.com", "e-cat.co.il"]`

### `start_url`

**Описание**: Начальный URL сайта поставщика.
**Тип**: `str`
**Пример**: `"https://hbdeadsea.co.il/"`

### `price_rule`

**Описание**: Правило ценообразования (например, "+0" для отсутствия наценки).
**Тип**: `str`
**Пример**: `"+0"`

### `if_list`

**Описание**: Условие для обработки списка.
**Тип**: `str`
**Пример**: `"first"`

### `use_mouse`

**Описание**: Флаг использования мыши.
**Тип**: `bool`
**Пример**: `false`
### `mandatory`

**Описание**: Флаг обязательного параметра.
**Тип**: `str`
**Пример**: `"true"`
### `if_login`

**Описание**: Флаг необходимости авторизации.
**Тип**: `bool`
**Пример**: `false`

### `login_url`

**Описание**: URL для авторизации, если требуется.
**Тип**: `str`
**Пример**: `""`

### `lang`

**Описание**: Язык, используемый на сайте поставщика.
**Тип**: `str`
**Пример**: `"HE"`

### `id_category_default`

**Описание**: Идентификатор категории по умолчанию.
**Тип**: `int`
**Пример**: `11246`

### `compare_categorie_dict`

**Описание**: Флаг сравнения категорий по словарю.
**Тип**: `bool`
**Пример**: `true`

### `collect_products_from_categorypage`

**Описание**: Флаг сбора товаров со страницы категории.
**Тип**: `bool`
**Пример**: `false`

### `scenario_files`

**Описание**: Список файлов сценариев для сбора данных.
**Тип**: `list[str]`
**Пример**:
```json
[
    "categories_20240503015900.json",
    "bodyspa.json",
    "soap-bar.json",
    "men-treatment.json",
    "health-products.json",
    "hair-treatment.json",
    "facial.json",
    "dead-sea-mud-products.json",
    "aromatherapy.json"
  ]
```
### `excluded`

**Описание**: Список исключенных элементов.
**Тип**: `list`
**Пример**: `[]`

### `last_runned_scenario`

**Описание**: Имя последнего запущенного сценария.
**Тип**: `str`
**Пример**: `"feet-hand-treatment"`

### `scenario_interrupted`

**Описание**: Имя прерванного сценария.
**Тип**: `str`
**Пример**: `"feet-hand-treatment"`

### `last_runned_scenario_filename`

**Описание**: Имя файла последнего запущенного сценария.
**Тип**: `str`
**Пример**: `"bodyspa.json"`

### `just_runned_scenario_filename`

**Описание**: Имя файла текущего запущенного сценария.
**Тип**: `str`
**Пример**: `"bodyspa.json"`
### `interrupted_scenario`

**Описание**: Список прерванных сценариев.
**Тип**: `list[str]`
**Пример**: `["feet-hand-treatment"]`