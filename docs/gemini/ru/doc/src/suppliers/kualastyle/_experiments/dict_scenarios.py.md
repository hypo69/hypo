# Модуль `dict_scenarios.py`

## Обзор

Модуль содержит словарь `scenarios`, который определяет сценарии для различных категорий товаров (например, "Sofas and Sectionals", "Bookcases and Display Cabinets"). Каждый сценарий включает информацию о URL категории, ее активности, состоянии товаров, соответствии категориям PrestaShop, наличии чекбокса и правиле ценообразования.

## Подробней

Этот файл предназначен для хранения и организации данных о различных сценариях категорий товаров. Эти сценарии используются для автоматизации процессов, связанных с категориями товаров. Например, для автоматической категоризации товаров в PrestaShop или для применения правил ценообразования.

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

**Структура**:

-   **Ключ**: Название категории товаров (например, `"Sofas and Sectionals"`).
-   **Значение**: Словарь, содержащий информацию о сценарии для данной категории:
    -   `"url"`: URL страницы категории.
    -   `"active"`: Активен ли сценарий (True/False).
    -   `"condition"`: Состояние товаров ("new").
    -   `"presta_categories"`: Словарь, содержащий информацию о категориях PrestaShop:
        -   `"default_category"`: Словарь, где ключ - ID категории PrestaShop, а значение - название категории.
    -   `"checkbox"`: Флаг, указывающий на наличие чекбокса (True/False).
    -   `"price_rule"`: Правило ценообразования (числовое значение).

**Примеры**:

```python
# Пример доступа к URL категории "Sofas and Sectionals"
sofas_url = scenarios["Sofas and Sectionals"]["url"]
print(sofas_url)  # Вывод: https://kualastyle.com/collections/%D7%A1%D7%A4%D7%95%D7%AA-%D7%9E%D7%A2%D7%95%D7%A6%D7%91%D7%95%D7%AA

# Пример проверки активности сценария для категории "Bookcases and Display Cabinets"
bookcases_active = scenarios["Bookcases and Display Cabinets"]["active"]
print(bookcases_active)  # Вывод: True
```