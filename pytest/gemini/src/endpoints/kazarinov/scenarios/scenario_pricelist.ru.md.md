```python
import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

# Assuming the necessary classes and functions are in these paths
# from src.webdriver.driver import Driver  # Mocked
# from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder, ProductFields # Mocked


# Mock the necessary classes and functions
class MockDriver:
    def __init__(self):
        pass

class MockProductFields:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class MockGraber:
    def grab_page(self, url):
        return {"title": "Test Product", "price": 100}


class MockGemini:
    def process(self, text, lang):
        if lang == 'ru':
            return f"AI processed ru: {text}"
        if lang == 'he':
            return f"AI processed he: {text}"
        return f"AI processed: {text}"


class MockFacebook:
    def post(self, data):
        return True


@pytest.fixture
def mock_driver():
    return MockDriver()

@pytest.fixture
def mock_mexiron_builder(mock_driver):
    # Mock dependencies for MexironBuilder
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.Driver', return_value=mock_driver), \
            patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.Gemini', return_value=MockGemini()), \
            patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.Facebook', return_value=MockFacebook()):
        from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
        return MexironBuilder(driver=mock_driver)

@pytest.fixture
def example_product_fields():
    return MockProductFields(title="Test Product", price=100)


def test_mexironbuilder_initialization(mock_driver):
    """Test the initialization of MexironBuilder with driver and optional name."""
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
    mexiron_builder = MexironBuilder(driver=mock_driver, mexiron_name="test_mexiron")
    assert mexiron_builder.driver == mock_driver
    assert mexiron_builder.mexiron_name == "test_mexiron"
    assert mexiron_builder.products_list == []
    assert mexiron_builder.timestamp is not None


def test_run_scenario_valid_urls(mock_mexiron_builder, example_product_fields):
    """Test run_scenario with valid URLs, checking if the data is processed."""

    with patch.object(mock_mexiron_builder, 'get_graber_by_supplier_url', return_value=MockGraber()), \
        patch.object(mock_mexiron_builder, 'convert_product_fields', return_value={'title': 'Test Product', 'price': 100}), \
        patch.object(mock_mexiron_builder, 'save_product_data', return_value=True), \
        patch.object(mock_mexiron_builder, 'process_ai', return_value=(f"AI processed ru: {[{'title': 'Test Product', 'price': 100}]}", f"AI processed he: {[{'title': 'Test Product', 'price': 100}]}")), \
        patch.object(mock_mexiron_builder, 'create_report', return_value=True), \
        patch.object(mock_mexiron_builder, 'post_facebook', return_value=True):
        
        urls = ["https://example.com/product1", "https://example.com/product2"]
        result = mock_mexiron_builder.run_scenario(urls=urls)
        assert result is True
        assert len(mock_mexiron_builder.products_list) == 2


def test_run_scenario_no_urls(mock_mexiron_builder):
    """Test run_scenario with no URLs provided. Should log and return True."""
    result = mock_mexiron_builder.run_scenario()
    assert result is True
    assert mock_mexiron_builder.products_list == []


def test_run_scenario_no_graber(mock_mexiron_builder):
    """Test run_scenario when no graber is found for a URL."""
    with patch.object(mock_mexiron_builder, 'get_graber_by_supplier_url', return_value=None):
        urls = ["https://example.com/product1"]
        result = mock_mexiron_builder.run_scenario(urls=urls)
        assert result is True
        assert mock_mexiron_builder.products_list == []


def test_run_scenario_parsing_failed(mock_mexiron_builder):
    """Test run_scenario when parsing the product fails."""
    with patch.object(mock_mexiron_builder, 'get_graber_by_supplier_url', return_value=MockGraber()), \
         patch.object(mock_mexiron_builder, 'convert_product_fields', return_value=None):
        urls = ["https://example.com/product1"]
        result = mock_mexiron_builder.run_scenario(urls=urls)
        assert result is True
        assert mock_mexiron_builder.products_list == []


def test_run_scenario_conversion_failed(mock_mexiron_builder):
    """Test run_scenario when product fields conversion fails."""
    with patch.object(mock_mexiron_builder, 'get_graber_by_supplier_url', return_value=MockGraber()), \
         patch.object(mock_mexiron_builder, 'convert_product_fields', side_effect=Exception("Conversion failed")):
        urls = ["https://example.com/product1"]
        result = mock_mexiron_builder.run_scenario(urls=urls)
        assert result is True
        assert mock_mexiron_builder.products_list == []


def test_run_scenario_save_data_fails(mock_mexiron_builder):
    """Test run_scenario when product data saving fails."""
    with patch.object(mock_mexiron_builder, 'get_graber_by_supplier_url', return_value=MockGraber()), \
         patch.object(mock_mexiron_builder, 'convert_product_fields', return_value={'title': 'Test Product', 'price': 100}), \
         patch.object(mock_mexiron_builder, 'save_product_data', return_value=False):
        urls = ["https://example.com/product1"]
        result = mock_mexiron_builder.run_scenario(urls=urls)
        assert result is True
        assert mock_mexiron_builder.products_list == []


def test_get_graber_by_supplier_url_found(mock_mexiron_builder):
    """Test get_graber_by_supplier_url when a graber is found."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.supplier_graber_mapping', return_value={'example.com': MockGraber}):
        graber = mock_mexiron_builder.get_graber_by_supplier_url("https://example.com/product1")
        assert isinstance(graber, MockGraber)


def test_get_graber_by_supplier_url_not_found(mock_mexiron_builder):
    """Test get_graber_by_supplier_url when no graber is found."""
    with patch('src.endpoints.kazarinov.scenarios.scenario_pricelist.supplier_graber_mapping', return_value={}):
        graber = mock_mexiron_builder.get_graber_by_supplier_url("https://unknown.com/product1")
        assert graber is None


def test_convert_product_fields_valid_input(mock_mexiron_builder, example_product_fields):
    """Test convert_product_fields with valid input."""
    product_data = mock_mexiron_builder.convert_product_fields(example_product_fields)
    assert isinstance(product_data, dict)
    assert product_data['title'] == "Test Product"
    assert product_data['price'] == 100


def test_save_product_data(mock_mexiron_builder):
    """Test save_product_data to ensure it saves to a file."""
    product_data = {"title": "Test Product", "price": 100}
    with patch("src.endpoints.kazarinov.scenarios.scenario_pricelist.Path.open",  MagicMock()):
      mock_mexiron_builder.save_product_data(product_data)
    #  Add asserts to check file write
    
def test_process_ai_valid_input(mock_mexiron_builder):
    """Test process_ai with valid input and ensure it returns processed text."""
    products_list = [{"title": "Test Product", "price": 100}]
    
    result_ru, result_he = mock_mexiron_builder.process_ai(str(products_list), lang='ru')
    assert result_ru == f"AI processed ru: {str(products_list)}"
    
    result_ru, result_he = mock_mexiron_builder.process_ai(str(products_list), lang='he')
    assert result_he == f"AI processed he: {str(products_list)}"


def test_post_facebook_success(mock_mexiron_builder):
    """Test post_facebook with successful post."""
    mexiron_data = SimpleNamespace(test='data')
    assert mock_mexiron_builder.post_facebook(mexiron_data) is True


def test_create_report_success(mock_mexiron_builder):
    """Test create_report to check if file operations are called."""
    data = {"test": "data"}
    html_file = Path("test.html")
    pdf_file = Path("test.pdf")

    with patch("src.endpoints.kazarinov.scenarios.scenario_pricelist.Path.open", MagicMock()), \
        patch("src.endpoints.kazarinov.scenarios.scenario_pricelist.pdfkit.from_string", MagicMock()):
            mock_mexiron_builder.create_report(data, html_file, pdf_file)


def test_run_scenario_from_onetab(mock_mexiron_builder):
    """Test run_scenario when a URL is from OneTab."""
    with patch.object(mock_mexiron_builder, 'get_graber_by_supplier_url', return_value=MockGraber()), \
          patch.object(mock_mexiron_builder, 'convert_product_fields', return_value={'title': 'Test Product', 'price': 100}), \
            patch.object(mock_mexiron_builder, 'save_product_data', return_value=True), \
            patch.object(mock_mexiron_builder, 'process_ai', return_value=(f"AI processed ru: {[{'title': 'Test Product', 'price': 100}]}", f"AI processed he: {[{'title': 'Test Product', 'price': 100}]}")), \
          patch.object(mock_mexiron_builder, 'create_report', return_value=True), \
        patch.object(mock_mexiron_builder, 'post_facebook', return_value=True):
        urls = "onetab:https://example.com/product1,https://example.com/product2"
        result = mock_mexiron_builder.run_scenario(urls=urls)
        assert result is True
        assert len(mock_mexiron_builder.products_list) == 2
```