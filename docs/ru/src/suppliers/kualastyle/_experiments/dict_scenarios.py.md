# `dict_scenarios.py`

## Обзор

Файл `dict_scenarios.py` содержит словарь `scenarios`, определяющий параметры для различных категорий товаров (например, "Sofas and Sectionals", "Bookcases and Display Cabinets") на сайте `kualastyle.com`. Каждый сценарий включает URL, статус активности, состояние товара, категории PrestaShop и правила ценообразования. Этот файл, вероятно, используется для конфигурации процесса сбора данных о товарах или для интеграции с PrestaShop.

## Подробней

Словарь `scenarios` содержит настройки для каждой категории товаров, необходимые для парсинга данных с сайта Kualastyle и их последующей обработки. Например, `url` указывает на страницу категории товаров, `active` определяет, активна ли категория для обработки, `condition` указывает состояние товара (например, "new"), `presta_categories` содержит информацию для интеграции с PrestaShop, а `price_rule` задает правило ценообразования.

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

**Описание**: Словарь, содержащий настройки для различных категорий товаров.

**Как работает переменная**:
Словарь `scenarios` содержит ключи, соответствующие названиям категорий товаров. Для каждой категории заданы параметры в виде словаря, включающие:

- `"url"`: URL страницы категории товаров.
- `"active"`: Флаг, указывающий, активна ли данная категория для обработки.
- `"condition"`: Состояние товара (например, `"new"`).
- `"presta_categories"`: Информация о категориях PrestaShop, включая `"default_category"` и её ID.
- `"checkbox"`: Не используется
- `"price_rule"`: Правило ценообразования.

**Параметры**:

- Нет отдельных параметров, так как это переменная, а не функция или класс.

**Примеры**:

```python
# Пример доступа к данным для категории "Sofas and Sectionals"
sofas_scenario = scenarios["Sofas and Sectionals"]
print(sofas_scenario["url"])
# Вывод: https://kualastyle.com/collections/%D7%A1%D7%A4%D7%95%D7%AA-%D7%9E%D7%A2%D7%95%D7%A6%D7%91%D7%95%D7%AA
```