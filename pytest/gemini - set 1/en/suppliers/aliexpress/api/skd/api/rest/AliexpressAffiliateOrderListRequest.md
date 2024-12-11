```python
import pytest
from hypotez.src.suppliers.aliexpress.api.skd.api.rest import AliexpressAffiliateOrderListRequest


class TestAliexpressAffiliateOrderListRequest:
    def test_init_valid_input(self):
        """Tests the __init__ method with valid input."""
        request = AliexpressAffiliateOrderListRequest(domain="custom-domain.com", port=443)
        assert request.domain == "custom-domain.com"
        assert request.port == 443
        assert request.app_signature is None
        assert request.end_time is None
        assert request.fields is None
        assert request.locale_site is None
        assert request.page_no is None
        assert request.page_size is None
        assert request.start_time is None
        assert request.status is None


    def test_init_default_values(self):
        """Tests the __init__ method with default values."""
        request = AliexpressAffiliateOrderListRequest()
        assert request.domain == "api-sg.aliexpress.com"
        assert request.port == 80
        assert request.app_signature is None
        assert request.end_time is None
        assert request.fields is None
        assert request.locale_site is None
        assert request.page_no is None
        assert request.page_size is None
        assert request.start_time is None
        assert request.status is None

    def test_getapiname(self):
        """Tests the getapiname method."""
        request = AliexpressAffiliateOrderListRequest()
        assert request.getapiname() == "aliexpress.affiliate.order.list"

    def test_init_invalid_port(self):
        """Tests the __init__ method with an invalid port (not an integer)."""
        with pytest.raises(TypeError):
            AliexpressAffiliateOrderListRequest(port="invalid")


    def test_init_invalid_domain(self):
        """Tests the __init__ method with an invalid domain (non-string)."""
        with pytest.raises(TypeError):
            AliexpressAffiliateOrderListRequest(domain=123)


    def test_init_with_all_attributes(self):
        """Tests __init__ method with all optional attributes set."""
        request = AliexpressAffiliateOrderListRequest(
            domain="test.com",
            port=8080,
            app_signature="some_signature",
            end_time="2024-10-26",
            fields="order_id,title",
            locale_site="en_US",
            page_no=2,
            page_size=10,
            start_time="2024-10-25",
            status="completed",
        )
        assert request.app_signature == "some_signature"
        assert request.end_time == "2024-10-26"
        assert request.fields == "order_id,title"
        assert request.locale_site == "en_US"
        assert request.page_no == 2
        assert request.page_size == 10
        assert request.start_time == "2024-10-25"
        assert request.status == "completed"

```

**Explanation and Improvements:**

* **Clearer Test Names:** Test names now explicitly state the purpose (e.g., `test_init_valid_input`, `test_getapiname`).
* **Comprehensive Input Coverage:**  Tests cover valid input, default values, and important edge cases like invalid port types and domain types.
* **Exception Handling:**  Uses `pytest.raises` to test for `TypeError` when providing incorrect data types for the `port` and `domain` parameters.
* **`with` statement:**   The `with pytest.raises` block ensures that the expected exception is correctly caught.
* **`assert` statements:**  The assertions verify the correct values assigned to the attributes.
* **Example Usage of All Parameters** A test now demonStartes setting all the optional parameters in the constructor.

This improved test suite is more robust and provides better coverage for the `AliexpressAffiliateOrderListRequest` class. Remember to install `pytest` if you haven't already: `pip install pytest`. Then run the tests from your terminal using `pytest`.  If you have the file structure correctly, this should find and run the tests within the same directory.