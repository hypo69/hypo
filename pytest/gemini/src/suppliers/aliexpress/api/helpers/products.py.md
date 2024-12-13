```python
import pytest
from unittest.mock import MagicMock
from hypotez.src.suppliers.aliexpress.api.helpers.products import parse_product, parse_products


@pytest.fixture
def mock_product():
    """Provides a mock product object for testing."""
    product = MagicMock()
    product.product_small_image_urls = MagicMock()
    product.product_small_image_urls.string = "test_url"
    return product


@pytest.fixture
def mock_products():
    """Provides a list of mock product objects for testing."""
    product1 = MagicMock()
    product1.product_small_image_urls = MagicMock()
    product1.product_small_image_urls.string = "url1"

    product2 = MagicMock()
    product2.product_small_image_urls = MagicMock()
    product2.product_small_image_urls.string = "url2"

    return [product1, product2]



def test_parse_product_valid_input(mock_product):
    """Checks if parse_product correctly extracts and assigns the string value of product_small_image_urls."""
    result = parse_product(mock_product)
    assert result.product_small_image_urls == "test_url"


def test_parse_product_with_empty_string(mock_product):
    """Checks if parse_product handles an empty string for image urls correctly."""
    mock_product.product_small_image_urls.string = ""
    result = parse_product(mock_product)
    assert result.product_small_image_urls == ""


def test_parse_products_valid_input(mock_products):
    """Checks if parse_products correctly processes a list of products and returns a list of modified products."""
    result = parse_products(mock_products)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0].product_small_image_urls == "url1"
    assert result[1].product_small_image_urls == "url2"


def test_parse_products_empty_list():
    """Checks that parse_products handles an empty list correctly."""
    result = parse_products([])
    assert result == []

def test_parse_products_with_one_product(mock_product):
    """Checks if parse_products works correctly when only one product is in the list"""
    products_list = [mock_product]
    result = parse_products(products_list)
    assert len(result) == 1
    assert result[0].product_small_image_urls == "test_url"


def test_parse_products_with_none_input():
    """Checks that parse_products raises an error when input is None"""
    with pytest.raises(TypeError):
        parse_products(None)


def test_parse_product_with_none_input():
    """Checks that parse_product raises an error when input is None"""
    with pytest.raises(AttributeError):
        parse_product(None)
```