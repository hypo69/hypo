# ProductEditor Class Documentation

## Overview

This module provides a graphical user interface (GUI) for editing product data, specifically for products sourced from AliExpress.  It leverages the `AliCampaignEditor` class for product preparation.  The `ProductEditor` class handles file loading, UI setup, and asynchronous product preparation.


## Table of Contents

* [ProductEditor](#product-editor)
    * [__init__](#__init__)
    * [setup_ui](#setup_ui)
    * [setup_connections](#setup_connections)
    * [open_file](#open_file)
    * [load_file](#load_file)
    * [create_widgets](#create_widgets)
    * [prepare_product_async](#prepare_product_async)


## Classes

### `ProductEditor`

**Description**: This class provides a Qt-based widget for editing product information. It handles loading product data from a JSON file, displaying basic details, and initiating the product preparation process using `AliCampaignEditor`.

**Attributes**:

- `data`: `SimpleNamespace`: Holds the loaded product data.
- `language`: `str`: Product language.
- `currency`: `str`: Product currency.
- `file_path`: `str`: Path to the loaded JSON file.
- `editor`: `AliCampaignEditor`: Instance for product preparation.

**Methods**:

#### `__init__`

```python
def __init__(self, parent=None, main_app=None):
    """ Initialize the ProductEditor widget 

    Args:
        parent (Optional[QWidget], optional): Parent widget. Defaults to None.
        main_app (Optional[MainApp], optional): Main application instance. Defaults to None.

    """
    super().__init__(parent)
    self.main_app = main_app  # Save the MainApp instance

    self.setup_ui()
    self.setup_connections()
```

#### `setup_ui`

```python
def setup_ui(self):
    """ Setup the user interface """
    self.setWindowTitle("Product Editor")
    self.resize(1800, 800)

    # Define UI components... (see file for full implementation)
    # ... (rest of the setup_ui method)
```

#### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections """
    pass
```

#### `open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        self,
        "Open JSON File",
        "c:/user/documents/repos/hypotez/data/aliexpress/products",
        "JSON files (*.json)"
    )
    if not file_path:
        return  # No file selected

    self.load_file(file_path)
```

#### `load_file`

```python
def load_file(self, file_path):
    """ Load a JSON file """
    try:
        self.data = j_loads_ns(file_path)
        self.file_path = file_path
        self.file_name_label.setText(f"File: {self.file_path}")
        self.editor = AliCampaignEditor(file_path=file_path)
        self.create_widgets(self.data)
    except Exception as ex:
        QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")
```

#### `create_widgets`

```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
    layout = self.layout()
    # Remove previous widgets... (see file for full implementation)
    # ... (rest of the create_widgets method)
```

#### `prepare_product_async`

```python
@asyncSlot()
async def prepare_product_async(self):
    """ Asynchronously prepare the product """
    if self.editor:
        try:
            await self.editor.prepare_product()
            QtWidgets.QMessageBox.information(self, "Success", "Product prepared successfully.")
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to prepare product: {ex}")
```


## Functions (Imported)

This section lists functions from imported modules, but their documentation is not provided within this file.


```
```