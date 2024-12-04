# Локаторы полей на странице `HTML`

## Обзор

Данный файл содержит описание локаторов для поиска элементов на веб-странице с использованием Selenium. Локаторы представлены в формате JSON и описывают способ нахождения элементов, атрибуты, которые нужно получить, действия, которые нужно выполнить (например, клик или скриншот), и другие важные параметры.

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
    "locator_description": "Закрывает всплывающее окно. Если оно не отображается, это не критическая ошибка (`mandatory`:`false`)."
  },
  "additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
    "event": null,
    "locator_description": "Получает список `URL` дополнительных изображений."
  },
  "id_supplier": {
    "attribute": "innerText",
    "by": "XPATH",
    "selector": "//span[@class = 'ltr sku-copy']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "event": null,
    "locator_description": "SKU для Morlevi."
  },
  "default_image_url": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//a[@id = 'mainpic']//img",
    "if_list": "first",
    "use_mouse": false,
    "event": "screenshot()",
    "mandatory": true,
    "locator_description": "Внимание! В Morlevi изображение захватывается через скриншот и возвращается как PNG (`bytes`). "
  }
```

## Детали

- **`attribute`**: Атрибут, который нужно получить от веб-элемента. Примеры: `innerText`, `src`, `id`, `href` и т.д. Если установлено значение `null/false`, WebDriver вернет весь веб-элемент (`WebElement`).

- **`by`**: Стратегия поиска элемента:
  - `ID` соответствует `By.ID`
  - `NAME` соответствует `By.NAME`
  - `CLASS_NAME` соответствует `By.CLASS_NAME`
  - `TAG_NAME` соответствует `By.TAG_NAME`
  - `LINK_TEXT` соответствует `By.LINK_TEXT`
  - `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`
  - `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`
  - `XPATH` соответствует `By.XPATH`

- **`selector`**: Селектор, определяющий, как найти веб-элемент. Примеры:
  `(//li[@class = 'slide selected previous'])[1]//img`,
  `//a[@id = 'mainpic']//img`,
  `//span[@class = 'ltr sku-copy']`.

- **`if_list`**: Указывает, что делать со списком найденных веб-элементов. Возможные значения:
  - `first`: Возвращает первый элемент из списка.
  - `all`: Возвращает все веб-элементы на странице.
  - `last`: Возвращает последний веб-элемент из списка.
  - `even`, `odd`: Возвращает элементы с четными/нечетными индексами.
  - Конкретные индексы, например `1,2,...` или `[1,3,5]`: Возвращает элементы из указанных строк.

- **`use_mouse`**: `true` | `false`
  Указывает, нужно ли взаимодействовать с страницей с помощью мыши.

- **`event`**: WebDriver может выполнить действия над веб-элементом, такие как `click()`, `screenshot()`, `scroll()` и т.д.
  **Важно**: Если указан `event`, он будет выполнен *перед* получением значения `attribute`.

- **`mandatory`**: Указывает, является ли локатор обязательным. Если `{mandatory: true}` и веб-элемент не может быть обработан, возникает ошибка. В противном случае элемент пропускается.

- **`locator_description`**: Комментарий к локатору.

## Сложные локаторы

Ключи в локаторе могут содержать списки/кортежи или словари.

## Пример локатора со списками

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
      "Клик по вкладке для открытия поля описания",
      "Чтение данных из div"
    ]
  }
```

## Пример локатора со словарем

```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```