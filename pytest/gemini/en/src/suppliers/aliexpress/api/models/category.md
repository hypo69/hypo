```python
import pytest
from hypotez.src.suppliers.aliexpress.api.models.category import Category, ChildCategory


def test_category_creation_valid():
    """Tests creating a Category object with valid data."""
    category = Category(category_id=1, category_name="Electronics")
    assert category.category_id == 1
    assert category.category_name == "Electronics"


def test_child_category_creation_valid():
    """Tests creating a ChildCategory object with valid data."""
    child_category = ChildCategory(category_id=2, category_name="Phones", parent_category_id=1)
    assert child_category.category_id == 2
    assert child_category.category_name == "Phones"
    assert child_category.parent_category_id == 1


def test_category_creation_invalid_category_id():
    """Tests creating a Category object with an invalid category_id (non-integer)."""
    with pytest.raises(TypeError):
        Category(category_id="abc", category_name="Electronics")


def test_category_creation_invalid_category_name():
    """Tests creating a Category object with an invalid category_name (non-string)."""
    with pytest.raises(TypeError):
        Category(category_id=1, category_name=123)

def test_child_category_creation_invalid_parent_category_id():
    """Tests creating a ChildCategory object with an invalid parent_category_id (non-integer)."""
    with pytest.raises(TypeError):
        ChildCategory(category_id=2, category_name="Phones", parent_category_id="abc")


def test_child_category_creation_missing_parent_category_id():
    """Tests creating a ChildCategory object without parent_category_id."""
    with pytest.raises(TypeError) as excinfo: #Use excinfo for more detailed error catching
        ChildCategory(category_id=2, category_name="Phones")

    assert "missing 1 required positional argument: 'parent_category_id'" in str(excinfo.value)


def test_category_creation_missing_category_id():
    """Tests creating a Category object without category_id."""
    with pytest.raises(TypeError) as excinfo:
        Category(category_name="Electronics")
    assert "missing 1 required positional argument: 'category_id'" in str(excinfo.value)


def test_category_creation_missing_category_name():
    """Tests creating a Category object without category_name."""
    with pytest.raises(TypeError) as excinfo:
        Category(category_id=1)
    assert "missing 1 required positional argument: 'category_name'" in str(excinfo.value)

```