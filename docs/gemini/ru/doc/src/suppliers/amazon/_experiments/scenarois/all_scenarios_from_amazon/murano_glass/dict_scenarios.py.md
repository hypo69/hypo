# Модуль `dict_scenarios.py`

## Обзор

Модуль содержит словарь `scenario`, который определяет сценарий для поиска и категоризации товаров "Murano Glass" на сайте Amazon. Этот сценарий включает URL для поиска, условия поиска ("new"), категории PrestaShop для классификации товаров и правило ценообразования.

## Подробней

Этот модуль предоставляет структуру данных, необходимую для автоматизации процесса поиска и категоризации товаров "Murano Glass" на Amazon. Словарь `scenario` содержит всю необходимую информацию для определения, как искать продукты, какие условия использовать и как их категоризировать в PrestaShop.

## Переменные

### `scenario`

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

**Описание**: Словарь, содержащий сценарий для поиска и категоризации товаров "Murano Glass" на Amazon.

**Структура**:

- `"Murano Glass"` (str): Ключ, идентифицирующий сценарий для "Murano Glass".
    - `"url"` (str): URL для поиска товаров "Art Deco murano glass" на Amazon.
    - `"condition"` (str): Условие для поиска товаров, в данном случае "new" (новые).
    - `"presta_categories"` (dict): Словарь категорий PrestaShop для классификации товаров.
        - `"default_category"` (dict): Словарь, содержащий соответствие между идентификатором категории (11209) и названием категории ("MURANO GLASS").
    - `"price_rule"` (int): Правило ценообразования, используемое для товаров (в данном случае 1).

**Как работает словарь `scenario`**:

Словарь `scenario` определяет параметры для автоматического поиска и категоризации товаров "Murano Glass" на Amazon. Он указывает URL для поиска, условие (новые товары), категории PrestaShop для классификации товаров и правило ценообразования.

**Примеры**:

```python
scenario = {
    "Murano Glass": {
        "url": "https://www.amazon.com/s?k=Art+Deco+murano+glass&crid=24Q0ZZYVNOQMP&sprefix=art+deco+murano+glass%2Caps%2C230&ref=nb_sb_noss",
        "condition": "new",
        "presta_categories": {
            "default_category":{"11209":"MURANO GLASS"}
        },
        "price_rule": 1
    }
}

# Доступ к URL для поиска товаров "Murano Glass"
url = scenario["Murano Glass"]["url"]
print(url)  # Вывод: https://www.amazon.com/s?k=Art+Deco+murano+glass&crid=24Q0ZZYVNOQMP&sprefix=art+deco+murano+glass%2Caps%2C230&ref=nb_sb_noss

# Доступ к условию для поиска товаров
condition = scenario["Murano Glass"]["condition"]
print(condition)  # Вывод: new

# Доступ к категориям PrestaShop для классификации товаров
presta_categories = scenario["Murano Glass"]["presta_categories"]
print(presta_categories)  # Вывод: {'default_category': {'11209': 'MURANO GLASS'}}

# Доступ к правилу ценообразования
price_rule = scenario["Murano Glass"]["price_rule"]
print(price_rule)  # Вывод: 1