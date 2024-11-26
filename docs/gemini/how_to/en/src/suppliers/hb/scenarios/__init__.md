Usage Guide for hypotez/src/suppliers/hb/scenarios/__init__.py

This file initializes the HB (hb.co.il) product supplier module for the Hypotez project.  It defines important variables and imports functions for interacting with the HB website.

**Key Variables:**

* **MODE = 'dev'**: This variable likely controls the execution mode (e.g., development, production).  The value 'dev' suggests a development environment.  Changing this variable would affect how the supplier interacts with the HB website.

**Functions:**

* **`from .version import __version__, __doc__, __details__`**: Imports version information, documentation, and other details for the supplier.  This is useful for tracking updates and managing different versions of the supplier.  It's good practice to call these to check for updates or release versions.

* **`from .categories import get_list_products_in_category, get_list_categories_from_site`**:
    * **`get_list_products_in_category(...)`**: Retrieves a list of products within a specified category.  You'll likely need to provide the category ID or name as input.
    * **`get_list_categories_from_site(...)`**: Retrieves a list of all available categories from the HB website. This is a useful starting point for scraping product listings across the site.

* **`from .grabber import grab_product_page`**:
    * **`grab_product_page(...)`**: Retrieves the HTML source code of a specific product page. This is a crucial function for extracting product details (name, price, description, etc.).  You'll need to supply the URL of the product page to this function.

* **`from .login import login`**:
    * **`login(...)`**: Handles the login process for the HB website.  This function is crucial if accessing product information requires authentication (e.g., API access).  It is likely that the inputs needed for login are username, password and potentially other authentication data.

**How to Use:**

1. **Import necessary functions:**

   ```python
   from hypotez.src.suppliers.hb.scenarios import (
       get_list_products_in_category,
       get_list_categories_from_site,
       grab_product_page,
       login
   )
   ```

2. **Initialize and authenticate (if required):**

   ```python
   login(...) # Call login function with appropriate parameters
   ```

3. **Fetch product lists and data:**

   ```python
   category_id = 123 # Example category ID
   product_list = get_list_products_in_category(category_id)
   for product in product_list:
       product_page_url = product['url'] # Example assuming product contains a url
       product_page_html = grab_product_page(product_page_url)

       # Process the product_page_html to extract product details
       # ... (e.g., using Beautiful Soup or similar libraries)
   ```

**Important Considerations:**

* **Error Handling:**  Implement robust error handling (e.g., `try...except` blocks) within your code to manage potential issues like network problems, invalid inputs, or authentication failures. The provided code lacks error handling, which is critical for production code.

* **Rate Limiting:**  Be mindful of the HB website's rate limits. Avoid making too many requests in a short period to prevent your IP address from being blocked.  Implement delays between requests.

* **Data Validation:**  Validate the data extracted from the website to ensure its accuracy and integrity. This helps to catch any issues early and prevents errors down the line.

* **Dependencies:** Ensure all required libraries (e.g., `packaging`, `requests`, `BeautifulSoup`) are installed in your environment.


This guide provides a starting point.  Detailed implementations within the functions `.categories`, `.grabber` and `.login` are needed for a complete understanding.  Understanding the structure of the HTML and the expected output format of each function is essential for effective use.