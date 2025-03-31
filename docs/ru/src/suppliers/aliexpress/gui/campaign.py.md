# Модуль: src.suppliers.aliexpress.gui.campaign

## Обзор

Модуль `campaign.py` предоставляет графический интерфейс (GUI) для редактирования и подготовки кампаний AliExpress. Он включает в себя функциональность открытия JSON-файлов, отображения данных кампании в редактируемых полях и асинхронной подготовки кампании с использованием класса `AliCampaignEditor`.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за визуальное представление и редактирование данных кампаний AliExpress. Он использует библиотеку `PyQt6` для создания графического интерфейса и асинхронные операции для подготовки кампаний. Модуль позволяет пользователям загружать JSON-файлы с данными кампаний, редактировать основные параметры, такие как заголовок, описание и название промоакции, а также запускать процесс подготовки кампании.

## Классы

### `CampaignEditor`

**Описание**: Класс `CampaignEditor` представляет собой виджет (QWidget) для редактирования кампаний. Он содержит методы для настройки пользовательского интерфейса, загрузки файлов, создания виджетов на основе данных и подготовки кампании.

**Как работает класс**:

1.  **Инициализация**: При инициализации класса `CampaignEditor` создается экземпляр виджета, сохраняется ссылка на главное приложение (`main_app`) и вызываются методы `setup_ui` и `setup_connections` для настройки интерфейса и соединений.
2.  **Настройка UI**: Метод `setup_ui` создает основные элементы интерфейса, такие как кнопки "Open JSON File" и "Prepare Campaign", текстовые поля для заголовка, описания и названия промоакции, а также область прокрутки для размещения виджетов.
3.  **Загрузка файла**: Метод `open_file` открывает диалоговое окно выбора файла, позволяя пользователю выбрать JSON-файл с данными кампании. После выбора файла вызывается метод `load_file` для загрузки данных.
4.  **Создание виджетов**: Метод `create_widgets` создает виджеты на основе загруженных данных, отображая заголовок, описание и название промоакции в соответствующих текстовых полях.
5.  **Подготовка кампании**: Метод `prepare_campaign` асинхронно подготавливает кампанию, используя экземпляр класса `AliCampaignEditor`.

**Методы**:

*   `__init__`: Инициализирует виджет `CampaignEditor`.
*   `setup_ui`: Настраивает пользовательский интерфейс.
*   `setup_connections`: Устанавливает соединения между сигналами и слотами.
*   `open_file`: Открывает диалоговое окно выбора файла.
*   `load_file`: Загружает JSON-файл с данными кампании.
*   `create_widgets`: Создает виджеты на основе данных из JSON-файла.
*   `prepare_campaign`: Асинхронно подготавливает кампанию.

**Параметры**:

*   `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
*   `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**:

```python
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.campaign import CampaignEditor

app = QtWidgets.QApplication([])
campaign_editor = CampaignEditor()
campaign_editor.show()
app.exec()
```

## Функции

### `__init__`

```python
def __init__(self, parent=None, main_app=None):
    """ Initialize the CampaignEditor widget """
    super().__init__(parent)
    self.main_app = main_app  # Save the MainApp instance

    self.setup_ui()
    self.setup_connections()
```

**Описание**: Инициализирует виджет `CampaignEditor`.

**Как работает функция**:
Вызывает конструктор родительского класса `QtWidgets.QWidget`, сохраняет ссылку на экземпляр главного приложения (`main_app`), настраивает пользовательский интерфейс (`setup_ui`) и устанавливает соединения (`setup_connections`).

**Параметры**:

*   `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
*   `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**:

```python
campaign_editor = CampaignEditor()
```

### `setup_ui`

```python
def setup_ui(self):
    """ Setup the user interface """
    self.setWindowTitle("Campaign Editor")
    self.resize(1800, 800)

    # Create a QScrollArea
    self.scroll_area = QtWidgets.QScrollArea()
    self.scroll_area.setWidgetResizable(True)

    # Create a QWidget for the content of the scroll area
    self.scroll_content_widget = QtWidgets.QWidget()
    self.scroll_area.setWidget(self.scroll_content_widget)

    # Create the layout for the scroll content widget
    self.layout = QtWidgets.QGridLayout(self.scroll_content_widget)
    self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

    # Define UI components
    self.open_button = QtWidgets.QPushButton("Open JSON File")
    self.open_button.clicked.connect(self.open_file)
    set_fixed_size(self.open_button, width=250, height=25)

    self.file_name_label = QtWidgets.QLabel("No file selected")
    set_fixed_size(self.file_name_label, width=500, height=25)

    self.prepare_button = QtWidgets.QPushButton("Prepare Campaign")
    self.prepare_button.clicked.connect(self.prepare_campaign)
    set_fixed_size(self.prepare_button, width=250, height=25)

    # Add components to layout
    self.layout.addWidget(self.open_button, 0, 0)
    self.layout.addWidget(self.file_name_label, 0, 1)
    self.layout.addWidget(self.prepare_button, 1, 0, 1, 2)  # Span across two columns

    # Add the scroll area to the main layout of the widget
    main_layout = QtWidgets.QVBoxLayout(self)
    main_layout.addWidget(self.scroll_area)
    self.setLayout(main_layout)
```

**Описание**: Настраивает пользовательский интерфейс виджета `CampaignEditor`.

