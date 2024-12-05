```python
import pytest

# Placeholder for the PrestaShop module (replace with actual code)
class Product:
    def get_product_data(self, product_id):
        if product_id == "12345":
            return {"id": 12345, "name": "Example Product"}
        elif product_id == "invalid":
            raise ValueError("Invalid product ID")
        else:
            return None
        
    def get_all_products(self):
        return [{"id":1, "name":"Product 1"}, {"id": 2, "name": "Product 2"}]
        


# Tests for the Product class
def test_get_product_data_valid_input():
    """Checks if get_product_data returns the correct data for a valid product ID."""
    product = Product()
    product_data = product.get_product_data("12345")
    assert product_data == {"id": 12345, "name": "Example Product"}


def test_get_product_data_invalid_input():
    """Checks if get_product_data raises a ValueError for an invalid product ID."""
    product = Product()
    with pytest.raises(ValueError) as excinfo:
        product.get_product_data("invalid")
    assert str(excinfo.value) == "Invalid product ID"

def test_get_product_data_nonexistent_product():
    """Checks if get_product_data returns None for a non-existent product ID."""
    product = Product()
    product_data = product.get_product_data("67890")
    assert product_data is None


def test_get_all_products():
    """Checks if get_all_products returns a list of product dictionaries."""
    product = Product()
    products = product.get_all_products()
    assert isinstance(products, list)
    assert len(products) == 2
    assert isinstance(products[0], dict)  # Validate each product is a dictionary
    assert products[0].get("id") == 1
```