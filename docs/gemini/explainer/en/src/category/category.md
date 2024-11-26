## hypotez/src/category/category.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.category \n\t:platform: Windows, Unix\n\t:synopsis: Модуль работы с категориями \nНа сегодняшний день модуль заточен в основном под Престашоп\n\n"""\nMODE = \'dev\'\n\nfrom pathlib import Path\nimport os\nimport asyncio\nfrom typing import List, Dict\nfrom lxml import html\nimport requests\n\nimport header\nfrom src import gs\nfrom src.logger import logger \nfrom src.utils import j_loads, j_dumps, pprint\nfrom src.utils.string import StringFormatter\nfrom src.endpoints.prestashop import PrestaShop\nfrom src.endpoints.prestashop import PrestaCategory \n\n\nclass Category(PrestaCategory):\n    """ Класс категорий товара. Наследует `PrestaCategory` """\n\n    credentials: dict = None\n\n    def __init__(self, api_credentials, *args, **kwards):\n        super().__init__(api_credentials, *args, **kwards)\n\n    def get_parents(self, id_category, dept):\n        """ Получение родительских категорий """\n        return super().get_list_parent_categories(id_category)\n\n    async def crawl_categories_async(self, url, depth, driver, locator, dump_file, id_category_default, category: dict = None):\n        """ Асинхронная рекурсивная функция для обхода категорий и построения иерархического словаря.\n        ... (docstring continues)\n        """\n        if category is None:\n            category = {\'url\': url,\n                        \'name\': \'\',\n                        "presta_categories": {\n                            "default_category": id_category_default,\n                            "additional_categories": []\n                        },\n                        \'children\': {}}\n\n        if depth <= 0:\n            return category\n\n        driver.get(url)\n        driver.wait(1)\n        category_links = driver.execute_locator(locator)\n        if not category_links:\n            logger.error(f"Что-то упало")\n            ...\n            return category\n\n        tasks = []\n        for link in category_links:\n            for name, link_url in link.items():\n                if check_duplicate_url(category, link_url):\n                    continue\n                new_category = {\'url\': link_url,\n                                \'name\': name,\n                                "presta_categories": {\n                                    "default_category": id_category_default,\n                                    "additional_categories": []\n                                },\n                                \'children\': {}}\n                task = self.crawl_categories_async(url=link_url,\n                                                   depth=depth - 1,\n                                                   driver=driver,\n                                                   locator=locator,\n                                                   dump_file=dump_file,\n                                                   id_category_default=id_category_default,\n                                                   category=new_category)\n                tasks.append(task)\n\n        await asyncio.gather(*tasks)\n\n        return category\n\n    def crawl_categories(self, url, depth: int, driver, locator: dict, dump_file: Path, id_category_default, category: dict = {}):\n        """ Рекурсивная функция для обхода категорий с сайта и построения иерархического словаря.\n        ... (docstring continues)\n        """\n        # ... (code as before) \n```

```<algorithm>
**Overall Workflow (High-Level):**

1.  **Initialization:** The `Category` class is initialized.  It likely retrieves credentials from a configuration file or environment variables.
2.  **Crawling (Async):** `crawl_categories_async` is called.  This function recursively traverses category pages using Selenium (driver) to collect links to child categories.
3.  **Data Storage:** Collected categories, represented as a hierarchical dictionary, are built and stored to `dump_file`.  It uses `j_dumps` and `j_loads`.
4.  **Crawling (Sync):** `crawl_categories` is a synchronous recursive function with a similar goal as the async function.
5. **Data Validation:** `check_duplicate_url` function is used to prevent redundancy in the output dictionary.
6. **Comparison & Reporting:** `compare_and_print_new_keys` compares the data in `dump_file` with the newly crawled categories to identify missing keys.


**Step-by-Step Block Diagram (crawl_categories_async):**

```
+-----------------+      +-----------------+      +-----------------+
| Input: url, depth |----->| Get Page (driver)|----->| Parse Links (driver)|
+-----------------+      +-----------------+      +-----------------+
       |                               |       |   (e.g., xpath)  |
       V                               V       V
     +----------------------+           +-----------------+
     | Create New Category  |-----------|Check Duplicate URL|
     +----------------------+           +-----------------+
            |                   |           |  (Returns bool)   |
            V                   V           V
     +-----------------+     +-----------+   +-----------------+
     | Recurse Async  |----->| Yes/No    |---|New Category    |
     +-----------------+     +-----------+   +-----------------+
            |                               |            |
            V   (if depth > 0)             |           V
     +-----------------+      +-----------------+
     | Collect Children|----->| Store to Category|
     +-----------------+      +-----------------+
             |                   ^
             |                   |
             V                   |
        +-----------------+   +-----------------+
        | Async Gather     |---| Return Category |
        +-----------------+   +-----------------+
           |            |
           V  ...
```
```


