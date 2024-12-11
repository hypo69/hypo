# Locator Documentation

## Overview

This module defines locators for various elements on an HTML page.  Each locator is represented as a JSON object, specifying the method to locate an element, the attribute to retrieve, any actions to perform, and other details.  The locators are used to automate interactions with web pages.

## Table of Contents

* [Locators](#locators)
    * [Example Locator](#example-locator)
    * [Details](#details)
    * [Complex Locators](#complex-locators)
        * [Example of a Locator with Lists](#example-of-a-locator-with-lists)
        * [Example of a Locator with a Dictionary](#example-of-a-locator-with-a-dictionary)

## Locators

### Example Locator

```json
  "close_banner": {
    "attribute": null, 
    "by": "XPATH",
    "selector": "//button[@id = 'closeXButton']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": false,
    "event": "click()",
    "locator_description": "Closes the pop-up window. If it doesn’t appear, it’s not critical (`mandatory`:`false`).",
  },
  "additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
    "event": null,
    "locator_description": "Retrieves a list of `URL`s for additional images.",
  },
  "id_supplier": {
    "attribute": "innerText",
    "by": "XPATH",
    "selector": "//span[@class = 'ltr sku-copy']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "event": null,
    "locator_description": "SKU for Morlevi.",
  },
  "default_image_url": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//a[@id = 'mainpic']//img",
    "if_list": "first",
    "use_mouse": false,
    "event": "screenshot()",
    "mandatory": true,
    "locator_description": "Attention! In Morlevi, the image is captured via a screenshot and returned as a PNG (`bytes`).",
  }
```

### Details

This section describes the structure and content of each locator JSON object.

* **`attribute`**: (Optional, can be `null`) The attribute to retrieve from the located element. Examples: `innerText`, `src`, `id`, `href`, etc. If `null` or `false`, the WebDriver will return the entire web element (`WebElement`).

* **`by`**: (Required) The method used to locate the element: 
    - `ID`, `NAME`, `CLASS_NAME`, `TAG_NAME`, `LINK_TEXT`, `PARTIAL_LINK_TEXT`, `CSS_SELECTOR`, `XPATH`.

* **`selector`**: (Required) The selector string used to identify the element based on the `by` method.  Correct XPath syntax is critical.

* **`if_list`**: (Required) Specifies the handling of multiple found elements. Possible values: `first`, `all`, `last`, `even`, `odd`, or an explicit index or list of indices.

* **`use_mouse`**: (Required, Boolean) Indicates whether to interact with the element using the mouse.

* **`event`**: (Optional, can be `null`)  The action to perform on the element before retrieving the attribute, e.g., `click()`, `screenshot()`, `scroll()`.  The action is executed *before* retrieving the `attribute`.

* **`mandatory`**: (Required, Boolean) Indicates if the locator is mandatory for the test. If `true` and the element cannot be located, an error will be raised.  If `false`, the element is skipped.

* **`locator_description`**: (Optional) A descriptive note about the locator's purpose.


### Complex Locators

#### Example of a Locator with Lists

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
      "Clicking the tab to open the description field",
      "Reading data from the div"
    ]
  }
```

#### Example of a Locator with a Dictionary

```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```


This demonStartes nested structure within the `attribute` key, allowing more complex retrieval logic to be defined.