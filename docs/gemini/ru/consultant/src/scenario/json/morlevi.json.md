# Анализ кода модуля `morlevi.json`

**Качество кода**
8
-  Плюсы
    - Код представляет собой JSON-файл, который является стандартным форматом для хранения данных и легко читается.
    - Структура файла логически организована, что облегчает понимание его содержимого.
    - Файл содержит все необходимые поля для настройки сценария парсинга, такие как `supplier`, `supplier_id`, `start_url` и другие.
 -  Минусы
    - Отсутствуют комментарии, поясняющие назначение каждого поля, что может затруднить понимание структуры файла для новых пользователей.
    - Использование магических чисел (например, `1.43` в `price_rule`) без объяснения их значения может снизить читаемость.
    - Некоторые поля, такие как `"about method web scrapping [webdriver|api]"` содержат неформатированный текст, который должен быть описан в виде reStructuredText (RST).
    - `if_list` принимает значение `"first"`, но нет описания, какие значения еще может принимать и как это работает.

**Рекомендации по улучшению**

1.  Добавить комментарии в формате RST для каждого поля, объясняющие его назначение и возможные значения.
2.  Заменить магические числа на константы с понятными именами.
3.  Уточнить возможные значения и принцип работы поля `if_list`.
4.  Удалить лишние пробелы.
5.  Преобразовать поясняющий текст `"about method web scrapping [webdriver|api]"` в reStructuredText.
6.  Заменить `parcing method [webdriver|api]` на `parsing_method` .
7.  Удалить `last_runned_scenario`, так как он не используется в коде.

**Оптимизированный код**

```json
{
  "supplier": "morlevi",
  "supplier_id": "2784",
  "supplier_prefix": "mlv",
  "start_url": "https://www.morlevi.co.il/",
  "login_url": "https://www.morlevi.co.il/",
  "price_rule": "*1.43",
  "if_list":"first",
  "use_mouse": false,
  "mandatory": true,
  "collect_products_from_categorypage": false,
  "num_items_4_flush": 500,
  "if_login": true,
  "parsing_method": "web",
    "about_method_web_scrapping": "Если я работаю через API мне не нужен webdriver",
  "scenario_files": [
    { "$ref": "morlevi_categories_cases_antec.json#" },
    "morlevi_categories_storage_samsung.json",
    "morlevi_categories_storage_kingston.json",
    "morlevi_categories_video.json",
    "morlevi_categories_monitors_samsung.json",
    "morlevi_categories_monitors_lenovo.json",
    "morlevi_categories_mb_gigabyte.json",
    "morlevi_categories_cases_coolermaster.json",
    "morlevi_categories_cases_corsair.json",
    "morlevi_categories_cases_generic.json",
    "morlevi_categories_headsets.json",
    "morlevi_categories_laptops_asus.json",
    "morlevi_categories_laptops_gigabyte.json",
    "morlevi_categories_laptops_dell.json",
    "morlevi_categories_laptops_hp.json",
    "morlevi_categories_laptops_lenovo.json",
    "morlevi_categories_memory.json",
    "morlevi_categories_cpu.json",
    "morlevi_categories_cases_antec.json"
  ],
  "excluded": [
    [],
    [
      "morlevi_categories_minipc_gigabyte.json",
      "morlevi_categories_minipc_intel.json"
    ],
    [
      "morlevi_categories_video.json"
    ],
    [
      "morlevi_categories_memory_dimm_ddr4.json",
      "morlevi_categories_memory_sodimm_ddr3.json",
      "morlevi_categories_memory_sodimm_ddr4.json"
    ],
    [
      "morlevi_categories_monitors_aoc.json",
      "morlevi_categories_monitors_dell.json",
      "morlevi_categories_monitors_lenovo.json",
      "morlevi_categories_monitors_philips.json",
      "morlevi_categories_monitors_mag.json"
    ],
    [
      "morlevi_categories_psu_antec.json",
      "morlevi_categories_psu_cooler_maser.json",
      "morlevi_categories_psu_gigabyte.json",
      "morlevi_categories_psu_corsair.json"
    ],
    [
      "morlevi_categories_sound.json"
    ],
    [
      "morlevi_categories_storage_crucial.json",
      "morlevi_categories_storage_gigabyte.json",
      "morlevi_categories_storage_intel.json",
      "morlevi_categories_storage_kingston.json",
      "morlevi_categories_storage_samsung.json",
      "morlevi_categories_storage_sandisk.json",
      "morlevi_categories_storage_toshiba.json",
      "morlevi_categories_storage_wd.json"
    ],
    [
      "morlevi_categories_ups.json"
    ],
    [
      "morlevi_categories_printers.json"
    ],
    [],
    [
      "morlevi_categories_cases_zalman.json"
    ],
    [
      "morlevi_categories_keyboards_coolermaster.json",
      "morlevi_categories_keyboards_genius.json",
      "morlevi_categories_keyboards_hp.json",
      "morlevi_categories_keyboards_logitech.json",
      "morlevi_categories_keyboards_microsoft.json"
    ],
    [
      "morlevi_categories_network.json"
    ],
    [
      "morlevi_categories_printers.json"
    ]
  ]
}
```