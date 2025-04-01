# Модуль `category.py`

## Обзор

Модуль `category.py` предоставляет графический интерфейс (GUI) для подготовки рекламных кампаний AliExpress. Он позволяет пользователю загружать JSON-файлы с данными о кампаниях, просматривать категории товаров и запускать процесс подготовки категорий. Модуль использует библиотеку PyQt6 для создания интерфейса и `asyncio` для асинхронного выполнения задач.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации процесса подготовки рекламных кампаний на AliExpress. Он предоставляет удобный интерфейс для загрузки данных о кампаниях из JSON-файлов и запуска подготовки категорий. GUI позволяет визуально контролировать процесс и отображает информацию о загруженных данных.

## Классы

### `CategoryEditor`

**Описание**: Основной класс, представляющий виджет редактора категорий. Он содержит методы для загрузки файлов, создания виджетов на основе данных из файла и запуска подготовки категорий.

**Методы**:
- `__init__`: Инициализирует виджет редактора категорий.
- `setup_ui`: Настраивает пользовательский интерфейс.
- `setup_connections`: Настраивает соединения между сигналами и слотами.
- `open_file`: Открывает диалоговое окно для выбора JSON-файла.
- `load_file`: Загружает JSON-файл и создает виджеты на основе данных.
- `create_widgets`: Создает виджеты для отображения данных о категориях.
- `prepare_all_categories_async`: Асинхронно подготавливает все категории.
- `prepare_category_async`: Асинхронно подготавливает указанную категорию.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.category import CategoryEditor

app = QtWidgets.QApplication([])
category_editor = CategoryEditor()
category_editor.show()
app.exec()
```

## Функции

### `__init__`

```python
def __init__(self, parent=None, main_app=None):
    """ Initialize the main window"""
    super().__init__(parent)
    self.main_app = main_app  # Save the MainApp instance

    self.setup_ui()
    self.setup_connections()
```

**Описание**: Инициализирует виджет редактора категорий.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.category import CategoryEditor

app = QtWidgets.QApplication([])
category_editor = CategoryEditor()
category_editor.show()
app.exec()
```

### `setup_ui`

```python
def setup_ui(self):
    """ Setup the user interface"""
    self.setWindowTitle("Category Editor")
    self.resize(1800, 800)

    # Define UI components
    self.open_button = QtWidgets.QPushButton("Open JSON File")
    self.open_button.clicked.connect(self.open_file)
    
    self.file_name_label = QtWidgets.QLabel("No file selected")
    
    self.prepare_all_button = QtWidgets.QPushButton("Prepare All Categories")
    self.prepare_all_button.clicked.connect(self.prepare_all_categories_async)

    self.prepare_specific_button = QtWidgets.QPushButton("Prepare Category")
    self.prepare_specific_button.clicked.connect(self.prepare_category_async)

    layout = QtWidgets.QVBoxLayout(self)
    layout.addWidget(self.open_button)
    layout.addWidget(self.file_name_label)
    layout.addWidget(self.prepare_all_button)
    layout.addWidget(self.prepare_specific_button)

    self.setLayout(layout)
```

**Описание**: Настраивает пользовательский интерфейс виджета.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.category import CategoryEditor

app = QtWidgets.QApplication([])
category_editor = CategoryEditor()
category_editor.setup_ui()
category_editor.show()
app.exec()
```

### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections"""
    pass
```

**Описание**: Настраивает соединения между сигналами и слотами.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.category import CategoryEditor

app = QtWidgets.QApplication([])
category_editor = CategoryEditor()
category_editor.setup_connections()
category_editor.show()
app.exec()
```

### `open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        self,
        "Open JSON File",
        "c:/user/documents/repos/hypotez/data/aliexpress/campaigns",
        "JSON files (*.json)"
    )
    if not file_path:
        return  # No file selected

    self.load_file(file_path)
