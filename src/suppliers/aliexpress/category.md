
# Aliexpress Category Management Module

This module provides functionality for managing categories on AliExpress. It allows for retrieving product URLs, updating category lists, and interacting with the AliExpress platform for category synchronization.

## Overview

The module contains various functions and methods for interacting with product categories on AliExpress, including retrieving product URLs, updating categories in scenario files, and managing category data within a database.

### Key Features:
- **Retrieve Product URLs**: Collects product URLs from category pages.
- **Category Synchronization**: Compares and updates categories on the site with those in local scenario files.
- **Database Interaction**: Offers database operations for managing categories.
  
## Functions

### `get_list_products_in_category(s: Supplier) -> list[str, str]`
Retrieves the list of product URLs from the category page, including pagination.

#### Parameters:
- `s` (`Supplier`): The supplier instance with the browser driver and locators.

#### Returns:
- A list of product URLs from the category page.

---

### `get_prod_urls_from_pagination(s: Supplier) -> list[str]`
Fetches product URLs from category pages, handling pagination.

#### Parameters:
- `s` (`Supplier`): The supplier instance with the browser driver and locators.

#### Returns:
- A list of product URLs.

---

### `update_categories_in_scenario_file(s: Supplier, scenario_filename: str) -> bool`
Compares the categories on the site with those in the provided scenario file and updates the file with any changes.

#### Parameters:
- `s` (`Supplier`): The supplier instance with the browser driver and locators.
- `scenario_filename` (`str`): The name of the scenario file to be updated.

#### Returns:
- `True` if the categories were successfully updated, `False` otherwise.

---

### `get_list_categories_from_site(s: Supplier, scenario_file: str, brand: str = '') -> list`
Fetches the list of categories from the AliExpress site, based on the provided scenario file.

#### Parameters:
- `s` (`Supplier`): The supplier instance with the browser driver and locators.
- `scenario_file` (`str`): The scenario file containing category information.
- `brand` (`str`, optional): The brand filter for the categories.

#### Returns:
- A list of categories from the site.

---

## Classes

### `DBAdaptor`
Provides methods for interacting with the database, allowing for standard operations such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE` on `AliexpressCategory` records.

#### Methods:
- `select`: Retrieves records from the `AliexpressCategory` table.
- `insert`: Inserts a new record into the `AliexpressCategory` table.
- `update`: Updates an existing record in the `AliexpressCategory` table.
- `delete`: Deletes a record from the `AliexpressCategory` table.

---

## Dependencies

This module relies on several other modules for various functionalities:

- `src.db.manager_categories.suppliers_categories`: For managing categories in the database.
- `src.utils.jjson`: For working with JSON data.
- `src.logger`: For logging errors and messages.
- `requests`: For making HTTP requests to retrieve category data from the AliExpress site.

---

## Usage Example

```python
from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file

# Example usage
supplier_instance = Supplier()
category_urls = get_list_products_in_category(supplier_instance)
update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
```

---

## License

This module is licensed under the MIT License.

```

This README provides a comprehensive overview of the module, its functions, and how to use it.