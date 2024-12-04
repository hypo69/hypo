```python
import pytest
from hypotez.src.suppliers.aliexpress.api.tools.get_product_id import get_product_id
from hypotez.src.suppliers.aliexpress.errors import ProductIdNotFoundException
from hypotez.src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids


def test_get_product_id_valid_input():
    """Tests get_product_id with a valid input string."""
    valid_input = "product-id:123456"
    expected_output = "123456"
    actual_output = get_product_id(valid_input)
    assert actual_output == expected_output


def test_get_product_id_valid_input_with_space():
    """Tests get_product_id with a valid input string containing spaces."""
    valid_input = " ProductID : 654321 "
    expected_output = "654321"
    actual_output = get_product_id(valid_input)
    assert actual_output == expected_output


@pytest.mark.parametrize("input_string, expected_output", [
    ("12345", "12345"),
    ("987654321", "987654321"),
    ("1234567890", "1234567890")
])
def test_get_product_id_various_valid_inputs(input_string, expected_output):
    """Tests get_product_id with various valid input strings."""
    actual_output = get_product_id(input_string)
    assert actual_output == expected_output


def test_get_product_id_empty_string():
    """Tests get_product_id with an empty string."""
    empty_string = ""
    with pytest.raises(ProductIdNotFoundException) as excinfo:
        get_product_id(empty_string)
    assert "Product id not found: " in str(excinfo.value)


def test_get_product_id_invalid_format_no_numbers():
    """Tests get_product_id with invalid input string, no numbers."""
    invalid_format = "product-xyz"
    with pytest.raises(ProductIdNotFoundException) as excinfo:
        get_product_id(invalid_format)
    assert "Product id not found: " in str(excinfo.value)


def test_get_product_id_complex_input():
    """Tests get_product_id with complex input string."""
    complex_input = "This is a test string with productID: 9876543210"
    expected_output = "9876543210"
    actual_output = get_product_id(complex_input)
    assert actual_output == expected_output

def test_extract_prod_ids_valid_input():
    valid_input = "12345"
    expected_output = "12345"
    actual_output = extract_prod_ids(valid_input)
    assert actual_output == expected_output


def test_extract_prod_ids_invalid_input():
    invalid_input = "invalid_input"
    with pytest.raises(ProductIdNotFoundException) as excinfo:
        extract_prod_ids(invalid_input)
    assert "Product id not found: " in str(excinfo.value)

def test_extract_prod_ids_empty_input():
    with pytest.raises(ProductIdNotFoundException) as excinfo:
        extract_prod_ids("")
    assert "Product id not found: " in str(excinfo.value)

```