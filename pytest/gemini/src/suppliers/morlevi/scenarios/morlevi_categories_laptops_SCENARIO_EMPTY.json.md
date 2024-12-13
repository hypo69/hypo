```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def laptop_data():
    """Provides the laptop data from the JSON file."""
    json_data = """
{
  "<BRAND> 11.6 I3": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I3", "11" ]
      }
    }
  },
  "<BRAND> 11.6 I5": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I5", "11" ]
      }
    }
  },
  "<BRAND> 11.6 I7": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I7", "11" ]
      }
    }
  },
  "<BRAND> 11.6 I9": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I9", "11" ]
      }
    }
  },
  "<BRAND> 11.6 AMD": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS AMD", "11" ]
      }
    }
  },
  "<BRAND> 11.6 Celeron": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "11" ]
      }
    }
  },
  "<BRAND> 11.6 Pentium": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "11" ]
      }
    }
  },
  "<BRAND> 13.4 - 13.3 I3": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I3", "13" ]
      }
    }
  },
  "<BRAND> 13.4 - 13.3 I5": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I5", "13" ]
      }
    }
  },
  "<BRAND> 13.4 - 13.3 I7": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I7", "13" ]
      }
    }
  },
  "<BRAND> 13.4 - 13.3 I9": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I9", "13" ]
      }
    }
  },
  "<BRAND> 13.4 - 13.3 AMD": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS AMD", "13" ]
      }
    }
  },
  "<BRAND> 13.4 - 13.3 Celeron": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "13" ]
      }
    }
  },
  "<BRAND> 13.4 - 13.3 Pentium": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "13" ]
      }
    }
  },
  "<BRAND> 14 I3": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I3", "14" ]
      }
    }
  },
  "<BRAND> 14 I5": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I5", "14" ]
      }
    }
  },
  "<BRAND> 14 I7": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I7", "14" ]
      }
    }
  },
  "<BRAND> 14 I9": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I9", "14" ]
      }
    }
  },
  "<BRAND> 14 AMD RYZEN 7": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I7", "14" ]
      }
    }
  },
  "<BRAND> 14 Celeron": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "14" ]
      }
    }
  },
  "<BRAND> 14 Pentium": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "14" ]
      }
    }
  },
  "<BRAND> 15 I3": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I3", "15" ]
      }
    }
  },
  "<BRAND> 15 I5": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I5", "15" ]
      }
    }
  },
  "<BRAND> 15 I7": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I7", "15" ]
      }
    }
  },
  "<BRAND> 15 I9": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I9", "15" ]
      }
    }
  },
  "<BRAND> 15 AMD RYZEN 5": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "gigabyte": [ "LAPTOPS AMD RYZEN 5", "15" ]
      }
    }
  },
  "<BRAND> 15 AMD RYZEN 7": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS AMD RYZEN 7", "15" ]
      }
    }
  },
  "<BRAND> 15 Celeron": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "15" ]
      }
    }
  },
  "<BRAND> 15 Pentium": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "15" ]
      }
    }
  },
  "<BRAND> 17.3 I3": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I3", "17" ]
      }
    }
  },
  "<BRAND> 17.3 I5": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I5", "17" ]
      }
    }
  },
  "<BRAND> 17.3 I7": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I7", "17" ]
      }
    }
  },
  "<BRAND> 17.3 I9": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL I9", "17" ]
      }
    }
  },
  "<BRAND> 17.3 AMD": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS AMD", "17" ]
      }
    }
  },
  "<BRAND> 17.3 Celeron": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "17" ]
      }
    }
  },
  "<BRAND> 17.3 Pentium": {
    "brand": "<BRAND>",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
      "template": {
        "<BRAND>": [ "LAPTOPS INTEL CELERON", "17" ]
      }
    }
  }
}
    """
    return json.loads(json_data)

def test_laptop_data_is_not_empty(laptop_data):
    """Checks if the loaded laptop data is not empty."""
    assert laptop_data, "Laptop data should not be empty."

def test_laptop_has_expected_keys(laptop_data):
    """Checks if each laptop entry has the expected keys."""
    expected_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for laptop_model, data in laptop_data.items():
        assert all(key in data for key in expected_keys), f"Laptop model '{laptop_model}' does not contain all expected keys."
        assert isinstance(data["presta_categories"], dict), f"presta_categories for {laptop_model} is not a dict"
        assert "template" in data["presta_categories"] , f"template not in presta_categories for {laptop_model}"
        assert isinstance(data["presta_categories"]["template"], dict), f"template for {laptop_model} is not a dict"

def test_laptop_presta_categories_template_has_brand_key(laptop_data):
  """Checks if the presta_categories template has a brand key"""
  for laptop_model, data in laptop_data.items():
      template = data["presta_categories"]["template"]
      assert len(template.keys()) == 1 , f"template should have one key for {laptop_model}"
      
      for key in template.keys():
        assert isinstance(key, str), f"template key should be string for {laptop_model}"


def test_laptop_presta_categories_template_has_expected_values(laptop_data):
    """Checks if presta_categories template values are lists of strings with len=2."""
    for laptop_model, data in laptop_data.items():
        template = data["presta_categories"]["template"]
        for key, value in template.items():
            assert isinstance(value, list), f"Template value for {laptop_model} under key '{key}' is not a list."
            assert len(value) == 2, f"Template list for {laptop_model} under key '{key}' does not have 2 elements."
            assert all(isinstance(item, str) for item in value), f"Template list for {laptop_model} under key '{key}' contains non-string elements."

def test_laptop_data_brand_is_string(laptop_data):
    """Checks if brand for every laptop is a string."""
    for laptop_model, data in laptop_data.items():
        assert isinstance(data["brand"], str), f"Brand for {laptop_model} is not a string."

def test_laptop_data_url_is_nullable(laptop_data):
    """Checks if url for every laptop is null or string."""
    for laptop_model, data in laptop_data.items():
        assert data["url"] is None , f"url for {laptop_model} is not null"
        
def test_laptop_data_checkbox_is_boolean(laptop_data):
    """Checks if checkbox for every laptop is boolean."""
    for laptop_model, data in laptop_data.items():
      assert isinstance(data["checkbox"], bool), f"checkbox for {laptop_model} is not boolean"

def test_laptop_data_active_is_boolean(laptop_data):
    """Checks if active for every laptop is boolean."""
    for laptop_model, data in laptop_data.items():
      assert isinstance(data["active"], bool), f"active for {laptop_model} is not boolean"

def test_laptop_data_condition_is_string(laptop_data):
    """Checks if condition for every laptop is string."""
    for laptop_model, data in laptop_data.items():
        assert isinstance(data["condition"], str), f"condition for {laptop_model} is not a string."

def test_laptop_data_condition_is_new(laptop_data):
    """Checks if condition for every laptop is 'new'."""
    for laptop_model, data in laptop_data.items():
        assert data["condition"] == "new", f"condition for {laptop_model} is not 'new'"
```