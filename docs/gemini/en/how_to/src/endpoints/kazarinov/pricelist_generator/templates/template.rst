How to use this HTML template for generating price lists
========================================================================================

Description
-------------------------
This HTML template (`template.html`) is designed to generate a dynamic price list.  It displays a list of products, each with an image, title, description, and specification.  The template also calculates and displays the total price of all products, along with the currency.  Crucially, it utilizes Jinja templating language for dynamic content insertion.


Execution steps
-------------------------
1. **Data Preparation:**  Populate the `products` variable with a list of dictionaries. Each dictionary should contain the following keys and values:
    * `product_title`: The title of the product.
    * `product_description`: A description of the product.
    * `specification`: Product specification details.
    * `image_local_saved_path`: The local path to the product image.

2. **Template Filling (using Jinja):** Use a templating engine (like Jinja) to populate the template placeholders with your data.  This will substitute values from the `products`, `title`, `description`, `price`, `currency` variables into the HTML.  The Jinja syntax `{{ variable_name }}` is used for this substitution.
   * `{{ title }}`:  The title of the price list.
   * `{{ description }}`:  A description for the price list.
   * `{{ price }}`: The total price.
   * `{{ currency }}`: The currency.


3. **Rendering the template:** The templating engine (Jinja) will create the rendered HTML output, ready to be displayed in a web browser.

Usage example
-------------------------
.. code-block:: python

    # Example Python code (using Jinja2 as an example)

    from jinja2 import Environment, FileSystemLoader

    # Load the template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Sample data (replace with your actual data)
    products = [
        {'product_title': 'Product 1', 'product_description': 'Description for Product 1', 'specification': 'Spec 1', 'image_local_saved_path': 'path/to/image1.jpg'},
        {'product_title': 'Product 2', 'product_description': 'Description for Product 2', 'specification': 'Spec 2', 'image_local_saved_path': 'path/to/image2.jpg'},
    ]
    price = 100
    currency = "USD"
    title = "Price List Example"
    description = "Price list of products"

    # Render the template
    rendered_html = template.render(
        title=title,
        description=description,
        products=products,
        price=price,
        currency=currency,
    )

    # Now, you can use rendered_html to display the price list, e.g. save to a file or pass to a web framework.


Important Note:  The code assumes you are using a templating engine (like Jinja2) to dynamically insert data.  Replace `'.'` in the `FileSystemLoader` with the path to the directory containing `template.html`.  You need to install Jinja2 if you haven't already: `pip install Jinja2`.  Also, ensure that the paths to the image files (`image_local_saved_path`) are correct and accessible.