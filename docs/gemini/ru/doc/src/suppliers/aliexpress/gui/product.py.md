# Модуль `product.py`

## Обзор

Модуль `product.py` предоставляет графический интерфейс для редактирования информации о продуктах, получаемых от поставщика AliExpress. Он включает в себя функциональность для загрузки данных о продуктах из JSON-файлов, отображения этих данных в пользовательском интерфейсе и подготовки продукта к дальнейшему использованию, например, для рекламных кампаний. Модуль использует библиотеку PyQt6 для создания графического интерфейса и включает асинхронные операции для обеспечения отзывчивости интерфейса во время выполнения длительных задач.

## Подробнее

Этот модуль является частью GUI-интерфейса для работы с данными AliExpress. Он позволяет пользователю загружать информацию о продукте из JSON-файла, просматривать основные характеристики продукта (например, заголовок и детали) и запускать процесс подготовки продукта с помощью `AliCampaignEditor`. Подготовка продукта может включать в себя различные операции, такие как оптимизация описания, выбор целевой аудитории и настройка параметров рекламной кампании.

## Классы

### `ProductEditor`

**Описание**: Класс `ProductEditor` является основным виджетом для редактирования информации о продукте. Он предоставляет интерфейс для загрузки JSON-файлов с данными о продуктах, отображения этих данных и запуска процесса подготовки продукта.

**Принцип работы**:
Класс `ProductEditor` создает окно с кнопками "Open JSON File" и "Prepare Product", а также меткой для отображения имени выбранного файла. При нажатии на кнопку "Open JSON File" открывается диалоговое окно выбора файла, позволяющее пользователю выбрать JSON-файл с данными о продукте. После выбора файла данные загружаются, отображаются в интерфейсе, и создается экземпляр класса `AliCampaignEditor` для подготовки продукта. Кнопка "Prepare Product" запускает асинхронный процесс подготовки продукта с использованием `AliCampaignEditor`.

**Аттрибуты**:

- `data` (SimpleNamespace): Пространство имен для хранения данных о продукте, загруженных из JSON-файла.
- `language` (str): Язык, используемый в данных о продукте (по умолчанию 'EN').
- `currency` (str): Валюта, используемая в данных о продукте (по умолчанию 'USD').
- `file_path` (str): Путь к загруженному JSON-файлу.
- `editor` (AliCampaignEditor): Экземпляр класса `AliCampaignEditor`, используемый для подготовки продукта.
- `main_app`: Ссылка на главный экземпляр приложения.

**Методы**:

- `__init__(self, parent=None, main_app=None)`: Инициализирует виджет `ProductEditor`, устанавливает пользовательский интерфейс и соединения между сигналами и слотами.
- `setup_ui(self)`: Настраивает пользовательский интерфейс виджета, добавляя кнопки, метки и определяя их расположение.
- `setup_connections(self)`: Устанавливает соединения между сигналами и слотами.
- `open_file(self)`: Открывает диалоговое окно выбора файла и загружает выбранный JSON-файл.
- `load_file(self, file_path)`: Загружает JSON-файл, извлекает данные и создает виджеты для отображения информации о продукте.
- `create_widgets(self, data)`: Создает виджеты для отображения информации о продукте на основе загруженных данных.
- `prepare_product_async(self)`: Асинхронно подготавливает продукт с использованием `AliCampaignEditor`.

## Функции

### `__init__`

```python
def __init__(self, parent=None, main_app=None):
    """ Initialize the ProductEditor widget """
    super().__init__(parent)
    self.main_app = main_app  # Save the MainApp instance

    self.setup_ui()
    self.setup_connections()
```

**Назначение**: Инициализирует виджет `ProductEditor`.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Вызывает конструктор родительского класса (`QtWidgets.QWidget`).
2. Сохраняет ссылку на экземпляр главного приложения.
3. Вызывает методы `setup_ui()` и `setup_connections()` для настройки пользовательского интерфейса и соединений между сигналами и слотами.

```
Инициализация ProductEditor
│
├─── Сохранение ссылки на главное приложение
│
├─── Настройка пользовательского интерфейса
│
└─── Установка соединений между сигналами и слотами
```

