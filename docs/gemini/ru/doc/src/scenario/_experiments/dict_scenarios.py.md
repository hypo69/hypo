# Модуль `dict_scenarios`

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, который определяет конфигурации для различных сценариев парсинга продуктов с сайта Amazon. Каждый сценарий включает параметры, такие как URL, условия, категории PrestaShop и правила ценообразования.

## Подробней

Этот модуль предоставляет структуру данных, которая используется для настройки и управления сценариями для автоматизированного парсинга и категоризации продуктов. Он особенно полезен для интеграции с PrestaShop, позволяя автоматизировать процесс добавления и обновления товаров.
Словарь `scenario` предназначен для хранения информации о различных продуктах или категориях продуктов, которые необходимо обработать. Ключи словаря представляют собой названия сценариев (например, "Apple Wathes", "Murano Glass"), а значения — это словари с детальной конфигурацией для каждого сценария.

## Переменные

### `scenario`

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

**Описание**: Словарь, содержащий сценарии для парсинга продуктов.

**Как работает переменная**:
Словарь `scenario` содержит конфигурации для парсинга продуктов с Amazon и их категоризации в PrestaShop. Каждый ключ в словаре представляет собой название продукта или категории, а значение — это словарь с параметрами парсинга и категоризации.

**Параметры**:

-   `"Apple Wathes"`:
    -   `"url"` (str): URL для парсинга товаров "Apple Watches" на Amazon.
    -   `"active"` (bool): Указывает, активен ли данный сценарий (в данном случае `True`).
    -   `"condition"` (str): Условие для выбора товаров (в данном случае `"new"`).
    -   `"presta_categories"` (dict): Категории PrestaShop, в которые нужно добавить товары. Используется шаблон `"apple": "WATCHES"`.
    -   `"checkbox"` (bool): Указывает, использовать ли чекбокс (в данном случае `False`).
    -   `"price_rule"` (int): Правило ценообразования (в данном случае `1`).
-   `"Murano Glass"`:
    -   `"url"` (str): URL для парсинга товаров "Murano Glass" на Amazon.
    -   `"condition"` (str): Условие для выбора товаров (в данном случае `"new"`).
    -   `"presta_categories"` (dict): Категории PrestaShop, в которые нужно добавить товары. Используется категория по умолчанию `{"11209":"MURANO GLASS"}`.
    -   `"price_rule"` (int): Правило ценообразования (в данном случае `1`).

**Примеры**:

Пример структуры словаря `scenario` для двух категорий товаров: "Apple Wathes" и "Murano Glass".

```python
scenario = {
    "Apple Wathes": {
        "url": "https://www.amazon.com/...",
        "active": True,
        "condition": "new",
        "presta_categories": {
            "template": {"apple": "WATCHES"}
        },
        "checkbox": False,
        "price_rule": 1
    },
    "Murano Glass": {
        "url": "https://www.amazon.com/...",
        "condition": "new",
        "presta_categories": {
            "default_category":{"11209":"MURANO GLASS"}
        },
        "price_rule": 1
    }
}
```