# Модуль `dict_scenarios.py`

## Обзор

Модуль содержит словарь `scenario`, который определяет параметры для поиска и обработки товаров "Murano Glass" на сайте Amazon, а также их последующей загрузки в PrestaShop.

## Подробней

Данный модуль является частью экспериментального кода в проекте `hypotez`, предназначенного для автоматизации процессов, связанных с поставщиками, в частности, Amazon. Словарь `scenario` содержит конфигурацию для конкретного сценария работы с товарами "Murano Glass".

## Переменные

### `scenario`

```python
scenario: dict
```

Словарь, содержащий параметры для поиска и обработки товаров на Amazon.

**Структура словаря `scenario`**:

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

**Ключи верхнего уровня**:
- `"Murano Glass"`: Название сценария.

**Вложенные ключи**:
- `"url"`: URL для поиска товаров на Amazon.
- `"condition"`: Состояние товара (в данном случае, "new").
- `"presta_categories"`: Информация о категориях PrestaShop, куда следует загружать товары.
    - `"default_category"`: Словарь, где ключ - ID категории (в данном случае, "11209"), а значение - название категории ("MURANO GLASS").
- `"price_rule"`: Правило ценообразования (в данном случае, "1").

**Как работает переменная `scenario`**:

1.  **Определение сценария**: Переменная `scenario` определяет параметры для поиска и обработки товаров "Murano Glass" на Amazon.
2.  **Конфигурация параметров**: Включает URL поиска, состояние товара, категории PrestaShop и правило ценообразования.
3.  **Использование в процессах**: Используется для автоматизации поиска, извлечения данных и загрузки товаров в PrestaShop.

**Примеры**:

```python
# Пример доступа к URL поиска
url = scenario["Murano Glass"]["url"]
print(url)
# Вывод: https://www.amazon.com/s?k=Art+Deco+murano+glass&crid=24Q0ZZYVNOQMP&sprefix=art+deco+murano+glass%2Caps%2C230&ref=nb_sb_noss

# Пример доступа к категории PrestaShop
category_id = list(scenario["Murano Glass"]["presta_categories"]["default_category"].keys())[0]
category_name = scenario["Murano Glass"]["presta_categories"]["default_category"][category_id]
print(f"ID категории: {category_id}, Название категории: {category_name}")
# Вывод: ID категории: 11209, Название категории: MURANO GLASS