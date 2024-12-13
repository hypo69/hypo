```python
import pytest
from unittest.mock import patch, mock_open
from types import SimpleNamespace
from src.product.product import Product
from src.product.product_fields.product_fields import ProductFields


# Fixture for ProductFields
@pytest.fixture
def product_fields():
    """Provides an instance of ProductFields for testing."""
    return ProductFields()

# Mock the PrestaShop class for testing Product
class MockPrestaShop:
    def __init__(self, return_value):
        self.return_value = return_value

    def get_parent_categories(self, id_category, dept=0):
        return self.return_value

# Mock the Category class for testing static get_parent_categories
class MockCategory:
    @staticmethod
    def get_parents(id_category, dept=0):
        return [f"mock_category_{id_category}_{dept}"]


# Tests for Product class

def test_product_init():
    """Checks if Product object can be initialized."""
    product = Product()
    assert isinstance(product, Product)

@patch('src.product.product.Category', MockCategory)
def test_product_get_parent_categories_valid_input():
    """Checks if get_parent_categories returns correct categories with valid input."""
    mock_prestashop = MockPrestaShop(["mock_category_123_0", "mock_category_123_1"])
    product = Product()
    product.prestashop = mock_prestashop
    categories = product.get_parent_categories(123)
    assert categories == ["mock_category_123_0", "mock_category_123_1"]

@patch('src.product.product.Category', MockCategory)
def test_product_get_parent_categories_with_dept():
    """Checks if get_parent_categories handles a different depth."""
    mock_prestashop = MockPrestaShop(["mock_category_456_2", "mock_category_456_3"])
    product = Product()
    product.prestashop = mock_prestashop
    categories = product.get_parent_categories(456, dept=2)
    assert categories == ["mock_category_456_2", "mock_category_456_3"]


# Tests for static method get_parent_categories

@patch('src.product.product.Category', MockCategory)
def test_get_parent_categories_static_valid_input():
    """Checks if the static method returns the correct categories with valid input."""
    categories = Product.get_parent_categories(123)
    assert categories == ["mock_category_123_0"]


@patch('src.product.product.Category', MockCategory)
def test_get_parent_categories_static_with_depth():
    """Checks if the static method handles depth correctly."""
    categories = Product.get_parent_categories(456, dept=2)
    assert categories == ["mock_category_456_2"]


def test_get_parent_categories_static_invalid_input():
    """Checks if TypeError is raised if id_category is not an integer."""
    with pytest.raises(TypeError):
        Product.get_parent_categories("invalid_id")


# Tests for ProductFields class

def test_product_fields_init(product_fields):
    """Checks if ProductFields object can be initialized and loads attributes."""
    assert isinstance(product_fields, ProductFields)
    assert isinstance(product_fields.product_fields_list, list)
    assert isinstance(product_fields.language, dict)
    assert isinstance(product_fields.presta_fields, SimpleNamespace)
    assert isinstance(product_fields.assist_fields_dict, dict)


def test_load_product_fields_list(product_fields):
    """Checks if the fields list is loaded correctly."""
    test_fields_list = ['field1', 'field2', 'field3']
    with patch('builtins.open', mock_open(read_data='\n'.join(test_fields_list))):
        loaded_list = product_fields._load_product_fields_list()
        assert loaded_list == test_fields_list


def test_payload_success(product_fields):
    """Checks if payload loads defaults successfully."""
    test_defaults = {'field1': 'value1', 'field2': 'value2'}
    with patch('builtins.open', mock_open(read_data='{"field1": "value1", "field2": "value2"}')):
        assert product_fields._payload() is True
        assert product_fields.presta_fields.field1 == "value1"
        assert product_fields.presta_fields.field2 == "value2"


def test_payload_failure(product_fields):
    """Checks if payload returns False on error."""
    with patch('builtins.open', side_effect=FileNotFoundError):
       assert product_fields._payload() is False


def test_id_product_property(product_fields):
    """Checks if the id_product property works correctly."""
    product_fields.id_product = 123
    assert product_fields.id_product == 123


def test_price_property(product_fields):
    """Checks if the price property works correctly."""
    product_fields.price = 19.99
    assert product_fields.price == 19.99

def test_active_property(product_fields):
    """Checks if the active property works correctly."""
    product_fields.active = 1
    assert product_fields.active == 1

def test_non_existent_property(product_fields):
    """Checks if accessing a non-existent property returns None"""
    assert product_fields.non_existent_field is None

def test_set_non_existent_property(product_fields):
    """Checks if setting a non-existent property creates it"""
    product_fields.new_field = "new_value"
    assert product_fields.new_field == "new_value"
```