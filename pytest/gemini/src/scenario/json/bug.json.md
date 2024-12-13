```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def bug_json_data():
    """Provides the bug.json data as a dictionary."""
    json_str = """
    {
        "supplier": "bug",
        "supplier_prefix": "BUG-",
        "start_url": "https://www.bug.co.il/",
        "if_list":"first",
        "use_mouse": false,
        "mandatory": true,
        "price_rule": "1",
        "num_items_4_flush": 300,
        "scenario_files": [
            [
                "cdata_categories_aio_asus.json",
                "cdata_categories_aio_dell.json",
                "cdata_categories_aio_hp.json"
            ],
            [
                "cdata_categories_desktops.json",
                "cdata_categories_gaming_desktops.json",
                "cdata_categories_workstatios.json"
            ],
            [
                "cdata_categories_laptops_asus.json",
                "cdata_categories_laptops_dell.json",
                "cdata_categories_laptops_hp.json",
                "cdata_categories_gaming_laptops_asus.json",
                "cdata_categories_gaming_laptops_dell.json",
                "cdata_categories_gaming_laptops_hp.json"
            ],
            [
                "cdata_categories_monitors_apple.json",
                "cdata_categories_monitors_dell.json",
                "cdata_categories_monitors_hp.json"
            ],
            [ "cdata_categories_keyboards.json" ],
            [ "cdata_categories_printers.json" ],
            [ "cdata_categories_webcams.json" ],
            [ "cdata_categories_video.json" ],
            [ "cdata_categories_ups.json" ]
        ],
        "last_runned_scenario": ""
    }
    """
    return json.loads(json_str)


def test_bug_json_supplier(bug_json_data):
    """Checks if the 'supplier' field is correctly set to 'bug'."""
    assert bug_json_data["supplier"] == "bug"


def test_bug_json_supplier_prefix(bug_json_data):
    """Checks if the 'supplier_prefix' field is correctly set to 'BUG-'."""
    assert bug_json_data["supplier_prefix"] == "BUG-"


def test_bug_json_start_url(bug_json_data):
    """Checks if the 'start_url' field is set to the correct URL."""
    assert bug_json_data["start_url"] == "https://www.bug.co.il/"


def test_bug_json_if_list_is_first(bug_json_data):
     """Checks if the 'if_list' field is set to 'first'."""
     assert bug_json_data["if_list"] == "first"


def test_bug_json_use_mouse_is_false(bug_json_data):
    """Checks if the 'use_mouse' field is set to False."""
    assert bug_json_data["use_mouse"] is False


def test_bug_json_mandatory_is_true(bug_json_data):
    """Checks if the 'mandatory' field is set to True."""
    assert bug_json_data["mandatory"] is True


def test_bug_json_price_rule(bug_json_data):
    """Checks if the 'price_rule' field is set to '1'."""
    assert bug_json_data["price_rule"] == "1"


def test_bug_json_num_items_4_flush(bug_json_data):
    """Checks if the 'num_items_4_flush' field is set to 300."""
    assert bug_json_data["num_items_4_flush"] == 300


def test_bug_json_scenario_files_is_list(bug_json_data):
    """Checks if the 'scenario_files' field is a list."""
    assert isinstance(bug_json_data["scenario_files"], list)


def test_bug_json_scenario_files_not_empty(bug_json_data):
    """Checks if the 'scenario_files' list is not empty."""
    assert len(bug_json_data["scenario_files"]) > 0


def test_bug_json_scenario_files_contains_lists(bug_json_data):
    """Checks if each item in 'scenario_files' is a list."""
    for item in bug_json_data["scenario_files"]:
        assert isinstance(item, list)


def test_bug_json_scenario_files_content(bug_json_data):
    """Checks if 'scenario_files' contains the expected files."""
    expected_files = [
         [
                "cdata_categories_aio_asus.json",
                "cdata_categories_aio_dell.json",
                "cdata_categories_aio_hp.json"
            ],
            [
                "cdata_categories_desktops.json",
                "cdata_categories_gaming_desktops.json",
                "cdata_categories_workstatios.json"
            ],
            [
                "cdata_categories_laptops_asus.json",
                "cdata_categories_laptops_dell.json",
                "cdata_categories_laptops_hp.json",
                "cdata_categories_gaming_laptops_asus.json",
                "cdata_categories_gaming_laptops_dell.json",
                "cdata_categories_gaming_laptops_hp.json"
            ],
            [
                "cdata_categories_monitors_apple.json",
                "cdata_categories_monitors_dell.json",
                "cdata_categories_monitors_hp.json"
            ],
            [ "cdata_categories_keyboards.json" ],
            [ "cdata_categories_printers.json" ],
            [ "cdata_categories_webcams.json" ],
            [ "cdata_categories_video.json" ],
            [ "cdata_categories_ups.json" ]
    ]
    assert bug_json_data["scenario_files"] == expected_files


def test_bug_json_last_runned_scenario(bug_json_data):
    """Checks if 'last_runned_scenario' is a string and empty."""
    assert isinstance(bug_json_data["last_runned_scenario"], str)
    assert bug_json_data["last_runned_scenario"] == ""


def test_bug_json_invalid_data():
    """Checks if the test fails on invalid json"""
    with pytest.raises(json.JSONDecodeError):
            json_str = """
            {
                "supplier": "bug",
                "supplier_prefix": "BUG-",
                "start_url": "https://www.bug.co.il/",
                 "if_list":"first",
                "use_mouse": false,
                 "mandatory": true,
                "price_rule": "1",
                "num_items_4_flush": 300,
                "scenario_files": [
                [
                        "cdata_categories_aio_asus.json",
                        "cdata_categories_aio_dell.json",
                        "cdata_categories_aio_hp.json"
                    ],
                    [
                        "cdata_categories_desktops.json",
                        "cdata_categories_gaming_desktops.json",
                        "cdata_categories_workstatios.json"
                    ],
                    [
                        "cdata_categories_laptops_asus.json",
                        "cdata_categories_laptops_dell.json",
                        "cdata_categories_laptops_hp.json",
                        "cdata_categories_gaming_laptops_asus.json",
                        "cdata_categories_gaming_laptops_dell.json",
                        "cdata_categories_gaming_laptops_hp.json"
                    ],
                    [
                        "cdata_categories_monitors_apple.json",
                        "cdata_categories_monitors_dell.json",
                        "cdata_categories_monitors_hp.json"
                    ],
                    [ "cdata_categories_keyboards.json" ],
                    [ "cdata_categories_printers.json" ],
                    [ "cdata_categories_webcams.json" ],
                    [ "cdata_categories_video.json" ],
                    [ "cdata_categories_ups.json" ]
                ],
                "last_runned_scenario" ""
            }
            """
            json.loads(json_str)
```