# Анализ кода модуля `bangood.json`

**Качество кода**

*   Соответствие требованиям по оформлению кода: 3/10
*   **Плюсы:**
    *   Структура JSON файла соответствует формату конфигурационного файла.
    *   Присутствуют необходимые поля для настройки парсинга.
*   **Минусы:**
    *   Отсутствует описание структуры JSON файла в формате reStructuredText.
    *   Много лишних комментариев в формате `#`, которые не соответствуют стандарту документации RST.
    *   Использование неконсистентных кавычек в строковых значениях (как двойных, так и одинарных), следует использовать одинарные кавычки.
    *   Присутствует избыточное количество исключений в `excluded` (повторяющиеся вендоры).
    *   Наличие комментариев внутри json, что не является хорошей практикой.

**Рекомендации по улучшению**

1.  Добавить описание структуры JSON файла в формате reStructuredText для документирования назначения каждого поля.
2.  Удалить комментарии в формате `#` внутри JSON, так как это не соответствует стандарту JSON.
3.  Использовать одинарные кавычки (`'`) во всех строковых значениях.
4.  Сократить список исключений `excluded` убрав дубликаты.
5.  Изменить название `parcing method [webdriver|api]` на `parsing_method` и `about method web scrapping [webdriver|api]` на `about_web_scrapping_method` для соответствия ранее используемому code style.
6.  Удалить комментарии внутри файла, добавить необходимые комментарии в виде RST перед файлом.
7.  Добавить логирование и обработку ошибок.

**Оптимизированный код**

```json
{
    "supplier": "ksp",
    "supplier_prefix": "ksp",
    "start_url": "https://www.banggood.com/search/rc-drones.html?last_spm=1a981.SearchResultPage.0001393399.00012138459.bc2a93ecdf3644b08e434b1e6b3f5d05",
    "price_rule": "+100",
    "num_items_4_flush": 300,
    "if_login": false,
    "parsing_method": "web",
     "about_web_scrapping_method": "Если я работаю через API мне не нужен webdriver",
    "collect_products_from_categorypage": false,
    "scenario_files": [
        "ksp_categories_consoles_microsoft.json",
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