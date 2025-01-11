# Документация для `morlevi_categories_keyboards.json`

## Обзор

Данный JSON-файл содержит конфигурации сценариев для категорий клавиатур и мышей, используемых поставщиком Morlevi. Каждый сценарий определяет соответствие между брендом, шаблоном, URL-адресом, условием, а также категориями PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
- [Описание полей](#описание-полей)
  - [scenarios](#scenarios)
    - [`COOLER MASTER USB KEYBOARD`](#cooler-master-usb-keyboard)
    - [GENIUS USB KEYBOARD](#genius-usb-keyboard)
    - [`COOLER MASTER USB MOUSE`](#cooler-master-usb-mouse)
    - [`COOLER MASTER WIRELESS MOUSE`](#cooler-master-wireless-mouse)
    - [`COOLER MASTER USB KEYBOARD-MOUSE SET`](#cooler-master-usb-keyboard-mouse-set)
    - [`COOLER MASTER WIRELESS  KEYBOARD-MOUSE SET`](#cooler-master-wireless-keyboard-mouse-set)
    - [`COOLER MASTER GAMING  KEYBOARD`](#cooler-master-gaming-keyboard)
    - [`COOLER MASTER GAMING  MOUSE`](#cooler-master-gaming-mouse)

## Структура файла

Файл представляет собой JSON-объект с единственным ключом `scenarios`, значением которого является объект, содержащий наборы данных для каждого сценария. Каждый ключ в объекте `scenarios` представляет собой название сценария, а его значение - это объект с детальными настройками.

## Описание полей

### scenarios

Объект, содержащий конфигурации для каждого сценария.

#### `COOLER MASTER USB KEYBOARD`

**Описание**: Конфигурация для проводной USB клавиатуры Cooler Master.

- **`brand`** (str): Бренд продукта - `COOLER MASTER`.
- **`template`** (str): Шаблон продукта - `COOLER MASTER KEYBOARD`.
- **`url`** (str): URL-адрес категории на сайте поставщика - `https://www.morlevi.co.il/Cat/113?p_315=74&sort=datafloat2%2Cprice&keyword=`.
- **`checkbox`** (bool): Флаг, указывающий на использование чекбокса - `false`.
- **`active`** (bool): Флаг, указывающий на активность сценария - `true`.
- **`condition`** (str): Состояние товара - `new`.
- **`presta_categories`** (object): Объект категорий PrestaShop.
  - **`template`** (object): Шаблон для категорий.
    - **`computer accessories`** (str): Категория для аксессуаров - `WIRED KB`.

#### GENIUS USB KEYBOARD

**Описание**: Конфигурация для проводной USB клавиатуры GENIUS.

- **`brand`** (str): Бренд продукта - `COOLER MASTER`.
- **`template`** (str): Шаблон продукта - `COOLER MASTER USB KEYBOARD`.
- **`url`** (str): URL-адрес категории на сайте поставщика - `https://www.morlevi.co.il/Cat/113?p_315=43&sort=datafloat2%2Cprice&keyword=`.
- **`checkbox`** (bool): Флаг, указывающий на использование чекбокса - `false`.
- **`active`** (bool): Флаг, указывающий на активность сценария - `true`.
- **`condition`** (str): Состояние товара - `new`.
- **`presta_categories`** (str): Строка с id категорий PrestaShop - `203,204,315`.

#### `COOLER MASTER USB MOUSE`

**Описание**: Конфигурация для проводной USB мыши Cooler Master.

- **`brand`** (str): Бренд продукта - `COOLER MASTER`.
- **`template`** (str): Шаблон продукта - `COOLER MASTER USB MOUSE`.
- **`url`** (str): URL-адрес категории на сайте поставщика - `https://www.morlevi.co.il/Cat/108?p_315=74&sort=datafloat2%2Cprice&keyword=`.
- **`checkbox`** (bool): Флаг, указывающий на использование чекбокса - `false`.
- **`active`** (bool): Флаг, указывающий на активность сценария - `true`.
- **`condition`** (str): Состояние товара - `new`.
- **`presta_categories`** (str): Строка с id категорий PrestaShop - `203,206,317`.

#### `COOLER MASTER WIRELESS MOUSE`

**Описание**: Конфигурация для беспроводной мыши Cooler Master.

- **`brand`** (str): Бренд продукта - `COOLER MASTER`.
- **`template`** (str): Шаблон продукта - `COOLER MASTER WIRELESS MOUSE`.
- **`url`** (str): URL-адрес категории на сайте поставщика - `--------------------------------------COOLER MASTER WIRELESS MOUSE--------------------------------`.
- **`checkbox`** (bool): Флаг, указывающий на использование чекбокса - `false`.
- **`active`** (bool): Флаг, указывающий на активность сценария - `true`.
- **`condition`** (str): Состояние товара - `new`.
- **`presta_categories`** (str): Строка с id категорий PrestaShop - `203,206,318`.

#### `COOLER MASTER USB KEYBOARD-MOUSE SET`

**Описание**: Конфигурация для набора проводных клавиатуры и мыши Cooler Master.

- **`brand`** (str): Бренд продукта - `COOLER MASTER`.
- **`template`** (str): Шаблон продукта - `COOLER MASTER USB KEYBOARD-MOUSE SET`.
- **`url`** (str): URL-адрес категории на сайте поставщика - `https://www.morlevi.co.il/Cat/113?p_315=74&sort=datafloat2%2Cprice&keyword=`.
- **`checkbox`** (bool): Флаг, указывающий на использование чекбокса - `false`.
- **`active`** (bool): Флаг, указывающий на активность сценария - `true`.
- **`condition`** (str): Состояние товара - `new`.
- **`presta_categories`** (str): Строка с id категорий PrestaShop - `203,207,208`.

#### `COOLER MASTER WIRELESS  KEYBOARD-MOUSE SET`

**Описание**: Конфигурация для набора беспроводных клавиатуры и мыши Cooler Master.

- **`brand`** (str): Бренд продукта - `COOLER MASTER`.
- **`template`** (str): Шаблон продукта - `COOLER MASTER WIRELESS KEYBOARD-MOUSE SET`.
- **`url`** (str): URL-адрес категории на сайте поставщика - `--------------------------------------COOLER MASTER WIRELESS  KEYBOARD-MOUSE SET--------------------------------`.
- **`checkbox`** (bool): Флаг, указывающий на использование чекбокса - `false`.
- **`active`** (bool): Флаг, указывающий на активность сценария - `true`.
- **`condition`** (str): Состояние товара - `new`.
- **`presta_categories`** (str): Строка с id категорий PrestaShop - `203,207,334`.

#### `COOLER MASTER GAMING  KEYBOARD`

**Описание**: Конфигурация для игровой клавиатуры Cooler Master.

- **`brand`** (str): Бренд продукта - `COOLER MASTER`.
- **`template`** (str): Шаблон продукта - `COOLER MASTER GAMING  KEYBOARD`.
- **`url`** (str): URL-адрес категории на сайте поставщика - `https://www.morlevi.co.il/Cat/239?p_315=74&sort=datafloat2%2Cprice&keyword=`.
- **`checkbox`** (bool): Флаг, указывающий на использование чекбокса - `false`.
- **`active`** (bool): Флаг, указывающий на активность сценария - `true`.
- **`condition`** (str): Состояние товара - `new`.
- **`presta_categories`** (str): Строка с id категорий PrestaShop - `203,205`.

#### `COOLER MASTER GAMING  MOUSE`

**Описание**: Конфигурация для игровой мыши Cooler Master.

- **`brand`** (str): Бренд продукта - `COOLER MASTER`.
- **`template`** (str): Шаблон продукта - `COOLER MASTER GAMING  MOUSE`.
- **`url`** (str): URL-адрес категории на сайте поставщика - `https://www.morlevi.co.il/Cat/252?p_315=74&sort=datafloat2%2Cprice&keyword=`.
- **`checkbox`** (bool): Флаг, указывающий на использование чекбокса - `false`.
- **`active`** (bool): Флаг, указывающий на активность сценария - `true`.
- **`condition`** (str): Состояние товара - `new`.
- **`presta_categories`** (str): Строка с id категорий PrestaShop - `203,206,343`.