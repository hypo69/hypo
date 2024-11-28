# Модуль locator

## Обзор

Этот модуль содержит определения локаторов для элементов на веб-странице, используемых для взаимодействия с ними через Selenium. Локаторы представлены в формате JSON и описывают различные способы поиска элементов на странице, включая атрибуты, стратегии поиска (XPath, CSS-селекторы и т.д.), обработку списков элементов, действия (клик, скриншот) и обязательность локатора.

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
    "locator_description": "Закрывает всплывающее окно. Если оно не появляется, это некритично (`mandatory`:`false`).",
  },
  "additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
    "event": null,
    "locator_description": "Получает список `URL` дополнительных изображений.",
  },
  "id_supplier": {
    "attribute": "innerText",
    "by": "XPATH",
    "selector": "//span[@class = 'ltr sku-copy']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "event": null,
    "locator_description": "SKU для Morlevi.",
  },
  "default_image_url": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//a[@id = 'mainpic']//img",
    "if_list": "first",
    "use_mouse": false,
    "event": "screenshot()",
    "mandatory": true,
    "locator_description": "Внимание! В Morlevi изображение захватывается с помощью скриншота и возвращается как PNG (`bytes`).",
  }
```


**Детали:**

- **`attribute`**: Атрибут, который нужно извлечь из веб-элемента. Примеры: `innerText`, `src`, `id`, `href` и т.д.  Если установлено в `null/false`, WebDriver вернёт весь веб-элемент (`WebElement`).

- **`by`**: Стратегия, используемая для поиска элемента:
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
  - `first`: Извлекает первый элемент из списка.
  - `all`: Извлекает все веб-элементы на странице.
  - `last`: Извлекает последний веб-элемент из списка.
  - `even`, `odd`: Извлекает чётные/нечётные элементы из списка.
  - Конкретные индексы, такие как `1,2,...` или `[1,3,5]`: Извлекает элементы из указанных строк.


- **`use_mouse`**: `true` | `false`
  Указывает, нужно ли взаимодействовать со страницей с помощью мыши.


- **`event`**: WebDriver может выполнять действия над веб-элементом, такие как `click()`, `screenshot()`, `scroll()` и т.д.
  **Важно**: Если задан `event`, он будет выполнен *перед* извлечением значения `attribute`.

- **`mandatory`**: Указывает, является ли локатор обязательным.
  Если `{mandatory: true}` и веб-элемент нельзя взаимодействовать, генерируется ошибка. В противном случае элемент пропускается.

- **`locator_description`**: Примечание к локатору.


## Сложные локаторы

Ключи в локаторах могут содержать списки/кортежи или словари.

#### Пример локатора со списками:

```json
"sample_locator": {
    "attribute": [
      null,
      "href"
    ],
    // ... (другие поля)
}
```

#### Пример локатора со словарем:

```json
"sample_locator": {
  "attribute": {"href": "name"},
  // ... (другие поля)
}
```

```