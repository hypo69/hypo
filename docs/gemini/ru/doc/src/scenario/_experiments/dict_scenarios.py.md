# Модуль `dict_scenarios.py`

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, который определяет набор сценариев для парсинга товаров с сайта Amazon и их последующего добавления в PrestaShop. Каждый сценарий включает в себя информацию о URL, условиях, категориях PrestaShop и правилах ценообразования. Этот модуль предназначен для настройки и управления параметрами парсинга товаров.

## Подробней

Файл предназначен для хранения конфигурации сценариев в виде словаря. Ключи словаря представляют собой названия сценариев (например, "Apple Wathes", "Murano Glass"), а значения - это словари с параметрами для каждого сценария. Эти параметры включают URL страницы Amazon для парсинга, состояние товара, категории PrestaShop, необходимость использования чекбоксов и правила ценообразования. Этот файл является частью процесса автоматизации парсинга товаров и их добавления в PrestaShop.

## Переменные

### `scenario`

```python
scenario: dict
```

**Описание**: Словарь, содержащий конфигурации сценариев для парсинга товаров с Amazon и их добавления в PrestaShop.

**Структура**:
- Ключ: Название сценария (например, `"Apple Wathes"`, `"Murano Glass"`).
- Значение: Словарь с параметрами сценария, включающий:
    - `"url"`: URL страницы Amazon для парсинга.
    - `"active"`: Флаг, указывающий, активен ли сценарий.
    - `"condition"`: Состояние товара (например, `"new"`).
    - `"presta_categories"`: Словарь, определяющий категории PrestaShop для товара. Может включать:
        - `"template"`: Шаблон категорий.
        - `"default_category"`: Категория по умолчанию.
    - `"checkbox"`: Флаг, указывающий, нужно ли использовать чекбокс.
    - `"price_rule"`: Правило ценообразования.

**Примеры**:

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
В данном примере `scenario` представляет собой словарь, содержащий два сценария: "Apple Wathes" и "Murano Glass". Каждый сценарий имеет свой URL, состояние товара, категории PrestaShop и правило ценообразования.