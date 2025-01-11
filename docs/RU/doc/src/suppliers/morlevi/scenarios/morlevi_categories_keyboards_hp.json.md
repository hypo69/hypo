# Документация для `morlevi_categories_keyboards_hp.json`

## Обзор

Данный файл содержит JSON-конфигурацию сценариев для парсинга категорий клавиатур и мышей бренда HP с сайта Morlevi. Каждый сценарий определяет параметры для конкретного типа продукта, такие как URL, марку, активность, состояние и категории PrestaShop.

## Оглавление
1. [Обзор](#Обзор)
2. [Структура JSON](#Структура-JSON)
3. [Описание сценариев](#Описание-сценариев)
    - [HP WIRELESS KEYBOARD](#HP-WIRELESS-KEYBOARD)
    - [HP USB KEYBOARD](#HP-USB-KEYBOARD)
    - [HP USB MOUSE](#HP-USB-MOUSE)
    - [HP WIRELESS MOUSE](#HP-WIRELESS-MOUSE)
    - [HP USB KEYBOARD-MOUSE SET](#HP-USB-KEYBOARD-MOUSE-SET)
    - [HP WIRELESS KEYBOARD-MOUSE SET](#HP-WIRELESS-KEYBOARD-MOUSE-SET)

## Структура JSON

Файл имеет следующую структуру:

```json
{
  "scenarios": {
    "PRODUCT_NAME_1": {
      "brand": "BRAND_NAME",
      "url": "PRODUCT_URL",
      "checkbox": BOOLEAN,
      "active": BOOLEAN,
      "condition": "PRODUCT_CONDITION",
      "presta_categories": "CATEGORY_IDS"
    },
    "PRODUCT_NAME_2": {
      "brand": "BRAND_NAME",
      "url": "PRODUCT_URL",
      "checkbox": BOOLEAN,
      "active": BOOLEAN,
      "condition": "PRODUCT_CONDITION",
      "presta_categories": "CATEGORY_IDS"
    },
    "...": {
    
    }
  }
}
```

Где:
- `"scenarios"`:  Объект, содержащий все сценарии.
- `"PRODUCT_NAME_X"`: Ключ - имя продукта, являющееся уникальным идентификатором для сценария.
- `"brand"`: Строка, указывающая марку продукта (например, "HP").
- `"url"`: Строка, представляющая URL-адрес, используемый для парсинга (или просто разделитель в виде строки).
- `"checkbox"`: Логическое значение, указывающее, включен ли сценарий (используется, например, для ручного включения/выключения, всегда `false` в данном случае).
- `"active"`: Логическое значение, указывающее, активен ли сценарий (всегда `true` в данном случае).
- `"condition"`: Строка, указывающая состояние товара (например, "new").
- `"presta_categories"`: Строка, содержащая идентификаторы категорий PrestaShop через запятую (например, "203,204,316").

## Описание сценариев

### `HP WIRELESS KEYBOARD`
    
**Описание**: Сценарий для парсинга беспроводных клавиатур HP.

**Параметры**:

-   `brand` (str): `"HP"`
-   `url` (str): `"-----------------------------------------------HP WIRELESS KEYBOARD----------------------------------------------"`
-   `checkbox` (bool): `false`
-   `active` (bool): `true`
-   `condition` (str): `"new"`
-   `presta_categories` (str): `"203,204,316"`
    
### `HP USB KEYBOARD`

**Описание**: Сценарий для парсинга USB-клавиатур HP.
    
**Параметры**:

-   `brand` (str): `"HP"`
-   `url` (str): `"-------------------------------------------------------------------------------"`
-   `checkbox` (bool): `false`
-   `active` (bool): `true`
-   `condition` (str): `"new"`
-   `presta_categories` (str): `"203,204,315"`

### `HP USB MOUSE`

**Описание**: Сценарий для парсинга USB-мышей HP.

**Параметры**:

-   `brand` (str): `"HP"`
-   `url` (str): `"------------------------------------------------------HP USB MOUSE------------------------------------------------"`
-   `checkbox` (bool): `false`
-   `active` (bool): `true`
-   `condition` (str): `"new"`
-   `presta_categories` (str): `"203,206,317"`

### `HP WIRELESS MOUSE`

**Описание**: Сценарий для парсинга беспроводных мышей HP.

**Параметры**:

-   `brand` (str): `"HP"`
-   `url` (str): `"---------------------------------------------------------------------------"`
-   `checkbox` (bool): `false`
-   `active` (bool): `true`
-   `condition` (str): `"new"`
-   `presta_categories` (str): `"203,206,318"`

### `HP USB KEYBOARD-MOUSE SET`

**Описание**: Сценарий для парсинга комплектов USB-клавиатура + мышь HP.
   
**Параметры**:

-   `brand` (str): `"HP"`
-   `url` (str): `"--------------------------------------------------------------------------"`
-   `checkbox` (bool): `false`
-   `active` (bool): `true`
-   `condition` (str): `"new"`
-   `presta_categories` (str): `"203,207,208"`

### `HP WIRELESS KEYBOARD-MOUSE SET`

**Описание**: Сценарий для парсинга беспроводных комплектов клавиатура + мышь HP.
    
**Параметры**:

-   `brand` (str): `"HP"`
-   `url` (str): `"https://www.morlevi.co.il/Cat/114?p_315=10&sort=datafloat2%2Cprice&keyword="`
-   `checkbox` (bool): `false`
-   `active` (bool): `true`
-   `condition` (str): `"new"`
-   `presta_categories` (str): `"203,207,334"`