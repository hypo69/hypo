```python
import pytest
from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateFeaturedpromoProductsGetRequest import AliexpressAffiliateFeaturedpromoProductsGetRequest

# Fixture for creating an instance of the class
@pytest.fixture
def api_request():
    """Provides an instance of AliexpressAffiliateFeaturedpromoProductsGetRequest for testing."""
    return AliexpressAffiliateFeaturedpromoProductsGetRequest()

def test_aliexpress_affiliate_featuredpromo_products_get_request_initialization(api_request):
    """
    Test that the AliexpressAffiliateFeaturedpromoProductsGetRequest class initializes correctly.
    Checks that all the attributes are initialized to None.
    """
    assert api_request.app_signature is None
    assert api_request.category_id is None
    assert api_request.country is None
    assert api_request.fields is None
    assert api_request.page_no is None
    assert api_request.page_size is None
    assert api_request.promotion_end_time is None
    assert api_request.promotion_name is None
    assert api_request.promotion_start_time is None
    assert api_request.sort is None
    assert api_request.target_currency is None
    assert api_request.target_language is None
    assert api_request.tracking_id is None

def test_aliexpress_affiliate_featuredpromo_products_get_request_default_domain_and_port(api_request):
    """
    Test the default domain and port are set correctly during initialization.
    """
    assert api_request.domain == "api-sg.aliexpress.com"
    assert api_request.port == 80


def test_aliexpress_affiliate_featuredpromo_products_get_request_custom_domain_and_port():
    """
    Test that the domain and port can be set during initialization.
    """
    custom_domain = "test.aliexpress.com"
    custom_port = 443
    api_request = AliexpressAffiliateFeaturedpromoProductsGetRequest(domain=custom_domain, port=custom_port)
    assert api_request.domain == custom_domain
    assert api_request.port == custom_port


def test_aliexpress_affiliate_featuredpromo_products_get_request_getapiname(api_request):
    """
    Test the `getapiname` method returns the correct API name.
    """
    api_name = api_request.getapiname()
    assert api_name == 'aliexpress.affiliate.featuredpromo.products.get'
```