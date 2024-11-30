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

# Fixtures (if needed)
@pytest.fixture
def example_products_data():
    return [
        {"id": 1, "name": "Product 1", "category": 101},
        {"id": 2, "name": "Product 2", "category": 102},
        {"id": 3, "name": "Product 3", "category": 101},
    ]


@pytest.fixture
def example_categories_data():
  return {
    "parent_categories": [{"id": 101, "name": "Category A"} , {"id": 102, "name": "Category B"}],
    "child_categories": [
        {"id": 201, "parent_id": 101, "name": "Subcategory 1"},
        {"id": 202, "parent_id": 101, "name": "Subcategory 2"},
        {"id": 203, "parent_id": 102, "name": "Subcategory 3"}
    ]
}



# Tests for api_request
def test_api_request_valid_response(monkeypatch):
  """Tests api_request with a valid mock response."""
  # Mock the requests library
  mock_response = {"products": [{"id": 1}]}  # Replace with actual expected response
  def mock_get(*args, **kwargs):
    return mock_response
  monkeypatch.setattr("requests.get", mock_get)

  result = api_request("some_url")
  assert result == mock_response

def test_api_request_invalid_response(monkeypatch):
    """Tests api_request with an invalid mock response."""
    # Mock an error response
    def mock_get(*args, **kwargs):
      raise Exception("Mock API Error")
    monkeypatch.setattr("requests.get", mock_get)
    with pytest.raises(Exception) as excinfo:
      api_request("some_url")
    assert "Mock API Error" in str(excinfo.value)


# Tests for other functions
def test_get_list_as_string_valid_input(example_products_data):
    """Tests get_list_as_string with valid input."""
    product_ids = [p["id"] for p in example_products_data]
    result = get_list_as_string(product_ids)
    assert result == "1,2,3"

def test_get_list_as_string_empty_input():
  """Tests get_list_as_string with empty input."""
  result = get_list_as_string([])
  assert result == ""

def test_get_product_ids_valid_input(example_products_data):
  """Tests get_product_ids with valid input."""
  products = example_products_data
  result = get_product_ids(products)
  assert result == [1, 2, 3]

def test_parse_products_valid_input(example_products_data):
  """Tests parse_products with valid input."""
  result = parse_products(example_products_data)
  assert result == example_products_data  # Check if the input is returned without modification



def test_filter_parent_categories_valid_input(example_categories_data):
    """Tests filter_parent_categories with valid input."""
    parent_categories = example_categories_data["parent_categories"]
    result = filter_parent_categories(parent_categories, [101])
    assert result == [{"id": 101, "name": "Category A"}]


def test_filter_parent_categories_invalid_input(example_categories_data):
  """Tests filter_parent_categories with invalid input (empty list)."""
  parent_categories = example_categories_data["parent_categories"]
  result = filter_parent_categories(parent_categories, [])
  assert result == []

def test_filter_child_categories_valid_input(example_categories_data):
  """Tests filter_child_categories with valid input."""
  child_categories = example_categories_data["child_categories"]
  result = filter_child_categories(child_categories, [101])
  assert result == [{"id": 201, "parent_id": 101, "name": "Subcategory 1"}, {"id": 202, "parent_id": 101, "name": "Subcategory 2"}]


# Add more test cases for other functions as needed (e.g., filter_child_categories)
```