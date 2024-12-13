```python
import pytest
from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateHotproductQueryRequest import AliexpressAffiliateHotproductQueryRequest

# Fixture for creating an instance of the class
@pytest.fixture
def api_request():
    """Provides an instance of AliexpressAffiliateHotproductQueryRequest for testing."""
    return AliexpressAffiliateHotproductQueryRequest()

def test_aliexpress_affiliate_hotproduct_query_request_init(api_request):
    """
    Test the initialization of the AliexpressAffiliateHotproductQueryRequest class.
    Checks if all attributes are initialized to None, and the domain/port are set correctly.
    """
    assert api_request.domain == "api-sg.aliexpress.com"
    assert api_request.port == 80
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


def test_aliexpress_affiliate_hotproduct_query_request_getapiname(api_request):
    """
    Test the getapiname method to ensure it returns the correct API name.
    """
    assert api_request.getapiname() == 'aliexpress.affiliate.hotproduct.query'

def test_aliexpress_affiliate_hotproduct_query_request_custom_domain_and_port():
    """
    Test initialization with a custom domain and port.
    """
    custom_domain = "test.aliexpress.com"
    custom_port = 443
    api_request = AliexpressAffiliateHotproductQueryRequest(domain=custom_domain, port=custom_port)
    assert api_request.domain == custom_domain
    assert api_request.port == custom_port

def test_aliexpress_affiliate_hotproduct_query_request_attribute_setting(api_request):
    """
    Test setting attributes of the AliexpressAffiliateHotproductQueryRequest class.
    """
    api_request.app_signature = "test_signature"
    api_request.category_ids = [1, 2, 3]
    api_request.delivery_days = 7
    api_request.fields = "field1,field2"
    api_request.keywords = "test keywords"
    api_request.max_sale_price = 100.0
    api_request.min_sale_price = 10.0
    api_request.page_no = 1
    api_request.page_size = 20
    api_request.platform_product_type = "normal"
    api_request.ship_to_country = "US"
    api_request.sort = "price_asc"
    api_request.target_currency = "USD"
    api_request.target_language = "en"
    api_request.tracking_id = "test_tracking_id"

    assert api_request.app_signature == "test_signature"
    assert api_request.category_ids == [1, 2, 3]
    assert api_request.delivery_days == 7
    assert api_request.fields == "field1,field2"
    assert api_request.keywords == "test keywords"
    assert api_request.max_sale_price == 100.0
    assert api_request.min_sale_price == 10.0
    assert api_request.page_no == 1
    assert api_request.page_size == 20
    assert api_request.platform_product_type == "normal"
    assert api_request.ship_to_country == "US"
    assert api_request.sort == "price_asc"
    assert api_request.target_currency == "USD"
    assert api_request.target_language == "en"
    assert api_request.tracking_id == "test_tracking_id"
```