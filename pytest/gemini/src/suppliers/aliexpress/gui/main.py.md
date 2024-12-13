```python
import pytest
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication
from unittest.mock import MagicMock, patch
import sys
from src.suppliers.aliexpress.gui.main import MainApp

@pytest.fixture
def app(qtbot):
    """Fixture to initialize the MainApp and QApplication for testing."""
    test_app = QApplication(sys.argv)
    main_app = MainApp()
    qtbot.addWidget(main_app)
    return main_app

def test_main_app_initialization(app):
    """Test if MainApp initializes correctly."""
    assert app.windowTitle() == "Main Application with Tabs"
    assert app.centralWidget() is not None
    assert len(app.tab_widget.children()) == 3  # Check if all tabs are created
    assert app.menuBar() is not None
    assert app.promotion_app is not None
    assert app.campaign_editor_app is not None
    assert app.product_editor_app is not None

def test_create_menubar(app):
    """Test if menu bar is created with all actions."""
    menubar = app.menuBar()
    assert menubar.findChild(QtGui.QMenu, "File") is not None
    assert menubar.findChild(QtGui.QMenu, "Edit") is not None
    file_menu = menubar.findChild(QtGui.QMenu, "File")
    edit_menu = menubar.findChild(QtGui.QMenu, "Edit")
    
    assert len(file_menu.actions()) == 4
    assert len(edit_menu.actions()) == 2

    assert file_menu.actions()[0].text() == "Open"
    assert file_menu.actions()[1].text() == "Save"
    assert file_menu.actions()[2].text() == "Exit"
    assert file_menu.actions()[3].text() == "Open Product File"

    assert edit_menu.actions()[0].text() == "Copy"
    assert edit_menu.actions()[1].text() == "Paste"

def test_open_file_dialog(app, qtbot, monkeypatch):
    """Test open file dialog."""
    mock_getOpenFileName = MagicMock(return_value=("/path/to/file.json", "JSON files (*.json)"))
    monkeypatch.setattr(QtWidgets.QFileDialog, "getOpenFileName", mock_getOpenFileName)
    mock_load_file = MagicMock()
    app.load_file = mock_load_file
    
    
    open_action = app.menuBar().findChild(QtGui.QMenu, "File").actions()[0]
    qtbot.mouseClick(open_action, QtCore.Qt.MouseButton.LeftButton)
    
    mock_getOpenFileName.assert_called()
    mock_load_file.assert_called_once_with("/path/to/file.json")
    
def test_open_file_dialog_cancelled(app, qtbot, monkeypatch):
    """Test open file dialog when cancelled."""
    mock_getOpenFileName = MagicMock(return_value=("", "JSON files (*.json)"))
    monkeypatch.setattr(QtWidgets.QFileDialog, "getOpenFileName", mock_getOpenFileName)
    mock_load_file = MagicMock()
    app.load_file = mock_load_file
    
    open_action = app.menuBar().findChild(QtGui.QMenu, "File").actions()[0]
    qtbot.mouseClick(open_action, QtCore.Qt.MouseButton.LeftButton)

    mock_getOpenFileName.assert_called()
    mock_load_file.assert_not_called()

def test_save_file_promotion_app(app, qtbot):
    """Test save file functionality for the promotion editor."""
    app.tab_widget.setCurrentIndex(0)
    mock_save_changes = MagicMock()
    app.promotion_app.save_changes = mock_save_changes
    
    save_action = app.menuBar().findChild(QtGui.QMenu, "File").actions()[1]
    qtbot.mouseClick(save_action, QtCore.Qt.MouseButton.LeftButton)
    
    mock_save_changes.assert_called_once()
    
def test_save_file_product_app(app, qtbot):
    """Test save file functionality for the product editor."""
    app.tab_widget.setCurrentIndex(2)
    mock_save_product = MagicMock()
    app.product_editor_app.save_product = mock_save_product
    
    save_action = app.menuBar().findChild(QtGui.QMenu, "File").actions()[1]
    qtbot.mouseClick(save_action, QtCore.Qt.MouseButton.LeftButton)
    
    mock_save_product.assert_called_once()

def test_exit_application(app, qtbot):
    """Test exit application functionality."""
    with qtbot.wait_signal(app.destroyed):
        exit_action = app.menuBar().findChild(QtGui.QMenu, "File").actions()[2]
        qtbot.mouseClick(exit_action, QtCore.Qt.MouseButton.LeftButton)
    assert not app.isVisible()

def test_copy_with_focus_widget(app, qtbot):
    """Test copy action with focused text widget."""
    text_edit = QtWidgets.QTextEdit()
    text_edit.setText("test text")
    app.setFocusProxy(text_edit)
    app.setCentralWidget(text_edit)
    
    copy_action = app.menuBar().findChild(QtGui.QMenu, "Edit").actions()[0]
    qtbot.mouseClick(copy_action, QtCore.Qt.MouseButton.LeftButton)
    
    clipboard = QApplication.clipboard()
    assert clipboard.text() == "test text"


def test_copy_without_focus_widget(app, qtbot):
     """Test copy action without a focused text widget."""
     mock_message_box = MagicMock()
     QtWidgets.QMessageBox.warning = mock_message_box
     
     copy_action = app.menuBar().findChild(QtGui.QMenu, "Edit").actions()[0]
     qtbot.mouseClick(copy_action, QtCore.Qt.MouseButton.LeftButton)
     
     mock_message_box.assert_called_once()

def test_paste_with_focus_widget(app, qtbot):
    """Test paste action with focused text widget."""
    text_edit = QtWidgets.QTextEdit()
    app.setFocusProxy(text_edit)
    app.setCentralWidget(text_edit)
    
    clipboard = QApplication.clipboard()
    clipboard.setText("pasted text")
    
    paste_action = app.menuBar().findChild(QtGui.QMenu, "Edit").actions()[1]
    qtbot.mouseClick(paste_action, QtCore.Qt.MouseButton.LeftButton)
    
    assert text_edit.toPlainText() == "pasted text"

def test_paste_without_focus_widget(app, qtbot):
    """Test paste action without a focused text widget."""
    mock_message_box = MagicMock()
    QtWidgets.QMessageBox.warning = mock_message_box
    
    paste_action = app.menuBar().findChild(QtGui.QMenu, "Edit").actions()[1]
    qtbot.mouseClick(paste_action, QtCore.Qt.MouseButton.LeftButton)
    
    mock_message_box.assert_called_once()

def test_load_file_success(app, qtbot):
    """Test loading of a JSON file successfully."""
    mock_load_file = MagicMock()
    app.promotion_app.load_file = mock_load_file
    
    app.load_file("test_file.json")
    
    mock_load_file.assert_called_once_with("test_file.json")
    

def test_load_file_failure(app, qtbot):
    """Test loading of a JSON file with failure."""
    mock_load_file = MagicMock(side_effect=Exception("test error"))
    app.promotion_app.load_file = mock_load_file
    mock_message_box = MagicMock()
    QtWidgets.QMessageBox.critical = mock_message_box
    
    app.load_file("test_file.json")
    
    mock_load_file.assert_called_once_with("test_file.json")
    mock_message_box.assert_called_once()


def test_main_function(qtbot, monkeypatch):
     """Test the main function which initializes and runs the app."""
     mock_qapplication = MagicMock()
     mock_qevent_loop = MagicMock()
     mock_main_app = MagicMock()
     mock_show = MagicMock()
     mock_run_forever = MagicMock()
     
     monkeypatch.setattr(QtWidgets, "QApplication", mock_qapplication)
     monkeypatch.setattr("src.suppliers.aliexpress.gui.main.QEventLoop", mock_qevent_loop)
     monkeypatch.setattr("src.suppliers.aliexpress.gui.main.MainApp", mock_main_app)
     mock_main_app_instance = mock_main_app()
     mock_main_app_instance.show = mock_show
     mock_qevent_loop_instance = mock_qevent_loop()
     mock_qevent_loop_instance.__enter__ = MagicMock(return_value=mock_qevent_loop_instance)
     mock_qevent_loop_instance.run_forever = mock_run_forever
     
     from src.suppliers.aliexpress.gui.main import main
     main()
     
     mock_qapplication.assert_called_once()
     mock_qevent_loop.assert_called_once()
     mock_main_app.assert_called_once()
     mock_show.assert_called_once()
     mock_run_forever.assert_called_once()

def test_open_product_file(app, qtbot):
    """Test if open product file action calls the correct method of ProductEditor."""
    mock_open_file = MagicMock()
    app.product_editor_app.open_file = mock_open_file
    
    open_product_action = app.menuBar().findChild(QtGui.QMenu, "File").actions()[3]
    qtbot.mouseClick(open_product_action, QtCore.Qt.MouseButton.LeftButton)
    
    mock_open_file.assert_called_once()
```