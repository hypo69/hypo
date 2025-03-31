# Модуль `dict_scenarios.py`

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, который определяет сценарий для категории "Murano Glass" на Amazon. Он задает URL для поиска товаров, условие (состояние) товаров, категории PrestaShop, к которым они должны быть отнесены, и правило ценообразования.

## Подробней

Этот модуль предоставляет конфигурацию для автоматизации поиска и категоризации товаров "Murano Glass" на Amazon. Он определяет параметры, необходимые для извлечения данных о товарах и их импорта в PrestaShop.

## Переменные

### `scenario`

**Описание**: Словарь, содержащий конфигурацию сценария для категории "Murano Glass".

**Как работает переменная**:
Словарь `scenario` содержит следующие ключи:
- `"Murano Glass"`: Ключ, идентифицирующий категорию сценария.
    - `"url"`: URL для поиска товаров "Art Deco murano glass" на Amazon.
    - `"condition"`: Условие товаров, в данном случае "new".
    - `"presta_categories"`: Словарь, определяющий категории PrestaShop, к которым должны быть отнесены товары.
        - `"default_category"`: Категория по умолчанию, содержащая соответствие между идентификатором категории `11209` и названием `"MURANO GLASS"`.
    - `"price_rule"`: Правило ценообразования, в данном случае `1`.

## Примеры

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
В данном примере показана структура словаря `scenario` с определенными значениями для категории "Murano Glass".