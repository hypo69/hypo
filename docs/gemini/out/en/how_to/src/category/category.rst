rst
How to use the `hypotez/src/category/category.py` module
========================================================================================

Description
-------------------------
This module provides classes for interacting with and processing product category data, particularly for PrestaShop.  It includes methods for retrieving parent categories, asynchronously crawling categories, and building a hierarchical dictionary of categories and their relationships.  Error handling and logging are included for robustness. The module relies on external libraries like `lxml`, `requests`, and `asyncio`.  Crucially, it uses a JSON handling utility (`jjson`) to load and save hierarchical data.


Execution steps
-------------------------
1. **Import the necessary modules:** Import `Category`, `PrestaShop`, `PrestaCategory`, `asyncio`, `Path`, `os`, `requests`, `lxml`, `gs`, `logger` and other related modules.  Example: `from hypotez.src.category.category import Category`.


2. **Initialize a `Category` object:** Create an instance of the `Category` class, passing in the API credentials needed to access the PrestaShop category data. Example: `category_handler = Category(api_credentials)`.


3. **Use `get_parents` (if needed):** Retrieve parent categories for a specific category ID using the `get_parents` method. Example: `parent_categories = category_handler.get_parents(id_category, dept)`.


4. **Use `crawl_categories_async` (for asynchronous crawling):**  This method takes several parameters:
    - `url`: The URL of the category page to start the crawl from.
    - `depth`: The maximum recursion depth (how many levels of sub-categories to crawl).
    - `driver`: A Selenium WebDriver instance for interacting with the website.
    - `locator`: An XPath locator string that identifies category links on the pages.
    - `dump_file`: The path to a file where the resulting hierarchical category dictionary will be saved as JSON.
    - `id_category_default`: The default category ID.
    - `category`: (optional)  An existing category dictionary to append the crawl results to (e.g. for recursive calls).

   Example of using `crawl_categories_async`:  
   ```python
   async def main():
       category_data = await category_handler.crawl_categories_async(
           url='starting_url', depth=3, driver=webdriver_instance,
           locator='xpath_to_category_links',
           dump_file='category_data.json', id_category_default=123)
   ```

5. **Use `crawl_categories` (for synchronous crawling):** This method is similar to `crawl_categories_async` but operates synchronously without awaiting tasks.  Important note - the synchronous approach might not be suitable for extensive crawling due to blocking.
    Example of using `crawl_categories`:  
    ```python
    category_data = category_handler.crawl_categories(
        url='starting_url', depth=3, driver=webdriver_instance,
        locator='xpath_to_category_links',
        dump_file='category_data.json', id_category_default=123)
    ```


6. **Process the results:** The `crawl_categories` and `crawl_categories_async` methods return a hierarchical dictionary of categories.  This dictionary represents the structure of the categories and their relationships.  The results are saved as JSON to the specified file.


7. **Use `compare_and_print_missing_keys`:** This function helps identify missing keys in a comparison of the fetched data to data in a file (e.g., a previously-saved or expected structure).
    ```python
    compare_and_print_missing_keys(category_data, 'expected_category_data.json')
    ```


Usage example
-------------------------
```python
# Example usage (requires Selenium WebDriver setup)
from selenium import webdriver
from hypotez.src.category.category import Category
import asyncio

async def main():
    # Replace with your API credentials and other necessary variables
    api_credentials = {'username': 'your_username', 'password': 'your_password'}
    id_category_default = 123  # Example default category ID

    # Initialize Selenium WebDriver instance (choose the appropriate driver for your browser)
    driver = webdriver.Chrome()
    
    category_handler = Category(api_credentials)
    
    # Example call to crawl_categories_async. Make sure to handle any potential exceptions.
    try:
        category_data = await category_handler.crawl_categories_async(
            url='https://your-prestashop-site.com/category-page',
            depth=2, driver=driver, locator='your-xpath-locator-for-links',
            dump_file='category_data.json', id_category_default=id_category_default)
        print("Category crawling completed successfully.")

    except Exception as e:
        print(f"Error during crawling: {e}")
    finally:
      driver.quit()

asyncio.run(main())
```

**Important Considerations:**

- Replace placeholders like `'your-prestashop-site.com'`, `'your-xpath-locator-for-links'`, `'your_username'`, `'your_password'`, and `123` with your actual values.
- Ensure that you have the necessary Python libraries installed (e.g., `lxml`, `requests`, `selenium`, and `asyncio`).
- Adapt the XPath locator to match the structure of the PrestaShop website you are working with.
- Handle potential errors during the crawling process (e.g., network issues, page load failures) using `try...except` blocks.
- Configure logging appropriately for detailed error messages.


```