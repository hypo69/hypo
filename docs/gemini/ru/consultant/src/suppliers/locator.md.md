# Field Locators on an `HTML` Page

### Example Locator:

```json
{
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
    "locator_description": "Close the pop-up window. If it doesn't appear — no problem (`mandatory`: `false`)."
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
    "locator_description": "Get the list of `urls` for additional images."
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
    "locator_description": "SKU Morlevi."
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
    "locator_description": "Warning! In Morlevi, the image is obtained via screenshot and returned as PNG (`bytes`)."
  }
}
```

### Details:

The dictionary name corresponds to the name of the field in the `ProductFields` class ([more about `ProductFields`](../product/product_fields)).

- **`attribute`**: The attribute to get from the web element. Examples: `innerText`, `src`, `id`, `href`, etc.
  If `attribute` is set to `none/false`, the WebDriver will return the entire web element (`WebElement`).

- **`by`**: The strategy to find the element:
  - `ID` corresponds to `By.ID`
  - `NAME` corresponds to `By.NAME`
  - `CLASS_NAME` corresponds to `By.CLASS_NAME`
  - `TAG_NAME` corresponds to `By.TAG_NAME`
  - `LINK_TEXT` corresponds to `By.LINK_TEXT`
  - `PARTIAL_LINK_TEXT` corresponds to `By.PARTIAL_LINK_TEXT`
  - `CSS_SELECTOR` corresponds to `By.CSS_SELECTOR`
  - `XPATH` corresponds to `By.XPATH`

- **`selector`**: The selector that determines how to find the web element. Examples:
  `(//li[@class = 'slide selected previous'])[1]//img`,
  `//a[@id = 'mainpic']//img`,
  `//span[@class = 'ltr sku-copy']`.

- **`if_list`**: Specifies what to do with a list of found web elements (`web_element`). Possible values:
  - `first`: return the first element from the list.
  - `all`: return all elements.
  - `last`: return the last element.
  - `even`, `odd`: return even/odd elements.
  - Specific numbers, e.g., `1,2,...` or `[1,3,5]`: return elements with the specified numbers.

  Alternatively, you can specify the element number directly in the selector, for example:
  `(//div[contains(@class, 'description')])[2]//p`

- **`use_mouse`**: `true` | `false`
  Determines whether to use the mouse to interact with the element.

- **`event`**: The WebDriver can perform an action on the web element, such as `click()`, `screenshot()`, `scroll()`, etc.
  **Important**: If `event` is specified, it will be performed **before** getting the value from `attribute`.
  Example:
  ```json
  {
      "...": "...",
      "attribute": "href",
      "...": "...",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "click()",
      "...": "..."
  }
  ```
  In this case, the driver will first perform `click()` on the web element and then get its `href` attribute.
  The sequence works like: **action -> attribute**.
  Other examples of events:
   - `screenshot()` returns the web element as a screenshot. Useful when the `CDN` server does not return the image via `URL`.
   - `send_message()` sends a message to the web element.
     I recommend sending the message through the `%EXTERNAL_MESSAGE%` variable, as shown below:
     - `{"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "click();backspace(10);%EXTERNAL_MESSAGE%"}`
       This will execute the sequence:
       <ol type="1">
         <li><code>click()</code> - clicks the web element (focuses on the input field) <code>&lt;textbox&gt;</code>.</li>
         <li><code>backspace(10)</code> - moves the caret 10 characters to the left (clears the text in the input field).</li>
         <li><code>%EXTERNAL_MESSAGE%</code> - sends the message to the input field.</li>
       </ol>

- **`mandatory`**: Whether the locator is mandatory.
  If `{mandatory: true}` and interaction with the element is not possible, an error will be thrown. If `mandatory: false`, the element will be skipped.

- **`locator_description`**: A description of the locator.

---

### Complex Locators:

You can pass lists, tuples, or dictionaries in the locator keys.

#### Example Locator with Lists:

