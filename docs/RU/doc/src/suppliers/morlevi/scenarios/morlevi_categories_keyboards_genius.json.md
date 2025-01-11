# Документация для `morlevi_categories_keyboards_genius.json`

## Обзор

Данный файл содержит JSON-структуру, определяющую сценарии для категорий товаров "GENIUS", связанных с клавиатурами и мышками. Каждый сценарий включает в себя информацию о бренде, URL для поиска товаров, статусе чекбокса, активности и условиях (condition) , а также связанных с категориями PrestaShop.

## Оглавление
- [Обзор](#Обзор)
- [Структура JSON](#Структура-JSON)
    - [Сценарии](#Сценарии)
        - [GENIUS WIRELESS KEYBOARD](#GENIUS-WIRELESS-KEYBOARD)
        - [GENIUS USB KEYBOARD](#GENIUS-USB-KEYBOARD)
        - [GENIUS USB MOUSE](#GENIUS-USB-MOUSE)
        - [GENIUS WIRELESS MOUSE](#GENIUS-WIRELESS-MOUSE)
        - [GENIUS USB KEYBOARD-MOUSE SET](#GENIUS-USB-KEYBOARD-MOUSE-SET)
        - [GENIUS WIRELESS KEYBOARD-MOUSE SET](#GENIUS-WIRELESS-KEYBOARD-MOUSE-SET)


## Структура JSON

### Сценарии
JSON содержит объект `scenarios`, который представляет собой словарь, где каждый ключ — это название сценария (например, `"GENIUS WIRELESS KEYBOARD"`), а значение — это объект с подробными параметрами сценария.

#### `GENIUS WIRELESS KEYBOARD`

**Описание**: Сценарий для беспроводных клавиатур GENIUS.

**Параметры**:
- `brand` (str): Название бренда, в данном случае "GENIUS".
- `url` (str):  URL для поиска товаров.
- `checkbox` (bool): Статус чекбокса (false).
- `active` (bool):  Активность сценария (true).
- `condition` (str): Состояние товара ("new").
- `presta_categories` (str): Строка с ID категорий PrestaShop, разделенными запятыми "203,204,316".

#### `GENIUS USB KEYBOARD`

**Описание**: Сценарий для USB клавиатур GENIUS.

**Параметры**:
- `brand` (str): Название бренда, в данном случае "GENIUS".
- `url` (str): URL для поиска товаров: "https://www.morlevi.co.il/Cat/155?p_315=43&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): Статус чекбокса (false).
- `active` (bool): Активность сценария (true).
- `condition` (str): Состояние товара ("new").
- `presta_categories` (str): Строка с ID категорий PrestaShop, разделенными запятыми "203,204,315".

#### `GENIUS USB MOUSE`

**Описание**: Сценарий для USB мышей GENIUS.

**Параметры**:
- `brand` (str): Название бренда, в данном случае "GENIUS".
- `url` (str): URL для поиска товаров: "https://www.morlevi.co.il/Cat/108?p_315=43&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): Статус чекбокса (false).
- `active` (bool): Активность сценария (true).
- `condition` (str): Состояние товара ("new").
- `presta_categories` (str): Строка с ID категорий PrestaShop, разделенными запятыми "203,206,317".

#### `GENIUS WIRELESS MOUSE`

**Описание**: Сценарий для беспроводных мышей GENIUS.

**Параметры**:
- `brand` (str): Название бренда, в данном случае "GENIUS".
- `url` (str): URL для поиска товаров: "https://www.morlevi.co.il/Cat/109?p_315=43&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): Статус чекбокса (false).
- `active` (bool): Активность сценария (true).
- `condition` (str): Состояние товара ("new").
- `presta_categories` (str): Строка с ID категорий PrestaShop, разделенными запятыми "203,206,318".

#### `GENIUS USB KEYBOARD-MOUSE SET`

**Описание**: Сценарий для наборов USB клавиатура + мышь GENIUS.

**Параметры**:
- `brand` (str): Название бренда, в данном случае "GENIUS".
- `url` (str): URL для поиска товаров: "https://www.morlevi.co.il/Cat/113?p_315=43&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): Статус чекбокса (false).
- `active` (bool): Активность сценария (true).
- `condition` (str): Состояние товара ("new").
- `presta_categories` (str): Строка с ID категорий PrestaShop, разделенными запятыми "203,207,208".

#### `GENIUS WIRELESS KEYBOARD-MOUSE SET`

**Описание**: Сценарий для наборов беспроводная клавиатура + мышь GENIUS.

**Параметры**:
- `brand` (str): Название бренда, в данном случае "GENIUS".
- `url` (str): URL для поиска товаров: "https://www.morlevi.co.il/Cat/114?p_315=43&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): Статус чекбокса (false).
- `active` (bool): Активность сценария (true).
- `condition` (str): Состояние товара ("new").
- `presta_categories` (str): Строка с ID категорий PrestaShop, разделенными запятыми "203,207,334".