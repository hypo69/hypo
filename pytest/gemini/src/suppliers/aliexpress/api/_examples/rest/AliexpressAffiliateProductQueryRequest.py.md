```python
import pytest
from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateProductQueryRequest import AliexpressAffiliateProductQueryRequest

# Fixture for creating an instance of AliexpressAffiliateProductQueryRequest
@pytest.fixture
def api_request():
    """Provides an instance of AliexpressAffiliateProductQueryRequest for testing."""
    return AliexpressAffiliateProductQueryRequest()

def test_aliexpress_affiliate_product_query_request_initialization(api_request):
    """
    Test the initialization of the AliexpressAffiliateProductQueryRequest class.
    Checks if all attributes are initialized to None by default.
    """
    assert api_request.app_signature is None
    assert api_request.category_ids is None
    assert api_request.delivery_days is None
    assert api_request.fields is None
    assert api_request.keywords is None
    assert api_request.max_sale_price is None
    assert api_request.min_sale_price is None
    assert api_request.page_no is None
    assert api_request.page_size is None
    assert api_request.platform_product_type is None
    assert api_request.ship_to_country is None
    assert api_request.sort is None
    assert api_request.target_currency is None
    assert api_request.target_language is None
    assert api_request.tracking_id is None

def test_aliexpress_affiliate_product_query_request_default_domain_and_port():
    """
    Test if the AliexpressAffiliateProductQueryRequest class is initialized with the correct default domain and port.
    """
    api_request = AliexpressAffiliateProductQueryRequest()
    assert api_request.domain == "api-sg.aliexpress.com"
    assert api_request.port == 80

def test_aliexpress_affiliate_product_query_request_custom_domain_and_port():
    """
    Test if the AliexpressAffiliateProductQueryRequest class is initialized with a custom domain and port.
    """
    custom_domain = "example.com"
    custom_port = 443
    api_request = AliexpressAffiliateProductQueryRequest(domain=custom_domain, port=custom_port)
    assert api_request.domain == custom_domain
    assert api_request.port == custom_port

def test_getapiname(api_request):
    """
    Test the getapiname method to ensure it returns the correct API name.
    """
    assert api_request.getapiname() == 'aliexpress.affiliate.product.query'
```