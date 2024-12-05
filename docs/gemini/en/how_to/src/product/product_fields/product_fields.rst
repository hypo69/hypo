rst
How to use the `ProductFields` class
========================================================================================

Description
-------------------------
This Python code defines a `ProductFields` class designed for handling product data in the PrestaShop API format.  It meticulously maps product fields to their corresponding database columns in PrestaShop's `ps_product` and `ps_product_lang` tables. The class allows for setting and retrieving values for these fields, facilitating the creation and update of product information. Importantly, it incorporates language handling, designed for multilingual product descriptions and other fields.  The `ProductFields` class also includes error handling using the `ProductFieldException` class and logging to help with debugging.


Execution steps
-------------------------
1. **Import necessary modules:** The code begins by importing various modules, including `pathlib`, `pydantic`, `sqlite3`, `langdetect`, `functools`, `enum`, and custom modules (`gs`, `jjson`, `category`, `string`, `logger`, and `header`). These modules provide functionalities for file handling, data validation, language detection, and logging.

2. **Define the `ProductFields` class:**  This class encapsulates the logic for handling product fields.  It includes an `__init__` method to initialize product fields, language mappings, and default values.

3. **`_load_product_fields_list()` method:** This helper function reads a list of product field names from a text file (`fields_list.txt`). This list likely corresponds to the order of fields in the PrestaShop database tables.

4. **`_payload()` method:**  This method loads default values for product fields from a JSON file (`product_fields_default_values.json`).

5. **Property and Setter Methods:** The class defines numerous properties (`@property`) and setters (`@setter`) for each product field. Each field has a dedicated getter and setter method, allowing access to and modification of the field's value while employing error handling and logging for robustness.  Crucially, the setters handle various data types, including integers, floats, strings, and date/time objects.

6. **Multilingual Field Handling:** The most significant aspect of the code is its handling of multilingual fields in the `ps_product_lang` table.  Setter methods for these fields (`description`, `description_short`, `name`, etc.) create dictionaries with language-specific values, which will likely need further processing to be used effectively in PrestaShop.

7. **Error Handling:** The code utilizes `try...except` blocks within setter methods to catch potential exceptions (`ProductFieldException`) related to field population. This helps prevent unexpected crashes during data manipulation.

8. **Logging:**  The code makes extensive use of the `logger` module to document actions, debug, and log errors.

9. **Data Types:** The code specifically defines type hints (`typing.List`, `typing.Dict`, etc.) for various parameters to improve code readability and maintainability.

10. **Usage Example (Illustrative):**  While not a required step, the file includes usage examples in code blocks (using `langdetect`.) This is not critical in understanding the `ProductFields` class itself, but highlights how to use the imported language detection libraries.  You'd replace these examples with code that actually utilizes the getters and setters to populate product data.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.product.product_fields.product_fields import ProductFields

    # Create an instance of the ProductFields class
    product_fields = ProductFields()

    # Set a product's name in English
    product_fields.name = "Example Product", 'en'

    # Get the product's name
    product_name = product_fields.name

    # Print the name
    print(f"Product name: {product_name}")