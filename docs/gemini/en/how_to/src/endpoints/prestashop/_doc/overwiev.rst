rst
How to use the PrestaShop Module
========================================================================================

Description
-------------------------
This document outlines the directory structure and key components of the PrestaShop module. It details how the module is organized to manage various aspects of PrestaShop functionality, including categories, customers, products, languages, price lists, shops, suppliers, warehouses, and the PrestaShop API interaction.  It also includes an example of how to use the `product` module.

Execution steps
-------------------------
1. **Understanding the Directory Structure:** The PrestaShop module is structured into several directories, including `PrestaShop`, `_examples`, `api`, `api_schemas`, and `domains`.
    * The `PrestaShop` directory contains core modules for each PrestaShop entity (e.g., `category.py`, `product.py`).
    * The `_examples` directory provides example scripts and documentation.
    * The `api` directory handles interactions with the PrestaShop API.
    * The `api_schemas` directory defines JSON schemas for API resources.
    * The `domains` directory contains settings for different PrestaShop instances (e.g., `ecat.co.il`).

2. **Identifying Key Components:**  The module comprises several key components, each responsible for a specific PrestaShop functionality. This includes modules for categories, customers, languages, price lists, products, shops, suppliers, warehouses, the API, and API schemas.

3. **Using the API:** The `api` directory provides the main logic for interacting with the PrestaShop API.   Specific modules within the PrestaShop directory (e.g., `product.py`) likely use the API to retrieve or update data.

4. **Understanding API Schemas:** The `api_schemas` directory contains JSON schemas defining the structure of data exchanged with the PrestaShop API.  These are used to validate and structure the data.

5. **Utilizing Domain-Specific Settings:** The `domains` directory allows for customization of the module for different PrestaShop instances. Each domain folder contains a `settings.json` file to define configuration options.

6. **Example Usage (Product Module):** To utilize the product module, import the `Product` class from `PrestaShop.product`.
    * Create an instance of the `Product` class.
    * Use the `get_product_data` method, providing a product ID to retrieve the product's data.
    * The `get_product_data` method is likely interacting with the PrestaShop API to fetch the required information.


Usage example
-------------------------
.. code-block:: python

    from PrestaShop.product import Product

    # Initialize the Product module
    product = Product()

    # Example: Get product data for product ID 12345
    try:
        product_data = product.get_product_data(product_id="12345")
        print(product_data)
    except Exception as e:
        print(f"Error fetching product data: {e}")