```python
import pytest
from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink

# Fixture definitions, if needed
@pytest.fixture
def valid_affiliate_link_data():
    """Provides valid test data for the AffiliateLink class."""
    return {
        "promotion_link": "https://s.click.aliexpress.com/e/_DmK72x1",
        "source_value": "123456"
    }

@pytest.fixture
def invalid_affiliate_link_data():
    """Provides invalid test data for the AffiliateLink class."""
    return {
        "promotion_link": 1234,
        "source_value": None
    }


# Tests for AffiliateLink class
def test_affiliate_link_creation_valid(valid_affiliate_link_data):
    """Checks correct instantiation of AffiliateLink with valid data."""
    affiliate_link = AffiliateLink(**valid_affiliate_link_data)
    assert affiliate_link.promotion_link == valid_affiliate_link_data["promotion_link"]
    assert affiliate_link.source_value == valid_affiliate_link_data["source_value"]

def test_affiliate_link_creation_invalid_types(invalid_affiliate_link_data):
    """Checks that instantiation with incorrect types does not break and assigns values """
    affiliate_link = AffiliateLink(**invalid_affiliate_link_data)
    assert affiliate_link.promotion_link == invalid_affiliate_link_data["promotion_link"]
    assert affiliate_link.source_value == invalid_affiliate_link_data["source_value"]

def test_affiliate_link_empty_values():
    """Checks correct instantiation of AffiliateLink with empty string data."""
    affiliate_link = AffiliateLink(promotion_link="", source_value="")
    assert affiliate_link.promotion_link == ""
    assert affiliate_link.source_value == ""

def test_affiliate_link_none_values():
    """Checks correct instantiation of AffiliateLink with None data."""
    affiliate_link = AffiliateLink(promotion_link=None, source_value=None)
    assert affiliate_link.promotion_link is None
    assert affiliate_link.source_value is None


def test_affiliate_link_attribute_access(valid_affiliate_link_data):
    """Checks that attributes can be accessed correctly."""
    affiliate_link = AffiliateLink(**valid_affiliate_link_data)
    assert hasattr(affiliate_link, "promotion_link")
    assert hasattr(affiliate_link, "source_value")
    assert affiliate_link.promotion_link == valid_affiliate_link_data["promotion_link"]
    assert affiliate_link.source_value == valid_affiliate_link_data["source_value"]

def test_affiliate_link_assignment_valid(valid_affiliate_link_data):
     """Checks that attributes can be assigned correctly."""
     affiliate_link = AffiliateLink(**valid_affiliate_link_data)
     new_promotion_link = "https://s.click.aliexpress.com/e/_De0Xk7f"
     new_source_value = "789012"
     affiliate_link.promotion_link = new_promotion_link
     affiliate_link.source_value = new_source_value
     assert affiliate_link.promotion_link == new_promotion_link
     assert affiliate_link.source_value == new_source_value


def test_affiliate_link_assignment_invalid_types(invalid_affiliate_link_data):
     """Checks that attributes can be assigned correctly."""
     affiliate_link = AffiliateLink(promotion_link="test", source_value="test")
     affiliate_link.promotion_link = invalid_affiliate_link_data["promotion_link"]
     affiliate_link.source_value = invalid_affiliate_link_data["source_value"]
     assert affiliate_link.promotion_link == invalid_affiliate_link_data["promotion_link"]
     assert affiliate_link.source_value == invalid_affiliate_link_data["source_value"]
```