# Модуль `dict_scenarios.py`

## Обзор

Модуль содержит словарь `scenario`, который определяет параметры для сценария поиска и категоризации товаров "Murano Glass" на Amazon. Эти параметры включают URL для поиска, условие товара, категории PrestaShop и правило цены.

## Подробней

Этот модуль предназначен для хранения конфигурации, необходимой для автоматизации процесса сбора и категоризации товаров "Murano Glass" с Amazon. Словарь `scenario` содержит всю необходимую информацию для определения источника данных, условий отбора товаров и правил их категоризации в PrestaShop.

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

**Описание**: Словарь, содержащий параметры сценария для "Murano Glass".

- `"Murano Glass"`: Ключ, идентифицирующий сценарий.

  - `"url"`: URL для поиска товаров "Art Deco murano glass" на Amazon.
  - `"condition"`: Условие товара, в данном случае "new" (новый).
  - `"presta_categories"`: Категории PrestaShop, в которые следует отнести товары.
    - `"default_category"`: Словарь, связывающий ID категории (11209) с названием ("MURANO GLASS").
  - `"price_rule"`: Правило цены, применяемое к товарам (в данном случае 1).

**Как работает переменная**:

Переменная `scenario` представляет собой структуру данных, которая определяет параметры для автоматизированного сценария сбора и категоризации товаров "Murano Glass" с Amazon. URL используется для поиска товаров на Amazon. Параметр "condition" указывает, что необходимо собирать только новые товары. "presta_categories" определяет, в какую категорию PrestaShop следует помещать товары. "price_rule" задает правило для определения цены товаров.

**Примеры**:

```python
# Пример использования словаря scenario для получения URL:
url = scenario["Murano Glass"]["url"]
print(url)  # Вывод: https://www.amazon.com/s?k=Art+Deco+murano+glass&crid=24Q0ZZYVNOQMP&sprefix=art+deco+murano+glass%2Caps%2C230&ref=nb_sb_noss

# Пример использования словаря scenario для получения ID категории PrestaShop:
category_id = list(scenario["Murano Glass"]["presta_categories"]["default_category"].keys())[0]
print(category_id)  # Вывод: 11209