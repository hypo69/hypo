# Модуль `product`

## Обзор

Модуль `product` предоставляет графический интерфейс (GUI) для редактирования информации о товарах, полученных с AliExpress. Он позволяет открывать JSON-файлы с данными о товарах, отображать эту информацию в удобном виде и подготавливать товары к дальнейшей обработке, например, к созданию рекламных кампаний.

## Подорбней

Этот модуль является частью проекта `hypotez` и предназначен для работы с данными о товарах с AliExpress. Он использует библиотеку PyQt6 для создания графического интерфейса, который позволяет пользователю просматривать и редактировать информацию о товаре, загруженную из JSON-файла. Основная задача модуля - предоставить удобный инструмент для работы с данными о товарах, полученных с AliExpress, и подготовки этих данных к дальнейшему использованию. Модуль позволяет открывать JSON-файлы, отображать основные детали товара, такие как заголовок и описание, и запускать процесс подготовки товара к рекламной кампании.

## Классы

### `ProductEditor`

**Описание**: Класс `ProductEditor` представляет собой виджет (QWidget) для редактирования информации о товарах.

**Методы**:
- `__init__`: Инициализирует виджет `ProductEditor`, устанавливает пользовательский интерфейс и соединения между элементами интерфейса.
- `setup_ui`: Создает и размещает элементы пользовательского интерфейса, такие как кнопки и метки.
- `setup_connections`: Устанавливает соединения между сигналами и слотами для обработки действий пользователя.
- `open_file`: Открывает диалоговое окно для выбора JSON-файла с данными о товаре.
- `load_file`: Загружает данные из выбранного JSON-файла и отображает их в виджете.
- `create_widgets`: Создает виджеты для отображения информации о товаре на основе загруженных данных.
- `prepare_product_async`: Асинхронно подготавливает товар к дальнейшей обработке.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.product import ProductEditor

app = QtWidgets.QApplication([])
editor = ProductEditor()
editor.show()
app.exec()
```

## Функции

### `__init__`

```python
def __init__(self, parent=None, main_app=None):
    """ Initialize the ProductEditor widget """
```

**Описание**: Инициализирует виджет `ProductEditor`.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.product import ProductEditor

app = QtWidgets.QApplication([])
editor = ProductEditor()
editor.show()
app.exec()
```

### `setup_ui`

```python
def setup_ui(self):
    """ Setup the user interface """
```

**Описание**: Настраивает пользовательский интерфейс виджета.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.product import ProductEditor

app = QtWidgets.QApplication([])
editor = ProductEditor()
editor.setup_ui()
editor.show()
app.exec()
```

### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections """
```

**Описание**: Устанавливает соединения между сигналами и слотами.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.product import ProductEditor

app = QtWidgets.QApplication([])
editor = ProductEditor()
editor.setup_ui()
editor.setup_connections()
editor.show()
app.exec()
```

### `open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
```

**Описание**: Открывает диалоговое окно для выбора JSON-файла.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.product import ProductEditor

app = QtWidgets.QApplication([])
editor = ProductEditor()
editor.setup_ui()
editor.setup_connections()
editor.open_button.clicked.connect(editor.open_file)  # Подключаем сигнал напрямую для примера
editor.show()
app.exec()
```

### `load_file`

```python
def load_file(self, file_path):
    """ Load a JSON file """
```

**Описание**: Загружает JSON-файл.

**Параметры**:
- `file_path` (str): Путь к JSON-файлу.

**Вызывает исключения**:
- `Exception`: Если не удается загрузить JSON-файл.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.product import ProductEditor
from pathlib import Path

app = QtWidgets.QApplication([])
editor = ProductEditor()
file_path = str(Path('./data/aliexpress/products/example.json'))  # Укажите актуальный путь к файлу
editor.setup_ui()
editor.setup_connections()
editor.load_file(file_path)
editor.show()
app.exec()
```

### `create_widgets`

```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
```

**Описание**: Создает виджеты на основе данных из JSON-файла.

**Параметры**:
- `data` (SimpleNamespace): Данные о товаре из JSON-файла.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.product import ProductEditor
from pathlib import Path
from src.utils.jjson import j_loads_ns

app = QtWidgets.QApplication([])
editor = ProductEditor()
file_path = str(Path('./data/aliexpress/products/example.json'))  # Укажите актуальный путь к файлу
editor.setup_ui()
editor.setup_connections()
data = j_loads_ns(file_path)
editor.create_widgets(data)
editor.show()
app.exec()
```

### `prepare_product_async`

```python
@asyncSlot()
async def prepare_product_async(self):
    """ Asynchronously prepare the product """
```

**Описание**: Асинхронно подготавливает продукт.

**Примеры**:
```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.product import ProductEditor
from pathlib import Path
from src.utils.jjson import j_loads_ns
import asyncio

app = QtWidgets.QApplication([])
editor = ProductEditor()
file_path = str(Path('./data/aliexpress/products/example.json'))  # Укажите актуальный путь к файлу
editor.setup_ui()
editor.setup_connections()
data = j_loads_ns(file_path)
editor.load_file(file_path)

async def run_prepare_product():
    await editor.prepare_product_async()

asyncio.run(run_prepare_product())
editor.show()
app.exec()
```