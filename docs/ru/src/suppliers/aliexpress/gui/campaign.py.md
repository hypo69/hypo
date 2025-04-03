# Модуль для работы с редактором кампаний AliExpress
## Обзор

Модуль `campaign.py` предоставляет графический интерфейс (GUI) для редактирования кампаний AliExpress. Он включает в себя функциональность для загрузки данных кампании из JSON-файлов, отображения и редактирования основных параметров кампании, таких как название, описание и название продвижения, а также подготовки кампании к дальнейшему использованию.
## Подробнее

Модуль `campaign.py` предназначен для создания и управления кампаниями AliExpress через графический интерфейс. Он позволяет пользователям открывать JSON-файлы, содержащие данные кампаний, редактировать эти данные и подготавливать кампании для дальнейшей обработки.

## Классы

### `CampaignEditor`

**Описание**: Класс `CampaignEditor` представляет собой виджет (QWidget) для редактирования кампаний. Он содержит методы для настройки пользовательского интерфейса, обработки открытия и загрузки файлов, создания виджетов на основе данных кампании и асинхронной подготовки кампании.
**Принцип работы**:
Класс `CampaignEditor` использует библиотеку PyQt6 для создания графического интерфейса. Он содержит кнопки для открытия JSON-файлов и подготовки кампании, текстовые поля для отображения и редактирования данных кампании, а также QScrollArea для прокрутки контента, если он не помещается на экране.

**Аттрибуты**:
- `data` (SimpleNamespace): Пространство имен для хранения данных кампании.
- `current_campaign_file` (str): Путь к текущему открытому файлу кампании.
- `editor` (AliCampaignEditor): Экземпляр класса `AliCampaignEditor` для подготовки кампании.
- `main_app`: Ссылка на главный экземпляр приложения.
- `open_button` (QtWidgets.QPushButton): Кнопка для открытия файла.
- `file_name_label` (QtWidgets.QLabel): Отображает имя выбранного файла.
- `prepare_button` (QtWidgets.QPushButton): Кнопка для подготовки кампании.
- `scroll_area` (QtWidgets.QScrollArea): Область прокрутки для содержимого.
- `scroll_content_widget` (QtWidgets.QWidget): Виджет содержимого области прокрутки.
- `layout` (QtWidgets.QGridLayout): Сетка для размещения виджетов.
- `title_input` (QtWidgets.QLineEdit): Поле ввода для заголовка кампании.
- `description_input` (QtWidgets.QLineEdit): Поле ввода для описания кампании.
- `promotion_name_input` (QtWidgets.QLineEdit): Поле ввода для названия продвижения кампании.

**Методы**:
- `__init__(self, parent=None, main_app=None)`: Инициализирует виджет `CampaignEditor`.
- `setup_ui(self)`: Настраивает пользовательский интерфейс виджета.
- `setup_connections(self)`: Настраивает соединения сигнал-слот.
- `open_file(self)`: Открывает диалоговое окно выбора файла и загружает выбранный JSON-файл.
- `load_file(self, campaign_file)`: Загружает JSON-файл и создает виджеты на основе данных.
- `create_widgets(self, data)`: Создает виджеты для отображения и редактирования данных кампании.
- `prepare_campaign(self)`: Асинхронно подготавливает кампанию.

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

**Назначение**: Инициализирует виджет `CampaignEditor`, вызывая конструктор родительского класса, сохраняет ссылку на главное приложение, настраивает пользовательский интерфейс и устанавливает соединения между сигналами и слотами.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Как работает функция**:

1.  Вызывается конструктор родительского класса `QtWidgets.QWidget` для инициализации базовых атрибутов виджета.
2.  Сохраняется ссылка на экземпляр главного приложения `main_app` в атрибуте `self.main_app`.
3.  Вызывается метод `self.setup_ui()` для настройки пользовательского интерфейса виджета.
4.  Вызывается метод `self.setup_connections()` для установки соединений между сигналами и слотами.

```
Инициализация виджета CampaignEditor
↓
Сохранение ссылки на экземпляр главного приложения
↓
Настройка пользовательского интерфейса
↓
Установка соединений между сигналами и слотами
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

**Назначение**: Настраивает пользовательский интерфейс виджета `CampaignEditor`, устанавливая заголовок окна, изменяя размер окна, создавая область прокрутки, определяя компоненты пользовательского интерфейса, добавляя компоненты в макет и устанавливая основной макет виджета.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Как работает функция**:

1.  Устанавливается заголовок окна виджета `CampaignEditor` на "Campaign Editor".
2.  Изменяется размер окна виджета на 1800x800 пикселей.
3.  Создается область прокрутки `QScrollArea` и устанавливается ее свойство `widgetResizable` в `True`, чтобы содержимое области прокрутки могло изменять свой размер в зависимости от размера области прокрутки.
4.  Создается виджет `QWidget` для содержимого области прокрутки и устанавливается этот виджет в качестве содержимого области прокрутки.
5.  Создается макет `QGridLayout` для содержимого области прокрутки и устанавливается выравнивание макета по верхнему краю.
6.  Определяются компоненты пользовательского интерфейса:
    - Кнопка `QPushButton` с текстом "Open JSON File", которая при нажатии вызывает метод `self.open_file`.
    - Метка `QLabel` с текстом "No file selected".
    - Кнопка `QPushButton` с текстом "Prepare Campaign", которая при нажатии вызывает метод `self.prepare_campaign`.
7.  Добавляются компоненты в макет:
    - Кнопка открытия файла в ячейку (0, 0).
    - Метка имени файла в ячейку (0, 1).
    - Кнопка подготовки кампании в ячейку (1, 0), занимающую две колонки.
8.  Добавляется область прокрутки в основной макет виджета `QVBoxLayout` и устанавливается основной макет виджета.

```
Установка заголовка окна
↓
Изменение размера окна
↓
Создание области прокрутки
↓
Создание виджета для содержимого области прокрутки
↓
Создание макета для содержимого области прокрутки
↓
Определение компонентов пользовательского интерфейса
↓
Добавление компонентов в макет
↓
Добавление области прокрутки в основной макет
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

