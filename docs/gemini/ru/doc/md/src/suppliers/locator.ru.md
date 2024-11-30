# Локаторы полей на HTML-странице

## Обзор

Данный файл описывает локаторы для поиска элементов на HTML-страницах с использованием Selenium WebDriver.  Каждый локатор представлен в формате JSON и содержит необходимые параметры для поиска и взаимодействия с элементом.  Документация включает примеры сложных локаторов, использующих списки и словари.

## Локаторы

### Пример локатора:

```json
"close_banner": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//button[@id = 'closeXButton']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": false,
    "event": "click()",
    "locator_description": "Закрываю pop-up окно. Если оно не появилось — не страшно (`mandatory`: `false`).",
},
"additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
    "event": null,
    "locator_description": "Получает список `url` дополнительных изображений."
},
"id_supplier": {
    "attribute": "innerText",
    "by": "XPATH",
    "selector": "//span[@class = 'ltr sku-copy']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "event": null,
    "locator_description": "SKU Morlevi."
},
"default_image_url": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//a[@id = 'mainpic']//img",
    "if_list": "first",
    "use_mouse": false,
    "event": "screenshot()",
    "mandatory": true,
    "locator_description": "Внимание! В Morlevi картинка получается через screenshot и возвращается как PNG (`bytes`).",
}
```


### Детали:

**Ключевые параметры локаторов:**

- **`attribute`**: (str | list): Атрибут, который нужно получить. `null` означает, что возвращается весь элемент.
- **`by`**: (str | list): Стратегия поиска (XPATH, ID, NAME, CLASS_NAME, TAG_NAME, LINK_TEXT, PARTIAL_LINK_TEXT, CSS_SELECTOR).
- **`selector`**: (str | list): Селектор для поиска элемента.
- **`if_list`**: (str): Определяет, как обрабатывать список найденных элементов. Допустимые значения: `first`, `all`, `last`, `even`, `odd`, или числа/списки номеров.
- **`use_mouse`**: (bool | list):  Используется ли мышь для взаимодействия с элементом.
- **`mandatory`**: (bool | list): Обязателен ли локатор. `True` - обязателен, `False` - необязателен.
- **`event`**: (str | list):  Действие, выполняемое с элементом (например, `click()`, `screenshot()`).
- **`locator_description`**: (str | list):  Описание локатора.

**Обработка списков:**

В некоторых случаях локаторы могут содержать списки значений для параметров `attribute`, `by`, `selector`, `event`, `use_mouse`, `mandatory` и `locator_description`. Это позволяет определять несколько вариантов поиска или действий.

**Пример со списками:**

```json
"sample_locator": {
    "attribute": ["null", "href"],
    "by": ["XPATH", "XPATH"],
    "selector": ["//a[contains(@href, '#tab-description')]", "//div[@id = 'tab-description']//p"],
    "event": ["click()", null],
    "if_list": "first",
    "use_mouse": [false, false],
    "mandatory": [true, true],
    "locator_description": ["Нажимаю на вкладку для открытия поля description.", "Читаю данные из div."]
}
```


**Обработка словарей:**

В некоторых случаях значения локаторов могут быть представлены в формате словарей, например:

```json
"sample_locator_dictionary": {
  "attribute": {"href": "name"},
  ...
}
```

В этом случае каждый ключ в словаре соответствует атрибуту, а значение - тому, что нужно получить.

## Сложные локаторы

Более сложные локаторы могут использовать списки и словари.  Эти примеры демонстрируют, как обрабатывать различные варианты поиска и действий с элементом.


```