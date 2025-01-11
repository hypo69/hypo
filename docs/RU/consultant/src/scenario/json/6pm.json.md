# Анализ кода модуля `6pm.json`

**Качество кода**
7
- Плюсы
    - Код представляет собой JSON-файл, который соответствует структуре, ожидаемой для сценариев.
    - Структура файла логически понятна и содержит необходимые поля для определения параметров поставщика, правил сбора данных и исключений.
    - Присутствует поле `excluded`, позволяющее исключать определенные категории товаров, что улучшает управляемость процесса сбора данных.
- Минусы
    - Отсутствует описание назначения файла или его структуры.
    - Нет комментариев или документации, объясняющих назначение каждого поля.
    - В `scenario_files` указано расширение ".json", что может быть не совсем корректно, поскольку подразумевается, что в этом поле должен находиться список конкретных файлов, а не расширений.
    - Стилистически вложенность в `excluded` не очень удобна.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла, используя reStructuredText.
2.  Добавить документацию для каждого поля, объясняя его назначение и ожидаемые значения.
3.  Уточнить значение поля `scenario_files`, либо убрать расширение ".json" и указать конкретный файл.
4.  Пересмотреть структуру вложенности в `excluded`, либо оставить как есть.

**Оптимизированный код**

```json
{
  "supplier": "6pm",
  "supplier_prefix": "6pm",
  "start_url": "https://www.6pm.com/",
  "price_rule": "+0",
  "if_login": false,
  "collect_products_from_categorypage": false,
  "root_category": 3,
  "scenario_files": [
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