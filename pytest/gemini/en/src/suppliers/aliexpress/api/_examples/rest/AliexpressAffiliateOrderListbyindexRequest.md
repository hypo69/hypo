```python
import pytest
from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateOrderListbyindexRequest import AliexpressAffiliateOrderListbyindexRequest

# Fixture for providing test data.
@pytest.fixture
def request_data():
    return AliexpressAffiliateOrderListbyindexRequest()

def test_getapiname_valid(request_data):
    """Tests getapiname with valid data."""
    expected_api_name = 'aliexpress.affiliate.order.listbyindex'
    actual_api_name = request_data.getapiname()
    assert actual_api_name == expected_api_name

def test_init_valid_default_values(request_data):
    """Tests __init__ with default values."""
    assert request_data.app_signature is None
    assert request_data.end_time is None
    assert request_data.fields is None
    assert request_data.page_size is None
    assert request_data.start_query_index_id is None
    assert request_data.start_time is None
    assert request_data.status is None

    
def test_init_custom_values(request_data):
    """Tests __init__ with custom values."""
    domain = "test-domain.com"
    port = 8080
    request = AliexpressAffiliateOrderListbyindexRequest(domain, port)
    assert request.domain == domain
    assert request.port == port
    
def test_init_with_invalid_domain(request_data):
    """Tests __init__ with invalid domain (e.g. empty)."""
   # Ensure the RestApi class raises an appropriate exception for an invalid domain.
    with pytest.raises(TypeError):
        AliexpressAffiliateOrderListbyindexRequest("")
    with pytest.raises(TypeError):
      AliexpressAffiliateOrderListbyindexRequest("test-invalid-domain")

def test_init_with_invalid_port():
  """Tests __init__ with invalid port (e.g. not integer)."""
  with pytest.raises(TypeError):
        AliexpressAffiliateOrderListbyindexRequest("test.com", "invalid")
```