```python
import pytest

from hypotez.src.product.product_fields import ProductFields
from hypotez.src.product.product_fields import translate_presta_fields_dict

# Assuming ProductFields is a class and translate_presta_fields_dict is a function
# If there are more classes or function, they need to be defined accordingly

# Example fixture if needed by ProductFields class
@pytest.fixture
def sample_product_fields_data():
    """Provides sample data for testing ProductFields."""
    return {
        "name": "Test Product",
        "price": 100.0,
        "quantity": 10,
        "description": "This is a test product.",
    }

# Tests for ProductFields class
def test_product_fields_creation(sample_product_fields_data):
    """Checks that ProductFields object is created correctly."""
    product_fields = ProductFields(sample_product_fields_data)
    assert product_fields.fields == sample_product_fields_data
    
def test_product_fields_empty_data():
    """Checks that ProductFields object can be created with empty data."""
    product_fields = ProductFields({})
    assert product_fields.fields == {}

def test_product_fields_get_field(sample_product_fields_data):
    """Checks that correct field value is retrieved using get_field method."""
    product_fields = ProductFields(sample_product_fields_data)
    assert product_fields.get_field("name") == "Test Product"
    assert product_fields.get_field("price") == 100.0
    
def test_product_fields_get_field_not_found(sample_product_fields_data):
     """Checks that get_field method handles a non-existent field correctly."""
     product_fields = ProductFields(sample_product_fields_data)
     assert product_fields.get_field("not_found") is None

def test_product_fields_set_field(sample_product_fields_data):
    """Checks that a field is updated correctly using set_field method."""
    product_fields = ProductFields(sample_product_fields_data)
    product_fields.set_field("price", 120.0)
    assert product_fields.get_field("price") == 120.0

def test_product_fields_set_new_field(sample_product_fields_data):
     """Checks that a new field is created correctly using set_field method."""
     product_fields = ProductFields(sample_product_fields_data)
     product_fields.set_field("weight", 1.5)
     assert product_fields.get_field("weight") == 1.5
     assert "weight" in product_fields.fields

# Tests for translate_presta_fields_dict function
def test_translate_presta_fields_dict_valid_input():
    """Checks that translation of valid dictionary works correctly."""
    presta_fields = {
        'id_product': '123',
        'id_manufacturer': '456',
        'reference': 'REF123',
        'ean13': '1234567890123',
        'price': '100.00',
    }
    expected_fields = {
        'id': '123',
        'manufacturer_id': '456',
        'reference': 'REF123',
        'ean': '1234567890123',
        'price': '100.00',
    }
    translated_fields = translate_presta_fields_dict(presta_fields)
    assert translated_fields == expected_fields


def test_translate_presta_fields_dict_empty_input():
    """Checks behavior when input is an empty dict."""
    presta_fields = {}
    translated_fields = translate_presta_fields_dict(presta_fields)
    assert translated_fields == {}

def test_translate_presta_fields_dict_missing_fields():
    """Checks behavior when some expected keys are missing."""
    presta_fields = {
        'id_product': '123',
        'reference': 'REF123',
        'price': '100.00'
    }
    expected_fields = {
        'id': '123',
        'reference': 'REF123',
         'price': '100.00'
    }
    translated_fields = translate_presta_fields_dict(presta_fields)
    assert translated_fields == expected_fields

def test_translate_presta_fields_dict_extra_fields():
    """Checks behavior with extra fields in the dictionary."""
    presta_fields = {
        'id_product': '123',
        'id_manufacturer': '456',
        'reference': 'REF123',
        'ean13': '1234567890123',
        'price': '100.00',
        'extra_field': 'extra'
    }
    expected_fields = {
        'id': '123',
        'manufacturer_id': '456',
        'reference': 'REF123',
        'ean': '1234567890123',
        'price': '100.00',
        'extra_field': 'extra'
    }
    translated_fields = translate_presta_fields_dict(presta_fields)
    assert translated_fields == expected_fields

def test_translate_presta_fields_dict_with_none_values():
    """Checks the behavior when the dict has None values."""
    presta_fields = {
        'id_product': '123',
        'id_manufacturer': None,
        'reference': 'REF123',
        'ean13': None,
        'price': '100.00',
    }
    expected_fields = {
        'id': '123',
        'manufacturer_id': None,
        'reference': 'REF123',
         'ean': None,
        'price': '100.00'
    }
    translated_fields = translate_presta_fields_dict(presta_fields)
    assert translated_fields == expected_fields

```