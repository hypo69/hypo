# Анализ кода модуля `locator.md`

**Качество кода**
9
- Плюсы
    - Документ содержит подробное описание структуры локаторов для веб-элементов.
    - Приведены примеры использования локаторов, включая сложные случаи с списками и словарями.
    - Описаны различные параметры локаторов, такие как `attribute`, `by`, `selector`, `if_list`, `use_mouse`, `event`, `timeout`, `timeout_for_event`, `mandatory` и `locator_description`.
    - Присутствуют пояснения к каждому параметру, что делает документ понятным для пользователей.
    - Описано использование mouse event и отправки сообщений через  `%EXTERNAL_MESSAGE%`
- Минусы
    - Отсутствует явное указание на использование `src.utils.jjson` для загрузки JSON, хотя это подразумевается контекстом инструкции.
    - Нет примеров как использовать `timeout`, и `timeout_for_event`, какое значение указывать. 
    - Отсутствует использование RST для оформления документации.

**Рекомендации по улучшению**

1. **Добавить**  в начало документа описание модуля в формате RST.
2. **Преобразовать** описание каждого раздела в формат RST с использованием правильной разметки (например, `:param`, `:return`, `.. code-block::`).
3. **Уточнить**  примеры использования `timeout` и `timeout_for_event`.
4. **Указать**  рекомендации по применению значений `timeout` и `timeout_for_event`.
5.  **Добавить**  информацию о том, что документ предназначен для разработчиков и как его использовать при создании локаторов.
6.  **Добавить**  информацию как использовать  `%EXTERNAL_MESSAGE%`

