```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink


# Tests for the AffiliateLink class
def test_affiliate_link_creation_valid_data():
    """Tests creation of AffiliateLink with valid data."""
    link = "https://example.com/affiliate"
    source = "some_source"
    affiliate_link = AffiliateLink(promotion_link=link, source_value=source)
    assert affiliate_link.promotion_link == link
    assert affiliate_link.source_value == source


def test_affiliate_link_creation_missing_promotion_link():
    """Tests creation with missing promotion_link, expecting TypeError."""
    with pytest.raises(TypeError):
        AffiliateLink(source_value="some_source")


def test_affiliate_link_creation_missing_source_value():
    """Tests creation with missing source_value, expecting TypeError."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link="https://example.com/affiliate")


def test_affiliate_link_creation_invalid_promotion_link_type():
    """Tests creation with promotion_link of incorrect type, expecting TypeError."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link=123, source_value="some_source")


def test_affiliate_link_creation_invalid_source_value_type():
    """Tests creation with source_value of incorrect type, expecting TypeError."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link="https://example.com/affiliate", source_value=123)


def test_affiliate_link_creation_empty_promotion_link():
    """Tests creation with empty promotion_link, expecting TypeError. """
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link="", source_value="some_source")


def test_affiliate_link_creation_empty_source_value():
    """Tests creation with empty source_value, expecting TypeError."""
    with pytest.raises(TypeError):
        AffiliateLink(promotion_link="https://example.com/affiliate", source_value="")

```