**Как работает функция**:
Устанавливает заголовок окна, изменяет размер окна, создает область прокрутки, создает виджет для содержимого области прокрутки, создает макет для содержимого области прокрутки, определяет компоненты пользовательского интерфейса (кнопки, метки), добавляет компоненты в макет и добавляет область прокрутки в основной макет виджета.

**Параметры**:

*   Отсутствуют

**Примеры**:

```python
campaign_editor = CampaignEditor()
campaign_editor.setup_ui()
```

### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections """
    pass
```

**Описание**: Устанавливает соединения между сигналами и слотами.

**Как работает функция**:
В текущей реализации функция пуста и не выполняет никаких действий. Она предназначена для установки соединений между сигналами и слотами, но в данном коде эти соединения не определены.

**Параметры**:

*   Отсутствуют

**Примеры**:

```python
campaign_editor = CampaignEditor()
campaign_editor.setup_connections()
```

### `open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
    campaign_file, _ = QtWidgets.QFileDialog.getOpenFileName(
        self,
        "Open JSON File",
        "c:/user/documents/repos/hypotez/data/aliexpress/campaigns",
        "JSON files (*.json)"
    )
    if not campaign_file:
        return

    self.load_file(campaign_file)
```

**Описание**: Открывает диалоговое окно выбора файла для выбора и загрузки JSON-файла.

**Как работает функция**:
Вызывает `QtWidgets.QFileDialog.getOpenFileName` для отображения диалогового окна выбора файла. Если файл выбран, вызывает метод `load_file` для загрузки выбранного файла.

**Параметры**:

*   Отсутствуют

**Примеры**:

```python
campaign_editor = CampaignEditor()
campaign_editor.open_file()
```

### `load_file`

```python
def load_file(self, campaign_file):
    """ Load a JSON file """
    try:
        self.data = j_loads_ns(campaign_file)
        self.current_campaign_file = campaign_file
        self.file_name_label.setText(f"File: {self.current_campaign_file}")
        self.create_widgets(self.data)
        self.editor = AliCampaignEditor(campaign_file=campaign_file)
    except Exception as ex:
        QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")
```

**Описание**: Загружает JSON-файл.

**Как работает функция**:
Пытается загрузить JSON-файл, используя `j_loads_ns`. В случае успеха сохраняет данные, устанавливает текст метки имени файла и создает виджеты на основе загруженных данных. В случае неудачи отображает сообщение об ошибке.

**Параметры**:

*   `campaign_file` (str): Путь к JSON-файлу.

**Вызывает исключения**:

*   `Exception`: Если не удается загрузить JSON-файл.

**Примеры**:

```python
campaign_editor = CampaignEditor()
campaign_editor.load_file("path/to/campaign.json")
```

### `create_widgets`

```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
    layout = self.layout

    # Remove previous widgets except open button and file label
    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if widget not in [self.open_button, self.file_name_label, self.prepare_button]:
            widget.deleteLater()

    self.title_input = QtWidgets.QLineEdit(data.title)
    layout.addWidget(QtWidgets.QLabel("Title:"), 2, 0)
    layout.addWidget(self.title_input, 2, 1)
    set_fixed_size(self.title_input, width=500, height=25)

    self.description_input = QtWidgets.QLineEdit(data.description)
    layout.addWidget(QtWidgets.QLabel("Description:"), 3, 0)
    layout.addWidget(self.description_input, 3, 1)
    set_fixed_size(self.description_input, width=500, height=25)

    self.promotion_name_input = QtWidgets.QLineEdit(data.promotion_name)
    layout.addWidget(QtWidgets.QLabel("Promotion Name:"), 4, 0)
    layout.addWidget(self.promotion_name_input, 4, 1)
    set_fixed_size(self.promotion_name_input, width=500, height=25)
```

**Описание**: Создает виджеты на основе данных, загруженных из JSON-файла.

**Как работает функция**:
Удаляет предыдущие виджеты (за исключением кнопок "Open JSON File", "Prepare Campaign" и метки имени файла), создает текстовые поля для заголовка, описания и названия промоакции, добавляет метки и текстовые поля в макет.

**Параметры**:

*   `data` (SimpleNamespace): Данные, загруженные из JSON-файла.

**Примеры**:

```python
from types import SimpleNamespace
campaign_editor = CampaignEditor()
data = SimpleNamespace(title="Example Campaign", description="Example Description", promotion_name="Example Promotion")
campaign_editor.create_widgets(data)
```

### `prepare_campaign`

```python
@asyncSlot()
async def prepare_campaign(self):
    """ Asynchronously prepare the campaign """
    if self.editor:
        try:
            await self.editor.prepare()
            QtWidgets.QMessageBox.information(self, "Success", "Campaign prepared successfully.")
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to prepare campaign: {ex}")
```

**Описание**: Асинхронно подготавливает кампанию.

**Как работает функция**:
Если `self.editor` существует, пытается асинхронно подготовить кампанию, используя `self.editor.prepare()`. В случае успеха отображает сообщение об успехе, в случае неудачи отображает сообщение об ошибке.

**Параметры**:

*   Отсутствуют

**Вызывает исключения**:

*   `Exception`: Если не удается подготовить кампанию.

**Примеры**:

```python
import asyncio
campaign_editor = CampaignEditor()
asyncio.run(campaign_editor.prepare_campaign())