```

**Описание**: Открывает диалоговое окно для выбора JSON-файла.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.category import CategoryEditor

app = QtWidgets.QApplication([])
category_editor = CategoryEditor()
category_editor.open_file()
category_editor.show()
app.exec()
```

### `load_file`

```python
def load_file(self, campaign_file):
    """ Load a JSON file """
    try:
        self.data = j_loads_ns(campaign_file)
        self.campaign_file = campaign_file
        self.file_name_label.setText(f"File: {self.campaign_file}")
        self.campaign_name = self.data.campaign_name
        path = Path(campaign_file)
        self.language = path.stem  # This will give you the file name without extension
        self.editor = AliCampaignEditor(campaign_file=campaign_file)
        self.create_widgets(self.data)
    except Exception as ex:
        QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")
```

**Описание**: Загружает JSON-файл и создает виджеты на основе данных.

**Параметры**:
- `campaign_file` (str): Путь к JSON-файлу.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.category import CategoryEditor

app = QtWidgets.QApplication([])
category_editor = CategoryEditor()
category_editor.load_file("c:/user/documents/repos/hypotez/data/aliexpress/campaigns/example.json")
category_editor.show()
app.exec()
```

### `create_widgets`

```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
    layout = self.layout()

    # Remove previous widgets except open button and file label
    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if widget not in [self.open_button, self.file_name_label, self.prepare_all_button, self.prepare_specific_button]:
            widget.deleteLater()

    title_label = QtWidgets.QLabel(f"Title: {data.title}")
    layout.addWidget(title_label)

    campaign_label = QtWidgets.QLabel(f"Campaign Name: {data.campaign_name}")
    layout.addWidget(campaign_label)

    # Correct way to handle SimpleNamespace as a dict
    for category in data.categories:
        category_label = QtWidgets.QLabel(f"Category: {category.name}")
        layout.addWidget(category_label)
```

**Описание**: Создает виджеты для отображения данных о категориях.

**Параметры**:
- `data` (SimpleNamespace): Данные о категориях.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.category import CategoryEditor
from types import SimpleNamespace

app = QtWidgets.QApplication([])
category_editor = CategoryEditor()
data = SimpleNamespace(title="Example Title", campaign_name="Example Campaign", categories=[SimpleNamespace(name="Category 1"), SimpleNamespace(name="Category 2")])
category_editor.create_widgets(data)
category_editor.show()
app.exec()
```

### `prepare_all_categories_async`

```python
@asyncSlot()
async def prepare_all_categories_async(self):
    """ Asynchronously prepare all categories """
    if self.editor:
        try:
            await self.editor.prepare_all_categories()
            QtWidgets.QMessageBox.information(self, "Success", "All categories prepared successfully.")
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to prepare all categories: {ex}")
```

**Описание**: Асинхронно подготавливает все категории.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.category import CategoryEditor
import asyncio
from qasync import QEventLoop

app = QtWidgets.QApplication([])
loop = QEventLoop(app)
asyncio.set_event_loop(loop)
category_editor = CategoryEditor()
asyncio.run(category_editor.prepare_all_categories_async())
category_editor.show()
app.exec()
```

### `prepare_category_async`

```python
@asyncSlot()
async def prepare_category_async(self):
    """ Asynchronously prepare a specific category """
    if self.editor:
        try:
            await self.editor.prepare_category(self.data.campaign_name)
            QtWidgets.QMessageBox.information(self, "Success", "Category prepared successfully.")
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to prepare category: {ex}")
```

**Описание**: Асинхронно подготавливает указанную категорию.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.category import CategoryEditor
import asyncio
from qasync import QEventLoop
from types import SimpleNamespace

app = QtWidgets.QApplication([])
loop = QEventLoop(app)
asyncio.set_event_loop(loop)
category_editor = CategoryEditor()
category_editor.data = SimpleNamespace(campaign_name="Example Campaign")
asyncio.run(category_editor.prepare_category_async())
category_editor.show()
app.exec()