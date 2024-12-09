```python
import pytest
import winreg as reg
import os
from PyQt6 import QtWidgets
import sys  # Needed for mocking sys.exit
from unittest.mock import patch, Mock

# Mock the necessary imports
import header
from src import gs


@patch("src.gui.context_menu.qt6.QtWidgets")
@patch("src.gui.context_menu.qt6.gs")
@patch("src.gui.context_menu.qt6.os")
def test_add_context_menu_item(mock_os, mock_gs, mock_QtWidgets):
    """Tests the add_context_menu_item function."""

    # Mock the file existence check
    mock_os.path.exists.return_value = True
    mock_gs.path.src.return_value = Mock(
        __truediv__=lambda self, path: f"/path/{path}"
    )
    
    # Test valid case
    add_context_menu_item()
    mock_QtWidgets.QMessageBox.information.assert_called_once_with(
        None, "Успех", "Пункт меню успешно добавлен!"
    )
    mock_QtWidgets.QMessageBox.critical.assert_not_called()  

    # Test file not found
    mock_os.path.exists.return_value = False
    add_context_menu_item()
    mock_QtWidgets.QMessageBox.critical.assert_called_once()

    # Test exception handling
    mock_os.path.exists.side_effect = Exception("Test exception")
    with pytest.raises(Exception) as excinfo:
        add_context_menu_item()

    mock_QtWidgets.QMessageBox.critical.assert_called_once()
    assert "Test exception" in str(excinfo.value)

@patch("src.gui.context_menu.qt6.QtWidgets")
@patch("src.gui.context_menu.qt6.reg")
def test_remove_context_menu_item(mock_reg, mock_QtWidgets):
    """Tests the remove_context_menu_item function."""

    # Test successful removal
    mock_reg.DeleteKey.return_value = None
    remove_context_menu_item()
    mock_QtWidgets.QMessageBox.information.assert_called_once_with(
        None, "Успех", "Пункт меню успешно удален!"
    )


    # Test item not found
    mock_reg.DeleteKey.side_effect = FileNotFoundError()
    remove_context_menu_item()
    mock_QtWidgets.QMessageBox.warning.assert_called_once()

    # Test other exception
    mock_reg.DeleteKey.side_effect = Exception("Test exception")
    with pytest.raises(Exception) as excinfo:
        remove_context_menu_item()
    mock_QtWidgets.QMessageBox.critical.assert_called_once_with(None, "Ошибка", "Ошибка: Test exception")
    
    # Check if warning is called in case of other exceptions.
    mock_reg.DeleteKey.side_effect = ValueError('Fake value')
    with pytest.raises(ValueError) as excinfo:
        remove_context_menu_item()
    assert "Fake value" in str(excinfo.value)


@patch("src.gui.context_menu.qt6.QtWidgets")
def test_context_menu_manager_init(mock_QtWidgets):
    """Tests the ContextMenuManager class."""
    window = ContextMenuManager()
    assert isinstance(window, ContextMenuManager)
    mock_QtWidgets.QApplication.assert_called_once_with([])
    assert window.windowTitle() == "Управление контекстным меню"

# Import the necessary modules to avoid circular import issues.
from hypotez.src.gui.context_menu.qt6.main import add_context_menu_item, remove_context_menu_item, ContextMenuManager

```

**Explanation and Improvements:**

1. **Mocking:** The tests now effectively mock `QtWidgets.QMessageBox`, `gs.path`, and `os`. This is crucial because these functions interact with external resources (like the registry and files).  Mocking prevents unexpected interactions and ensures your tests are isolated.

2. **Comprehensive Error Handling:**  The tests cover cases where the script file is not found (`FileNotFoundError`), and more importantly, they test the exception handling in `add_context_menu_item` and `remove_context_menu_item`, which is vital in real-world applications.

3. **Clearer Assertions:** Assertions now directly check for the expected calls to `QMessageBox.information`, `QMessageBox.warning`, and `QMessageBox.critical`, making it easier to understand the test results.

4. **Specific Error Catching:** The `test_remove_context_menu_item` function is improved to use `pytest.raises` for exception testing and now includes catching `ValueError` as well.


5. **Test for `ContextMenuManager`:** Added a `test_context_menu_manager_init` to verify the instantiation of the `ContextMenuManager` class, including checks for the window title and the correct initialization.


**How to Run the Tests:**

1.  Save the code as a Python file (e.g., `test_context_menu.py`).
2.  Make sure you have `pytest` installed (`pip install pytest`).
3.  Run the tests from your terminal: `pytest test_context_menu.py`

This improved set of tests provides a much more comprehensive and robust way to ensure the correctness of your code, addressing the crucial aspect of error handling and interaction with external resources. Remember to replace the placeholder `gs.path.src` with your actual path implementation.