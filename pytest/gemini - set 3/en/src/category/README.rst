```python
import pytest
import datetime


# Replace with the actual code for the Product and Supplier classes.
# Example implementation:
class Supplier:
    def __init__(self, name, product_list):
        self.name = name
        self.products = product_list

    def get_products(self):
        return self.products

class Product:
    def __init__(self, name, price, date):
        self.name = name
        self.price = price
        self.date = date


def categorize_products(supplier):
    """
    Categorizes products from a supplier based on their price.
    Products with prices below 10 are categorized as 'cheap'.
    Products with prices between 10 and 50 are categorized as 'medium'.
    Products with prices above 50 are categorized as 'expensive'.
    Raises TypeError if input is not a Supplier object.
    Raises ValueError if a Product object within the Supplier does not have a valid price.
    """
    if not isinstance(supplier, Supplier):
        raise TypeError("Input must be a Supplier object.")

    categories = {
        'cheap': [],
        'medium': [],
        'expensive': []
    }

    for product in supplier.get_products():
        if not isinstance(product, Product):
            raise ValueError("Invalid product object found.")
        if not isinstance(product.price, (int, float)):
             raise ValueError("Product price must be a number.")

        if product.price < 10:
            categories['cheap'].append(product)
        elif 10 <= product.price <= 50:
            categories['medium'].append(product)
        elif product.price > 50:
            categories['expensive'].append(product)
        else:
            raise ValueError("Invalid product price")


    return categories


@pytest.fixture
def supplier_data():
    """Provides test data for the supplier."""
    return Supplier("Test Supplier", [
        Product("Product A", 5, datetime.date(2023, 10, 26)),
        Product("Product B", 25, datetime.date(2023, 10, 27)),
        Product("Product C", 75, datetime.date(2023, 10, 28))
    ])


def test_categorize_products_valid_input(supplier_data):
    """Tests categorization with valid input."""
    categories = categorize_products(supplier_data)
    assert len(categories['cheap']) == 1
    assert len(categories['medium']) == 1
    assert len(categories['expensive']) == 1


def test_categorize_products_invalid_supplier_type():
    """Tests handling of non-Supplier input."""
    with pytest.raises(TypeError):
        categorize_products("not a supplier")


def test_categorize_products_invalid_product_type():
    """Test with invalid product object in the supplier list."""
    supplier = Supplier("Invalid Supplier", ["not a product"])
    with pytest.raises(ValueError):
        categorize_products(supplier)


def test_categorize_products_invalid_product_price():
    """Test with invalid product price."""
    supplier = Supplier("Invalid Price", [Product("Bad Price", "abc", datetime.date(2023, 10, 28))])
    with pytest.raises(ValueError):
        categorize_products(supplier)

```