# Модуль для редактирования кампаний AliExpress

## Обзор

Модуль `campaign.py` предоставляет графический интерфейс для редактирования кампаний AliExpress. Он позволяет загружать JSON-файлы с данными о кампаниях, отображать их в виде редактируемых виджетов и подготавливать кампании к дальнейшей обработке.

## Подробней

Этот модуль является частью GUI приложения для работы с AliExpress. Он предоставляет возможность визуального редактирования параметров кампаний, хранящихся в формате JSON. Класс `CampaignEditor` содержит основную логику для загрузки, отображения и подготовки кампаний. Он использует библиотеку `PyQt6` для создания графического интерфейса.

## Классы

### `CampaignEditor`

**Описание**: Класс `CampaignEditor` представляет собой виджет для редактирования кампаний. Он позволяет загружать JSON-файлы с данными о кампаниях, отображать их в виде редактируемых полей и подготавливать кампании к дальнейшей обработке.

**Наследует**: `QtWidgets.QWidget`

**Атрибуты**:

- `data` (SimpleNamespace): Данные кампании, загруженные из JSON-файла.
- `current_campaign_file` (str): Путь к текущему загруженному файлу кампании.
- `editor` (AliCampaignEditor): Экземпляр редактора кампаний `AliCampaignEditor` из модуля `src.suppliers.aliexpress.campaign`.
- `main_app`: Ссылка на экземпляр главного приложения.
- `scroll_area`: Область с возможностью прокрутки для размещения контента.
- `scroll_content_widget`: Виджет для размещения контента внутри области прокрутки.
- `layout`: Макет для размещения виджетов внутри виджета контента области прокрутки.
- `open_button`: Кнопка для открытия JSON файла.
- `file_name_label`: Лейбл для отображения имени выбранного файла.
- `prepare_button`: Кнопка для подготовки кампании.
- `title_input`: Поле ввода для заголовка кампании.
- `description_input`: Поле ввода для описания кампании.
- `promotion_name_input`: Поле ввода для названия промоакции кампании.

**Методы**:

- `__init__(parent=None, main_app=None)`: Инициализирует виджет `CampaignEditor`.
- `setup_ui()`: Настраивает пользовательский интерфейс.
- `setup_connections()`: Устанавливает связи между сигналами и слотами.
- `open_file()`: Открывает диалоговое окно для выбора и загрузки JSON-файла.
- `load_file(campaign_file: str)`: Загружает JSON-файл.
- `create_widgets(data)`: Создает виджеты на основе данных, загруженных из JSON-файла.
- `prepare_campaign()`: Асинхронно подготавливает кампанию.

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

**Назначение**: Инициализирует виджет `CampaignEditor`, устанавливает родительский виджет, сохраняет ссылку на главное приложение, настраивает пользовательский интерфейс и устанавливает связи между сигналами и слотами.

**Параметры**:

- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Возвращает**: `None`

**Как работает функция**:

1. Вызывает конструктор базового класса `QtWidgets.QWidget` для инициализации виджета.
2. Сохраняет ссылку на экземпляр главного приложения `main_app` в атрибуте `self.main_app`.
3. Вызывает метод `self.setup_ui()` для настройки пользовательского интерфейса.
4. Вызывает метод `self.setup_connections()` для установки связей между сигналами и слотами.

```
Инициализация виджета
│
├── Вызов конструктора базового класса (QtWidgets.QWidget)
│
├── Сохранение ссылки на экземпляр главного приложения
│
├── Настройка пользовательского интерфейса (setup_ui)
│
└── Установка связей между сигналами и слотами (setup_connections)
```

**Примеры**:

