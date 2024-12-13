```python
import pytest
from unittest.mock import patch, MagicMock
from types import SimpleNamespace
from src.endpoints.prestashop.customer import PrestaCustomer
from src.logger.exceptions import PrestaShopException
from pytest import raises


@pytest.fixture
def mock_prestashop():
    """Mocks the PrestaShop base class for testing."""
    with patch('src.endpoints.prestashop.customer.PrestaShop.__init__', return_value=None) as mock:
      yield mock

def test_prestacustomer_init_with_credentials_dict(mock_prestashop):
    """Test initialization with credentials as a dictionary."""
    credentials = {'api_domain': 'test_domain', 'api_key': 'test_key'}
    customer = PrestaCustomer(credentials=credentials)
    mock_prestashop.assert_called_once_with('test_domain', 'test_key')

def test_prestacustomer_init_with_credentials_simplenamespace(mock_prestashop):
    """Test initialization with credentials as a SimpleNamespace."""
    credentials = SimpleNamespace(api_domain='test_domain', api_key='test_key')
    customer = PrestaCustomer(credentials=credentials)
    mock_prestashop.assert_called_once_with('test_domain', 'test_key')

def test_prestacustomer_init_with_explicit_params(mock_prestashop):
    """Test initialization with explicit api_domain and api_key."""
    customer = PrestaCustomer(api_domain='test_domain', api_key='test_key')
    mock_prestashop.assert_called_once_with('test_domain', 'test_key')


def test_prestacustomer_init_missing_api_domain(mock_prestashop):
    """Test initialization with missing api_domain."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaCustomer(api_key='test_key')

def test_prestacustomer_init_missing_api_key(mock_prestashop):
    """Test initialization with missing api_key."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaCustomer(api_domain='test_domain')

def test_prestacustomer_init_missing_both_params(mock_prestashop):
    """Test initialization with missing both api_domain and api_key."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaCustomer()


def test_prestacustomer_init_credentials_override_explicit(mock_prestashop):
    """Test that credentials override explicit api_domain and api_key if both are provided."""
    credentials = {'api_domain': 'credentials_domain', 'api_key': 'credentials_key'}
    customer = PrestaCustomer(credentials=credentials, api_domain='explicit_domain', api_key='explicit_key')
    mock_prestashop.assert_called_once_with('credentials_domain', 'credentials_key')
```