# Модуль `dict_scenarios`

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, который определяет сценарии для сбора данных с Amazon. В частности, он содержит настройки для категории "Murano Glass", включая URL для поиска, состояние товара, соответствие категориям PrestaShop и правило для определения цены.

## Подробней

Этот модуль используется для конфигурации процесса сбора данных с Amazon, определяя параметры для конкретных категорий товаров. Словарь `scenario` служит центральным местом для хранения этих параметров, позволяя легко настраивать и расширять процесс сбора данных.

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

**Описание**: Словарь, содержащий сценарии для сбора данных с Amazon.

**Как работает переменная**:

1.  **Ключ `"Murano Glass"`**: Определяет категорию товара "Murano Glass".
2.  **`"url"`**: URL для поиска товаров Murano Glass на Amazon.
3.  **`"condition"`**: Состояние товара, в данном случае "new" (новый).
4.  **`"presta_categories"`**: Соответствие категорий Amazon категориям в PrestaShop.
    *   `"default_category"`: Словарь, где ключ `"11209"` - это ID категории в PrestaShop, а значение `"MURANO GLASS"` - название категории.
5.  **`"price_rule"`**: Правило для определения цены товара. В данном случае установлено значение `1`.

**Примеры**:

```python
# Пример доступа к URL для категории Murano Glass
murano_glass_url = scenario["Murano Glass"]["url"]
print(murano_glass_url)
# Вывод: https://www.amazon.com/s?k=Art+Deco+murano+glass&crid=24Q0ZZYVNOQMP&sprefix=art+deco+murano+glass%2Caps%2C230&ref=nb_sb_noss