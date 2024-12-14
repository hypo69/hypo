# Анализ кода модуля `amazon.json`

**Качество кода**

7
- Плюсы
    - Код представляет собой JSON-конфигурацию, которая хорошо структурирована и понятна.
    - Присутствуют необходимые поля для настройки парсера, такие как `supplier`, `supplier_id`, `start_url` и т.д.
    - Используется `excluded` для списка исключений.
- Минусы
    - Отсутствуют комментарии, поясняющие назначение каждого поля.
    - Названия полей не соответствуют `snake_case` стандарту.
    - Нет документации, описывающей структуру и назначение файла.
    - Некоторые поля, такие как `if_list` и `use_mouse`, не имеют описания, что затрудняет понимание их предназначения.
    - Присутствуют дубликаты в исключениях.
    - Отсутствует проверка на корректность введенных значений.

**Рекомендации по улучшению**

1.  Добавить комментарии в формате RST для описания назначения каждого поля.
2.  Привести имена полей в соответствие со стилем `snake_case`.
3.  Добавить описание структуры JSON файла в формате RST в начало файла.
4.  Указать назначение полей `if_list`, `use_mouse`, `mandatory`, `if_login` и других неявных полей в документации.
5.  Удалить дубликаты из списка исключений `excluded`.
6.  Реализовать проверки на корректность данных в конфигурации при ее использовании.
7.  Добавить описание каждого поля в формате docstring для улучшения читаемости.

**Оптимизированный код**

```json
{
  "supplier": "amazon",
  "supplier_id": "2800",
  "supplier_prefix": "amazon",
  "start_url": "https://www.amazon.com/",
  "price_rule": "+0",
  "if_list": "first",
  "use_mouse": false,
  "mandatory": true,
  "if_login": false,
  "login_url": "https://amazon.com",
  "lang": "EN",
  "check_categories_on_site": false,
  "parsing_via_api": false,
  "collect_products_from_categorypage": false,
  "scenario_files": [
    "amazon_categories_murano_glass.json"
  ],
  "excluded": [
    "amazon_categories_lighting.json",
    "amazon_categories_shelves.json",
    "amazon_categories_consoles.json",
    "amazon_categories_office_chairs.json",
    "amazon_categories_ottomans.json",
    "amazon_categories_desktops_dell_ref.json",
    "amazon_categories_videocards.json",
    "amazon_categories_copmuter_cooling_corsair_new.json",
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
  ],
  "last_runned_scenario": "",
  "last_runned_scenario_filename": ""
}
```