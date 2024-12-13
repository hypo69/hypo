```python
import pytest
from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateOrderGetRequest import AliexpressAffiliateOrderGetRequest

# Fixture definitions, if needed
@pytest.fixture
def api_request():
    """Provides an instance of AliexpressAffiliateOrderGetRequest for testing."""
    return AliexpressAffiliateOrderGetRequest()


def test_aliexpress_affiliate_order_get_request_default_initialization(api_request):
    """Checks the default initialization of the AliexpressAffiliateOrderGetRequest class."""
    assert api_request.domain == "api-sg.aliexpress.com"
    assert api_request.port == 80
    assert api_request.app_signature is None
    assert api_request.fields is None
    assert api_request.order_ids is None

def test_aliexpress_affiliate_order_get_request_custom_initialization():
    """Checks the initialization with custom domain and port."""
    api_request = AliexpressAffiliateOrderGetRequest(domain="test.example.com", port=443)
    assert api_request.domain == "test.example.com"
    assert api_request.port == 443
    assert api_request.app_signature is None
    assert api_request.fields is None
    assert api_request.order_ids is None


def test_aliexpress_affiliate_order_get_request_getapiname(api_request):
    """Checks that the getapiname method returns the correct API name."""
    assert api_request.getapiname() == 'aliexpress.affiliate.order.get'


def test_aliexpress_affiliate_order_get_request_set_attributes(api_request):
    """Checks that attributes can be set correctly"""
    api_request.app_signature = 'test_signature'
    api_request.fields = 'order_id, order_amount'
    api_request.order_ids = '123456, 789012'
    
    assert api_request.app_signature == 'test_signature'
    assert api_request.fields == 'order_id, order_amount'
    assert api_request.order_ids == '123456, 789012'

```