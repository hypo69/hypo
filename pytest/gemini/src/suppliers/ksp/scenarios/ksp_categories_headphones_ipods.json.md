```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_data():
    """Provides the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "in-ear-bud": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/242..245..1250",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "ipods in-ear-bud" }
          }
        },
        "Overear": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/242..245..1252",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "ipods Overear" }
          }
        },
        "Ear-clip": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/242..245..1254",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "3455": "Ear-clip",
            "template": { "apple": "ipods Ear-clip" }
          }
        }
      }
    }
    """
    return json.loads(json_data)

# Test cases for the 'scenarios' data structure
def test_scenarios_exists(ksp_categories_data):
    """Check if 'scenarios' key exists in the JSON data."""
    assert "scenarios" in ksp_categories_data, "The 'scenarios' key should exist."

def test_scenarios_is_dict(ksp_categories_data):
    """Check if 'scenarios' is a dictionary."""
    assert isinstance(ksp_categories_data["scenarios"], dict), "The 'scenarios' should be a dictionary."

def test_scenarios_not_empty(ksp_categories_data):
    """Check if 'scenarios' is not empty."""
    assert ksp_categories_data["scenarios"], "The 'scenarios' dictionary should not be empty."

# Test cases for individual scenarios within 'scenarios'
def test_in_ear_bud_exists(ksp_categories_data):
    """Check if the 'in-ear-bud' scenario exists."""
    assert "in-ear-bud" in ksp_categories_data["scenarios"], "The 'in-ear-bud' scenario should exist."

def test_in_ear_bud_has_brand(ksp_categories_data):
    """Check if 'in-ear-bud' has the 'brand' key."""
    assert "brand" in ksp_categories_data["scenarios"]["in-ear-bud"], "The 'in-ear-bud' should have a 'brand'."

def test_in_ear_bud_brand_value(ksp_categories_data):
    """Check if the 'brand' value of 'in-ear-bud' is 'APPLE'."""
    assert ksp_categories_data["scenarios"]["in-ear-bud"]["brand"] == "APPLE", "The brand for 'in-ear-bud' should be 'APPLE'."

def test_in_ear_bud_has_url(ksp_categories_data):
    """Check if 'in-ear-bud' has the 'url' key."""
    assert "url" in ksp_categories_data["scenarios"]["in-ear-bud"], "The 'in-ear-bud' should have a 'url'."

def test_in_ear_bud_url_value(ksp_categories_data):
     """Check if the 'url' value is a string and not empty."""
     assert isinstance(ksp_categories_data["scenarios"]["in-ear-bud"]["url"], str) and ksp_categories_data["scenarios"]["in-ear-bud"]["url"] , "The 'url' value for 'in-ear-bud' should be non-empty string."

def test_in_ear_bud_has_checkbox(ksp_categories_data):
    """Check if 'in-ear-bud' has the 'checkbox' key."""
    assert "checkbox" in ksp_categories_data["scenarios"]["in-ear-bud"], "The 'in-ear-bud' should have a 'checkbox'."

def test_in_ear_bud_checkbox_is_bool(ksp_categories_data):
    """Check if 'checkbox' of 'in-ear-bud' is a boolean."""
    assert isinstance(ksp_categories_data["scenarios"]["in-ear-bud"]["checkbox"], bool), "The 'checkbox' for 'in-ear-bud' should be a boolean."


def test_in_ear_bud_has_active(ksp_categories_data):
     """Check if 'in-ear-bud' has the 'active' key."""
     assert "active" in ksp_categories_data["scenarios"]["in-ear-bud"], "The 'in-ear-bud' should have an 'active' key."

def test_in_ear_bud_active_is_bool(ksp_categories_data):
     """Check if 'active' of 'in-ear-bud' is a boolean."""
     assert isinstance(ksp_categories_data["scenarios"]["in-ear-bud"]["active"], bool), "The 'active' for 'in-ear-bud' should be a boolean."
     
def test_in_ear_bud_has_condition(ksp_categories_data):
    """Check if 'in-ear-bud' has the 'condition' key."""
    assert "condition" in ksp_categories_data["scenarios"]["in-ear-bud"], "The 'in-ear-bud' should have a 'condition'."

def test_in_ear_bud_condition_value(ksp_categories_data):
    """Check if the 'condition' value of 'in-ear-bud' is 'new'."""
    assert ksp_categories_data["scenarios"]["in-ear-bud"]["condition"] == "new", "The condition for 'in-ear-bud' should be 'new'."

def test_in_ear_bud_has_presta_categories(ksp_categories_data):
    """Check if 'in-ear-bud' has the 'presta_categories' key."""
    assert "presta_categories" in ksp_categories_data["scenarios"]["in-ear-bud"], "The 'in-ear-bud' should have 'presta_categories'."

def test_in_ear_bud_presta_categories_is_dict(ksp_categories_data):
    """Check if 'presta_categories' of 'in-ear-bud' is a dictionary."""
    assert isinstance(ksp_categories_data["scenarios"]["in-ear-bud"]["presta_categories"], dict), "The 'presta_categories' should be a dictionary."

def test_in_ear_bud_presta_categories_has_template(ksp_categories_data):
      """Check if 'presta_categories' of 'in-ear-bud' has the 'template' key."""
      assert "template" in ksp_categories_data["scenarios"]["in-ear-bud"]["presta_categories"], "The 'presta_categories' for 'in-ear-bud' should have a 'template'."

def test_in_ear_bud_presta_categories_template_is_dict(ksp_categories_data):
      """Check if 'template' of 'presta_categories' of 'in-ear-bud' is a dictionary."""
      assert isinstance(ksp_categories_data["scenarios"]["in-ear-bud"]["presta_categories"]["template"], dict), "The 'template' in 'presta_categories' should be a dictionary."

def test_in_ear_bud_presta_categories_template_has_apple(ksp_categories_data):
      """Check if 'template' of 'presta_categories' of 'in-ear-bud' has the 'apple' key."""
      assert "apple" in ksp_categories_data["scenarios"]["in-ear-bud"]["presta_categories"]["template"], "The 'template' in 'presta_categories' for 'in-ear-bud' should have a 'apple'."


def test_overear_exists(ksp_categories_data):
    """Check if the 'Overear' scenario exists."""
    assert "Overear" in ksp_categories_data["scenarios"], "The 'Overear' scenario should exist."

def test_overear_has_brand(ksp_categories_data):
     """Check if 'Overear' has the 'brand' key."""
     assert "brand" in ksp_categories_data["scenarios"]["Overear"], "The 'Overear' should have a 'brand'."

def test_overear_brand_value(ksp_categories_data):
     """Check if the 'brand' value of 'Overear' is 'APPLE'."""
     assert ksp_categories_data["scenarios"]["Overear"]["brand"] == "APPLE", "The brand for 'Overear' should be 'APPLE'."

def test_overear_has_url(ksp_categories_data):
     """Check if 'Overear' has the 'url' key."""
     assert "url" in ksp_categories_data["scenarios"]["Overear"], "The 'Overear' should have a 'url'."

def test_overear_url_value(ksp_categories_data):
      """Check if the 'url' value is a string and not empty."""
      assert isinstance(ksp_categories_data["scenarios"]["Overear"]["url"], str) and ksp_categories_data["scenarios"]["Overear"]["url"] , "The 'url' value for 'Overear' should be non-empty string."

def test_overear_has_checkbox(ksp_categories_data):
    """Check if 'Overear' has the 'checkbox' key."""
    assert "checkbox" in ksp_categories_data["scenarios"]["Overear"], "The 'Overear' should have a 'checkbox'."

def test_overear_checkbox_is_bool(ksp_categories_data):
    """Check if 'checkbox' of 'Overear' is a boolean."""
    assert isinstance(ksp_categories_data["scenarios"]["Overear"]["checkbox"], bool), "The 'checkbox' for 'Overear' should be a boolean."

def test_overear_has_active(ksp_categories_data):
     """Check if 'Overear' has the 'active' key."""
     assert "active" in ksp_categories_data["scenarios"]["Overear"], "The 'Overear' should have an 'active' key."
     
def test_overear_active_is_bool(ksp_categories_data):
     """Check if 'active' of 'Overear' is a boolean."""
     assert isinstance(ksp_categories_data["scenarios"]["Overear"]["active"], bool), "The 'active' for 'Overear' should be a boolean."
     
def test_overear_has_condition(ksp_categories_data):
    """Check if 'Overear' has the 'condition' key."""
    assert "condition" in ksp_categories_data["scenarios"]["Overear"], "The 'Overear' should have a 'condition'."

def test_overear_condition_value(ksp_categories_data):
    """Check if the 'condition' value of 'Overear' is 'new'."""
    assert ksp_categories_data["scenarios"]["Overear"]["condition"] == "new", "The condition for 'Overear' should be 'new'."

def test_overear_has_presta_categories(ksp_categories_data):
    """Check if 'Overear' has the 'presta_categories' key."""
    assert "presta_categories" in ksp_categories_data["scenarios"]["Overear"], "The 'Overear' should have 'presta_categories'."

def test_overear_presta_categories_is_dict(ksp_categories_data):
    """Check if 'presta_categories' of 'Overear' is a dictionary."""
    assert isinstance(ksp_categories_data["scenarios"]["Overear"]["presta_categories"], dict), "The 'presta_categories' should be a dictionary."
    
def test_overear_presta_categories_has_template(ksp_categories_data):
     """Check if 'presta_categories' of 'Overear' has the 'template' key."""
     assert "template" in ksp_categories_data["scenarios"]["Overear"]["presta_categories"], "The 'presta_categories' for 'Overear' should have a 'template'."

def test_overear_presta_categories_template_is_dict(ksp_categories_data):
     """Check if 'template' of 'presta_categories' of 'Overear' is a dictionary."""
     assert isinstance(ksp_categories_data["scenarios"]["Overear"]["presta_categories"]["template"], dict), "The 'template' in 'presta_categories' should be a dictionary."

def test_overear_presta_categories_template_has_apple(ksp_categories_data):
     """Check if 'template' of 'presta_categories' of 'Overear' has the 'apple' key."""
     assert "apple" in ksp_categories_data["scenarios"]["Overear"]["presta_categories"]["template"], "The 'template' in 'presta_categories' for 'Overear' should have a 'apple'."


def test_ear_clip_exists(ksp_categories_data):
    """Check if the 'Ear-clip' scenario exists."""
    assert "Ear-clip" in ksp_categories_data["scenarios"], "The 'Ear-clip' scenario should exist."

def test_ear_clip_has_brand(ksp_categories_data):
     """Check if 'Ear-clip' has the 'brand' key."""
     assert "brand" in ksp_categories_data["scenarios"]["Ear-clip"], "The 'Ear-clip' should have a 'brand'."

def test_ear_clip_brand_value(ksp_categories_data):
     """Check if the 'brand' value of 'Ear-clip' is 'APPLE'."""
     assert ksp_categories_data["scenarios"]["Ear-clip"]["brand"] == "APPLE", "The brand for 'Ear-clip' should be 'APPLE'."

def test_ear_clip_has_url(ksp_categories_data):
     """Check if 'Ear-clip' has the 'url' key."""
     assert "url" in ksp_categories_data["scenarios"]["Ear-clip"], "The 'Ear-clip' should have a 'url'."

def test_ear_clip_url_value(ksp_categories_data):
      """Check if the 'url' value is a string and not empty."""
      assert isinstance(ksp_categories_data["scenarios"]["Ear-clip"]["url"], str) and ksp_categories_data["scenarios"]["Ear-clip"]["url"], "The 'url' value for 'Ear-clip' should be non-empty string."

def test_ear_clip_has_checkbox(ksp_categories_data):
    """Check if 'Ear-clip' has the 'checkbox' key."""
    assert "checkbox" in ksp_categories_data["scenarios"]["Ear-clip"], "The 'Ear-clip' should have a 'checkbox'."
    
def test_ear_clip_checkbox_is_bool(ksp_categories_data):
     """Check if 'checkbox' of 'Ear-clip' is a boolean."""
     assert isinstance(ksp_categories_data["scenarios"]["Ear-clip"]["checkbox"], bool), "The 'checkbox' for 'Ear-clip' should be a boolean."
     
def test_ear_clip_has_active(ksp_categories_data):
     """Check if 'Ear-clip' has the 'active' key."""
     assert "active" in ksp_categories_data["scenarios"]["Ear-clip"], "The 'Ear-clip' should have an 'active' key."
     
def test_ear_clip_active_is_bool(ksp_categories_data):
     """Check if 'active' of 'Ear-clip' is a boolean."""
     assert isinstance(ksp_categories_data["scenarios"]["Ear-clip"]["active"], bool), "The 'active' for 'Ear-clip' should be a boolean."
     
def test_ear_clip_has_condition(ksp_categories_data):
    """Check if 'Ear-clip' has the 'condition' key."""
    assert "condition" in ksp_categories_data["scenarios"]["Ear-clip"], "The 'Ear-clip' should have a 'condition'."

def test_ear_clip_condition_value(ksp_categories_data):
    """Check if the 'condition' value of 'Ear-clip' is 'new'."""
    assert ksp_categories_data["scenarios"]["Ear-clip"]["condition"] == "new", "The condition for 'Ear-clip' should be 'new'."


def test_ear_clip_has_presta_categories(ksp_categories_data):
    """Check if 'Ear-clip' has the 'presta_categories' key."""
    assert "presta_categories" in ksp_categories_data["scenarios"]["Ear-clip"], "The 'Ear-clip' should have 'presta_categories'."

def test_ear_clip_presta_categories_is_dict(ksp_categories_data):
    """Check if 'presta_categories' of 'Ear-clip' is a dictionary."""
    assert isinstance(ksp_categories_data["scenarios"]["Ear-clip"]["presta_categories"], dict), "The 'presta_categories' should be a dictionary."
    
def test_ear_clip_presta_categories_has_3455_key(ksp_categories_data):
    """Check if 'presta_categories' of 'Ear-clip' has the '3455' key."""
    assert "3455" in ksp_categories_data["scenarios"]["Ear-clip"]["presta_categories"], "The 'presta_categories' for 'Ear-clip' should have a '3455' key."

def test_ear_clip_presta_categories_3455_value(ksp_categories_data):
    """Check if value of '3455' key is 'Ear-clip'"""
    assert ksp_categories_data["scenarios"]["Ear-clip"]["presta_categories"]["3455"] == "Ear-clip" , "The value of '3455' key should be 'Ear-clip'."

def test_ear_clip_presta_categories_has_template(ksp_categories_data):
    """Check if 'presta_categories' of 'Ear-clip' has the 'template' key."""
    assert "template" in ksp_categories_data["scenarios"]["Ear-clip"]["presta_categories"], "The 'presta_categories' for 'Ear-clip' should have a 'template'."

def test_ear_clip_presta_categories_template_is_dict(ksp_categories_data):
     """Check if 'template' of 'presta_categories' of 'Ear-clip' is a dictionary."""
     assert isinstance(ksp_categories_data["scenarios"]["Ear-clip"]["presta_categories"]["template"], dict), "The 'template' in 'presta_categories' should be a dictionary."
     
def test_ear_clip_presta_categories_template_has_apple(ksp_categories_data):
     """Check if 'template' of 'presta_categories' of 'Ear-clip' has the 'apple' key."""
     assert "apple" in ksp_categories_data["scenarios"]["Ear-clip"]["presta_categories"]["template"], "The 'template' in 'presta_categories' for 'Ear-clip' should have a 'apple'."
```