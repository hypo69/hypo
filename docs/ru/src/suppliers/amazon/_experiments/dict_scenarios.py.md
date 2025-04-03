# Модуль `dict_scenarios.py`

## Обзор

Модуль содержит словарь `scenario`, который определяет настройки для парсинга товаров с Amazon. Каждый ключ в словаре представляет собой название товара (например, "Apple Wathes", "Murano Glass"), а значение - это словарь с параметрами для парсинга этого товара.

## Подробней

Этот код используется для настройки процесса сбора данных о товарах с Amazon. Словарь `scenario` позволяет задавать URL страницы Amazon, условия (например, состояние товара), категории PrestaShop, правила обработки цен и другие параметры для каждого товара.
Анализ этого файла помогает понять, как определяются настройки для каждого товара и как они используются в процессе парсинга.

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

**Описание**: Словарь, содержащий настройки для парсинга товаров с Amazon.

**Структура**:

-   `"Название товара"` (str): Ключ, представляющий название товара.
    -   `"url"` (str): URL страницы товара на Amazon.
    -   `"active"` (bool): Указывает, активен ли парсинг для данного товара.
    -   `"condition"` (str): Условие товара (например, "new").
    -   `"presta_categories"` (dict): Категории PrestaShop, в которые следует добавить товар.
        -   `"template"` (dict): Шаблон категорий (например, `{"apple": "WATCHES"}`).
        -   `"default_category"` (dict): Категории по умолчанию (например, `{"11209": "MURANO GLASS"}`).
    -   `"checkbox"` (bool): Флаг, указывающий на необходимость установки чекбокса.
    -   `"price_rule"` (int): Правило обработки цен.

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