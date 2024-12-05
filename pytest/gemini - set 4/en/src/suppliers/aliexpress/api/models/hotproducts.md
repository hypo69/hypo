```python
import pytest
from hypotez.src.suppliers.aliexpress.api.models.hotproducts import HotProductsResponse
from hypotez.src.suppliers.aliexpress.api.models.product import Product  # Import Product
import typing


# Fixture for creating test data
@pytest.fixture
def example_product_data():
    """Provides test data for Product."""
    return Product(
        id=123,
        name="Test Product",
        price=19.99,
        image_url="https://example.com/image.jpg",
    )


@pytest.fixture
def example_hotproducts_data():
    """Provides test data for HotProductsResponse."""
    products = [
        pytest.param(example_product_data()),
        pytest.param(example_product_data()),
    ]
    return HotProductsResponse(
        current_page_no=1,
        current_record_count=2,
        total_record_count=100,
        products=products,
    )




# Tests for HotProductsResponse
def test_hotproductsresponse_valid_data(example_hotproducts_data):
    """Checks correct instantiation with valid data."""
    assert isinstance(example_hotproducts_data, HotProductsResponse)
    assert isinstance(example_hotproducts_data.products, list)  # Verify products is a list
    assert all(isinstance(p, Product) for p in example_hotproducts_data.products)  # Check if all items in the list are Product objects
    
def test_hotproductsresponse_empty_products(example_hotproducts_data):
    """Checks instantiation with an empty products list."""
    products_empty = []
    hotproducts_empty = HotProductsResponse(
        current_page_no=1,
        current_record_count=0,
        total_record_count=0,
        products=products_empty
    )
    assert isinstance(hotproducts_empty, HotProductsResponse)
    assert isinstance(hotproducts_empty.products, list) and len(hotproducts_empty.products) == 0 # Check for empty list

def test_hotproductsresponse_invalid_products_type():
    """Checks for correct exception when products is not a list."""
    with pytest.raises(TypeError):
        HotProductsResponse(
            current_page_no=1,
            current_record_count=2,
            total_record_count=100,
            products=123,  # Invalid type
        )


def test_hotproductsresponse_missing_products():
    """Checks for exception when products is missing."""
    with pytest.raises(TypeError):
        HotProductsResponse(
            current_page_no=1,
            current_record_count=2,
            total_record_count=100,
        )

def test_hotproductsresponse_invalid_data_types():
    """Checks if data types for other fields are valid."""
    with pytest.raises(TypeError):
        HotProductsResponse(
            current_page_no="invalid",  # Invalid type
            current_record_count=2,
            total_record_count=100,
            products=[],
        )
    with pytest.raises(TypeError):
        HotProductsResponse(
            current_page_no=1,
            current_record_count="invalid",  # Invalid type
            total_record_count=100,
            products=[],
        )
    with pytest.raises(TypeError):
        HotProductsResponse(
            current_page_no=1,
            current_record_count=2,
            total_record_count="invalid",  # Invalid type
            products=[],
        )


```