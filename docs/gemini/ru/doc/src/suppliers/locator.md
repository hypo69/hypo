# Локаторы полей на странице `HTML`

## Обзор

Данный файл содержит локаторы для различных полей на веб-странице, используемые для извлечения данных.  Локаторы основаны на `XPATH` и определяют способ нахождения элементов на странице, а также действия, которые могут быть выполнены с ними.  Ключевые особенности: `attribute`, `by`, `selector`, `if_list`, `use_mouse`, `mandatory`, `timeout`, `timeout_for_event`, `event` и `locator_description`.

## Пример локатора

```json
"close_banner": {
    "attribute": null, 
    "by": "XPATH",
    "selector": "//button[@id = 'closeXButton']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": false,
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": "click()",
    "locator_description": "Закрыть всплывающее окно. Если оно не появляется — не проблема (`mandatory`: `false`).",
  },
  "additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": null,
    "locator_description": "Получить список `URL` дополнительных изображений.",
  },
  "id_supplier": {
    "attribute": "innerText",
    "by": "XPATH",
    "selector": "//span[@class = 'ltr sku-copy']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": null,
    "locator_description": "Артикул Morlevi.",
  },
  "default_image_url": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//a[@id = 'mainpic']//img",
    "if_list": "first",
    "use_mouse": false,
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": "screenshot()",
    "mandatory": true,
    "locator_description": "Внимание! В Morlevi изображение получается через скриншот и возвращается как PNG (`bytes`).",
  }
```

## Подробности

Имя словаря соответствует имени поля в классе `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).

- **`attribute`**: Атрибут, который нужно получить от веб-элемента. Примеры: `innerText`, `src`, `id`, `href` и т.д.  Если `attribute` установлено в `null/false`, WebDriver вернет весь веб-элемент (`WebElement`).

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
  `//li[@class = 'slide selected previous'][1]//img`,
  `//a[@id = 'mainpic']//img`,
  `//span[@class = 'ltr sku-copy']`.

- **`if_list`**: Указывает, что делать со списком найденных веб-элементов (`web_element`). Возможные значения:
  - `first`: вернуть первый элемент из списка.
  - `all`: вернуть все элементы.
  - `last`: вернуть последний элемент.
  - `even`, `odd`: вернуть элементы с четными/нечетными индексами.
  - Конкретные числа, например, `1,2,...` или `[1,3,5]`: вернуть элементы с указанными номерами.

- **`use_mouse`**: `true` | `false`
  Определяет, использовать ли мышь для взаимодействия с элементом.

- **`event`**: WebDriver может выполнить действие над веб-элементом, например, `click()`, `screenshot()`, `scroll()` и т.д.
  **Важно**: Если `event` указан, он будет выполнен **перед** получением значения из `attribute`.
  Пример:
  ```json
  {
      ...
      "attribute": "href",
      ...
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "click()",
      ...
  }
  ```
  В этом случае драйвер сначала выполнит `click()` над веб-элементом, а затем получит атрибут `href`. Последовательность: **действие -> атрибут**.

- **`timeout`**: Таймаут (в секундах) для поиска элемента. Значение `0` означает без ожидания; элемент будет найден немедленно.

- **`timeout_for_event`**: Таймаут (в секундах) для события. `"presence_of_element_located"` означает, что WebDriver будет ожидать появления элемента перед выполнением события.

- **`mandatory`**: Является ли локатор обязательным.
  Если `{mandatory: true}` и взаимодействие с элементом невозможно, будет выброшено исключение. Если `mandatory: false`, элемент будет пропущен.


- **`locator_description`**: Описание локатора, предоставляющее больше контекста о том, что он делает.


## Сложные локаторы

Вы можете передавать списки, кортежи или словари в ключах локатора.


## Комплексные Локаторы (с примерами)

… (здесь размещаются примеры локаторов с списками и словарями, как в исходном коде)


## Ключевые описания для локаторов


… (здесь размещаются описания ключей, как в исходном коде)



---
- Структура страницы может различаться, например, между десктопной и мобильной версиями. В таких случаях я рекомендую сохранять отдельные файлы локаторов для каждой версии.
Пример: `product.json`, `product_mobile_site.json`.