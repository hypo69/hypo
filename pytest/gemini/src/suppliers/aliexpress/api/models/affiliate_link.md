```python
import pytest

# Tests for the AffiliateLink class
from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink


def test_affiliate_link_creation_valid_data():
    """Tests creating an AffiliateLink object with valid data."""
    link = "https://example.com/affiliate"
    source = "some_source"
    affiliate_link = AffiliateLink(promotion_link=link, source_value=source)
    assert affiliate_link.promotion_link == link
    assert affiliate_link.source_value == source


def test_affiliate_link_creation_with_none_source():
    """Tests creating an AffiliateLink object with None source."""
    link = "https://example.com/affiliate"
    affiliate_link = AffiliateLink(promotion_link=link, source_value=None)
    assert affiliate_link.promotion_link == link
    assert affiliate_link.source_value is None


def test_affiliate_link_creation_with_none_link():
    """Tests creating an AffiliateLink object with None link (shouldn't crash)."""
    source = "some_source"
    with pytest.raises(TypeError) as excinfo:
        affiliate_link = AffiliateLink(promotion_link=None, source_value=source)
    assert "promotion_link" in str(excinfo.value)


def test_affiliate_link_creation_invalid_link_type():
    """Tests creating an AffiliateLink object with invalid link type."""
    source = "some_source"
    with pytest.raises(TypeError) as excinfo:
        affiliate_link = AffiliateLink(promotion_link=123, source_value=source)
    assert "promotion_link" in str(excinfo.value)
    
def test_affiliate_link_creation_invalid_source_type():
    """Tests creating an AffiliateLink object with invalid source type."""
    link = "https://example.com/affiliate"
    with pytest.raises(TypeError) as excinfo:
        affiliate_link = AffiliateLink(promotion_link=link, source_value=123)
    assert "source_value" in str(excinfo.value)



def test_affiliate_link_creation_empty_string_link():
    """Tests creating an AffiliateLink object with an empty string for link."""
    source = "some_source"
    with pytest.raises(ValueError) as excinfo:
        affiliate_link = AffiliateLink(promotion_link="", source_value=source)
    assert "promotion_link" in str(excinfo.value)
  
  
def test_affiliate_link_creation_empty_string_source():
    """Tests creating an AffiliateLink object with an empty string for source."""
    link = "https://example.com/affiliate"
    affiliate_link = AffiliateLink(promotion_link=link, source_value="")
    assert affiliate_link.promotion_link == link
    assert affiliate_link.source_value == ""  # Important to check for empty string
```

**Explanation and Improvements:**

1. **Clear Test Names:**  Test names now clearly indicate the type of input and expected outcome.

2. **Comprehensive Scenarios:** Tests now cover various scenarios: valid input, `None` values, invalid types, empty strings, etc.

3. **`pytest.raises` for Exceptions:**  Uses `pytest.raises` to specifically test for the expected `TypeError` when incorrect types are passed. This is crucial for robust error handling verification.

4. **Detailed Error Messages:** The `pytest.raises` checks now ensure the correct attribute is mentioned in the error message.

5. **Edge Cases:** Addresses the edge case of an empty string as input for the `source_value`.

6. **Empty String Handling:**  Tests the behaviour when `source_value` is an empty string. (Crucial for real-world data!)

7. **Docstrings:** Added detailed docstrings to explain the purpose of each test.


This improved test suite provides more comprehensive and targeted tests for the `AffiliateLink` class, making it more reliable and robust. Remember to adapt the test cases further if the code has more complex logic or additional attributes. For example, if `AffiliateLink` had validation rules, these should be tested. Also, consider using parametrization for test data if the inputs vary frequently.