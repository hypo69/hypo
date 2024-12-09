```python
import pytest
import os

# Replace with actual code from the 'campaign' module
class Campaign:
    def __init__(self, name, language, currency):
        self.name = name
        self.language = language
        self.currency = currency
        self.data = {}

    def initialize_campaign(self, name, language, currency):
      if not all([name, language, currency]):
        raise ValueError("All parameters are required")
      self.name = name
      self.language = language
      self.currency = currency
      return True

    def create_directories(self):
      # Simulate directory creation
      os.makedirs(f"campaign_{self.name}", exist_ok=True)
      os.makedirs(f"campaign_{self.name}/categories", exist_ok=True)
      return True

    def save_config(self):
      # Simulate saving config
      with open(f"campaign_{self.name}/config.json", "w") as f:
          f.write(f'{{"name": "{self.name}", "language": "{self.language}", "currency": "{self.currency}"}}')
      return True

    def collect_product_data(self, source="ali"):
        # Simulate collecting data
        if source == "ali":
            self.data = {"products": [{"name": "Product 1", "price": 10}]}
        elif source == "html":
            self.data = {"products": [{"name": "Product 2", "price": 20}]}
        else:
            raise ValueError("Invalid data source")
        return True

    def save_product_data(self):
        # Simulate saving data
        with open(f"campaign_{self.name}/products.json", "w") as f:
            import json
            json.dump(self.data, f, indent=4)
        return True

    def generate_materials(self):
        # Simulate material generation
        return True

    def validate_campaign(self):
        # Simulate validation
        return True  # True if valid, False otherwise


# Fixture definitions
@pytest.fixture
def campaign():
    return Campaign("TestCampaign", "en", "USD")


# Tests for Campaign Class
def test_initialize_campaign_valid_input(campaign):
    assert campaign.initialize_campaign("TestName", "fr", "EUR") == True


def test_initialize_campaign_missing_input(campaign):
    with pytest.raises(ValueError, match="All parameters are required"):
        campaign.initialize_campaign("", "", "")


def test_create_directories(campaign):
  #This test will not fail as it simulates directory creation; actual directory creation is outside the scope
  assert campaign.create_directories() == True

def test_save_config(campaign):
  campaign.initialize_campaign("TestCampaign", "en", "USD")
  assert campaign.save_config() == True


def test_collect_product_data_ali(campaign):
    assert campaign.collect_product_data("ali") == True

def test_collect_product_data_invalid(campaign):
    with pytest.raises(ValueError, match="Invalid data source"):
        campaign.collect_product_data("invalid")


def test_save_product_data(campaign):
    campaign.collect_product_data("ali")
    assert campaign.save_product_data() == True

def test_generate_materials(campaign):
    assert campaign.generate_materials() == True

def test_validate_campaign(campaign):
    assert campaign.validate_campaign() == True
```