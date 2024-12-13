# Документация для `hypotez/src/scenario/json/cdata.json`

## Обзор

Файл `cdata.json` представляет собой конфигурационный файл в формате JSON, описывающий параметры и сценарии для сбора данных с веб-сайта поставщика "cdata". Этот файл содержит информацию о поставщике, правилах ценообразования, методах парсинга и списках файлов сценариев.

## Содержание

- [Основные параметры](#основные-параметры)
- [Сценарии](#сценарии)

## Основные параметры

### `supplier`

**Описание**: Название поставщика.

**Значение**: `"cdata"`

### `supplier_prefix`

**Описание**: Префикс для идентификации товаров поставщика.

**Значение**: `"CDT-"`

### `if_list`

**Описание**:  Указывает порядок обработки списков.

**Значение**: `"first"`

### `use_mouse`

**Описание**: Указывает, нужно ли использовать мышь при парсинге.

**Значение**: `false`

### `mandatory`

**Описание**: Указывает, является ли обязательным данный сценарий.

**Значение**: `true`

### `start_url`

**Описание**: Начальный URL-адрес веб-сайта поставщика.

**Значение**: `"https://www.c-data.co.il/"`

### `price_rule`

**Описание**: Правило ценообразования.

**Значение**: `"3.5*1.17"`

### `num_items_4_flush`

**Описание**: Количество элементов для сброса (flush).

**Значение**: `300`

### `parcing method [webdriver|api]`

**Описание**: Метод парсинга данных. Может быть "webdriver" или "api".

**Значение**: `"web"`

### `about method web scrapping [webdriver|api]`

**Описание**: Описание метода веб-скреппинга.

**Значение**: `"Если я работаю через API мне не нужен webdriver"`

## Сценарии

### `scenario_files`

**Описание**: Массив массивов, каждый из которых содержит список файлов сценариев для различных категорий товаров.

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

**Описание**: Имя последнего запущенного сценария.

**Значение**: `""`