**Примеры**:
```python
editor = ProductEditor(main_app=app)
```

### `setup_ui`

```python
def setup_ui(self):
    """ Setup the user interface """
    self.setWindowTitle("Product Editor")
    self.resize(1800, 800)

    # Define UI components
    self.open_button = QtWidgets.QPushButton("Open JSON File")
    self.open_button.clicked.connect(self.open_file)

    self.file_name_label = QtWidgets.QLabel("No file selected")
    
    self.prepare_button = QtWidgets.QPushButton("Prepare Product")
    self.prepare_button.clicked.connect(self.prepare_product_async)

    layout = QtWidgets.QVBoxLayout(self)
    layout.addWidget(self.open_button)
    layout.addWidget(self.file_name_label)
    layout.addWidget(self.prepare_button)

    self.setLayout(layout)
```

**Назначение**: Настраивает пользовательский интерфейс виджета `ProductEditor`.

**Параметры**:
- `self` (ProductEditor): Экземпляр класса `ProductEditor`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Устанавливает заголовок окна.
2. Устанавливает размеры окна.
3. Создает кнопку "Open JSON File" и подключает ее к методу `open_file()`.
4. Создает метку для отображения имени выбранного файла.
5. Создает кнопку "Prepare Product" и подключает ее к асинхронному методу `prepare_product_async()`.
6. Создает вертикальный макет и добавляет в него кнопку "Open JSON File", метку для имени файла и кнопку "Prepare Product".
7. Устанавливает макет для виджета.

```
Настройка UI
│
├─── Установка заголовка окна
│
├─── Установка размеров окна
│
├─── Создание кнопки "Open JSON File"
│   │
│   └─── Подключение к методу open_file()
│
├─── Создание метки для имени файла
│
├─── Создание кнопки "Prepare Product"
│   │
│   └─── Подключение к асинхронному методу prepare_product_async()
│
├─── Создание вертикального макета
│   │
│   ├─── Добавление кнопки "Open JSON File"
│   │
│   ├─── Добавление метки для имени файла
│   │
│   └─── Добавление кнопки "Prepare Product"
│
└─── Установка макета для виджета
```

**Примеры**:
```python
editor = ProductEditor()
editor.setup_ui()
```

### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections """
    pass
```

**Назначение**: Устанавливает соединения между сигналами и слотами.

**Параметры**:
- `self` (ProductEditor): Экземпляр класса `ProductEditor`.

**Возвращает**:
- `None`

**Как работает функция**:
- В текущей реализации функция ничего не делает (`pass`). Она предназначена для установки соединений между сигналами и слотами, но в данном коде такие соединения не определены.

```
Установка соединений
│
└─── (В текущей реализации ничего не делает)
```

**Примеры**:
```python
editor = ProductEditor()
editor.setup_connections()
```

### `open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        self,
        "Open JSON File",
        "c:/user/documents/repos/hypotez/data/aliexpress/products",
        "JSON files (*.json)"
    )
    if not file_path:
        return  # No file selected

    self.load_file(file_path)
```

**Назначение**: Открывает диалоговое окно выбора файла и загружает выбранный JSON-файл.

**Параметры**:
- `self` (ProductEditor): Экземпляр класса `ProductEditor`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Открывает диалоговое окно выбора файла с заголовком "Open JSON File" и фильтром для JSON-файлов.
2. Если файл не выбран, функция завершается.
3. Вызывает метод `load_file()` для загрузки выбранного файла.

```
Открытие файла
│
├─── Открытие диалогового окна выбора файла
│
├─── Проверка, выбран ли файл
│   │
│   └─── Если нет, завершение функции
│
└─── Загрузка выбранного файла
```

**Примеры**:
```python
editor = ProductEditor()
editor.open_file()
```

### `load_file`

```python
def load_file(self, file_path):
    """ Load a JSON file """
    try:
        self.data = j_loads_ns(file_path)
        self.file_path = file_path
        self.file_name_label.setText(f"File: {self.file_path}")
        self.editor = AliCampaignEditor(file_path=file_path)
        self.create_widgets(self.data)
    except Exception as ex:
        QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")
