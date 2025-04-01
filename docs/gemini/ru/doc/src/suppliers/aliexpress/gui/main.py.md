# Модуль `main.py`

## Обзор

Модуль `main.py` представляет собой основной файл графического интерфейса (GUI) для управления рекламными кампаниями, редактором продуктов и редактором категорий AliExpress. Он использует библиотеку PyQt6 для создания интерфейса и включает функции для открытия, сохранения и редактирования файлов JSON, а также для копирования и вставки текста.

## Подробней

Этот модуль является отправной точкой для запуска приложения, которое предоставляет пользователю возможность управлять рекламными кампаниями, редактировать информацию о продуктах и категориях. Он организует различные редакторы в отдельные вкладки, обеспечивая удобный доступ к различным функциям.

## Классы

### `MainApp`

**Описание**: Основной класс приложения, который создает главное окно с вкладками для различных редакторов.

**Наследует**: `QtWidgets.QMainWindow`

**Атрибуты**:
- `tab_widget` (QtWidgets.QTabWidget): Виджет для организации вкладок в главном окне.
- `tab1` (QtWidgets.QWidget): Виджет первой вкладки (JSON Editor).
- `promotion_app` (CampaignEditor): Экземпляр редактора кампаний, связанный с первой вкладкой.
- `tab2` (QtWidgets.QWidget): Виджет второй вкладки (Campaign Editor).
- `campaign_editor_app` (CategoryEditor): Экземпляр редактора категорий, связанный со второй вкладкой.
- `tab3` (QtWidgets.QWidget): Виджет третьей вкладки (Product Editor).
- `product_editor_app` (ProductEditor): Экземпляр редактора продуктов, связанный с третьей вкладкой.

**Методы**:
- `__init__`: Инициализирует главное окно приложения, создает вкладки и добавляет их в виджет вкладок, а также создает меню.
- `create_menubar`: Создает меню с опциями для работы с файлами и редактирования.
- `open_file`: Открывает диалоговое окно для выбора и загрузки JSON-файла.
- `save_file`: Сохраняет текущий файл в зависимости от активной вкладки.
- `exit_application`: Закрывает приложение.
- `copy`: Копирует выделенный текст в буфер обмена.
- `paste`: Вставляет текст из буфера обмена.
- `load_file`: Загружает JSON-файл.

### `MainApp.__init__`

```python
def __init__(self):
    """ Initialize the main application with tabs """
    super().__init__()
    self.setWindowTitle("Main Application with Tabs")
    self.setGeometry(100, 100, 1800, 800)

    self.tab_widget = QtWidgets.QTabWidget()
    self.setCentralWidget(self.tab_widget)

    # Create the JSON Editor tab and add it to the tab widget
    self.tab1 = QtWidgets.QWidget()
    self.tab_widget.addTab(self.tab1, "JSON Editor")
    self.promotion_app = CampaignEditor(self.tab1, self)

    # Create the Campaign Editor tab and add it to the tab widget
    self.tab2 = QtWidgets.QWidget()
    self.tab_widget.addTab(self.tab2, "Campaign Editor")
    self.campaign_editor_app = CategoryEditor(self.tab2, self)

    # Create the Product Editor tab and add it to the tab widget
    self.tab3 = QtWidgets.QWidget()
    self.tab_widget.addTab(self.tab3, "Product Editor")
    self.product_editor_app = ProductEditor(self.tab3, self)

    self.create_menubar()
```

**Назначение**: Инициализирует главное окно приложения, создавая вкладки для различных редакторов (JSON Editor, Campaign Editor, Product Editor) и добавляя их в виджет вкладок. Также вызывает метод `create_menubar` для создания меню.

**Как работает функция**:
1. Вызывает конструктор родительского класса `QtWidgets.QMainWindow`.
2. Устанавливает заголовок окна приложения.
3. Устанавливает геометрию окна (размер и положение).
4. Создает виджет вкладок `QTabWidget` и устанавливает его в качестве центрального виджета.
5. Создает виджеты для каждой вкладки (`QWidget`) и добавляет их в виджет вкладок.
6. Создает экземпляры редакторов (`CampaignEditor`, `CategoryEditor`, `ProductEditor`) и связывает их с соответствующими вкладками.
7. Вызывает метод `create_menubar` для создания меню.

### `MainApp.create_menubar`

```python
def create_menubar(self):
    """ Create a menu bar with options for file operations and edit commands """
    menubar = self.menuBar()

    file_menu = menubar.addMenu("File")
    open_action = QtGui.QAction("Open", self)
    open_action.triggered.connect(self.open_file)
    file_menu.addAction(open_action)
    save_action = QtGui.QAction("Save", self)
    save_action.triggered.connect(self.save_file)
    file_menu.addAction(save_action)
    exit_action = QtGui.QAction("Exit", self)
    exit_action.triggered.connect(self.exit_application)
    file_menu.addAction(exit_action)

    edit_menu = menubar.addMenu("Edit")
    copy_action = QtGui.QAction("Copy", self)
    copy_action.triggered.connect(self.copy)
    edit_menu.addAction(copy_action)
    paste_action = QtGui.QAction("Paste", self)
    paste_action.triggered.connect(self.paste)
    edit_menu.addAction(paste_action)

    open_product_action = QtGui.QAction("Open Product File", self)
    open_product_action.triggered.connect(self.product_editor_app.open_file)
    file_menu.addAction(open_product_action)
```

**Назначение**: Создает меню в главном окне приложения с опциями для работы с файлами (открытие, сохранение, выход) и редактирования (копирование, вставка).

