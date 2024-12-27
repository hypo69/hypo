# Анализ кода модуля `amazon.json`

**Качество кода**

7
- Плюсы
    - Структура файла соответствует формату JSON.
    - Присутствуют основные поля, необходимые для конфигурации поставщика (supplier, start_url, price_rule и т.д.).
    - Есть разделение на включенные и исключенные сценарии, что позволяет гибко управлять процессом парсинга.
- Минусы
    - Отсутствует какая-либо документация по назначению полей.
    - Нет явного описания типов данных для полей.
    - Наличие полей `last_runned_scenario` и `last_runned_scenario_filename` может указывать на необходимость рефакторинга, для сохранения состояния, и вынесение этого функционала из json.
    - Некоторые названия полей не соответствуют принятому code style (например, `check categories on site`).
    - Несоответствие в названии ключей, например, `parsing via api` но  `collect_products_from_categorypage`.

**Рекомендации по улучшению**

1. **Добавить документацию:**
   - Добавить описание каждого поля, указать его тип и назначение.
   - Привести примеры допустимых значений для каждого поля.
2. **Переименовать ключи:**
    - Использовать snake_case для всех ключей, например `check_categories_on_site`.
    - Привести в соответствие названия ключей, например `parse_via_api` или `collect_products_from_category_page`.
3. **Уточнить назначение:**
   - Уточнить назначение полей `last_runned_scenario` и `last_runned_scenario_filename`, и вынести этот функционал в отдельный объект или функцию.
4. **Использовать единый стиль:**
    - Привести все названия полей к единому стилю, snake_case.
5.  **Улучшить читаемость:**
   - Добавить отступы и переводы строк для улучшения читаемости.

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
  "parse_via_api": false,
  "collect_products_from_category_page": false,
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
    "amazon_categories_desktops_dell_ref.json",
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