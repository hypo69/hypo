# Модуль `category.py`

## Обзор

Модуль предоставляет графический интерфейс для подготовки рекламных кампаний AliExpress. Он включает в себя функциональность для открытия и загрузки JSON файлов с данными кампаний, отображения информации о категориях и подготовки категорий асинхронно.

## Подробнее

Модуль `category.py` предоставляет класс `CategoryEditor`, который является виджетом `QtWidgets.QWidget` и предназначен для редактирования категорий в рекламных кампаниях AliExpress. Он позволяет загружать JSON файлы с данными о кампаниях, отображать информацию о категориях и запускать процессы подготовки категорий в асинхронном режиме. Этот модуль является частью графического интерфейса приложения и обеспечивает взаимодействие пользователя с функциональностью редактирования кампаний.

## Классы

### `CategoryEditor`

**Описание**:
Класс `CategoryEditor` представляет собой виджет для редактирования категорий рекламных кампаний AliExpress. Он позволяет загружать JSON файлы с данными о кампаниях, отображать информацию о категориях и запускать процессы подготовки категорий в асинхронном режиме.

**Принцип работы**:
Класс `CategoryEditor` инициализируется с родительским виджетом и экземпляром главного приложения. Он настраивает пользовательский интерфейс, включая кнопки для открытия файлов, подготовки категорий и отображения информации. При загрузке JSON файла данные кампании извлекаются и отображаются в виде виджетов. Пользователь может запустить подготовку всех категорий или конкретной категории, используя асинхронные методы.

**Методы**:
- `__init__(self, parent=None, main_app=None)`: Инициализирует экземпляр класса `CategoryEditor`.
- `setup_ui(self)`: Настраивает пользовательский интерфейс виджета.
- `setup_connections(self)`: Устанавливает соединения между сигналами и слотами.
- `open_file(self)`: Открывает диалоговое окно для выбора JSON файла кампании.
- `load_file(self, campaign_file)`: Загружает данные кампании из JSON файла.
- `create_widgets(self, data)`: Создает виджеты на основе загруженных данных кампании.
- `prepare_all_categories_async(self)`: Асинхронно подготавливает все категории кампании.
- `prepare_category_async(self)`: Асинхронно подготавливает указанную категорию кампании.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `data` (SimpleNamespace): Данные кампании, загруженные из JSON файла.
- `language` (str): Язык кампании (по умолчанию 'EN').
- `currency` (str): Валюта кампании (по умолчанию 'USD').
- `file_path` (str): Путь к файлу кампании.
- `editor` (AliCampaignEditor): Редактор кампании.
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**:
```python
# Пример создания экземпляра CategoryEditor
category_editor = CategoryEditor(main_app=main_app_instance)
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

**Назначение**:
Инициализирует класс `CategoryEditor`, устанавливает родительский элемент, сохраняет экземпляр главного приложения, настраивает пользовательский интерфейс и устанавливает соединения.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Как работает функция**:
1.  Вызывает конструктор родительского класса `QtWidgets.QWidget` для инициализации базового виджета.
2.  Сохраняет ссылку на экземпляр главного приложения `main_app` для дальнейшего использования.
3.  Вызывает метод `setup_ui()` для настройки пользовательского интерфейса.
4.  Вызывает метод `setup_connections()` для установки соединений между сигналами и слотами.

**Примеры**:
```python
category_editor = CategoryEditor(main_app=main_app_instance)
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

**Назначение**:
Настраивает пользовательский интерфейс виджета `CategoryEditor`, включая установку заголовка окна, изменение размера окна, определение компонентов пользовательского интерфейса и добавление их в макет.

**Как работает функция**:
1.  Устанавливает заголовок окна виджета как "Category Editor".
2.  Устанавливает размер окна виджета как 1800x800 пикселей.
3.  Определяет компоненты пользовательского интерфейса, такие как кнопки ("Open JSON File", "Prepare All Categories", "Prepare Category") и метку для отображения имени файла.
4.  Устанавливает соединение сигнала `clicked` кнопки "Open JSON File" со слотом `open_file()`.
5.  Устанавливает соединение сигнала `clicked` кнопки "Prepare All Categories" со слотом `prepare_all_categories_async()`.
6.  Устанавливает соединение сигнала `clicked` кнопки "Prepare Category" со слотом `prepare_category_async()`.
7.  Создает вертикальный макет `QVBoxLayout` и добавляет в него компоненты пользовательского интерфейса.
8.  Устанавливает созданный макет в качестве макета для виджета.

