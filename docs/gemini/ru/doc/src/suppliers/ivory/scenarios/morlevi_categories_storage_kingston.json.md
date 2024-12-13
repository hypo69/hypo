# Документация для `morlevi_categories_storage_kingston.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Раздел "scenarios"](#раздел-scenarios)
   - [Описание сценариев](#описание-сценариев)
     - [Пример сценария](#пример-сценария)
     - [Свойства сценария](#свойства-сценария)
   - [Ключи сценариев](#ключи-сценариев)
4. [Раздел "presta_categories"](#раздел-presta_categories)
   - [Описание presta_categories](#описание-presta_categories)
   - [Свойства presta_categories](#свойства-presta_categories)
5. [Заключение](#заключение)

## Обзор

Файл `morlevi_categories_storage_kingston.json` содержит JSON-структуру, описывающую различные сценарии для товаров бренда Kingston, предназначенные для использования в системе PrestaShop. Файл структурирован для автоматизации процессов сбора данных и категоризации товаров. Он включает в себя сценарии для различных моделей SSD (SATA и NVMe), а также их объёмы.

## Структура файла

Файл представлен в формате JSON и имеет следующую общую структуру:

```json
{
  "scenarios": {
    "SCENARIO_NAME_1": {
      "brand": "BRAND_NAME",
      "url": "URL_TO_PRODUCT_LISTING",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "kingston": "PRESTA_CATEGORY_NAME"
        }
      }
    },
    "SCENARIO_NAME_2": {
       "brand": "BRAND_NAME",
      "url": "URL_TO_PRODUCT_LISTING",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "kingston": "PRESTA_CATEGORY_NAME"
        }
      }
    },
    ...
  }
}
```

## Раздел "scenarios"

### Описание сценариев

Раздел `scenarios` содержит набор сценариев, где каждый сценарий представляет собой конкретную модель продукта Kingston (в данном случае, SSD накопителей) и правила для её обработки. Каждый сценарий идентифицируется по уникальному ключу (названию сценария).

#### Пример сценария

```json
"KINGSTON NVME GEN4 512GB": {
    "brand": "KINGSTON",
    "url": "https://www.morlevi.co.il/Cat/314?p_315=22&p_175=826&sort=datafloat2%2Cprice&keyword=",
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
        "template": {
            "kingston": "SSD NVME GEN4 512GB"
        }
    }
}
```

#### Свойства сценария

Каждый сценарий включает следующие свойства:

- `brand` (str): Название бренда товара (`KINGSTON`).
- `url` (str): URL-адрес страницы с товарами на сайте поставщика (Morlevi).
- `checkbox` (bool): Логическое значение (всегда `false`), указывающее, что чекбокс не выбран. Возможно, для каких-то других целей.
- `active` (bool): Логическое значение (всегда `true`), указывающее, что сценарий активен.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Раздел с настройками для категорий PrestaShop.

### Ключи сценариев

Ключи сценариев представляют собой названия моделей товаров, например:

- `KINGSTON NVME GEN4 512GB`
- `KINGSTON NVME GEN4 1TB`
- `KINGSTON NVME GEN4 2TB`
- `KINGSTON SATA 3 256GB`
- `KINGSTON SATA 3 512GB`
- `KINGSTON SATA 3 1TB`
- `KINGSTON SATA 3 2TB`
- `KINGSTON SATA 3 4TB`
- `KINGSTON SSD NVME PCIE 256GB`
- `KINGSTON SSD NVME PCIE 512GB`

## Раздел "presta_categories"

### Описание presta_categories

Раздел `presta_categories` содержит информацию о категориях товаров в PrestaShop.

### Свойства presta_categories

Раздел `presta_categories` включает следующие свойства:

- `template` (dict): Словарь с шаблонами соответствия, где ключ - бренд (`kingston`) и значение - категория PrestaShop.

## Заключение

Файл `morlevi_categories_storage_kingston.json` представляет собой структурированный набор данных, предназначенных для автоматизации процессов сбора и категоризации товаров бренда Kingston на платформе PrestaShop. Он обеспечивает гибкую настройку и позволяет легко масштабировать процесс, добавляя новые сценарии. Структура файла проста и понятна, что облегчает её использование и поддержку.