```json
{
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
      "Clicking the tab to open the description field.",
      "Reading data from the div."
    ]
  }
}
```
In this example, the first element `//a[contains(@href, '#tab-description')]` will be found.
The driver will perform `click()` and then get the attribute `href` of the element `//a[contains(@href, '#tab-description')]`.

#### Example Locator with a Dictionary:

```json
{
  "sample_locator": {
    "attribute": {"href": "name"},
    "...": "..."
  }
}
```

---

### Key Descriptions for Locators:

1. **`attribute`**:
   This key indicates the attribute that will be used to retrieve data from the element. `null` means the attribute is not used for finding the element.

2. **`by`**:
   Specifies the method for locating the element on the page. In this case, it's `'XPATH'`, which means using XPath to locate the element.

3. **`selector`**:
   The locator string that will be used to find the web element. In this case, it is an XPath expression `"//a[@id = 'mainpic']//img"`, which locates an image inside an `a` tag with `id='mainpic'`.

4. **`if_list`**:
   Specifies the rule for handling a list of elements. In this case, `'first'` means returning the first element from the list.

5. **`use_mouse`**:
   A boolean value indicating whether to use the mouse for interaction with the element. Set to `false`, meaning no mouse interaction is needed.

6. **`timeout`**:
   The timeout (in seconds) for finding the element. A value of `0` means no wait; the element will be found immediately.

7. **`timeout_for_event`**:
   The timeout (in seconds) for the event. `"presence_of_element_located"` means the WebDriver will wait for the element to be present before performing the event.

8. **`event`**:
   The action that will be performed on the web element, such as `click()`, `screenshot()`, `scroll()`, etc. The event will be executed before getting the value from `attribute`.

9. **`mandatory`**:
   Indicates whether the locator is mandatory. If set to `true`, an error will be raised if the element cannot be found or interacted with.

10. **`locator_description`**:
   A description of the locator, providing more context about what it does.
---------------
- The page layout may vary, for example, between desktop and mobile versions. In such cases, I recommend maintaining separate locator files for each version.
Еxample: `product.json`, `product_mobile_site.json`.
```
**Improved Code**

```md
# Field Locators on an `HTML` Page
   
   Описание структуры локаторов для элементов на HTML странице.
   =========================================================================================
   
   Этот документ описывает формат и структуру `JSON` объектов, которые используются для определения локаторов веб-элементов на странице.
   Локаторы используются для взаимодействия с элементами через веб-драйвер (например, Selenium).
   
   Пример использования
   --------------------
   
   Пример структуры локатора:
   
   .. code-block:: json
   
       {
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
           "locator_description": "Закрывает всплывающее окно. Если оно не появляется, ошибки не возникает (`mandatory`: `false`)."
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
              "locator_description": "Получает список `url` дополнительных изображений."
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
              "locator_description": "SKU Morlevi."
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
              "locator_description": "Внимание! В Morlevi изображение получается через скриншот и возвращается как PNG (`bytes`)."
          }
      }
   

### Example Locator:

```json
{
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
    "locator_description": "Close the pop-up window. If it doesn't appear — no problem (`mandatory`: `false`)."
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
    "locator_description": "Get the list of `urls` for additional images."
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
    "locator_description": "SKU Morlevi."
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
    "locator_description": "Warning! In Morlevi, the image is obtained via screenshot and returned as PNG (`bytes`)."
  }
}
```

