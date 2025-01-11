# Модуль `category.py`

## Обзор

Модуль `category.py` предоставляет графический интерфейс (GUI) для подготовки рекламных кампаний AliExpress. Он позволяет пользователю загружать JSON-файлы с данными кампаний, просматривать их содержимое, а также подготавливать все категории или конкретную категорию асинхронно. Модуль разработан с использованием библиотеки PyQt6 для создания графического интерфейса и `qasync` для асинхронных операций.

## Содержание

- [Классы](#классы)
  - [`CategoryEditor`](#categoryeditor)
- [Функции](#функции)

## Классы

### `CategoryEditor`

**Описание**: 
Класс `CategoryEditor` представляет собой виджет PyQt6 для редактирования и подготовки категорий рекламных кампаний AliExpress.

**Атрибуты**:
- `campaign_name` (str): Имя кампании.
- `data` (SimpleNamespace): Данные кампании, загруженные из JSON-файла.
- `language` (str): Язык кампании (по умолчанию 'EN').
- `currency` (str): Валюта кампании (по умолчанию 'USD').
- `file_path` (str): Путь к файлу кампании.
- `editor` (AliCampaignEditor): Экземпляр класса `AliCampaignEditor` для подготовки кампании.

**Методы**:

- `__init__`
- `setup_ui`
- `setup_connections`
- `open_file`
- `load_file`
- `create_widgets`
- `prepare_all_categories_async`
- `prepare_category_async`

#### `__init__`
```python
def __init__(self, parent=None, main_app=None):
```

**Описание**:
Инициализирует виджет `CategoryEditor`.
**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (Any, optional): Экземпляр основного приложения. По умолчанию `None`.

#### `setup_ui`
```python
def setup_ui(self):
```
**Описание**:
Настраивает пользовательский интерфейс виджета, включая кнопки, метки и размещение.

#### `setup_connections`
```python
def setup_connections(self):
```
**Описание**:
Устанавливает соединения сигнал-слот. В текущей версии не имеет реализаций.

#### `open_file`
```python
def open_file(self):
```
**Описание**:
Открывает диалоговое окно для выбора JSON-файла кампании и загружает его.

#### `load_file`
```python
def load_file(self, campaign_file):
```
**Описание**:
Загружает JSON-файл кампании, извлекает данные и создает виджеты.
**Параметры**:
- `campaign_file` (str): Путь к JSON-файлу кампании.

**Вызывает исключения**:
- `Exception`: Если не удается загрузить JSON-файл.

#### `create_widgets`
```python
def create_widgets(self, data):
```
**Описание**:
Создает виджеты для отображения данных кампании, включая название, имя кампании и список категорий.
**Параметры**:
- `data` (SimpleNamespace): Данные кампании.

#### `prepare_all_categories_async`
```python
@asyncSlot()
async def prepare_all_categories_async(self):
```
**Описание**:
Асинхронно подготавливает все категории кампании с помощью `AliCampaignEditor`.
**Вызывает исключения**:
- `Exception`: Если не удается подготовить все категории.

#### `prepare_category_async`
```python
@asyncSlot()
async def prepare_category_async(self):
```
**Описание**:
Асинхронно подготавливает конкретную категорию кампании с помощью `AliCampaignEditor`.
**Вызывает исключения**:
- `Exception`: Если не удается подготовить категорию.

## Функции

В данном модуле отсутствуют функции вне класса `CategoryEditor`.