**Как работает функция**:
1. Получает строку меню (`menubar`) с помощью `self.menuBar()`.
2. Создает меню "File" и добавляет действия "Open", "Save" и "Exit", связывая их с соответствующими методами (`open_file`, `save_file`, `exit_application`).
3. Создает меню "Edit" и добавляет действия "Copy" и "Paste", связывая их с соответствующими методами (`copy`, `paste`).
4. Добавляет действие "Open Product File" в меню "File", связывая его с методом `open_file` редактора продуктов.

### `MainApp.open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
    file_dialog = QtWidgets.QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "JSON files (*.json)")
    if not file_path:
        return

    if self.tab_widget.currentIndex() == 0:
        self.load_file(file_path)
```

**Назначение**: Открывает диалоговое окно выбора файла для загрузки JSON-файла и, если выбрана вкладка "JSON Editor", вызывает метод `load_file` для загрузки файла.

**Как работает функция**:
1. Создает экземпляр `QFileDialog` для открытия диалогового окна выбора файла.
2. Открывает диалоговое окно с заголовком "Open File" и фильтром для JSON-файлов.
3. Получает путь к выбранному файлу.
4. Проверяет, была ли выбрана вкладка "JSON Editor" (индекс 0).
5. Если вкладка "JSON Editor" активна, вызывает метод `load_file` для загрузки выбранного файла.

### `MainApp.save_file`

```python
def save_file(self):
    """ Save the current file """
    current_index = self.tab_widget.currentIndex()
    if current_index == 0:
        self.promotion_app.save_changes()
    elif current_index == 2:
        self.product_editor_app.save_product()
```

**Назначение**: Сохраняет текущий файл в зависимости от активной вкладки.

**Как работает функция**:
1. Определяет индекс текущей активной вкладки.
2. Если активна вкладка "JSON Editor" (индекс 0), вызывает метод `save_changes` редактора кампаний.
3. Если активна вкладка "Product Editor" (индекс 2), вызывает метод `save_product` редактора продуктов.

### `MainApp.exit_application`

```python
def exit_application(self):
    """ Exit the application """
    self.close()
```

**Назначение**: Закрывает приложение.

**Как работает функция**:
1. Вызывает метод `close` для закрытия главного окна приложения.

### `MainApp.copy`

```python
def copy(self):
    """ Copy selected text to the clipboard """
    widget = self.focusWidget()
    if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
        widget.copy()
    else:
        QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to copy.")
```

**Назначение**: Копирует выделенный текст из активного текстового виджета в буфер обмена.

**Как работает функция**:
1. Получает виджет, находящийся в фокусе.
2. Проверяет, является ли виджет экземпляром `QLineEdit`, `QTextEdit` или `QPlainTextEdit`.
3. Если виджет является текстовым виджетом, вызывает его метод `copy` для копирования выделенного текста.
4. Если виджет не является текстовым виджетом, отображает предупреждающее сообщение.

### `MainApp.paste`

```python
def paste(self):
    """ Paste text from the clipboard """
    widget = self.focusWidget()
    if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
        widget.paste()
    else:
        QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to paste.")
```

**Назначение**: Вставляет текст из буфера обмена в активный текстовый виджет.

**Как работает функция**:
1. Получает виджет, находящийся в фокусе.
2. Проверяет, является ли виджет экземпляром `QLineEdit`, `QTextEdit` или `QPlainTextEdit`.
3. Если виджет является текстовым виджетом, вызывает его метод `paste` для вставки текста.
4. Если виджет не является текстовым виджетом, отображает предупреждающее сообщение.

### `MainApp.load_file`

```python
def load_file(self, campaign_file):
    """ Load the JSON file """
    try:
        self.promotion_app.load_file(campaign_file)
    except Exception as ex:
        QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")
```

**Назначение**: Загружает JSON-файл, используя метод `load_file` редактора кампаний.

**Как работает функция**:
1. Пытается вызвать метод `load_file` редактора кампаний для загрузки указанного файла.
2. В случае возникновения исключения отображает сообщение об ошибке.

## Функции

### `main`

```python
def main():
    """ Initialize and run the application """
    app = QtWidgets.QApplication(sys.argv)

    # Create an event loop for asynchronous operations
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    main_app = MainApp()
    main_app.show()

    # Run the event loop
    with loop:
        loop.run_forever()
```

**Назначение**: Инициализирует и запускает приложение.

**Как работает функция**:
1. Создает экземпляр `QApplication`.
2. Создает цикл событий для асинхронных операций, используя `QEventLoop`.
3. Устанавливает цикл событий для модуля `asyncio`.
4. Создает экземпляр класса `MainApp`.
5. Отображает главное окно приложения.
6. Запускает цикл событий для обработки событий приложения.

### **Как работает функция `main`**:

1.  **Создание экземпляра `QApplication`**: Инициализирует Qt-приложение, необходимое для работы графического интерфейса.
2.  **Создание и настройка цикла событий**: Создает цикл событий `QEventLoop`, который позволяет асинхронно обрабатывать события в приложении. Этот цикл событий связывается с asyncio, что позволяет использовать асинхронные операции.
3.  **Создание и отображение главного окна**: Создает экземпляр `MainApp`, который представляет собой главное окно приложения, и отображает его.
4.  **Запуск цикла событий**: Запускает цикл событий, который обрабатывает все события приложения до его завершения.

```
Создание QApplication
│
↓
Создание QEventLoop
│
↓
Создание MainApp
│
↓
Отображение MainApp
│
↓
Запуск цикла событий QEventLoop
```

**Примеры**:

```python
if __name__ == "__main__":
    main()