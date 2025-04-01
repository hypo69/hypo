# Модуль `dict_scenarios.py`

## Обзор

Модуль содержит словарь `scenario`, который определяет конфигурации для парсинга товаров с сайта Amazon. Каждая запись в словаре представляет собой набор параметров для определенной категории товаров, включая URL, условия, категории PrestaShop и правила ценообразования.

## Подробней

Этот модуль предназначен для хранения сценариев (наборов параметров) для автоматизации процесса сбора данных о товарах с Amazon и их последующей интеграции с платформой PrestaShop.
Сценарии включают в себя URL для поиска товаров, условия (например, состояние товара), категории для PrestaShop и правила ценообразования.

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

**Описание**:
Словарь `scenario` содержит настройки для различных категорий товаров, которые будут обрабатываться.
Ключами словаря являются названия категорий товаров (например, `"Apple Wathes"` или `"Murano Glass"`).
Значениями являются словари с параметрами для каждой категории.

**Как работает переменная**:\
Переменная scenario представляет собой словарь, содержащий сценарии для парсинга товаров с Amazon. Каждый сценарий включает следующие параметры:
*   `url`: URL страницы Amazon, с которой необходимо собирать данные.
*   `active`: Определяет, активен ли данный сценарий.
*   `condition`: Условие товара (например, "new").
*   `presta_categories`: Категории PrestaShop, к которым следует отнести товары.
*   `checkbox`: Флаг, указывающий на необходимость установки флажка (вероятно, для фильтрации товаров).
*   `price_rule`: Правило ценообразования, которое следует применять к товарам.

Пример структуры для категории "Apple Wathes":

*   `"Apple Wathes"`:
    *   `"url"`: "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A2811119011%2Cn%3A2407755011%2Cn%3A7939902011%2Cp\_n\_is\_free\_shipping%3A10236242011%2Cp\_89%3AApple&dc&ds=v1%3AyDxGiVC9lCk%2BzGvhkah6ZCjaellz7FcqKtRIfFA3o2A&qid=1671818889&rnid=2407755011&ref=sr\_nr\_n\_2"
    *   `"active"`: `True`
    *   `"condition"`: `"new"`
    *   `"presta_categories"`: `{"template": {"apple": "WATCHES"}}`
    *   `"checkbox"`: `False`
    *   `"price_rule"`: `1`