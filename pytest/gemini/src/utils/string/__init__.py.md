```python
import pytest

from hypotez.src.utils.string import (
    ProductFieldsValidator,
    normalize_string,
    normalize_int,
    normalize_float,
    normalize_boolean,
    normalize_sql_date,
)

# --- Tests for ProductFieldsValidator ---
def test_product_fields_validator_valid_fields():
    """Checks if ProductFieldsValidator correctly identifies valid fields."""
    validator = ProductFieldsValidator(['field1', 'field2', 'field3'])
    assert validator.is_valid_field('field1')
    assert validator.is_valid_field('field2')
    assert validator.is_valid_field('field3')

def test_product_fields_validator_invalid_fields():
    """Checks if ProductFieldsValidator correctly identifies invalid fields."""
    validator = ProductFieldsValidator(['field1', 'field2', 'field3'])
    assert not validator.is_valid_field('field4')
    assert not validator.is_valid_field('field5')
    assert not validator.is_valid_field('another_field')

def test_product_fields_validator_empty_fields():
    """Checks behavior when initialized with an empty list of fields."""
    validator = ProductFieldsValidator([])
    assert not validator.is_valid_field('any_field')
    assert not validator.is_valid_field('')

def test_product_fields_validator_with_non_string_fields():
    """Checks ProductFieldsValidator handles non-string fields."""
    validator = ProductFieldsValidator([1, 2, None, True]) # It will convert it to string so it should be valid.
    assert validator.is_valid_field('1')
    assert validator.is_valid_field('2')
    assert validator.is_valid_field('None')
    assert validator.is_valid_field('True')

def test_product_fields_validator_empty_string_field():
    """Checks ProductFieldsValidator correctly handles an empty string as field."""
    validator = ProductFieldsValidator(['', 'field1'])
    assert validator.is_valid_field('')
    assert validator.is_valid_field('field1')

# --- Tests for normalize_string ---
def test_normalize_string_valid_string():
    """Checks correct behavior with valid string input."""
    assert normalize_string(" Test String ") == "test string"
    assert normalize_string("  Another Test  ") == "another test"

def test_normalize_string_empty_string():
    """Checks behavior with an empty string input."""
    assert normalize_string("") == ""

def test_normalize_string_none_input():
    """Checks handling of None input."""
    assert normalize_string(None) is None

def test_normalize_string_non_string_input():
   """Checks handling of non-string input."""
   with pytest.raises(AttributeError):
       normalize_string(123)

def test_normalize_string_with_special_characters():
    """Checks correct normalization with special characters."""
    assert normalize_string("  Tëst String!@#  ") == "tëst string!@#"


# --- Tests for normalize_int ---
def test_normalize_int_valid_integer():
    """Checks correct behavior with valid integer input."""
    assert normalize_int("123") == 123
    assert normalize_int("  456  ") == 456

def test_normalize_int_zero():
    """Checks behavior with zero input."""
    assert normalize_int("0") == 0

def test_normalize_int_negative_integer():
   """Checks behavior with negative integer input"""
   assert normalize_int("-123") == -123

def test_normalize_int_invalid_input():
    """Checks handling of invalid integer input."""
    assert normalize_int("abc") is None
    assert normalize_int("123.45") is None
    assert normalize_int(None) is None
    assert normalize_int("  ") is None
    assert normalize_int("123a") is None


# --- Tests for normalize_float ---
def test_normalize_float_valid_float():
    """Checks correct behavior with valid float input."""
    assert normalize_float("123.45") == 123.45
    assert normalize_float("  678.90  ") == 678.90

def test_normalize_float_integer_input():
    """Checks correct behavior with valid integer as string input."""
    assert normalize_float("123") == 123.0
    assert normalize_float(" 456 ") == 456.0

def test_normalize_float_zero():
    """Checks behavior with zero input."""
    assert normalize_float("0.0") == 0.0
    assert normalize_float("0") == 0.0
def test_normalize_float_negative_input():
    """Checks behavior with negative float input."""
    assert normalize_float("-123.45") == -123.45
    assert normalize_float("-123") == -123.0

def test_normalize_float_invalid_input():
    """Checks handling of invalid float input."""
    assert normalize_float("abc") is None
    assert normalize_float("123a") is None
    assert normalize_float(None) is None
    assert normalize_float("  ") is None

# --- Tests for normalize_boolean ---
def test_normalize_boolean_valid_true():
    """Checks correct behavior with valid true input."""
    assert normalize_boolean("true") == True
    assert normalize_boolean("  True ") == True
    assert normalize_boolean("1") == True
    assert normalize_boolean("  1  ") == True
    assert normalize_boolean(True) == True # Check true as boolean

def test_normalize_boolean_valid_false():
    """Checks correct behavior with valid false input."""
    assert normalize_boolean("false") == False
    assert normalize_boolean("  False ") == False
    assert normalize_boolean("0") == False
    assert normalize_boolean("  0  ") == False
    assert normalize_boolean(False) == False # Check false as boolean

def test_normalize_boolean_invalid_input():
    """Checks handling of invalid boolean input."""
    assert normalize_boolean("abc") is None
    assert normalize_boolean("123") is None
    assert normalize_boolean(None) is None
    assert normalize_boolean(" ") is None


# --- Tests for normalize_sql_date ---
def test_normalize_sql_date_valid_date():
    """Checks correct behavior with valid SQL date input."""
    assert normalize_sql_date("2023-10-26") == "2023-10-26"
    assert normalize_sql_date("  2024-01-01  ") == "2024-01-01"

def test_normalize_sql_date_invalid_date_format():
   """Checks handling of invalid sql date format."""
   assert normalize_sql_date("2023/10/26") is None
   assert normalize_sql_date("26-10-2023") is None
   assert normalize_sql_date("10-26-2023") is None
   assert normalize_sql_date("20231026") is None
   assert normalize_sql_date("2023-10-26 12:00:00") is None

def test_normalize_sql_date_invalid_input():
    """Checks handling of invalid date input."""
    assert normalize_sql_date("abc") is None
    assert normalize_sql_date(123) is None
    assert normalize_sql_date(None) is None
    assert normalize_sql_date("  ") is None
```