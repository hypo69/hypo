# Документация для `grandadvance_categories_keyboards_hp.json`

## Обзор

Данный JSON файл содержит конфигурацию категорий для продукции HP (клавиатуры и мыши) для сайта Grand Advance. В файле определены различные типы устройств (проводные и беспроводные клавиатуры и мыши, а также комплекты), их бренды, URL-адреса страниц с этими товарами на сайте Grand Advance, а также их сопоставление с категориями PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Описание полей](#описание-полей)

## Структура JSON

JSON файл представляет собой словарь, где ключи - это названия продуктов, а значения - это словари с детальной информацией о каждом продукте.

```json
{
  "HP WIRELESS KEYBOARD": {
    "brand": "HP",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=585&manid=116",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,204,316"
  },
  "HP USB KEYBOARD": {
    "brand": "HP",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=587&manId=38",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,204,315"
  },
  "HP USB MOUSE": {
    "brand": "HP",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=587&manid=116",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,206,317"
  },
  "HP WIRELESS MOUSE": {
    "brand": "HP",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=586&manid=116",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,206,318"
  },
  "HP USB KEYBOARD-MOUSE SET": {
    "brand": "HP",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manid=116",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,207,208"
  },
  "HP WIRELESS  KEYBOARD-MOUSE SET": {
    "brand": "HP",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manid=116",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,207,334"
  }
}
```

## Описание полей

Каждый элемент словаря в JSON файле, представляет собой словарь со следующими полями:

-   `brand` (str): Бренд продукта (в данном случае всегда "HP").
-   `url` (str): URL-адрес страницы продукта на сайте Grand Advance.
-   `checkbox` (bool): Логическое значение, указывающее на состояние чекбокса (всегда `false`).
-   `active` (bool): Логическое значение, указывающее на активность товара (всегда `true`).
-   `condition` (str): Состояние продукта (всегда "new").
-   `presta_categories` (str): Строка, содержащая идентификаторы категорий PrestaShop, к которым принадлежит продукт, разделенные запятыми.