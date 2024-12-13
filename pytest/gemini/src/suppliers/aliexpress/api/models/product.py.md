```python
import pytest
from hypotez.src.suppliers.aliexpress.api.models.product import Product
from typing import List

@pytest.fixture
def valid_product_data():
    """Provides valid data for creating a Product instance."""
    return {
        "app_sale_price": "10.00",
        "app_sale_price_currency": "USD",
        "commission_rate": "0.05",
        "discount": "0.1",
        "evaluate_rate": "4.5",
        "first_level_category_id": 1,
        "first_level_category_name": "Electronics",
        "lastest_volume": 100,
        "hot_product_commission_rate": "0.06",
        "original_price": "12.00",
        "original_price_currency": "USD",
        "product_detail_url": "https://example.com/product/123",
        "product_id": 123,
        "product_main_image_url": "https://example.com/image1.jpg",
        "product_small_image_urls": ["https://example.com/image1_small.jpg", "https://example.com/image2_small.jpg"],
        "product_title": "Test Product",
        "product_video_url": "https://example.com/video.mp4",
        "promotion_link": "https://example.com/promotion/123",
        "relevant_market_commission_rate": "0.04",
        "sale_price": "11.00",
        "sale_price_currency": "USD",
        "second_level_category_id": 2,
        "second_level_category_name": "Mobile Phones",
        "shop_id": 456,
        "shop_url": "https://example.com/shop/456",
        "target_app_sale_price": "9.50",
        "target_app_sale_price_currency": "USD",
        "target_original_price": "11.50",
        "target_original_price_currency": "USD",
        "target_sale_price": "10.50",
        "target_sale_price_currency": "USD"
    }


def test_product_creation_with_valid_data(valid_product_data):
    """Tests that a Product object can be created with valid data."""
    product = Product(**valid_product_data)
    assert product.app_sale_price == "10.00"
    assert product.app_sale_price_currency == "USD"
    assert product.commission_rate == "0.05"
    assert product.discount == "0.1"
    assert product.evaluate_rate == "4.5"
    assert product.first_level_category_id == 1
    assert product.first_level_category_name == "Electronics"
    assert product.lastest_volume == 100
    assert product.hot_product_commission_rate == "0.06"
    assert product.original_price == "12.00"
    assert product.original_price_currency == "USD"
    assert product.product_detail_url == "https://example.com/product/123"
    assert product.product_id == 123
    assert product.product_main_image_url == "https://example.com/image1.jpg"
    assert product.product_small_image_urls == ["https://example.com/image1_small.jpg", "https://example.com/image2_small.jpg"]
    assert product.product_title == "Test Product"
    assert product.product_video_url == "https://example.com/video.mp4"
    assert product.promotion_link == "https://example.com/promotion/123"
    assert product.relevant_market_commission_rate == "0.04"
    assert product.sale_price == "11.00"
    assert product.sale_price_currency == "USD"
    assert product.second_level_category_id == 2
    assert product.second_level_category_name == "Mobile Phones"
    assert product.shop_id == 456
    assert product.shop_url == "https://example.com/shop/456"
    assert product.target_app_sale_price == "9.50"
    assert product.target_app_sale_price_currency == "USD"
    assert product.target_original_price == "11.50"
    assert product.target_original_price_currency == "USD"
    assert product.target_sale_price == "10.50"
    assert product.target_sale_price_currency == "USD"


def test_product_creation_with_empty_list_of_images(valid_product_data):
    """Tests product creation with empty image URL list"""
    valid_product_data["product_small_image_urls"] = []
    product = Product(**valid_product_data)
    assert product.product_small_image_urls == []
    

def test_product_creation_with_missing_data():
    """Tests that TypeError is raised when data is missing during Product initialization."""
    with pytest.raises(TypeError):
        Product(app_sale_price="10.00")


def test_product_creation_with_invalid_data_type():
    """Tests that TypeError is raised when invalid type is passed for an attribute"""
    with pytest.raises(TypeError):
        Product(app_sale_price=10.00,
                app_sale_price_currency="USD",
                commission_rate="0.05",
                discount="0.1",
                evaluate_rate="4.5",
                first_level_category_id=1,
                first_level_category_name="Electronics",
                lastest_volume=100,
                hot_product_commission_rate="0.06",
                original_price="12.00",
                original_price_currency="USD",
                product_detail_url="https://example.com/product/123",
                product_id=123,
                product_main_image_url="https://example.com/image1.jpg",
                product_small_image_urls=["https://example.com/image1_small.jpg", "https://example.com/image2_small.jpg"],
                product_title="Test Product",
                product_video_url="https://example.com/video.mp4",
                promotion_link="https://example.com/promotion/123",
                relevant_market_commission_rate="0.04",
                sale_price="11.00",
                sale_price_currency="USD",
                second_level_category_id=2,
                second_level_category_name="Mobile Phones",
                shop_id=456,
                shop_url="https://example.com/shop/456",
                target_app_sale_price="9.50",
                target_app_sale_price_currency="USD",
                target_original_price="11.50",
                target_original_price_currency="USD",
                target_sale_price="10.50",
                target_sale_price_currency="USD",
                product_id = "123",
                )
```