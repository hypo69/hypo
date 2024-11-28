# Локаторы полей на HTML-странице

## Обзор

Данный файл содержит описание локаторов для различных элементов на HTML-страницах.  Локаторы определяют способ нахождения веб-элементов с помощью Selenium WebDriver.  Каждый локатор представлен в формате JSON и содержит информацию о стратегии поиска, селекторе, атрибутах и дополнительных параметрах.

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
},
```

### Детали:

#### Описание полей:

- **`attribute`**: Атрибут, который нужно получить от веб-элемента.  Например: `innerText`, `src`, `id`, `href` и т.д. Если установить значение `attribute` в `none/false`, то WebDriver вернёт весь веб-элемент (`WebElement`).
- **`by`**: Стратегия поиска элемента (соответствует `By` в Selenium).
- **`selector`**: Селектор, определяющий способ нахождения веб-элемента.
- **`if_list`**: Определяет, как обработать список найденных элементов. Возможные значения: `first`, `all`, `last`, `even`, `odd` и конкретные номера элементов.
- **`use_mouse`**: `true` | `false`.  Используется для выполнения действий с помощью мыши.
- **`event`**: WebDriver может выполнить действие с веб-элементом (например, `click()`, `screenshot()`, `scroll()`).  Важно: `event` выполняется *до* получения значения `attribute`.
- **`mandatory`**: Является ли локатор обязательным.
- **`locator_description`**: Подробное описание локатора.

#### Сложные локаторы:

Локаторы могут содержать списки, кортежи или словари для более сложных случаев поиска.  Примеры сложных локаторов приведены ниже.

#### Пример локатора со списками:

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
},
```

#### Пример локатора со словарем:

```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```

**Обратите внимание**: Приведённые примеры локаторов иллюстрируют их структуру и содержание, но могут не соответствовать реальным условиям конкретной задачи.  Нужно адаптировать локаторы к структуре и содержанию целевой HTML-страницы.