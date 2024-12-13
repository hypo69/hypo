```python
import pytest
import json

# Fixture definitions
@pytest.fixture
def valid_cdata_json():
    """Provides a valid cdata JSON object for testing."""
    return {
        "supplier": "cdata",
        "supplier_prefix": "CDT-",
        "if_list":"first",
        "use_mouse": False,
        "mandatory": True,
        "start_url": "https://www.c-data.co.il/",
        "price_rule": "3.5*1.17",
        "num_items_4_flush": 300,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "scenario_files": [
            ["cdata_categories_aio_asus.json", "cdata_categories_aio_dell.json", "cdata_categories_aio_hp.json"],
            ["cdata_categories_desktops.json", "cdata_categories_gaming_desktops.json", "cdata_categories_workstatios.json"],
            [
                "cdata_categories_laptops_asus.json",
                "cdata_categories_laptops_dell.json",
                "cdata_categories_laptops_hp.json",
                "cdata_categories_gaming_laptops_asus.json",
                "cdata_categories_gaming_laptops_dell.json",
                "cdata_categories_gaming_laptops_hp.json",
            ],
            [
                "cdata_categories_monitors_apple.json",
                "cdata_categories_monitors_dell.json",
                "cdata_categories_monitors_hp.json",
            ],
            ["cdata_categories_keyboards.json"],
            ["cdata_categories_printers.json"],
            ["cdata_categories_webcams.json"],
            ["cdata_categories_video.json"],
            ["cdata_categories_ups.json"],
        ],
        "last_runned_scenario": "",
    }


@pytest.fixture
def invalid_cdata_json_missing_field():
    """Provides an invalid cdata JSON object missing the 'supplier' field."""
    return {
        "supplier_prefix": "CDT-",
        "if_list":"first",
        "use_mouse": False,
        "mandatory": True,
        "start_url": "https://www.c-data.co.il/",
        "price_rule": "3.5*1.17",
        "num_items_4_flush": 300,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "scenario_files": [
            ["cdata_categories_aio_asus.json", "cdata_categories_aio_dell.json", "cdata_categories_aio_hp.json"],
            ["cdata_categories_desktops.json", "cdata_categories_gaming_desktops.json", "cdata_categories_workstatios.json"],
            [
                "cdata_categories_laptops_asus.json",
                "cdata_categories_laptops_dell.json",
                "cdata_categories_laptops_hp.json",
                "cdata_categories_gaming_laptops_asus.json",
                "cdata_categories_gaming_laptops_dell.json",
                "cdata_categories_gaming_laptops_hp.json",
            ],
            [
                "cdata_categories_monitors_apple.json",
                "cdata_categories_monitors_dell.json",
                "cdata_categories_monitors_hp.json",
            ],
            ["cdata_categories_keyboards.json"],
            ["cdata_categories_printers.json"],
            ["cdata_categories_webcams.json"],
            ["cdata_categories_video.json"],
            ["cdata_categories_ups.json"],
        ],
        "last_runned_scenario": "",
    }


@pytest.fixture
def invalid_cdata_json_wrong_type():
    """Provides an invalid cdata JSON object with a wrong type for 'price_rule'."""
    return {
        "supplier": "cdata",
        "supplier_prefix": "CDT-",
        "if_list":"first",
        "use_mouse": False,
        "mandatory": True,
        "start_url": "https://www.c-data.co.il/",
        "price_rule": 3.5 * 1.17,  # Should be a string
        "num_items_4_flush": 300,
        "parcing method [webdriver|api]": "web",
         "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "scenario_files": [
            ["cdata_categories_aio_asus.json", "cdata_categories_aio_dell.json", "cdata_categories_aio_hp.json"],
            ["cdata_categories_desktops.json", "cdata_categories_gaming_desktops.json", "cdata_categories_workstatios.json"],
            [
                "cdata_categories_laptops_asus.json",
                "cdata_categories_laptops_dell.json",
                "cdata_categories_laptops_hp.json",
                "cdata_categories_gaming_laptops_asus.json",
                "cdata_categories_gaming_laptops_dell.json",
                "cdata_categories_gaming_laptops_hp.json",
            ],
            [
                "cdata_categories_monitors_apple.json",
                "cdata_categories_monitors_dell.json",
                "cdata_categories_monitors_hp.json",
            ],
            ["cdata_categories_keyboards.json"],
            ["cdata_categories_printers.json"],
            ["cdata_categories_webcams.json"],
            ["cdata_categories_video.json"],
            ["cdata_categories_ups.json"],
        ],
        "last_runned_scenario": "",
    }

def test_valid_cdata_json_structure(valid_cdata_json):
    """
    Test that the structure of valid_cdata_json is correct.
    """
    assert isinstance(valid_cdata_json, dict)
    assert "supplier" in valid_cdata_json
    assert "supplier_prefix" in valid_cdata_json
    assert "if_list" in valid_cdata_json
    assert "use_mouse" in valid_cdata_json
    assert "mandatory" in valid_cdata_json
    assert "start_url" in valid_cdata_json
    assert "price_rule" in valid_cdata_json
    assert "num_items_4_flush" in valid_cdata_json
    assert "parcing method [webdriver|api]" in valid_cdata_json
    assert "about method web scrapping [webdriver|api]" in valid_cdata_json
    assert "scenario_files" in valid_cdata_json
    assert "last_runned_scenario" in valid_cdata_json


def test_invalid_cdata_json_missing_field_raises_keyerror(invalid_cdata_json_missing_field):
    """
    Test that missing field `supplier` will raise KeyError during access.
    """
    with pytest.raises(KeyError):
        _ = invalid_cdata_json_missing_field["supplier"]


def test_invalid_cdata_json_wrong_type_raises_typeerror(invalid_cdata_json_wrong_type):
    """
    Test that invalid type of `price_rule` raises TypeError during type checks.
    """
    assert isinstance(invalid_cdata_json_wrong_type['price_rule'],(int,float))
    with pytest.raises(TypeError):
      if not isinstance(invalid_cdata_json_wrong_type['price_rule'],str):
        raise TypeError

def test_cdata_json_scenario_files_structure(valid_cdata_json):
    """
    Test that 'scenario_files' is a list of lists of strings
    """
    assert isinstance(valid_cdata_json["scenario_files"], list)
    for scenario_list in valid_cdata_json["scenario_files"]:
        assert isinstance(scenario_list, list)
        for file_name in scenario_list:
            assert isinstance(file_name, str)


def test_cdata_json_url_valid(valid_cdata_json):
    """
    Test that the start_url is a valid URL
    """
    assert valid_cdata_json['start_url'].startswith("https://")

def test_cdata_json_supplier_prefix_valid(valid_cdata_json):
    """
    Test that the supplier_prefix is a string and not empty
    """
    assert isinstance(valid_cdata_json['supplier_prefix'],str)
    assert len(valid_cdata_json['supplier_prefix']) > 0

def test_cdata_json_price_rule_valid(valid_cdata_json):
    """
    Test that the price_rule is a string and not empty
    """
    assert isinstance(valid_cdata_json['price_rule'],str)
    assert len(valid_cdata_json['price_rule']) > 0

def test_cdata_json_num_items_4_flush_valid(valid_cdata_json):
    """
    Test that the num_items_4_flush is an int and greater than zero
    """
    assert isinstance(valid_cdata_json['num_items_4_flush'],int)
    assert valid_cdata_json['num_items_4_flush'] > 0
```