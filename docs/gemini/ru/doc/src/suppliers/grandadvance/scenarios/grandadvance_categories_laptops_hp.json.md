# Документация для `grandadvance_categories_laptops_hp.json`

## Обзор

Файл `grandadvance_categories_laptops_hp.json` содержит конфигурационные данные для определения категорий ноутбуков HP на сайте GrandAdvance. Данные включают в себя информацию о различных моделях ноутбуков HP, их характеристиках (процессор, размер экрана), URL для поиска, CSS-селекторы для фильтров, а также параметры активности, состояния и категории PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура данных](#структура-данных)
    - [Ключи верхнего уровня](#ключи-верхнего-уровня)
    - [Структура вложенных объектов](#структура-вложенных-объектов)
- [Примеры](#примеры)

## Структура данных

Файл представляет собой JSON-объект, где каждый ключ верхнего уровня является названием модели ноутбука HP. Значением каждого ключа является объект с подробными характеристиками и настройками для фильтрации.

### Ключи верхнего уровня

Каждый ключ верхнего уровня представляет собой название модели ноутбука HP, например:
- "HP 11.6 I3"
- "HP 12 i5"
- "HP 13.4 - 13.3 I7"
- и т.д.

### Структура вложенных объектов

Каждый объект, являющийся значением ключа верхнего уровня, имеет следующую структуру:

- `brand` (str): Бренд ноутбука, всегда "HP".
- `url` (str): URL-адрес страницы со списком товаров на сайте GrandAdvance, используемый для парсинга.
- `checkbox` (dict): Словарь, содержащий настройки для фильтрации товаров по характеристикам.
    - `cpu` (dict): Настройки для фильтрации по типу процессора.
        - `class` (str): CSS-класс для элементов фильтра процессора (".fSel").
        - `by` (str): Метод поиска элемента ("css selector").
        - `value` (list): Список возможных значений процессора для фильтрации (например, "CORE I3", "AMD").
    - `screensize` (dict): Настройки для фильтрации по размеру экрана.
        - `class` (str): CSS-класс для элементов фильтра размера экрана (".fSel").
        - `by` (str): Метод поиска элемента ("css selector").
        - `value` (list): Список возможных значений размеров экрана для фильтрации (например, "10.1", "13.3").
- `active` (bool): Флаг, указывающий, активна ли данная конфигурация.
- `condition` (str): Состояние товара, всегда "new".
- `presta_categories` (str): Строка, содержащая ID категорий PrestaShop, разделенных запятыми.

## Примеры

```json
{
  "HP 11.6 I3": {
    "brand": "HP",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=654&manId=38",
    "checkbox": {
      "cpu": {
        "class": ".fSel",
        "by": "css selector",
        "value": [
          "CORE I3",
          "CORE I 3",
          "CORE i3",
          "CORE i 3",
          "Core I3",
          "Core I 3",
          "Core i3",
          "Core i 3",
          "I3",
          "I 3",
          "i3",
          "i 3"
        ]
      },
      "screensize": {
        "class": ".fSel",
        "by": "css selector",
        "value": [ "10.1", "10.2", "10.3", "10.4", "10.5", "10.9", "11", "10,1", "10,2", "10,3", "10,4", "10,5", "10,9" ]
      }
    },
    "active": true,
    "condition": "new",
    "presta_categories": "3,52,8,52,4,362,989"
  },
    "HP 15 Celeron": {
    "brand": "HP",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=654&manId=38",
    "checkbox": {
      "cpu": {
        "class": ".fSel",
        "by": "css selector",
        "value": [
          "CELERON",
          "Celeron",
          "celeron"
        ]
      },
      "screensize": {
        "class": ".fSel",
        "by": "css selector",
        "value": [ "AMD", "15", "15.6", "15,6", "16" ]
      }
    },
    "active": true,
    "condition": "new",
    "presta_categories": "3,11,233,53"
  }
}
```