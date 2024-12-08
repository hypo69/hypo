# Локаторы полей на HTML-странице

## Обзор

Данный документ описывает формат локаторов для поиска элементов на веб-страницах, используемых для взаимодействия с веб-сайтом. Локаторы определяют способ поиска элементов на основе различных атрибутов и селекторов.

## Таблица содержания

* [Локаторы полей на HTML-странице](#локаторы-полей-на-html-странице)
* [Обзор](#обзор)
* [Пример локатора](#пример-локатора)
* [Детали](#детали)
* [Сложные локаторы](#сложные-локаторы)
    * [Пример локатора со списками](#пример-локатора-со-списками)
    * [Пример локатора со словарем](#пример-локатора-со-словаре)


## Пример локатора

```json
"close_banner": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//button[@id = 'closeXButton']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": false,
    "event": "click()",
    "locator_description": "Закрываю pop-up окно. Если оно не появилось — не страшно (`mandatory`: `false`)."
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
    "locator_description": "Внимание! В Morlevi картинка получается через screenshot и возвращается как PNG (`bytes`).}"
  }
```


## Детали

### Атрибут (`attribute`)

Атрибут, который нужно получить от веб-элемента. Например: `innerText`, `src`, `id`, `href` и т.д. Если установить значение `attribute` в `none/false`, то WebDriver вернёт весь веб-элемент (`WebElement`).

### Стратегия поиска (`by`)

Стратегия для поиска элемента:

- `ID` соответствует `By.ID`
- `NAME` соответствует `By.NAME`
- `CLASS_NAME` соответствует `By.CLASS_NAME`
- `TAG_NAME` соответствует `By.TAG_NAME`
- `LINK_TEXT` соответствует `By.LINK_TEXT`
- `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`
- `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`
- `XPATH` соответствует `By.XPATH`

### Селектор (`selector`)

Селектор, определяющий способ нахождения веб-элемента. Примеры:
`(//li[@class = 'slide selected previous'])[1]//img`,
`//a[@id = 'mainpic']//img`,
`//span[@class = 'ltr sku-copy']`.

### Обработка списков (`if_list`)

Определяет, что делать со списком найденных веб-элементов (`web_element`). Возможные значения:
- `first`: выбрать первый элемент из списка.
- `all`: выбрать все элементы.
- `last`: выбрать последний элемент.
- `even`, `odd`: выбрать чётные/нечётные элементы.
- Указание конкретных номеров, например, `1,2,...` или `[1,3,5]`: выбрать элементы с указанными номерами.

### Использование мыши (`use_mouse`)

`true` | `false`. Используется для выполнения действий с помощью мыши.

### Действия (`event`)

WebDriver может выполнить действие с веб-элементом, например, `click()`, `screenshot()`, `scroll()` и т.д.
**Важно**: Если указан `event`, он будет выполнен **до** получения значения из `attribute`.

### Обязательность (`mandatory`)

Является ли локатор обязательным. Если `mandatory: true` и взаимодействие с веб-элементом невозможно, код выбросит ошибку. Если `mandatory: false`, элемент будет пропущен.

### Описание локатора (`locator_description`)

Описание локатора.

## Сложные локаторы

В ключи локатора можно передавать списки, кортежи или словари.

### Пример локатора со списками

```json
"sample_locator": {
    "attribute": [
      null,
      "href"
    ],
    "by": [
      "XPATH",
      "XPATH"
    ],
    "selector": [
      "//a[contains(@href, '#tab-description')]",
      "//div[@id = 'tab-description']//p"
    ],
    "event": [
      "click()",
      null
    ],
    "if_list": "first",
    "use_mouse": [
      false,
      false
    ],
    "mandatory": [
      true,
      true
    ],
    "locator_description": [
      "Нажимаю на вкладку для открытия поля description.",
      "Читаю данные из div."
    ]
  }
```

### Пример локатора со словарем

```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```