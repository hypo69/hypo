# Анализ кода модуля `crow_pi.json`

**Качество кода**
    7
-   Плюсы
        -   Структура JSON файла логична и соответствует ожидаемым данным для конфигурации парсинга.
        -   Наличие ключей `supplier`, `supplier_prefix`, `start_url` и `price_rule`  указывает на подготовленность к интеграции в систему парсинга.
        -   Использование `excluded` массива позволяет исключить ненужные файлы сценариев.
-   Минусы
    -   Отсутствуют комментарии в формате reStructuredText (RST), что затрудняет понимание назначения каждого поля.
    -   Использование строк типа `"parcing method [webdriver|api]"`  и `"about method web scrapping [webdriver|api]"` не соответствует стандартам именования ключей.
    -   Некоторые ключи содержат опечатки  (`parcing`).
    -   Поле  `last_runned_scenario`  не имеет описания.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить описание к каждому ключу в формате RST, чтобы улучшить читаемость и понимание структуры JSON.

2.  **Именование ключей:**
    -   Переименовать ключи `parcing method [webdriver|api]` в `parsing_method` и `"about method web scrapping [webdriver|api]"` в `web_scraping_method_description` для ясности и соответствия стандартам.

3.  **Исправление опечаток:**
    -   Исправить опечатку в ключе `parcing method` на `parsing_method`.

4.  **Описание поля:**
    -  Добавить описание к полю `last_runned_scenario`.

**Оптимизированный код**

```json
{
  "supplier": "crow_pi",
  "supplier_prefix": "crow_pi",
  "start_url": "https://www.crowpi.cc/",
  "price_rule": "+0",
  "if_login": false,
  "collect_products_from_categorypage": false,
  "root_category": 3,
  "parsing_method": "web",
  "web_scraping_method_description": "Если я работаю через API мне не нужен webdriver",
  "scenario_files": [
    ".json",
    "ksp_categories_wathces_apple.json"
  ],
  "excluded": [
    "ksp_categories_speakers_google.json",
    "ksp_categories_speakers_jbl.json",
    "ksp_categories_phones_philips.json",
    "ksp_categories_phones_samsung.json",
    "ksp_categories_phones_google.json",
    "ksp_categories_phones_asus.json",
    "ksp_categories_phones_nokia.json",
    "ksp_categories_phones_oppo.json",
    "ksp_categories_phones_oneplus.json",
    "ksp_categories_phones_philips.json",
    "ksp_categories_phones_xiaomi.json",
    "ksp_categories_headphones_bang_olufsen.json",
    "ksp_categories_headphones_hyperx.json",
    "ksp_categories_headphones_jbl.json",
    "ksp_categories_headphones_razer.json",
    "ksp_categories_headphones_sony.json",
    "ksp_categories_headphones_xiaomi.json",
    "ksp_categories_tablets_amazon.json",
    "ksp_categories_tablets_lenovo.json",
    "ksp_categories_tablets_samsung.json",
    "ksp_categories_tablets_xiaomi.json",
    "ksp_categories_iphones.json",
    "ksp_categories_macbook.json",
    "ksp_categories_apple_wathces.json",
    "ksp_categories_ipods.json",
    "ksp_categories_ipads.json",
    "ksp_categories_imacs.json",
    "ksp_categories_consoles_microsoft.json",
    "ksp_categories_consoles_nintendo.json",
    "ksp_categories_notebooks_asus_by_model.json",
    "ksp_categories_notebooks_lenovo_by_model.json",
    "ksp_categories_notebooks_hp_by_model.json",
    "ksp_categories_notebooks_dell_by_model.json",
    "ksp_categories_notebooks_huawei_by_model.json",
    "ksp_categories_speakers_google.json",
    "ksp_categories_speakers_jbl.json",
    "ksp_categories_watches_honor.json",
    "ksp_categories_watches_lenovo.json",
    "ksp_categories_watches_garmin.json",
    "ksp_categories_watches_samsung.json",
    "ksp_categories_watches_xiaomi.json",
    "ksp_categories_watches_amazfit.json",
    "ksp_categories_streamers_google.json",
    "ksp_categories_monitors_samsung.json",
    "ksp_categories_monitors_lg.json"
  ],
  "last_runned_scenario": ""
}
```