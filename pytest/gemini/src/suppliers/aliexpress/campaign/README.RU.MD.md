```python
import pytest
import os
import shutil
from pathlib import Path
from unittest.mock import patch, mock_open

# Assuming the code described in the README.RU.MD is implemented in a class or module
# named 'campaign_manager'. This is a placeholder. You'll need to adapt it
# to your actual implementation
from hypotez.src.suppliers.aliexpress.campaign.campaign_manager import CampaignManager

# Fixture definitions, if needed
@pytest.fixture
def campaign_manager_instance():
    """Provides an instance of the CampaignManager class."""
    return CampaignManager()

@pytest.fixture
def base_campaign_dir(tmp_path):
    """Provides a temporary directory for the campaign."""
    base_dir = tmp_path / "campaigns"
    os.makedirs(base_dir, exist_ok=True)
    return base_dir


# Tests for Initialization
def test_init_campaign_parameters(campaign_manager_instance):
    """Checks correct initialization of campaign parameters."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    assert campaign_manager_instance.campaign_name == "test_campaign"
    assert campaign_manager_instance.campaign_language == "en"
    assert campaign_manager_instance.campaign_currency == "USD"


def test_init_campaign_parameters_empty_name(campaign_manager_instance):
     """Checks handling of an empty campaign name."""
     with pytest.raises(ValueError, match="Campaign name cannot be empty"):
         campaign_manager_instance.init_campaign_parameters(name="", language="en", currency="USD")


def test_init_campaign_parameters_invalid_language(campaign_manager_instance):
    """Checks handling of an invalid language code."""
    with pytest.raises(ValueError, match="Invalid language code format"):
       campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="invalid", currency="USD")


def test_init_campaign_parameters_invalid_currency(campaign_manager_instance):
    """Checks handling of an invalid currency code."""
    with pytest.raises(ValueError, match="Invalid currency code format"):
       campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="invalid")



# Tests for Directory Creation
def test_create_campaign_directories(campaign_manager_instance, base_campaign_dir):
    """Checks creation of campaign directories."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    campaign_manager_instance.base_dir = base_campaign_dir
    campaign_manager_instance.create_campaign_directories()

    expected_campaign_path = base_campaign_dir / "test_campaign"
    assert os.path.exists(expected_campaign_path)
    assert os.path.exists(expected_campaign_path / "categories")
    assert os.path.exists(expected_campaign_path / "config")
    assert os.path.exists(expected_campaign_path / "products")


def test_create_campaign_directories_existing_dir(campaign_manager_instance, base_campaign_dir):
    """Checks that function does not overwrite existing directory."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    campaign_manager_instance.base_dir = base_campaign_dir
    campaign_manager_instance.create_campaign_directories()

    expected_campaign_path = base_campaign_dir / "test_campaign"
    assert os.path.exists(expected_campaign_path)
    
    # try to create again
    campaign_manager_instance.create_campaign_directories()
    
    assert os.path.exists(expected_campaign_path) # should still be there
    
def test_create_campaign_directories_base_dir_not_set(campaign_manager_instance):
    """Check that error is raised when base_dir is not set."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    with pytest.raises(ValueError, match="Base directory is not set"):
        campaign_manager_instance.create_campaign_directories()



# Tests for Configuration Saving
@patch("builtins.open", new_callable=mock_open)
def test_save_campaign_config(mock_file, campaign_manager_instance, base_campaign_dir):
    """Checks saving of campaign configuration."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    campaign_manager_instance.base_dir = base_campaign_dir
    campaign_manager_instance.create_campaign_directories()
    campaign_manager_instance.save_campaign_config()

    mock_file.assert_called_with(base_campaign_dir / "test_campaign" / "config" / "config.json", "w")
    handle = mock_file()
    handle.write.assert_called()


def test_save_campaign_config_no_config_dir(campaign_manager_instance, base_campaign_dir):
    """Checks saving config fails when no config dir exists."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    campaign_manager_instance.base_dir = base_campaign_dir

    with pytest.raises(FileNotFoundError, match="No such file or directory"):
        campaign_manager_instance.save_campaign_config()

def test_save_campaign_config_no_base_dir(campaign_manager_instance):
    """Check that error is raised when base_dir is not set."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    with pytest.raises(ValueError, match="Base directory is not set"):
         campaign_manager_instance.save_campaign_config()


# Tests for Product Data Collection and Storage (Mocked for demonstration)
@patch('hypotez.src.suppliers.aliexpress.campaign.campaign_manager.CampaignManager.collect_product_data')
def test_collect_and_save_products(mock_collect, campaign_manager_instance, base_campaign_dir):
    """Checks collection and saving of product data."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    campaign_manager_instance.base_dir = base_campaign_dir
    campaign_manager_instance.create_campaign_directories()
    
    mock_collect.return_value = [{"product_id": 123, "name": "test_product"}]

    campaign_manager_instance.collect_and_save_products(source="ali", query="test")
    
    mock_collect.assert_called_once()
    
    product_file_path = base_campaign_dir / "test_campaign" / "products" / "products.json"
    assert os.path.exists(product_file_path)

    with open(product_file_path, 'r') as f:
       import json
       data = json.load(f)
    
    assert data == [{"product_id": 123, "name": "test_product"}]
    

def test_collect_and_save_products_invalid_source(campaign_manager_instance, base_campaign_dir):
    """Checks error handling for an invalid data source."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    campaign_manager_instance.base_dir = base_campaign_dir
    campaign_manager_instance.create_campaign_directories()
    
    with pytest.raises(ValueError, match="Invalid source for product data collection"):
        campaign_manager_instance.collect_and_save_products(source="invalid_source", query="test")


def test_collect_and_save_products_no_product_dir(campaign_manager_instance, base_campaign_dir):
    """Checks saving config fails when no product dir exists."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    campaign_manager_instance.base_dir = base_campaign_dir

    with pytest.raises(FileNotFoundError, match="No such file or directory"):
        campaign_manager_instance.collect_and_save_products(source="ali", query="test")

def test_collect_and_save_products_no_base_dir(campaign_manager_instance):
    """Check that error is raised when base_dir is not set."""
    campaign_manager_instance.init_campaign_parameters(name="test_campaign", language="en", currency="USD")
    with pytest.raises(ValueError, match="Base directory is not set"):
         campaign_manager_instance.collect_and_save_products(source="ali", query="test")

# Tests for Ad Material Generation, Campaign Verification and Publishing (Mocked)
@patch('hypotez.src.suppliers.aliexpress.campaign.campaign_manager.CampaignManager.generate_ad_materials')
def test_generate_ad_materials_calls_subfunction(mock_generate, campaign_manager_instance):
    """Checks ad material generation calls the subfunction."""
    campaign_manager_instance.generate_ad_materials()
    mock_generate.assert_called_once()


@patch('hypotez.src.suppliers.aliexpress.campaign.campaign_manager.CampaignManager.verify_campaign')
def test_verify_campaign_calls_subfunction(mock_verify, campaign_manager_instance):
    """Checks campaign verification calls the subfunction."""
    campaign_manager_instance.verify_campaign()
    mock_verify.assert_called_once()


@patch('hypotez.src.suppliers.aliexpress.campaign.campaign_manager.CampaignManager.publish_campaign')
def test_publish_campaign_calls_subfunction(mock_publish, campaign_manager_instance):
    """Checks campaign publishing calls the subfunction."""
    campaign_manager_instance.publish_campaign()
    mock_publish.assert_called_once()
```