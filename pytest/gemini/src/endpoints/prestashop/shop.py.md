```python
import pytest
from unittest.mock import patch, MagicMock
from types import SimpleNamespace
from src.endpoints.prestashop.shop import PrestaShopShop
from src.logger.exceptions import PrestaShopException


# Fixture for valid credentials
@pytest.fixture
def valid_credentials():
    return {"api_domain": "test_domain", "api_key": "test_key"}

# Fixture for SimpleNamespace credentials
@pytest.fixture
def valid_credentials_namespace():
    return SimpleNamespace(api_domain="test_domain", api_key="test_key")

# Fixture for invalid credentials
@pytest.fixture
def invalid_credentials():
    return {}


# Test cases for PrestaShopShop class initialization
def test_prestashopshop_init_valid_credentials_dict(valid_credentials):
    """Test successful initialization with valid credentials dictionary."""
    shop = PrestaShopShop(credentials=valid_credentials)
    assert shop.api_domain == "test_domain"
    assert shop.api_key == "test_key"

def test_prestashopshop_init_valid_credentials_namespace(valid_credentials_namespace):
    """Test successful initialization with valid credentials namespace."""
    shop = PrestaShopShop(credentials=valid_credentials_namespace)
    assert shop.api_domain == "test_domain"
    assert shop.api_key == "test_key"

def test_prestashopshop_init_api_domain_and_key_provided(valid_credentials):
    """Test initialization with both api_domain and api_key provided."""
    shop = PrestaShopShop(api_domain='test_domain', api_key='test_key')
    assert shop.api_domain == "test_domain"
    assert shop.api_key == "test_key"

def test_prestashopshop_init_credentials_override_api_domain_key(valid_credentials):
    """Test that credentials override direct api_domain and api_key parameters."""
    shop = PrestaShopShop(credentials=valid_credentials, api_domain='override_domain', api_key='override_key')
    assert shop.api_domain == "test_domain"
    assert shop.api_key == "test_key"

def test_prestashopshop_init_missing_credentials():
    """Test initialization fails with missing credentials."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaShopShop()

def test_prestashopshop_init_missing_api_domain(valid_credentials):
    """Test initialization fails with missing api_domain in credentials."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
         PrestaShopShop(credentials={'api_key': 'test_key'})
        
def test_prestashopshop_init_missing_api_key(valid_credentials):
    """Test initialization fails with missing api_key in credentials."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
         PrestaShopShop(credentials={'api_domain': 'test_domain'})

def test_prestashopshop_init_with_none_credentials_and_no_api_domain_key():
    """Test initialization fails with None credentials and no api_domain and api_key."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaShopShop(credentials = None)

def test_prestashopshop_init_with_none_credentials_and_api_domain_key():
    """Test initialization with None credentials and api_domain and api_key params."""
    shop = PrestaShopShop(credentials = None, api_domain='test_domain', api_key='test_key')
    assert shop.api_domain == "test_domain"
    assert shop.api_key == "test_key"

@patch("src.endpoints.prestashop.shop.PrestaShop.__init__")
def test_prestashopshop_init_calls_parent_init(mock_super_init, valid_credentials):
    """Test that the parent's __init__ method is called."""
    PrestaShopShop(credentials=valid_credentials)
    mock_super_init.assert_called_once_with('test_domain', 'test_key')

@patch("src.endpoints.prestashop.shop.PrestaShop.__init__")
def test_prestashopshop_init_calls_parent_init_with_args_kwargs(mock_super_init, valid_credentials):
    """Test that the parent's __init__ method is called with args and kwargs."""
    PrestaShopShop(credentials=valid_credentials, arg1=1, kwarg1='test')
    mock_super_init.assert_called_once_with('test_domain', 'test_key', arg1=1, kwarg1='test')

```