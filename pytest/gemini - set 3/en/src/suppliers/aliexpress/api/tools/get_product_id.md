```python
import pytest
from hypotez.src.suppliers.aliexpress.api.tools.get_product_id import get_product_id
from hypotez.src.suppliers.aliexpress.api.tools import get_product_id
from ..errors import ProductIdNotFoundException
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
import re


# Fixture for mocking extract_prod_ids
@pytest.fixture
def mock_extract_prod_ids(mocker):
    def mock_func(raw_product_id):
        if raw_product_id == "valid_id":
            return "valid_id"
        elif raw_product_id == "invalid_id":
            return None
        else:
            return raw_product_id

    mocker.patch("hypotez.src.suppliers.aliexpress.api.tools.get_product_id.extract_prod_ids",
                 side_effect=mock_func)
    return mock_func


# Tests for get_product_id
def test_get_product_id_valid_input(mock_extract_prod_ids):
    """Checks correct behavior with valid input."""
    product_id = get_product_id("valid_id")
    assert product_id == "valid_id"


def test_get_product_id_invalid_input_return_none(mock_extract_prod_ids):
    """Checks correct handling of invalid input (returns None from extract_prod_ids)."""
    with pytest.raises(ProductIdNotFoundException) as excinfo:
        get_product_id("invalid_id")
    assert "Product id not found: " in str(excinfo.value)


def test_get_product_id_empty_string(mock_extract_prod_ids):
    """Test with an empty string as input."""
    product_id = get_product_id("")
    assert product_id == ""


def test_get_product_id_non_string_input(mock_extract_prod_ids):
    """Test with non-string input."""
    with pytest.raises(TypeError):
      get_product_id(123)


def test_get_product_id_valid_extracted_id(mock_extract_prod_ids):
  """Test a valid id is extracted from the input."""
  expected_id = "12345"
  mock_extract_prod_ids.return_value = expected_id
  actual_id = get_product_id("some_text_with_" + expected_id + "_in_it")
  assert actual_id == expected_id

def test_get_product_id_no_match_found(mock_extract_prod_ids):
    """Test if an exception is raised when no match is found."""
    with pytest.raises(ProductIdNotFoundException) as excinfo:
      get_product_id("no_match_found")
    assert "Product id not found: no_match_found" in str(excinfo.value)

#This test is important, as the original code has a flawed/incomplete implementation
#of exception handling.
def test_get_product_id_none_returned_by_extract_prod_ids(mock_extract_prod_ids):
  """Test the case where extract_prod_ids returns None, which should raise an exception."""
  mock_extract_prod_ids.return_value = None
  with pytest.raises(ProductIdNotFoundException) as excinfo:
    get_product_id("some_text")
  assert "Product id not found: some_text" in str(excinfo.value)

```