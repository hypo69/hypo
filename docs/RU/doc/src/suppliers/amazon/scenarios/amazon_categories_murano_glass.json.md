# Документация для `amazon_categories_murano_glass.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
   - [Murano Glass](#murano-glass)
    
## Обзор
Файл `amazon_categories_murano_glass.json` содержит конфигурацию для сценария обработки категорий товаров "Муранское стекло" на Amazon. Включает в себя URL страницы товара, условие, категории PrestaShop, и правило ценообразования.

## Структура JSON

Файл представляет собой JSON-объект со следующей структурой:

```json
{
  "scenarios": {
    "Название сценария": {
      "url": "URL страницы товара на Amazon",
      "condition": "Условие товара (например, new)",
      "presta_categories": {
        "default_category": { 
          "ID категории": "Название категории PrestaShop" 
         },
        "additional_categories": [ "Дополнительные категории" ]
      },
      "price_rule": "Правило ценообразования"
    }
  }
}
```

## Сценарии

### `Murano Glass`

**Описание**: Сценарий для обработки товаров категории "Муранское стекло".

**Параметры**:

-   `url` (str): URL страницы товаров "Муранское стекло" на Amazon. Значение: `https://amzn.to/3OhRz2g`
-   `condition` (str): Условие товара. Значение: `new`
-   `presta_categories` (dict):
    -   `default_category` (dict): Сопоставление ID категории PrestaShop с её названием.
        - `11209` (str): ID категории PrestaShop. Значение: `MURANO GLASS`
    -   `additional_categories` (list): Список дополнительных категорий. Значение: `[""]` (пустой список)
-   `price_rule` (int): Идентификатор правила ценообразования. Значение: `1`