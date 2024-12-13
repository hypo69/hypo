```python
import pytest
from hypotez.src.suppliers.aliexpress.api.helpers.arguments import (
    get_list_as_string,
    get_product_ids,
)
from hypotez.src.suppliers.aliexpress.api.errors.exceptions import InvalidArgumentException


def test_get_list_as_string_none_input():
    """Checks the behavior with None input, should return None."""
    assert get_list_as_string(None) is None


def test_get_list_as_string_valid_string_input():
    """Checks the behavior with a valid string input, should return the same string."""
    test_string = "test_string"
    assert get_list_as_string(test_string) == test_string


def test_get_list_as_string_valid_list_input():
    """Checks the behavior with a valid list input, should return a comma-separated string."""
    test_list = ["item1", "item2", "item3"]
    assert get_list_as_string(test_list) == "item1,item2,item3"


def test_get_list_as_string_empty_list_input():
    """Checks the behavior with an empty list, should return an empty string."""
    assert get_list_as_string([]) == ""


def test_get_list_as_string_invalid_input():
    """Checks the behavior with invalid input type, should raise InvalidArgumentException."""
    with pytest.raises(InvalidArgumentException):
        get_list_as_string(123)


def test_get_list_as_string_invalid_input_bool():
    """Checks the behavior with invalid boolean input, should raise InvalidArgumentException."""
    with pytest.raises(InvalidArgumentException):
        get_list_as_string(True)


def test_get_product_ids_valid_string_input(mocker):
    """Checks the behavior with a valid string input, should return a list of product IDs."""
    mock_get_product_id = mocker.patch(
        "hypotez.src.suppliers.aliexpress.api.helpers.arguments.get_product_id",
        side_effect=lambda x: f"id_{x}",
    )
    test_string = "item1,item2,item3"
    expected_ids = ["id_item1", "id_item2", "id_item3"]
    assert get_product_ids(test_string) == expected_ids
    mock_get_product_id.assert_called_with("item3")
    assert mock_get_product_id.call_count == 3


def test_get_product_ids_valid_list_input(mocker):
    """Checks the behavior with a valid list input, should return a list of product IDs."""
    mock_get_product_id = mocker.patch(
        "hypotez.src.suppliers.aliexpress.api.helpers.arguments.get_product_id",
        side_effect=lambda x: f"id_{x}",
    )
    test_list = ["item1", "item2", "item3"]
    expected_ids = ["id_item1", "id_item2", "id_item3"]
    assert get_product_ids(test_list) == expected_ids
    mock_get_product_id.assert_called_with("item3")
    assert mock_get_product_id.call_count == 3


def test_get_product_ids_empty_string_input(mocker):
    """Checks the behavior with an empty string, should return an empty list."""
    mock_get_product_id = mocker.patch(
        "hypotez.src.suppliers.aliexpress.api.helpers.arguments.get_product_id",
        side_effect=lambda x: f"id_{x}",
    )
    assert get_product_ids("") == ["id_"]
    mock_get_product_id.assert_called_once_with("")

def test_get_product_ids_empty_list_input(mocker):
    """Checks the behavior with an empty list, should return an empty list."""
    mock_get_product_id = mocker.patch(
        "hypotez.src.suppliers.aliexpress.api.helpers.arguments.get_product_id",
        side_effect=lambda x: f"id_{x}",
    )
    assert get_product_ids([]) == []
    mock_get_product_id.assert_not_called()



def test_get_product_ids_invalid_input():
    """Checks the behavior with invalid input type, should raise InvalidArgumentException."""
    with pytest.raises(InvalidArgumentException):
        get_product_ids(123)

def test_get_product_ids_invalid_input_bool():
    """Checks the behavior with invalid bool input type, should raise InvalidArgumentException."""
    with pytest.raises(InvalidArgumentException):
        get_product_ids(True)


def test_get_product_ids_string_with_spaces(mocker):
    """Checks the behavior with a string containing spaces before and after commas, should return a list of product IDs."""
    mock_get_product_id = mocker.patch(
        "hypotez.src.suppliers.aliexpress.api.helpers.arguments.get_product_id",
        side_effect=lambda x: f"id_{x.strip()}",
    )
    test_string = " item1 , item2 , item3 "
    expected_ids = ["id_item1", "id_item2", "id_item3"]
    assert get_product_ids(test_string) == expected_ids
    mock_get_product_id.assert_called_with(" item3 ")
    assert mock_get_product_id.call_count == 3
```