**Оптимизированный код**
```markdown
"""
Модуль: Описание локаторов элементов на HTML странице
=======================================================

Этот модуль содержит описание структуры и параметров локаторов, используемых для взаимодействия с элементами на HTML странице.
Локаторы определяют, как WebDriver находит и взаимодействует с элементами, такими как кнопки, поля ввода, изображения и т.д.

Описание параметров локатора
---------------------------
В данном модуле описываются параметры, которые используются для определения локаторов.
Эти параметры помогают точно определить элемент на веб-странице и выполнить с ним необходимые действия.
"""

# Field Locators on an `HTML` Page
# =====================================

### Example Locator:
# --------------------
# Пример JSON структуры локатора

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
# -------------

# :
#     Этот раздел содержит подробное описание каждого ключа в JSON структуре локатора
#     :
#         -   `dictionary_name` -  имя поля в классе `ProductFields`
#         -   :ref:`ProductFields<product_fields>` - подробнее о классе `ProductFields`

The dictionary name corresponds to the name of the field in the `ProductFields` class ([more about `ProductFields`](../product/product_fields)).

- **`attribute`**:
# :
#     Атрибут для получения значения из веб-элемента.
#
#     :param str attribute: Атрибут HTML элемента.
#     :return:  Значение атрибута или весь веб-элемент.
#
#     Если `attribute` установлен в `none/false`, WebDriver возвращает весь веб-элемент (`WebElement`).

  The attribute to get from the web element. Examples: `innerText`, `src`, `id`, `href`, etc.
  If `attribute` is set to `none/false`, the WebDriver will return the entire web element (`WebElement`).

- **`by`**:
# :
#     Стратегия поиска элемента
#
#     :param str by: Стратегия поиска элемента
#
#     Возможные значения:
#         - `ID` - By.ID
#         - `NAME` - By.NAME
#         - `CLASS_NAME` - By.CLASS_NAME
#         - `TAG_NAME` - By.TAG_NAME
#         - `LINK_TEXT` - By.LINK_TEXT
#         - `PARTIAL_LINK_TEXT` - By.PARTIAL_LINK_TEXT
#         - `CSS_SELECTOR` - By.CSS_SELECTOR
#         - `XPATH` - By.XPATH
#
  The strategy to find the element:
  - `ID` corresponds to `By.ID`
  - `NAME` corresponds to `By.NAME`
  - `CLASS_NAME` corresponds to `By.CLASS_NAME`
  - `TAG_NAME` corresponds to `By.TAG_NAME`
  - `LINK_TEXT` corresponds to `By.LINK_TEXT`
  - `PARTIAL_LINK_TEXT` corresponds to `By.PARTIAL_LINK_TEXT`
  - `CSS_SELECTOR` corresponds to `By.CSS_SELECTOR`
  - `XPATH` corresponds to `By.XPATH`

- **`selector`**:
# :
#     Селектор для поиска веб-элемента.
#
#     :param str selector: Строка селектора
#     :return:  Веб-элемент, соответствующий селектору

  The selector that determines how to find the web element. Examples:
  `(//li[@class = 'slide selected previous'])[1]//img`,
  `//a[@id = 'mainpic']//img`,
  `//span[@class = 'ltr sku-copy']`.

- **`if_list`**:
# :
#     Указывает, что делать со списком найденных веб-элементов.
#     :param str if_list: Правило обработки списка элементов.
#     :return:  элемент(ы) или список элементов в соответствии с правилом
#
#     Возможные значения:
#         -   `first`: вернуть первый элемент из списка.
#         -   `all`: вернуть все элементы.
#         -   `last`: вернуть последний элемент.
#         -   `even`, `odd`: вернуть четные/нечетные элементы.
#         -   Конкретные числа, например, `1,2,...` или `[1,3,5]`: вернуть элементы с указанными номерами.
#
#     Также, можно указать номер элемента в селекторе:
#         ``(//div[contains(@class, 'description')])[2]//p``
  Specifies what to do with a list of found web elements (`web_element`). Possible values:
  - `first`: return the first element from the list.
  - `all`: return all elements.
  - `last`: return the last element.
  - `even`, `odd`: return even/odd elements.
  - Specific numbers, e.g., `1,2,...` or `[1,3,5]`: return elements with the specified numbers.

  Alternatively, you can specify the element number directly in the selector, for example:
  `(//div[contains(@class, 'description')])[2]//p`

- **`use_mouse`**: `true` | `false`
# :
#    Указывает, использовать ли мышь для взаимодействия с элементом.
#    :param bool use_mouse:  Флаг использования мыши.
#    :return:  `true` - использовать мышь, `false` - не использовать.

  Determines whether to use the mouse to interact with the element.

- **`event`**:
# :
#     Действие, которое WebDriver выполняет над веб-элементом.
#     :param str event:  Строка с действием
#     :return:  Выполняет действие над элементом.
#
#     Например: `click()`, `screenshot()`, `scroll()`, `send_message()`
#         `event` выполняется *перед* получением значения `attribute`.
#
#     Пример:
#     ````json
#       {
#           ...,
#           "attribute": "href",
#           ...,
#           "timeout": 0,
#           "timeout_for_event": "presence_of_element_located",
#           "event": "click()",
#           ...
#       }
#     ````
#
#     В этом случае, драйвер сначала выполнит `click()` над элементом и затем получит его `href` атрибут.
#
#     Последовательность действий: **действие -> атрибут**.
#
#     Другие примеры событий:
#        - `screenshot()`: возвращает скриншот элемента.
#           Полезно, когда CDN не возвращает изображение по `URL`.
#        - `send_message()`: отправляет сообщение элементу
#            Сообщение лучше отправлять через переменную `%EXTERNAL_MESSAGE%`, как показано ниже:
#           - `{"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "click();backspace(10);%EXTERNAL_MESSAGE%"}`
#                 Эта последовательность выполнит:
#                   1.  `click()` - клик по элементу (фокусировка на поле ввода `<textbox>`).
#                   2. `backspace(10)` - перемещает каретку на 10 символов влево (очищает поле ввода).
#                   3. `%EXTERNAL_MESSAGE%` - отправляет сообщение в поле ввода.

  The WebDriver can perform an action on the web element, such as `click()`, `screenshot()`, `scroll()`, etc.
  **Important**: If `event` is specified, it will be performed **before** getting the value from `attribute`.
  Example:
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

- **`timeout`**:
# :
#     Таймаут (в секундах) для поиска элемента.
#     :param int timeout: Время ожидания элемента (в секундах)
#     :return:  Время, в течение которого WebDriver ждет появления элемента.
#
#     Значение `0` означает, что элемент должен быть найден немедленно.
#     Рекомендуемые значения от `0` до `10` секунд.

   The timeout (in seconds) for finding the element. A value of `0` means no wait; the element will be found immediately.

- **`timeout_for_event`**:
# :
#     Таймаут (в секундах) для выполнения события.
#     :param str timeout_for_event:  Таймаут для события
#     :return:  Время, в течение которого WebDriver ждет перед выполнением события.
#
#     `"presence_of_element_located"` означает, что WebDriver будет ждать появления элемента перед выполнением действия.
#      Рекомендуемые значения от `0` до `10` секунд.

   The timeout (in seconds) for the event. `"presence_of_element_located"` means the WebDriver will wait for the element to be present before performing the event.

- **`mandatory`**:
# :
#    Указывает, является ли локатор обязательным.
#    :param bool mandatory: Флаг обязательности локатора.
#    :return: `true` - локатор обязательный, `false` - локатор не обязательный.
#
#    Если `{mandatory: true}` и взаимодействие с элементом невозможно, будет выдана ошибка.
#    Если `mandatory: false`, элемент будет пропущен.

   Whether the locator is mandatory.
  If `{mandatory: true}` and interaction with the element is not possible, an error will be thrown. If `mandatory: false`, the element will be skipped.

- **`locator_description`**:
# :
#     Описание локатора.
#     :param str locator_description: Описание локатора
#     :return:  Текстовое описание локатора.

  A description of the locator.

---

### Complex Locators:
# -------------------
# :
#     Вы можете передавать списки, кортежи или словари в ключах локаторов.

You can pass lists, tuples, or dictionaries in the locator keys.

#### Example Locator with Lists:
# -----------------------------
# :
#     Пример использования списка для определения нескольких локаторов.

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
# :
#     В этом примере, сначала будет найден первый элемент `//a[contains(@href, '#tab-description')]`.
#     Затем выполнится `click()` и после получим атрибут `href` элемента.

In this example, the first element `//a[contains(@href, '#tab-description')]` will be found.
The driver will perform `click()` and then get the attribute `href` of the element `//a[contains(@href, '#tab-description')]`.

#### Example Locator with a Dictionary:
# -----------------------------------
# :
#     Пример использования словаря в качестве значения параметра `attribute`.

```json
{
"sample_locator": {
  "attribute": {"href": "name"},
  ...
  }
}
```

---

### Key Descriptions for Locators:
# --------------------------------
# :
#     Описание ключей локатора.

1.  **`attribute`**:
#  :
#     Указывает атрибут, который будет использоваться для получения данных элемента.
#     `null` означает, что атрибут не используется для поиска элемента.
   This key indicates the attribute that will be used to retrieve data from the element. `null` means the attribute is not used for finding the element.

2.  **`by`**:
#  :
#     Указывает метод для определения местоположения элемента на странице.
#     `XPATH` - поиск по XPath.
   Specifies the method for locating the element on the page. In this case, it's `'XPATH'`, which means using XPath to locate the element.

3.  **`selector`**:
#  :
#      Строка селектора, используемая для поиска веб-элемента.
#      В этом примере, XPath выражение `"//a[@id = 'mainpic']//img"` находит изображение внутри тега `a` с `id='mainpic'`.
   The locator string that will be used to find the web element. In this case, it is an XPath expression `"//a[@id = 'mainpic']//img"`, which locates an image inside an `a` tag with `id='mainpic'`.

4.  **`if_list`**:
#  :
#     Указывает правило обработки списка элементов.
#     `'first'` означает, что вернется первый элемент из списка.
   Specifies the rule for handling a list of elements. In this case, `'first'` means returning the first element from the list.

5.  **`use_mouse`**:
#  :
#      Логическое значение, определяющее использование мыши для взаимодействия с элементом.
#      `false` - мышь не используется.
   A boolean value indicating whether to use the mouse for interaction with the element. Set to `false`, meaning no mouse interaction is needed.

6.  **`timeout`**:
#   :
#     Таймаут (в секундах) для поиска элемента.
#     `0` - элемент должен быть найден немедленно.
   The timeout (in seconds) for finding the element. A value of `0` means no wait; the element will be found immediately.

7.  **`timeout_for_event`**:
#   :
#     Таймаут (в секундах) для события.
#     `"presence_of_element_located"` -  WebDriver будет ждать появления элемента перед выполнением события.
   The timeout (in seconds) for the event. `"presence_of_element_located"` means the WebDriver will wait for the element to be present before performing the event.

8.  **`event`**:
#  :
#      Действие, выполняемое над веб-элементом, например, `click()`, `screenshot()`, `scroll()`, и т.д.
#      Событие выполняется *перед* получением значения `attribute`.
   The action that will be performed on the web element, such as `click()`, `screenshot()`, `scroll()`, etc. The event will be executed before getting the value from `attribute`.

9.  **`mandatory`**:
#  :
#     Указывает, является ли локатор обязательным.
#     Если `true`, то будет вызвана ошибка, если элемент не найден.
   Indicates whether the locator is mandatory. If set to `true`, an error will be raised if the element cannot be found or interacted with.

10. **`locator_description`**:
#   :
#      Описание локатора.
    A description of the locator, providing more context about what it does.
---------------
- The page layout may vary, for example, between desktop and mobile versions. In such cases, I recommend maintaining separate locator files for each version.
  Еxample: `product.json`, `product_mobile_site.json`.
```