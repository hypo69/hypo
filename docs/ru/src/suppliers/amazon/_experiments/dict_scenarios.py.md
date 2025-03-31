# Модуль: src.suppliers.amazon._experiments.dict_scenarios

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, который определяет различные сценарии для поиска и категоризации товаров на Amazon. Он предназначен для настройки параметров поиска и правил категоризации для последующей обработки данных о товарах.

## Подробней

Этот файл используется для хранения конфигурации поиска товаров на Amazon и их сопоставления с категориями PrestaShop.  `dict_scenarios.py`  содержит словарь `scenario`, где каждый ключ представляет собой название товара или категории (например, "Apple Wathes", "Murano Glass"), а значение - словарь с параметрами поиска и категоризации для этого товара. Этот файл позволяет гибко настраивать процесс сбора и обработки данных о товарах, определяя URL для поиска, условия (например, состояние товара) и правила категоризации.

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

**Описание**: Словарь `scenario` содержит настройки для различных сценариев поиска товаров на Amazon.

**Как работает переменная**:

-   **Ключи** словаря представляют собой названия товаров или категорий товаров (например, "Apple Wathes", "Murano Glass").
-   **Значения** - это словари, содержащие параметры для каждого сценария, такие как:
    -   `url` (str): URL для поиска товаров на Amazon.
    -   `active` (bool): Указывает, активен ли данный сценарий.
    -   `condition` (str): Условие для выбора товаров (например, "new").
    -   `presta_categories` (dict): Правила сопоставления категорий Amazon с категориями PrestaShop.
        -   `template` (dict): Шаблон для сопоставления категорий, где ключ - название бренда/товара, а значение - категория в PrestaShop.
        -   `default_category` (dict): Сопоставление ID категории в Amazon с категорией в PrestaShop.
    -   `checkbox` (bool): Флаг для использования чекбоксов (не используется в данном примере).
    -   `price_rule` (int): Правило для определения цены товара.

**Примеры**:

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