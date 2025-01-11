# Документация для `visualdg_categories_laptops_lenovo_thinkpad_p.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание полей](#описание-полей)

## Обзор

Файл `visualdg_categories_laptops_lenovo_thinkpad_p.json` содержит JSON-структуру, описывающую сценарии для категорий ноутбуков Lenovo ThinkPad P в VisualDG. Каждый сценарий представляет собой набор параметров, определяющих соответствие конкретной модели ноутбука Lenovo ThinkPad P.

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "LENOVO  THINKPAD P 14 I5": {
      "brand": "LENOVO",
      "template": "THINKPAD P",
      "url": "-----------------LENOVO  THINKPAD P 14 I-----------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,53,104,10,5,378,838"
    },
    "LENOVO  THINKPAD P 14 I7": {
      "brand": "LENOVO",
      "template": "THINKPAD P",
      "url": "https://www.visualdg.co.il/172327-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-P/253274/253295",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,53,104,10,6,379,838"
    },
    "LENOVO  THINKPAD P 14 I9": {
      "brand": "LENOVO",
      "template": "THINKPAD P",
      "url": "----------------------------- ",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,53,104,10,7,380,838"
    },
    "LENOVO  THINKPAD P 14 AMD": {
      "brand": "LENOVO",
      "template": "THINKPAD P",
      "url": "----------------LENOVO  THINKPAD P 14 AMD--------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,53,104,10,234,381,838"
    },
    "LENOVO   THINKPAD P 15 I5": {
      "brand": "LENOVO",
      "template": "THINKPAD P",
      "url": "-----------------------------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,53,105,11,5,385,838"
    },
    "LENOVO   THINKPAD P 15 I7": {
      "brand": "LENOVO",
      "template": "THINKPAD P",
      "url": "https://www.visualdg.co.il/172327-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-P/253274/253296",
      "checkbox": false,
       "active": true,
       "condition":"new",
      "presta_categories": "3,53,105,11,6,386,838"
    },
    "LENOVO   THINKPAD P 15 I9": {
      "brand": "LENOVO",
      "template": "THINKPAD P",
      "url": "https://www.visualdg.co.il/172327-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-P/253278/253296",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,53,105,11,7,387,838"
    },
    "LENOVO   THINKPAD P 15 AMD": {
      "brand": "LENOVO",
      "template": "THINKPAD P",
      "url": "--------------------LENOVO   THINKPAD P 15 AMD------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,53,105,11,234,388,838"
    }
  }
}
```

## Описание полей

### `scenarios`

- **Описание**: Объект, содержащий набор сценариев для различных моделей ноутбуков Lenovo ThinkPad P.
- **Тип данных**: `object`
- **Содержимое**: Ключами объекта являются названия моделей ноутбуков, а значениями - объекты с параметрами сценариев.

### Поля внутри каждого сценария:

#### `brand`

- **Описание**: Бренд ноутбука.
- **Тип данных**: `string`
- **Пример**: `"LENOVO"`

#### `template`

- **Описание**: Шаблон ноутбука.
- **Тип данных**: `string`
- **Пример**: `"THINKPAD P"`

#### `url`

- **Описание**: URL-адрес, связанный с категорией ноутбука.
- **Тип данных**: `string`
- **Пример**: `"https://www.visualdg.co.il/172327-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-P/253274/253295"` или `"-----------------LENOVO  THINKPAD P 14 I-----------------------"`

#### `checkbox`

- **Описание**: Флаг, указывающий, выбран ли сценарий.
- **Тип данных**: `boolean`
- **Пример**: `false`

#### `active`

- **Описание**: Флаг, указывающий, активен ли сценарий.
- **Тип данных**: `boolean`
- **Пример**: `true`
  
#### `condition`

- **Описание**: Состояние ноутбука (например, "new").
- **Тип данных**: `string`
- **Пример**: `"new"`
  
#### `presta_categories`

- **Описание**: Строка, представляющая ID категорий PrestaShop через запятую.
- **Тип данных**: `string`
- **Пример**: `"3,53,104,10,5,378,838"`