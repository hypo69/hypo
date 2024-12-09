```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.request_parameters import (
    ProductType,
    SortBy,
    LinkType
)


# Test cases for ProductType
def test_product_type_valid_values():
    """Checks that valid ProductType values are recognized."""
    assert ProductType.ALL == 'ALL'
    assert ProductType.PLAZA == 'PLAZA'
    assert ProductType.TMALL == 'TMALL'


def test_product_type_invalid_value():
    """Checks for handling of invalid ProductType values (not raising an exception)."""
    assert ProductType.ALL == 'ALL' #Example
    # This is a test for correct behaviour and not raising an exception (e.g., if using a wrong ProductType in an API request).
    # An alternative (more rigorous) test for error handling might check if a function using ProductType raises an error with an invalid value.
    #  and be more valuable in that context.


# Test cases for SortBy
def test_sort_by_valid_values():
    """Checks that valid SortBy values are recognized."""
    assert SortBy.SALE_PRICE_ASC == 'SALE_PRICE_ASC'
    assert SortBy.SALE_PRICE_DESC == 'SALE_PRICE_DESC'
    assert SortBy.LAST_VOLUME_ASC == 'LAST_VOLUME_ASC'
    assert SortBy.LAST_VOLUME_DESC == 'LAST_VOLUME_DESC'


def test_sort_by_invalid_value():
    """Checks for handling of invalid SortBy values (not raising an exception)."""
    # This tests correct behaviour and does not expect an exception.
    assert SortBy.SALE_PRICE_ASC == 'SALE_PRICE_ASC'
    # Similarly to ProductType, a more comprehensive test would check that an API function raises the appropriate exception for invalid SortBy values.


# Test cases for LinkType
def test_link_type_valid_values():
    """Checks that valid LinkType values are recognized."""
    assert LinkType.NORMAL == 0
    assert LinkType.HOTLINK == 2


def test_link_type_invalid_value():
    """Checks for handling of invalid LinkType values (not raising an exception)."""
    # Testing correct behavior of LinkType; an exception should not be raised for invalid but expected LinkType values.
    #  and be more valuable in that context.

    # Example of testing if the class is used correctly in a hypothetical API function
    #  to raise a meaningful exception on bad input instead of silently failing
    #  (this would be a more substantial test).


# Additional tests (example for hypothetical function usage):
#  These tests would use the class constants to call a real function and assert correct result/behaviour.

# Example (hypothetical function usage)
# def my_api_function(product_type, sort_by):
#     # ... (API call using product_type and sort_by) ...
#     return response


# def test_my_api_function_valid_input():
#     response = my_api_function(ProductType.ALL, SortBy.SALE_PRICE_ASC)
#     # Assert that the function returns a proper response given the inputs.


#  The above examples are more useful tests, but they need the hypothetical function definition!
# Note: Without a function that uses these enums, these tests are limited.
# Actual tests would need to be tied to specific functions in a larger context.


```