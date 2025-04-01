# Модуль main.py

## Обзор

Модуль `main.py` представляет собой основной модуль графического интерфейса (GUI) для управления рекламными кампаниями AliExpress. Он предоставляет главное окно приложения с вкладками для редактирования JSON, управления кампаниями, редактирования продуктов и категорий. Модуль использует библиотеку PyQt6 для создания графического интерфейса и qasync для интеграции с асинхронным кодом.

## Подробней

Этот модуль является отправной точкой для запуска GUI приложения, предназначенного для управления рекламными кампаниями на AliExpress. Он включает в себя следующие основные компоненты:

-   Главное окно приложения (`MainApp`), которое содержит вкладки для различных функций, таких как редактирование JSON, управление кампаниями, редактирование продуктов и категорий.

-   Реализация меню бара с опциями для открытия, сохранения и выхода из приложения, а также для копирования и вставки текста.

-   Интеграция с другими модулями, такими как `CampaignEditor`, `CategoryEditor` и `ProductEditor`, для предоставления специализированных инструментов редактирования.

Модуль использует асинхронный цикл событий (`QEventLoop`) для обеспечения отзывчивости пользовательского интерфейса при выполнении длительных операций.

## Классы

### `MainApp`

**Описание**: Главное окно приложения, которое содержит вкладки для редактирования JSON, управления кампаниями и редактирования продуктов.

**Как работает класс**:

1.  **Инициализация**:
    *   Создает главное окно приложения с заголовком "Main Application with Tabs".
    *   Устанавливает размеры окна.
    *   Создает виджет вкладок (`QTabWidget`) и устанавливает его в качестве центрального виджета.
    *   Создает вкладки для редактирования JSON, управления кампаниями и редактирования продуктов, используя виджеты `CampaignEditor`, `CategoryEditor` и `ProductEditor` соответственно.
    *   Создает меню бар с опциями для работы с файлами и редактирования.
2.  **Меню бар**:
    *   Содержит пункты меню "File" (Open, Save, Exit) и "Edit" (Copy, Paste).
    *   Подключает действия меню к соответствующим функциям.
3.  **Взаимодействие с вкладками**:
    *   Позволяет пользователю переключаться между вкладками для выполнения различных задач.
    *   Передает события и данные между главным окном и виджетами вкладок.

**Методы**:

*   `__init__`: Инициализирует главное окно приложения с вкладками.
*   `create_menubar`: Создает меню бар с опциями для работы с файлами и редактирования.
*   `open_file`: Открывает диалоговое окно для выбора и загрузки JSON файла.
*   `save_file`: Сохраняет текущий файл.
*   `exit_application`: Закрывает приложение.
*   `copy`: Копирует выделенный текст в буфер обмена.
*   `paste`: Вставляет текст из буфера обмена.
*   `load_file`: Загружает JSON файл.

#### `__init__`

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

**Описание**: Инициализирует главное окно приложения с вкладками.

**Как работает функция**:

1.  Вызывает конструктор базового класса `QtWidgets.QMainWindow`.
2.  Устанавливает заголовок окна в "Main Application with Tabs".
3.  Устанавливает геометрию окна (позиция и размеры).
4.  Создает виджет вкладок `QTabWidget` и устанавливает его в качестве центрального виджета.
5.  Создает три вкладки:
    *   "JSON Editor": Использует виджет `CampaignEditor`.
    *   "Campaign Editor": Использует виджет `CategoryEditor`.
    *   "Product Editor": Использует виджет `ProductEditor`.
6.  Вызывает метод `create_menubar` для создания меню бара.

#### `create_menubar`

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

**Описание**: Создает меню бар с опциями для работы с файлами и редактирования.

**Как работает функция**:

1.  Получает объект меню бара (`menuBar`).
2.  Создает меню "File" с опциями:
    *   "Open": Открывает диалоговое окно для выбора файла.
    *   "Save": Сохраняет текущий файл.
    *   "Exit": Закрывает приложение.
3.  Создает меню "Edit" с опциями:
    *   "Copy": Копирует выделенный текст.
    *   "Paste": Вставляет текст из буфера обмена.
4.  Подключает действия меню к соответствующим функциям.

#### `open_file`

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

**Описание**: Открывает диалоговое окно для выбора и загрузки JSON файла.

**Как работает функция**:

1.  Создает объект `QFileDialog` для открытия диалогового окна выбора файла.
2.  Открывает диалоговое окно и позволяет пользователю выбрать JSON файл.
3.  Если файл не выбран, функция завершается.
4.  Если выбрана вкладка "JSON Editor" (индекс 0), вызывает метод `load_file` для загрузки файла.

#### `save_file`

```python
    def save_file(self):
        """ Save the current file """
        current_index = self.tab_widget.currentIndex()
        if current_index == 0:
            self.promotion_app.save_changes()
        elif current_index == 2:
            self.product_editor_app.save_product()
```

**Описание**: Сохраняет текущий файл.

**Как работает функция**:

1.  Получает индекс текущей вкладки.
2.  Если выбрана вкладка "JSON Editor" (индекс 0), вызывает метод `save_changes` виджета `CampaignEditor`.
3.  Если выбрана вкладка "Product Editor" (индекс 2), вызывает метод `save_product` виджета `ProductEditor`.

#### `exit_application`

```python
    def exit_application(self):
        """ Exit the application """
        self.close()
```

**Описание**: Закрывает приложение.

**Как работает функция**:

1.  Вызывает метод `close` для закрытия главного окна приложения.

#### `copy`

```python
    def copy(self):
        """ Copy selected text to the clipboard """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.copy()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to copy.")
```

**Описание**: Копирует выделенный текст в буфер обмена.

**Как работает функция**:

1.  Получает виджет, находящийся в фокусе.
2.  Проверяет, является ли виджет текстовым полем (`QLineEdit`, `QTextEdit`, `QPlainTextEdit`).
3.  Если виджет является текстовым полем, вызывает метод `copy` для копирования выделенного текста в буфер обмена.
4.  Если виджет не является текстовым полем, отображает предупреждающее сообщение.

#### `paste`

```python
    def paste(self):
        """ Paste text from the clipboard """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.paste()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to paste.")
```

**Описание**: Вставляет текст из буфера обмена.

**Как работает функция**:

1.  Получает виджет, находящийся в фокусе.
2.  Проверяет, является ли виджет текстовым полем (`QLineEdit`, `QTextEdit`, `QPlainTextEdit`).
3.  Если виджет является текстовым полем, вызывает метод `paste` для вставки текста из буфера обмена.
4.  Если виджет не является текстовым полем, отображает предупреждающее сообщение.

#### `load_file`

```python
    def load_file(self, campaign_file):
        """ Load the JSON file """
        try:
            self.promotion_app.load_file(campaign_file)
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")
```

**Описание**: Загружает JSON файл.

**Как работает функция**:

1.  Пытается загрузить JSON файл с помощью метода `load_file` виджета `CampaignEditor`.
2.  Если возникает исключение, отображает сообщение об ошибке.

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

**Описание**: Инициализирует и запускает приложение.

**Как работает функция**:

1.  Создает экземпляр `QApplication`.
2.  Создает цикл событий для асинхронных операций, используя `QEventLoop`.
3.  Устанавливает созданный цикл событий как текущий цикл событий asyncio.
4.  Создает экземпляр главного окна приложения (`MainApp`).
5.  Отображает главное окно приложения.
6.  Запускает цикл событий для обработки событий пользовательского интерфейса.