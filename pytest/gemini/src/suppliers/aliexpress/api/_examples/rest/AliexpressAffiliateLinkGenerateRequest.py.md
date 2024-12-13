```python
import pytest

from hypotez.src.suppliers.aliexpress.api._examples.rest.AliexpressAffiliateLinkGenerateRequest import (
    AliexpressAffiliateLinkGenerateRequest,
)

# Fixture definitions, if needed
@pytest.fixture
def api_request():
    """Provides an instance of AliexpressAffiliateLinkGenerateRequest for testing."""
    return AliexpressAffiliateLinkGenerateRequest()


# Tests for __init__ method
def test_init_default_values(api_request):
    """Checks if __init__ sets default values correctly."""
    assert api_request.domain == "api-sg.aliexpress.com"
    assert api_request.port == 80
    assert api_request.app_signature is None
    assert api_request.promotion_link_type is None
    assert api_request.source_values is None
    assert api_request.tracking_id is None


def test_init_custom_domain_port():
    """Checks if __init__ sets custom domain and port."""
    api_request = AliexpressAffiliateLinkGenerateRequest(
        domain="custom.aliexpress.com", port=443
    )
    assert api_request.domain == "custom.aliexpress.com"
    assert api_request.port == 443


# Tests for getapiname method
def test_getapiname(api_request):
    """Checks if getapiname returns the correct API name."""
    assert api_request.getapiname() == "aliexpress.affiliate.link.generate"


# Tests for setting attributes
def test_set_app_signature(api_request):
    """Checks if app_signature can be set."""
    api_request.app_signature = "test_signature"
    assert api_request.app_signature == "test_signature"


def test_set_promotion_link_type(api_request):
    """Checks if promotion_link_type can be set."""
    api_request.promotion_link_type = "test_link_type"
    assert api_request.promotion_link_type == "test_link_type"


def test_set_source_values(api_request):
    """Checks if source_values can be set."""
    api_request.source_values = "test_source_values"
    assert api_request.source_values == "test_source_values"


def test_set_tracking_id(api_request):
    """Checks if tracking_id can be set."""
    api_request.tracking_id = "test_tracking_id"
    assert api_request.tracking_id == "test_tracking_id"
```