**Step-by-Step Block Diagram (crawl_categories):**


```
+-----------------+      +-----------------+
| Input: url, depth |----->| Get Page (driver)|
+-----------------+      +-----------------+
       |                               |
       V                               V
     +----------------------+           +-----------------+
     | Create New Category  |-----------|Check Duplicate URL|
     +----------------------+           +-----------------+
            |                   |           |  (Returns bool)   |
            V                   V           V
     +-----------------+     +-----------+   +-----------------+
     | Recurse Sync  |----->| Yes/No    |---|New Category    |
     +-----------------+     +-----------+   +-----------------+
            |                               |            |
            V                   |                   |
        +-----------------+   +-----------------+
        | Store to dict   |---| Update dict from file |
        +-----------------+   +-----------------+
             |                   ^
             |                   |
             V                   |
        +-----------------+   +-----------------+
        | Store to dump_file|---| Return Category |
        +-----------------+   +-----------------+
```
```

```<explanation>

**Imports:**

- `pathlib`: Provides object oriented way of working with file system paths (e.g., `Path`). Useful for handling file paths.
- `os`: Provides operating system dependent functionality, but usage is minimal in this code.
- `asyncio`: Enables asynchronous operations, vital for handling potentially lengthy web requests in a non-blocking way.
- `typing`: For type hints (`List`, `Dict`). Improves code readability and maintainability.
- `lxml`: An XML/HTML processing library used for parsing web pages.
- `requests`: Used for making HTTP requests to fetch web pages.
- `header`: Likely contains module-specific header information.
- `gs`: Suggests a Google Sheets library import, but not apparent.
- `logger`: Import from `src.logger` module, implying logging is used for debugging and monitoring.
- `j_loads`, `j_dumps`, `pprint`: JSON loading/dumping and pretty printing functions from the `src.utils` module.  Likely custom helpers or extensions for handling JSON data.
- `StringFormatter`:  Custom class for string formatting from `src.utils.string` module.
- `PrestaShop`, `PrestaCategory`: Classes from the `src.endpoints.prestashop` module, likely specific to interacting with PrestaShop APIs.

**Classes:**

- `Category(PrestaCategory)`: Represents a product category. It inherits from `PrestaCategory` which is in the `src.endpoints.prestashop` module. This structure implies a modular approach, with `PrestaCategory` handling core functionality related to PrestaShop categories and `Category` extending that functionality, possibly adding features specific to this program.
    - `credentials`: Stores API credentials, likely for authentication with PrestaShop.
    - `__init__`: Initializes the `Category` object. Calls the parent class's initializer.
    - `get_parents`: Retrieves parent categories for a given category ID using the functionality from the parent class.
    - `crawl_categories_async`: An asynchronous recursive function for crawling category pages and building a hierarchical category tree. Takes the URL of a category page and recursively fetches sub-categories.
    - `crawl_categories`: A synchronous recursive function for the same purpose.

**Functions:**

- `check_duplicate_url`: Checks if a given URL already exists in the hierarchy. Improves data integrity and prevents duplicates.
- `compare_and_print_new_keys`: Compares the category data to a file and reports missing keys in the current data structure. Useful for detecting changes or missing data.

**Variables:**

- `MODE`: A variable set to 'dev'. It could be used to configure different behaviors in development or production.
- `url`, `depth`, `driver`, `locator`, `dump_file`, `id_category_default`, `category`: Parameters passed to `crawl_categories` and `crawl_categories_async`, representing important inputs for crawling and storing category data.
- `category_links`: List of category links found on a page.
- `tasks`: List of asynchronous tasks for traversing children categories.

**Potential Errors and Improvements:**

- **Error Handling:** The code uses `...` for error handling in several places (e.g., `if not category_links`, and `dump_file` operations). Robust error handling is crucial for production use.  The `try...except` blocks should include specific error types and informative logging messages.
- **`driver.wait(1)`:** This code assumes a delay of 1 second after every page load; a more dynamic approach based on actual page load time or explicit Selenium wait conditions is recommended for better performance and responsiveness.
- **`check_duplicate_url`:** While functional, the duplicate check logic could be improved by storing URLs in a set for constant-time lookup.
- **Asynchronous and synchronous functions:** It is unclear why both an asynchronous and synchronous version of the crawling function are implemented.  Asynchronous version is generally preferable, especially when dealing with web requests.
- **Missing `driver` Initialization:** The code assumes a `driver` object exists. This object (e.g., from Selenium) needs to be properly initialized for the code to function correctly.

**Relationship with Other Parts:**

The code heavily relies on other parts of the project in the `src` package, including `src.logger`, `src.utils`, and `src.endpoints.prestashop`, signifying a structured design where different modules handle distinct responsibilities.  The `gs` import suggests this project is intended for managing data, which could be stored in Google Sheets, but this functionality is not fully apparent.