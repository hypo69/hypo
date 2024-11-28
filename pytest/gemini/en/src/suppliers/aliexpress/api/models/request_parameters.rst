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
    """Tests for invalid ProductType values."""
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
    """Tests for invalid SortBy values."""
    with pytest.raises(AttributeError):
        SortBy.INVALID_VALUE


# Tests for LinkType
def test_link_type_valid_values():
    """Tests valid LinkType values."""
    assert LinkType.NORMAL == 0
    assert LinkType.HOTLINK == 2

def test_link_type_invalid_value():
    """Tests for invalid LinkType values."""
    with pytest.raises(AttributeError):
        LinkType.INVALID_VALUE

def test_link_type_non_int():
  """Tests for non-integer value in LinkType."""
  with pytest.raises(TypeError) as e:
    LinkType.NORMAL = "abc"
  assert "cannot set attribute" in str(e.value)

def test_link_type_incorrect_type():
  """Tests for incorrect type of value in LinkType."""
  with pytest.raises(AttributeError) as e:
    LinkType.NON_EXISTING_ATTRIBUTE = "invalid type"
  assert "cannot set attribute" in str(e.value)



# Example tests demonstrating how to test class attributes in a more general way.
# Using strings as an example since there is no other way to test an enum value

def test_product_type_has_all():
  """Tests that ProductType has the 'ALL' attribute"""
  assert hasattr(ProductType, 'ALL')


def test_product_type_has_plaza():
    """Tests that ProductType has the 'PLAZA' attribute."""
    assert hasattr(ProductType, 'PLAZA')

def test_product_type_has_tmall():
    """Tests that ProductType has the 'TMALL' attribute."""
    assert hasattr(ProductType, 'TMALL')




# These tests are included to demonstrate testing for the presence and type of attributes, rather than just values. 
# However, given the simple nature of the code, this level of detail may not always be strictly necessary
```