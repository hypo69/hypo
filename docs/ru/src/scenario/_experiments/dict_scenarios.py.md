# Модуль `dict_scenarios.py`

## Обзор

Модуль содержит словарь `scenario`, который определяет различные сценарии для обработки данных, вероятно, для автоматизации задач, связанных с веб-сайтами, такими как Amazon. Каждый сценарий включает в себя URL, условия, категории PrestaShop и правила ценообразования.

## Подробнее

Этот модуль, расположенный в `src/scenario/_experiments/dict_scenarios.py`, предоставляет структуру данных в виде словаря Python. Эта структура, вероятно, используется для конфигурации и управления процессами автоматизации, такими как сбор данных о продуктах, категоризация и определение цен. Структура данных позволяет гибко настраивать сценарии для различных продуктов и категорий.

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

**Описание**: Словарь, содержащий конфигурации сценариев для различных продуктов.

**Принцип работы**:
Словарь `scenario` содержит данные для различных сценариев, каждый из которых представляет собой определенный продукт или категорию продуктов. Каждый сценарий включает в себя следующие параметры:

-   `url`: URL-адрес страницы продукта на Amazon.
-   `active`: Указывает, активен ли сценарий.
-   `condition`: Условие продукта (например, "new").
-   `presta_categories`: Категории PrestaShop, связанные с продуктом.
-   `checkbox`: Флаг, указывающий, нужно ли использовать чекбокс.
-   `price_rule`: Правило ценообразования для продукта.

**Примеры**

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

В данном примере представлены два сценария: "Apple Wathes" и "Murano Glass".
```