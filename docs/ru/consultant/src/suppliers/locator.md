# Анализ кода модуля `locator.md`

## Качество кода:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Документ подробно описывает структуру локаторов и их применение.
    - Присутствуют примеры использования различных типов локаторов, включая списки и словари.
    - Описаны основные атрибуты локаторов и их предназначение.
    - Добавлены новые параметры `timeout` и `timeout_for_event`.
- **Минусы**:
    - Отсутствует форматирование кода в соответствии со стандартами Python (использование двойных кавычек вместо одинарных в коде).
    - Нет явного указания на использование `j_loads` или `j_loads_ns` для загрузки JSON (хотя подразумевается, что это JSON).
    - Не хватает примеров использования `logger` для обработки ошибок.
    - Некоторые формулировки описаний могут быть улучшены для большей ясности.

## Рекомендации по улучшению:

- Переформатировать все примеры JSON в документе, используя одинарные кавычки (`'`) для значений, чтобы соответствовать Python-стандартам.
- Явно указать, что данные из файла локаторов загружаются с использованием `j_loads` или `j_loads_ns` из `src.utils.jjson`.
- Добавить примеры использования `logger.error` для обработки ошибок, возникающих при взаимодействии с элементами, которые являются `mandatory = True`.
- Уточнить описания некоторых параметров, чтобы сделать их более понятными. Например, для `attribute` пояснить, что он может быть `None`.
- Разместить примеры кодов в отдельные блоки кода с указанием языка.
- Привести примеры как можно более похожими на реальный код.

## Оптимизированный код:

```
# Field Locators on an `HTML` Page

### Example Locator:

```json
{
  'close_banner': {
    'attribute': None,
    'by': 'XPATH',
    'selector': '//button[@id = \'closeXButton\']',
    'if_list': 'first',
    'use_mouse': False,
    'mandatory': False,
    'timeout': 0,
    'timeout_for_event': 'presence_of_element_located',
    'event': 'click()',
    'locator_description': 'Close the pop-up window. If it doesn\'t appear — no problem (`mandatory`: `false`).'
  },
  'additional_images_urls': {
    'attribute': 'src',
    'by': 'XPATH',
    'selector': '//ol[contains(@class, \'flex-control-thumbs\')]//img',
    'if_list': 'all',
    'use_mouse': False,
    'mandatory': False,
    'timeout': 0,
    'timeout_for_event': 'presence_of_element_located',
    'event': None,
    'locator_description': 'Get the list of `urls` for additional images.'
  },
  'id_supplier': {
    'attribute': 'innerText',
    'by': 'XPATH',
    'selector': '//span[@class = \'ltr sku-copy\']',
    'if_list': 'first',
    'use_mouse': False,
    'mandatory': True,
    'timeout': 0,
    'timeout_for_event': 'presence_of_element_located',
    'event': None,
    'locator_description': 'SKU Morlevi.'
  },
  'default_image_url': {
    'attribute': None,
    'by': 'XPATH',
    'selector': '//a[@id = \'mainpic\']//img',
    'if_list': 'first',
    'use_mouse': False,
    'timeout': 0,
    'timeout_for_event': 'presence_of_element_located',
    'event': 'screenshot()',
    'mandatory': True,
    'locator_description': 'Warning! In Morlevi, the image is obtained via screenshot and returned as PNG (`bytes`).'
    }
}
```

### Details:

The dictionary name corresponds to the name of the field in the `ProductFields` class ([more about `ProductFields`](../product/product_fields)).

- **`attribute`**: The attribute to get from the web element. Examples: `innerText`, `src`, `id`, `href`, etc.  
  If `attribute` is set to `None`, the WebDriver will return the entire web element (`WebElement`).

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

- **`use_mouse`**: `True` | `False`  
  Determines whether to use the mouse to interact with the element.

- **`event`**: The WebDriver can perform an action on the web element, such as `click()`, `screenshot()`, `scroll()`, etc.  
  **Important**: If `event` is specified, it will be performed **before** getting the value from `attribute`.  
  Example:  
    ```json
    {
      '...',
      'attribute': 'href',
      '...',
      'timeout': 0,
      'timeout_for_event': 'presence_of_element_located',
      'event': 'click()',
      '...'
    }
    ```
  In this case, the driver will first perform `click()` on the web element and then get its `href` attribute.  
  The sequence works like: **action -> attribute**.  
  Other examples of events:
   - `screenshot()` returns the web element as a screenshot. Useful when the `CDN` server does not return the image via `URL`.
   - `send_message()` sends a message to the web element.  
     I recommend sending the message through the `%EXTERNAL_MESSAGE%` variable, as shown below:  
     - `{'timeout': 0, 'timeout_for_event': 'presence_of_element_located', 'event': 'click();backspace(10);%EXTERNAL_MESSAGE%'}`  
       This will execute the sequence:  
       <ol type="1">
         <li><code>click()</code> - clicks the web element (focuses on the input field) <code>&lt;textbox&gt;</code>.</li>
         <li><code>backspace(10)</code> - moves the caret 10 characters to the left (clears the text in the input field).</li>
         <li><code>%EXTERNAL_MESSAGE%</code> - sends the message to the input field.</li>
       </ol>

- **`mandatory`**: Whether the locator is mandatory.  
  If `{mandatory: True}` and interaction with the element is not possible, an error will be thrown via logger.error. If `mandatory: False`, the element will be skipped.

- **`locator_description`**: A description of the locator.

---

### Complex Locators:

You can pass lists, tuples, or dictionaries in the locator keys.

#### Example Locator with Lists:

```json
{
  'sample_locator': {
    'attribute': [
      None,
      'href'
    ],
    'by': [
      'XPATH',
      'XPATH'
    ],
    'selector': [
      '//a[contains(@href, \'#tab-description\')]',
      '//div[@id = \'tab-description\']//p'
    ],
    'timeout': 0,
    'timeout_for_event': 'presence_of_element_located',
    'event': [
      'click()',
      None
    ],
    'if_list': 'first',
    'use_mouse': [
      False,
      False
    ],
    'mandatory': [
      True,
      True
    ],
    'locator_description': [
      'Clicking the tab to open the description field.',
      'Reading data from the div.'
    ]
  }
}
```
In this example, the first element `//a[contains(@href, '#tab-description')]` will be found.  
The driver will perform `click()` and then get the attribute `href` of the element `//a[contains(@href, '#tab-description')]`.

