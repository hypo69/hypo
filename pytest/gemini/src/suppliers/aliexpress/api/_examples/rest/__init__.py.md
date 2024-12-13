```python
import pytest

from hypotez.src.suppliers.aliexpress.api._examples.rest import (
    AliexpressAffiliateProductSmartmatchRequest,
    AliexpressAffiliateOrderGetRequest,
    AliexpressAffiliateOrderListRequest,
    AliexpressAffiliateHotproductDownloadRequest,
    AliexpressAffiliateProductdetailGetRequest,
    AliexpressAffiliateHotproductQueryRequest,
    AliexpressAffiliateFeaturedpromoProductsGetRequest,
    AliexpressAffiliateFeaturedpromoGetRequest,
    AliexpressAffiliateProductQueryRequest,
    AliexpressAffiliateCategoryGetRequest,
    AliexpressAffiliateOrderListbyindexRequest,
    AliexpressAffiliateLinkGenerateRequest,
)


# Test cases for AliexpressAffiliateProductSmartmatchRequest
def test_aliexpress_affiliate_product_smartmatch_request_creation():
    """Checks if an instance of AliexpressAffiliateProductSmartmatchRequest can be created."""
    request = AliexpressAffiliateProductSmartmatchRequest()
    assert isinstance(
        request, AliexpressAffiliateProductSmartmatchRequest
    ), "Should create an instance of AliexpressAffiliateProductSmartmatchRequest"


# Test cases for AliexpressAffiliateOrderGetRequest
def test_aliexpress_affiliate_order_get_request_creation():
    """Checks if an instance of AliexpressAffiliateOrderGetRequest can be created."""
    request = AliexpressAffiliateOrderGetRequest()
    assert isinstance(
        request, AliexpressAffiliateOrderGetRequest
    ), "Should create an instance of AliexpressAffiliateOrderGetRequest"


# Test cases for AliexpressAffiliateOrderListRequest
def test_aliexpress_affiliate_order_list_request_creation():
    """Checks if an instance of AliexpressAffiliateOrderListRequest can be created."""
    request = AliexpressAffiliateOrderListRequest()
    assert isinstance(
        request, AliexpressAffiliateOrderListRequest
    ), "Should create an instance of AliexpressAffiliateOrderListRequest"


# Test cases for AliexpressAffiliateHotproductDownloadRequest
def test_aliexpress_affiliate_hotproduct_download_request_creation():
    """Checks if an instance of AliexpressAffiliateHotproductDownloadRequest can be created."""
    request = AliexpressAffiliateHotproductDownloadRequest()
    assert isinstance(
        request, AliexpressAffiliateHotproductDownloadRequest
    ), "Should create an instance of AliexpressAffiliateHotproductDownloadRequest"


# Test cases for AliexpressAffiliateProductdetailGetRequest
def test_aliexpress_affiliate_productdetail_get_request_creation():
    """Checks if an instance of AliexpressAffiliateProductdetailGetRequest can be created."""
    request = AliexpressAffiliateProductdetailGetRequest()
    assert isinstance(
        request, AliexpressAffiliateProductdetailGetRequest
    ), "Should create an instance of AliexpressAffiliateProductdetailGetRequest"


# Test cases for AliexpressAffiliateHotproductQueryRequest
def test_aliexpress_affiliate_hotproduct_query_request_creation():
    """Checks if an instance of AliexpressAffiliateHotproductQueryRequest can be created."""
    request = AliexpressAffiliateHotproductQueryRequest()
    assert isinstance(
        request, AliexpressAffiliateHotproductQueryRequest
    ), "Should create an instance of AliexpressAffiliateHotproductQueryRequest"


# Test cases for AliexpressAffiliateFeaturedpromoProductsGetRequest
def test_aliexpress_affiliate_featuredpromo_products_get_request_creation():
    """Checks if an instance of AliexpressAffiliateFeaturedpromoProductsGetRequest can be created."""
    request = AliexpressAffiliateFeaturedpromoProductsGetRequest()
    assert isinstance(
        request, AliexpressAffiliateFeaturedpromoProductsGetRequest
    ), "Should create an instance of AliexpressAffiliateFeaturedpromoProductsGetRequest"


# Test cases for AliexpressAffiliateFeaturedpromoGetRequest
def test_aliexpress_affiliate_featuredpromo_get_request_creation():
    """Checks if an instance of AliexpressAffiliateFeaturedpromoGetRequest can be created."""
    request = AliexpressAffiliateFeaturedpromoGetRequest()
    assert isinstance(
        request, AliexpressAffiliateFeaturedpromoGetRequest
    ), "Should create an instance of AliexpressAffiliateFeaturedpromoGetRequest"


# Test cases for AliexpressAffiliateProductQueryRequest
def test_aliexpress_affiliate_product_query_request_creation():
    """Checks if an instance of AliexpressAffiliateProductQueryRequest can be created."""
    request = AliexpressAffiliateProductQueryRequest()
    assert isinstance(
        request, AliexpressAffiliateProductQueryRequest
    ), "Should create an instance of AliexpressAffiliateProductQueryRequest"


# Test cases for AliexpressAffiliateCategoryGetRequest
def test_aliexpress_affiliate_category_get_request_creation():
    """Checks if an instance of AliexpressAffiliateCategoryGetRequest can be created."""
    request = AliexpressAffiliateCategoryGetRequest()
    assert isinstance(
        request, AliexpressAffiliateCategoryGetRequest
    ), "Should create an instance of AliexpressAffiliateCategoryGetRequest"


# Test cases for AliexpressAffiliateOrderListbyindexRequest
def test_aliexpress_affiliate_order_listbyindex_request_creation():
    """Checks if an instance of AliexpressAffiliateOrderListbyindexRequest can be created."""
    request = AliexpressAffiliateOrderListbyindexRequest()
    assert isinstance(
        request, AliexpressAffiliateOrderListbyindexRequest
    ), "Should create an instance of AliexpressAffiliateOrderListbyindexRequest"


# Test cases for AliexpressAffiliateLinkGenerateRequest
def test_aliexpress_affiliate_link_generate_request_creation():
    """Checks if an instance of AliexpressAffiliateLinkGenerateRequest can be created."""
    request = AliexpressAffiliateLinkGenerateRequest()
    assert isinstance(
        request, AliexpressAffiliateLinkGenerateRequest
    ), "Should create an instance of AliexpressAffiliateLinkGenerateRequest"
```