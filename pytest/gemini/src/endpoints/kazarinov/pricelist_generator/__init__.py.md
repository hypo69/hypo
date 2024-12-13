```python
import pytest

from hypotez.src.endpoints.kazarinov.pricelist_generator import ReportGenerator


# Fixture definitions, if needed
@pytest.fixture
def mock_report_generator():
    """Provides a mock ReportGenerator object for testing."""
    return ReportGenerator()


# Tests for ReportGenerator class
def test_report_generator_initialization(mock_report_generator):
    """Checks if ReportGenerator is initialized correctly."""
    assert isinstance(mock_report_generator, ReportGenerator)


def test_report_generator_default_mode():
    """Checks if default mode is set correctly"""
    assert ReportGenerator.MODE == 'dev'


# Test that MODE constant is initialized correctly
def test_mode_constant():
    """Checks that the MODE constant is initialized correctly."""
    from hypotez.src.endpoints.kazarinov.pricelist_generator import MODE

    assert MODE == 'dev'
```