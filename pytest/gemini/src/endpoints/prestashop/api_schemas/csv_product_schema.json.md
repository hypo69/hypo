```python
import pytest
import json

# Fixture to load the schema
@pytest.fixture
def csv_product_schema():
    """Loads the CSV product schema from the JSON file."""
    with open("hypotez/src/endpoints/prestashop/api_schemas/csv_product_schema.json", 'r') as f:
        schema = json.load(f)
    return schema

def test_csv_product_schema_structure(csv_product_schema):
    """Checks if the loaded schema is a dictionary and not empty."""
    assert isinstance(csv_product_schema, dict), "The loaded schema is not a dictionary."
    assert csv_product_schema, "The loaded schema is empty."

def test_csv_product_schema_keys(csv_product_schema):
    """Checks if specific keys exist in the schema."""
    expected_keys = [
        "ID", "Active (0/1)", "Name*", "Categories (x,y,z...)", "Price tax excluded",
        "Price tax included", "Tax rule ID", "Cost price", "On sale (0/1)",
        "Discount amount", "Discount percent", "Discount from (yyyy-mm-dd)",
        "Discount to (yyyy-mm-dd)", "reference #", "Supplier reference #",
        "Supplier", "Brand", "EAN13", "UPC", "MPN", "Ecotax", "Width", "Height",
        "Depth", "Weight", "Delivery time of in-stock products:",
        "Delivery time of out-of-stock products with allowed orders:", "Quantity",
        "Minimal quantity", "Low stock level",
        "Send me an email when the quantity is under this level", "Visibility",
        "Additional shipping cost", "Unit for base price", "Base price", "Summary",
        "Description", "Tags (x,y,z...)", "Meta title", "Meta keywords",
        "Meta description", "Rewritten URL", "Label when in stock",
        "Label when backorder allowed", "Available for order (0 = No, 1 = Yes)",
        "Product availability date", "Product creation date",
        "Show price (0 = No, 1 = Yes)", "additional_images_urls",
        "additional_images_alts", "Delete existing images (0 = No, 1 = Yes)",
        "Feature (Name:Value:Position:Customized)",
        "Available online only (0 = No, 1 = Yes)", "Condition",
        "Customizable (0 = No, 1 = Yes)", "Uploadable files (0 = No, 1 = Yes)",
        "Text fields (0 = No, 1 = Yes)", "Action when out of stock",
        "Virtual product (0 = No, 1 = Yes)", "File URL",
        "Number of allowed downloads", "Expiration date (yyyy-mm-dd)",
        "Number of days", "ID / Name of shop", "Advanced Stock Management",
        "Depends on stock", "Warehouse", "Accessories (x,y,z...)",
        "affiliate short link", "affiliate text", "affiliate summary",
        "affiliate summary 2", "Open AI Product Description", "Byer protection",
         "Specification", "Refirbished product description",
        "Additional shipping details", "Product features", "Additional product info"
    ]
    for key in expected_keys:
        assert key in csv_product_schema, f"Key '{key}' not found in schema."

def test_csv_product_schema_null_values(csv_product_schema):
    """Checks if most of the schema values are initialized as None"""
    nullable_keys = [
        "ID", "Active (0/1)", "Name*", "Price tax excluded",
        "Price tax included", "Tax rule ID", "Cost price", "On sale (0/1)",
        "Discount amount", "Discount percent", "Discount from (yyyy-mm-dd)",
        "Discount to (yyyy-mm-dd)", "reference #", "Supplier reference #",
        "Supplier", "Brand", "EAN13", "UPC", "MPN", "Ecotax", "Width", "Height",
        "Depth", "Weight", "Delivery time of in-stock products:",
        "Delivery time of out-of-stock products with allowed orders:", "Quantity",
        "Minimal quantity", "Low stock level",
        "Send me an email when the quantity is under this level", "Visibility",
        "Additional shipping cost", "Unit for base price", "Base price", "Summary",
        "Description", "Tags (x,y,z...)", "Meta title", "Meta keywords",
        "Meta description", "Rewritten URL", "Label when in stock",
        "Label when backorder allowed", "Available for order (0 = No, 1 = Yes)",
        "Product availability date", "Product creation date",
        "Show price (0 = No, 1 = Yes)", "additional_images_urls",
        "additional_images_alts", "Delete existing images (0 = No, 1 = Yes)",
        "Feature (Name:Value:Position:Customized)",
        "Available online only (0 = No, 1 = Yes)", "Condition",
        "Customizable (0 = No, 1 = Yes)", "Uploadable files (0 = No, 1 = Yes)",
        "Text fields (0 = No, 1 = Yes)", "Action when out of stock",
        "Virtual product (0 = No, 1 = Yes)", "File URL",
        "Number of allowed downloads", "Expiration date (yyyy-mm-dd)",
        "Number of days", "ID / Name of shop", "Advanced Stock Management",
        "Depends on stock", "Warehouse", "Accessories (x,y,z...)",
        "affiliate short link", "affiliate text", "affiliate summary",
        "affiliate summary 2", "Open AI Product Description", "Byer protection",
         "Specification", "Refirbished product description", "Product features", "Additional product info"
    ]
    for key in nullable_keys:
        assert csv_product_schema[key] is None, f"Key '{key}' value is not None"

def test_csv_product_schema_non_null_values(csv_product_schema):
    """Check if particular schema values are not None"""
    assert csv_product_schema["Categories (x,y,z...)"] == "2,", "Categories value is not '2,'."
    assert csv_product_schema["Additional shipping details"] == "", "Additional shipping details value is not ''."
```