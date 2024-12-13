# Модуль `campaign.py`

## Обзор

Модуль `campaign.py` предоставляет пользовательский интерфейс для редактирования и подготовки кампаний AliExpress. Он включает в себя виджет для загрузки JSON-файлов, отображения полей кампании и инициирования процесса подготовки кампании.

## Содержание

- [Классы](#классы)
  - [`CampaignEditor`](#CampaignEditor)
- [Функции](#функции)

## Классы

### `CampaignEditor`

**Описание**:
Виджет `CampaignEditor` предоставляет интерфейс для редактирования и подготовки кампаний AliExpress. Он позволяет пользователю загружать JSON-файлы, отображать основные поля кампании и запускать процесс подготовки.

**Методы**:

- `__init__`: Инициализирует виджет `CampaignEditor`.
- `setup_ui`: Настраивает пользовательский интерфейс виджета.
- `setup_connections`: Настраивает связи между сигналами и слотами.
- `open_file`: Открывает диалоговое окно для выбора и загрузки JSON-файла.
- `load_file`: Загружает JSON-файл и создаёт виджеты для его отображения.
- `create_widgets`: Создаёт виджеты для отображения и редактирования данных кампании.
- `prepare_campaign`: Асинхронно подготавливает кампанию с использованием `AliCampaignEditor`.

**Параметры**:

- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

#### `__init__`

```python
def __init__(self, parent=None, main_app=None):
    """ Initialize the CampaignEditor widget """
    ...
```
**Описание**: Инициализирует виджет `CampaignEditor`, сохраняет экземпляр `MainApp` и настраивает пользовательский интерфейс и соединения.

**Параметры**:

- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

#### `setup_ui`
```python
def setup_ui(self):
    """ Setup the user interface """
    ...
```

**Описание**: Настраивает пользовательский интерфейс виджета, включая создание макета, кнопок и меток.

#### `setup_connections`
```python
def setup_connections(self):
    """ Setup signal-slot connections """
    ...
```

**Описание**: Настраивает связи между сигналами и слотами виджета. В текущей реализации не используется.

#### `open_file`
```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
    ...
```

**Описание**: Открывает диалоговое окно для выбора JSON-файла и вызывает `load_file` для загрузки выбранного файла.

#### `load_file`
```python
def load_file(self, campaign_file):
    """ Load a JSON file """
    ...
```

**Описание**: Загружает JSON-файл, отображает имя файла и создает виджеты для редактирования.
**Параметры**:

- `campaign_file` (str): Путь к JSON файлу.

**Вызывает исключения**:
- Exception: Если не удалось загрузить JSON файл.

#### `create_widgets`
```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
    ...
```

**Описание**: Создает виджеты для отображения и редактирования данных кампании на основе загруженных данных.
**Параметры**:

- `data` (SimpleNamespace): Данные кампании, загруженные из JSON файла.

#### `prepare_campaign`
```python
@asyncSlot()
async def prepare_campaign(self):
    """ Asynchronously prepare the campaign """
    ...
```

**Описание**: Асинхронно подготавливает кампанию с использованием `AliCampaignEditor`.

## Функции

В данном файле функции отсутствуют.