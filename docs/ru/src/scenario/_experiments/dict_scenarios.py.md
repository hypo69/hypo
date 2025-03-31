# Модуль `src.scenario._experiments.dict_scenarios`

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, который определяет параметры для различных сценариев, связанных с продуктами, такими как "Apple Wathes" и "Murano Glass". Эти сценарии используются для настройки процесса сбора и обработки данных о продуктах на Amazon, а также для интеграции с PrestaShop.

## Подробней

Этот модуль предоставляет структуру данных для настройки экспериментов, связанных с извлечением информации о продуктах с Amazon и их последующей категоризацией в PrestaShop. Словарь `scenario` содержит конфигурации для различных продуктов, включая URL для поиска на Amazon, условия (например, состояние продукта), правила категоризации для PrestaShop и другие параметры. Этот модуль, вероятно, используется как часть системы автоматизации для обновления или создания листингов продуктов в PrestaShop на основе данных, полученных с Amazon.

## Переменные

### `scenario`

**Описание**: Словарь, содержащий конфигурации для различных сценариев продуктов.

**Как работает переменная**:
Словарь `scenario` определяет параметры для каждого продукта, включая URL для поиска на Amazon, условия продукта, правила категоризации для PrestaShop и другие настройки.

```python
scenario: dict = {
    "Apple Wathes": {
        "url": "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A2811119011%2Cn%3A2407755011%2Cn%3A7939902011%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3AApple&dc&ds=v1%3AyDxGiVC9lCk%2BzGvhkah6ZCjaellz7FcqKtRIfFA3o2A&qid=1671818889&rnid=2407755011&ref=sr_nr_n_2",
        "active": True,
        "condition": "new",
        "presta_categories": {
            "template": {"apple": "WATCHES"}
        },
        "checkbox": False,
        "price_rule": 1
    },
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

#### Ключи верхнего уровня:
- `"Apple Wathes"`: Ключ, представляющий сценарий для "Apple Watches".
- `"Murano Glass"`: Ключ, представляющий сценарий для "Murano Glass".

#### Значения для каждого сценария (например, `"Apple Wathes"`):
- `"url"` (str): URL для поиска продукта на Amazon.
- `"active"` (bool): Указывает, активен ли сценарий.
- `"condition"` (str): Условие продукта (например, `"new"`).
- `"presta_categories"` (dict): Правила категоризации для PrestaShop.
    - `"template"` (dict): Шаблон для категоризации Apple Watches, где `"apple"` соответствует `"WATCHES"`.
    - `"default_category"` (dict): Категория по умолчанию для Murano Glass, где `"11209"` соответствует `"MURANO GLASS"`.
- `"checkbox"` (bool): Указывает, использовать ли чекбокс.
- `"price_rule"` (int): Правило ценообразования.

**Примеры**:

```python
# Пример доступа к URL для Apple Watches
apple_watches_url = scenario["Apple Wathes"]["url"]
print(apple_watches_url)
# Вывод: https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A2811119011%2Cn%3A2407755011%2Cn%3A7939902011%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3AApple&dc&ds=v1%3AyDxGiVC9lCk%2BzGvhkah6ZCjaellz7FcqKtRIfFA3o2A&qid=1671818889&rnid=2407755011&ref=sr_nr_n_2

# Пример доступа к категории PrestaShop для Murano Glass
murano_glass_category = scenario["Murano Glass"]["presta_categories"]["default_category"]
print(murano_glass_category)
# Вывод: {'11209': 'MURANO GLASS'}
```