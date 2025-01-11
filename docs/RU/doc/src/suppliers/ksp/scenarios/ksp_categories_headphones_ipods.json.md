# Документация для `ksp_categories_headphones_ipods.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев парсинга категорий наушников и iPods с сайта KSP. Каждый сценарий определяет параметры для конкретной категории наушников, такие как бренд, URL для парсинга, состояние товара, и соответствия категориям PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [Сценарии](#сценарии)
        - [`in-ear-bud`](#in-ear-bud)
        - [`Overear`](#overear)
        - [`Ear-clip`](#ear-clip)
- [Описание полей](#описание-полей)
- [Пример использования](#пример-использования)

## Структура JSON

Файл JSON имеет следующую структуру:

```json
{
  "scenarios": {
    "in-ear-bud": {
      "brand": "APPLE",
      "url": "https://ksp.co.il/web/cat/242..245..1250",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
          "template": { "apple": "ipods in-ear-bud" }
      }
    },
    "Overear": {
      "brand": "APPLE",
      "url": "https://ksp.co.il/web/cat/242..245..1252",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": {
          "template": { "apple": "ipods Overear" }
      }
    },
    "Ear-clip": {
      "brand": "APPLE",
      "url": "https://ksp.co.il/web/cat/242..245..1254",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": {
          "3455": "Ear-clip",
          "template": { "apple": "ipods Ear-clip" }
      }
    }
  }
}
```

### Сценарии

#### `in-ear-bud`

**Описание**: Сценарий для парсинга наушников-вкладышей (in-ear bud) бренда APPLE.

**Поля**:

-   `brand` (str): Бренд товара (`"APPLE"`).
-   `url` (str): URL страницы категории на сайте KSP (`"https://ksp.co.il/web/cat/242..245..1250"`).
-   `checkbox` (bool): Индикатор выбора (всегда `false`).
-   `active` (bool): Индикатор активности сценария (всегда `true`).
-   `condition` (str): Состояние товара (всегда `"new"`).
-  `presta_categories` (dict): Соответствие категорий PrestaShop.
    - `template` (dict): Шаблон соответствия для бренда.
         - `"apple"` (str): Категория товара для PrestaShop (`"ipods in-ear-bud"`).
   

#### `Overear`

**Описание**: Сценарий для парсинга накладных наушников (over-ear) бренда APPLE.

**Поля**:
-   `brand` (str): Бренд товара (`"APPLE"`).
-   `url` (str): URL страницы категории на сайте KSP (`"https://ksp.co.il/web/cat/242..245..1252"`).
-   `checkbox` (bool): Индикатор выбора (всегда `false`).
-   `active` (bool): Индикатор активности сценария (всегда `true`).
-   `condition` (str): Состояние товара (всегда `"new"`).
-  `presta_categories` (dict): Соответствие категорий PrestaShop.
    - `template` (dict): Шаблон соответствия для бренда.
         - `"apple"` (str): Категория товара для PrestaShop (`"ipods Overear"`).

#### `Ear-clip`

**Описание**: Сценарий для парсинга наушников с клипсой (ear-clip) бренда APPLE.

**Поля**:
-   `brand` (str): Бренд товара (`"APPLE"`).
-   `url` (str): URL страницы категории на сайте KSP (`"https://ksp.co.il/web/cat/242..245..1254"`).
-   `checkbox` (bool): Индикатор выбора (всегда `false`).
-   `active` (bool): Индикатор активности сценария (всегда `true`).
-    `condition` (str): Состояние товара (всегда `"new"`).
-   `presta_categories` (dict): Соответствие категорий PrestaShop.
    - `"3455"` (str): Категория товара (`"Ear-clip"`).
    - `template` (dict): Шаблон соответствия для бренда.
         - `"apple"` (str): Категория товара для PrestaShop (`"ipods Ear-clip"`).

## Описание полей

-   **`scenarios`**: Основной объект, содержащий все сценарии парсинга.
-   **`brand`**: Бренд товара.
-   **`url`**: URL страницы категории на сайте KSP.
-   **`checkbox`**: Флаг, указывающий, должен ли быть выбран чекбокс на странице (в данном случае всегда `false`).
-   **`active`**: Флаг, указывающий, активен ли сценарий (в данном случае всегда `true`).
-   **`condition`**: Состояние товара.
-   **`presta_categories`**: Объект, определяющий соответствия категориям PrestaShop.
    - **`template`**: Объект для определения соответствия категорий по шаблону.
        - **`apple`**: Ключ для соответствия бренду APPLE.
- **`[number]`**:  Ключ-число для соответствия категориям PrestaShop.

## Пример использования

Данный JSON-файл используется для конфигурации парсера, который извлекает данные о наушниках и iPods с сайта KSP. Каждый сценарий определяет параметры для конкретной категории наушников и устанавливает соответствие категориям PrestaShop.