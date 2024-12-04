```python
import pytest
from types import SimpleNamespace
from hypotez.src.endpoints.prestashop.shop import PrestaShopShop
from src.logger.exceptions import PrestaShopException


# Fixture for providing credentials
@pytest.fixture
def credentials():
    return SimpleNamespace(api_domain="test.domain", api_key="test_key")


# Valid input test
def test_prestashop_shop_valid_input(credentials):
    """Tests initialization with valid credentials."""
    shop = PrestaShopShop(credentials=credentials)
    assert shop.api_domain == "test.domain"
    assert shop.api_key == "test_key"


# Test with credentials as a dictionary
def test_prestashop_shop_credentials_dict(credentials):
    """Tests initialization with credentials as a dictionary."""
    credentials_dict = {"api_domain": "test.domain", "api_key": "test_key"}
    shop = PrestaShopShop(credentials=credentials_dict)
    assert shop.api_domain == "test.domain"
    assert shop.api_key == "test_key"


# Test missing api_domain
def test_prestashop_shop_missing_api_domain(credentials):
    """Tests initialization with missing api_domain."""
    credentials.api_domain = None
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaShopShop(credentials=credentials)


# Test missing api_key
def test_prestashop_shop_missing_api_key(credentials):
    """Tests initialization with missing api_key."""
    credentials.api_key = None
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaShopShop(credentials=credentials)



# Test with both api_domain and api_key as None
def test_prestashop_shop_both_none():
    """Tests initialization with both api_domain and api_key as None."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaShopShop(api_domain=None, api_key=None)


# Test with only api_domain provided
def test_prestashop_shop_api_domain_only():
    """Tests initialization with only api_domain provided."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaShopShop(api_domain="test.domain")


# Test with only api_key provided
def test_prestashop_shop_api_key_only():
    """Tests initialization with only api_key provided."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaShopShop(api_key="test_key")


# Test with api_domain and api_key passed individually, not within credentials
def test_prestashop_shop_individual_parameters(credentials):
    """Tests initialization with individual api_domain and api_key."""
    shop = PrestaShopShop(api_domain=credentials.api_domain, api_key=credentials.api_key)
    assert shop.api_domain == "test.domain"
    assert shop.api_key == "test_key"


#  Test with mixed parameters including credentials
def test_prestashop_shop_mixed_parameters(credentials):
    """Tests initialization with mixed parameters including credentials."""
    shop = PrestaShopShop(api_domain="another.domain", credentials=credentials, api_key = "another_key")
    assert shop.api_domain == "another.domain"
    assert shop.api_key == "another_key"
```