**Назначение**: Настраивает соединения сигнал-слот. В текущей реализации функция пуста и не выполняет никаких действий.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Как работает функция**:
Функция не выполняет никаких действий, так как тело функции содержит только оператор `pass`.
```
setup_connections
↓
pass
```

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

**Назначение**: Открывает диалоговое окно выбора файла, чтобы выбрать и загрузить JSON-файл.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Как работает функция**:

1.  Вызывается метод `QtWidgets.QFileDialog.getOpenFileName` для открытия диалогового окна выбора файла.
2.  Если файл не выбран (переменная `campaign_file` пуста), функция завершается.
3.  Вызывается метод `self.load_file` для загрузки выбранного файла.

```
Открытие диалогового окна выбора файла
↓
Проверка, выбран ли файл
↓
Загрузка файла
```

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

**Назначение**: Загружает JSON-файл, устанавливает данные, имя текущего файла кампании, обновляет метку имени файла, создает виджеты на основе данных и создает экземпляр `AliCampaignEditor`.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.
- `campaign_file` (str): Путь к JSON-файлу кампании.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если не удается загрузить JSON-файл.

**Как работает функция**:

1.  Пытается загрузить JSON-файл с использованием функции `j_loads_ns` и сохранить данные в атрибуте `self.data`.
2.  Устанавливает путь к текущему файлу кампании в атрибут `self.current_campaign_file`.
3.  Обновляет текст метки `self.file_name_label` с именем текущего файла кампании.
4.  Вызывает метод `self.create_widgets` для создания виджетов на основе загруженных данных.
5.  Создает экземпляр класса `AliCampaignEditor`, передавая путь к файлу кампании.
6.  Если возникает исключение, отображает критическое сообщение об ошибке с использованием `QtWidgets.QMessageBox.critical`.

```
Попытка загрузки JSON-файла
↓
Установка имени текущего файла кампании
↓
Обновление метки имени файла
↓
Создание виджетов на основе данных
↓
Создание экземпляра AliCampaignEditor
↓
Обработка исключения
```

**Примеры**:
```python
campaign_editor = CampaignEditor()
campaign_editor.load_file("campaign.json")
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

**Назначение**: Создает виджеты на основе данных, загруженных из JSON-файла.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.
- `data` (SimpleNamespace): Данные кампании, загруженные из JSON-файла.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Как работает функция**:

1.  Получает макет `layout` из атрибута `self.layout`.
2.  Удаляет предыдущие виджеты из макета, за исключением кнопок `open_button` и `prepare_button`, а также метки `file_name_label`.
3.  Создает поле ввода `QLineEdit` для заголовка кампании, устанавливает его значение из атрибута `data.title`, добавляет метку "Title:" и поле ввода в макет, а также устанавливает фиксированный размер поля ввода.
4.  Создает поле ввода `QLineEdit` для описания кампании, устанавливает его значение из атрибута `data.description`, добавляет метку "Description:" и поле ввода в макет, а также устанавливает фиксированный размер поля ввода.
5.  Создает поле ввода `QLineEdit` для названия продвижения кампании, устанавливает его значение из атрибута `data.promotion_name`, добавляет метку "Promotion Name:" и поле ввода в макет, а также устанавливает фиксированный размер поля ввода.

```
Получение макета
↓
Удаление предыдущих виджетов
↓
Создание поля ввода для заголовка кампании
↓
Создание поля ввода для описания кампании
↓
Создание поля ввода для названия продвижения кампании
```

**Примеры**:
```python
campaign_editor = CampaignEditor()
data = SimpleNamespace(title="Test Campaign", description="Test Description", promotion_name="Test Promotion")
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

**Назначение**: Асинхронно подготавливает кампанию с использованием экземпляра `AliCampaignEditor`.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если не удается подготовить кампанию.

**Как работает функция**:

1.  Проверяет, существует ли экземпляр `AliCampaignEditor` в атрибуте `self.editor`.
2.  Если экземпляр существует, вызывает асинхронный метод `prepare` экземпляра `self.editor`.
3.  Если подготовка прошла успешно, отображает информационное сообщение с использованием `QtWidgets.QMessageBox.information`.
4.  Если возникает исключение, отображает критическое сообщение об ошибке с использованием `QtWidgets.QMessageBox.critical`.

```
Проверка наличия экземпляра AliCampaignEditor
↓
Асинхронный вызов метода prepare
↓
Отображение информационного сообщения об успехе
↓
Обработка исключения
```

**Примеры**:
```python
campaign_editor = CampaignEditor()
campaign_editor.editor = AliCampaignEditor(campaign_file="campaign.json")
asyncio.run(campaign_editor.prepare_campaign())