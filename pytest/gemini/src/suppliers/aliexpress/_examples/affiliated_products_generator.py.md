```python
import pytest
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from unittest.mock import patch
import requests
from io import BytesIO

# Fixture definitions
@pytest.fixture
def mock_ali_response():
    """Mocks the response from aliexpress API."""
    class MockResponse:
        def __init__(self, data, status_code):
            self.data = data
            self.status_code = status_code

        def json(self):
            return self.data
        
        def raise_for_status(self):
          if self.status_code >= 400:
            raise requests.exceptions.HTTPError(f"Error {self.status_code}")

    mock_data = {
      "result": {
        "promotionUrl": "https://s.click.aliexpress.com/e/_Ddtp42B",
        "productId": "123",
        "imageUrl": "https://ae01.alicdn.com/kf/S25c7048296c24012b195937784c2a9f2j.jpg",
        "videoUrl": "https://ae01.alicdn.com/kf/S25c7048296c24012b195937784c2a9f2j.mp4",
      }
    }

    return MockResponse(mock_data, 200)

@pytest.fixture
def mock_empty_ali_response():
    """Mocks the empty response from aliexpress API."""
    class MockResponse:
        def __init__(self, data, status_code):
            self.data = data
            self.status_code = status_code

        def json(self):
            return self.data
        def raise_for_status(self):
          if self.status_code >= 400:
            raise requests.exceptions.HTTPError(f"Error {self.status_code}")

    mock_data = {
      "result": None
    }

    return MockResponse(mock_data, 200)


@pytest.fixture
def mock_image_response():
    """Mocks image download response."""
    class MockResponse:
        def __init__(self, status_code, content=b'test_image_content'):
            self.status_code = status_code
            self.content = content

        def raise_for_status(self):
            if self.status_code >= 400:
                raise requests.exceptions.HTTPError(f"Error {self.status_code}")
    return MockResponse(200)

@pytest.fixture
def mock_video_response():
    """Mocks video download response."""
    class MockResponse:
        def __init__(self, status_code, content=b'test_video_content'):
            self.status_code = status_code
            self.content = content

        def raise_for_status(self):
            if self.status_code >= 400:
                raise requests.exceptions.HTTPError(f"Error {self.status_code}")

    return MockResponse(200)

@pytest.fixture
def parser():
    """Provides an instance of AliAffiliatedProducts class."""
    return AliAffiliatedProducts("test_campaign", "test_category", "EN", "USD")

# Tests for AliAffiliatedProducts class
def test_ali_affiliated_products_initialization():
    """Checks if AliAffiliatedProducts is initialized correctly."""
    parser = AliAffiliatedProducts("test_campaign", "test_category", "EN", "USD")
    assert parser.campaign_name == "test_campaign"
    assert parser.campaign_category == "test_category"
    assert parser.language == "EN"
    assert parser.currency == "USD"

def test_ali_affiliated_products_initialization_no_category():
    """Checks if AliAffiliatedProducts is initialized correctly when category is None."""
    parser = AliAffiliatedProducts("test_campaign", None, "EN", "USD")
    assert parser.campaign_name == "test_campaign"
    assert parser.campaign_category is None
    assert parser.language == "EN"
    assert parser.currency == "USD"


@patch('requests.get')
def test_process_affiliate_products_valid_urls(mock_get, parser, mock_ali_response, mock_image_response, mock_video_response):
    """Tests process_affiliate_products with valid URLs."""
    mock_get.side_effect = [mock_ali_response, mock_image_response, mock_video_response]
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
    ]
    products = parser.process_affiliate_products(prod_urls)
    assert len(products) == 2
    assert products[0].product_id == '123'
    assert products[0].promotion_link == "https://s.click.aliexpress.com/e/_Ddtp42B"
    assert products[1].product_id == '123'
    assert products[1].promotion_link == "https://s.click.aliexpress.com/e/_Ddtp42B"
    assert products[0].local_saved_image == "images/123.jpg"
    assert products[0].local_saved_video == "videos/123.mp4"


@patch('requests.get')
def test_process_affiliate_products_invalid_urls(mock_get, parser, mock_empty_ali_response, mock_image_response, mock_video_response):
    """Tests process_affiliate_products with invalid URLs."""
    mock_get.side_effect = [mock_empty_ali_response, mock_image_response, mock_video_response]
    prod_urls = [
        'invalid_id',
        'https://www.aliexpress.com/item/invalid_id.html',
    ]
    products = parser.process_affiliate_products(prod_urls)
    assert len(products) == 0


@patch('requests.get')
def test_process_affiliate_products_empty_list(mock_get, parser):
    """Tests process_affiliate_products with an empty list."""
    products = parser.process_affiliate_products([])
    assert len(products) == 0

@patch('requests.get')
def test_process_affiliate_products_api_error(mock_get, parser):
    """Tests process_affiliate_products with an API error."""
    mock_get.side_effect = requests.exceptions.HTTPError("API error")

    prod_urls = [
        '123',
    ]
    products = parser.process_affiliate_products(prod_urls)
    assert len(products) == 0

@patch('requests.get')
def test_download_image_success(mock_get, parser, mock_image_response):
     """Tests _download_image with valid URL."""
     mock_get.return_value = mock_image_response
     local_path = parser._download_image('https://example.com/test.jpg', '123')
     assert local_path == "images/123.jpg"

@patch('requests.get')
def test_download_image_failed(mock_get, parser):
    """Tests _download_image with an invalid url."""
    mock_get.side_effect = requests.exceptions.HTTPError("Image download error")
    local_path = parser._download_image("invalid_image_url", '123')
    assert local_path is None

@patch('requests.get')
def test_download_video_success(mock_get, parser, mock_video_response):
    """Tests _download_video with valid URL."""
    mock_get.return_value = mock_video_response
    local_path = parser._download_video('https://example.com/test.mp4', '123')
    assert local_path == "videos/123.mp4"

@patch('requests.get')
def test_download_video_failed(mock_get, parser):
    """Tests _download_video with an invalid url."""
    mock_get.side_effect = requests.exceptions.HTTPError("Video download error")
    local_path = parser._download_video("invalid_video_url", '123')
    assert local_path is None
```