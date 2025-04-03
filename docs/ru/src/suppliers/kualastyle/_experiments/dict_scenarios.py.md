# Модуль `dict_scenarios.py`

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenarios`, который определяет сценарии для категорий товаров, включая URL-адреса, статусы активности, условия, категории PrestaShop и правила ценообразования. Этот словарь используется для настройки параметров категорий товаров, которые будут обрабатываться или импортироваться.

## Подробней

Этот модуль предоставляет структуру данных для управления различными сценариями, связанными с категориями товаров. Он используется для настройки параметров категорий, таких как URL-адрес, статус активности, условие, категории PrestaShop и правила ценообразования.

## Переменные

### `scenarios`

```python
scenarios: dict = {
    "Sofas and Sectionals": {
        "url": "https://kualastyle.com/collections/%D7%A1%D7%A4%D7%95%D7%AA-%D7%9E%D7%A2%D7%95%D7%A6%D7%91%D7%95%D7%AA",
        "active": True,
        "condition": "new",
        "presta_categories": {
            "default_category": {"11055": "Sofas and Sectionals"}
        },
        "checkbox": False,
        "price_rule": 1
    },
    "Bookcases and Display Cabinets": {
        "url": "https://kualastyle.com/collections/%D7%9E%D7%96%D7%A0%D7%95%D7%A0%D7%99%D7%9D-%D7%99%D7%97%D7%99%D7%93%D7%95%D7%AA-%D7%98%D7%9C%D7%95%D7%95%D7%99%D7%96%D7%99%D7%94",
        "active": True,
        "condition": "new",
        "presta_categories": {
            "default_category": {"11061": "ספריות ומזנונים"}
        },
        "price_rule": 1
    }
}
```

**Описание**: Словарь, содержащий сценарии для различных категорий товаров.

- **Ключи**: Названия категорий товаров (например, "Sofas and Sectionals", "Bookcases and Display Cabinets").
- **Значения**: Словари, содержащие параметры для каждой категории.

**Параметры внутри словаря для каждой категории**:

- `"url"` (str): URL-адрес коллекции товаров.
- `"active"` (bool): Указывает, активна ли категория.
- `"condition"` (str): Условие товаров (например, "new").
- `"presta_categories"` (dict): Словарь, содержащий категории PrestaShop.
    - `"default_category"` (dict): Словарь, содержащий идентификатор и название категории по умолчанию.
- `"checkbox"` (bool): Указывает, используется ли чекбокс для данной категории.
- `"price_rule"` (int): Правило ценообразования для категории.

**Примеры**:

```python
scenarios = {
    "Sofas and Sectionals": {
        "url": "https://kualastyle.com/...",
        "active": True,
        "condition": "new",
        "presta_categories": {
            "default_category": {"11055": "Sofas and Sectionals"}
        },
        "checkbox": False,
        "price_rule": 1
    },
    "Bookcases and Display Cabinets": {
        "url": "https://kualastyle.com/...",
        "active": True,
        "condition": "new",
        "presta_categories": {
            "default_category": {"11061": "ספריות ומזנונים"}
        },
        "price_rule": 1
    }
}
```