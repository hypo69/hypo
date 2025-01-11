# Документация для `morlevi_categories_keyboards_hp.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)

## Обзор

Этот файл `morlevi_categories_keyboards_hp.json` содержит JSON-структуру, определяющую сценарии для категорий товаров бренда HP (клавиатуры и мыши) для использования на сайте Morlevi. Каждый сценарий включает информацию о бренде, URL (который, похоже, является плейсхолдером), активности, состоянии товара и соответствующих категориях PrestaShop.

## Структура JSON

### `scenarios`
Объект, содержащий сценарии для различных моделей клавиатур и мышей HP. Каждый ключ объекта представляет собой название модели.
Каждое поле  объекта сценария  включает:
- **`brand`**: Строка, представляющая бренд товара, в данном случае "HP".
- **`url`**: Строка, представляющая URL, но в большинстве случаев он является плейсхолдером.
- **`checkbox`**: Булево значение, указывающее, должен ли быть чекбокс отмечен, `false` по умолчанию.
- **`active`**: Булево значение, определяющее, активен ли сценарий, `true` по умолчанию.
- **`condition`**: Строка, указывающая состояние товара, в данном случае `new`.
- **`presta_categories`**: Строка, содержащая идентификаторы категорий PrestaShop, разделенные запятыми.

#### Примеры сценариев:
*  **"HP WIRELESS KEYBOARD"**:
    - `brand`: "HP"
    - `url`: "-----------------------------------------------HP WIRELESS KEYBOARD----------------------------------------------"
    - `checkbox`: false
    - `active`: true
    - `condition`: "new"
    - `presta_categories`: "203,204,316"
* **"HP USB KEYBOARD"**:
    - `brand`: "HP"
    - `url`: "-------------------------------------------------------------------------------"
    - `checkbox`: false
    - `active`: true
    - `condition`: "new"
    - `presta_categories`: "203,204,315"
* **"HP USB MOUSE"**:
    - `brand`: "HP"
    - `url`: "------------------------------------------------------HP USB MOUSE------------------------------------------------"
    - `checkbox`: false
    - `active`: true
    - `condition`: "new"
    - `presta_categories`: "203,206,317"
* **"HP WIRELESS MOUSE"**:
    - `brand`: "HP"
    - `url`: "---------------------------------------------------------------------------"
    - `checkbox`: false
    - `active`: true
    - `condition`: "new"
    - `presta_categories`: "203,206,318"
* **"HP USB KEYBOARD-MOUSE SET"**:
    - `brand`: "HP"
    - `url`: "--------------------------------------------------------------------------"
    - `checkbox`: false
    - `active`: true
    - `condition`: "new"
    - `presta_categories`: "203,207,208"
* **"HP WIRELESS  KEYBOARD-MOUSE SET"**:
    - `brand`: "HP"
    - `url`: "https://www.morlevi.co.il/Cat/114?p_315=10&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: false
    - `active`: true
    - `condition`: "new"
    - `presta_categories`: "203,207,334"