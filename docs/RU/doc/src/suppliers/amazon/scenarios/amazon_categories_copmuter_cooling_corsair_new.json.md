# Документация для `amazon_categories_copmuter_cooling_corsair_new.json`

## Обзор

Этот файл содержит JSON-конфигурацию для сценариев парсинга товаров Amazon, связанных с компьютерным охлаждением бренда Corsair. Конфигурация включает в себя сценарии для жидкостного и воздушного охлаждения, определяя URL-адреса для поиска, условия, правила ценообразования и категории PrestaShop.

## Оглавление

1. [Структура JSON](#структура-json)
2. [Сценарии](#сценарии)
   - [NEW CORSAIR LIQUID COOLING](#new-corsair-liquid-cooling)
   - [NEW CORSAIR AIR CHAISES COOLING](#new-corsair-air-chaises-cooling)

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "SCENARIO_NAME": {
      "brand": "BRAND_NAME",
      "url": "URL_FOR_PARSING",
      "active": true/false,
      "condition": "ref",
      "presta_categories": {
        "template": {
          "brand_name": "PRESTA_CATEGORY_NAME"
        }
      },
      "checkbox": true/false,
      "price_rule": INTEGER_VALUE
    }
  }
}
```
Где:
- `scenarios`: Основной объект, содержащий все сценарии парсинга.
- `SCENARIO_NAME`: Название сценария парсинга.
- `brand`: Название бренда товаров.
- `url`: URL для парсинга товаров на Amazon.
- `active`: Логическое значение, указывающее, активен ли сценарий.
- `condition`: Условие отбора товаров (в данном случае всегда "ref").
- `presta_categories`: Объект, содержащий сопоставление бренда с категорией PrestaShop.
- `checkbox`: Логическое значение, определяющее использование чекбокса в интерфейсе.
- `price_rule`: Целочисленное значение, определяющее правило ценообразования.

## Сценарии

### NEW CORSAIR LIQUID COOLING

**Описание**: Сценарий для парсинга жидкостного охлаждения Corsair на Amazon.

**Параметры**:

- `brand` (str): "CORSAIR"
- `url` (str): "https://www.amazon.com/s?k=corsair&i=computers&rh=n%3A3015422011%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ACorsair&dc&ds=v1%3A4UdJ5kFgxTrEAPAFY6KYx4O48jHaTgY%2BkKFEZHAmBy4&qid=1674395191&rnid=2528832011&ref=sr_nr_p_89_1"
- `active` (bool): true
- `condition` (str): "ref"
- `presta_categories` (dict): 
  - `template` (dict): 
    - `corsair` (str): "LIQUID CPU COOLING"
- `checkbox` (bool): false
- `price_rule` (int): 1

**Назначение**: Парсинг товаров жидкостного охлаждения Corsair с Amazon и их отнесение к категории "LIQUID CPU COOLING" в PrestaShop.

### NEW CORSAIR AIR CHAISES COOLING

**Описание**: Сценарий для парсинга воздушного охлаждения Corsair на Amazon.

**Параметры**:

- `brand` (str): "CORSAIR"
- `url` (str): "https://www.amazon.com/s?k=corsair&i=computers&rh=n%3A172282%2Cn%3A541966%2Cn%3A193870011%2Cn%3A17923671011%2Cn%3A3012290011%2Cn%3A11036291%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ACorsair&dc&ds=v1%3A62ROR5QIpRmdvHYid8HLE4S5XJ9aeeOJV%2B9%2Fka%2FPYS8&qid=1674395269&rnid=172282&ref=sr_nr_n_2"
- `active` (bool): true
- `condition` (str): "ref"
- `presta_categories` (dict):
   - `template` (dict):
       - `corsair` (str): "AIR CHAISES COOLING"
- `checkbox` (bool): false
- `price_rule` (int): 1

**Назначение**: Парсинг товаров воздушного охлаждения Corsair с Amazon и их отнесение к категории "AIR CHAISES COOLING" в PrestaShop.