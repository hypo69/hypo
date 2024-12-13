# Документация для `morlevi_categories_sound.json`

## Обзор

Файл `morlevi_categories_sound.json` содержит JSON-структуру с определениями сценариев для парсинга категорий товаров, связанных со звуком, с сайта morlevi.co.il. Каждый сценарий описывает конкретную категорию или бренд товаров, включая URL для парсинга, бренд, флаг активности, условие новизны и соответствующие категории PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [`scenarios`](#scenarios)
        - [Сценарий](#сценарий)

## Структура JSON

### `scenarios`

Объект `scenarios` содержит наборы сценариев, каждый из которых представляет собой объект с информацией для парсинга определенной категории товаров.

#### Сценарий

Каждый сценарий имеет следующие ключи:

- **`brand`** (string): Бренд товаров, для которого предназначен сценарий.
- **`url`** (string): URL-адрес страницы, с которой будет производиться парсинг товаров.
- **`checkbox`** (boolean): Флаг, который указывает, должен ли быть включен чекбокс (не используется в логике парсинга, может быть использован для UI).
- **`active`** (boolean): Флаг, указывающий, активен ли данный сценарий. Если `true`, сценарий используется при парсинге.
-  **`condition`** (string): Условие для товаров (в данном случае, всегда "new").
-  **`presta_categories`** (string): Список категорий PrestaShop, к которым относятся товары (в виде строки с номерами категорий, разделенных запятыми).

**Пример сценария:**

```json
    "Logitech speakers": {
      "brand": "LOGITECH",
      "url": "https://www.morlevi.co.il/Cat/161?p_315=29&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "520,521"
    }
```

**Описание сценариев:**

- `"Logitech speakers"`: Сценарий для парсинга акустических систем Logitech.
- `"GENIUS speakers"`: Сценарий для парсинга акустических систем GENIUS.
- `"CREATIVE speakers"`: Сценарий для парсинга акустических систем CREATIVE.
- `"CREATIVE sound cards"`: Сценарий для парсинга звуковых карт CREATIVE.
- `"Headphones Logitech"`: Сценарий для парсинга наушников Logitech.
- `"Headphones Microsoft"`: Сценарий для парсинга наушников Microsoft.
- `"Headphones ZALMAN"`: Сценарий для парсинга наушников ZALMAN.
- `"Headphones Corsair"`: Сценарий для парсинга наушников Corsair.
- `"Headphones Cooler Master"`: Сценарий для парсинга наушников Cooler Master.
- `"Cams Logitech"`: Сценарий для парсинга веб-камер Logitech.
- `"Cams GENIUS"`: Сценарий для парсинга веб-камер GENIUS.
- `"Cams MICROSOFT"`: Сценарий для парсинга веб-камер MICROSOFT.
- `"Cams GENERIC GOLDTOUCH"`: Сценарий для парсинга веб-камер GENERIC GOLDTOUCH.
- `"Cams GENERIC GENERIC"`: Сценарий для парсинга веб-камер GENERIC GENERIC.
- `"Cams GENERIC AONI"`: Сценарий для парсинга веб-камер GENERIC AONI.

Каждый из этих сценариев настроен для парсинга товаров определенной марки или категории с сайта morlevi.co.il и сопоставлен с категориями PrestaShop.