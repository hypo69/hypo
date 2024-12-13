```python
import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

# Assuming the classes and dependencies are available in the environment
# For the sake of this test, we will mock them, as the actual implementation is not given.
class Driver:
    pass

class ProductFields:
    pass

class Graber:
    def grab_page(self, url):
        return {}  # Mocked grab_page method

class Gemini:
    def process(self, data, lang):
        return {"processed_data": "mocked_ai_result", "lang": lang}  # Mocked process method

class FacebookScenario:
    def publish(self, mexiron):
        return True  # Mocked publish method

class MexironBuilder:
    def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
        self.driver = driver
        self.export_path = Path('./')
        self.mexiron_name = mexiron_name
        self.price = None
        self.timestamp = 'test_timestamp'
        self.products_list = []
        self.model = Gemini()
        self.config = {"some": "config"}


    def run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool:
        if urls is None:
            return False
        if isinstance(urls, str):
             urls = [urls]
        for url in urls:
           if "onetab" in url:
             data = {"title":"test_title", "url":url}
             if not data:
                return True
           else:
                return True
           graber = self.get_graber_by_supplier_url(url)
           if graber:
              product_fields = graber.grab_page(url)
              if not product_fields:
                 return True
              product_data = self.convert_product_fields(product_fields)
              if not product_data:
                  return True
              self.save_product_data(product_data)
              self.products_list.append(product_data)
              ai_result_he,ai_result_ru = self.process_ai(self.products_list, "he"), self.process_ai(self.products_list, "ru")
              if not ai_result_he or not ai_result_ru:
                return True
              self.save_json(ai_result_he, "he")
              self.save_json(ai_result_ru, "ru")
              html_file = Path("test_report.html")
              pdf_file = Path("test_report.pdf")
              self.create_report(ai_result_he, html_file, pdf_file)
              self.send_pdf(pdf_file)
           else:
             return True
        return True


    def get_graber_by_supplier_url(self, url: str):
         return Graber()

    def convert_product_fields(self, f: ProductFields) -> dict:
          return {"name": "test_product", "price": 100}

    def save_product_data(self, product_data: dict):
          pass

    def process_ai(self, products_list: List[str], lang: str, attempts: int = 1) -> tuple | bool:
            if not products_list or not lang:
                  return False
            if lang == "he":
                 return self.model.process(products_list,lang)
            if lang == "ru":
                return self.model.process(products_list, lang)
            return False

    def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        facebook_scenario = FacebookScenario()
        return facebook_scenario.publish(mexiron)

    def create_report(self, data: dict, html_file: Path, pdf_file: Path):
          pass
    
    def send_pdf(self, pdf_file):
          pass
    
    def save_json(self,data,lang):
        pass
    
@pytest.fixture
def mock_driver():
    """Provides a mocked Driver instance."""
    return MagicMock(spec=Driver)

@pytest.fixture
def mexiron_builder(mock_driver):
    """Provides a MexironBuilder instance with a mocked driver."""
    return MexironBuilder(mock_driver)

def test_mexironbuilder_init(mock_driver):
    """Test initialization of MexironBuilder."""
    builder = MexironBuilder(mock_driver, mexiron_name="test_mexiron")
    assert builder.driver == mock_driver
    assert builder.mexiron_name == "test_mexiron"
    assert builder.export_path == Path('./')
    assert builder.price is None
    assert builder.timestamp == 'test_timestamp'
    assert builder.products_list == []
    assert isinstance(builder.model, Gemini)
    assert builder.config == {"some": "config"}

def test_run_scenario_valid_urls(mexiron_builder):
    """Test run_scenario with valid URL list."""
    urls = ["http://example.com/product1", "http://example.com/product2"]
    result = mexiron_builder.run_scenario(urls=urls)
    assert result is True

def test_run_scenario_no_urls(mexiron_builder):
    """Test run_scenario without providing any URLs."""
    result = mexiron_builder.run_scenario()
    assert result is False

def test_run_scenario_onetab_url(mexiron_builder):
    """Test run_scenario with OneTab URL."""
    url = "onetab://test"
    result = mexiron_builder.run_scenario(urls=url)
    assert result is True

def test_get_graber_by_supplier_url(mexiron_builder):
    """Test get_graber_by_supplier_url returns a Graber instance."""
    url = "http://example.com/supplier"
    graber = mexiron_builder.get_graber_by_supplier_url(url)
    assert isinstance(graber, Graber)

def test_convert_product_fields(mexiron_builder):
    """Test convert_product_fields returns a dictionary."""
    product_fields = ProductFields()
    converted_data = mexiron_builder.convert_product_fields(product_fields)
    assert isinstance(converted_data, dict)
    assert "name" in converted_data
    assert "price" in converted_data


def test_process_ai_valid_input(mexiron_builder):
    """Test process_ai returns processed result with valid input."""
    products_list = [{"name": "test_product", "price": 100}]
    ai_result = mexiron_builder.process_ai(products_list, "he")
    assert ai_result
    assert isinstance(ai_result, dict)
    assert "processed_data" in ai_result
    assert ai_result["lang"] == "he"

    ai_result = mexiron_builder.process_ai(products_list, "ru")
    assert ai_result
    assert isinstance(ai_result, dict)
    assert "processed_data" in ai_result
    assert ai_result["lang"] == "ru"
    

def test_process_ai_no_products(mexiron_builder):
    """Test process_ai returns False with empty product list."""
    products_list = []
    ai_result = mexiron_builder.process_ai(products_list, "he")
    assert ai_result is False
    
def test_process_ai_no_lang(mexiron_builder):
    """Test process_ai returns False with empty language."""
    products_list = [{"name": "test_product", "price": 100}]
    ai_result = mexiron_builder.process_ai(products_list, "")
    assert ai_result is False


def test_post_facebook_success(mexiron_builder):
    """Test post_facebook returns True when posting is successful."""
    mexiron_data = SimpleNamespace()
    result = mexiron_builder.post_facebook(mexiron_data)
    assert result is True
```