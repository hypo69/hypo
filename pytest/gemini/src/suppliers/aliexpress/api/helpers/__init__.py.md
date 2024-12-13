```python
import pytest

from hypotez.src.suppliers.aliexpress.api.helpers import (
    api_request,
    get_list_as_string,
    get_product_ids,
    parse_products,
    filter_parent_categories,
    filter_child_categories,
)


# Fixture definitions (if needed, add here, example below)
@pytest.fixture
def example_product_list():
    """Provides a list of example products"""
    return [
        {"productId": 123, "title": "Product 1"},
        {"productId": 456, "title": "Product 2"},
        {"productId": 789, "title": "Product 3"},
    ]


@pytest.fixture
def example_category_list():
    """Provides a list of example categories."""
    return [
        {"id": 1, "parentId": 0, "name": "Category 1"},
        {"id": 2, "parentId": 1, "name": "Category 2"},
        {"id": 3, "parentId": 0, "name": "Category 3"},
        {"id": 4, "parentId": 2, "name": "Category 4"},
    ]


# Tests for api_request (assuming the actual implementation makes HTTP requests)
# Mocking would be appropriate if we want to test the api_request function directly
# Example:
# def test_api_request_successful():
#     # Mock HTTP request to return a successful response
#     pass

# def test_api_request_failure():
#     # Mock HTTP request to simulate a failure
#     pass


# Tests for get_list_as_string
def test_get_list_as_string_valid_list():
    """Checks that a valid list is correctly converted to a string"""
    test_list = ["apple", "banana", "cherry"]
    expected_string = "apple,banana,cherry"
    assert get_list_as_string(test_list) == expected_string


def test_get_list_as_string_empty_list():
    """Checks that an empty list returns an empty string."""
    test_list = []
    expected_string = ""
    assert get_list_as_string(test_list) == expected_string


def test_get_list_as_string_list_of_numbers():
    """Checks that a list of numbers is correctly converted to a string."""
    test_list = [1, 2, 3]
    expected_string = "1,2,3"
    assert get_list_as_string(test_list) == expected_string


def test_get_list_as_string_list_with_mixed_types():
    """Checks that a list with mixed types is correctly converted to a string."""
    test_list = [1, "apple", 3.14]
    expected_string = "1,apple,3.14"
    assert get_list_as_string(test_list) == expected_string


def test_get_list_as_string_none_input():
    """Checks that None input returns an empty string."""
    assert get_list_as_string(None) == ""


# Tests for get_product_ids
def test_get_product_ids_valid_products(example_product_list):
    """Checks that a valid product list returns a list of ids."""
    expected_ids = [123, 456, 789]
    assert get_product_ids(example_product_list) == expected_ids


def test_get_product_ids_empty_products():
    """Checks that an empty product list returns an empty list."""
    assert get_product_ids([]) == []


def test_get_product_ids_missing_id():
    """Checks that product without id are skipped."""
    products = [
        {"productId": 123},
        {"title": "Product 2"},  # Missing productId
        {"productId": 789},
    ]
    assert get_product_ids(products) == [123, 789]


def test_get_product_ids_none_products():
    """Checks that None input returns an empty list."""
    assert get_product_ids(None) == []


# Tests for parse_products (assuming it takes some data and returnes parsed data)
def test_parse_products_valid_data():
    """Checks that a valid data input is handled."""
    # Given a valid input, ensure some structure is handled as expected.
    # The exact validation needs to follow the function implementation
    # This is an example and should be adapted to the function logic
    test_data = [{"item": "value"}]
    assert isinstance(parse_products(test_data), list)


def test_parse_products_empty_data():
    """Checks that empty data returns an empty list."""
    assert parse_products([]) == []


def test_parse_products_none_data():
    """Checks that None input returns an empty list."""
    assert parse_products(None) == []


# Tests for filter_parent_categories
def test_filter_parent_categories_valid_categories(example_category_list):
    """Checks that valid parent categories are filtered out."""
    expected_parent_ids = [1, 3]
    parent_categories = filter_parent_categories(example_category_list)
    assert [cat["id"] for cat in parent_categories] == expected_parent_ids


def test_filter_parent_categories_empty_categories():
    """Checks an empty list of categories."""
    assert filter_parent_categories([]) == []


def test_filter_parent_categories_no_parent():
    """Checks categories without parents."""
    categories = [{"id": 1, "parentId": 1}, {"id": 2, "parentId": 2}]
    assert filter_parent_categories(categories) == []


def test_filter_parent_categories_none_input():
    """Checks if None input returns an empty list"""
    assert filter_parent_categories(None) == []


# Tests for filter_child_categories
def test_filter_child_categories_valid_categories(example_category_list):
    """Checks that valid child categories are filtered out."""
    expected_child_ids = [2, 4]
    child_categories = filter_child_categories(example_category_list)
    assert [cat["id"] for cat in child_categories] == expected_child_ids


def test_filter_child_categories_empty_categories():
    """Checks an empty list of categories."""
    assert filter_child_categories([]) == []


def test_filter_child_categories_no_child():
    """Checks categories without children."""
    categories = [{"id": 1, "parentId": 0}, {"id": 2, "parentId": 0}]
    assert filter_child_categories(categories) == []


def test_filter_child_categories_none_input():
    """Checks if None input returns an empty list."""
    assert filter_child_categories(None) == []
```