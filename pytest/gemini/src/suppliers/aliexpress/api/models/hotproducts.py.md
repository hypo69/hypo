```python
import pytest
from typing import List
from hypotez.src.suppliers.aliexpress.api.models.hotproducts import HotProductsResponse
from hypotez.src.suppliers.aliexpress.api.models.product import Product  # Assuming Product class exists

@pytest.fixture
def sample_product():
    """Provides a sample Product object for testing."""
    return Product(
        product_id=123,
        product_title="Test Product",
        product_url="https://example.com/product/123",
        image_url="https://example.com/image1.jpg",
        price=10.00,
        discount=5.00
    )

@pytest.fixture
def sample_products(sample_product):
    """Provides a list of sample Product objects for testing."""
    return [sample_product, sample_product]

def test_hotproductsresponse_valid_data(sample_products):
    """Checks correct instantiation of HotProductsResponse with valid data."""
    response = HotProductsResponse()
    response.current_page_no = 1
    response.current_record_count = 2
    response.total_record_count = 10
    response.products = sample_products

    assert response.current_page_no == 1
    assert response.current_record_count == 2
    assert response.total_record_count == 10
    assert response.products == sample_products
    assert isinstance(response.products, List)
    assert all(isinstance(product, Product) for product in response.products)

def test_hotproductsresponse_empty_products():
    """Checks instantiation with an empty product list."""
    response = HotProductsResponse()
    response.current_page_no = 1
    response.current_record_count = 0
    response.total_record_count = 0
    response.products = []

    assert response.current_page_no == 1
    assert response.current_record_count == 0
    assert response.total_record_count == 0
    assert response.products == []
    assert isinstance(response.products, List)


def test_hotproductsresponse_no_products():
    """Checks instantiation with no products provided."""
    response = HotProductsResponse()
    response.current_page_no = 1
    response.current_record_count = 0
    response.total_record_count = 0
    response.products = None

    assert response.current_page_no == 1
    assert response.current_record_count == 0
    assert response.total_record_count == 0
    assert response.products is None

def test_hotproductsresponse_invalid_current_page_no():
    """Checks behavior with invalid page numbers"""
    response = HotProductsResponse()
    response.current_page_no = -1
    response.current_record_count = 0
    response.total_record_count = 0
    response.products = []

    assert response.current_page_no == -1
    assert response.current_record_count == 0
    assert response.total_record_count == 0
    assert response.products == []

def test_hotproductsresponse_invalid_current_record_count():
    """Checks behavior with invalid record counts"""
    response = HotProductsResponse()
    response.current_page_no = 1
    response.current_record_count = -1
    response.total_record_count = 0
    response.products = []

    assert response.current_page_no == 1
    assert response.current_record_count == -1
    assert response.total_record_count == 0
    assert response.products == []

def test_hotproductsresponse_invalid_total_record_count():
    """Checks behavior with invalid record counts"""
    response = HotProductsResponse()
    response.current_page_no = 1
    response.current_record_count = 0
    response.total_record_count = -1
    response.products = []

    assert response.current_page_no == 1
    assert response.current_record_count == 0
    assert response.total_record_count == -1
    assert response.products == []
```