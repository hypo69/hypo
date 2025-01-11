# Документация для `ksp_categories_watches_xiaomi.json`

## Обзор

Файл `ksp_categories_watches_xiaomi.json` содержит конфигурацию сценариев для парсинга категорий часов Xiaomi с сайта KSP. Каждый сценарий определяет бренд, URL для парсинга, флаги активности и чекбокса, а также привязку к категориям PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
    - [Xiaomi Redmi Watch](#xiaomi-redmi-watch)
    - [Xiaomi Mi Watch](#xiaomi-mi-watch)

## Структура файла

Файл представляет собой JSON-объект со следующим форматом:

```json
{
  "scenarios": {
    "scenario_name": {
      "brand": "brand_name",
      "url": "url_to_parse",
      "checkbox": boolean,
      "active": boolean,
       "condition": "condition_of_product",
      "presta_categories": {
        "category_id": "category_name",
        "...": "..."
      }
    },
    "...": {
      // ... другие сценарии
    }
  }
}
```

- **`scenarios`**: Объект, содержащий сценарии парсинга. Каждый ключ является именем сценария.
    - **`brand`**: (string) Бренд продукта.
    - **`url`**: (string) URL страницы для парсинга.
    - **`checkbox`**: (boolean) Флаг, указывающий, выбран ли чекбокс.
    - **`active`**: (boolean) Флаг, указывающий, активен ли сценарий.
     - **`condition`**: (string) Указывает состояние товара ("new" - новый).
    - **`presta_categories`**: (object) Объект, связывающий ID категорий PrestaShop с их названиями.

## Сценарии

### `Xiaomi Redmi Watch`

**Описание**: Сценарий для парсинга категории часов Xiaomi Redmi Watch.

**Параметры**:
- `brand` (str): "XIAOMI".
- `url` (str): "https://ksp.co.il/web/cat/2085..2202..34255".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (dict): Словарь, связывающий ID категорий PrestaShop с их названиями:
    - `3405`: "GOOGLE PIXEL PRO"
    - `3198`: "CONSUMER ELECTRONICS"
    - `3202`: "computer,smartphone,gaming console,smart device"
    - `6471`: "Smartphones"
    - `3403`: "GOOGLE"

### `Xiaomi Mi Watch`

**Описание**: Сценарий для парсинга категории часов Xiaomi Mi Watch.

**Параметры**:
- `brand` (str): "XIAOMI".
- `url` (str): "https://ksp.co.il/web/cat/2085..2202..29146..29145".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (dict): Словарь, связывающий ID категорий PrestaShop с их названиями:
    - `3405`: "GOOGLE PIXEL PRO"
    - `3198`: "CONSUMER ELECTRONICS"
    - `3202`: "computer,smartphone,gaming console,smart device"
    - `6471`: "Smartphones"
    - `3403`: "GOOGLE"