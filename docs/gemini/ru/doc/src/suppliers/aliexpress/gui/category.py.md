# Модуль `category`

## Обзор

Модуль `category.py` предоставляет графический интерфейс для редактирования категорий рекламных кампаний AliExpress. Он позволяет загружать JSON-файлы с данными о кампаниях, отображать информацию о категориях и подготавливать все или отдельные категории для дальнейшей обработки. Модуль использует библиотеку PyQt6 для создания графического интерфейса и `AliCampaignEditor` для подготовки категорий.

## Подробнее

Этот модуль предназначен для визуализации и редактирования данных категорий, используемых в рекламных кампаниях AliExpress. Он позволяет загружать данные из JSON-файлов, отображать их в удобном формате и запускать процесс подготовки категорий. Подготовка категорий включает в себя обработку данных и их приведение к нужному формату для дальнейшего использования в рекламных кампаниях.
Модуль взаимодействует с классом `AliCampaignEditor` для выполнения задач подготовки категорий.

## Классы

### `CategoryEditor`

**Описание**: Основной класс, представляющий виджет графического интерфейса для редактирования категорий.

**Наследует**: `QtWidgets.QWidget`

**Атрибуты**:
- `campaign_name` (str): Имя кампании. Инициализируется как `None`.
- `data` (SimpleNamespace): Данные, загруженные из JSON-файла. Инициализируется как `None`.
- `language` (str): Язык кампании. По умолчанию `'EN'`.
- `currency` (str): Валюта кампании. По умолчанию `'USD'`.
- `file_path` (str): Путь к файлу с данными кампании. Инициализируется как `None`.
- `editor` (AliCampaignEditor): Экземпляр класса `AliCampaignEditor` для подготовки кампании.
- `main_app`: Ссылка на основной экземпляр приложения.
- `open_button`: Кнопка для открытия JSON-файла.
- `file_name_label`: Метка для отображения имени выбранного файла.
- `prepare_all_button`: Кнопка для подготовки всех категорий.
- `prepare_specific_button`: Кнопка для подготовки конкретной категории.

**Методы**:
- `__init__(self, parent=None, main_app=None)`: Инициализирует виджет, устанавливает пользовательский интерфейс и соединения между сигналами и слотами.
- `setup_ui(self)`: Создает и настраивает элементы пользовательского интерфейса (кнопки, метки, макеты).
- `setup_connections(self)`: Устанавливает соединения между сигналами и слотами. В текущей реализации не содержит соединений.
- `open_file(self)`: Открывает диалоговое окно для выбора JSON-файла и загружает его содержимое.
- `load_file(self, campaign_file)`: Загружает JSON-файл, устанавливает имя кампании, язык и создает виджеты на основе загруженных данных.
- `create_widgets(self, data)`: Создает виджеты для отображения данных о категориях кампании.
- `prepare_all_categories_async(self)`: Асинхронно подготавливает все категории с использованием `AliCampaignEditor`.
- `prepare_category_async(self)`: Асинхронно подготавливает определенную категорию с использованием `AliCampaignEditor`.

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

**Назначение**: Инициализирует класс `CategoryEditor`.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр основного приложения. По умолчанию `None`.

**Как работает функция**:
1. Вызывает конструктор родительского класса `QtWidgets.QWidget`.
2. Сохраняет ссылку на основной экземпляр приложения `main_app`.
3. Вызывает методы `setup_ui()` и `setup_connections()` для настройки пользовательского интерфейса и соединений.

```
A: Вызов конструктора родительского класса
|
B: Сохранение ссылки на экземпляр MainApp
|
C: Настройка пользовательского интерфейса (setup_ui)
|
D: Установка соединений (setup_connections)
```

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

**Назначение**: Настраивает пользовательский интерфейс виджета `CategoryEditor`.

**Как работает функция**:
1. Устанавливает заголовок окна как "Category Editor".
2. Устанавливает размеры окна на 1800x800 пикселей.
3. Определяет компоненты пользовательского интерфейса:
   - Кнопку "Open JSON File" (`self.open_button`) и подключает её к методу `self.open_file`.
   - Метку для отображения имени файла (`self.file_name_label`) с начальным текстом "No file selected".
   - Кнопку "Prepare All Categories" (`self.prepare_all_button`) и подключает её к асинхронному методу `self.prepare_all_categories_async`.
   - Кнопку "Prepare Category" (`self.prepare_specific_button`) и подключает её к асинхронному методу `self.prepare_category_async`.
4. Создает вертикальный макет (`QVBoxLayout`) и добавляет в него созданные компоненты.
5. Устанавливает созданный макет для виджета.

```
A: Установка заголовка окна
|
B: Установка размеров окна
|
C: Определение компонентов UI
|   |
|   C1: Создание кнопки "Open JSON File" и подключение к self.open_file
|   |
|   C2: Создание метки для имени файла
|   |
|   C3: Создание кнопки "Prepare All Categories" и подключение к self.prepare_all_categories_async
|   |
|   C4: Создание кнопки "Prepare Category" и подключение к self.prepare_category_async
|
D: Создание вертикального макета
|
E: Добавление компонентов в макет
|
F: Установка макета для виджета
```

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

**Назначение**: Устанавливает соединения между сигналами и слотами.

**Как работает функция**:
В текущей реализации функция пуста и не выполняет никаких действий.  Предполагается, что в будущем здесь будут установлены соединения между сигналами и слотами для обеспечения интерактивности пользовательского интерфейса.

