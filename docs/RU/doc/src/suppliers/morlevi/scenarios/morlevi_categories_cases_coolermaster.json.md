# Документация для `morlevi_categories_cases_coolermaster.json`

## Оглавление
- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Сценарии](#сценарии)
    - [COOLERMASTER MID TOWER](#coolermaster-mid-tower)
    - [COOLERMASTER full tower](#coolermaster-full-tower)
    - [COOLERMASTER mini tower](#coolermaster-mini-tower)
    - [COOLERMASTER gaming MID TOWER](#coolermaster-gaming-mid-tower)
    - [COOLERMASTER gaming full tower](#coolermaster-gaming-full-tower)
    - [COOLERMASTER mini itx](#coolermaster-mini-itx)
   
## Обзор

Файл `morlevi_categories_cases_coolermaster.json` содержит JSON-структуру, описывающую сценарии для категорий корпусов (cases) бренда COOLER MASTER. Каждый сценарий определяет параметры для фильтрации и сопоставления товаров с категориями на сайте Morlevi.

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "SCENARIO_NAME": {
      "brand": "BRAND_NAME",
      "template": "TEMPLATE_STRING",
      "url": "URL_STRING",
      "checkbox": BOOLEAN,
      "active": BOOLEAN,
      "condition": "CONDITION_STRING",
       "presta_categories": {
         "template": {
           "BRAND_NAME": "CATEGORY_NAME"
         }
       }
    }
    ...
  }
}
```
Где:

- `"scenarios"`: Основной объект, содержащий сценарии.
- `"SCENARIO_NAME"`: Ключ, идентифицирующий конкретный сценарий (например, "COOLERMASTER MID TOWER").
- `"brand"`: Строка, указывающая бренд товара (например, `"COOLER MASTER"`).
- `"template"`: Строка, представляющая шаблон (в данном случае пустая строка).
- `"url"`: Строка, содержащая URL-адрес страницы с товарами на сайте Morlevi.
- `"checkbox"`: Логическое значение, указывающее, нужно ли использовать checkbox.
- `"active"`: Логическое значение, указывающее, активен ли сценарий.
- `"condition"`: Строка, указывающая условие товара (например, `"new"`).
- `"presta_categories"`: Объект, содержащий информацию о категориях PrestaShop.
    - `"template"`: Объект, содержащий сопоставление бренда и категории.

## Сценарии

### `COOLERMASTER MID TOWER`

**Описание**: Сценарий для корпусов COOLER MASTER типа MID TOWER.

**Параметры**:

- `brand`: `"COOLER MASTER"`
- `template`: `""`
- `url`: `"https://www.morlevi.co.il/Cat/285?p_315=74&p_124=540&sort=datafloat2%2Cprice&keyword="`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`: `{"cooler master": "MID TOWER"}`

### `COOLERMASTER full tower`

**Описание**: Сценарий для корпусов COOLER MASTER типа FULL TOWER.

**Параметры**:

- `brand`: `"COOLER MASTER"`
- `template`: `""`
- `url`: `"https://www.morlevi.co.il/Cat/285?p_315=74&p_124=541&sort=datafloat2%2Cprice&keyword="`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`: `{"cooler master": "FULL TOWER"}`

### `COOLERMASTER mini tower`

**Описание**: Сценарий для корпусов COOLER MASTER типа MINI TOWER.

**Параметры**:

- `brand`: `"COOLER MASTER"`
- `template`: `""`
- `url`: `"https://www.morlevi.co.il/Cat/285?p_315=74&p_124=542&sort=datafloat2%2Cprice&keyword="`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`: `{"cooler master": "MINI TOWER"}`

### `COOLERMASTER gaming MID TOWER`

**Описание**: Сценарий для игровых корпусов COOLER MASTER типа MID TOWER.

**Параметры**:

- `brand`: `"COOLER MASTER"`
- `template`: `""`
- `url`: `"https://www.morlevi.co.il/Cat/285?p_315=74&p_124=545&sort=datafloat2%2Cprice&keyword="`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`: `{"cooler master": "GAMING MID TOWER"}`

### `COOLERMASTER gaming full tower`

**Описание**: Сценарий для игровых корпусов COOLER MASTER типа FULL TOWER.

**Параметры**:

- `brand`: `"COOLER MASTER"`
- `template`: `""`
- `url`: `"----------------------------COOLER MASTER gaming full TOWER--------------------------------"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`: `{"cooler master": "GAMING FULL TOWER"}`

### `COOLERMASTER mini itx`

**Описание**: Сценарий для корпусов COOLER MASTER типа MINI ITX.

**Параметры**:

- `brand`: `"COOLER MASTER"`
- `template`: `""`
- `url`: `"https://www.morlevi.co.il/Cat/285?p_124=3527&sort=datafloat2%2Cprice&keyword="`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`: `{"cooler master": "MINI ITX"}`