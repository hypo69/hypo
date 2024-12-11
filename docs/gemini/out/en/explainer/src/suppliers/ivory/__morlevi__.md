# Code Explanation: hypotez/src/suppliers/ivory/__morlevi__.py

## <input code>

```python
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.ivory 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'dev'
  
""" module: src.suppliers.ivory """


"""    Supplier: morlevi

@namespace src: src
 \package src.suppliers.morlevi
\file __morlevi__.py

 @section libs imports:
  - pathlib 
  - requests 
  - pandas 
  - selenium.webdriver.remote.webelement 
  - selenium.webdriver.common.keys 
  - gs 
  - gs 
  - suppliers.Product 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""


from pathlib import Path
import requests
import pandas as pd

from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.common.keys import Keys

import settings 
from src.settings import StringFormatter
json_loads = settings.json_loads
logger = settings.logger
from src.suppliers.Product import Product 


def login(supplier):
    # ... (login function code)
    
def grab_product_page(s):
    # ... (product page grabbing function code)

def list_products_in_category_from_pagination(supplier):
    # ... (pagination function code)

def get_list_products_in_category(s, scenario, presath):
    # ... (function to get product list)

def get_list_categories_from_site(s,scenario_file,brand=''):
    # ...
```

## <algorithm>

The code implements functions for interacting with the Morlevi website to gather product data.  It relies on Selenium for web automation, requests for potential API calls, and Pandas for data manipulation.

**1. Login (login):**
   - Attempts to log in to the Morlevi website.
   - Handles potential pop-up windows using `_d.page_refresh()` and `close_pop_up_locator`.
   - Uses `_login` helper function for the core login process.


**2. Product Page Scraping (grab_product_page):**
   - Creates a `Product` object to store data.
   - Closes pop-up windows (if any).
   - Extracts product details (SKU, title, description, price, etc.) using locators.
   - Uses helper functions (`set_id`, `set_sku_suppl`, `set_sku_prod`, etc.) to extract data and populate the `Product` object.
   - Stores images (if applicable).


**3. Pagination and Product Listing (list_products_in_category_from_pagination):**
   - Fetches a list of product links from a given category.
   - Iterates through the page pagination to fetch all products in a category.
   - Handles cases where the product list is a single item or a list.
   - Removes duplicates using `list(set(...))`.


**4. Product Data Gathering (get_list_products_in_category):**
   - Uses the `list_products_in_category_from_pagination` function to get products.
   - Processes the returned product list.


**5. Category Listing (get_list_categories_from_site):**
   - Retrieves a list of categories from the Morlevi website.


## <mermaid>

```mermaid
graph LR
    subgraph "Morlevi Supplier"
        A[login(supplier)] --> B{Login Success?};
        B -- Yes --> C[grab_product_page(s)];
        B -- No --> D[Handle Popup(s)];
        D --> B;
        C --> E[Product Data];
        E --> F[Store Data];
        F --> G[List Products];
        G --> H[Process Products];
        G --> I[Pagination];
        I --> H;
        H --> J[Return Product Data];
        G --> K[List Categories];
    end
    J --> L[Data Processing]; 
```

**Dependencies Analysis:**

*   `pathlib`: Used for file path manipulation.
*   `requests`: Likely for handling external API calls (though not directly used in the provided snippet).
*   `pandas`: For potentially processing or storing the gathered product data in a structured format.
*   `selenium.webdriver.remote.webelement`: For interacting with web elements using Selenium.
*   `selenium.webdriver.common.keys`: Used for keyboard interactions like pressing Enter.
*   `gs`: (Possibly) A custom library or package. Its exact purpose isn't clear without seeing more context.
*   `suppliers.Product`: Indicates a class or module in the `suppliers` package that likely defines a structure for product data.
*   `settings`: Contains variables that likely define configurations such as logger settings.
*   `src.settings`: Contains custom functions for string formatting and possibly logging.
*   `src.suppliers.Product`: Contains the class definition for `Product` objects used to store product information.


## <explanation>

**Imports:**

*   `pathlib`: Essential for working with file paths in a platform-independent way.
*   `requests`:  Potentially used for fetching data from external APIs, but not directly utilized in this file.
*   `pandas`: Used for handling data in tabular format (like DataFrames).
*   `selenium.webdriver.remote.webelement`: Necessary for controlling web elements using Selenium.
*   `selenium.webdriver.common.keys`: Allows simulating keyboard input.
*   `settings`: Provides access to global settings (e.g., logger).
*   `src.settings`: Likely contains utility functions for formatting or logging, enhancing code modularity.
*   `src.suppliers.Product`: Defines a `Product` class to represent product data, adhering to the project's modular structure.


**Classes:**

*   No classes are defined directly in this file, but the code assumes the existence of a `Product` class (imported from `src.suppliers.Product`). This class is used to encapsulate product information.


**Functions:**

*   `login(supplier)`: Attempts to log into the Morlevi website. Uses `_login` for the actual login attempt, and error handling for potential failures. Crucially, it attempts to handle popups and refreshing the page if the login fails.
*   `grab_product_page(s)`: Fetches product details from a given product page. Extract various product attributes from HTML using locators. This function clearly demonStartes the use of locators for interacting with web elements.
*   `list_products_in_category_from_pagination(supplier)`: Retrieves a list of products from a given category on the Morlevi website, handling pagination.
*   `get_list_products_in_category(s, scenario, presath)`: likely a higher-level function to orcheStarte the fetching of product lists from different scenarios or with different parameters.
*   `get_list_categories_from_site(s,scenario_file,brand='')`:  Probably fetches a list of categories from the website. This could use the same techniques as `list_products_in_category_from_pagination`.


**Variables:**

*   `MODE`: A global variable likely used for configuration (e.g., 'dev', 'prod').
*   `json_loads`, `logger`: Variables imported from the `settings` module;  likely for handling JSON data and logging, respectively. These demonStarte the use of external modules for consistent functionality across the project.


**Potential Errors/Improvements:**

*   **Error Handling:** While the code has `try...except` blocks, the error handling could be more specific.  Catching `Exception` is too general; more targeted exception handling would lead to more informative error messages.
*   **Locator Management:**  Locators are hardcoded.  Using a more organized approach to managing locators (e.g., a dedicated config file) is highly recommended to make the code more maintainable.
*   **`set_images`:** The function has commented-out code related to saving images via FTP. This suggests further functionality isn't fully implemented.
*   **Data Validation:** The code lacks validation for the data extracted.  There should be checks to ensure the data collected is in the expected format.
*   **`close_pop_up_locator` handling:** The code checks if there are multiple elements matching the locator (`str(type(close_pop_up_btn)).execute_locator("class \'list\'") >-1`). It could be improved by finding all elements matching the class and trying to click each one. It also lacks clarity on how the locator is determined.

**Relationships with other project components:**

The code interacts with `src.suppliers.Product`, `src.settings`, and `settings` modules, demonStarting a clear modular structure for handling supplier data and global configurations.  The use of `StringFormatter` within `src.settings` suggests other related functions to handle text formatting for product listings. This modular design is crucial for maintainability and scalability.

```