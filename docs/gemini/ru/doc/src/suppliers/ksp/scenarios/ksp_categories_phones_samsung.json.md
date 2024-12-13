# Документация для `ksp_categories_phones_samsung.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
    - [`GALAXY A03 Core`](#galaxy-a03-core)
    - [`GALAXY A03s`](#galaxy-a03s)
    - [`GALAXY A04`](#galaxy-a04)
    - [`GALAXY A12`](#galaxy-a12)
    - [`GALAXY A22 5G`](#galaxy-a22-5g)
    - [`GALAXY A22`](#galaxy-a22)
    - [`GALAXY A32`](#galaxy-a32)
    - [`GALAXY A52`](#galaxy-a52)
    - [`GALAXY A52s`](#galaxy-a52s)
    - [`GALAXY A53`](#galaxy-a53)
    - [`GALAXY A53 5G`](#galaxy-a53-5g)
    - [`GALAXY A72`](#galaxy-a72)
    - [`GALAXY S20 FE`](#galaxy-s20-fe)
    - [`GALAXY S21`](#galaxy-s21)
    - [`GALAXY S21 Plus`](#galaxy-s21-plus)
    - [`GALAXY S21 FE 5G`](#galaxy-s21-fe-5g)
    - [`GALAXY S22`](#galaxy-s22)
    - [`GALAXY S21 Ultra`](#galaxy-s21-ultra)
    - [`GALAXY S22+`](#galaxy-s22)
    - [`GALAXY S22 Ultra`](#galaxy-s22-ultra)
    - [`GALAXY NOTE 20 Ultra`](#galaxy-note-20-ultra)
    - [`GALAXY M12`](#galaxy-m12)
    - [`GALAXY M52 5G`](#galaxy-m52-5g)
    - [`GALAXY Z Flip 3`](#galaxy-z-flip-3)
    - [`GALAXY Z Fold 3`](#galaxy-z-fold-3)
    - [`GALAXY Z Flip 4`](#galaxy-z-flip-4)
    - [`GALAXY Z Fold 4`](#galaxy-z-fold-4)
    - [`GALAXY A33`](#galaxy-a33)
    - [`GALAXY A73`](#galaxy-a73)

## Обзор

Данный файл `ksp_categories_phones_samsung.json` содержит конфигурационные данные для различных моделей телефонов Samsung, используемые для парсинга и категоризации товаров на сайте KSP. Он определяет соответствия между названиями моделей и URL-адресами категорий на сайте, а также содержит информацию для интеграции с PrestaShop.

## Структура файла

Файл представляет собой JSON-объект со следующей структурой:

```json
{
  "scenarios": {
    "Название модели": {
      "brand": "SAMSUNG",
      "url": "URL категории на сайте KSP",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "samsung": "Название модели"
        }
      }
    },
     "...": {
      
     }
  }
}
```

Где:
- `"scenarios"`:  Корневой объект, содержащий определения для всех моделей.
- `"Название модели"`: Ключ, представляющий название конкретной модели телефона.
  - `"brand"`: Бренд телефона, всегда `"SAMSUNG"`.
  - `"url"`: URL-адрес категории на сайте KSP для данной модели.
  - `"checkbox"`: Логический флаг, определяющий, используется ли чекбокс (всегда `false`).
  - `"active"`: Логический флаг, определяющий, активен ли сценарий (всегда `true`).
  - `"condition"`: Строка, указывающая состояние товара (всегда `"new"`).
  - `"presta_categories"`: Объект, содержащий информацию для интеграции с PrestaShop.
    - `"template"`: Объект, содержащий соответствие для PrestaShop.
        - `"samsung"`: Название модели телефона, соответствующее ключу `"Название модели"`.

## Сценарии

### `GALAXY A03 Core`

**Описание**:  Конфигурация для модели GALAXY A03 Core.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..37060..32787`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A03 Core`

### `GALAXY A03s`

**Описание**:  Конфигурация для модели GALAXY A03s.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..28236`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A03s`

### `GALAXY A04`

**Описание**:  Конфигурация для модели GALAXY A04.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..45166..45177`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A04`

### `GALAXY A12`

**Описание**:  Конфигурация для модели GALAXY A12.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..19585`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A12`

### `GALAXY A22 5G`

**Описание**:  Конфигурация для модели GALAXY A22 5G.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..30128`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A22 5G`

### `GALAXY A22`

**Описание**:  Конфигурация для модели GALAXY A22.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..30128`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A22 5G`

### `GALAXY A32`

**Описание**:  Конфигурация для модели GALAXY A32.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..23847`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A32`

### `GALAXY A52`

**Описание**:  Конфигурация для модели GALAXY A52.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..23549`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A52`

### `GALAXY A52s`

**Описание**:  Конфигурация для модели GALAXY A52s.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..28393`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A52s`

### `GALAXY A53`

**Описание**:  Конфигурация для модели GALAXY A53.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..23549`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A53`

### `GALAXY A53 5G`

**Описание**:  Конфигурация для модели GALAXY A53 5G.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..35674`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A53`

### `GALAXY A72`

**Описание**:  Конфигурация для модели GALAXY A72.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..23543`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A72`

### `GALAXY S20 FE`

**Описание**:  Конфигурация для модели GALAXY S20 FE.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..19507`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY S20 FE`

### `GALAXY S21`

**Описание**:  Конфигурация для модели GALAXY S21.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..20103`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY S21`

### `GALAXY S21 Plus`

**Описание**:  Конфигурация для модели GALAXY S21 Plus.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..20110`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY S21 Plus`

### `GALAXY S21 FE 5G`

**Описание**:  Конфигурация для модели GALAXY S21 FE 5G.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..31826`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY S21 FE 5G`

### `GALAXY S22`

**Описание**:  Конфигурация для модели GALAXY S22.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..33651`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY S22`

### `GALAXY S21 Ultra`

**Описание**:  Конфигурация для модели GALAXY S21 Ultra.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..20116`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY S21 Ultra`

### `GALAXY S22+`

**Описание**:  Конфигурация для модели GALAXY S22+.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..33652`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY S22+`

### `GALAXY S22 Ultra`

**Описание**:  Конфигурация для модели GALAXY S22 Ultra.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..33650`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY S22 Ultra`

### `GALAXY NOTE 20 Ultra`

**Описание**:  Конфигурация для модели GALAXY NOTE 20 Ultra.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..14168`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY NOTE 20 Ultra`

### `GALAXY M12`

**Описание**:  Конфигурация для модели GALAXY M12.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..31272`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY M12`

### `GALAXY M52 5G`

**Описание**:  Конфигурация для модели GALAXY M52 5G.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..29972`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY M52 5G`

### `GALAXY Z Flip 3`

**Описание**:  Конфигурация для модели GALAXY Z Flip 3.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..27347`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY Z Flip 3`

### `GALAXY Z Fold 3`

**Описание**:  Конфигурация для модели GALAXY Z Fold 3.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..27321`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY Z Fold 3`

### `GALAXY Z Flip 4`

**Описание**:  Конфигурация для модели GALAXY Z Flip 4.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..41258`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY Z Flip 4`

### `GALAXY Z Fold 4`

**Описание**:  Конфигурация для модели GALAXY Z Fold 4.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..41243`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY Z Fold 4`

### `GALAXY A33`

**Описание**:  Конфигурация для модели GALAXY A33.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/137..573..36526`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A33`

### `GALAXY A73`

**Описание**:  Конфигурация для модели GALAXY A73.
-   **`brand`**:  `SAMSUNG`
-   **`url`**:  `https://ksp.co.il/web/cat/573..137..41243..36938`
-  **`checkbox`**: `false`
-  **`active`**:  `true`
-  **`condition`**: `new`
-   **`presta_categories.template.samsung`**:  `GALAXY A73`