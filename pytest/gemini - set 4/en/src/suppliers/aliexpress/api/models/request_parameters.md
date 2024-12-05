```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.request_parameters import (
    ProductType,
    SortBy,
    LinkType
)

# Tests for ProductType
def test_product_type_valid_values():
    """Tests valid ProductType values."""
    assert ProductType.ALL == 'ALL'
    assert ProductType.PLAZA == 'PLAZA'
    assert ProductType.TMALL == 'TMALL'

def test_product_type_invalid_value():
    """Tests for invalid ProductType value."""
    with pytest.raises(AttributeError):
        ProductType.INVALID_VALUE

# Tests for SortBy
def test_sort_by_valid_values():
    """Tests valid SortBy values."""
    assert SortBy.SALE_PRICE_ASC == 'SALE_PRICE_ASC'
    assert SortBy.SALE_PRICE_DESC == 'SALE_PRICE_DESC'
    assert SortBy.LAST_VOLUME_ASC == 'LAST_VOLUME_ASC'
    assert SortBy.LAST_VOLUME_DESC == 'LAST_VOLUME_DESC'

def test_sort_by_invalid_value():
    """Tests for invalid SortBy value."""
    with pytest.raises(AttributeError):
        SortBy.INVALID_VALUE

# Tests for LinkType
def test_link_type_valid_values():
    """Tests valid LinkType values."""
    assert LinkType.NORMAL == 0
    assert LinkType.HOTLINK == 2

def test_link_type_invalid_value():
    """Tests for invalid LinkType value."""
    with pytest.raises(AttributeError):
        LinkType.INVALID_VALUE

def test_linktype_wrong_type():
    """Tests for a wrong type input for LinkType."""
    with pytest.raises(AttributeError):
        LinkType("not an int")
    
def test_product_type_wrong_type():
    """Tests for a wrong type input for ProductType."""
    with pytest.raises(AttributeError):
        ProductType("not a string")

def test_sortby_wrong_type():
    """Tests for a wrong type input for SortBy."""
    with pytest.raises(AttributeError):
        SortBy("not a string")


```