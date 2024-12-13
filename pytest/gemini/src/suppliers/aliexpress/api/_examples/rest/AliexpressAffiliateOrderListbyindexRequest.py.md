```python
import pytest

from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateOrderListbyindexRequest import AliexpressAffiliateOrderListbyindexRequest

# Fixture for creating an instance of the class
@pytest.fixture
def api_request():
    """Provides an instance of AliexpressAffiliateOrderListbyindexRequest for testing."""
    return AliexpressAffiliateOrderListbyindexRequest()

# Test case for default domain and port
def test_default_domain_port(api_request):
    """Checks if the default domain and port are set correctly during initialization."""
    assert api_request.domain == "api-sg.aliexpress.com"
    assert api_request.port == 80


# Test case for custom domain and port
def test_custom_domain_port():
    """Checks if the domain and port can be customized during initialization."""
    custom_api = AliexpressAffiliateOrderListbyindexRequest(domain="custom.aliexpress.com", port=443)
    assert custom_api.domain == "custom.aliexpress.com"
    assert custom_api.port == 443

# Test case for initial attribute values
def test_initial_attribute_values(api_request):
    """Checks if the attributes are initialized to None."""
    assert api_request.app_signature is None
    assert api_request.end_time is None
    assert api_request.fields is None
    assert api_request.page_size is None
    assert api_request.start_query_index_id is None
    assert api_request.start_time is None
    assert api_request.status is None

# Test case for getapiname method
def test_getapiname(api_request):
    """Checks if the getapiname method returns the correct API name."""
    assert api_request.getapiname() == 'aliexpress.affiliate.order.listbyindex'

# Test case for setting and getting attributes
def test_set_get_attributes(api_request):
    """Checks if the attributes can be set and retrieved correctly."""
    api_request.app_signature = "test_signature"
    api_request.end_time = "2024-01-31"
    api_request.fields = "order_id,create_time"
    api_request.page_size = 20
    api_request.start_query_index_id = 123
    api_request.start_time = "2024-01-01"
    api_request.status = "WAIT_SELLER_SEND_GOODS"

    assert api_request.app_signature == "test_signature"
    assert api_request.end_time == "2024-01-31"
    assert api_request.fields == "order_id,create_time"
    assert api_request.page_size == 20
    assert api_request.start_query_index_id == 123
    assert api_request.start_time == "2024-01-01"
    assert api_request.status == "WAIT_SELLER_SEND_GOODS"
```