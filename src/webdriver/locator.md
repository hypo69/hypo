[Русский](https://github.com/hypo69/hypo/blob/master/src/webdriver/locator.ru.md)
## Explanation of Locators and Their Interaction with `executor`

Locators are configuration objects that describe how to find and interact with web elements on a page. They are passed to the `ExecuteLocator` class to perform various actions such as clicks, sending messages, extracting attributes, etc. Let's break down the examples of locators and their keys, as well as their interaction with `executor`.

### Examples of Locators

#### 1. `close_banner`

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
  "locator_description": "Close the pop-up window, if it does not appear - it's okay (`mandatory`:`false`)"
}
```

**Purpose of the Locator**: Close the banner (pop-up window) if it appears on the page.

**Keys**:
- `attribute`: Not used in this case.
- `by`: Locator type (`XPATH`).
- `selector`: Expression to find the element (`//button[@id = 'closeXButton']`).
- `if_list`: If multiple elements are found, use the first one (`first`).
- `use_mouse`: Do not use the mouse (`false`).
- `mandatory`: Optional action (`false`).
- `timeout`: Timeout for finding the element (`0`).
- `timeout_for_event`: Wait condition (`presence_of_element_located`).
- `event`: Event to execute (`click()`).
- `locator_description`: Description of the locator.

**Interaction with `executor`**:
- `executor` will find the element by XPATH and perform a click on it.
- If the element is not found, `executor` will continue execution since the action is not mandatory (`mandatory: false`).

#### 2. `id_manufacturer`

```json
"id_manufacturer": {
  "attribute": 11290,
  "by": "VALUE",
  "selector": null,
  "if_list": "first",
  "use_mouse": false,
  "mandatory": true,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": null,
  "locator_description": "id_manufacturer"
}
```

**Purpose of the Locator**: Return the value set in `attribute`.

**Keys**:
- `attribute`: Attribute value (`11290`).
- `by`: Locator type (`VALUE`).
- `selector`: Not used in this case.
- `if_list`: If multiple elements are found, use the first one (`first`).
- `use_mouse`: Do not use the mouse (`false`).
- `mandatory`: Mandatory action (`true`).
- `timeout`: Timeout for finding the element (`0`).
- `timeout_for_event`: Wait condition (`presence_of_element_located`).
- `event`: No event (`null`).
- `locator_description`: Description of the locator.

**Interaction with `executor`**:
- `executor` will return the value set in `attribute` (`11290`).
- Since `by` is set to `VALUE`, `executor` will not search for the element on the page.

#### 3. `additional_images_urls`

```json
"additional_images_urls": {
  "attribute": "src",
  "by": "XPATH",
  "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
  "if_list": "first",
  "use_mouse": false,
  "mandatory": false,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": null
}
```

**Purpose of the Locator**: Extract URLs of additional images.

**Keys**:
- `attribute`: Attribute to extract (`src`).
- `by`: Locator type (`XPATH`).
- `selector`: Expression to find elements (`//ol[contains(@class, 'flex-control-thumbs')]//img`).
- `if_list`: If multiple elements are found, use the first one (`first`).
- `use_mouse`: Do not use the mouse (`false`).
- `mandatory`: Optional action (`false`).
- `timeout`: Timeout for finding the element (`0`).
- `timeout_for_event`: Wait condition (`presence_of_element_located`).
- `event`: No event (`null`).

**Interaction with `executor`**:
- `executor` will find elements by XPATH and extract the `src` attribute value for each element.
- If elements are not found, `executor` will continue execution since the action is not mandatory (`mandatory: false`).

#### 4. `default_image_url`

```json
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
  "locator_description": "Attention! In Morlevi, the image is obtained via screenshot and returned as png (`bytes`)"
}
```

**Purpose of the Locator**: Take a screenshot of the default image.

**Keys**:
- `attribute`: Not used in this case.
- `by`: Locator type (`XPATH`).
- `selector`: Expression to find the element (`//a[@id = 'mainpic']//img`).
- `if_list`: If multiple elements are found, use the first one (`first`).
- `use_mouse`: Do not use the mouse (`false`).
- `timeout`: Timeout for finding the element (`0`).
- `timeout_for_event`: Wait condition (`presence_of_element_located`).
- `event`: Event to execute (`screenshot()`).
- `mandatory`: Mandatory action (`true`).
- `locator_description`: Description of the locator.

**Interaction with `executor`**:
- `executor` will find the element by XPATH and take a screenshot of the element.
- If the element is not found, `executor` will raise an error since the action is mandatory (`mandatory: true`).

#### 5. `id_supplier`

```json
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
  "locator_description": "SKU morlevi"
}
```

**Purpose of the Locator**: Extract the text inside the element containing the SKU.

**Keys**:
- `attribute`: Attribute to extract (`innerText`).
- `by`: Locator type (`XPATH`).
- `selector`: Expression to find the element (`//span[@class = 'ltr sku-copy']`).
- `if_list`: If multiple elements are found, use the first one (`first`).
- `use_mouse`: Do not use the mouse (`false`).
- `mandatory`: Mandatory action (`true`).
- `timeout`: Timeout for finding the element (`0`).
- `timeout_for_event`: Wait condition (`presence_of_element_located`).
- `event`: No event (`null`).
- `locator_description`: Description of the locator.

**Interaction with `executor`**:
- `executor` will find the element by XPATH and extract the text inside the element (`innerText`).
- If the element is not found, `executor` will raise an error since the action is mandatory (`mandatory: true`).

### Interaction with `executor`

`executor` uses locators to perform various actions on the web page. The main steps of interaction are:

1. **Parsing the Locator**: Converts the locator to a `SimpleNamespace` object if necessary.
2. **Finding the Element**: Uses the locator type (`by`) and selector (`selector`) to find the element on the page.
3. **Executing the Event**: If the `event` key is specified, performs the corresponding action (e.g., click, screenshot).
4. **Extracting the Attribute**: If the `attribute` key is specified, extracts the attribute value from the found element.
5. **Error Handling**: If the element is not found and the action is not mandatory (`mandatory: false`), continues execution. If the action is mandatory, raises an error.

Thus, locators provide a flexible and powerful tool for automating interaction with web elements, and `executor` ensures their execution considering all parameters and conditions.