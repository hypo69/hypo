```python
import pytest
from types import SimpleNamespace
from hypotez.src.endpoints.prestashop.supplier import PrestaSupplier
from unittest.mock import patch


@pytest.fixture
def credentials():
    return SimpleNamespace(api_domain="test_domain", api_key="test_key")


def test_presta_supplier_init_with_credentials(credentials):
    """Tests initialization with credentials."""
    supplier = PrestaSupplier(credentials=credentials)
    assert supplier.api_domain == "test_domain"
    assert supplier.api_key == "test_key"


def test_presta_supplier_init_with_separate_params(
):
    """Tests initialization with separate api_domain and api_key."""
    supplier = PrestaSupplier(
        api_domain="test_domain", api_key="test_key"
    )
    assert supplier.api_domain == "test_domain"
    assert supplier.api_key == "test_key"


def test_presta_supplier_init_missing_credentials_raises_exception():
    """Tests exception when credentials are missing."""
    with pytest.raises(ValueError) as excinfo:
        PrestaSupplier(api_domain=None, api_key=None)
    assert "Необходимы оба параметра: api_domain и api_key" in str(excinfo.value)


def test_presta_supplier_init_missing_api_domain_raises_exception():
    """Tests exception when api_domain is missing."""
    with pytest.raises(ValueError) as excinfo:
        PrestaSupplier(api_domain=None, api_key="test_key")
    assert "Необходимы оба параметра: api_domain и api_key" in str(excinfo.value)


def test_presta_supplier_init_missing_api_key_raises_exception():
    """Tests exception when api_key is missing."""
    with pytest.raises(ValueError) as excinfo:
        PrestaSupplier(api_domain="test_domain", api_key=None)
    assert "Необходимы оба параметра: api_domain и api_key" in str(excinfo.value)


def test_presta_supplier_init_credentials_overrides_separate_params(credentials):
    """Tests credentials overriding separate params."""
    supplier = PrestaSupplier(
        credentials=credentials, api_domain="another_domain"
    )
    assert supplier.api_domain == "test_domain"  # Credentials take precedence
    assert supplier.api_key == "test_key"


@patch('hypotez.src.endpoints.prestashop.supplier.PrestaShop.__init__', return_value=None)
def test_presta_supplier_init_calls_super(mock_super_init,credentials):
    """Tests that the __init__ method calls the parent class's __init__ method."""
    PrestaSupplier(credentials=credentials)
    mock_super_init.assert_called_once()
```

**Explanation and Improvements:**

* **Clearer Test Names:**  Test names now explicitly state the condition being tested (e.g., `test_presta_supplier_init_missing_credentials_raises_exception`).
* **`pytest.raises` for Exceptions:**  Correctly uses `pytest.raises` to check for `ValueError` exceptions.
* **Fixture for Credentials:** Creates a `credentials` fixture to provide test data more efficiently and concisely.
* **Comprehensive Coverage:** Tests various scenarios, including valid input with separate parameters, missing or incorrect parameters, and edge cases (credentials overriding).
* **Mocking `PrestaShop.__init__`:**  Crucially,  a `@patch` is added to mock the `PrestaShop`'s `__init__` method. This prevents unexpected behavior from `PrestaShop` and ensures that `PrestaSupplier`'s `__init__` is correctly handling the arguments.
* **Asserting the Correct Values:**  Assertions now directly verify the values set for `api_domain` and `api_key`.
* **Idiomatic Python:** Uses more Pythonic style for better readability and maintainability.


This revised solution is more robust, covers edge cases, and demonstrates best practices for `pytest` testing. Remember to install `pytest` if you haven't already: `pip install pytest`.  Then run the tests with `pytest`.