# Модуль `category.py`

## Обзор

Модуль `category.py` предоставляет графический интерфейс для редактирования категорий, используемых в рекламных кампаниях AliExpress. Он позволяет загружать данные о кампаниях из JSON-файлов, отображать информацию о категориях и подготавливать категории к использованию в кампаниях.

## Подробней

Этот модуль является частью GUI (`Graphical User Interface`) для работы с рекламными кампаниями AliExpress. Он предоставляет инструменты для открытия и загрузки JSON-файлов, содержащих данные о категориях кампаний, отображает основные параметры кампании и позволяет запускать процессы подготовки всех или конкретных категорий. Класс `CategoryEditor` является основным элементом интерфейса, обеспечивающим взаимодействие пользователя с функциональностью подготовки категорий.
Взаимосвязь с другими файлами проекта:
- `src.suppliers.aliexpress.campaign.AliCampaignEditor`: Используется для подготовки категорий.
- `src.utils.jjson`: Используется для загрузки JSON-файлов.
- `PyQt6`: Используется для создания графического интерфейса.

## Классы

### `CategoryEditor`

**Описание**: Класс `CategoryEditor` представляет собой виджет (`QWidget`) для редактирования категорий.

**Как работает класс**:
Класс `CategoryEditor` предоставляет пользовательский интерфейс для загрузки, отображения и подготовки категорий для рекламных кампаний AliExpress. Он включает в себя кнопки для открытия JSON-файлов, отображения имени выбранного файла, а также кнопки для подготовки всех или конкретных категорий. Данные о категориях загружаются из JSON-файла с использованием `j_loads_ns`, и интерфейс динамически обновляется для отображения этих данных.

**Методы**:
- `__init__`: Инициализирует окно редактирования категорий.
- `setup_ui`: Настраивает пользовательский интерфейс.
- `setup_connections`: Настраивает соединения сигнал-слот.
- `open_file`: Открывает диалоговое окно выбора файла для загрузки JSON-файла.
- `load_file`: Загружает JSON-файл и отображает данные.
- `create_widgets`: Создает виджеты на основе загруженных данных.
- `prepare_all_categories_async`: Асинхронно подготавливает все категории.
- `prepare_category_async`: Асинхронно подготавливает конкретную категорию.

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

## Функции

### `__init__`

```python
def __init__(self, parent=None, main_app=None):
    """ Initialize the main window"""
```

**Описание**: Инициализирует окно редактирования категорий.

**Как работает функция**:
Функция инициализации создает экземпляр класса `CategoryEditor`, сохраняет ссылку на экземпляр главного приложения, настраивает пользовательский интерфейс и устанавливает соединения между сигналами и слотами.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**:
```python
category_editor = CategoryEditor()
```

### `setup_ui`

```python
def setup_ui(self):
    """ Setup the user interface"""
```

**Описание**: Настраивает пользовательский интерфейс.

**Как работает функция**:
Создает и настраивает основные элементы пользовательского интерфейса, такие как кнопки "Open JSON File", "Prepare All Categories", "Prepare Category" и метку для отображения имени файла. Размещает эти элементы в вертикальном макете (`QVBoxLayout`).

**Примеры**:
```python
category_editor.setup_ui()
```

### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections"""
```

**Описание**: Настраивает соединения сигнал-слот.

**Как работает функция**:
В текущей реализации функция пуста и не выполняет никаких действий. Предполагается, что в будущем здесь будут устанавливаться соединения между сигналами, генерируемыми элементами интерфейса, и слотами, обрабатывающими эти сигналы.

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

**Как работает функция**:
Открывает диалоговое окно с помощью `QtWidgets.QFileDialog.getOpenFileName`, позволяя пользователю выбрать JSON-файл. Если файл выбран, вызывает метод `load_file` для загрузки данных из файла.

**Примеры**:
```python
category_editor.open_file()
```

### `load_file`

```python
def load_file(self, campaign_file):
    """ Load a JSON file """
```

**Описание**: Загружает JSON-файл.

**Как работает функция**:
Загружает JSON-файл, используя `j_loads_ns`, и сохраняет данные в атрибуте `data`. Обновляет метку `file_name_label` с именем загруженного файла, извлекает имя кампании и язык из имени файла, а также создает экземпляр `AliCampaignEditor` для подготовки категорий. В случае ошибки отображает сообщение об ошибке.

**Параметры**:
- `campaign_file` (str): Путь к JSON-файлу.

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

**Как работает функция**:
Удаляет все предыдущие виджеты (кроме кнопок "Open JSON File", "Prepare All Categories", "Prepare Category" и метки имени файла) из макета. Создает метки для отображения заголовка и имени кампании, а также метки для каждой категории. Добавляет новые виджеты в макет.

**Параметры**:
- `data` (SimpleNamespace): Данные, загруженные из JSON-файла.

**Примеры**:
```python
data = j_loads_ns('path/to/campaign.json')
category_editor.create_widgets(data)
```

### `prepare_all_categories_async`

```python
@asyncSlot()
async def prepare_all_categories_async(self):
    """ Asynchronously prepare all categories """
```

**Описание**: Асинхронно подготавливает все категории.

**Как работает функция**:
Асинхронно вызывает метод `prepare_all_categories` экземпляра `AliCampaignEditor` для подготовки всех категорий. Отображает сообщение об успехе или ошибке в зависимости от результата.

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

**Описание**: Асинхронно подготавливает конкретную категорию.

**Как работает функция**:
Асинхронно вызывает метод `prepare_category` экземпляра `AliCampaignEditor` для подготовки конкретной категории. Отображает сообщение об успехе или ошибке в зависимости от результата.

**Примеры**:
```python
await category_editor.prepare_category_async()