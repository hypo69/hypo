# Локаторы полей на странице `HTML`

## Обзор

Данный файл содержит локаторы для различных элементов на странице HTML.  Локаторы определяют, как найти конкретное поле или элемент на странице с помощью WebDriver.  Каждый локатор представляет собой словарь, содержащий информацию о стратегии поиска, атрибуте, селекторе и дополнительных параметрах.

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
    "locator_description": "Закрыть всплывающее окно. Если оно не появляется — без проблем (`mandatory`: `false`).",
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
    "locator_description": "Получить список `ссылок` для дополнительных изображений.",
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
    "locator_description": "Код товара Morlevi.",
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
    "locator_description": "Внимание! В Morlevi изображение получается через скриншот и возвращается в формате PNG (`bytes`).",
  }
}
```

## Детали

Имя словаря соответствует имени поля в классе `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).

- **`attribute`**: Атрибут, который необходимо получить от веб-элемента. Примеры: `innerText`, `src`, `id`, `href` и т.д.  
  Если `attribute` задано как `null/false`, WebDriver вернёт весь веб-элемент (`WebElement`).

- **`by`**: Стратегия поиска элемента:
  - `ID` соответствует `By.ID`
  - `NAME` соответствует `By.NAME`
  - `CLASS_NAME` соответствует `By.CLASS_NAME`
  - `TAG_NAME` соответствует `By.TAG_NAME`
  - `LINK_TEXT` соответствует `By.LINK_TEXT`
  - `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`
  - `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`
  - `XPATH` соответствует `By.XPATH`

- **`selector`**: Селектор, определяющий способ поиска веб-элемента. Примеры:
  `(//li[@class = 'slide selected previous'])[1]//img`,
  `//a[@id = 'mainpic']//img`,
  `//span[@class = 'ltr sku-copy']`.

- **`if_list`**: Указывает, что делать со списком найденных веб-элементов (`web_element`). Возможные значения:
  - `first`: возвращает первый элемент из списка.
  - `all`: возвращает все элементы.
  - `last`: возвращает последний элемент.
  - `even`, `odd`: возвращает чётные/нечётные элементы.
  - Конкретные числа, например, `1,2,...` или `[1,3,5]`: возвращает элементы с указанными номерами.

- **`use_mouse`**: `true` | `false`
  Определяет, использовать ли мышь для взаимодействия с элементом.

- **`event`**: WebDriver может выполнить действие над веб-элементом, такое как `click()`, `screenshot()`, `scroll()` и т.д.
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
  В этом случае драйвер сначала выполнит `click()` над веб-элементом, а затем получит его атрибут `href`. Порядок: **действие -> атрибут**.

- **`timeout`**: Таймаут (в секундах) для поиска элемента. Значение `0` означает отсутствие ожидания; элемент будет найден немедленно.

- **`timeout_for_event`**: Таймаут (в секундах) для события. `"presence_of_element_located"` означает, что WebDriver будет ожидать наличия элемента перед выполнением события.

- **`mandatory`**: Является ли локатор обязательным.
  Если `{mandatory: true}` и взаимодействие с элементом невозможно, будет выброшено исключение. Если `mandatory: false`, элемент будет пропущен.

- **`locator_description`**: Описание локатора, предоставляющее дополнительный контекст о его назначении.

## Сложные локаторы

В локаторах можно передавать списки, кортежи или словари.

## Пример локатора со списками:

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
      "Чтение данных из div."
    ]
  }
```

## Ключевые описания для локаторов

1. **`attribute`**: Этот ключ указывает атрибут, который будет использоваться для извлечения данных из элемента. `null` означает, что атрибут не используется для поиска элемента.

2. **`by`**: Указывает метод поиска элемента на странице. В данном случае это `'XPATH'`, что означает использование XPath для поиска элемента.

3. **`selector`**: Строка локатора, которая будет использоваться для поиска веб-элемента. В данном случае это выражение XPath `"//a[@id = 'mainpic']//img"`, которое находит изображение внутри тега `a` с `id='mainpic'`.

4. **`if_list`**: Указывает правило обработки списка элементов. В данном случае `'first'` означает возврат первого элемента из списка.

5. **`use_mouse`**: Булево значение, указывающее, использовать ли мышь для взаимодействия с элементом.

6. **`timeout`**, **`timeout_for_event`**: Время ожидания для поиска элемента и события.

7. **`event`**: Действие, выполняемое над веб-элементом.

8. **`mandatory`**: Указывает, является ли локатор обязательным.

9. **`locator_description`**: Описание локатора.


---
Обратите внимание на возможность использования отдельных файлов локаторов для разных версий страницы (например, десктопная и мобильная).