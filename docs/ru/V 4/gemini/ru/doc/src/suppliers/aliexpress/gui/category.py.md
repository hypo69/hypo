# Модуль: `category.py`

## Обзор

Модуль `category.py` предоставляет графический интерфейс (GUI) для подготовки рекламных кампаний AliExpress. Он включает в себя функциональность для загрузки данных кампании из JSON-файлов, отображения информации о категориях и подготовки категорий асинхронно.

## Подробнее

Этот модуль предназначен для создания и управления рекламными кампаниями AliExpress через графический интерфейс. Он позволяет пользователям загружать данные кампании из JSON-файлов, просматривать информацию о категориях и запускать процессы подготовки категорий. Модуль использует библиотеку PyQt6 для создания интерфейса и `qasync` для асинхронного выполнения задач. Располагается в подкаталоге `gui`.

## Классы

### `CategoryEditor`

**Описание**:
Класс `CategoryEditor` является основным виджетом, который предоставляет интерфейс для редактирования категорий.

**Методы**:
- `__init__`: Инициализирует окно редактирования категорий.
- `setup_ui`: Настраивает пользовательский интерфейс.
- `setup_connections`: Устанавливает соединения между сигналами и слотами.
- `open_file`: Открывает диалоговое окно выбора файла для загрузки JSON-файла.
- `load_file`: Загружает JSON-файл и создает виджеты на основе загруженных данных.
- `create_widgets`: Создает виджеты на основе данных, загруженных из JSON-файла.
- `prepare_all_categories_async`: Асинхронно подготавливает все категории.
- `prepare_category_async`: Асинхронно подготавливает определенную категорию.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**:
```python
# Пример создания и использования CategoryEditor
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
```

**Описание**: Инициализирует главный виджет `CategoryEditor`.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
category_editor = CategoryEditor(main_app=main_app)
```

### `setup_ui`

```python
def setup_ui(self):
    """ Setup the user interface"""
```

**Описание**: Настраивает пользовательский интерфейс, включая создание кнопок и меток.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
category_editor.setup_ui()
```

### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections"""
```

**Описание**: Устанавливает соединения между сигналами и слотами.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
category_editor.setup_connections()
```

### `open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
```

**Описание**: Открывает диалоговое окно выбора файла для загрузки JSON-файла.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
category_editor.open_file()
```

### `load_file`

```python
def load_file(self, campaign_file):
    """ Load a JSON file """
```

**Описание**: Загружает JSON-файл и создает виджеты на основе загруженных данных.

**Параметры**:
- `campaign_file` (str): Путь к JSON-файлу.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если не удается загрузить JSON-файл.

**Примеры**:
```python
category_editor.load_file('path/to/campaign.json')
```

### `create_widgets`

```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
```

**Описание**: Создает виджеты на основе данных, загруженных из JSON-файла.

**Параметры**:
- `data` (SimpleNamespace): Данные, загруженные из JSON-файла.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
category_editor.create_widgets(data)
```

### `prepare_all_categories_async`

```python
@asyncSlot()
async def prepare_all_categories_async(self):
    """ Asynchronously prepare all categories """
```

**Описание**: Асинхронно подготавливает все категории.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если не удается подготовить все категории.

**Примеры**:
```python
await category_editor.prepare_all_categories_async()
```

### `prepare_category_async`

```python
@asyncSlot()
async def prepare_category_async(self):
    """ Asynchronously prepare a specific category """
```

**Описание**: Асинхронно подготавливает определенную категорию.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если не удается подготовить категорию.

**Примеры**:
```python
await category_editor.prepare_category_async()