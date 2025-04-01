# Модуль `dict_scenarios.py`

## Обзор

Модуль содержит словарь `scenarios`, который используется для хранения информации о различных категориях товаров (например, "Sofas and Sectionals", "Bookcases and Display Cabinets") для поставщика Kualastyle. Каждая категория содержит URL, флаг активности, состояние товара, настройки категорий PrestaShop, флаг для чекбоксов и правило для цены.

## Подробней

Этот модуль предназначен для хранения и организации данных, необходимых для работы с категориями товаров на сайте Kualastyle. Данные включают URL страниц категорий, информацию об активности, состоянии товаров и настройках для интеграции с PrestaShop. Эта информация может использоваться для автоматизации процессов, связанных с загрузкой и обновлением данных о товарах на сайте.

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

**Как работает**:

1.  Словарь `scenarios` предназначен для хранения конфигураций категорий товаров.
2.  Каждый ключ в словаре представляет собой название категории товара (например, `"Sofas and Sectionals"`).
3.  Значением каждого ключа является словарь, содержащий параметры конфигурации для данной категории:
    *   `url`: URL страницы категории на сайте Kualastyle.
    *   `active`: Булево значение, указывающее, активна ли категория.
    *   `condition`: Состояние товара (например, `"new"`).
    *   `presta_categories`: Словарь, содержащий настройки категорий для PrestaShop. Включает подкатегорию `default_category` с идентификатором и названием категории.
    *   `checkbox`: Булево значение, определяющее необходимость использования чекбокса.
    *   `price_rule`: Правило для определения цены товара.

**Примеры**:

```python
scenarios = {
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