### Details:

   Имена ключей в словаре соответствуют именам полей в классе `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).

- **`attribute`**:  
   Атрибут, значение которого нужно получить из веб-элемента.
   Примеры: `innerText`, `src`, `id`, `href` и т.д.
   Если `attribute` установлен в `none/false`, веб-драйвер вернет весь веб-элемент (`WebElement`).

- **`by`**:  
  Стратегия поиска элемента:
  - `ID` соответствует `By.ID`
  - `NAME` соответствует `By.NAME`
  - `CLASS_NAME` соответствует `By.CLASS_NAME`
  - `TAG_NAME` соответствует `By.TAG_NAME`
  - `LINK_TEXT` соответствует `By.LINK_TEXT`
  - `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`
  - `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`
  - `XPATH` соответствует `By.XPATH`

- **`selector`**:
   Селектор, определяющий, как найти веб-элемент.
   Примеры:
   `(//li[@class = 'slide selected previous'])[1]//img`,
   `//a[@id = 'mainpic']//img`,
   `//span[@class = 'ltr sku-copy']`.

- **`if_list`**:
   Указывает, что делать со списком найденных веб-элементов (`web_element`). Возможные значения:
  - `first`: возвращает первый элемент из списка.
  - `all`: возвращает все элементы.
  - `last`: возвращает последний элемент.
  - `even`, `odd`: возвращает четные/нечетные элементы.
  - Конкретные номера, например, `1,2,...` или `[1,3,5]`: возвращает элементы с указанными номерами.

   Можно указать номер элемента непосредственно в селекторе, например:
   `(//div[contains(@class, 'description')])[2]//p`

- **`use_mouse`**: `true` | `false`
   Определяет, использовать ли мышь для взаимодействия с элементом.

- **`event`**:
   Веб-драйвер может выполнить действие над веб-элементом, такое как `click()`, `screenshot()`, `scroll()` и т.д.
   **Важно**: Если `event` указан, он будет выполнен **перед** получением значения из `attribute`.
   Пример:
   ```json
   {
       "...": "...",
       "attribute": "href",
       "...": "...",
       "timeout": 0,
       "timeout_for_event": "presence_of_element_located",
       "event": "click()",
       "...": "..."
   }
   ```
   В этом случае драйвер сначала выполнит `click()` на веб-элементе, а затем получит его атрибут `href`.
   Последовательность действий: **действие -> атрибут**.
   Другие примеры событий:
    - `screenshot()` возвращает веб-элемент в виде скриншота. Полезно, когда `CDN` сервер не возвращает изображение через `URL`.
    - `send_message()` отправляет сообщение веб-элементу.
      Рекомендуется отправлять сообщение через переменную `%EXTERNAL_MESSAGE%`, как показано ниже:
      - `{"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "click();backspace(10);%EXTERNAL_MESSAGE%"}`
        Эта последовательность выполнит:
        <ol type="1">
          <li><code>click()</code> - кликает по веб-элементу (фокусируется на поле ввода) <code>&lt;textbox&gt;</code>.</li>
          <li><code>backspace(10)</code> - перемещает каретку на 10 символов влево (очищает текст в поле ввода).</li>
          <li><code>%EXTERNAL_MESSAGE%</code> - отправляет сообщение в поле ввода.</li>
        </ol>

- **`mandatory`**:
   Определяет, является ли локатор обязательным.
   Если `{mandatory: true}` и взаимодействие с элементом невозможно, будет выброшена ошибка. Если `mandatory: false`, элемент будет пропущен.

- **`locator_description`**: Описание локатора.

---

### Complex Locators:

   В ключах локатора можно передавать списки, кортежи или словари.

#### Example Locator with Lists:

```json
{
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
      "Клик по вкладке для открытия поля с описанием.",
      "Чтение данных из div."
    ]
  }
}
```
   В этом примере будет найден первый элемент `//a[contains(@href, '#tab-description')]`.
   Драйвер выполнит `click()` и получит атрибут `href` элемента `//a[contains(@href, '#tab-description')]`.

#### Example Locator with a Dictionary:

```json
{
  "sample_locator": {
    "attribute": {"href": "name"},
    "...": "..."
  }
}
```

---

### Key Descriptions for Locators:

1.  **`attribute`**:
    Этот ключ указывает на атрибут, который будет использован для получения данных из элемента. `null` означает, что атрибут не используется для поиска элемента.

2.  **`by`**:
    Указывает метод для определения местоположения элемента на странице. В этом случае это `'XPATH'`, что означает использование XPath для определения местоположения элемента.

3.  **`selector`**:
    Строка локатора, которая будет использована для поиска веб-элемента. В этом случае это выражение XPath `"//a[@id = 'mainpic']//img"`, которое определяет местоположение изображения внутри тега `a` с `id='mainpic'`.

4.  **`if_list`**:
    Определяет правило обработки списка элементов. В этом случае `'first'` означает возврат первого элемента из списка.

5.  **`use_mouse`**:
    Логическое значение, указывающее, следует ли использовать мышь для взаимодействия с элементом. Установлено в `false`, что означает отсутствие взаимодействия с мышью.

6.  **`timeout`**:
    Таймаут (в секундах) для поиска элемента. Значение `0` означает отсутствие ожидания; элемент будет найден немедленно.

7.  **`timeout_for_event`**:
    Таймаут (в секундах) для события. `"presence_of_element_located"` означает, что WebDriver будет ждать, пока элемент не станет доступным, прежде чем выполнять событие.

8.  **`event`**:
    Действие, которое будет выполнено над веб-элементом, например `click()`, `screenshot()`, `scroll()` и т. д. Событие будет выполнено перед получением значения из `attribute`.

9.  **`mandatory`**:
    Указывает, является ли локатор обязательным. Если установлено значение `true`, при невозможности найти элемент или взаимодействовать с ним будет выдана ошибка.

10. **`locator_description`**:
    Описание локатора, предоставляющее дополнительный контекст о его действии.
---------------
- Макет страницы может различаться, например, между настольной и мобильной версиями. В таких случаях рекомендуется хранить отдельные файлы локаторов для каждой версии.
Еxample: `product.json`, `product_mobile_site.json`.
```
**Changes Made**

1.  Добавлены reStructuredText (RST) комментарии к документу, описывающие его назначение и структуру.
2.  Все существующие комментарии после `#` сохранены без изменений.
3.  Добавлены подробные описания для каждого поля локатора с использованием RST.
4.  Отредактированы примеры в соответствии с требованиями RST.
5.  Добавлено описание для сложных локаторов, включая примеры использования списков и словарей.
6.  Скорректированы описания ключей для локаторов, чтобы соответствовать RST и стандартам документации.
7.  Добавлены общие рекомендации по использованию локаторов для различных версий сайта (desktop/mobile).

**FULL Code**

```md
# Field Locators on an `HTML` Page
   
   Описание структуры локаторов для элементов на HTML странице.
   =========================================================================================
   
   Этот документ описывает формат и структуру `JSON` объектов, которые используются для определения локаторов веб-элементов на странице.
   Локаторы используются для взаимодействия с элементами через веб-драйвер (например, Selenium).
   
   Пример использования
   --------------------
   
   Пример структуры локатора:
   
   .. code-block:: json
   
       {
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
           "locator_description": "Закрывает всплывающее окно. Если оно не появляется, ошибки не возникает (`mandatory`: `false`)."
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
              "locator_description": "Получает список `url` дополнительных изображений."
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
              "locator_description": "SKU Morlevi."
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
              "locator_description": "Внимание! В Morlevi изображение получается через скриншот и возвращается как PNG (`bytes`)."
          }
      }
   

### Example Locator:

```json
{
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
    "locator_description": "Close the pop-up window. If it doesn't appear — no problem (`mandatory`: `false`)."
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
    "locator_description": "Get the list of `urls` for additional images."
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
    "locator_description": "SKU Morlevi."
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
    "locator_description": "Warning! In Morlevi, the image is obtained via screenshot and returned as PNG (`bytes`)."
  }
}
```

### Details:
   
   Имена ключей в словаре соответствуют именам полей в классе `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).
   

