# morlevi_categories_memory.json

## Обзор

Этот файл содержит JSON-структуру, описывающую различные сценарии для категорий памяти (RAM) от разных производителей, таких как CORSAIR, CRUCIAL, G.SKILL и KINGSTON, на сайте Morlevi. Каждый сценарий включает информацию о бренде, URL-адресе для поиска товара, статусе активации, состоянии товара ("new") и соответствующих категориях PrestaShop.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура](#структура)
    *   [scenarios](#scenarios)
        *   [Сценарий](#сценарий)
            *   [brand](#brand)
            *   [url](#url)
            *   [checkbox](#checkbox)
            *   [active](#active)
            *   [condition](#condition)
            *   [presta_categories](#presta_categories)
                *  [template](#template)
 

## Структура

### `scenarios`

**Описание**: Объект, содержащий все сценарии для категорий памяти. Каждый ключ этого объекта - это название сценария, а значение - объект, описывающий конкретный сценарий.

### `Сценарий`
  
  **Описание**: Каждый сценарий представляет собой набор параметров для поиска и категоризации определенного типа памяти.

#### `brand`

**Описание**: Бренд производителя памяти (например, "CORSAIR", "CRUCIAL", "G.SKILL", "KINGSTON").

#### `url`

**Описание**: URL-адрес для поиска соответствующей категории памяти на сайте Morlevi. Содержит параметры фильтрации по бренду, объему и другим характеристикам.

#### `checkbox`

**Описание**: Логическое значение, указывающее, выбран ли сценарий для обработки (всегда `false` в текущем контексте).

#### `active`

**Описание**: Логическое значение, указывающее, активен ли сценарий. (`true` - активен).

#### `condition`

**Описание**: Состояние товара, всегда `"new"` для всех сценариев.

#### `presta_categories`

**Описание**: Объект, содержащий информацию о категориях PrestaShop.

##### `template`

**Описание**: Объект, где ключи - это бренды в нижнем регистре, а значения - категории памяти для PrestaShop.

## Примеры сценариев

### CORSAIR DIMM DDR 4 16GB
  
  **Описание**: Сценарий для поиска памяти CORSAIR DIMM DDR 4 16GB.
  
  **Параметры**:
    - `brand`: "CORSAIR"
    - `url`:  "https://www.morlevi.co.il/Cat/149?p_315=20&p_45=100&p_44=93&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: `"new"`
    - `presta_categories`:
        - `template`: {"corsair": "DIMM DDR 4 16GB"}

### CRUCIAL DIMM DDR 4 8GB
  
  **Описание**: Сценарий для поиска памяти CRUCIAL DIMM DDR 4 8GB.
  
  **Параметры**:
    - `brand`: "CRUCIAL"
    - `url`:  "https://www.morlevi.co.il/Cat/152?p_315=19&p_45=100&p_44=92&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: `"new"`
    - `presta_categories`:
        - `template`: {"crucial": "DIMM DDR 4 8GB"}

### KINGSTON DIMM DDR5 8GB
  
  **Описание**: Сценарий для поиска памяти KINGSTON DIMM DDR5 8GB.
  
  **Параметры**:
    - `brand`: "KINGSTON"
    - `url`:  "https://www.morlevi.co.il/Cat/149?p_315=22&p_45=4090&p_44=92&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: `"new"`
    - `presta_categories`:
        - `template`: {"kingston": "DIMM DDR 5 8GB"}