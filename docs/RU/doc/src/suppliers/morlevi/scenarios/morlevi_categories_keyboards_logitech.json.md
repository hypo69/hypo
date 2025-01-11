# Документация для `morlevi_categories_keyboards_logitech.json`

## Обзор

Файл `morlevi_categories_keyboards_logitech.json` содержит JSON-конфигурацию для сценариев обработки категорий клавиатур и мышей бренда LOGITECH. Каждый сценарий определяет URL, бренд, активность, состояние товара и категории PrestaShop, к которым он относится.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание сценариев](#описание-сценариев)
    - [`LOGITECH WIRELESS KEYBOARD`](#logitech-wireless-keyboard)
    - [`LOGITECH USB KEYBOARD`](#logitech-usb-keyboard)
    - [`LOGITECH USB MOUSE`](#logitech-usb-mouse)
    - [`LOGITECH WIRELESS MOUSE`](#logitech-wireless-mouse)
    - [`LOGITECH USB KEYBOARD-MOUSE SET`](#logitech-usb-keyboard-mouse-set)
    - [`LOGITECH WIRELESS  KEYBOARD-MOUSE SET`](#logitech-wireless--keyboard-mouse-set)
    - [`LOGITECH GAMING  KEYBOARD`](#logitech-gaming--keyboard)

## Структура JSON

JSON-файл содержит объект с ключом `"scenarios"`, значением которого является объект, содержащий сценарии, где каждый ключ - это название сценария, а значение - объект с параметрами сценария.

## Описание сценариев

### `LOGITECH WIRELESS KEYBOARD`

**Описание**: Сценарий для беспроводных клавиатур LOGITECH.

**Параметры**:

- `brand` (str): Бренд продукта, всегда `"LOGITECH"`.
- `url` (str):  Строка, указывающая на источник для  беспроводных клавиатур LOGITECH.
- `checkbox` (bool):  Логическое значение, указывающее, включен ли сценарий в пользовательском интерфейсе (всегда `false`).
- `active` (bool):  Логическое значение, определяющее, активен ли сценарий (всегда `true`).
- `condition` (str):  Состояние товара (всегда `"new"`).
- `presta_categories` (str):  Строка, содержащая ID категорий PrestaShop, разделенные запятыми (`"203,204,316"`).

### `LOGITECH USB KEYBOARD`

**Описание**: Сценарий для USB клавиатур LOGITECH.

**Параметры**:

- `brand` (str): Бренд продукта, всегда `"LOGITECH"`.
- `url` (str):  Строка, указывающая на источник для  USB клавиатур LOGITECH.
- `checkbox` (bool):  Логическое значение, указывающее, включен ли сценарий в пользовательском интерфейсе (всегда `false`).
- `active` (bool):  Логическое значение, определяющее, активен ли сценарий (всегда `true`).
- `condition` (str):  Состояние товара (всегда `"new"`).
- `presta_categories` (str):  Строка, содержащая ID категорий PrestaShop, разделенные запятыми (`"203,204,315"`).

### `LOGITECH USB MOUSE`

**Описание**: Сценарий для USB мышей LOGITECH.

**Параметры**:

- `brand` (str): Бренд продукта, всегда `"LOGITECH"`.
- `url` (str):  URL-адрес страницы с USB мышами LOGITECH.
- `checkbox` (bool):  Логическое значение, указывающее, включен ли сценарий в пользовательском интерфейсе (всегда `false`).
- `active` (bool):  Логическое значение, определяющее, активен ли сценарий (всегда `true`).
- `condition` (str):  Состояние товара (всегда `"new"`).
- `presta_categories` (str):  Строка, содержащая ID категорий PrestaShop, разделенные запятыми (`"203,206,317"`).

### `LOGITECH WIRELESS MOUSE`

**Описание**: Сценарий для беспроводных мышей LOGITECH.

**Параметры**:

- `brand` (str): Бренд продукта, всегда `"LOGITECH"`.
- `url` (str):  URL-адрес страницы с беспроводными мышами LOGITECH.
- `checkbox` (bool):  Логическое значение, указывающее, включен ли сценарий в пользовательском интерфейсе (всегда `false`).
- `active` (bool):  Логическое значение, определяющее, активен ли сценарий (всегда `true`).
- `condition` (str):  Состояние товара (всегда `"new"`).
- `presta_categories` (str):  Строка, содержащая ID категорий PrestaShop, разделенные запятыми (`"203,206,318"`).

### `LOGITECH USB KEYBOARD-MOUSE SET`

**Описание**: Сценарий для наборов USB клавиатура и мышь от LOGITECH.

**Параметры**:

- `brand` (str): Бренд продукта, всегда `"LOGITECH"`.
- `url` (str):  URL-адрес страницы с наборами USB клавиатура и мышь LOGITECH.
- `checkbox` (bool):  Логическое значение, указывающее, включен ли сценарий в пользовательском интерфейсе (всегда `false`).
- `active` (bool):  Логическое значение, определяющее, активен ли сценарий (всегда `true`).
- `condition` (str):  Состояние товара (всегда `"new"`).
- `presta_categories` (str):  Строка, содержащая ID категорий PrestaShop, разделенные запятыми (`"203,207,208"`).

### `LOGITECH WIRELESS  KEYBOARD-MOUSE SET`

**Описание**: Сценарий для беспроводных наборов клавиатура и мышь от LOGITECH.

**Параметры**:

- `brand` (str): Бренд продукта, всегда `"LOGITECH"`.
- `url` (str):  URL-адрес страницы с беспроводными наборами клавиатура и мышь LOGITECH.
- `checkbox` (bool):  Логическое значение, указывающее, включен ли сценарий в пользовательском интерфейсе (всегда `false`).
- `active` (bool):  Логическое значение, определяющее, активен ли сценарий (всегда `true`).
- `condition` (str):  Состояние товара (всегда `"new"`).
- `presta_categories` (str):  Строка, содержащая ID категорий PrestaShop, разделенные запятыми (`"203,207,334"`).

### `LOGITECH GAMING  KEYBOARD`

**Описание**: Сценарий для игровых клавиатур LOGITECH.

**Параметры**:

- `brand` (str): Бренд продукта, всегда `"LOGITECH"`.
- `url` (str):  URL-адрес страницы с игровыми клавиатурами LOGITECH.
- `checkbox` (bool):  Логическое значение, указывающее, включен ли сценарий в пользовательском интерфейсе (всегда `false`).
- `active` (bool):  Логическое значение, определяющее, активен ли сценарий (всегда `true`).
- `condition` (str):  Состояние товара (всегда `"new"`).
- `presta_categories` (str):  Строка, содержащая ID категорий PrestaShop, разделенные запятыми (`"203,205"`).