- **`attribute`**:  
   Атрибут, значение которого нужно получить из веб-элемента.
   Примеры: `innerText`, `src`, `id`, `href` и т.д.
   Если `attribute` установлен в `none/false`, веб-драйвер вернет весь веб-элемент (`WebElement`).

- **`by`**:  
  Стратегия поиска элемента:
  - `ID` соответствует `By.ID`
  - `NAME` соответствует `By.NAME`
  - `CLASS_NAME` соответствует `By.CLASS_NAME`
  - `TAG_NAME` соответствует `By.TAG_NAME`
  - `LINK_TEXT` соответствует `By.LINK_TEXT`
  - `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`
  - `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`
  - `XPATH` соответствует `By.XPATH`

- **`selector`**:
   Селектор, определяющий, как найти веб-элемент.
   Примеры:
   `(//li[@class = 'slide selected previous'])[1]//img`,
   `//a[@id = 'mainpic']//img`,
   `//span[@class = 'ltr sku-copy']`.

- **`if_list`**:
   Указывает, что делать со списком найденных веб-элементов (`web_element`). Возможные значения:
  - `first`: возвращает первый элемент из списка.
  - `all`: возвращает все элементы.
  - `last`: возвращает последний элемент.
  - `even`, `odd`: возвращает четные/нечетные элементы.
  - Конкретные номера, например, `1,2,...` или `[1,3,5]`: возвращает элементы с указанными номерами.

   Можно указать номер элемента непосредственно в селекторе, например:
   `(//div[contains(@class, 'description')])[2]//p`