```

**Назначение**: Загружает JSON-файл, извлекает данные и создает виджеты для отображения информации о продукте.

**Параметры**:
- `self` (ProductEditor): Экземпляр класса `ProductEditor`.
- `file_path` (str): Путь к JSON-файлу.

**Возвращает**:
- `None`

**Как работает функция**:
1. Пытается загрузить JSON-файл с использованием функции `j_loads_ns()` из модуля `src.utils.jjson`.
2. Сохраняет путь к файлу в атрибуте `file_path`.
3. Устанавливает текст метки `file_name_label` с именем загруженного файла.
4. Создает экземпляр класса `AliCampaignEditor`, передавая путь к файлу.
5. Вызывает метод `create_widgets()` для создания виджетов на основе загруженных данных.
6. Если возникает исключение, отображает сообщение об ошибке.

```
Загрузка файла
│
├─── Попытка загрузки JSON-файла
│   │
│   ├─── Сохранение пути к файлу
│   │
│   ├─── Установка текста метки с именем файла
│   │
│   ├─── Создание экземпляра AliCampaignEditor
│   │
│   └─── Создание виджетов на основе загруженных данных
│
└─── Обработка исключения
│   │
│   └─── Отображение сообщения об ошибке
```

**Примеры**:
```python
editor = ProductEditor()
editor.load_file("path/to/product.json")
```

### `create_widgets`

```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
    layout = self.layout()

    # Remove previous widgets except open button and file label
    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if widget not in [self.open_button, self.file_name_label, self.prepare_button]:
            widget.deleteLater()

    title_label = QtWidgets.QLabel(f"Product Title: {data.title}")
    layout.addWidget(title_label)

    # Additional product-specific details
    product_details_label = QtWidgets.QLabel(f"Product Details: {data.details}")
    layout.addWidget(product_details_label)
```

**Назначение**: Создает виджеты для отображения информации о продукте на основе загруженных данных.

**Параметры**:
- `self` (ProductEditor): Экземпляр класса `ProductEditor`.
- `data` (SimpleNamespace): Данные о продукте, загруженные из JSON-файла.

**Возвращает**:
- `None`

**Как работает функция**:
1. Получает макет виджета.
2. Удаляет все предыдущие виджеты из макета, кроме кнопок "Open JSON File" и "Prepare Product" и метки имени файла.
3. Создает метку для отображения заголовка продукта.
4. Добавляет метку заголовка в макет.
5. Создает метку для отображения деталей продукта.
6. Добавляет метку деталей продукта в макет.

```
Создание виджетов
│
├─── Получение макета виджета
│
├─── Удаление предыдущих виджетов
│
├─── Создание метки для заголовка продукта
│
├─── Добавление метки заголовка в макет
│
├─── Создание метки для деталей продукта
│
└─── Добавление метки деталей продукта в макет
```

**Примеры**:
```python
editor = ProductEditor()
data = j_loads_ns("path/to/product.json")
editor.create_widgets(data)
```

### `prepare_product_async`

```python
@asyncSlot()
async def prepare_product_async(self):
    """ Asynchronously prepare the product """
    if self.editor:
        try:
            await self.editor.prepare_product()
            QtWidgets.QMessageBox.information(self, "Success", "Product prepared successfully.")
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to prepare product: {ex}")
```

**Назначение**: Асинхронно подготавливает продукт с использованием `AliCampaignEditor`.

**Параметры**:
- `self` (ProductEditor): Экземпляр класса `ProductEditor`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Проверяет, создан ли экземпляр `AliCampaignEditor`.
2. Пытается асинхронно подготовить продукт, вызвав метод `prepare_product()` у экземпляра `AliCampaignEditor`.
3. Если подготовка продукта прошла успешно, отображает сообщение об успехе.
4. Если возникает исключение, отображает сообщение об ошибке.

```
Асинхронная подготовка продукта
│
├─── Проверка наличия AliCampaignEditor
│
├─── Попытка асинхронной подготовки продукта
│   │
│   ├─── Отображение сообщения об успехе
│
└─── Обработка исключения
│   │
│   └─── Отображение сообщения об ошибке
```

**Примеры**:
```python
editor = ProductEditor()
editor.editor = AliCampaignEditor()
await editor.prepare_product_async()