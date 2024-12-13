```python
import pytest
import json

# Since the input code is a JSON structure, we'll define a fixture to load it.
@pytest.fixture
def cdata_categories_ups_data():
    """Provides the JSON data as a dictionary."""
    json_data = """
    {
      "scenarios": {
        "ups": {
          "brand": "APC",
          "url": "https://reseller.c-data.co.il/UPS-%D7%90%D7%9C-%D7%A4%D7%A1%D7%A7",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "158,247"
        }
      }
    }
    """
    return json.loads(json_data)

def test_cdata_categories_ups_data_structure(cdata_categories_ups_data):
    """
    Checks that the loaded data has the expected dictionary structure.
    """
    assert isinstance(cdata_categories_ups_data, dict)
    assert "scenarios" in cdata_categories_ups_data
    assert isinstance(cdata_categories_ups_data["scenarios"], dict)
    assert "ups" in cdata_categories_ups_data["scenarios"]
    assert isinstance(cdata_categories_ups_data["scenarios"]["ups"], dict)

def test_cdata_categories_ups_brand(cdata_categories_ups_data):
    """
    Checks if the 'brand' field has the correct value.
    """
    assert cdata_categories_ups_data["scenarios"]["ups"]["brand"] == "APC"

def test_cdata_categories_ups_url(cdata_categories_ups_data):
    """
    Checks if the 'url' field has the correct value.
    """
    assert cdata_categories_ups_data["scenarios"]["ups"]["url"] == "https://reseller.c-data.co.il/UPS-%D7%90%D7%9C-%D7%A4%D7%A1%D7%A7"

def test_cdata_categories_ups_checkbox(cdata_categories_ups_data):
    """
    Checks if the 'checkbox' field has the correct boolean value (False).
    """
    assert cdata_categories_ups_data["scenarios"]["ups"]["checkbox"] is False

def test_cdata_categories_ups_active(cdata_categories_ups_data):
    """
    Checks if the 'active' field has the correct boolean value (True).
    """
    assert cdata_categories_ups_data["scenarios"]["ups"]["active"] is True

def test_cdata_categories_ups_condition(cdata_categories_ups_data):
    """
    Checks if the 'condition' field has the correct string value.
    """
    assert cdata_categories_ups_data["scenarios"]["ups"]["condition"] == "new"

def test_cdata_categories_ups_presta_categories(cdata_categories_ups_data):
    """
    Checks if the 'presta_categories' field has the correct value
    """
    assert cdata_categories_ups_data["scenarios"]["ups"]["presta_categories"] == "158,247"

def test_cdata_categories_ups_missing_key():
  """
  Checks behavior when a key is missing from the structure
  """
  json_data = """
    {
      "scenarios": {
        "ups": {
          "brand": "APC",
          "url": "https://reseller.c-data.co.il/UPS-%D7%90%D7%9C-%D7%A4%D7%A1%D7%A7",
          "checkbox": false,
          "active": true,
          "condition":"new"
          
        }
      }
    }
    """
  data = json.loads(json_data)
  with pytest.raises(KeyError):
    _ = data["scenarios"]["ups"]["presta_categories"]
```