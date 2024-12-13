```python
import pytest
from unittest.mock import patch, MagicMock
from src.endpoints.prestashop.product import PrestaProduct
from types import SimpleNamespace

# Fixture definitions
@pytest.fixture
def valid_credentials():
    """Provides valid credentials for testing."""
    return SimpleNamespace(api_domain="test.domain.com", api_key="test_key")

@pytest.fixture
def api_domain():
    return "test.domain.com"

@pytest.fixture
def api_key():
    return "test_key"

@pytest.fixture
def mock_prestashop():
     """Mocks the PrestaShop API for testing."""
     with patch('src.endpoints.prestashop.product.PrestaShop.__init__', return_value=None) as mock_init:
        yield mock_init

# Test cases for PrestaProduct class initialization
def test_prestaproduct_init_valid_credentials(mock_prestashop, valid_credentials):
    """Checks successful initialization with valid credentials using SimpleNamespace."""
    product = PrestaProduct(credentials=valid_credentials)
    assert product.api_domain == "test.domain.com"
    assert product.api_key == "test_key"
    mock_prestashop.assert_called_once_with("test.domain.com", "test_key")

def test_prestaproduct_init_valid_credentials_dict(mock_prestashop, api_domain, api_key):
    """Checks successful initialization with valid credentials using dictionary."""
    credentials = {"api_domain": api_domain, "api_key": api_key}
    product = PrestaProduct(credentials=credentials)
    assert product.api_domain == api_domain
    assert product.api_key == api_key
    mock_prestashop.assert_called_once_with(api_domain, api_key)

def test_prestaproduct_init_explicit_credentials(mock_prestashop, api_domain, api_key):
    """Checks successful initialization with explicit api_domain and api_key."""
    product = PrestaProduct(api_domain=api_domain, api_key=api_key)
    assert product.api_domain == api_domain
    assert product.api_key == api_key
    mock_prestashop.assert_called_once_with(api_domain, api_key)

def test_prestaproduct_init_missing_credentials():
    """Checks ValueError when missing credentials."""
    with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
        PrestaProduct()

def test_prestaproduct_init_missing_api_domain(api_key):
    """Checks ValueError when missing api_domain."""
    with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
        PrestaProduct(api_key=api_key)

def test_prestaproduct_init_missing_api_key(api_domain):
    """Checks ValueError when missing api_key."""
    with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
        PrestaProduct(api_domain=api_domain)

def test_prestaproduct_init_credentials_override(mock_prestashop, valid_credentials, api_domain, api_key):
    """Checks that explicit parameters override values from credentials."""
    product = PrestaProduct(credentials=valid_credentials, api_domain=api_domain, api_key=api_key)
    assert product.api_domain == api_domain
    assert product.api_key == api_key
    mock_prestashop.assert_called_once_with(api_domain, api_key)
```