```python
campaign_editor = CampaignEditor(main_app=main_app_instance)
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

**Назначение**: Настраивает пользовательский интерфейс виджета `CampaignEditor`.

**Параметры**: `None`

**Возвращает**: `None`

**Как работает функция**:

1. Устанавливает заголовок окна виджета как "Campaign Editor".
2. Устанавливает размер окна виджета как 1800x800 пикселей.
3. Создает область прокрутки `QScrollArea` и устанавливает для нее возможность изменения размера виджета.
4. Создает виджет `QWidget` для содержимого области прокрутки и устанавливает его в качестве виджета для `QScrollArea`.
5. Создает макет `QGridLayout` для виджета содержимого области прокрутки и устанавливает выравнивание по верхнему краю.
6. Определяет компоненты пользовательского интерфейса:
   - Кнопку "Open JSON File" (`QPushButton`) с подключением к функции `self.open_file` по клику.
   - Лейбл (`QLabel`) для отображения имени файла с текстом "No file selected".
   - Кнопку "Prepare Campaign" (`QPushButton`) с подключением к функции `self.prepare_campaign` по клику.
7. Добавляет компоненты в макет:
   - Кнопку "Open JSON File" в ячейку (0, 0).
   - Лейбл имени файла в ячейку (0, 1).
   - Кнопку "Prepare Campaign" в ячейку (1, 0), занимающую две колонки.
8. Создает основной макет `QVBoxLayout` для виджета.
9. Добавляет область прокрутки в основной макет.
10. Устанавливает основной макет для виджета.

```
Настройка пользовательского интерфейса
│
├── Установка заголовка окна
│
├── Установка размера окна
│
├── Создание области прокрутки (QScrollArea)
│
├── Создание виджета содержимого области прокрутки (QWidget)
│
├── Создание макета (QGridLayout) для виджета содержимого
│
├── Определение компонентов пользовательского интерфейса (кнопки, лейблы)
│
├── Добавление компонентов в макет
│
├── Создание основного макета (QVBoxLayout)
│
├── Добавление области прокрутки в основной макет
│
└── Установка основного макета для виджета
```

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

**Назначение**: Устанавливает связи между сигналами и слотами. В текущей реализации функция пуста.

**Параметры**: `None`

**Возвращает**: `None`

**Как работает функция**:

Функция не выполняет никаких действий, так как содержит только `pass`.

```
Установка связей между сигналами и слотами
│
└── (Нет действий)
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

**Назначение**: Открывает диалоговое окно для выбора JSON-файла и загружает его.

**Параметры**: `None`

**Возвращает**: `None`

**Как работает функция**:

1. Открывает диалоговое окно выбора файла с помощью `QtWidgets.QFileDialog.getOpenFileName`.
   - Указывает заголовок диалогового окна "Open JSON File".
   - Указывает начальный каталог для диалогового окна: "c:/user/documents/repos/hypotez/data/aliexpress/campaigns".
   - Указывает фильтр файлов "JSON files (*.json)".
2. Проверяет, был ли выбран файл. Если файл не выбран (`campaign_file` пуст), функция завершается.
3. Вызывает метод `self.load_file(campaign_file)` для загрузки выбранного файла.

```
Открытие диалогового окна выбора файла
│
├── Открытие диалогового окна (QtWidgets.QFileDialog.getOpenFileName)
│
├── Проверка, был ли выбран файл
│   └── Если файл не выбран, завершение функции
│
└── Загрузка выбранного файла (self.load_file)
```

**Примеры**:

```python
campaign_editor = CampaignEditor()
campaign_editor.open_file()
```

### `load_file`

```python
def load_file(self, campaign_file: str):
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

**Назначение**: Загружает JSON-файл, отображает его имя в `file_name_label`, создает виджеты для отображения данных и инициализирует редактор кампании `AliCampaignEditor`.

**Параметры**:

- `campaign_file` (str): Путь к JSON-файлу.

**Возвращает**: `None`

**Как работает функция**:

1. Пытается выполнить следующие действия:
   - Загружает данные из JSON-файла с помощью `j_loads_ns(campaign_file)` и сохраняет их в атрибуте `self.data`.
   - Сохраняет путь к файлу в атрибуте `self.current_campaign_file`.
   - Устанавливает текст лейбла `self.file_name_label` равным "File: {путь к файлу}".
   - Вызывает метод `self.create_widgets(self.data)` для создания виджетов на основе загруженных данных.
   - Создает экземпляр `AliCampaignEditor` с указанием пути к файлу кампании.
2. Если происходит исключение, отображает критическое сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical`.

