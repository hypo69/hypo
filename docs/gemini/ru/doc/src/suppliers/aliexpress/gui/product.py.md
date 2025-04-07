# Модуль для работы с редактором продуктов AliExpress (GUI)

## Обзор

Модуль `product.py` предоставляет графический интерфейс (GUI) для редактирования информации о продуктах, полученных с AliExpress. Он позволяет открывать JSON-файлы с данными о продуктах, отображать основную информацию о продукте и подготавливать продукт с использованием функциональности, предоставляемой классом `AliCampaignEditor`.

## Подробней

Этот модуль является частью GUI-интерфейса для работы с данными AliExpress в проекте `hypotez`. Он обеспечивает визуальное представление и редактирование данных о продуктах, полученных из JSON-файлов, и использует `AliCampaignEditor` для подготовки продукта к дальнейшему использованию.

## Классы

### `ProductEditor`

**Описание**:
Класс `ProductEditor` представляет собой виджет (QWidget) для редактирования информации о продуктах. Он позволяет пользователю открывать JSON-файлы с данными о продуктах, отображать основную информацию о продукте и подготавливать продукт с использованием `AliCampaignEditor`.

**Наследует**:
- `QtWidgets.QWidget`: Класс `ProductEditor` наследует функциональность стандартного виджета PyQt6.

**Атрибуты**:
- `data` (SimpleNamespace): Данные о продукте, загруженные из JSON-файла.
- `language` (str): Язык, используемый в редакторе (по умолчанию 'EN').
- `currency` (str): Валюта, используемая в редакторе (по умолчанию 'USD').
- `file_path` (str): Путь к открытому JSON-файлу с данными о продукте.
- `editor` (AliCampaignEditor): Экземпляр класса `AliCampaignEditor`, используемый для подготовки продукта.
- `main_app`: Ссылка на основной экземпляр приложения.

**Методы**:

- `__init__(self, parent=None, main_app=None)`:
    - Инициализирует виджет `ProductEditor`, устанавливает пользовательский интерфейс, настраивает связи между сигналами и слотами.
- `setup_ui(self)`:
    - Создает и настраивает элементы пользовательского интерфейса, такие как кнопки и метки.
- `setup_connections(self)`:
    - Настраивает связи между сигналами и слотами для обработки событий пользовательского интерфейса.
- `open_file(self)`:
    - Открывает диалоговое окно выбора файла, позволяющее пользователю выбрать JSON-файл с данными о продукте.
- `load_file(self, file_path)`:
    - Загружает данные из JSON-файла, создает экземпляр `AliCampaignEditor` и отображает информацию о продукте в виджете.
- `create_widgets(self, data)`:
    - Создает виджеты для отображения информации о продукте на основе загруженных данных.
- `prepare_product_async(self)`:
    - Асинхронно подготавливает продукт с использованием `AliCampaignEditor`.

## Функции

### `__init__`

```python
def __init__(self, parent=None, main_app=None):
    """ Initialize the ProductEditor widget """
```

**Назначение**:
Инициализирует виджет `ProductEditor`.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app`: Ссылка на основной экземпляр приложения. По умолчанию `None`.

**Как работает функция**:
1. Вызывает конструктор базового класса `QtWidgets.QWidget`.
2. Сохраняет ссылку на основной экземпляр приложения.
3. Вызывает методы `setup_ui()` и `setup_connections()` для настройки пользовательского интерфейса и связей между сигналами и слотами.

**Примеры**:

```python
from PyQt6 import QtWidgets
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

**Назначение**:
Настраивает пользовательский интерфейс виджета `ProductEditor`.

**Как работает функция**:
1. Устанавливает заголовок окна виджета.
2. Устанавливает размеры окна виджета.
3. Создает кнопку "Open JSON File" и связывает ее с методом `open_file()`.
4. Создает метку для отображения имени выбранного файла.
5. Создает кнопку "Prepare Product" и связывает ее с методом `prepare_product_async()`.
6. Создает вертикальный макет и добавляет в него созданные элементы интерфейса.
7. Устанавливает макет для виджета.

**Примеры**:

```python
from PyQt6 import QtWidgets
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

**Назначение**:
Настраивает связи между сигналами и слотами виджета `ProductEditor`.

**Как работает функция**:
1. В текущей реализации функция ничего не делает (`pass`), но может быть расширена для добавления связей между сигналами и слотами в будущем.

**Примеры**:
```python
from PyQt6 import QtWidgets
app = QtWidgets.QApplication([])
editor = ProductEditor()
editor.setup_connections()
editor.show()
app.exec()
```

### `open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
```

**Назначение**:
Открывает диалоговое окно выбора файла для выбора JSON-файла с данными о продукте.

**Как работает функция**:
1. Открывает диалоговое окно выбора файла с помощью `QtWidgets.QFileDialog.getOpenFileName()`.
2. Если файл не выбран, функция завершается.
3. Вызывает метод `load_file()` для загрузки выбранного файла.

**Примеры**:

```python
from PyQt6 import QtWidgets
app = QtWidgets.QApplication([])
editor = ProductEditor()
editor.open_file()
editor.show()
app.exec()
```

### `load_file`

```python
def load_file(self, file_path):
    """ Load a JSON file """
```

**Назначение**:
Загружает данные из JSON-файла.

**Параметры**:
- `file_path` (str): Путь к JSON-файлу.

**Как работает функция**:
1. Пытается загрузить данные из JSON-файла с использованием `j_loads_ns()`.
2. Сохраняет путь к файлу в атрибуте `file_path`.
3. Устанавливает текст метки `file_name_label` с именем выбранного файла.
4. Создает экземпляр класса `AliCampaignEditor`, передавая путь к файлу.
5. Вызывает метод `create_widgets()` для создания виджетов на основе загруженных данных.
6. В случае ошибки отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

**Примеры**:

```python
from PyQt6 import QtWidgets
app = QtWidgets.QApplication([])
editor = ProductEditor()
editor.load_file('path/to/your/file.json')
editor.show()
app.exec()
```

### `create_widgets`

```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
```

**Назначение**:
Создает виджеты для отображения информации о продукте на основе загруженных данных.

**Параметры**:
- `data` (SimpleNamespace): Данные о продукте.

**Как работает функция**:
1. Получает макет виджета.
2. Удаляет все предыдущие виджеты, кроме кнопок "Open JSON File", "Prepare Product" и метки имени файла.
3. Создает метку для отображения заголовка продукта.
4. Создает метку для отображения деталей продукта.
5. Добавляет созданные метки в макет.

**Примеры**:

```python
from PyQt6 import QtWidgets
from types import SimpleNamespace

app = QtWidgets.QApplication([])
editor = ProductEditor()
data = SimpleNamespace(title='Test Title', details='Test Details')
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

**Назначение**:
Асинхронно подготавливает продукт с использованием `AliCampaignEditor`.

**Как работает функция**:
1. Проверяет, создан ли экземпляр `AliCampaignEditor`.
2. Пытается вызвать метод `prepare_product()` экземпляра `AliCampaignEditor`.
3. В случае успеха отображает сообщение об успехе с помощью `QtWidgets.QMessageBox.information()`.
4. В случае ошибки отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

**Примеры**:

```python
from PyQt6 import QtWidgets
app = QtWidgets.QApplication([])
editor = ProductEditor()
# Assuming editor.editor is an instance of AliCampaignEditor
# and editor.editor.prepare_product() is a coroutine function
# await editor.prepare_product_async() # This should be called within an event loop
editor.show()
app.exec()