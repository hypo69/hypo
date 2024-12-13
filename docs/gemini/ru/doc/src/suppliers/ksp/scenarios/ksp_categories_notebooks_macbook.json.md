# Документация для `ksp_categories_notebooks_macbook.json`

## Обзор

Данный файл содержит JSON-структуру, определяющую сценарии для различных моделей MacBook. Каждый сценарий включает в себя информацию о бренде, URL-адресе страницы продукта на сайте KSP, статусе чекбокса, активности и соответствующих категориях PrestaShop.

## Оглавление
1. [Обзор](#Обзор)
2. [Структура JSON](#Структура-JSON)
3. [Сценарии](#Сценарии)
    - [MacBook Air 13 Late 2020](#MacBook-Air-13-Late-2020)
    - [MacBook Pro 13 Late 2020](#MacBook-Pro-13-Late-2020)
    - [MacBook Pro 14 Late 2021](#MacBook-Pro-14-Late-2021)
    - [MacBook Pro 16 Late 2021](#MacBook-Pro-16-Late-2021)

## Структура JSON

JSON-файл имеет следующую структуру:
```json
{
  "scenarios": {
    "имя_сценария_1": {
      "brand": "строка",
      "url": "строка",
      "checkbox": логическое_значение,
      "active": логическое_значение,
      "condition":"строка",
      "presta_categories": {
        "id_категории_1": "строка",
        "id_категории_2": "строка",
        "...": "..."
      }
    },
    "имя_сценария_2": {
      "brand": "строка",
      "url": "строка",
      "checkbox": логическое_значение,
       "active": логическое_значение,
        "condition":"строка",
      "presta_categories": {
        "id_категории_1": "строка",
        "id_категории_2": "строка",
        "...": "..."
      }
    },
    "...": "..."
  }
}
```

## Сценарии

### `MacBook Air 13 Late 2020`

**Описание**: Сценарий для MacBook Air 13 Late 2020.

**Поля**:
- `brand` (str): Бренд устройства, значение "APPLE".
- `url` (str): URL-адрес страницы продукта на сайте KSP: `"https://ksp.co.il/web/cat/271..245..19037"`.
- `checkbox` (bool): Статус чекбокса, значение `false`.
- `active` (bool): Статус активности сценария, значение `true`.
- `condition` (str): Состояние товара, значение `new`.
- `presta_categories` (dict): Словарь категорий PrestaShop.
  - `"3405"` (str): `"GOOGLE PIXEL PRO"`
  - `"3198"` (str): `"CONSUMER ELECTRONICS"`
  - `"3202"` (str): `"computer,smartphone,gaming console,smart device"`
  - `"6471"` (str): `"Smartphones"`
  - `"3403"` (str): `"GOOGLE"`

### `MacBook Pro 13 Late 2020`

**Описание**: Сценарий для MacBook Pro 13 Late 2020.

**Поля**:
- `brand` (str): Бренд устройства, значение "APPLE".
- `url` (str): URL-адрес страницы продукта на сайте KSP: `"https://ksp.co.il/web/cat/271..245..19085"`.
- `checkbox` (bool): Статус чекбокса, значение `false`.
- `active` (bool): Статус активности сценария, значение `true`.
- `condition` (str): Состояние товара, значение `new`.
- `presta_categories` (dict): Словарь категорий PrestaShop.
  - `"3405"` (str): `"GOOGLE PIXEL PRO"`
  - `"3198"` (str): `"CONSUMER ELECTRONICS"`
  - `"3202"` (str): `"computer,smartphone,gaming console,smart device"`
  - `"6471"` (str): `"Smartphones"`
  - `"3403"` (str): `"GOOGLE"`

### `MacBook Pro 14 Late 2021`

**Описание**: Сценарий для MacBook Pro 14 Late 2021.

**Поля**:
- `brand` (str): Бренд устройства, значение "APPLE".
- `url` (str): URL-адрес страницы продукта на сайте KSP: `"https://ksp.co.il/web/cat/271..245..29598"`.
- `checkbox` (bool): Статус чекбокса, значение `false`.
- `active` (bool): Статус активности сценария, значение `true`.
- `condition` (str): Состояние товара, значение `new`.
- `presta_categories` (dict): Словарь категорий PrestaShop.
  - `"3405"` (str): `"GOOGLE PIXEL PRO"`
  - `"3198"` (str): `"CONSUMER ELECTRONICS"`
  - `"3202"` (str): `"computer,smartphone,gaming console,smart device"`
  - `"6471"` (str): `"Smartphones"`
  - `"3403"` (str): `"GOOGLE"`

### `MacBook Pro 16 Late 2021`

**Описание**: Сценарий для MacBook Pro 16 Late 2021.

**Поля**:
- `brand` (str): Бренд устройства, значение "APPLE".
- `url` (str): URL-адрес страницы продукта на сайте KSP: `"https://ksp.co.il/web/cat/271..245..29608"`.
- `checkbox` (bool): Статус чекбокса, значение `false`.
- `active` (bool): Статус активности сценария, значение `true`.
- `condition` (str): Состояние товара, значение `new`.
- `presta_categories` (dict): Словарь категорий PrestaShop.
  - `"3405"` (str): `"GOOGLE PIXEL PRO"`
  - `"3198"` (str): `"CONSUMER ELECTRONICS"`
  - `"3202"` (str): `"computer,smartphone,gaming console,smart device"`
  - `"6471"` (str): `"Smartphones"`
  - `"3403"` (str): `"GOOGLE"`