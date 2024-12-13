```python
import pytest

# Since the provided input is a README.md file describing modules, 
# there is no actual Python code to test. 
# Therefore, the tests will focus on simulating how tests would be structured if we had the `product.py` and `product_fields` modules.
# This is a test file based on the description provided by the user


# Simulated product module (product.py) - replace with actual product.py
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError("Price must be positive")
        self.price = new_price

    @staticmethod
    def create_product(product_id, name, price):
        if not all([isinstance(product_id, int) , isinstance(price, (int, float)), isinstance(name, str) ]):
          raise TypeError("Invalid type of arguments")
        if price <= 0:
            raise ValueError("Price must be positive")
        return Product(product_id, name, price)
    
    def __repr__(self) -> str:
      return f"Product(product_id={self.product_id}, name='{self.name}', price={self.price})"

# Simulated product fields module - replace with actual code
class ProductField:
    def __init__(self, name, data_type, validation_rules=None):
        self.name = name
        self.data_type = data_type
        self.validation_rules = validation_rules or []

    def validate(self, value):
        if self.data_type == "int" and not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer.")
        if self.data_type == "str" and not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string.")
        if self.data_type == "float" and not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a float.")
        for rule in self.validation_rules:
            if not rule(value):
               raise ValueError(f"{self.name} validation failed: {rule}")
        return True
    
    def add_validation(self, rule):
        self.validation_rules.append(rule)
    

def is_not_empty(value):
  return  value != ""

# Fixtures
@pytest.fixture
def sample_product():
    return Product(1, "Test Product", 100.0)

@pytest.fixture
def sample_product_field():
    return ProductField("test_field", "str", [is_not_empty])

# Tests for product.py (simulated)
def test_product_creation_valid():
    """Checks correct product creation with valid input."""
    product = Product.create_product(1, "Test", 100)
    assert product.product_id == 1
    assert product.name == "Test"
    assert product.price == 100

def test_product_creation_invalid_price():
    """Checks correct exception handling when price is invalid (<=0)."""
    with pytest.raises(ValueError, match="Price must be positive"):
        Product.create_product(1, "Test", 0)

def test_product_creation_invalid_type():
    """Checks correct exception handling when incorrect type of arguments is passed."""
    with pytest.raises(TypeError, match="Invalid type of arguments"):
        Product.create_product("1", "Test", 0)

def test_product_update_price_valid(sample_product):
    """Checks correct price update with a valid price."""
    sample_product.update_price(150.0)
    assert sample_product.price == 150.0

def test_product_update_price_invalid(sample_product):
    """Checks correct exception handling when updating with an invalid price (<= 0)."""
    with pytest.raises(ValueError, match="Price must be positive"):
        sample_product.update_price(0)

def test_product_repr(sample_product):
  assert repr(sample_product) == "Product(product_id=1, name='Test Product', price=100.0)"

# Tests for product_fields (simulated)
def test_product_field_validation_valid(sample_product_field):
    """Checks correct validation with a valid value."""
    assert sample_product_field.validate("test_value") is True

def test_product_field_validation_invalid_type(sample_product_field):
    """Checks correct exception handling with an invalid type."""
    sample_product_field.add_validation(lambda x: x!= 1)
    with pytest.raises(TypeError, match="test_field must be a string"):
        sample_product_field.validate(123)

def test_product_field_validation_invalid_rule(sample_product_field):
    """Checks correct exception handling when validation rule fails."""
    with pytest.raises(ValueError, match="test_field validation failed"):
        sample_product_field.validate("")
```