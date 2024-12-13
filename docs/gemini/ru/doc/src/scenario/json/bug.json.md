# Документация для `bug.json`

## Обзор

Файл `bug.json` содержит конфигурацию для поставщика "bug", включая префикс, начальный URL, правила обработки, список файлов сценариев и другие настройки, необходимые для выполнения сбора данных.

## Содержание

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
  - [supplier](#supplier)
  - [supplier_prefix](#supplier_prefix)
  - [start_url](#start_url)
  - [if_list](#if_list)
  - [use_mouse](#use_mouse)
  - [mandatory](#mandatory)
  - [price_rule](#price_rule)
  - [num_items_4_flush](#num_items_4_flush)
  - [scenario_files](#scenario_files)
  - [last_runned_scenario](#last_runned_scenario)

## Структура файла

### `supplier`

**Описание**: Название поставщика.

**Тип**: `str`

**Значение**: `"bug"`

### `supplier_prefix`

**Описание**: Префикс для идентификатора товара.

**Тип**: `str`

**Значение**: `"BUG-"`

### `start_url`

**Описание**: Начальный URL для сбора данных.

**Тип**: `str`

**Значение**: `"https://www.bug.co.il/"`

### `if_list`

**Описание**: Условие для обработки списков (например, "первый").

**Тип**: `str`

**Значение**: `"first"`

### `use_mouse`

**Описание**: Флаг, указывающий на необходимость использования мыши.

**Тип**: `bool`

**Значение**: `false`

### `mandatory`

**Описание**: Флаг, указывающий на обязательность выполнения сценария.

**Тип**: `bool`

**Значение**: `true`

### `price_rule`

**Описание**: Правило ценообразования.

**Тип**: `str`

**Значение**: `"1"`

### `num_items_4_flush`

**Описание**: Количество элементов для сброса данных.

**Тип**: `int`

**Значение**: `300`

### `scenario_files`

**Описание**: Список файлов сценариев, сгруппированных в массивы. Каждый массив представляет собой этап сбора данных.

**Тип**: `list[list[str]]`

**Значение**:
```json
[
    [
      "cdata_categories_aio_asus.json",
      "cdata_categories_aio_dell.json",
      "cdata_categories_aio_hp.json"
    ],
    [
      "cdata_categories_desktops.json",
      "cdata_categories_gaming_desktops.json",
      "cdata_categories_workstatios.json"
    ],
    [
      "cdata_categories_laptops_asus.json",
      "cdata_categories_laptops_dell.json",
      "cdata_categories_laptops_hp.json",
      "cdata_categories_gaming_laptops_asus.json",
      "cdata_categories_gaming_laptops_dell.json",
      "cdata_categories_gaming_laptops_hp.json"
    ],
    [
      "cdata_categories_monitors_apple.json",
      "cdata_categories_monitors_dell.json",
      "cdata_categories_monitors_hp.json"
    ],
    [ "cdata_categories_keyboards.json" ],
    [ "cdata_categories_printers.json" ],
    [ "cdata_categories_webcams.json" ],
    [ "cdata_categories_video.json" ],
    [ "cdata_categories_ups.json" ]
  ]
```

### `last_runned_scenario`

**Описание**: Имя последнего выполненного сценария.

**Тип**: `str`

**Значение**: `""` (пустая строка, что означает отсутствие выполненного сценария)