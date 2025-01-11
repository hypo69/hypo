# Документация для `kualastyle.json`

## Обзор

Файл `kualastyle.json` содержит конфигурационные данные для парсера поставщика Kualastyle. Он включает в себя информацию о поставщике, URL-адреса, правила обработки цен, настройки сбора данных и список исключенных сценариев.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание полей](#описание-полей)

## Структура JSON

Файл представляет собой JSON-объект со следующими полями:

```json
{
  "supplier": "kualastyle",
  "supplier_id": "11028",
  "supplier_prefix": "kualastyle",
  "start_url": "https://kualastyle.com",
  "login_url": "https://kualastyle.com",
  "if_login": true,
  "price_rule": "*1",
  "if_list":"first",
   "use_mouse": false,
  "id_category_default": 11036,
  "compare_categorie_dict": true,
  "collect_products_from_categorypage": false,
  "scenario_files": [
    "bedroom.json"
  ],
  "last_runned_scenario": "",
  "excluded": [
    "bedroom.json",
    "bathroom.json",
    "livingroom.json",
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
}
```

## Описание полей

### `supplier`
- **Описание**: Имя поставщика.
- **Тип**: `str`
- **Значение**: `"kualastyle"`

### `supplier_id`
- **Описание**: Идентификатор поставщика.
- **Тип**: `str`
- **Значение**: `"11028"`

### `supplier_prefix`
- **Описание**: Префикс поставщика.
- **Тип**: `str`
- **Значение**: `"kualastyle"`

### `start_url`
- **Описание**: Начальный URL для парсинга.
- **Тип**: `str`
- **Значение**: `"https://kualastyle.com"`

### `login_url`
- **Описание**: URL для входа в систему.
- **Тип**: `str`
- **Значение**: `"https://kualastyle.com"`

### `if_login`
- **Описание**: Флаг, указывающий, требуется ли вход в систему.
- **Тип**: `bool`
- **Значение**: `true`

### `price_rule`
- **Описание**: Правило расчета цены.
- **Тип**: `str`
- **Значение**: `"*1"` (умножение на 1, то есть без изменения)

### `if_list`
- **Описание**: Указывает, какой элемент списка использовать при парсинге.
- **Тип**: `str`
- **Значение**: `"first"` (использовать первый элемент списка)
### `use_mouse`
-   **Описание**: Флаг, указывающий использовать ли эмуляцию мыши при парсинге.
-   **Тип**: `bool`
-   **Значение**: `false`

### `id_category_default`
- **Описание**: Идентификатор категории по умолчанию.
- **Тип**: `int`
- **Значение**: `11036`

### `compare_categorie_dict`
- **Описание**: Флаг, указывающий необходимость сравнения категорий.
- **Тип**: `bool`
- **Значение**: `true`

### `collect_products_from_categorypage`
- **Описание**: Флаг, определяющий, нужно ли собирать товары со страниц категорий.
- **Тип**: `bool`
- **Значение**: `false`

### `scenario_files`
- **Описание**: Список файлов сценариев для парсинга.
- **Тип**: `list`
- **Значение**: `["bedroom.json"]`

### `last_runned_scenario`
- **Описание**: Название последнего запущенного сценария.
- **Тип**: `str`
- **Значение**: `""` (пустая строка)

### `excluded`
- **Описание**: Список исключенных файлов сценариев.
- **Тип**: `list`
- **Значение**:
  ```json
[
    "bedroom.json",
    "bathroom.json",
    "livingroom.json",
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