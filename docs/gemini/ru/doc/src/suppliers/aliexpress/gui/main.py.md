# Модуль `main.py`

## Обзор

Модуль `main.py` представляет собой основной файл графического интерфейса (GUI) для управления рекламными кампаниями AliExpress. Он использует библиотеку PyQt6 для создания оконного приложения с несколькими вкладками, предназначенными для редактирования JSON-файлов, управления кампаниями и редактирования информации о продуктах.

## Подробней

Этот модуль является отправной точкой для запуска приложения, предоставляющего инструменты для работы с данными AliExpress. Он включает в себя создание главного окна, добавление вкладок для различных функций (редактор JSON, редактор кампаний, редактор продуктов) и настройку меню с опциями для открытия, сохранения и редактирования файлов.

## Классы

### `MainApp`

**Описание**: Основной класс приложения, наследуемый от `QtWidgets.QMainWindow`, создает главное окно с вкладками для различных редакторов.

**Принцип работы**:
Класс `MainApp` инициализирует главное окно приложения, создает виджеты вкладок для редактора JSON, редактора кампаний и редактора продуктов, а также настраивает меню с опциями для работы с файлами и редактирования. Он использует другие классы, такие как `CampaignEditor`, `CategoryEditor` и `ProductEditor`, для реализации функциональности каждой вкладки.

**Методы**:

- `__init__(self)`:
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
    **Назначение**: Инициализирует главное окно приложения с вкладками.

    **Как работает функция**:
    1.  Вызывает конструктор родительского класса `QtWidgets.QMainWindow`.
    2.  Устанавливает заголовок окна приложения.
    3.  Устанавливает геометрию окна (размер и положение).
    4.  Создает виджет `QTabWidget` для управления вкладками.
    5.  Создает три вкладки: "JSON Editor", "Campaign Editor" и "Product Editor".
    6.  Инициализирует соответствующие редакторы (`CampaignEditor`, `CategoryEditor` и `ProductEditor`) для каждой вкладки.
    7.  Вызывает метод `create_menubar` для создания меню.

- `create_menubar(self)`:
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
    **Назначение**: Создает строку меню с опциями для операций с файлами и командами редактирования.

    **Как работает функция**:
    1.  Создает строку меню (`menubar`) в главном окне.
    2.  Создает меню "File" с опциями "Open", "Save" и "Exit".
    3.  Назначает действия для каждой опции ("Open" вызывает `self.open_file`, "Save" вызывает `self.save_file`, "Exit" вызывает `self.exit_application`).
    4.  Создает меню "Edit" с опциями "Copy" и "Paste".
    5.  Назначает действия для каждой опции ("Copy" вызывает `self.copy`, "Paste" вызывает `self.paste`).
    6.  Добавляет опцию "Open Product File", которая вызывает метод `open_file` редактора продуктов.

- `open_file(self)`:
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
    **Назначение**: Открывает диалоговое окно выбора файла для загрузки JSON-файла.

    **Как работает функция**:
    1.  Создает экземпляр класса `QFileDialog` для открытия диалогового окна выбора файла.
    2.  Вызывает метод `getOpenFileName` для отображения диалогового окна и получения пути к выбранному файлу.
    3.  Проверяет, был ли выбран файл. Если нет, функция завершается.
    4.  Проверяет, какая вкладка активна. Если активна первая вкладка (JSON Editor), вызывает метод `self.load_file` для загрузки файла.

- `save_file(self)`:
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
    1.  Определяет индекс активной вкладки.
    2.  Если активна первая вкладка (JSON Editor), вызывает метод `save_changes` редактора кампаний.
    3.  Если активна третья вкладка (Product Editor), вызывает метод `save_product` редактора продуктов.

- `exit_application(self)`:
    ```python
    def exit_application(self):
        """ Exit the application """
        self.close()
    ```
    **Назначение**: Закрывает приложение.

    **Как работает функция**:
    1.  Вызывает метод `close` для закрытия главного окна приложения.

- `copy(self)`:
    ```python
    def copy(self):
        """ Copy selected text to the clipboard """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.copy()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to copy.")
    ```
    **Назначение**: Копирует выделенный текст в буфер обмена.

    **Как работает функция**:
    1.  Определяет виджет, находящийся в фокусе.
    2.  Проверяет, является ли виджет текстовым полем (QLineEdit, QTextEdit, QPlainTextEdit).
    3.  Если да, вызывает метод `copy` для копирования выделенного текста в буфер обмена.
    4.  Если нет, выводит предупреждающее сообщение.

- `paste(self)`:
    ```python
    def paste(self):
        """ Paste text from the clipboard """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.paste()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to paste.")
    ```
    **Назначение**: Вставляет текст из буфера обмена.

    **Как работает функция**:
    1.  Определяет виджет, находящийся в фокусе.
    2.  Проверяет, является ли виджет текстовым полем (QLineEdit, QTextEdit, QPlainTextEdit).
    3.  Если да, вызывает метод `paste` для вставки текста из буфера обмена.
    4.  Если нет, выводит предупреждающее сообщение.

- `load_file(self, campaign_file: str)`:
    ```python
    def load_file(self, campaign_file):
        """ Load the JSON file """
        try:
            self.promotion_app.load_file(campaign_file)
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")
    ```
    **Назначение**: Загружает JSON-файл с использованием `promotion_app`.

    **Параметры**:
    - `campaign_file` (str): Путь к JSON-файлу.

    **Как работает функция**:
    1.  Пытается загрузить JSON-файл с использованием метода `load_file` объекта `self.promotion_app`.
    2.  Если возникает исключение, выводит сообщение об ошибке.

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
1.  Создает экземпляр класса `QApplication`.
2.  Создает цикл событий для асинхронных операций с использованием `QEventLoop` и устанавливает его как текущий цикл событий asyncio.
3.  Создает экземпляр класса `MainApp`.
4.  Отображает главное окно приложения.
5.  Запускает цикл событий для обработки событий приложения.

**Примеры**:

```python
if __name__ == "__main__":
    main()
```
```
Здесь демонстрируется стандартный способ запуска графического приложения PyQt6 с использованием асинхронного цикла событий.