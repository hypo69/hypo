# Модуль `category.py`

## Обзор

Модуль предоставляет графический интерфейс для подготовки рекламных кампаний AliExpress. Он позволяет загружать JSON-файлы с данными о категориях, отображать информацию о кампаниях и категориях, а также асинхронно подготавливать все категории или конкретную категорию.

## Подробней

Модуль `category.py` является частью проекта `hypotez` и предназначен для работы с рекламными кампаниями на AliExpress. Он предоставляет интерфейс для редактирования категорий, загрузки данных из JSON-файлов и подготовки кампаний.  Модуль использует библиотеку `PyQt6` для создания графического интерфейса и `qasync` для асинхронного выполнения операций. `AliCampaignEditor` - класс, отвечающий за редактирование кампаний.

## Классы

### `CategoryEditor`

**Описание**:
Класс `CategoryEditor` представляет собой виджет (окно) для редактирования категорий рекламных кампаний.

**Наследует**:
- `QtWidgets.QWidget`: Класс `CategoryEditor` наследует функциональность стандартного виджета `QWidget` из библиотеки `PyQt6`.

**Атрибуты**:
- `campaign_name` (str): Имя кампании. По умолчанию `None`.
- `data` (SimpleNamespace): Данные кампании, загруженные из JSON-файла. По умолчанию `None`.
- `language` (str): Язык кампании. По умолчанию `'EN'`.
- `currency` (str): Валюта кампании. По умолчанию `'USD'`.
- `file_path` (str): Путь к файлу кампании. По умолчанию `None`.
- `editor` (AliCampaignEditor): Объект класса `AliCampaignEditor` для редактирования кампании.
- `main_app`: Ссылка на главный экземпляр приложения.
- `open_button`: Кнопка для открытия JSON-файла.
- `file_name_label`: Метка для отображения имени выбранного файла.
- `prepare_all_button`: Кнопка для подготовки всех категорий.
- `prepare_specific_button`: Кнопка для подготовки конкретной категории.

**Методы**:
- `__init__(self, parent=None, main_app=None)`: Инициализирует окно редактирования категорий.
- `setup_ui(self)`: Настраивает пользовательский интерфейс.
- `setup_connections(self)`: Устанавливает соединения между сигналами и слотами.
- `open_file(self)`: Открывает диалоговое окно для выбора и загрузки JSON-файла.
- `load_file(self, campaign_file)`: Загружает JSON-файл.
- `create_widgets(self, data)`: Создает виджеты на основе данных, загруженных из JSON-файла.
- `prepare_all_categories_async(self)`: Асинхронно подготавливает все категории.
- `prepare_category_async(self)`: Асинхронно подготавливает конкретную категорию.

### `__init__`

```python
def __init__(self, parent=None, main_app=None):
    """ Initialize the main window"""
```

**Назначение**:
Инициализирует основной виджет (окно) `CategoryEditor`.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app`: Ссылка на главный экземпляр приложения.

**Как работает функция**:
1. Вызывает конструктор родительского класса `QtWidgets.QWidget`.
2. Сохраняет ссылку на главный экземпляр приложения в атрибуте `self.main_app`.
3. Вызывает методы `setup_ui()` и `setup_connections()` для настройки пользовательского интерфейса и соединений между сигналами и слотами.

**Примеры**:

```python
category_editor = CategoryEditor(main_app=main_app_instance)
```

### `setup_ui`

```python
def setup_ui(self):
    """ Setup the user interface"""
```

**Назначение**:
Настраивает пользовательский интерфейс виджета `CategoryEditor`.

**Как работает функция**:
1. Устанавливает заголовок окна как "Category Editor".
2. Устанавливает размер окна как 1800x800 пикселей.
3. Определяет компоненты пользовательского интерфейса:
   - `open_button`: Кнопка "Open JSON File", при нажатии вызывается метод `open_file()`.
   - `file_name_label`: Метка "No file selected", отображает имя выбранного файла.
   - `prepare_all_button`: Кнопка "Prepare All Categories", при нажатии вызывается метод `prepare_all_categories_async()`.
   - `prepare_specific_button`: Кнопка "Prepare Category", при нажатии вызывается метод `prepare_category_async()`.
4. Создает вертикальный макет (`QVBoxLayout`) и добавляет в него компоненты пользовательского интерфейса.
5. Устанавливает созданный макет в качестве макета для виджета `CategoryEditor`.

**Примеры**:

```python
category_editor.setup_ui()
```

### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections"""
```

