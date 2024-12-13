# Документация для `hypotez/src/suppliers/amazon/scenarios/amazon_categories_desktops_hp_used.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [`USED HP DESKTOP INTEL I5`](#used-hp-desktop-intel-i5)
    - [`USED HP DESKTOP AMD RYZEN 5`](#used-hp-desktop-amd-ryzen-5)
## Обзор

Этот файл содержит JSON-конфигурацию для сценариев парсинга категорий товаров (десктопов) бренда HP с сайта Amazon. Он определяет настройки для различных условий и типов процессоров (Intel i5 и AMD Ryzen 5) подержанных товаров.

## Структура JSON

JSON файл имеет следующую структуру:

```json
{
  "scenarios": {
    "SCENARIO_NAME_1": {
      "brand": "string",
      "url": "string",
      "active": "boolean",
      "condition": "string",
      "presta_categories": {
        "template": {
          "brand_name": "string"
        }
      },
      "checkbox": "boolean",
      "price_rule": "number"
    },
     "SCENARIO_NAME_2": {
      "brand": "string",
      "url": "string",
      "active": "boolean",
      "condition": "string",
      "presta_categories": {
        "template": {
          "brand_name": "string"
        }
      },
      "checkbox": "boolean",
      "price_rule": "number"
    }
  }
}
```

где:

- `scenarios`: Объект, содержащий различные сценарии.
- `SCENARIO_NAME_X`: Ключ, представляющий имя конкретного сценария.
- `brand`: Название бренда.
- `url`: URL для парсинга с сайта Amazon.
- `active`: Логический флаг, указывающий, активен ли сценарий.
- `condition`: Условие товара (например, "new", "used").
- `presta_categories`: Объект, содержащий соответствия категорий для PrestaShop.
    - `template`: Объект, содержащий соответствия категорий с ключом, равным названию бренда.
- `checkbox`: Логический флаг, используемый для каких-то целей.
- `price_rule`: Идентификатор правила цены.

## Сценарии

### `USED HP DESKTOP INTEL I5`

**Описание**: Сценарий для парсинга подержанных десктопов HP с процессором Intel i5.

**Параметры**:
- `brand` (string): "HP"
- `url` (string): "https://www.amazon.com/s?i=computers&bbn=565098&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565098%2Cp_n_is_free_shipping%3A10236242011%2Cp_n_condition-type%3A2224373011%2Cp_89%3AHP%2Cp_n_feature_four_browse-bin%3A2289793011&dc&qid=1674309202&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_1&ds=v1%3A3opKFvNsBrAlTma48Fhm9Z15nWOKHypDzbdHeg0IvUI"
- `active` (boolean): `true`
- `condition` (string): `"new"`
- `presta_categories` (object):
    - `template` (object):
        - `hp`: `"DESKTOPS INTEL I3"`
- `checkbox` (boolean): `false`
- `price_rule` (number): `1`

### `USED HP DESKTOP AMD RYZEN 5`

**Описание**: Сценарий для парсинга подержанных десктопов HP с процессором AMD Ryzen 5.

**Параметры**:
- `brand` (string): "HP"
- `url` (string): "https://www.amazon.com/s?i=computers&bbn=565098&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565098%2Cp_n_is_free_shipping%3A10236242011%2Cp_n_condition-type%3A2224373011%2Cp_89%3AHP%2Cp_n_feature_four_browse-bin%3A18107801011%7C2289793011&dc&qid=1674309214&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_2&ds=v1%3Ahqid0YcY15vr344QTI%2Bwl3faAO4P4Fa7PRg81bZauW8"
- `active` (boolean): `true`
- `condition` (string): `"new"`
- `presta_categories` (object):
    - `template` (object):
        - `hp`: `"DESKTOPS INTEL I5"`
- `checkbox` (boolean): `false`
- `price_rule` (number): `1`