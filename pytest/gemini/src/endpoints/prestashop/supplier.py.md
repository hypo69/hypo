```python
import pytest
from types import SimpleNamespace
from src.endpoints.prestashop.supplier import PrestaSupplier
from src.endpoints.prestashop.api import PrestaShop  # Assuming PrestaShop is in api.py

# Fixture for valid credentials
@pytest.fixture
def valid_credentials():
    """Provides valid credentials for testing."""
    return {"api_domain": "test.prestashop.com", "api_key": "test_api_key"}

# Fixture for invalid credentials
@pytest.fixture
def invalid_credentials():
    """Provides invalid credentials for testing."""
    return {}

# Fixture for valid credentials as SimpleNamespace
@pytest.fixture
def valid_credentials_ns():
    """Provides valid credentials as SimpleNamespace for testing."""
    return SimpleNamespace(api_domain="test.prestashop.com", api_key="test_api_key")

# Tests for PrestaSupplier.__init__
def test_prestasuplier_init_valid_credentials_dict(valid_credentials):
    """Checks successful initialization with valid credentials as dict."""
    supplier = PrestaSupplier(credentials=valid_credentials)
    assert supplier.api_domain == valid_credentials["api_domain"]
    assert supplier.api_key == valid_credentials["api_key"]

def test_prestasuplier_init_valid_credentials_separate_args(valid_credentials):
    """Checks successful initialization with valid credentials as separate args."""
    supplier = PrestaSupplier(api_domain=valid_credentials["api_domain"], api_key=valid_credentials["api_key"])
    assert supplier.api_domain == valid_credentials["api_domain"]
    assert supplier.api_key == valid_credentials["api_key"]

def test_prestasuplier_init_valid_credentials_simplenamespace(valid_credentials_ns):
    """Checks successful initialization with valid credentials as SimpleNamespace."""
    supplier = PrestaSupplier(credentials=valid_credentials_ns)
    assert supplier.api_domain == valid_credentials_ns.api_domain
    assert supplier.api_key == valid_credentials_ns.api_key

def test_prestasuplier_init_invalid_credentials_missing_domain(invalid_credentials):
    """Checks exception when missing api_domain."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
         PrestaSupplier(credentials=invalid_credentials, api_key="some_key")
         
def test_prestasuplier_init_invalid_credentials_missing_key(invalid_credentials):
    """Checks exception when missing api_key."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaSupplier(credentials=invalid_credentials, api_domain="some_domain")

def test_prestasuplier_init_no_credentials_no_args():
    """Checks exception when missing all credentials and arguments"""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaSupplier()

def test_prestasuplier_init_empty_credentials_dict():
     """Checks exception when credentials are empty dict"""
     with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
         PrestaSupplier(credentials={})

def test_prestasuplier_init_with_extra_args(valid_credentials):
     """Checks init with extra args for compatibility"""
     supplier = PrestaSupplier(credentials=valid_credentials, extra="test_extra_arg")
     assert hasattr(supplier, 'extra') == False
     assert supplier.api_domain == valid_credentials["api_domain"]
     assert supplier.api_key == valid_credentials["api_key"]

def test_prestasuplier_init_with_none_credentials(valid_credentials):
    """Checks if api_domain and api_key are correctly taken from positional arguments if credentials are None"""
    supplier = PrestaSupplier(credentials=None, api_domain=valid_credentials["api_domain"], api_key=valid_credentials["api_key"])
    assert supplier.api_domain == valid_credentials["api_domain"]
    assert supplier.api_key == valid_credentials["api_key"]

def test_prestasuplier_init_with_empty_string_credentials(invalid_credentials):
    """Checks exception when credentials has empty strings"""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaSupplier(credentials={"api_domain":"", "api_key":""})
```