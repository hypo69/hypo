# Locators for Fields on an `HTML` Page

### Example Locator:
```json
  "close_banner": {
    "attribute": null, 
    "by": "XPATH",
    "selector": "//button[@id = 'closeXButton']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": false,
    "event": "click()",
    "locator_description": "Closes the pop-up window. If it doesn't appear, it's fine (`mandatory`: `false`)."
  },
  "additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
    "event": null,
    "locator_description": "Retrieves a list of additional image `urls`."
  },
  "id_supplier": {
    "attribute": "innerText",
    "by": "XPATH",
    "selector": "//span[@class = 'ltr sku-copy']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "event": null,
    "locator_description": "SKU morlevi."
  },
  "default_image_url": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//a[@id = 'mainpic']//img",
    "if_list": "first",
    "use_mouse": false,
    "event": "screenshot()",
    "mandatory": true,
    "locator_description": "Note: in Morlevi, the image is captured via screenshot and returned as a `png` (`bytes`)."
  }
```

Where:
The dictionary key is the field name in the `ProductFields` class ([details about `ProductFields`](../product/product_fields)).

- **`attribute`**: The attribute we want to retrieve from the web element, such as `innerText`, `src`, `id`, `href`, etc. If the attribute is set to `none/false`, the webdriver will return the entire web element (`WebElement`).

- **`by`**: The strategy for locating the element:

    - `ID` corresponds to `By.ID`  
    - `NAME` corresponds to `By.NAME`  
    - `CLASS_NAME` corresponds to `By.CLASS_NAME`  
    - `TAG_NAME` corresponds to `By.TAG_NAME`  
    - `LINK_TEXT` corresponds to `By.LINK_TEXT`  
    - `PARTIAL_LINK_TEXT` corresponds to `By.PARTIAL_LINK_TEXT`  
    - `CSS_SELECTOR` corresponds to `By.CSS_SELECTOR`  
    - `XPATH` corresponds to `By.XPATH`

- **`selector`**: The selector used to locate the web element. Examples:  
  `(//li[@class = 'slide selected previous'])[1]//img`, `//a[@id = 'mainpic']//img`, `//span[@class = 'ltr sku-copy']`.

- **`if_list`**: Specifies what to do with a list of web elements retrieved. Possible values:  
  - `first`: Retrieve the first element from the list.  
  - `all`: Retrieve all web elements from the page.  
  - `last`: Retrieve the last element from the list.  
  - `even`, `odd`: Retrieve even/odd elements from the list.

- **`use_mouse`**: `true` | `false`.

- **`event`**: The webdriver can perform an action on the web element, such as `click()`, `screenshot()`, `scroll()`, etc.  
  **Note**: If an `event` is specified, it will be executed **before** retrieving the value of the `attribute`.  
  For example:  
  ```json
  {"attribute":"href",
  ....
  "event":"click()"
  }
  ```  
  In this case, the driver will first send the command to the web element and then retrieve its attribute.  
  Principle: **Action -> Attribute**.

- **`mandatory`**: Indicates whether the locator is mandatory. If {`mandatory`: `true`} and interaction with the web element fails, the code will raise an error. Otherwise, it will skip the web element.

- **`locator_description`**: A note about the locator.

### More Complex Locators:
You can pass lists, tuples, or dictionaries into the locator keys.

#### Example Locator with Lists:
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
      "Clicks on the tab to open the description field.",
      "Reads data from the `div`."
    ]
  }
```
In this example:
1. The element `//a[contains(@href, '#tab-description')]` will be located first.
2. The driver will send a `click()` command to it.
3. Then it will retrieve the `href` attribute of the element `//a[contains(@href, '#tab-description')]`.

#### Example Dictionary in a Locator:
```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```