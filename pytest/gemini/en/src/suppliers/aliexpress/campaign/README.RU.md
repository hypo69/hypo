```python
import pytest
import os
# Replace with actual module if available
from pathlib import Path

# Dummy implementation for testing purposes. Replace with actual code.
class Campaign:
    def __init__(self, name, language, currency):
        self.name = name
        self.language = language
        self.currency = currency
        self.directory = None
        self.products = []

    def initialize(self, name, language, currency):
        self.name = name
        self.language = language
        self.currency = currency
        return self

    def create_directories(self):
        # Simulate directory creation
        self.directory = Path(f"campaign_{self.name}")
        self.directory.mkdir(parents=True, exist_ok=True)
        return self

    def save_config(self):
        # Simulate config saving
        with open(os.path.join(self.directory, "config.json"), "w") as f:
            f.write(f'{{"name": "{self.name}", "language": "{self.language}", "currency": "{self.currency}"}}')

    def collect_products(self, source="ali"):
      # Simulate product collection
      if source == "ali":
        self.products = [{"name": "Product 1", "price": 10}]
      elif source == "html":
        self.products = [{"name": "Product 2", "price": 20}]
      else:
        raise ValueError("Invalid source for product collection.")
      return self

    def save_products(self):
      # Simulate saving product data
      with open(os.path.join(self.directory, "products.json"), "w") as f:
        import json
        json.dump(self.products, f, indent=4)

    def create_ads(self):
        # Simulate ad creation
        pass

    def validate(self):
        # Simulate validation
        if not self.products:
          return False
        return True

    def publish(self):
        # Simulate Facebook publication
        print(f"Campaign '{self.name}' published successfully.")


def test_campaign_creation():
    campaign = Campaign("My Campaign", "en", "USD")
    assert campaign.name == "My Campaign"
    assert campaign.language == "en"
    assert campaign.currency == "USD"


def test_campaign_initialization():
    campaign = Campaign("Test Campaign", "fr", "EUR").initialize("New Name", "es", "USD")
    assert campaign.name == "New Name"
    assert campaign.language == "es"
    assert campaign.currency == "USD"


def test_campaign_directory_creation():
    campaign = Campaign("Test Campaign", "fr", "EUR").create_directories()
    assert os.path.exists(campaign.directory)


def test_campaign_config_saving():
    campaign = Campaign("Config Test", "de", "GBP").create_directories().save_config()
    with open(os.path.join(campaign.directory, "config.json"), "r") as f:
        data = f.read()
    assert '"name": "Config Test"' in data


def test_campaign_product_collection_ali():
    campaign = Campaign("Product Test", "fr", "EUR").collect_products("ali")
    assert len(campaign.products) == 1


def test_campaign_product_collection_invalid_source():
    with pytest.raises(ValueError):
        Campaign("Invalid Source", "fr", "EUR").collect_products("invalid")


def test_campaign_validation_no_products():
    campaign = Campaign("No Products", "fr", "EUR")
    assert not campaign.validate()


def test_campaign_validation_with_products():
    campaign = Campaign("Products Test", "fr", "EUR").collect_products("ali")
    assert campaign.validate()

def test_campaign_publication():
  campaign = Campaign("Pub Test", "fr", "EUR").create_directories().collect_products("ali").save_products().create_ads().validate()
  campaign.publish()
```