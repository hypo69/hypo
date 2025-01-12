# src.suppliers.aliexpress.gui.campaign

## Обзор

Данный модуль предоставляет виджет для редактирования кампаний AliExpress. Он позволяет загружать, редактировать и подготавливать данные кампаний из JSON-файлов.

## Содержание

1. [Классы](#классы)
    - [CampaignEditor](#campaigneditor)
2. [Функции](#функции)

## Классы

### `CampaignEditor`

**Описание**:
Класс `CampaignEditor` представляет собой виджет для редактирования кампаний AliExpress. Он позволяет загружать данные кампаний из JSON-файлов, отображать их в интерфейсе и подготавливать кампанию.

**Методы**:
- `__init__`: Инициализирует виджет `CampaignEditor`.
- `setup_ui`: Настраивает пользовательский интерфейс виджета.
- `setup_connections`: Устанавливает связи между сигналами и слотами.
- `open_file`: Открывает диалоговое окно для выбора и загрузки JSON-файла.
- `load_file`: Загружает JSON-файл и создает виджеты на основе его данных.
- `create_widgets`: Создает виджеты для отображения данных кампании.
- `prepare_campaign`: Асинхронно подготавливает кампанию.

#### `__init__`
```python
def __init__(self, parent=None, main_app=None) -> None:
    """
    Args:
        parent (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
        main_app (QtWidgets.QMainWindow, optional): Экземпляр главного приложения. По умолчанию `None`.
    """
```
**Описание**:
Инициализирует виджет `CampaignEditor`.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (QtWidgets.QMainWindow, optional): Экземпляр главного приложения. По умолчанию `None`.

#### `setup_ui`
```python
def setup_ui(self) -> None:
    """
    """
```
**Описание**:
Настраивает пользовательский интерфейс виджета.

#### `setup_connections`
```python
def setup_connections(self) -> None:
    """
    """
```
**Описание**:
Устанавливает связи между сигналами и слотами.

#### `open_file`
```python
def open_file(self) -> None:
    """
    """
```
**Описание**:
Открывает диалоговое окно для выбора и загрузки JSON-файла.

#### `load_file`
```python
def load_file(self, campaign_file: str) -> None:
    """
    Args:
        campaign_file (str): Путь к JSON-файлу.
    
    Raises:
        Exception: Если не удалось загрузить JSON-файл.
    """
```
**Описание**:
Загружает JSON-файл и создает виджеты на основе его данных.

**Параметры**:
- `campaign_file` (str): Путь к JSON-файлу.

**Вызывает исключения**:
- `Exception`: Если не удалось загрузить JSON-файл.

#### `create_widgets`
```python
def create_widgets(self, data: SimpleNamespace) -> None:
    """
    Args:
        data (SimpleNamespace): Данные для создания виджетов.
    """
```
**Описание**:
Создает виджеты для отображения данных кампании.

**Параметры**:
- `data` (SimpleNamespace): Данные для создания виджетов.

#### `prepare_campaign`
```python
@asyncSlot()
async def prepare_campaign(self) -> None:
    """
    Raises:
        Exception: Если не удалось подготовить кампанию.
    """
```
**Описание**:
Асинхронно подготавливает кампанию.

**Вызывает исключения**:
- `Exception`: Если не удалось подготовить кампанию.

## Функции
Нет функций, определенных в данном файле, только класс `CampaignEditor`.