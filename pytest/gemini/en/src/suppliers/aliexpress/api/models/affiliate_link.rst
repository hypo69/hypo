```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink


def test_affiliate_link_creation_valid():
    """Checks creation of AffiliateLink with valid data."""
    link = "https://example.com/affiliate"
    source = "some_source"
    affiliate_link = AffiliateLink(promotion_link=link, source_value=source)
    assert affiliate_link.promotion_link == link
    assert affiliate_link.source_value == source


def test_affiliate_link_creation_empty_source():
    """Checks creation with empty source value."""
    link = "https://example.com/affiliate"
    source = ""
    affiliate_link = AffiliateLink(promotion_link=link, source_value=source)
    assert affiliate_link.promotion_link == link
    assert affiliate_link.source_value == source

def test_affiliate_link_creation_none_source():
    """Checks creation with None source value."""
    link = "https://example.com/affiliate"
    source = None
    affiliate_link = AffiliateLink(promotion_link=link, source_value=source)
    assert affiliate_link.promotion_link == link
    assert affiliate_link.source_value is None


def test_affiliate_link_creation_invalid_link():
    """Tests creation with invalid link (not a string)."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link=123, source_value="valid_source")


def test_affiliate_link_creation_no_link():
    """Tests creation with no promotion_link."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link=None, source_value="valid_source")
    

def test_affiliate_link_creation_invalid_link_type():
    """Tests creation with promotion_link that is not a string."""
    with pytest.raises(TypeError):
       AffiliateLink(promotion_link=123, source_value="valid_source")

def test_affiliate_link_creation_invalid_source_type():
    """Tests creation with source_value that is not a string or None."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link="valid_link", source_value=123)

# Add more tests if necessary based on the intended functionality of the class
# e.g., tests for __eq__ or other methods if applicable
```

**Explanation and Improvements:**

1. **Comprehensive Test Cases:** The provided tests now cover a wider range of scenarios, including empty strings, `None` values, and type errors, making the test suite more robust.

2. **Clear Test Names:**  Test names are more descriptive, clearly indicating the purpose of each test.

3. **`pytest.raises` for Exceptions:**  Correctly uses `pytest.raises` to test for expected `TypeError` exceptions when invalid types are passed to the constructor.

4. **Type Handling:** The tests now specifically check for `TypeError` when providing a non-string value for `promotion_link` and `source_value`, ensuring the code handles type validation correctly.

5. **No Unnecessary Fixtures:**  No fixtures are needed in this case, as the tests are focused on the class's constructor.


This improved test suite provides more confidence in the correctness of the `AffiliateLink` class, especially concerning type handling and edge cases like empty strings and `None` values.  Remember to adapt the tests further if the class has other methods or functionalities. Remember to adapt the tests based on the intended behavior of the `AffiliateLink` class, such as checking the `__eq__` method if it's implemented.