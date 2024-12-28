# Анализ кода модуля `morlevi_categories_cpu.json`

**Качество кода**
7
-  Плюсы
    - Код представляет собой JSON-структуру, которая хорошо читается и легко парсится.
    - Структура данных четкая и логичная, содержит необходимые поля для описания категорий CPU.
    - Присутствует поле `active` для управления активностью каждой категории.
-  Минусы
    - Отсутствуют комментарии, описывающие назначение полей и структуры данных.
    - В некоторых местах структура `presta_categories`  дублируется, в других есть `template` c вложенным `cpu`.
    - Имена ключей в структуре (`Intel CELERON LGA1200 Gen 10`) не соответствуют PEP8 и могут быть более стандартизированы.
    - Некоторые URL выглядят повторяющимися и могут быть параметризованными.
    - Значения `sort=datafloat2%2Cprice&keyword=` могут быть вынесены в отдельную переменную.
    - Есть неточности в значениях `cpu`  например `I9 LGA1200` и `I7 LGA1200`.
    - Не все URL используют параметры `p_134`

**Рекомендации по улучшению**

1. **Добавить комментарии**:
   - Добавить описание структуры JSON.
   - Описать назначение каждого поля (`brand`, `url`, `checkbox`, `active`, `condition`, `presta_categories`, `template`, `cpu`).
   - Добавить описания для каждой категории CPU.

2. **Унификация структуры**:
   - Привести к единому виду структуру `presta_categories`, избавившись от `template`, т.е. сделать  `{"cpu": "значение"}`.

3. **Стандартизация имен ключей**:
   - Привести имена ключей (`Intel CELERON LGA1200 Gen 10`) к более стандартному виду (`intel_celeron_lga1200_gen10`) для облегчения работы с кодом.

4. **Параметризация URL**:
   - Вынести общие части URL и параметры в переменные для уменьшения дублирования кода.

5. **Вынесение общих параметров**:
   - Вынести параметры `sort=datafloat2%2Cprice&keyword=` в отдельную переменную.

6. **Устранить неточности**:
   - Исправить значения `cpu` в соответствии с названиями ключей.

7. **Привести все URL к единому виду**:
   - Добавить ко всем URL параметр `p_134`  где это необходимо, например, для `I5 LGA1700 13` , `I7 LGA1700 13` и `I9 LGA1700 12`.

**Оптимизированный код**

```json
{
  "scenarios": {
    "intel_celeron_lga1200_gen10": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/337?p_134=584&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "INTEL CELERON LGA1200"
      }
    },
    "intel_celeron_lga1200_gen11": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/363?p_134=584&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "INTEL CELERON LGA1200"
      }
    },
    "intel_pentium_lga1200_gen10": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/337?p_134=585&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
       "condition": "new",
      "presta_categories": {
        "cpu": "INTEL PENTIUM LGA1200"
      }
    },
    "i3_lga1200": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/337?p_134=586&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I3 LGA1200"
      }
    },
    "i5_lga1200": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/399?p_134=587&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I5 LGA1200"
      }
    },
    "i5_lga1200_11": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/363?p_134=587&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I5 LGA1200"
      }
    },
    "i5_lga1700_12": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/380?p_134=587&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I5 LGA1700"
      }
    },
     "i5_lga1700_13": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/399?p_134=587&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I5 LGA1700"
      }
    },
    "i7_lga1200": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/399?p_134=588&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I7 LGA1200"
      }
    },
    "i7_lga1200_11": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/363?p_134=588&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I7 LGA1200"
      }
    },
    "i7_lga1700_12": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/380?p_134=588&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
       "presta_categories": {
        "cpu": "I7 LGA1700"
      }
    },
    "i7_lga1700_13": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/399?p_134=588&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I7 LGA1700"
      }
    },
    "i9_lga1200": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/399?p_134=588&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I9 LGA1200"
      }
    },
      "i9_lga1700_12": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/380?p_134=848&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I9 LGA1700"
      }
    },
    "i9_lga1700_13": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/399?p_134=848&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "cpu": "I9 LGA1700"
      }
    }
  }
}
```