# Модуль: src.scenario._experiments.dict_scenarios

## Обзор

Модуль `dict_scenarios.py` содержит словарь `scenario`, который определяет параметры для различных сценариев, связанных с парсингом и категоризацией товаров на платформах электронной коммерции, таких как Amazon и PrestaShop. Этот модуль используется для настройки и управления параметрами сценариев, таких как URL, условия, категории и правила ценообразования для определенных продуктов.

## Подробнее

Этот файл предоставляет структуру данных, определяющую параметры для автоматизации задач парсинга и категоризации товаров. Он содержит информацию о продуктах, таких как "Apple Wathes" и "Murano Glass", а также параметры, специфичные для каждой категории продуктов, включая URL для парсинга, условия (например, состояние продукта), категории PrestaShop и правила ценообразования. Эти параметры позволяют гибко настраивать поведение системы при обработке различных категорий продуктов.

## Переменные

### `scenario`

```python
scenario: dict
```

**Описание**: Словарь, содержащий конфигурации для различных сценариев. Ключи словаря — это названия сценариев (например, "Apple Wathes", "Murano Glass"), а значения — это словари с параметрами для каждого сценария.

**Структура словаря `scenario`**:

-   `"Apple Wathes"`:

    *   `"url"` (str): URL для парсинга товаров "Apple Wathes" на Amazon.
    *   `"active"` (bool): Указывает, активен ли данный сценарий.
    *   `"condition"` (str): Условие товара (в данном случае "new").
    *   `"presta_categories"` (dict): Конфигурация категорий для PrestaShop.

        *   `"template"` (dict): Шаблон категорий для "Apple Wathes".

            *   `"apple"` (str): Категория "WATCHES".
    *   `"checkbox"` (bool): Флаг для использования чекбоксов (в данном случае `False`).
    *   `"price_rule"` (int): Правило ценообразования (в данном случае `1`).
-   `"Murano Glass"`:

    *   `"url"` (str): URL для парсинга товаров "Murano Glass" на Amazon.
    *   `"condition"` (str): Условие товара (в данном случае "new").
    *   `"presta_categories"` (dict): Конфигурация категорий для PrestaShop.

        *   `"default_category"` (dict): Категория по умолчанию.

            *   `"11209"` (str): Категория "MURANO GLASS".
    *   `"price_rule"` (int): Правило ценообразования (в данном случае `1`).

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