**Назначение**:
Устанавливает соединения между сигналами и слотами. В текущей реализации метод пуст.

**Как работает функция**:
1. В текущей реализации ничего не делает, но предназначен для установки соединений между сигналами и слотами в будущем.

**Примеры**:

```python
category_editor.setup_connections()
```

### `open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
```

**Назначение**:
Открывает диалоговое окно для выбора и загрузки JSON-файла.

**Как работает функция**:
1. Открывает диалоговое окно с помощью `QtWidgets.QFileDialog.getOpenFileName()`:
   - Устанавливает заголовок окна как "Open JSON File".
   - Устанавливает начальную директорию как "c:/user/documents/repos/hypotez/data/aliexpress/campaigns".
   - Устанавливает фильтр файлов как "JSON files (*.json)".
2. Если файл не выбран, функция завершается.
3. Если файл выбран, вызывается метод `load_file()` с путем к выбранному файлу.

**Примеры**:

```python
category_editor.open_file()
```

### `load_file`

```python
def load_file(self, campaign_file):
    """ Load a JSON file """
```

**Назначение**:
Загружает JSON-файл.

**Параметры**:
- `campaign_file` (str): Путь к JSON-файлу.

**Как работает функция**:
1. Пытается загрузить JSON-файл с помощью `j_loads_ns()`:
   - Если загрузка прошла успешно, сохраняет данные в атрибуте `self.data`.
   - Сохраняет путь к файлу в атрибуте `self.campaign_file`.
   - Устанавливает текст метки `self.file_name_label` с именем файла.
   - Извлекает имя кампании из данных и сохраняет в атрибуте `self.campaign_name`.
   - Извлекает язык кампании из имени файла (без расширения) и сохраняет в атрибуте `self.language`.
   - Создает экземпляр класса `AliCampaignEditor` с путем к файлу.
   - Вызывает метод `create_widgets()` с загруженными данными.
2. Если возникает исключение, отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

**Примеры**:

```python
category_editor.load_file("c:/user/documents/repos/hypotez/data/aliexpress/campaigns/EN.json")
```

### `create_widgets`

```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
```

**Назначение**:
Создает виджеты на основе данных, загруженных из JSON-файла.

**Параметры**:
- `data` (SimpleNamespace): Данные, загруженные из JSON-файла.

**Как работает функция**:
1. Получает макет виджета.
2. Удаляет все предыдущие виджеты из макета, кроме кнопок `open_button`, `file_name_label`, `prepare_all_button` и `prepare_specific_button`.
3. Создает метку с заголовком кампании и добавляет ее в макет.
4. Создает метку с именем кампании и добавляет ее в макет.
5. Для каждой категории в данных создает метку с именем категории и добавляет ее в макет.

**Примеры**:

```python
category_editor.create_widgets(data)
```

### `prepare_all_categories_async`

```python
@asyncSlot()
async def prepare_all_categories_async(self):
    """ Asynchronously prepare all categories """
```

**Назначение**:
Асинхронно подготавливает все категории.

**Как работает функция**:
1. Проверяет, существует ли редактор кампании (`self.editor`).
2. Если редактор существует, пытается асинхронно подготовить все категории с помощью `await self.editor.prepare_all_categories()`:
   - Если подготовка прошла успешно, отображает сообщение об успехе с помощью `QtWidgets.QMessageBox.information()`.
   - Если возникает исключение, отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

**Примеры**:

```python
asyncio.run(category_editor.prepare_all_categories_async())
```

### `prepare_category_async`

```python
@asyncSlot()
async def prepare_category_async(self):
    """ Asynchronously prepare a specific category """
```

**Назначение**:
Асинхронно подготавливает конкретную категорию.

**Как работает функция**:
1. Проверяет, существует ли редактор кампании (`self.editor`).
2. Если редактор существует, пытается асинхронно подготовить конкретную категорию с помощью `await self.editor.prepare_category(self.data.campaign_name)`:
   - Если подготовка прошла успешно, отображает сообщение об успехе с помощью `QtWidgets.QMessageBox.information()`.
   - Если возникает исключение, отображает сообщение об ошибке с помощью `QtWidgets.QMessageBox.critical()`.

**Примеры**:

```python
asyncio.run(category_editor.prepare_category_async())
```

## Функции

В данном модуле функции отсутствуют.

```