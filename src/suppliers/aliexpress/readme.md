# Aliexpress  
## Module for interactions with the supplier `aliexpress.com`

This module provides access to supplier data via the `HTTPS` (webdriver) and `API` protocols.

**webdriver**
- Direct access to the product's `html` pages via `Driver`. It allows executing data collection scripts, including navigating through categories.

**api**
- Used to obtain `affiliate links` and brief product descriptions.

## Internal Modules:
### `utils`  
Contains helper functions and utility classes for performing common operations in the AliExpress integration. It likely includes tools for data formatting, error handling, logging, and other tasks that simplify interaction with the AliExpress ecosystem.

---

### `api`  
Provides methods and classes for direct interaction with the AliExpress API. Likely includes functionality for sending requests, processing responses, and managing authentication, simplifying interaction with the API for retrieving or sending data.

---

### `campaign`  
Designed for managing marketing campaigns on AliExpress. It likely includes tools for creating, updating, and tracking campaigns, as well as methods for analyzing their effectiveness and optimizing based on provided metrics.

---

### `gui`  
Provides graphical user interface elements for interacting with AliExpress functionality. It likely includes implementations of forms, dialogs, and other visual components that allow users to more intuitively manage AliExpress operations.

---

### `locators`  
Contains definitions for locating elements on AliExpress web pages. These locators are used in conjunction with WebDriver tools to perform automated interactions, such as data collection or executing actions on the AliExpress platform.

---

### `scenarios`  
Defines complex scenarios or sequences of actions for interacting with AliExpress. It likely includes combinations of tasks (e.g., API requests, GUI interactions, and data processing) as part of larger operations, such as product synchronization, order management, or campaign execution.