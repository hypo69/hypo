```python
import pytest

from hypotez.src.endpoints.emil import EmilDesign
from hypotez.src.endpoints.emil import MODE


def test_module_mode():
    """
    Test if the module's MODE variable is set correctly.
    """
    assert MODE == "dev", "Module MODE should be set to 'dev' by default."


def test_emildesign_instantiation():
    """
    Test if EmilDesign class can be instantiated.
    """
    try:
        emil_design = EmilDesign()
    except Exception as e:
        pytest.fail(f"EmilDesign instantiation failed with exception: {e}")
    assert isinstance(emil_design, EmilDesign), "EmilDesign object should be instantiated successfully."

    
def test_emildesign_has_default_attrs():
    """
    Test if EmilDesign class has necessary attributes after instantiation.
    """
    emil_design = EmilDesign()
    assert hasattr(emil_design, "_params"), "EmilDesign should have attribute _params"
    assert hasattr(emil_design, "_mode"), "EmilDesign should have attribute _mode"
    
def test_emildesign_default_mode_is_dev():
    """
    Test that EmilDesign's _mode attribute is set to 'dev' by default.
    """
    emil_design = EmilDesign()
    assert emil_design._mode == "dev", "EmilDesign's default mode should be 'dev'."

def test_emildesign_params_is_dict():
    """
    Test that EmilDesign's _params attribute is a dictionary.
    """
    emil_design = EmilDesign()
    assert isinstance(emil_design._params, dict), "EmilDesign's _params should be a dictionary."


def test_emildesign_has_set_mode():
    """
    Test that EmilDesign has set_mode method
    """
    emil_design = EmilDesign()
    assert hasattr(emil_design, "set_mode"), "EmilDesign should have attribute set_mode"

def test_emildesign_set_mode_correct():
    """
    Test if set_mode changes mode correctly
    """
    emil_design = EmilDesign()
    emil_design.set_mode("test")
    assert emil_design._mode == "test", "EmilDesign's mode should be changed by set_mode"

def test_emildesign_set_mode_invalid():
    """
    Test if set_mode throws exception on wrong input
    """
    emil_design = EmilDesign()
    with pytest.raises(ValueError) as excinfo:
        emil_design.set_mode(123)
    assert "set_mode accepts string parameter." in str(excinfo.value)
```