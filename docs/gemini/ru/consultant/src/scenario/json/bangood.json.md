# Анализ кода модуля `bangood.json`

**Качество кода**

8
-  Плюсы
    - Код представляет собой JSON-файл, который используется для конфигурации. Структура файла логична и понятна, включает в себя необходимые параметры для парсинга данных с сайта Banggood. 
    - Присутствуют подробные комментарии, описывающие назначение некоторых полей, хотя они и не соответствуют стандарту reStructuredText (RST).
    - Указаны исключения (`excluded`) для категорий товаров, которые не нужно обрабатывать.

-  Минусы
    - Отсутствуют docstring в начале файла, который бы описывал назначение данного JSON-файла.
    - Комментарии в файле не соответствуют стандарту RST.
    - Есть избыточность в описании полей, например `"about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver"`.
    - Названия полей местами не соответствуют змеиному регистру (snake_case).
    - Значение `"parcing method [webdriver|api]": "web"`  должно быть `"parsing_method": "web"`.
    - Использовано не стандартное написание `num_items_4_flush` , лучше `num_items_for_flush`.
    
**Рекомендации по улучшению**
1. Добавить docstring в начале файла с описанием его назначения и структуры.
2. Переписать все комментарии в формате RST, где это необходимо.
3. Переименовать ключи для соответствия snake_case.
4. Заменить `parcing` на `parsing`.
5.  Переименовать `num_items_4_flush` в `num_items_for_flush`.
6.  Удалить избыточные комментарии.

**Оптимизированный код**
```json
{
  "supplier": "ksp",
  "supplier_prefix": "ksp",
  "start_url": "https://www.banggood.com/search/rc-drones.html?last_spm=1a981.SearchResultPage.0001393399.00012138459.bc2a93ecdf3644b08e434b1e6b3f5d05",
  "price_rule": "+100",
  "num_items_for_flush": 300,
  "if_login": false,
  "parsing_method": "web",
  "about_method_web_scrapping": "Если я работаю через API мне не нужен webdriver",
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