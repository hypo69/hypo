## File hypotez/src/suppliers/aliexpress/campaign/html_generators.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.suppliers.aliexpress.campaign \n\t:platform: Windows, Unix\n\t:synopsis: Генератор HTML контента рекламной кампании\n\n"""\nMODE = 'dev'\n\nimport header   \n\nfrom pathlib import Path\nfrom types import SimpleNamespace\nfrom src.utils.file import save_text_file\nimport html\n\nclass ProductHTMLGenerator:\n    """ Class for generating HTML for individual products."""\n\n    @staticmethod\n    def set_product_html(product: SimpleNamespace, category_path: str | Path):\n        """ Creates an HTML file for an individual product.\n        \n        @param product: The product details to include in the HTML.\n        @param category_path: The path to save the HTML file.\n        """\n        category_name = Path(category_path).name\n        html_path = Path(category_path) / 'html' / f"{product.product_id}.html"\n        \n        html_content = f"""<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>{html.escape(product.product_title)}</title>\n    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css">\n    <link rel="stylesheet" href="styles.css"> <!-- Link to custom CSS file -->\n</head>\n<body>\n    <div class="container">\n        <h1 class="my-4">{html.escape(product.product_title)}</h1>\n        <div class="card">\n            <img src="{Path(product.local_saved_image).as_posix()}" alt="{html.escape(product.product_title)}" class="card-img-top">\n            <div class="card-body">\n                <p class="card-text">Price: <span class="product-price">{product.target_sale_price} {product.target_sale_price_currency}</span></p>\n                <p class="card-text">Original Price: <span class="product-original-price">{product.target_original_price} {product.target_original_price_currency}</span></p>\n                <p class="card-text">Category: <span class="product-category">{html.escape(product.second_level_category_name)}</span></p>\n                <a href="{product.promotion_link}" class="btn btn-primary">Buy Now</a>\n            </div>\n        </div>\n    </div>\n    \n    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>\n</body>\n</html>\n"""\n        save_text_file(html_content, html_path)\n\n# ... (rest of the code is similar)
```

```
<algorithm>
**Step 1: Product HTML Generation**

* **Input:** A `SimpleNamespace` object (`product`) containing product details and a `str` or `Path` object (`category_path`) representing the category directory.
* **Example:** `product = SimpleNamespace(product_id='123', product_title='Example Product', local_saved_image='images/image.jpg', ...)` and `category_path = 'electronics'`
* **Logic:** Extracts the category name, constructs the full path for the product HTML file, generates HTML content with product details and Bootstrap styling, and saves the HTML content to the specified file.
* **Output:** An HTML file named after the product ID within the specified category directory.

**Step 2: Category HTML Generation**

* **Input:** A `list` or `SimpleNamespace` object (`products_list`) containing a list of product details and a `str` or `Path` object (`category_path`) representing the category directory.
* **Example:** `products_list = [product1, product2]` and `category_path = 'clothing'`
* **Logic:**  Processes the input, converting a single `SimpleNamespace` to a list if necessary.  Creates an HTML file with the category's name. Loops through the product list, generating HTML for each product in the format defined in Step 1, embedding them in a Bootstrap grid layout.
* **Output:** An HTML file named "index.html" within the specified category directory containing the products in a grid format.

**Step 3: Campaign HTML Generation**

* **Input:** A `list` of `str` objects (`categories`) representing category names and a `str` or `Path` object (`campaign_path`) representing the campaign directory.
* **Example:** `categories = ['electronics', 'clothing']` and `campaign_path = 'my_campaign'`
* **Logic:** Creates an HTML file named "index.html" within the campaign directory. Generates the HTML content for the campaign overview page containing links to each category's product page.
* **Output:** An HTML file named "index.html" in the campaign directory.


**Data Flow:**

The `ProductHTMLGenerator`, `CategoryHTMLGenerator`, and `CampaignHTMLGenerator` classes are designed to handle specific stages in HTML generation.  The `save_text_file` function in `src.utils.file` is used for saving generated HTML content. Data is passed between classes as arguments (product information, category paths).

```

```
<explanation>

**Imports:**

* `header`: Likely for including project-specific header files or configurations. Its relationship to the `src` package suggests this is a custom module within the project.
* `Path`: From the `pathlib` module, used for creating and manipulating file paths in a more object-oriented way, improving code readability and robustness.
* `SimpleNamespace`: From the `types` module; this is a lightweight container for storing data, often used when the precise structure of the data is not known in advance (e.g., data from an API).  Useful when there are many pieces of data associated with a specific element.
* `save_text_file`: From `src.utils.file`; this function likely handles saving text files to the file system. This import indicates a potential dependency on `src.utils.file`, suggesting a separation of concerns pattern within the project.
* `html`:  From the Python standard library, the `html` module allows escaping HTML special characters.  This prevents injection vulnerabilities when embedding user data within HTML.

**Classes:**

* **`ProductHTMLGenerator`:** Generates HTML content for individual products.
    * `set_product_html`: Takes product data and category path; constructs the file path, generates HTML using f-strings, and saves it using `save_text_file`.
* **`CategoryHTMLGenerator`:** Generates HTML content for product categories.
    * `set_category_html`: Takes a list of product data and category path; processes the input data (handles single-item input), generates HTML with Bootstrap formatting, and saves it using `save_text_file`.  Crucially, it handles both list and single-item inputs for greater flexibility.
* **`CampaignHTMLGenerator`:** Generates HTML for the campaign overview, listing all categories.
    * `set_campaign_html`: Takes a list of category names and campaign path. Creates a campaign overview page containing links to the individual category pages.

**Functions:**

* `save_text_file`: Takes the HTML content and path as arguments and saves the content to a file.  The implementation is missing.

**Variables:**

* `MODE`: A string variable likely used for configuration (e.g., 'dev', 'prod').
* `html_content`: Used to store the generated HTML content in each method.
* `html_path`: Stores the full path to the output HTML file.
* `category_name`: Holds the category name extracted from the path.
* `products_list`: List of product information, passed to `CategoryHTMLGenerator`.



**Potential Errors or Improvements:**

* **Error Handling:** The code lacks error handling.  If `product` or `products_list` is invalid, or if saving fails, the script will likely crash.  Using `try...except` blocks is crucial to prevent unexpected program termination.
* **File Existence:** The code doesn't check if the output directory exists.  It might lead to an error if the category path does not exist.  Using `os.makedirs(html_path.parent, exist_ok=True)` is a good practice to ensure directory creation only if it doesn't exist.
* **Validation:** Input validation for `product` data could be added. Missing `product` attributes could cause errors.
* **CSS:** The code assumes a file named "styles.css" exists in the same directory as the generated HTML files.  A better approach would be to pass the CSS file path as an argument for more flexibility.

**Relationship to Other Parts of the Project:**

The code depends on `src.utils.file` for saving HTML, which implies a clear separation of concerns and utility functions.  The `SimpleNamespace` usage suggests that data likely originates from another part of the project, potentially from an API call, data transformation, or another supplier module (since data like `local_saved_image`, etc. implies some processing before getting here). The `header` import also implies that the project has a structure where modules can import other modules.