```python
import pytest
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from unittest.mock import patch, MagicMock
from dataclasses import dataclass
from typing import List, Optional
import os


@dataclass
class MockProduct:
    product_id: str
    promotion_link: Optional[str] = None
    local_image_path: Optional[str] = None
    local_video_path: Optional[str] = None


@pytest.fixture
def mock_ali_affiliated_products():
    """Mocks the AliAffiliatedProducts class for testing."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts') as mock:
        yield mock


@pytest.fixture
def example_products():
    """Provides test data for the product processing."""
    return [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]


def test_ali_affiliated_products_initialization():
    """Checks if AliAffiliatedProducts initializes correctly."""
    campaign_name = "test_campaign"
    campaign_category = "test_category"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)

    assert parser.campaign_name == campaign_name
    assert parser.campaign_category == campaign_category
    assert parser.language == language
    assert parser.currency == currency


def test_process_affiliate_products_valid_input(mock_ali_affiliated_products, example_products):
    """Checks correct processing of valid product URLs and IDs."""
    mock_instance = mock_ali_affiliated_products.return_value
    mock_instance.process_product.side_effect = lambda url: MockProduct(product_id=url.replace('https://www.aliexpress.com/item/', '').replace('.html', ''), promotion_link=f"affiliate_link_{url}", local_image_path=f"image_{url}.jpg", local_video_path=f"video_{url}.mp4") if 'https' in url else MockProduct(product_id=url, promotion_link=f"affiliate_link_{url}", local_image_path=f"image_{url}.jpg", local_video_path=f"video_{url}.mp4")
    
    campaign_name = "test_campaign"
    campaign_category = "test_category"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
    products = parser.process_affiliate_products(example_products)

    assert len(products) == 4
    assert products[0].product_id == '123'
    assert products[1].product_id == '123'
    assert products[2].product_id == '456'
    assert products[3].product_id == '456'
    assert products[0].promotion_link == "affiliate_link_123"
    assert products[1].promotion_link == "affiliate_link_https://www.aliexpress.com/item/123.html"
    assert products[2].promotion_link == "affiliate_link_456"
    assert products[3].promotion_link == "affiliate_link_https://www.aliexpress.com/item/456.html"
    assert products[0].local_image_path == "image_123.jpg"
    assert products[1].local_image_path == "image_https://www.aliexpress.com/item/123.html.jpg"
    assert products[2].local_image_path == "image_456.jpg"
    assert products[3].local_image_path == "image_https://www.aliexpress.com/item/456.html.jpg"
    assert products[0].local_video_path == "video_123.mp4"
    assert products[1].local_video_path == "video_https://www.aliexpress.com/item/123.html.mp4"
    assert products[2].local_video_path == "video_456.mp4"
    assert products[3].local_video_path == "video_https://www.aliexpress.com/item/456.html.mp4"


def test_process_affiliate_products_empty_input():
    """Checks behavior with an empty list of product URLs/IDs."""
    campaign_name = "test_campaign"
    campaign_category = "test_category"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
    products = parser.process_affiliate_products([])
    assert products == []


def test_process_affiliate_products_invalid_url(mock_ali_affiliated_products):
    """Checks behavior with invalid product URLs."""
    mock_instance = mock_ali_affiliated_products.return_value
    mock_instance.process_product.side_effect = lambda url: None if 'invalid' in url else MockProduct(product_id=url, promotion_link=f"affiliate_link_{url}", local_image_path=f"image_{url}.jpg", local_video_path=f"video_{url}.mp4")
    
    campaign_name = "test_campaign"
    campaign_category = "test_category"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
    products = parser.process_affiliate_products(['123', 'invalid_url', '456'])
    
    assert len(products) == 2
    assert products[0].product_id == '123'
    assert products[1].product_id == '456'
    

def test_process_product_with_id_only(mock_ali_affiliated_products):
    """Checks correct handling of a product ID without a full URL."""
    mock_instance = mock_ali_affiliated_products.return_value
    mock_instance.process_product.return_value = MockProduct(product_id='123', promotion_link='test_link', local_image_path='image_path', local_video_path='video_path')
    
    campaign_name = "test_campaign"
    campaign_category = "test_category"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
    product = parser.process_product('123')

    assert product.product_id == '123'
    assert product.promotion_link == 'test_link'
    assert product.local_image_path == 'image_path'
    assert product.local_video_path == 'video_path'
    mock_instance.process_product.assert_called_once_with('123')


def test_process_product_with_url(mock_ali_affiliated_products):
    """Checks correct handling of a product URL."""
    mock_instance = mock_ali_affiliated_products.return_value
    mock_instance.process_product.return_value = MockProduct(product_id='123', promotion_link='test_link', local_image_path='image_path', local_video_path='video_path')

    campaign_name = "test_campaign"
    campaign_category = "test_category"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
    product = parser.process_product('https://www.aliexpress.com/item/123.html')

    assert product.product_id == '123'
    assert product.promotion_link == 'test_link'
    assert product.local_image_path == 'image_path'
    assert product.local_video_path == 'video_path'
    mock_instance.process_product.assert_called_once_with('https://www.aliexpress.com/item/123.html')


def test_process_product_with_no_promotion_link(mock_ali_affiliated_products):
    """Checks handling when a promotion link is not found for the product."""
    mock_instance = mock_ali_affiliated_products.return_value
    mock_instance.process_product.return_value = MockProduct(product_id='123', local_image_path='image_path', local_video_path='video_path')
    
    campaign_name = "test_campaign"
    campaign_category = "test_category"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
    product = parser.process_product('123')

    assert product.product_id == '123'
    assert product.promotion_link is None
    assert product.local_image_path == 'image_path'
    assert product.local_video_path == 'video_path'

def test_process_product_no_media(mock_ali_affiliated_products):
    """Checks handling of a product without any media files."""
    mock_instance = mock_ali_affiliated_products.return_value
    mock_instance.process_product.return_value = MockProduct(product_id='123', promotion_link='test_link')
    
    campaign_name = "test_campaign"
    campaign_category = "test_category"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
    product = parser.process_product('123')

    assert product.product_id == '123'
    assert product.promotion_link == 'test_link'
    assert product.local_image_path is None
    assert product.local_video_path is None
    

def test_process_product_exception(mock_ali_affiliated_products):
    """Checks exception handling during processing of a product."""
    mock_instance = mock_ali_affiliated_products.return_value
    mock_instance.process_product.side_effect = Exception("Failed to process product")
    
    campaign_name = "test_campaign"
    campaign_category = "test_category"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
    
    with pytest.raises(Exception, match="Failed to process product"):
        parser.process_product('123')
```