#### Example Locator with a Dictionary:

```json
{
  'sample_locator': {
    'attribute': {'href': 'name'},
     '...'
  }
}
```

---

### Key Descriptions for Locators:

1. **`attribute`**:  
   This key indicates the attribute that will be used to retrieve data from the element. `None` means the attribute is not used for finding the element.

2. **`by`**:  
   Specifies the method for locating the element on the page. In this case, it's `'XPATH'`, which means using XPath to locate the element.

3. **`selector`**:  
   The locator string that will be used to find the web element. In this case, it is an XPath expression `"//a[@id = 'mainpic']//img"`, which locates an image inside an `a` tag with `id='mainpic'`.

4. **`if_list`**:  
   Specifies the rule for handling a list of elements. In this case, `'first'` means returning the first element from the list.

5. **`use_mouse`**:  
   A boolean value indicating whether to use the mouse for interaction with the element. Set to `False`, meaning no mouse interaction is needed.

6. **`timeout`**:  
   The timeout (in seconds) for finding the element. A value of `0` means no wait; the element will be found immediately.

7. **`timeout_for_event`**:  
   The timeout (in seconds) for the event. `"presence_of_element_located"` means the WebDriver will wait for the element to be present before performing the event.

8. **`event`**:  
   The action that will be performed on the web element, such as `click()`, `screenshot()`, `scroll()`, etc. The event will be executed before getting the value from `attribute`.

9. **`mandatory`**:  
   Indicates whether the locator is mandatory. If set to `True`, an error will be raised if the element cannot be found or interacted with.

10. **`locator_description`**:  
   A description of the locator, providing more context about what it does.
---------------
- The page layout may vary, for example, between desktop and mobile versions. In such cases, I recommend maintaining separate locator files for each version.  
Еxample: `product.json`, `product_mobile_site.json`.