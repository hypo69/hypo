# Локаторы полей на странице `HTML`

## Обзор

Данный файл содержит локаторы для различных полей на веб-странице, используемые для автоматизации тестирования.  Локаторы определяются в формате JSON и описывают способ поиска элементов на странице, а также действия, которые нужно выполнить над ними.

## Пример Локатора:

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
    "locator_description": "Получить список `ссылок` для дополнительных изображений."
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
    "locator_description": "Код товара Morlevi."
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

## Детали:

Название словаря соответствует названию поля в классе `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).

- **`attribute`**: Атрибут, который нужно получить у веб-элемента. Примеры: `innerText`, `src`, `id`, `href` и т.д.  Если `attribute` установлено в `null/false`, WebDriver вернёт весь веб-элемент (`WebElement`).

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
  ` (//li[@class = 'slide selected previous'])[1]//img`,
  `//a[@id = 'mainpic']//img`,
  `//span[@class = 'ltr sku-copy']`.

- **`if_list`**: Указывает, что делать со списком найденных веб-элементов (`web_element`). Возможные значения:
  - `first`: вернуть первый элемент из списка.
  - `all`: вернуть все элементы.
  - `last`: вернуть последний элемент.
  - `even`, `odd`: вернуть элементы с чётными/нечётными индексами.
  - Конкретные номера, например, `1,2,...` или `[1,3,5]`: вернуть элементы с указанными номерами.

- **`use_mouse`**: `true` | `false`
  Определяет, нужно ли использовать мышь для взаимодействия с элементом.

- **`event`**: WebDriver может выполнить действие над веб-элементом, например, `click()`, `screenshot()`, `scroll()` и т.д.
  **Важно**: Если `event` указан, он будет выполнен **до** получения значения из `attribute`.
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
  Другие примеры событий:
   - `screenshot()` возвращает веб-элемент как скриншот. Полезно, когда сервер `CDN` не возвращает изображение через `URL`.
   - `send_message()` отправляет сообщение веб-элементу. Рекомендуется отправлять сообщение через переменную `%EXTERNAL_MESSAGE%`, как показано ниже:
     - `{"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "click();backspace(10);%EXTERNAL_MESSAGE%"}`
       Это выполнит последовательность:
       <ol type="1">
         <li><code>click()</code> - нажимает на веб-элемент (фокусируется на поле ввода).</li>
         <li><code>backspace(10)</code> - перемещает курсор на 10 символов влево (очищает текст в поле ввода).</li>
         <li><code>%EXTERNAL_MESSAGE%</code> - отправляет сообщение в поле ввода.</li>
       </ol>


- **`mandatory`**: Является ли локатор обязательным.
  Если `{mandatory: true}` и взаимодействие с элементом невозможно, будет выброшено исключение. Если `mandatory: false`, элемент будет пропущен.

- **`locator_description`**: Описание локатора, предоставляющее дополнительный контекст о его функции.

- **`timeout`**: Таймаут (в секундах) для поиска элемента. Значение `0` означает, что ожидание отсутствует; элемент будет найден сразу.

- **`timeout_for_event`**: Таймаут (в секундах) для события. `"presence_of_element_located"` означает, что WebDriver будет ожидать наличия элемента перед выполнением события.

## Сложные Локаторы:

В локаторах можно передавать списки, кортежи или словари.

#### Пример локатора со списками:

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
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
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
      "Нажатие на вкладку для открытия поля описания.",
      "Чтение данных из блока div."
    ]
  }
```

В этом примере будет найден первый элемент `//a[contains(@href, '#tab-description')]`.
Драйвер выполнит `click()`, а затем получит атрибут `href` элемента `//a[contains(@href, '#tab-description')]`.

#### Пример локатора со словарем:

```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```

## Ключевые описания локаторов:

Подробные описания ключевых параметров локаторов.

```
```
```
```
- Ссылки на другие файлы документации.

---
- Рекомендуется поддерживать отдельные файлы локаторов для разных версий страницы (например, десктопной и мобильной).  Пример: `product.json`, `product_mobile_site.json`.