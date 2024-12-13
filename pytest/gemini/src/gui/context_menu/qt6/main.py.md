```python
import pytest
import winreg as reg
import os
from unittest.mock import patch, mock_open, MagicMock
from PyQt6 import QtWidgets
from pathlib import Path

# Assuming 'header' and 'gs' are mocked or stubbed since they are external dependencies
# For example, you could create a mock gs.path object
class MockGSPath:
    def __init__(self, base_path):
      self.src = Path(base_path)
      
mock_gs = type('mock_gs', (object,), {'path': MockGSPath(Path(__file__).parent)})()

@pytest.fixture
def mock_qmessagebox():
    """Mocks QMessageBox for testing UI interactions."""
    with patch("src.gui.context_menu.qt6.main.QtWidgets.QMessageBox") as mock:
        yield mock
        
@pytest.fixture
def mock_os_path_exists():
    """Mocks os.path.exists for testing file existence."""
    with patch("src.gui.context_menu.qt6.main.os.path.exists") as mock:
        yield mock

@pytest.fixture
def mock_winreg_create_key():
    """Mocks winreg.CreateKey for testing registry interaction."""
    with patch("src.gui.context_menu.qt6.main.reg.CreateKey") as mock:
        yield mock

@pytest.fixture
def mock_winreg_set_value():
    """Mocks winreg.SetValue for testing registry interaction."""
    with patch("src.gui.context_menu.qt6.main.reg.SetValue") as mock:
        yield mock

@pytest.fixture
def mock_winreg_delete_key():
    """Mocks winreg.DeleteKey for testing registry interaction."""
    with patch("src.gui.context_menu.qt6.main.reg.DeleteKey") as mock:
        yield mock
        

def test_add_context_menu_item_success(mock_winreg_create_key, mock_winreg_set_value, mock_os_path_exists, mock_qmessagebox):
    """
    Test successful addition of the context menu item.
    This test checks if the correct registry keys and values are set
    and if the success message is displayed.
    """
    mock_os_path_exists.return_value = True
    mock_winreg_create_key.side_effect = lambda key, path: MagicMock()
    
    import src.gui.context_menu.qt6.main as main
    main.gs = mock_gs
    
    main.add_context_menu_item()
    
    mock_winreg_create_key.assert_called()
    mock_winreg_set_value.assert_called()
    mock_qmessagebox.information.assert_called_with(None, "Успех", "Пункт меню успешно добавлен!")

def test_add_context_menu_item_file_not_found(mock_os_path_exists, mock_qmessagebox):
    """
    Test case where the script file is not found.
    This test verifies that an error message is displayed when the command
    path does not exist.
    """
    mock_os_path_exists.return_value = False
    import src.gui.context_menu.qt6.main as main
    main.gs = mock_gs
    main.add_context_menu_item()
    mock_qmessagebox.critical.assert_called()
    
def test_add_context_menu_item_exception(mock_winreg_create_key, mock_os_path_exists, mock_qmessagebox):
    """
    Test exception during registry modification.
    This test checks if an error message is displayed if there's an exception 
    when creating a key or setting value
    """
    mock_os_path_exists.return_value = True
    mock_winreg_create_key.side_effect = Exception("Test Exception")
    
    import src.gui.context_menu.qt6.main as main
    main.gs = mock_gs
    
    main.add_context_menu_item()
    mock_qmessagebox.critical.assert_called()

def test_remove_context_menu_item_success(mock_winreg_delete_key, mock_qmessagebox):
    """
    Test successful removal of the context menu item.
    This test checks if the correct registry key is deleted
    and if the success message is displayed.
    """
    mock_winreg_delete_key.return_value = None
    
    import src.gui.context_menu.qt6.main as main
    main.remove_context_menu_item()
    mock_winreg_delete_key.assert_called()
    mock_qmessagebox.information.assert_called_with(None, "Успех", "Пункт меню успешно удален!")

def test_remove_context_menu_item_not_found(mock_winreg_delete_key, mock_qmessagebox):
    """
    Test case where the context menu item is not found.
    This test checks if the warning message is displayed
    if the key to delete does not exist.
    """
    mock_winreg_delete_key.side_effect = FileNotFoundError("Test File Not Found Error")
    import src.gui.context_menu.qt6.main as main
    main.remove_context_menu_item()
    mock_qmessagebox.warning.assert_called()

def test_remove_context_menu_item_exception(mock_winreg_delete_key, mock_qmessagebox):
    """
    Test exception during registry key deletion.
    This test checks if an error message is displayed if there's an exception during key deletion.
    """
    mock_winreg_delete_key.side_effect = Exception("Test Exception")
    import src.gui.context_menu.qt6.main as main
    main.remove_context_menu_item()
    mock_qmessagebox.critical.assert_called()

def test_context_menu_manager_init():
    """Test initialization of the ContextMenuManager class."""
    import src.gui.context_menu.qt6.main as main
    
    app = QtWidgets.QApplication([])
    manager = main.ContextMenuManager()
    assert manager.windowTitle() == "Управление контекстным меню"
    assert manager.layout() is not None

def test_context_menu_manager_add_button(mock_qmessagebox):
     """Test add button click event."""
     import src.gui.context_menu.qt6.main as main
     app = QtWidgets.QApplication([])
     manager = main.ContextMenuManager()
     manager.show()
     
     add_button = manager.findChild(QtWidgets.QPushButton, "Добавить пункт меню")
     
     with patch("src.gui.context_menu.qt6.main.add_context_menu_item") as mock_add:
         add_button.click()
         mock_add.assert_called()

def test_context_menu_manager_remove_button(mock_qmessagebox):
    """Test remove button click event."""
    import src.gui.context_menu.qt6.main as main
    app = QtWidgets.QApplication([])
    manager = main.ContextMenuManager()
    manager.show()
    
    remove_button = manager.findChild(QtWidgets.QPushButton, "Удалить пункт меню")
    
    with patch("src.gui.context_menu.qt6.main.remove_context_menu_item") as mock_remove:
      remove_button.click()
      mock_remove.assert_called()


def test_context_menu_manager_exit_button(qtbot):
    """Test exit button click event."""
    import src.gui.context_menu.qt6.main as main
    app = QtWidgets.QApplication([])
    manager = main.ContextMenuManager()
    manager.show()
    
    exit_button = manager.findChild(QtWidgets.QPushButton, "Выход")
    
    with patch.object(manager, 'close') as mock_close:
       exit_button.click()
       mock_close.assert_called()

```