# Документация для `aromatherapy.json`

## Обзор

Файл `aromatherapy.json` содержит JSON-конфигурацию для сценариев, связанных с категорией "ароматерапия" в интернет-магазине. В частности, он описывает сценарии для диффузоров, их URL, названия, условия и категории PrestaShop.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [Диффузоры (`diffusers`)](#диффузоры-diffusers)

## Структура JSON

Файл состоит из одного корневого объекта, содержащего ключ `scenarios`, который является словарем со сценариями.

```json
{
  "scenarios": {
    "diffusers": {
      "url": "https://hbdeadsea.co.il/product-category/aromatherapy/diffusers/",
      "name": "מפיצי ריח ומילוי",
      "condition": "new",
      "presta_categories": {
        "default_category": 11246,
        "additional_categories": []
      }
    }
  }
}
```

## Сценарии

### Диффузоры (`diffusers`)

**Описание**:  Сценарий для обработки данных, связанных с диффузорами для ароматерапии.

**Параметры**:

-   `url` (str): URL страницы с диффузорами. В данном случае `https://hbdeadsea.co.il/product-category/aromatherapy/diffusers/`.
-   `name` (str): Название сценария, представленное на иврите `מפיצי ריח ומילוי`.
-   `condition` (str): Условие для товаров, в данном случае "new", что означает новые товары.
-   `presta_categories` (dict): Словарь, содержащий информацию о категориях PrestaShop.
    - `default_category` (int): ID основной категории в PrestaShop, в данном случае 11246.
    - `additional_categories` (list): Список дополнительных категорий в PrestaShop. В данном случае пустой список `[]`.