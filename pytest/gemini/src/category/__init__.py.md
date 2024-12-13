```python
import pytest

from hypotez.src.category import Category


def test_category_creation_valid_input():
    """
    Test the creation of a Category object with valid input.
    """
    category = Category(name="Test Category", description="This is a test category.", slug="test-category")
    assert category.name == "Test Category"
    assert category.description == "This is a test category."
    assert category.slug == "test-category"
    assert category.parent is None


def test_category_creation_with_parent():
    """
    Test the creation of a Category object with a parent category.
    """
    parent_category = Category(name="Parent Category", description="Parent.", slug="parent-category")
    category = Category(name="Test Category", description="This is a test category.", slug="test-category", parent=parent_category)
    assert category.parent == parent_category


def test_category_creation_no_slug():
    """
    Test the creation of a Category object with no slug.
    The slug is automatically generated from the name.
    """
    category = Category(name="Test Category", description="This is a test category.")
    assert category.name == "Test Category"
    assert category.description == "This is a test category."
    assert category.slug == "test-category"
    assert category.parent is None


def test_category_add_child():
    """
    Test adding a child category to a Category object.
    """
    parent_category = Category(name="Parent Category", description="Parent.", slug="parent-category")
    child_category = Category(name="Child Category", description="Child.", slug="child-category")
    parent_category.add_child(child_category)
    assert child_category in parent_category.children
    assert child_category.parent == parent_category


def test_category_add_existing_child():
    """
    Test adding a child category that is already added.
    """
    parent_category = Category(name="Parent Category", description="Parent.", slug="parent-category")
    child_category = Category(name="Child Category", description="Child.", slug="child-category")
    parent_category.add_child(child_category)
    with pytest.raises(ValueError, match=r"Category already added"):
        parent_category.add_child(child_category)


def test_category_add_self_as_child():
    """
    Test adding a category as its own child, which should raise an exception.
    """
    category = Category(name="Self Category", description="Self.", slug="self-category")
    with pytest.raises(ValueError, match=r"A category cannot add itself as a child."):
        category.add_child(category)

def test_category_add_child_already_has_parent():
    """
    Test adding a category that already has a parent as a child.
    """
    parent_category = Category(name="Parent Category", description="Parent.", slug="parent-category")
    other_parent = Category(name="Other Parent", description="Other parent.", slug="other-parent")
    child_category = Category(name="Child Category", description="Child.", slug="child-category")
    other_parent.add_child(child_category)
    with pytest.raises(ValueError, match="Category already has a parent"):
        parent_category.add_child(child_category)

def test_category_remove_child():
    """
    Test removing a child category from a Category object.
    """
    parent_category = Category(name="Parent Category", description="Parent.", slug="parent-category")
    child_category = Category(name="Child Category", description="Child.", slug="child-category")
    parent_category.add_child(child_category)
    parent_category.remove_child(child_category)
    assert child_category not in parent_category.children
    assert child_category.parent is None


def test_category_remove_nonexistent_child():
    """
    Test removing a child category that does not belong to the parent category.
    """
    parent_category = Category(name="Parent Category", description="Parent.", slug="parent-category")
    child_category = Category(name="Child Category", description="Child.", slug="child-category")
    with pytest.raises(ValueError, match=r"Category does not belong to this parent"):
        parent_category.remove_child(child_category)


def test_category_remove_child_from_other_parent():
    """
    Test removing a child category from a category when it belongs to another parent.
    """
    parent_category = Category(name="Parent Category", description="Parent.", slug="parent-category")
    other_parent = Category(name="Other Parent", description="Other parent.", slug="other-parent")
    child_category = Category(name="Child Category", description="Child.", slug="child-category")
    other_parent.add_child(child_category)
    with pytest.raises(ValueError, match=r"Category does not belong to this parent"):
      parent_category.remove_child(child_category)

def test_category_slug_generation_from_name():
    """
    Test slug generation with special characters and spaces
    """
    category = Category(name="Test Category with & special $ chars", description="This is a test.")
    assert category.slug == "test-category-with-special-chars"

def test_category_repr():
    """
    Test the __repr__ method of Category.
    """
    category = Category(name="Test Category", description="This is a test category.", slug="test-category")
    expected_repr = "Category(name='Test Category', slug='test-category')"
    assert repr(category) == expected_repr
```