```
A: (Функция пуста и ничего не делает)
```

**Примеры**:

```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.setup_connections()  # В текущем виде ничего не делает
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

**Назначение**: Открывает диалоговое окно для выбора JSON-файла и загружает его содержимое.

**Как работает функция**:
1. Открывает диалоговое окно выбора файла с помощью `QtWidgets.QFileDialog.getOpenFileName()`.
   - Устанавливает заголовок окна как "Open JSON File".
   - Устанавливает начальный каталог для поиска файлов.
   - Устанавливает фильтр файлов для отображения только JSON-файлов.
2. Проверяет, был ли выбран файл. Если файл не выбран (пустой путь), функция завершает работу.
3. Если файл выбран, вызывает метод `self.load_file()` для загрузки содержимого файла.

```
A: Открытие диалогового окна выбора файла
|
B: Проверка, был ли выбран файл
|
C: Загрузка содержимого файла (load_file) - если файл был выбран
```

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

**Назначение**: Загружает JSON-файл, устанавливает имя кампании, язык и создает виджеты на основе загруженных данных.

**Как работает функция**:
1. Пытается выполнить следующие действия:
   - Загружает данные из JSON-файла с помощью функции `j_loads_ns()` и сохраняет их в атрибуте `self.data`.
   - Сохраняет путь к файлу в атрибуте `self.campaign_file`.
   - Устанавливает текст метки `self.file_name_label` с именем файла.
   - Извлекает имя кампании из загруженных данных и сохраняет его в атрибуте `self.campaign_name`.
   - Извлекает язык кампании из имени файла (без расширения) и сохраняет его в атрибуте `self.language`.
   - Создает экземпляр класса `AliCampaignEditor` с путем к файлу кампании.
   - Вызывает метод `self.create_widgets()` для создания виджетов на основе загруженных данных.
2. Если возникает исключение, отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

```
A: Попытка загрузки данных из JSON-файла
|
B: Загрузка данных (j_loads_ns)
|
C: Сохранение пути к файлу
|
D: Установка текста метки с именем файла
|
E: Извлечение имени кампании
|
F: Извлечение языка кампании
|
G: Создание экземпляра AliCampaignEditor
|
H: Создание виджетов (create_widgets)
|
I: Обработка исключений (если возникли)
|
J: Отображение сообщения об ошибке (если возникло исключение)
```

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

**Назначение**: Создает виджеты для отображения данных о категориях кампании.

**Как работает функция**:
1. Получает текущий макет виджета.
2. Удаляет все предыдущие виджеты из макета, кроме кнопок `open_button`, `prepare_all_button`, `prepare_specific_button` и метки `file_name_label`.
3. Создает метку для отображения заголовка кампании (`data.title`) и добавляет ее в макет.
4. Создает метку для отображения имени кампании (`data.campaign_name`) и добавляет ее в макет.
5. Перебирает категории в данных (`data.categories`) и для каждой категории создает метку с именем категории (`category.name`) и добавляет ее в макет.

```
A: Получение текущего макета
|
B: Удаление предыдущих виджетов (кроме open_button и file_name_label)
|
C: Создание и добавление метки для заголовка кампании
|
D: Создание и добавление метки для имени кампании
|
E: Перебор категорий
|
F: Создание и добавление метки для имени каждой категории
```

**Примеры**:

```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.load_file("path/to/campaign.json")
# После загрузки файла:
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

**Назначение**: Асинхронно подготавливает все категории с использованием `AliCampaignEditor`.

**Как работает функция**:
1. Проверяет, инициализирован ли `self.editor`.
2. Если `self.editor` инициализирован, пытается выполнить следующие действия:
   - Вызывает асинхронный метод `self.editor.prepare_all_categories()` для подготовки всех категорий.
   - Отображает сообщение об успешной подготовке категорий с помощью `QtWidgets.QMessageBox.information()`.
3. Если возникает исключение, отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

```
A: Проверка, инициализирован ли self.editor
|
B: Подготовка всех категорий (если self.editor инициализирован)
|   |
|   B1: Вызов self.editor.prepare_all_categories()
|   |
|   B2: Отображение сообщения об успехе
|
C: Обработка исключений (если возникли)
|
D: Отображение сообщения об ошибке (если возникло исключение)
```

**Примеры**:

```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.load_file("path/to/campaign.json")
# После загрузки файла:
await category_editor.prepare_all_categories_async()
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

**Назначение**: Асинхронно подготавливает определенную категорию с использованием `AliCampaignEditor`.

**Как работает функция**:
1. Проверяет, инициализирован ли `self.editor`.
2. Если `self.editor` инициализирован, пытается выполнить следующие действия:
   - Вызывает асинхронный метод `self.editor.prepare_category()` для подготовки определенной категории.
   - Отображает сообщение об успешной подготовке категории с помощью `QtWidgets.QMessageBox.information()`.
3. Если возникает исключение, отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

```
A: Проверка, инициализирован ли self.editor
|
B: Подготовка определенной категории (если self.editor инициализирован)
|   |
|   B1: Вызов self.editor.prepare_category()
|   |
|   B2: Отображение сообщения об успехе
|
C: Обработка исключений (если возникли)
|
D: Отображение сообщения об ошибке (если возникло исключение)
```

**Примеры**:

```python
category_editor = CategoryEditor(main_app=main_app_instance)
category_editor.load_file("path/to/campaign.json")
# После загрузки файла:
await category_editor.prepare_category_async()