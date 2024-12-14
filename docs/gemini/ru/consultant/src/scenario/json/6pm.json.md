# Анализ кода модуля 6pm.json

**Качество кода**

7
- Плюсы
    - Код представляет собой JSON-файл, который содержит конфигурационные данные для парсера.
    - Структура файла логична и понятна.
    - Присутствует разделение на различные секции, что облегчает чтение и понимание.
- Минусы
    - Отсутствует описание предназначения файла и его отдельных ключей в формате RST.
    - Нет комментариев, объясняющих значения полей, что может затруднить понимание их назначения.
    - Не хватает явного указания типов данных для каждого поля.
    - Присутствует неоднородность в написании названий файлов: есть и `ksp_categories_wathces_apple.json` и `ksp_categories_phones_samsung.json`. Это может вызвать ошибки.
    -  В массиве excluded есть дублирование `ksp_categories_phones_philips.json`.

**Рекомендации по улучшению**

1.  **Документирование JSON:**
    -   Добавить подробные комментарии в формате RST к каждому полю JSON, чтобы объяснить его назначение и возможные значения.
    -   Добавить описание модуля в начале файла в формате RST.
2.  **Типизация данных:**
    -   Хотя JSON не имеет строгой типизации, можно добавить комментарии, указывающие на ожидаемый тип данных для каждого поля (например, `string`, `number`, `boolean`, `array`).
3.  **Унификация именования файлов:**
    -   Привести имена файлов в массиве `excluded` к единому виду, например используя `snake_case` для всего списка.
    -   Удалить дубликат `ksp_categories_phones_philips.json`.
4. **Использовать j_loads:**
     - При чтении данного json файла использовать `j_loads_ns` из `src.utils.jjson`.
5.  **Логирование:**
    -   Добавить логирование в случае ошибок при загрузке JSON-файла.

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