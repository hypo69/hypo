# Документация для `morlevi_categories_keyboards_logitech.json`

## Обзор

Файл `morlevi_categories_keyboards_logitech.json` содержит конфигурацию сценариев для парсинга категорий клавиатур и мышей бренда LOGITECH с сайта Morlevi. Каждый сценарий определяет параметры для парсинга определенного типа товара (например, беспроводная клавиатура, USB мышь), а также URL, по которому необходимо парсить данные, активность сценария, условие товара и соответствие категориям PrestaShop.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
   - [Ключ `scenarios`](#ключ-scenarios)
   - [Сценарии](#сценарии)
3. [Описание полей сценария](#описание-полей-сценария)
4. [Примеры сценариев](#примеры-сценариев)

## Структура JSON

### Ключ `scenarios`

Основным ключом JSON-объекта является `scenarios`. Он содержит в себе словарь, где ключами являются названия сценариев, а значениями - сами сценарии.

### Сценарии

Каждый сценарий представляет собой объект JSON, описывающий параметры для парсинга определенной категории товаров. Сценарии имеют следующую структуру:

```json
    "SCENARIO_NAME": {
      "brand": "BRAND_NAME",
      "url": "URL_TO_PARSE",
      "checkbox": false,
      "active": true,
      "condition":"CONDITION",
      "presta_categories": "PRESTA_CATEGORIES"
    }
```

## Описание полей сценария

- **`brand`** (str): Название бренда товара (в данном случае всегда "LOGITECH").
- **`url`** (str): URL-адрес страницы, с которой необходимо парсить данные. В случае если url не указан - строка с разделителями.
- **`checkbox`** (bool): Флаг, указывающий, нужно ли использовать чекбокс (в данном файле всегда `false`).
- **`active`** (bool): Флаг, указывающий, активен ли сценарий (в данном файле всегда `true`).
- **`condition`** (str): Условие товара, например, "new" (новый).
- **`presta_categories`** (str): Строка, содержащая ID категорий PrestaShop, к которым относится товар, разделенные запятыми.

## Примеры сценариев

### `LOGITECH WIRELESS KEYBOARD`

```json
"LOGITECH WIRELESS KEYBOARD": {
  "brand": "LOGITECH",
  "url": "-----------------------------------------------LOGITECH WIRELESS KEYBOARD----------------------------------------------",
  "checkbox": false,
  "active": true,
  "condition":"new",
  "presta_categories": "203,204,316"
}
```

- **Описание**: Сценарий для парсинга беспроводных клавиатур LOGITECH. URL не указан.
- **Категории PrestaShop**: 203, 204, 316

### `LOGITECH USB KEYBOARD`

```json
"LOGITECH USB KEYBOARD": {
  "brand": "LOGITECH",
  "url": "-----------------------------------------------LOGITECH USB KEYBOARD----------------------------------------------",
  "checkbox": false,
  "active": true,
  "condition":"new",
  "presta_categories": "203,204,315"
}
```

- **Описание**: Сценарий для парсинга USB клавиатур LOGITECH. URL не указан.
- **Категории PrestaShop**: 203, 204, 315

### `LOGITECH USB MOUSE`

```json
"LOGITECH USB MOUSE": {
  "brand": "LOGITECH",
  "url": "https://www.morlevi.co.il/Cat/108?p_315=29&sort=datafloat2%2Cprice&keyword=",
  "checkbox": false,
  "active": true,
  "condition":"new",
  "presta_categories": "203,206,317"
}
```

- **Описание**: Сценарий для парсинга USB мышей LOGITECH.
- **URL**: `https://www.morlevi.co.il/Cat/108?p_315=29&sort=datafloat2%2Cprice&keyword=`
- **Категории PrestaShop**: 203, 206, 317

### `LOGITECH WIRELESS MOUSE`

```json
"LOGITECH WIRELESS MOUSE": {
  "brand": "LOGITECH",
  "url": "https://www.morlevi.co.il/Cat/109?p_315=29&sort=datafloat2%2Cprice&keyword=",
  "checkbox": false,
  "active": true,
  "condition":"new",
  "presta_categories": "203,206,318"
}
```

- **Описание**: Сценарий для парсинга беспроводных мышей LOGITECH.
- **URL**: `https://www.morlevi.co.il/Cat/109?p_315=29&sort=datafloat2%2Cprice&keyword=`
- **Категории PrestaShop**: 203, 206, 318

### `LOGITECH USB KEYBOARD-MOUSE SET`

```json
"LOGITECH USB KEYBOARD-MOUSE SET": {
  "brand": "LOGITECH",
  "url": "https://www.morlevi.co.il/Cat/113?p_315=29&sort=datafloat2%2Cprice&keyword=",
  "checkbox": false,
  "active": true,
  "condition":"new",
  "presta_categories": "203,207,208"
}
```

- **Описание**: Сценарий для парсинга комплектов USB клавиатура-мышь LOGITECH.
- **URL**: `https://www.morlevi.co.il/Cat/113?p_315=29&sort=datafloat2%2Cprice&keyword=`
- **Категории PrestaShop**: 203, 207, 208

### `LOGITECH WIRELESS  KEYBOARD-MOUSE SET`

```json
"LOGITECH WIRELESS  KEYBOARD-MOUSE SET": {
  "brand": "LOGITECH",
  "url": "https://www.morlevi.co.il/Cat/114?p_315=29&sort=datafloat2%2Cprice&keyword=",
  "checkbox": false,
  "active": true,
  "condition":"new",
  "presta_categories": "203,207,334"
}
```

- **Описание**: Сценарий для парсинга комплектов беспроводная клавиатура-мышь LOGITECH.
- **URL**: `https://www.morlevi.co.il/Cat/114?p_315=29&sort=datafloat2%2Cprice&keyword=`
- **Категории PrestaShop**: 203, 207, 334

### `LOGITECH GAMING  KEYBOARD`

```json
"LOGITECH GAMING  KEYBOARD": {
  "brand": "LOGITECH",
  "url": "https://www.morlevi.co.il/Cat/239?p_315=29&sort=datafloat2%2Cprice&keyword=",
  "checkbox": false,
  "active": true,
  "condition":"new",
  "presta_categories": "203,205"
}
```

- **Описание**: Сценарий для парсинга игровых клавиатур LOGITECH.
- **URL**: `https://www.morlevi.co.il/Cat/239?p_315=29&sort=datafloat2%2Cprice&keyword=`
- **Категории PrestaShop**: 203, 205