# Документация для `techorezef.json`

## Обзор

Данный файл представляет собой JSON-конфигурацию для поставщика "Techorezef". В нем содержатся параметры для скрапинга данных, включая правило ценообразования, количество элементов для сброса, метод парсинга и список файлов сценариев.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [Поставщик](#поставщик)
    - [Префикс поставщика](#префикс-поставщика)
    - [Правило цены](#правило-цены)
    - [Количество элементов для сброса](#количество-элементов-для-сброса)
    - [Метод парсинга](#метод-парсинга)
    - [Метод веб-скрейпинга](#метод-веб-скрейпинга)
    - [Файлы сценариев](#файлы-сценариев)
    - [Последний запущенный сценарий](#последний-запущенный-сценарий)

## Структура JSON

### Поставщик

**Описание**: Название поставщика.
  - `supplier` (str): "Techorezef"

### Префикс поставщика

**Описание**: Префикс для идентификации товаров поставщика.
  - `supplier_prefix` (str): "TRZ-"

### Правило цены

**Описание**: Правило для расчета цены товара.
   - `price_rule` (str): "1.4"

### Количество элементов для сброса

**Описание**: Количество элементов, после которых происходит сброс данных.
  - `num_items_4_flush` (int): 25

### Метод парсинга

**Описание**: Метод, используемый для парсинга данных (webdriver или api).
   -  `parcing method [webdriver|api]` (str): "web"

### Метод веб-скрейпинга

**Описание**: Комментарий о методе веб-скрейпинга.
   - `about method web scrapping [webdriver|api]` (str): "Если я работаю через API мне не нужен webdriver"

### Файлы сценариев

**Описание**: Список файлов сценариев, сгруппированных по типам.
  - `scenario_files` (list):
    - `[ "visualdg_categories_cases_asus.json" ]`
    - `[ "visualdg_categories_desktops_lenovo_workstation_p.json" ]`
    - `[ "visualdg_categories_laptops_asus.json", "visualdg_categories_laptops_lenovo_thinkbook.json", "visualdg_categories_laptops_lenovo_thinkpad_e.json", "visualdg_categories_laptops_lenovo_thinkpad_l.json", "visualdg_categories_laptops_lenovo_thinkpad_p.json", "visualdg_categories_laptops_lenovo_thinkpad_t.json", "visualdg_categories_laptops_lenovo_thinkpad_x.json", "visualdg_categories_laptops_lenovo_v_essentials.json", "visualdg_categories_laptops_lenovo_yoga.json" ]`
    - `[ "visualdg_categories_minipc_asus.json" ]`
    - `[ "visualdg_categories_mb_asus.json" ]`
    - `[ "visualdg_categories_video_asus.json" ]`
    - `[ "visualdg_categories_monitors_asus.json" ]`

### Последний запущенный сценарий

**Описание**: Имя последнего запущенного файла сценария.
  - `last_runned_scenario` (str): ""