```python
import pytest
import winreg as reg
import os
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch, mock_open, MagicMock
from hypotez.src.gui.context_menu.tkinter import main
from pathlib import Path


@pytest.fixture
def mock_gs_path(tmp_path):
    """Mocks the gs.path object to use a temporary directory for tests."""
    mock_gs_path = MagicMock()
    mock_gs_path.src = tmp_path
    mock_gs_path.src = mock_gs_path.src / "gui" / "context_menu"
    return mock_gs_path


@patch("hypotez.src.gui.context_menu.tkinter.main.gs")
@patch("hypotez.src.gui.context_menu.tkinter.main.messagebox")
@patch("hypotez.src.gui.context_menu.tkinter.main.reg")
def test_add_context_menu_item_success(mock_reg, mock_messagebox, mock_gs, mock_gs_path):
    """
    Tests the successful addition of a context menu item.
    Verifies that the correct registry keys are created and a success message is displayed.
    """
    mock_gs.path = mock_gs_path
    command_path = mock_gs_path.src / "main.py"
    command_path.parent.mkdir(parents=True, exist_ok=True)
    command_path.touch()

    main.add_context_menu_item()
    
    mock_reg.CreateKey.assert_any_call(reg.HKEY_CLASSES_ROOT, r"Directory\\Background\\shell\\hypo_AI_assistant")
    mock_reg.CreateKey.assert_any_call(reg.HKEY_CLASSES_ROOT, r"Directory\\Background\\shell\\hypo_AI_assistant\\command")
    
    mock_reg.SetValue.assert_any_call(mock_reg.CreateKey(), "", reg.REG_SZ, "hypo AI assistant")
    mock_reg.SetValue.assert_any_call(mock_reg.CreateKey(), "", reg.REG_SZ, f'python "{str(command_path)}" "%1"')
    
    mock_messagebox.showinfo.assert_called_with("Успех", "Пункт меню успешно добавлен!")


@patch("hypotez.src.gui.context_menu.tkinter.main.gs")
@patch("hypotez.src.gui.context_menu.tkinter.main.messagebox")
@patch("hypotez.src.gui.context_menu.tkinter.main.reg")
def test_add_context_menu_item_script_not_found(mock_reg, mock_messagebox, mock_gs, mock_gs_path):
    """
    Tests the case where the script file does not exist.
    Verifies that an error message is shown and no registry keys are created.
    """
    mock_gs.path = mock_gs_path
    main.add_context_menu_item()

    mock_messagebox.showerror.assert_called()
    mock_reg.CreateKey.assert_not_called()

@patch("hypotez.src.gui.context_menu.tkinter.main.gs")
@patch("hypotez.src.gui.context_menu.tkinter.main.messagebox")
@patch("hypotez.src.gui.context_menu.tkinter.main.reg")
def test_add_context_menu_item_registry_error(mock_reg, mock_messagebox, mock_gs, mock_gs_path):
    """
    Tests the case where an error occurs during registry modification.
    Verifies that an error message with the exception is displayed.
    """
    mock_gs.path = mock_gs_path
    command_path = mock_gs_path.src / "main.py"
    command_path.parent.mkdir(parents=True, exist_ok=True)
    command_path.touch()
    mock_reg.CreateKey.side_effect = Exception("Registry error")

    main.add_context_menu_item()

    mock_messagebox.showerror.assert_called()
    assert "Registry error" in mock_messagebox.showerror.call_args[0][1]


@patch("hypotez.src.gui.context_menu.tkinter.main.messagebox")
@patch("hypotez.src.gui.context_menu.tkinter.main.reg")
def test_remove_context_menu_item_success(mock_reg, mock_messagebox):
    """
    Tests the successful removal of a context menu item.
    Verifies that the registry key is deleted and a success message is displayed.
    """
    main.remove_context_menu_item()
    mock_reg.DeleteKey.assert_called_with(reg.HKEY_CLASSES_ROOT, r"Directory\\Background\\shell\\hypo_AI_assistant")
    mock_messagebox.showinfo.assert_called_with("Успех", "Пункт меню успешно удален!")

@patch("hypotez.src.gui.context_menu.tkinter.main.messagebox")
@patch("hypotez.src.gui.context_menu.tkinter.main.reg")
def test_remove_context_menu_item_not_found(mock_reg, mock_messagebox):
    """
    Tests the case where the context menu item does not exist.
    Verifies that a warning message is shown and no exception is raised.
    """
    mock_reg.DeleteKey.side_effect = FileNotFoundError("Key not found")
    main.remove_context_menu_item()
    mock_messagebox.showwarning.assert_called_with("Предупреждение", "Пункт меню не найден.")

@patch("hypotez.src.gui.context_menu.tkinter.main.messagebox")
@patch("hypotez.src.gui.context_menu.tkinter.main.reg")
def test_remove_context_menu_item_registry_error(mock_reg, mock_messagebox):
    """
    Tests the case where an error occurs during registry key deletion.
    Verifies that an error message is shown with the exception details.
    """
    mock_reg.DeleteKey.side_effect = Exception("Registry error")
    main.remove_context_menu_item()
    mock_messagebox.showerror.assert_called()
    assert "Registry error" in mock_messagebox.showerror.call_args[0][1]

def test_create_gui():
    """
    Tests the creation of the main GUI window.
    Verifies that the main window is created with buttons and that the main loop runs.
    This is a basic test to ensure GUI elements can initialize correctly.
    """
    with patch("tkinter.Tk") as mock_tk:
         with patch("tkinter.mainloop") as mock_mainloop:
            main.create_gui()
            mock_tk.assert_called_once()
            mock_mainloop.assert_called_once()
```