```python
import pytest
import json

# Fixture for the input data
@pytest.fixture
def category_data():
    """Provides the category data from the json."""
    return {
        "MSI": {
            "brand": "MSI",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=69",
            "checkbox": False,
            "active": True,
            "condition":"new",
            "presta_categories": "108,109"
        },
        "GIGABYTE": {
            "brand": "GIGABYTE",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=25",
            "checkbox": False,
            "active": True,
             "condition":"new",
            "presta_categories": "108,109"
        },
        "PNY": {
            "brand": "PNY",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=27",
            "checkbox": False,
            "active": True,
             "condition":"new",
            "presta_categories": "108,111"
        }
    }
    
def test_category_data_structure(category_data):
    """Checks if the data is a dictionary."""
    assert isinstance(category_data, dict)

def test_category_brand_names(category_data):
    """Checks if the brands are correctly stored as keys in dictionary"""
    expected_brands = ["MSI", "GIGABYTE", "PNY"]
    assert  list(category_data.keys()) == expected_brands

def test_category_msi_data(category_data):
    """Checks the data for the MSI brand."""
    msi_data = category_data["MSI"]
    assert msi_data["brand"] == "MSI"
    assert msi_data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=69"
    assert msi_data["checkbox"] == False
    assert msi_data["active"] == True
    assert msi_data["condition"] == "new"
    assert msi_data["presta_categories"] == "108,109"


def test_category_gigabyte_data(category_data):
    """Checks the data for the GIGABYTE brand."""
    gigabyte_data = category_data["GIGABYTE"]
    assert gigabyte_data["brand"] == "GIGABYTE"
    assert gigabyte_data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=25"
    assert gigabyte_data["checkbox"] == False
    assert gigabyte_data["active"] == True
    assert gigabyte_data["condition"] == "new"
    assert gigabyte_data["presta_categories"] == "108,109"

def test_category_pny_data(category_data):
    """Checks the data for the PNY brand."""
    pny_data = category_data["PNY"]
    assert pny_data["brand"] == "PNY"
    assert pny_data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=27"
    assert pny_data["checkbox"] == False
    assert pny_data["active"] == True
    assert pny_data["condition"] == "new"
    assert pny_data["presta_categories"] == "108,111"

def test_category_active_field_type(category_data):
    """Checks if the 'active' field is a boolean."""
    for brand_data in category_data.values():
        assert isinstance(brand_data["active"], bool)

def test_category_checkbox_field_type(category_data):
    """Checks if the 'checkbox' field is a boolean."""
    for brand_data in category_data.values():
       assert isinstance(brand_data["checkbox"], bool)

def test_category_url_field_type(category_data):
    """Checks if the 'url' field is a string."""
    for brand_data in category_data.values():
       assert isinstance(brand_data["url"], str)

def test_category_brand_field_type(category_data):
     """Checks if the 'brand' field is a string."""
     for brand_data in category_data.values():
          assert isinstance(brand_data["brand"], str)
def test_category_condition_field_type(category_data):
    """Checks if the 'condition' field is a string."""
    for brand_data in category_data.values():
        assert isinstance(brand_data["condition"], str)
def test_category_presta_categories_field_type(category_data):
    """Checks if the 'presta_categories' field is a string."""
    for brand_data in category_data.values():
        assert isinstance(brand_data["presta_categories"], str)

def test_category_empty_data():
    """Checks handling of empty input data."""
    with pytest.raises(KeyError):
      empty_data = {}
      empty_data["test"]
def test_category_wrong_url():
      """Test for url with wrong pattern"""
      data_with_wrong_url = {
        "MSI": {
            "brand": "MSI",
            "url": "wrongurl",
            "checkbox": False,
            "active": True,
            "condition":"new",
            "presta_categories": "108,109"
          }
      }
      assert data_with_wrong_url["MSI"]["url"] == "wrongurl"
def test_category_wrong_checkbox():
    """Test for checkbox with wrong pattern"""
    data_with_wrong_checkbox = {
        "MSI": {
            "brand": "MSI",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=69",
            "checkbox": "false",
            "active": True,
            "condition":"new",
            "presta_categories": "108,109"
          }
        }
    assert data_with_wrong_checkbox["MSI"]["checkbox"] == "false"

def test_category_wrong_active():
        """Test for active with wrong pattern"""
        data_with_wrong_active = {
        "MSI": {
            "brand": "MSI",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=69",
            "checkbox": False,
            "active": "true",
             "condition":"new",
            "presta_categories": "108,109"
          }
        }
        assert data_with_wrong_active["MSI"]["active"] == "true"
def test_category_wrong_condition():
          """Test for condition with wrong pattern"""
          data_with_wrong_condition = {
        "MSI": {
            "brand": "MSI",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=69",
            "checkbox": False,
            "active": True,
             "condition":123,
            "presta_categories": "108,109"
          }
      }
          assert data_with_wrong_condition["MSI"]["condition"] == 123
def test_category_wrong_presta_categories():
            """Test for presta_categories with wrong pattern"""
            data_with_wrong_presta_categories = {
        "MSI": {
            "brand": "MSI",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=571&manId=69",
            "checkbox": False,
            "active": True,
            "condition": "new",
            "presta_categories": 108
          }
      }
            assert data_with_wrong_presta_categories["MSI"]["presta_categories"] == 108
```