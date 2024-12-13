```python
import pytest

from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateProductSmartmatchRequest import AliexpressAffiliateProductSmartmatchRequest

@pytest.fixture
def api_request():
    """Provides a base instance of the AliexpressAffiliateProductSmartmatchRequest for testing."""
    return AliexpressAffiliateProductSmartmatchRequest()


def test_aliexpress_affiliate_product_smartmatch_request_init_default(api_request):
    """Checks if the class initializes with default values."""
    assert api_request.domain == "api-sg.aliexpress.com"
    assert api_request.port == 80
    assert api_request.app is None
    assert api_request.app_signature is None
    assert api_request.country is None
    assert api_request.device is None
    assert api_request.device_id is None
    assert api_request.fields is None
    assert api_request.keywords is None
    assert api_request.page_no is None
    assert api_request.product_id is None
    assert api_request.site is None
    assert api_request.target_currency is None
    assert api_request.target_language is None
    assert api_request.tracking_id is None
    assert api_request.user is None


def test_aliexpress_affiliate_product_smartmatch_request_init_custom():
    """Checks if the class initializes with custom domain and port values."""
    custom_api_request = AliexpressAffiliateProductSmartmatchRequest(domain="test.aliexpress.com", port=443)
    assert custom_api_request.domain == "test.aliexpress.com"
    assert custom_api_request.port == 443
    assert custom_api_request.app is None
    assert custom_api_request.app_signature is None
    assert custom_api_request.country is None
    assert custom_api_request.device is None
    assert custom_api_request.device_id is None
    assert custom_api_request.fields is None
    assert custom_api_request.keywords is None
    assert custom_api_request.page_no is None
    assert custom_api_request.product_id is None
    assert custom_api_request.site is None
    assert custom_api_request.target_currency is None
    assert custom_api_request.target_language is None
    assert custom_api_request.tracking_id is None
    assert custom_api_request.user is None


def test_aliexpress_affiliate_product_smartmatch_request_getapiname(api_request):
    """Checks if getapiname returns the correct API name."""
    assert api_request.getapiname() == 'aliexpress.affiliate.product.smartmatch'


def test_aliexpress_affiliate_product_smartmatch_request_set_attributes(api_request):
    """Checks if attributes can be set and retrieved correctly."""
    api_request.app = "test_app"
    api_request.app_signature = "test_signature"
    api_request.country = "US"
    api_request.device = "mobile"
    api_request.device_id = "12345"
    api_request.fields = "field1,field2"
    api_request.keywords = "test,keywords"
    api_request.page_no = 2
    api_request.product_id = 123
    api_request.site = "test_site"
    api_request.target_currency = "USD"
    api_request.target_language = "en"
    api_request.tracking_id = "test_tracking_id"
    api_request.user = "test_user"


    assert api_request.app == "test_app"
    assert api_request.app_signature == "test_signature"
    assert api_request.country == "US"
    assert api_request.device == "mobile"
    assert api_request.device_id == "12345"
    assert api_request.fields == "field1,field2"
    assert api_request.keywords == "test,keywords"
    assert api_request.page_no == 2
    assert api_request.product_id == 123
    assert api_request.site == "test_site"
    assert api_request.target_currency == "USD"
    assert api_request.target_language == "en"
    assert api_request.tracking_id == "test_tracking_id"
    assert api_request.user == "test_user"
```