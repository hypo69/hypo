# Модуль `dict_scenarios.py`

## Обзор

Модуль содержит словарь `scenario`, который определяет параметры для различных сценариев, таких как "Apple Wathes" и "Murano Glass". Каждый сценарий содержит информацию о URL, активности, состоянии товара, категориях PrestaShop, правиле цены и другие параметры.
Этот файл, вероятно, используется для конфигурации и настройки автоматизированных процессов, связанных с парсингом данных с веб-сайтов (в данном случае, с Amazon) и интеграцией с PrestaShop.

## Подробней

Данный модуль предоставляет структуру данных в виде словаря, который используется для определения различных сценариев для парсинга и категоризации товаров. 
Например, для сценария "Apple Wathes" определены:

-   URL для поиска на Amazon.
-   Условие товара ("new").
-   Категории PrestaShop для определения шаблона ("apple": "WATCHES").
-   Правило цены (price\_rule: 1).

Аналогично, для сценария "Murano Glass" определены другие параметры. Этот модуль позволяет гибко настраивать параметры для каждого сценария, что упрощает процесс парсинга и категоризации товаров.

## Переменные

### `scenario`

```python
scenario: dict
```

**Описание**: Словарь, содержащий параметры для различных сценариев.

**Структура**:

```python
{
    "Название сценария": {
        "url": "URL для поиска",
        "active": True/False,
        "condition": "Состояние товара",
        "presta_categories": {
            "template": {"ключ": "значение"}
        },
        "checkbox": True/False,
        "price_rule": Целое число
    }
}
```

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