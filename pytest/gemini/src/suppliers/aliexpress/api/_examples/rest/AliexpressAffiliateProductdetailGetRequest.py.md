```python
import pytest

from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateProductdetailGetRequest import (
    AliexpressAffiliateProductdetailGetRequest,
)


@pytest.fixture
def api_request():
    """Fixture to create an instance of AliexpressAffiliateProductdetailGetRequest."""
    return AliexpressAffiliateProductdetailGetRequest()


def test_aliexpress_affiliate_productdetail_get_request_init_default(api_request):
    """Test initialization with default domain and port."""
    assert api_request.domain == "api-sg.aliexpress.com"
    assert api_request.port == 80
    assert api_request.app_signature is None
    assert api_request.country is None
    assert api_request.fields is None
    assert api_request.product_ids is None
    assert api_request.target_currency is None
    assert api_request.target_language is None
    assert api_request.tracking_id is None


def test_aliexpress_affiliate_productdetail_get_request_init_custom():
    """Test initialization with custom domain and port."""
    api_request = AliexpressAffiliateProductdetailGetRequest(
        domain="example.com", port=443
    )
    assert api_request.domain == "example.com"
    assert api_request.port == 443
    assert api_request.app_signature is None
    assert api_request.country is None
    assert api_request.fields is None
    assert api_request.product_ids is None
    assert api_request.target_currency is None
    assert api_request.target_language is None
    assert api_request.tracking_id is None


def test_aliexpress_affiliate_productdetail_get_request_getapiname(api_request):
    """Test the getapiname method returns the correct API name."""
    assert api_request.getapiname() == "aliexpress.affiliate.productdetail.get"


def test_aliexpress_affiliate_productdetail_get_request_set_attributes(api_request):
    """Test setting attributes for the request object."""
    api_request.app_signature = "test_signature"
    api_request.country = "US"
    api_request.fields = "field1,field2"
    api_request.product_ids = "123,456"
    api_request.target_currency = "USD"
    api_request.target_language = "en"
    api_request.tracking_id = "test_tracking_id"

    assert api_request.app_signature == "test_signature"
    assert api_request.country == "US"
    assert api_request.fields == "field1,field2"
    assert api_request.product_ids == "123,456"
    assert api_request.target_currency == "USD"
    assert api_request.target_language == "en"
    assert api_request.tracking_id == "test_tracking_id"

def test_aliexpress_affiliate_productdetail_get_request_empty_attributes(api_request):
    """Test that all attributes are initialized to None when no values are passed."""
    assert api_request.app_signature is None
    assert api_request.country is None
    assert api_request.fields is None
    assert api_request.product_ids is None
    assert api_request.target_currency is None
    assert api_request.target_language is None
    assert api_request.tracking_id is None
```