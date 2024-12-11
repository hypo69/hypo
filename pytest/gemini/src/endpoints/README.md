```python
import pytest

# Placeholder for actual code from src.endpoints (replace with the actual code)
# These are dummy functions, replace with your actual implementations
class PrestashopAPI:
    def create_product(self, product_data):
        if not product_data:
            raise ValueError("Product data cannot be empty")
        return "Product created"

    def get_order(self, order_id):
        if not order_id:
            raise ValueError("Order ID cannot be empty")
        return {"order_id": order_id, "status": "pending"}


class AdvertisementAPI:
    def create_campaign(self, campaign_data):
        if not campaign_data:
            raise ValueError("Campaign data cannot be empty")
        return "Campaign created"

    def get_campaign_analytics(self, campaign_id):
        if not campaign_id:
            raise ValueError("Campaign ID cannot be empty")
        return {"campaign_id": campaign_id, "impressions": 1000}



# Tests for PrestashopAPI
def test_prestashop_create_product_valid_input(prestashop_api):
    """Tests creating a product with valid input."""
    product_data = {"name": "Test Product", "price": 10.00}
    result = prestashop_api.create_product(product_data)
    assert result == "Product created"

def test_prestashop_create_product_empty_input(prestashop_api):
    """Tests creating a product with empty input."""
    with pytest.raises(ValueError) as excinfo:
        prestashop_api.create_product({})
    assert str(excinfo.value) == "Product data cannot be empty"


def test_prestashop_get_order_valid_input(prestashop_api):
    """Tests getting an order with valid input."""
    order_id = 12345
    result = prestashop_api.get_order(order_id)
    assert result["order_id"] == order_id
    assert result["status"] == "pending"


def test_prestashop_get_order_empty_input(prestashop_api):
    """Tests getting an order with empty input."""
    with pytest.raises(ValueError) as excinfo:
        prestashop_api.get_order("")
    assert str(excinfo.value) == "Order ID cannot be empty"




# Tests for AdvertisementAPI
def test_advertisement_create_campaign_valid_input(advertisement_api):
    campaign_data = {"name": "Test Campaign", "budget": 1000}
    result = advertisement_api.create_campaign(campaign_data)
    assert result == "Campaign created"

def test_advertisement_create_campaign_empty_input(advertisement_api):
    with pytest.raises(ValueError) as excinfo:
        advertisement_api.create_campaign({})
    assert str(excinfo.value) == "Campaign data cannot be empty"

def test_advertisement_get_campaign_analytics_valid_input(advertisement_api):
    campaign_id = 67890
    result = advertisement_api.get_campaign_analytics(campaign_id)
    assert result["campaign_id"] == campaign_id
    assert result["impressions"] == 1000

def test_advertisement_get_campaign_analytics_empty_input(advertisement_api):
    with pytest.raises(ValueError) as excinfo:
        advertisement_api.get_campaign_analytics("")
    assert str(excinfo.value) == "Campaign ID cannot be empty"




# Fixture (replace with your actual fixture if needed)
@pytest.fixture
def prestashop_api():
    return PrestashopAPI()

@pytest.fixture
def advertisement_api():
    return AdvertisementAPI()

```

**Explanation and Improvements:**

1. **Dummy Classes:** Included placeholder `PrestashopAPI` and `AdvertisementAPI` classes with dummy methods.  **Crucially,** replace these with the actual classes from your `src.endpoints` module.

2. **Clear Test Names:**  Test names clearly indicate the input and expected behavior (e.g., `test_prestashop_create_product_valid_input`).

3. **pytest.raises:** Used `pytest.raises` to test for `ValueError` exceptions effectively.

4. **Fixtures:** Defined `prestashop_api` and `advertisement_api` fixtures to avoid creating new instances of these classes for each test.

5. **Edge Cases:** Included tests for empty inputs to ensure robustness.

6. **Comprehensive Coverage:** Tested both valid and invalid input scenarios for each function.

7. **Specific Assertions:** The assertions now check the expected values returned by the methods, ensuring precise test success criteria.

8. **Error Handling:**  The tests now accurately capture and verify the exceptions raised by the functions.

**How to Use:**

1. **Replace Placeholders:** Substitute the placeholder classes with the actual classes from your `src.endpoints` module.
2. **Run Tests:**  Run the tests using `pytest` in your terminal.  Ensure you have the `pytest` library installed (`pip install pytest`).

**Example Usage (if you have a module named `prestashop`):**

```python
# ... imports ...

# Replace these placeholder with actual classes from your module
from prestashop import PrestashopAPI

# ... rest of the code ...
```

This updated solution provides a more complete and reliable set of `pytest` tests for your code. Remember to adjust the tests based on the specifics of your actual `src.endpoints` module's functions and expected behavior. Remember to handle potential `ImportError` exceptions.  Import your actual module rather than redefining class contents in your test file.