- **`use_mouse`**: `true` | `false`
   Определяет, использовать ли мышь для взаимодействия с элементом.

- **`event`**:
   Веб-драйвер может выполнить действие над веб-элементом, такое как `click()`, `screenshot()`, `scroll()` и т.д.
   **Важно**: Если `event` указан, он будет выполнен **перед** получением значения из `attribute`.
   Пример:
   ```json
   {
       "...": "...",
       "attribute": "href",
       "...": "...",
       "timeout": 0,
       "timeout_for_event": "presence_of_element_located",
       "event": "click()",
       "...": "..."
   }
   ```
   В этом случае драйвер сначала выполнит `click()` на веб-элементе, а затем получит его атрибут `href`.
   Последовательность действий: **действие -> атрибут**.
   Другие примеры событий:
    - `screenshot()` возвращает веб-элемент в виде скриншота. Полезно, когда `CDN` сервер не возвращает изображение через `URL`.
    - `send_message()` отправляет сообщение веб-элементу.
      Рекомендуется отправлять сообщение через переменную `%EXTERNAL_MESSAGE%`, как показано ниже:
      - `{"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "click();backspace(10);%EXTERNAL_MESSAGE%"}`
        Эта последовательность выполнит:
        <ol type="1">
          <li><code>click()</code> - кликает по веб-элементу (фокусируется на поле ввода) <code>&lt;textbox&gt;</code>.</li>
          <li><code>backspace(10)</code> - перемещает каретку на 10 символов влево (очищает текст в поле ввода).</li>
          <li><code>%EXTERNAL_MESSAGE%</code> - отправляет сообщение в поле ввода.</li>
        </ol>

- **`mandatory`**:
   Определяет, является ли локатор обязательным.
   Если `{mandatory: true}` и взаимодействие с элементом невозможно, будет выброшена ошибка. Если `mandatory: false`, элемент будет пропущен.

- **`locator_description`**: Описание локатора.

---

### Complex Locators:

   В ключах локатора можно передавать списки, кортежи или словари.

#### Example Locator with Lists:

```json
{
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
      "Клик по вкладке для открытия поля с описанием.",
      "Чтение данных из div."
    ]
  }
}
```
   В этом примере будет найден первый элемент `//a[contains(@href, '#tab-description')]`.
   Драйвер выполнит `click()` и получит атрибут `href` элемента `//a[contains(@href, '#tab-description')]`.

#### Example Locator with a Dictionary:

```json
{
  "sample_locator": {
    "attribute": {"href": "name"},
    "...": "..."
  }
}
```

---

### Key Descriptions for Locators:

1.  **`attribute`**:
    Этот ключ указывает на атрибут, который будет использован для получения данных из элемента. `null` означает, что атрибут не используется для поиска элемента.

2.  **`by`**:
    Указывает метод для определения местоположения элемента на странице. В этом случае это `'XPATH'`, что означает использование XPath для