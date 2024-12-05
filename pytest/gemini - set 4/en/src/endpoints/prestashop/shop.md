```python
import pytest
from types import SimpleNamespace
from hypotez.src.endpoints.prestashop.shop import PrestaShopShop
from src.logger.exceptions import PrestaShopException


# Fixture for providing credentials
@pytest.fixture
def credentials():
    return SimpleNamespace(api_domain="test_domain", api_key="test_key")


# Valid input test cases
def test_prestashop_shop_valid_input(credentials):
    """Tests initialization with valid credentials."""
    shop = PrestaShopShop(credentials=credentials)
    assert shop.api_domain == "test_domain"
    assert shop.api_key == "test_key"


def test_prestashop_shop_valid_input_separate(credentials):
    """Tests initialization with valid separate parameters."""
    shop = PrestaShopShop(
        api_domain=credentials.api_domain, api_key=credentials.api_key
    )
    assert shop.api_domain == "test_domain"
    assert shop.api_key == "test_key"


# Invalid input (missing api_domain) test case
def test_prestashop_shop_invalid_input_missing_api_domain():
    """Tests initialization with missing api_domain."""
    credentials = SimpleNamespace(api_key="test_key")
    with pytest.raises(ValueError) as excinfo:
        PrestaShopShop(credentials=credentials)
    assert "Необходимы оба параметра: api_domain и api_key" in str(excinfo.value)


# Invalid input (missing api_key) test case
def test_prestashop_shop_invalid_input_missing_api_key():
    """Tests initialization with missing api_key."""
    credentials = SimpleNamespace(api_domain="test_domain")
    with pytest.raises(ValueError) as excinfo:
        PrestaShopShop(credentials=credentials)
    assert "Необходимы оба параметра: api_domain и api_key" in str(excinfo.value)


# Invalid input (empty string for api_domain)
def test_prestashop_shop_invalid_input_empty_api_domain():
    """Tests initialization with empty string for api_domain."""
    credentials = SimpleNamespace(api_domain="", api_key="test_key")
    with pytest.raises(ValueError) as excinfo:
        PrestaShopShop(credentials=credentials)
    assert "Необходимы оба параметра: api_domain и api_key" in str(excinfo.value)

#Invalid input (empty string for api_key)
def test_prestashop_shop_invalid_input_empty_api_key():
    """Tests initialization with empty string for api_key."""
    credentials = SimpleNamespace(api_domain="test_domain", api_key="")
    with pytest.raises(ValueError) as excinfo:
        PrestaShopShop(credentials=credentials)
    assert "Необходимы оба параметра: api_domain и api_key" in str(excinfo.value)



# Test with None values for api_domain and api_key to catch potential issues
def test_prestashop_shop_none_values():
    """Tests initialization with None values for api_domain and api_key."""
    with pytest.raises(ValueError) as excinfo:
        PrestaShopShop(api_domain=None, api_key=None)
    assert "Необходимы оба параметра: api_domain и api_key" in str(excinfo.value)


# Test with non-string values for api_domain
def test_prestashop_shop_invalid_domain_type():
    """Tests initialization with non-string value for api_domain."""
    with pytest.raises(TypeError):
        PrestaShopShop(api_domain=123, api_key="test_key")

# Test with non-string values for api_key
def test_prestashop_shop_invalid_key_type():
    """Tests initialization with non-string value for api_key."""
    with pytest.raises(TypeError):
        PrestaShopShop(api_domain="test_domain", api_key=123)
```