**Примеры**:
```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.setup_ui()
```

### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections"""
    pass
```

**Назначение**:
Устанавливает соединения между сигналами и слотами.

**Как работает функция**:
1.  В текущей реализации функция ничего не делает (`pass`). Предполагается, что в будущем здесь будут установлены соединения между сигналами и слотами, если это потребуется.

**Примеры**:
```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.setup_connections()
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

**Назначение**:
Открывает диалоговое окно для выбора JSON файла кампании.

**Как работает функция**:
1.  Открывает диалоговое окно выбора файла с помощью `QtWidgets.QFileDialog.getOpenFileName()`.
2.  Устанавливает заголовок диалогового окна как "Open JSON File".
3.  Устанавливает начальную директорию диалогового окна как "c:/user/documents/repos/hypotez/data/aliexpress/campaigns".
4.  Устанавливает фильтр файлов для отображения только JSON файлов (*.json).
5.  Если файл не выбран (путь к файлу отсутствует), функция завершает свою работу.
6.  Если файл выбран, вызывает метод `load_file()` для загрузки данных из выбранного файла.

**Примеры**:
```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.open_file()
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

**Назначение**:
Загружает данные кампании из JSON файла.

**Как работает функция**:
1.  Пытается загрузить данные из указанного JSON файла с помощью функции `j_loads_ns()`.
2.  Если загрузка прошла успешно, сохраняет путь к файлу кампании в переменной `self.campaign_file`.
3.  Устанавливает текст метки `self.file_name_label` с именем загруженного файла.
4.  Извлекает имя кампании из загруженных данных и сохраняет его в переменной `self.campaign_name`.
5.  Извлекает имя файла без расширения и сохраняет его в переменной `self.language`.
6.  Создает экземпляр класса `AliCampaignEditor` с указанным файлом кампании.
7.  Вызывает метод `create_widgets()` для создания виджетов на основе загруженных данных.
8.  Если во время загрузки или обработки данных возникает исключение, отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

**Параметры**:
- `campaign_file` (str): Путь к JSON файлу кампании.

**Примеры**:
```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.load_file("path/to/campaign.json")
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

**Назначение**:
Создает виджеты на основе данных, загруженных из JSON файла.

**Как работает функция**:
1.  Получает макет виджета.
2.  Удаляет все предыдущие виджеты из макета, кроме кнопок "Open JSON File", "Prepare All Categories", "Prepare Category" и метки с именем файла.
3.  Создает метку для отображения заголовка кампании и добавляет ее в макет.
4.  Создает метку для отображения имени кампании и добавляет ее в макет.
5.  Перебирает категории в данных кампании и для каждой категории создает метку с именем категории и добавляет ее в макет.

**Параметры**:
- `data` (SimpleNamespace): Данные кампании, загруженные из JSON файла.

**Примеры**:
```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.load_file("path/to/campaign.json")
category_editor.create_widgets(category_editor.data)
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

**Назначение**:
Асинхронно подготавливает все категории кампании.

**Как работает функция**:
1.  Проверяет, инициализирован ли редактор кампании (`self.editor`).
2.  Если редактор инициализирован, пытается асинхронно подготовить все категории с помощью метода `prepare_all_categories()` редактора.
3.  Если подготовка прошла успешно, отображает сообщение об успехе с помощью `QtWidgets.QMessageBox.information()`.
4.  Если во время подготовки возникает исключение, отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

**Примеры**:
```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.load_file("path/to/campaign.json")
asyncio.run(category_editor.prepare_all_categories_async())
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

**Назначение**:
Асинхронно подготавливает указанную категорию кампании.

**Как работает функция**:
1.  Проверяет, инициализирован ли редактор кампании (`self.editor`).
2.  Если редактор инициализирован, пытается асинхронно подготовить указанную категорию с помощью метода `prepare_category()` редактора, передавая имя кампании.
3.  Если подготовка прошла успешно, отображает сообщение об успехе с помощью `QtWidgets.QMessageBox.information()`.
4.  Если во время подготовки возникает исключение, отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

**Примеры**:
```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.load_file("path/to/campaign.json")
asyncio.run(category_editor.prepare_category_async())