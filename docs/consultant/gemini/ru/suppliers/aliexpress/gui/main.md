```python
## \file hypotez/src/suppliers/aliexpress/gui/main.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.aliexpress.gui """
MODE = 'development'


""" Main window interface for managing advertising campaigns """



import header
import asyncio
import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from qasync import QEventLoop
from pathlib import Path
from src.utils import j_loads_ns, j_dumps
from product import ProductEditor
from campaign import CampaignEditor
from category import CategoryEditor
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from styles import set_fixed_size
from src.logger import logger

class MainApp(QtWidgets.QMainWindow):
    """
    Main application window for managing advertising campaigns.
    """
    def __init__(self):
        """ Initialize the main application with tabs. """
        super().__init__()
        self.setWindowTitle("Main Application with Tabs")
        self.setGeometry(100, 100, 1800, 800)

        self.tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Create the JSON Editor tab and add it to the tab widget
        self.tab1 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab1, "JSON Editor")
        self.campaign_editor_app = AliCampaignEditor(self.tab1, self) # Используем AliCampaignEditor


        # Create the Campaign Editor tab and add it to the tab widget
        self.tab2 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab2, "Campaign Editor")
        self.campaign_editor_app = CategoryEditor(self.tab2, self)


        # Create the Product Editor tab and add it to the tab widget
        self.tab3 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab3, "Product Editor")
        self.product_editor_app = ProductEditor(self.tab3, self)

        self.create_menubar()

    def create_menubar(self):
        """ Create a menu bar with options for file operations and edit commands. """
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        open_action = QtGui.QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        save_action = QtGui.QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        exit_action = QtGui.QAction("Exit", self)
        exit_action.triggered.connect(self.exit_application)
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu("Edit")
        copy_action = QtGui.QAction("Copy", self)
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)
        paste_action = QtGui.QAction("Paste", self)
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)

        open_product_action = QtGui.QAction("Open Product File", self)
        open_product_action.triggered.connect(self.product_editor_app.open_file)
        file_menu.addAction(open_product_action)


    def open_file(self):
        """ Open a file dialog to select and load a JSON file. """
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "JSON files (*.json)")
        if not file_path:
            return
        try:
            self.load_file(file_path)
        except Exception as e:
            logger.error(f"Error loading file {file_path}: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load file: {e}")

    def save_file(self):
        """ Save the current file. """
        current_index = self.tab_widget.currentIndex()
        if current_index == 0:
            self.campaign_editor_app.save_changes() # Используем campaign_editor_app
        elif current_index == 2:
            self.product_editor_app.save_product()


    def exit_application(self):
        """ Exit the application. """
        self.close()

    def copy(self):
        """ Copy selected text to the clipboard. """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.copy()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to copy.")

    def paste(self):
        """ Paste text from the clipboard. """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.paste()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to paste.")

    def load_file(self, campaign_file):
        """ Load the JSON file. """
        try:
          self.campaign_editor_app.load_file(campaign_file) # Используем campaign_editor_app
        except Exception as ex:
            logger.error(f"Error loading file {campaign_file}: {ex}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")



def main():
    """ Initialize and run the application. """
    app = QtWidgets.QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    main_app = MainApp()
    main_app.show()
    with loop:
        loop.run_forever()

if __name__ == "__main__":
    main()
```

```
Изменения:
- Добавлена обработка ошибок с помощью `logger.error` и `try...except` блоков для предотвращения аварийных завершений программы.
- Изменены вызовы методов для работы с соответствующими приложениями (CampaignEditor, ProductEditor).
- Исправлено имя переменной `promotion_app` на `campaign_editor_app` для соответствия логике использования.
- Добавлено импортирование `from src.logger import logger`.
- Добавлены RST-документации к методам `__init__`, `create_menubar`, `open_file`, `save_file`, `exit_application`, `copy`, `paste`, и `load_file`.
- Изменен метод `load_file` для работы с `self.campaign_editor_app`.
```