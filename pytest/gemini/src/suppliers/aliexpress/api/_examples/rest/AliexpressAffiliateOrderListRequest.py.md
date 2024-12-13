```python
import pytest
from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateOrderListRequest import AliexpressAffiliateOrderListRequest

@pytest.fixture
def api_request():
    """Provides a basic instance of AliexpressAffiliateOrderListRequest for testing."""
    return AliexpressAffiliateOrderListRequest()

def test_aliexpress_affiliate_order_list_request_init_default(api_request):
    """Checks default initialization of the class."""
    assert api_request.domain == "api-sg.aliexpress.com"
    assert api_request.port == 80
    assert api_request.app_signature is None
    assert api_request.end_time is None
    assert api_request.fields is None
    assert api_request.locale_site is None
    assert api_request.page_no is None
    assert api_request.page_size is None
    assert api_request.start_time is None
    assert api_request.status is None

def test_aliexpress_affiliate_order_list_request_init_custom():
    """Checks initialization with custom domain and port."""
    api_request = AliexpressAffiliateOrderListRequest(domain="test.aliexpress.com", port=443)
    assert api_request.domain == "test.aliexpress.com"
    assert api_request.port == 443


def test_getapiname(api_request):
    """Checks if getapiname returns the correct API name."""
    assert api_request.getapiname() == 'aliexpress.affiliate.order.list'

def test_aliexpress_affiliate_order_list_request_set_properties(api_request):
    """Checks setting properties of the request."""
    api_request.app_signature = "test_signature"
    api_request.end_time = "2024-01-01"
    api_request.fields = "orderId,createTime"
    api_request.locale_site = "US"
    api_request.page_no = 2
    api_request.page_size = 10
    api_request.start_time = "2023-12-01"
    api_request.status = "WAIT_SELLER_SEND_GOODS"

    assert api_request.app_signature == "test_signature"
    assert api_request.end_time == "2024-01-01"
    assert api_request.fields == "orderId,createTime"
    assert api_request.locale_site == "US"
    assert api_request.page_no == 2
    assert api_request.page_size == 10
    assert api_request.start_time == "2023-12-01"
    assert api_request.status == "WAIT_SELLER_SEND_GOODS"

def test_aliexpress_affiliate_order_list_request_empty_init():
  """Tests if the class initializes correctly with no arguments."""
  api_request = AliexpressAffiliateOrderListRequest()
  assert api_request.domain == "api-sg.aliexpress.com"
  assert api_request.port == 80
  assert api_request.app_signature is None
  assert api_request.end_time is None
  assert api_request.fields is None
  assert api_request.locale_site is None
  assert api_request.page_no is None
  assert api_request.page_size is None
  assert api_request.start_time is None
  assert api_request.status is None
```