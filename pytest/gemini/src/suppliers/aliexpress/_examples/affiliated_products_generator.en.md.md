```python
import pytest
from unittest.mock import patch, MagicMock
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.suppliers.aliexpress.schemas import AliProduct


@pytest.fixture
def mock_ali_product():
    """Provides a mock AliProduct object for testing."""
    return AliProduct(
        product_id='123',
        promotion_link='https://example.com/affiliate/123',
        local_saved_image='path/to/image.jpg',
        local_saved_video='path/to/video.mp4'
    )


@pytest.fixture
def mock_ali_products_list(mock_ali_product):
    """Provides a list of mock AliProduct objects for testing."""
    return [mock_ali_product, mock_ali_product]


@pytest.fixture
def ali_affiliate_parser():
    """Provides an instance of AliAffiliatedProducts for testing."""
    return AliAffiliatedProducts("test_campaign", "test_category", "EN", "USD")


def test_ali_affiliated_products_init(ali_affiliate_parser):
    """Checks if AliAffiliatedProducts initializes correctly."""
    assert ali_affiliate_parser.campaign_name == "test_campaign"
    assert ali_affiliate_parser.campaign_category == "test_category"
    assert ali_affiliate_parser.language == "EN"
    assert ali_affiliate_parser.currency == "USD"


@patch("src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts._fetch_product_data")
@patch("src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts._save_media")
@patch("src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts._create_affiliate_link")
def test_process_affiliate_products_valid_input(
    mock_create_affiliate_link,
    mock_save_media,
    mock_fetch_product_data,
    ali_affiliate_parser,
    mock_ali_products_list,
):
    """
    Checks correct behavior with valid product IDs and URLs.
    Mocks the internal methods to avoid external API calls and file system operations.
    """
    mock_fetch_product_data.side_effect = lambda x: mock_ali_products_list[0] if '123' in x else mock_ali_products_list[1]
    mock_save_media.return_value = "path/to/saved/media"
    mock_create_affiliate_link.return_value = "https://example.com/affiliate/link"
    
    prod_urls = ['123', 'https://www.aliexpress.com/item/456.html']
    products = ali_affiliate_parser.process_affiliate_products(prod_urls)
    
    assert len(products) == 2
    for product in products:
        assert isinstance(product, AliProduct)
        assert product.promotion_link == "https://example.com/affiliate/link"
        assert product.local_saved_image == "path/to/saved/media"
        
    mock_fetch_product_data.assert_called()
    mock_save_media.assert_called()
    mock_create_affiliate_link.assert_called()


@patch("src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts._fetch_product_data")
def test_process_affiliate_products_empty_input(mock_fetch_product_data, ali_affiliate_parser):
    """Checks correct handling of an empty list of product URLs."""
    products = ali_affiliate_parser.process_affiliate_products([])
    assert products == []
    mock_fetch_product_data.assert_not_called()


@patch("src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts._fetch_product_data")
def test_process_affiliate_products_invalid_input(mock_fetch_product_data, ali_affiliate_parser):
    """
    Checks correct handling of invalid product URLs or IDs.
    Mocks `_fetch_product_data` to return None to simulate a product not found scenario.
    """
    mock_fetch_product_data.return_value = None
    prod_urls = ['invalid_id', 'https://www.aliexpress.com/item/invalid_url.html']
    products = ali_affiliate_parser.process_affiliate_products(prod_urls)
    assert products == []
    mock_fetch_product_data.assert_called()

@patch("src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts._fetch_product_data")
@patch("src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts._save_media")
@patch("src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts._create_affiliate_link")
def test_process_affiliate_products_mixed_input(
    mock_create_affiliate_link,
    mock_save_media,
    mock_fetch_product_data,
    ali_affiliate_parser,
    mock_ali_products_list,
):
    """
    Checks correct behavior with a mix of valid and invalid product IDs and URLs.
    Mocks the internal methods to control the behavior of valid/invalid product processing.
    """
    def side_effect(url):
      if '123' in url or '456' in url:
        return mock_ali_products_list[0]
      return None
    mock_fetch_product_data.side_effect = side_effect
    mock_save_media.return_value = "path/to/saved/media"
    mock_create_affiliate_link.return_value = "https://example.com/affiliate/link"
    prod_urls = ['123', 'invalid_id', 'https://www.aliexpress.com/item/456.html', 'https://www.aliexpress.com/item/invalid_url.html']
    products = ali_affiliate_parser.process_affiliate_products(prod_urls)
    assert len(products) == 2
    for product in products:
        assert isinstance(product, AliProduct)
        assert product.promotion_link == "https://example.com/affiliate/link"
        assert product.local_saved_image == "path/to/saved/media"
    mock_fetch_product_data.assert_called()
    mock_save_media.assert_called()
    mock_create_affiliate_link.assert_called()
```