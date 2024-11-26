```python
import pytest

# Tests for the AffiliateLink class
from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink


def test_affiliate_link_creation_valid_input():
    """Tests creating an AffiliateLink object with valid input."""
    link = "https://www.aliexpress.com/store/product/1234567890.html"
    source = "google"
    affiliate_link = AffiliateLink(promotion_link=link, source_value=source)
    assert affiliate_link.promotion_link == link
    assert affiliate_link.source_value == source


def test_affiliate_link_creation_empty_string_promotion_link():
    """Tests creating an AffiliateLink object with an empty string for promotion_link."""
    with pytest.raises(ValueError) as excinfo:
        AffiliateLink(promotion_link="", source_value="test")
    assert "promotion_link cannot be empty" in str(excinfo.value)

def test_affiliate_link_creation_none_promotion_link():
    """Tests creating an AffiliateLink object with None for promotion_link."""
    with pytest.raises(ValueError) as excinfo:
        AffiliateLink(promotion_link=None, source_value="test")
    assert "promotion_link cannot be empty" in str(excinfo.value)

def test_affiliate_link_creation_empty_string_source_value():
    """Tests creating an AffiliateLink object with an empty string for source_value."""
    with pytest.raises(ValueError) as excinfo:
        AffiliateLink(promotion_link="test", source_value="")
    assert "source_value cannot be empty" in str(excinfo.value)

def test_affiliate_link_creation_none_source_value():
    """Tests creating an AffiliateLink object with None for source_value."""
    with pytest.raises(ValueError) as excinfo:
        AffiliateLink(promotion_link="test", source_value=None)
    assert "source_value cannot be empty" in str(excinfo.value)


def test_affiliate_link_creation_valid_inputs_types():
    """Tests creating an AffiliateLink with valid input types."""
    link = "https://www.aliexpress.com/store/product/1234567890.html"
    source = "google"
    affiliate_link = AffiliateLink(promotion_link=link, source_value=source)

    assert isinstance(affiliate_link.promotion_link, str)
    assert isinstance(affiliate_link.source_value, str)


def test_affiliate_link_creation_invalid_promotion_link_type():
    """Tests creating an AffiliateLink with an invalid type for promotion_link."""
    with pytest.raises(TypeError) as excinfo:
        AffiliateLink(promotion_link=123, source_value="test")
    assert "promotion_link must be a string" in str(excinfo.value)

def test_affiliate_link_creation_invalid_source_value_type():
    """Tests creating an AffiliateLink with an invalid type for source_value."""
    with pytest.raises(TypeError) as excinfo:
        AffiliateLink(promotion_link="test", source_value=123)
    assert "source_value must be a string" in str(excinfo.value)



```