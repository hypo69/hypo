# Модуль dict_scenarios.py

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, который определяет сценарии для парсинга товаров с сайта Amazon. Каждый сценарий включает в себя URL, условия поиска, настройки категорий PrestaShop и другие параметры.

## Подробней

Этот модуль, вероятно, используется для настройки автоматизированных процессов сбора данных о товарах с Amazon, предназначенных для последующей публикации или анализа в PrestaShop. Ключевым элементом является словарь `scenario`, который позволяет задавать различные параметры для каждого типа товара.

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

**Описание**: Словарь, содержащий сценарии для парсинга товаров с Amazon.

**Ключи словаря (название товара)**:
- `"Apple Wathes"`: Настройки для парсинга Apple Watches.
    - `"url"` (str): URL для поиска Apple Watches на Amazon.
    - `"active"` (bool): Указывает, активен ли данный сценарий.
    - `"condition"` (str): Условие товара (в данном случае "new").
    - `"presta_categories"` (dict): Настройки категорий PrestaShop. В данном случае, используется шаблон для определения категории "WATCHES" для товаров Apple.
    - `"checkbox"` (bool): Флаг для использования чекбоксов (возможно, для фильтрации).
    - `"price_rule"` (int): Правило ценообразования.

- `"Murano Glass"`: Настройки для парсинга изделий из муранского стекла.
    - `"url"` (str): URL для поиска изделий из муранского стекла на Amazon.
    - `"condition"` (str): Условие товара (в данном случае "new").
    - `"presta_categories"` (dict): Настройки категорий PrestaShop. В данном случае, категория "MURANO GLASS" с идентификатором 11209.
    - `"price_rule"` (int): Правило ценообразования.

**Как работает словарь**:

1.  **Определение товара**: Для каждого товара задается его название, которое служит ключом в словаре `scenario`.
2.  **URL**: Указывается URL для поиска товаров на Amazon. Этот URL может содержать параметры поиска, фильтры и другие настройки.
3.  **Активность**: Параметр `active` определяет, будет ли использоваться данный сценарий при парсинге.
4.  **Условие товара**: Параметр `condition` указывает на состояние товара (например, "new" для новых товаров).
5.  **Категории PrestaShop**: С помощью параметра `presta_categories` задаются категории, в которые товар будет помещен в PrestaShop. Можно использовать шаблоны или указывать конкретные идентификаторы категорий.
6.  **Правила ценообразования**: Параметр `price_rule` определяет, какие правила будут использоваться для расчета цены товара.
7.  **Checkbox**: Параметр `checkbox` определяет, используется ли фильтрация по чекбоксу для данного товара.

**Примеры**:

```python
scenario = {
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