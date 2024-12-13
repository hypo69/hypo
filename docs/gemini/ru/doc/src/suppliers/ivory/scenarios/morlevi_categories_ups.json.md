# Документация для `morlevi_categories_ups.json`

## Обзор

Данный JSON-файл содержит конфигурацию сценариев для парсинга категорий ИБП (UPS) с сайта morlevi.co.il. Каждый сценарий определяет бренд, URL для парсинга, состояние чекбокса, активность, состояние товара и категории PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
- [Сценарии](#сценарии)
    - [ups APC](#ups-apc)
    - [ups EATON](#ups-eaton)

## Структура файла

Файл имеет следующую структуру:
```json
{
  "scenarios": {
    "ups APC": {
      "brand": "APC",
      "url": "https://www.morlevi.co.il/Cat/332?p_315=86&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "158,247"
    },
    "ups EATON": {
      "brand": "EATON",
      "url": "https://www.morlevi.co.il/Cat/332?p_315=59&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "158,247"
    }
  }
}
```

## Сценарии

### `ups APC`

**Описание**: Конфигурация для парсинга ИБП бренда APC.

**Параметры**:

- `brand` (str): Название бренда - "APC".
- `url` (str): URL для парсинга списка ИБП.
- `checkbox` (bool): Состояние чекбокса (по умолчанию `false`).
- `active` (bool): Активен ли данный сценарий (по умолчанию `true`).
- `condition` (str): Состояние товара (по умолчанию "new").
- `presta_categories` (str): ID категорий PrestaShop через запятую (например, "158,247").

### `ups EATON`

**Описание**: Конфигурация для парсинга ИБП бренда EATON.

**Параметры**:

- `brand` (str): Название бренда - "EATON".
- `url` (str): URL для парсинга списка ИБП.
- `checkbox` (bool): Состояние чекбокса (по умолчанию `false`).
- `active` (bool): Активен ли данный сценарий (по умолчанию `true`).
- `condition` (str): Состояние товара (по умолчанию "new").
- `presta_categories` (str): ID категорий PrestaShop через запятую (например, "158,247").