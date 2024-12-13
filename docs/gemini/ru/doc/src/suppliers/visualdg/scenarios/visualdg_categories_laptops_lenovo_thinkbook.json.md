# Документация для `visualdg_categories_laptops_lenovo_thinkbook.json`

## Обзор

Файл `visualdg_categories_laptops_lenovo_thinkbook.json` содержит JSON-конфигурацию для различных моделей ноутбуков Lenovo ThinkBook. Каждый элемент конфигурации представляет собой сценарий для определенной модели, включая ее бренд, шаблон, URL, активность, состояние и категории PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [Ключ "scenarios"](#ключ-scenarios)
    - [Сценарий](#сценарий)
        - [Параметры сценария](#параметры-сценария)
- [Примеры](#примеры)

## Структура JSON

### Ключ "scenarios"

Ключ `"scenarios"` содержит объект, где каждый ключ — это название модели ноутбука Lenovo ThinkBook, а значение — это объект, представляющий собой конфигурацию для этого сценария.

### Сценарий

Каждый сценарий (объект внутри `"scenarios"`) имеет следующие параметры:

#### Параметры сценария

-   `"brand"` (str): Бренд ноутбука, всегда `"LENOVO"`.
-   `"template"` (str): Шаблон, всегда `"THINKBOOK"`.
-   `"url"` (str): URL-адрес, связанный с моделью. Может быть как прямой ссылкой, так и заполнительной строкой.
-   `"checkbox"` (bool): Флаг для чекбокса, всегда `false`.
-   `"active"` (bool): Флаг активности сценария, всегда `true`.
-   `"condition"`(str): Состояние товара, всегда `"new"`.
-   `"presta_categories"` (str): Строка, содержащая идентификаторы категорий PrestaShop, разделенных запятыми.

## Примеры

```json
{
  "scenarios": {
    "LENOVO THINKBOOK 13.4 - 13.3 I3": {
      "brand": "LENOVO",
      "template": "THINKBOOK",
      "url": "-----------------THINKBOOK 13.4 - 13.3 I3-------------r ",
      "checkbox": false,
      "active": true,
      "condition":"new",
       "presta_categories": "3,53,306,9,4,370"
    },
    "LENOVO THINKBOOK 13.4 - 13.3 I5": {
      "brand": "LENOVO",
      "template": "THINKBOOK",
      "url": "https://www.visualdg.co.il/172332-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkBook-/253273/253294",
      "checkbox": false,
      "active": true,
      "condition":"new",
       "presta_categories": "3,53,306,9,5,371"
    },
    "LENOVO THINKBOOK 14 I3": {
      "brand": "LENOVO",
      "template": "THINKBOOK",
      "url": "------------------------LENOVO THINKBOOK 14 I3----------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,53,104,10,4,377"
    },
        "LENOVO THINKBOOK 15 AMD": {
      "brand": "LENOVO",
      "template": "THINKBOOK",
      "url": "----------------LENOVO THINKBOOK 15 AMD------------- ",
      "checkbox": false,
      "active": true,
      "condition":"new",
       "presta_categories": "3,53,105,11,234,388"
    }
  }
}
```

Этот файл используется для настройки параметров и категорий продуктов Lenovo ThinkBook в VisualDG.