```python
import pytest

# Tests for the AffiliateLink class
from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink


def test_affiliate_link_creation_valid():
    """Tests creating an AffiliateLink object with valid data."""
    promotion_link = "https://example.com/promotion"
    source_value = "some_source"
    affiliate_link = AffiliateLink(promotion_link=promotion_link, source_value=source_value)
    assert affiliate_link.promotion_link == promotion_link
    assert affiliate_link.source_value == source_value


def test_affiliate_link_creation_missing_promotion_link():
    """Tests creating an AffiliateLink object with missing promotion_link."""
    with pytest.raises(TypeError):
        AffiliateLink(source_value="some_source")


def test_affiliate_link_creation_missing_source_value():
    """Tests creating an AffiliateLink object with missing source_value."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link="https://example.com/promotion")


def test_affiliate_link_creation_invalid_promotion_link_type():
    """Tests creating an AffiliateLink object with incorrect promotion_link type."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link=123, source_value="some_source")


def test_affiliate_link_creation_invalid_source_value_type():
    """Tests creating an AffiliateLink object with incorrect source_value type."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link="https://example.com/promotion", source_value=123)


def test_affiliate_link_creation_empty_promotion_link():
    """Tests creating an AffiliateLink object with empty promotion_link."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link="", source_value="some_source")


def test_affiliate_link_creation_empty_source_value():
    """Tests creating an AffiliateLink object with empty source_value."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link="https://example.com/promotion", source_value="")

# Important:  Since the code only defines the class structure,
# these tests effectively demonStarte that the class *can* be instantiated
# with correct data and raises errors for invalid data, but they don't
# test *any* logic within the class itself, as the class itself has no methods.
# If the AffiliateLink class had methods like `get_promotion_link`, `validate`,
# you'd need additional test cases to cover those methods.
```