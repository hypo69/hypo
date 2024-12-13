```python
import pytest
from unittest.mock import MagicMock, patch

from src.suppliers.aliexpress.api.api import AliexpressApi
from src.suppliers.aliexpress.api.models import (
    AffiliateLink,
    Category,
    ChildCategory,
    Currency,
    HotProductsResponse,
    Language,
    LinkType,
    Product,
    ProductType,
    SortBy,
)
from src.suppliers.aliexpress.api.errors.exceptions import (
    CategoriesNotFoudException,
    ProductsNotFoudException,
    InvalidTrackingIdException,
)

# Mock necessary modules and classes
@pytest.fixture
def mock_api_request():
    with patch('src.suppliers.aliexpress.api.api.api_request') as mock:
        yield mock

@pytest.fixture
def mock_aliapi_rest():
    with patch('src.suppliers.aliexpress.api.api.aliapi.rest') as mock:
         yield mock

@pytest.fixture
def mock_logger():
    with patch('src.suppliers.aliexpress.api.api.logger') as mock:
        yield mock

@pytest.fixture
def aliexpress_api():
    return AliexpressApi(
        key="test_key",
        secret="test_secret",
        language=Language.EN,
        currency=Currency.USD,
        tracking_id="test_tracking_id",
        app_signature="test_signature"
    )


class MockResponse:
        def __init__(self, total_result_count=0, current_record_count=0, products=None, categories=None, promotion_links=None):
            self.total_result_count = total_result_count
            self.current_record_count = current_record_count
            self.products = products or MagicMock()
            self.categories = categories or MagicMock()
            self.promotion_links = promotion_links or MagicMock()

@pytest.fixture
def mock_product():
    return MagicMock(spec=Product)

@pytest.fixture
def mock_affiliate_link():
    return MagicMock(spec=AffiliateLink)


def test_aliexpress_api_initialization(aliexpress_api):
    """Test the initialization of the AliexpressApi class."""
    assert aliexpress_api._key == "test_key"
    assert aliexpress_api._secret == "test_secret"
    assert aliexpress_api._tracking_id == "test_tracking_id"
    assert aliexpress_api._language == Language.EN
    assert aliexpress_api._currency == Currency.USD
    assert aliexpress_api._app_signature == "test_signature"
    assert aliexpress_api.categories is None


def test_retrieve_product_details_valid_input(aliexpress_api, mock_api_request, mock_aliapi_rest, mock_product):
    """Test retrieving product details with valid input."""
    mock_response = MockResponse(current_record_count=1, products=MagicMock(product=[mock_product]))
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateProductdetailGetRequest.return_value = MagicMock()

    products = aliexpress_api.retrieve_product_details(product_ids="12345", fields=["title", "price"])

    assert isinstance(products, list)
    assert len(products) == 1
    # assert isinstance(products[0], Product)

    mock_aliapi_rest.AliexpressAffiliateProductdetailGetRequest.assert_called_once()
    mock_api_request.assert_called_once()

def test_retrieve_product_details_no_products_found(aliexpress_api, mock_api_request, mock_aliapi_rest, mock_logger):
    """Test retrieving product details when no products are found."""
    mock_response = MockResponse()
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateProductdetailGetRequest.return_value = MagicMock()

    products = aliexpress_api.retrieve_product_details(product_ids="12345")

    assert products is None
    mock_logger.warning.assert_called_once_with('No products found with current parameters')
    mock_aliapi_rest.AliexpressAffiliateProductdetailGetRequest.assert_called_once()
    mock_api_request.assert_called_once()



def test_retrieve_product_details_exception(aliexpress_api, mock_api_request, mock_aliapi_rest, mock_logger):
    """Test retrieving product details when an exception occurs."""
    mock_api_request.return_value = MockResponse(current_record_count=1, products=MagicMock(product=[MagicMock()]))
    mock_aliapi_rest.AliexpressAffiliateProductdetailGetRequest.return_value = MagicMock()
    mock_api_request.side_effect = Exception("Test Exception")

    products = aliexpress_api.retrieve_product_details(product_ids="12345")

    assert products is None
    mock_logger.error.assert_called_once()
    mock_aliapi_rest.AliexpressAffiliateProductdetailGetRequest.assert_called_once()
    mock_api_request.assert_called_once()


def test_get_affiliate_links_valid_input(aliexpress_api, mock_api_request, mock_aliapi_rest, mock_affiliate_link):
    """Test getting affiliate links with valid input."""
    mock_response = MockResponse(total_result_count=1, promotion_links=MagicMock(promotion_link=[mock_affiliate_link]))
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateLinkGenerateRequest.return_value = MagicMock()

    links = aliexpress_api.get_affiliate_links(links=["https://test.com"])

    assert isinstance(links, list)
    assert len(links) == 1
    # assert isinstance(links[0], AffiliateLink)
    mock_aliapi_rest.AliexpressAffiliateLinkGenerateRequest.assert_called_once()
    mock_api_request.assert_called_once()



def test_get_affiliate_links_invalid_tracking_id(aliexpress_api, mock_logger):
    """Test getting affiliate links when tracking ID is missing."""
    aliexpress_api._tracking_id = None

    links = aliexpress_api.get_affiliate_links(links=["https://test.com"])

    assert links is None
    mock_logger.error.assert_called_once_with('The tracking id is required for affiliate links')


def test_get_affiliate_links_no_links_found(aliexpress_api, mock_api_request, mock_aliapi_rest, mock_logger):
    """Test getting affiliate links when no links are found."""
    mock_response = MockResponse()
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateLinkGenerateRequest.return_value = MagicMock()

    links = aliexpress_api.get_affiliate_links(links=["https://test.com"])

    assert links is None
    mock_logger.warning.assert_called_once_with('Affiliate links not available')
    mock_aliapi_rest.AliexpressAffiliateLinkGenerateRequest.assert_called_once()
    mock_api_request.assert_called_once()


def test_get_hotproducts_valid_input(aliexpress_api, mock_api_request, mock_aliapi_rest, mock_product):
    """Test getting hot products with valid input."""
    mock_response = MockResponse(current_record_count=1, products=MagicMock(product=[mock_product]))
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateHotproductQueryRequest.return_value = MagicMock()

    hot_products = aliexpress_api.get_hotproducts(category_ids="123", page_size=10)

    assert isinstance(hot_products, MockResponse)
    assert hot_products.products is not None
    mock_aliapi_rest.AliexpressAffiliateHotproductQueryRequest.assert_called_once()
    mock_api_request.assert_called_once()


def test_get_hotproducts_no_products_found(aliexpress_api, mock_api_request, mock_aliapi_rest):
    """Test getting hot products when no products are found."""
    mock_response = MockResponse()
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateHotproductQueryRequest.return_value = MagicMock()

    with pytest.raises(ProductsNotFoudException):
       aliexpress_api.get_hotproducts(category_ids="123", page_size=10)
    mock_aliapi_rest.AliexpressAffiliateHotproductQueryRequest.assert_called_once()
    mock_api_request.assert_called_once()

def test_get_categories_valid_response(aliexpress_api, mock_api_request, mock_aliapi_rest):
    """Test getting categories with a valid response."""
    mock_response = MockResponse(total_result_count=1, categories=MagicMock(category=[MagicMock()]))
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.return_value = MagicMock()

    categories = aliexpress_api.get_categories()

    assert isinstance(categories, list)
    assert len(categories) == 1
    assert aliexpress_api.categories is not None
    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.assert_called_once()
    mock_api_request.assert_called_once()

def test_get_categories_no_categories_found(aliexpress_api, mock_api_request, mock_aliapi_rest):
    """Test getting categories when no categories are found."""
    mock_response = MockResponse()
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.return_value = MagicMock()

    with pytest.raises(CategoriesNotFoudException):
        aliexpress_api.get_categories()

    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.assert_called_once()
    mock_api_request.assert_called_once()

def test_get_parent_categories_with_cache(aliexpress_api, mock_api_request, mock_aliapi_rest):
    """Test getting parent categories using the cache."""
    mock_category1 = MagicMock(spec=Category, parent_category_id=0)
    mock_category2 = MagicMock(spec=Category, parent_category_id=1)
    aliexpress_api.categories = [mock_category1, mock_category2]

    parent_categories = aliexpress_api.get_parent_categories()

    assert isinstance(parent_categories, list)
    assert len(parent_categories) == 1
    assert parent_categories[0].parent_category_id == 0
    mock_api_request.assert_not_called()  # Ensure get_categories is not called when using cache
    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.assert_not_called()

def test_get_parent_categories_no_cache(aliexpress_api, mock_api_request, mock_aliapi_rest):
    """Test getting parent categories without using the cache."""
    mock_response = MockResponse(total_result_count=1, categories=MagicMock(category=[MagicMock(parent_category_id=0), MagicMock(parent_category_id=1)]))
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.return_value = MagicMock()
    
    parent_categories = aliexpress_api.get_parent_categories(use_cache=False)

    assert isinstance(parent_categories, list)
    assert len(parent_categories) == 1
    assert parent_categories[0].parent_category_id == 0
    mock_api_request.assert_called_once()
    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.assert_called_once()



def test_get_child_categories_with_cache(aliexpress_api, mock_api_request, mock_aliapi_rest):
    """Test getting child categories using the cache."""
    mock_category1 = MagicMock(spec=Category, parent_category_id=0, id=1)
    mock_category2 = MagicMock(spec=ChildCategory, parent_category_id=1, id=2)
    mock_category3 = MagicMock(spec=ChildCategory, parent_category_id=1, id=3)
    aliexpress_api.categories = [mock_category1, mock_category2, mock_category3]

    child_categories = aliexpress_api.get_child_categories(parent_category_id=1)

    assert isinstance(child_categories, list)
    assert len(child_categories) == 2
    assert child_categories[0].parent_category_id == 1
    mock_api_request.assert_not_called()
    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.assert_not_called()


def test_get_child_categories_no_cache(aliexpress_api, mock_api_request, mock_aliapi_rest):
    """Test getting child categories without using the cache."""
    mock_response = MockResponse(total_result_count=1, categories=MagicMock(category=[
        MagicMock(parent_category_id=0, id=1),
        MagicMock(parent_category_id=1, id=2),
        MagicMock(parent_category_id=1, id=3)
    ]))
    mock_api_request.return_value = mock_response
    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.return_value = MagicMock()

    child_categories = aliexpress_api.get_child_categories(parent_category_id=1, use_cache=False)

    assert isinstance(child_categories, list)
    assert len(child_categories) == 2
    assert child_categories[0].parent_category_id == 1
    mock_api_request.assert_called_once()
    mock_aliapi_rest.AliexpressAffiliateCategoryGetRequest.assert_called_once()
```