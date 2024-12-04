```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.request_parameters import (
    ProductType,
    SortBy,
    LinkType,
)


def test_product_type_valid_values():
    """Test valid ProductType values."""
    assert ProductType.ALL == "ALL"
    assert ProductType.PLAZA == "PLAZA"
    assert ProductType.TMALL == "TMALL"


def test_product_type_invalid_value():
    """Test invalid ProductType value."""
    with pytest.raises(AttributeError):
        ProductType.INVALID


def test_sort_by_valid_values():
    """Test valid SortBy values."""
    assert SortBy.SALE_PRICE_ASC == "SALE_PRICE_ASC"
    assert SortBy.SALE_PRICE_DESC == "SALE_PRICE_DESC"
    assert SortBy.LAST_VOLUME_ASC == "LAST_VOLUME_ASC"
    assert SortBy.LAST_VOLUME_DESC == "LAST_VOLUME_DESC"


def test_sort_by_invalid_value():
    """Test invalid SortBy value."""
    with pytest.raises(AttributeError):
        SortBy.INVALID


def test_link_type_valid_values():
    """Test valid LinkType values."""
    assert LinkType.NORMAL == 0
    assert LinkType.HOTLINK == 2


def test_link_type_invalid_value():
    """Test invalid LinkType value."""
    with pytest.raises(AttributeError):
        LinkType.INVALID


def test_link_type_out_of_range():
    """Test out-of-range LinkType value."""
    with pytest.raises(ValueError):
        LinkType(1) #1 is not a valid LinkType value


def test_link_type_non_integer():
    """Test non-integer value for LinkType."""
    with pytest.raises(TypeError):
        LinkType("invalid")
```