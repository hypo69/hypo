```python
import pytest

from hypotez.src.suppliers.wallmart import Graber  # Assuming Graber is defined in graber.py


# Fixture definitions, if needed
@pytest.fixture
def example_url():
    """Provides a sample URL for testing."""
    return "https://www.walmart.com/browse/electronics/c3_3944"


@pytest.fixture
def example_invalid_url():
    """Provides a sample invalid URL for testing."""
    return "invalid_url"


# Tests for Graber class
def test_graber_initialization():
    """Checks if the Graber class can be instantiated without errors."""
    try:
        graber = Graber()
    except Exception as e:
        pytest.fail(f"Graber initialization failed with exception: {e}")
    assert isinstance(graber, Graber)


def test_graber_extract_product_urls_valid_url(example_url):
    """Checks if extract_product_urls returns a non-empty list with a valid URL."""
    graber = Graber()
    product_urls = graber.extract_product_urls(example_url)
    assert isinstance(product_urls, list)
    assert len(product_urls) > 0


def test_graber_extract_product_urls_invalid_url(example_invalid_url):
    """Checks if extract_product_urls returns an empty list with an invalid URL."""
    graber = Graber()
    product_urls = graber.extract_product_urls(example_invalid_url)
    assert isinstance(product_urls, list)
    assert len(product_urls) == 0


def test_graber_extract_product_urls_edge_case_empty_url():
    """Checks if extract_product_urls returns an empty list with an empty URL."""
    graber = Graber()
    product_urls = graber.extract_product_urls("")
    assert isinstance(product_urls, list)
    assert len(product_urls) == 0


def test_graber_extract_product_details_valid_url_and_product_url(example_url):
    """Checks if extract_product_details can return details for a valid product URL.
    This requires that extract_product_urls works correctly.
    """
    graber = Graber()
    product_urls = graber.extract_product_urls(example_url)
    if product_urls:
        details = graber.extract_product_details(product_urls[0])
        assert isinstance(details, dict)
        assert "name" in details
        assert "price" in details
        assert "image_url" in details
    else:
        pytest.skip("No product URLs found to test extract_product_details.")


def test_graber_extract_product_details_invalid_url():
    """Checks if extract_product_details returns an empty dict when an invalid URL is provided."""
    graber = Graber()
    details = graber.extract_product_details("invalid_product_url")
    assert isinstance(details, dict)
    assert not details


def test_graber_extract_product_details_edge_case_none_url():
    """Checks if extract_product_details returns an empty dict when None is provided."""
    graber = Graber()
    details = graber.extract_product_details(None)
    assert isinstance(details, dict)
    assert not details
```