# Модуль `dict_scenarios.py`

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, который определяет сценарии для извлечения данных с Amazon. В частности, он содержит информацию о товарах, условиях, категориях PrestaShop и правилах ценообразования.

## Подробней

Этот модуль предназначен для хранения конфигураций, используемых при парсинге товаров с Amazon. Словарь `scenario` содержит настройки для различных категорий товаров, такие как "Murano Glass". Каждая категория содержит URL для поиска товаров на Amazon, условие товара, соответствия категориям в PrestaShop и правило ценообразования.

## Переменные

### `scenario`

```python
scenario: dict = {
    "Murano Glass": {
        "url": "https://www.amazon.com/s?k=Art+Deco+murano+glass&crid=24Q0ZZYVNOQMP&sprefix=art+deco+murano+glass%2Caps%2C230&ref=nb_sb_noss",
        "condition": "new",
        "presta_categories": {
            "default_category": {"11209": "MURANO GLASS"}
        },
        "price_rule": 1
    }
}
```

**Описание**: Словарь, содержащий сценарии для парсинга товаров с Amazon.

**Как работает переменная**:

Словарь `scenario` содержит настройки для различных категорий товаров, используемые при парсинге данных с Amazon.

- `"Murano Glass"`: Ключ, представляющий категорию товара "Муранское стекло".
    - `"url"`: URL для поиска товаров "Муранское стекло" на Amazon.
    - `"condition"`: Условие товара, в данном случае "new" (новый).
    - `"presta_categories"`: Словарь, определяющий соответствие категорий Amazon категориям в PrestaShop.
        - `"default_category"`: Словарь, содержащий соответствие идентификатора категории PrestaShop (11209) названию категории ("MURANO GLASS").
    - `"price_rule"`: Ценовое правило, применяемое к товарам этой категории (в данном случае 1).

**Примеры**:

```python
# Пример использования scenario для получения URL категории "Murano Glass"
url = scenario["Murano Glass"]["url"]
print(url)
# Вывод: https://www.amazon.com/s?k=Art+Deco+murano+glass&crid=24Q0ZZYVNOQMP&sprefix=art+deco+murano+glass%2Caps%2C230&ref=nb_sb_noss
```