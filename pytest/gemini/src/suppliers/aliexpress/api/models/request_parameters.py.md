```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.request_parameters import (
    ProductType,
    SortBy,
    LinkType,
)


def test_product_type_constants():
    """
    Tests that the ProductType constants are defined correctly and have expected values.
    """
    assert ProductType.ALL == "ALL"
    assert ProductType.PLAZA == "PLAZA"
    assert ProductType.TMALL == "TMALL"


def test_sort_by_constants():
    """
    Tests that the SortBy constants are defined correctly and have expected values.
    """
    assert SortBy.SALE_PRICE_ASC == "SALE_PRICE_ASC"
    assert SortBy.SALE_PRICE_DESC == "SALE_PRICE_DESC"
    assert SortBy.LAST_VOLUME_ASC == "LAST_VOLUME_ASC"
    assert SortBy.LAST_VOLUME_DESC == "LAST_VOLUME_DESC"


def test_link_type_constants():
    """
    Tests that the LinkType constants are defined correctly and have expected values.
    """
    assert LinkType.NORMAL == 0
    assert LinkType.HOTLINK == 2
```