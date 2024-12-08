rst
How to use the HTML Generators
========================================================================================

Description
-------------------------
This code defines classes for generating HTML content for AliExpress campaigns.  It creates HTML files for individual products, product categories, and an overall campaign overview.  The code uses the `save_text_file` function from a `src.utils.file` module to save the generated HTML content to files.  It leverages the `SimpleNamespace` object for product data, and handles different data types for the `products_list` parameter. The code also uses Bootstrap for styling.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports modules like `header`, `Path` from `pathlib`, `SimpleNamespace` from `types`, `save_text_file` from `src.utils.file`, `html` for escaping special characters, and ensures the proper encoding.


2. **`ProductHTMLGenerator` class:** This class handles generating HTML for individual products.
    - `set_product_html(product, category_path)`:
        - Takes a `product` object (likely containing product details) and `category_path` as input.
        - Constructs the full path for the HTML file (`html_path`) within the category directory.
        - Creates an HTML string containing product information, including title, image, price, original price, category, and a "Buy Now" button link.
        - Escapes HTML special characters using `html.escape` for security.
        - Uses Bootstrap for styling.
        - Saves the generated HTML content to the `html_path`.


3. **`CategoryHTMLGenerator` class:** This class handles generating HTML for product categories.
    - `set_category_html(products_list, category_path)`:
        - Takes a `products_list` (a list of products or a single product object) and `category_path` as input.
        - Creates the HTML file path (`html_path`).
        - Constructs an HTML string that displays a grid of product information (title, image, price, original price, category, "Buy Now" button) using Bootstrap.
        - Iterates through each product in the `products_list` and creates the HTML representation for it.
        - Saves the HTML content to the `html_path` file.


4. **`CampaignHTMLGenerator` class:** This class handles generating HTML for the entire campaign.
    - `set_campaign_html(categories, campaign_path)`:
        - Takes a list of `categories` and `campaign_path` as input.
        - Constructs the `html_path` for the campaign index page.
        - Constructs an HTML string that presents the campaign's categories as a list of links.
        - Saves the generated HTML to the `html_path`.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator
    from pathlib import Path
    from types import SimpleNamespace

    # Sample product data (replace with your actual product data)
    product = SimpleNamespace(
        product_id=123,
        product_title="Example Product",
        local_saved_image="images/example.jpg",  # Replace with the actual image path
        target_sale_price=10.99,
        target_sale_price_currency="USD",
        target_original_price=15.99,
        target_original_price_currency="USD",
        second_level_category_name="Electronics",
        promotion_link="https://www.example.com/product/123",
    )

    category_path = Path("./category1")
    campaign_path = Path("./campaign")

    # Generate HTML for a single product
    ProductHTMLGenerator.set_product_html(product, category_path)

    # Example with a list of products
    products_list = [product, product]

    CategoryHTMLGenerator.set_category_html(products_list, category_path)

    # Generate HTML for the entire campaign
    categories_list = ["category1"]
    CampaignHTMLGenerator.set_campaign_html(categories_list, campaign_path)