# Документация для `visualdg.json`

## Обзор

Файл `visualdg.json` содержит конфигурационные данные для сбора информации о товарах с веб-сайта `www.visualdg.co.il`. Он определяет параметры поставщика, правила ценообразования, список сценариев парсинга, и другие настройки для процесса извлечения данных.

## Оглавление

1. [Обзор](#обзор)
2. [Основные параметры](#основные-параметры)
3. [Правила ценообразования](#правила-ценообразования)
4. [Параметры сбора данных](#параметры-сбора-данных)
5. [Сценарии парсинга](#сценарии-парсинга)
6. [Последний запущенный сценарий](#последний-запущенный-сценарий)

## Основные параметры

### `supplier`

**Описание**: Идентификатор поставщика.

**Значение**: `visualdg`

### `supplier_prefix`

**Описание**: Префикс, используемый для идентификации товаров поставщика.

**Значение**: `VDG-`

### `start_url`

**Описание**: URL стартовой страницы веб-сайта для сбора данных.

**Значение**: `https://www.visualdg.co.il/`

## Правила ценообразования

### `price_rule`

**Описание**: Правило для расчета цены товара.

**Значение**: `*1.43`

## Параметры сбора данных

### `if_list`
   
**Описание**: Условие выбора списка.

**Значение**: `first`

### `use_mouse`

**Описание**: Флаг, указывающий, использовать ли эмуляцию мыши.

**Значение**: `false`

### `mandatory`
   
**Описание**: Флаг, указывающий является ли обязательным парсинг.

**Значение**: `true`

### `num_items_4_flush`

**Описание**: Количество элементов для сохранения в промежуточный файл.

**Значение**: `25`

### `collect_products_from_categorypage`

**Описание**: Флаг, определяющий, нужно ли собирать товары со страниц категорий.

**Значение**: `false`

### `parcing method [webdriver|api]`

**Описание**: Метод парсинга данных, либо через `webdriver` либо через `api`.

**Значение**: `web`

### `about method web scrapping [webdriver|api]`

**Описание**: Описание метода парсинга.

**Значение**: `Если я работаю через API мне не нужен webdriver`

## Сценарии парсинга

### `scenario_files`

**Описание**: Массив, содержащий списки файлов сценариев для различных категорий товаров.

**Значение**:

   ```json
    [
      [
        "visualdg_categories_laptops_asus.json",
        "visualdg_categories_laptops_lenovo_thinkbook.json",
        "visualdg_categories_laptops_lenovo_thinkpad_e.json",
        "visualdg_categories_laptops_lenovo_thinkpad_l.json",
        "visualdg_categories_laptops_lenovo_thinkpad_p.json",
        "visualdg_categories_laptops_lenovo_thinkpad_t.json",
        "visualdg_categories_laptops_lenovo_thinkpad_x.json",
        "visualdg_categories_laptops_lenovo_v_essentials.json",
        "visualdg_categories_laptops_lenovo_yoga.json"
      ],
      [ "visualdg_categories_desktops_lenovo_workstation_p.json" ],
      [ "visualdg_categories_cases_asus.json" ],
      [ "visualdg_categories_minipc_asus.json" ],
      [ "visualdg_categories_mb_asus.json" ],
      [ "visualdg_categories_video_asus.json" ],
      [ "visualdg_categories_monitors_asus.json" ]
    ]
   ```

## Последний запущенный сценарий

### `last_runned_scenario`

**Описание**: Имя последнего запущенного сценария парсинга.

**Значение**: `""` (пустая строка)