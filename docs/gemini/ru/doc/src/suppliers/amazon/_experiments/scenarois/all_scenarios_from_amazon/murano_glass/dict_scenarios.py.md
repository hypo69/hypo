# Модуль `dict_scenarios.py`

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, определяющий параметры для поиска и обработки товаров "Murano Glass" на сайте Amazon. Он включает URL для поиска, условие товара ("new"), категории PrestaShop и правило для определения цены.

## Подробней

Этот модуль предназначен для хранения конфигурации сценария импорта товаров "Murano Glass" с Amazon в PrestaShop. Словарь `scenario` определяет, какие товары и с какими параметрами необходимо искать на Amazon, а также в какие категории PrestaShop их следует импортировать.

## Переменные

### `scenario`

```python
scenario: dict
```

Словарь, содержащий параметры сценария для поиска и импорта товаров "Murano Glass" с Amazon.

**Как работает переменная**:

Словарь `scenario` определяет следующие параметры:

-   `"Murano Glass"`: Ключ, идентифицирующий сценарий.
    -   `"url"`: URL для поиска товаров "Art Deco murano glass" на Amazon.
    -   `"condition"`: Условие товара, в данном случае "new" (новый).
    -   `"presta_categories"`: Словарь, определяющий категории PrestaShop для импорта товаров.
        -   `"default_category"`: Словарь, связывающий ID категории PrestaShop (11209) с названием категории ("MURANO GLASS").
    -   `"price_rule"`: Правило определения цены (в данном случае 1).

**Примеры**:

```python
scenario: dict = {
    "Murano Glass": {
        "url": "https://www.amazon.com/s?k=Art+Deco+murano+glass&crid=24Q0ZZYVNOQMP&sprefix=art+deco+murano+glass%2Caps%2C230&ref=nb_sb_noss",
        "condition": "new",
        "presta_categories": {
            "default_category":{"11209":"MURANO GLASS"}
        },
        "price_rule": 1
    }
}
```