```
Загрузка JSON-файла
│
├── Попытка выполнить следующие действия:
│   ├── Загрузка данных из JSON-файла (j_loads_ns)
│   ├── Сохранение пути к файлу
│   ├── Отображение имени файла в лейбле
│   ├── Создание виджетов на основе данных (create_widgets)
│   └── Создание экземпляра AliCampaignEditor
│
└── Если происходит исключение:
    └── Отображение сообщения об ошибке
```

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

**Назначение**: Создает виджеты для отображения и редактирования данных кампании, загруженных из JSON-файла.

**Параметры**:

- `data` (SimpleNamespace): Данные кампании, загруженные из JSON-файла.

**Возвращает**: `None`

**Как работает функция**:

1. Получает макет `self.layout`.
2. Удаляет предыдущие виджеты из макета, за исключением кнопок `open_button`, `prepare_button` и лейбла `file_name_label`.
   - Итерируется по всем виджетам в макете в обратном порядке.
   - Проверяет, не является ли виджет одной из кнопок или лейблом.
   - Если виджет не является исключением, он удаляется с помощью `widget.deleteLater()`.
3. Создает виджет `QLineEdit` для заголовка кампании (`data.title`), добавляет лейбл "Title:" и виджет в макет.
4. Создает виджет `QLineEdit` для описания кампании (`data.description`), добавляет лейбл "Description:" и виджет в макет.
5. Создает виджет `QLineEdit` для названия промоакции (`data.promotion_name`), добавляет лейбл "Promotion Name:" и виджет в макет.
6. Устанавливает фиксированный размер для каждого из виджетов `QLineEdit`.

```
Создание виджетов на основе данных
│
├── Получение макета
│
├── Удаление предыдущих виджетов (кроме кнопок и лейбла)
│
├── Создание виджета для заголовка кампании (QLineEdit)
│
├── Создание виджета для описания кампании (QLineEdit)
│
└── Создание виджета для названия промоакции (QLineEdit)
```

**Примеры**:

```python
campaign_editor = CampaignEditor()
campaign_editor.load_file("path/to/campaign.json")
# После загрузки файла вызывается create_widgets для отображения данных
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

**Назначение**: Асинхронно подготавливает кампанию с использованием экземпляра `AliCampaignEditor`.

**Параметры**: `None`

**Возвращает**: `None`

**Как работает функция**:

1. Проверяет, инициализирован ли атрибут `self.editor` (является ли он экземпляром `AliCampaignEditor`).
2. Если `self.editor` инициализирован, пытается выполнить следующие действия:
   - Вызывает асинхронный метод `self.editor.prepare()` для подготовки кампании.
   - Отображает информационное сообщение об успешной подготовке кампании с помощью `QtWidgets.QMessageBox.information`.
3. Если происходит исключение, отображает критическое сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical`.

```
Асинхронная подготовка кампании
│
├── Проверка, инициализирован ли self.editor
│   └── Если self.editor инициализирован:
│       ├── Попытка выполнить следующие действия:
│       │   ├── Вызов асинхронного метода self.editor.prepare()
│       │   └── Отображение информационного сообщения об успехе
│       └── Если происходит исключение:
│           └── Отображение сообщения об ошибке
```

**Примеры**:

```python
campaign_editor = CampaignEditor()
campaign_editor.load_file("path/to/campaign.json")
# После загрузки файла и инициализации self.editor можно вызвать prepare_campaign
asyncio.run(campaign_editor.prepare_campaign())