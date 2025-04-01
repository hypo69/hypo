# Модуль `campaign`

## Обзор

Модуль `campaign.py` предоставляет графический интерфейс для редактирования кампаний AliExpress. Он позволяет пользователям открывать JSON-файлы, содержащие данные о кампаниях, редактировать их параметры, такие как заголовок, описание и название промоакции, и подготавливать кампании для дальнейшего использования.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для использования в GUI приложениях, связанных с управлением кампаниями AliExpress. Он включает в себя классы и методы для загрузки, отображения и редактирования данных кампаний в удобном для пользователя виде. Класс `CampaignEditor` является основным виджетом, который предоставляет интерфейс для работы с кампаниями. Он использует другие модули, такие как `src.utils.jjson` для загрузки и сохранения JSON-файлов, а также `src.suppliers.aliexpress.campaign` для подготовки кампаний.

## Классы

### `CampaignEditor`

**Описание**:
Виджет для редактирования кампаний. Предоставляет интерфейс для загрузки, отображения и редактирования данных кампаний.

**Методы**:
- `__init__`: Инициализирует виджет `CampaignEditor`.
- `setup_ui`: Настраивает пользовательский интерфейс виджета.
- `setup_connections`: Устанавливает соединения между сигналами и слотами.
- `open_file`: Открывает диалоговое окно для выбора и загрузки JSON-файла.
- `load_file`: Загружает JSON-файл и создает виджеты на основе загруженных данных.
- `create_widgets`: Создает виджеты для отображения и редактирования данных кампании.
- `prepare_campaign`: Асинхронно подготавливает кампанию.

**Параметры**:
- `parent` (QtWidgets.QWidget, optional): Родительский виджет. По умолчанию `None`.
- `main_app` (MainApp, optional): Экземпляр главного приложения. По умолчанию `None`.

**Примеры**:
```python
# Пример создания и использования CampaignEditor
from PyQt6 import QtWidgets
from campaign import CampaignEditor

app = QtWidgets.QApplication([])
campaign_editor = CampaignEditor()
campaign_editor.show()
app.exec()
```

## Функции

### `setup_ui`

```python
def setup_ui(self):
    """ Setup the user interface """
    ...
```

**Описание**: Настраивает пользовательский интерфейс виджета `CampaignEditor`.

**Методы**:
- Создает и настраивает основные элементы интерфейса, такие как кнопки, текстовые поля и область прокрутки.
- Устанавливает размеры и другие свойства элементов интерфейса.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.

**Возвращает**: None

**Вызывает исключения**: None

**Примеры**:
```python
# Пример вызова метода setup_ui
campaign_editor = CampaignEditor()
campaign_editor.setup_ui()
```

### `setup_connections`

```python
def setup_connections(self):
    """ Setup signal-slot connections """
    ...
```

**Описание**: Устанавливает соединения между сигналами и слотами.

**Методы**:
- В данном примере метод пустой, но в будущем он может быть использован для установки связей между сигналами и слотами виджета.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.

**Возвращает**: None

**Вызывает исключения**: None

**Примеры**:
```python
# Пример вызова метода setup_connections
campaign_editor = CampaignEditor()
campaign_editor.setup_connections()
```

### `open_file`

```python
def open_file(self):
    """ Open a file dialog to select and load a JSON file """
    ...
```

**Описание**: Открывает диалоговое окно для выбора и загрузки JSON-файла.

**Методы**:
- Открывает диалоговое окно с фильтром для JSON-файлов.
- Если файл выбран, вызывает метод `load_file` для загрузки данных из файла.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.

**Возвращает**: None

**Вызывает исключения**: None

**Примеры**:
```python
# Пример вызова метода open_file
campaign_editor = CampaignEditor()
campaign_editor.open_file()
```

### `load_file`

```python
def load_file(self, campaign_file):
    """ Load a JSON file """
    ...
```

**Описание**: Загружает JSON-файл и создает виджеты на основе загруженных данных.

**Методы**:
- Загружает данные из указанного JSON-файла с использованием `j_loads_ns`.
- Обновляет метку с именем файла.
- Создает виджеты для отображения и редактирования данных кампании с использованием `create_widgets`.
- Создает экземпляр `AliCampaignEditor` для подготовки кампании.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.
- `campaign_file` (str): Путь к JSON-файлу.

**Возвращает**: None

**Вызывает исключения**:
- `Exception`: Если не удается загрузить JSON-файл.

**Примеры**:
```python
# Пример вызова метода load_file
campaign_editor = CampaignEditor()
campaign_editor.load_file('path/to/campaign.json')
```

### `create_widgets`

```python
def create_widgets(self, data):
    """ Create widgets based on the data loaded from the JSON file """
    ...
```

**Описание**: Создает виджеты для отображения и редактирования данных кампании.

**Методы**:
- Удаляет предыдущие виджеты (кроме кнопок "Open JSON File", "Prepare Campaign" и метки имени файла).
- Создает текстовые поля для заголовка, описания и названия промоакции.
- Добавляет виджеты в макет.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.
- `data` (SimpleNamespace): Данные кампании, загруженные из JSON-файла.

**Возвращает**: None

**Вызывает исключения**: None

**Примеры**:
```python
# Пример вызова метода create_widgets
campaign_editor = CampaignEditor()
data = SimpleNamespace(title='Example Campaign', description='This is an example campaign', promotion_name='Summer Sale')
campaign_editor.create_widgets(data)
```

### `prepare_campaign`

```python
@asyncSlot()
async def prepare_campaign(self):
    """ Asynchronously prepare the campaign """
    ...
```

**Описание**: Асинхронно подготавливает кампанию.

**Методы**:
- Вызывает метод `prepare` объекта `AliCampaignEditor` для подготовки кампании.
- Отображает информационное сообщение об успешной подготовке кампании или сообщение об ошибке, если подготовка не удалась.

**Параметры**:
- `self` (CampaignEditor): Экземпляр класса `CampaignEditor`.

**Возвращает**: None

**Вызывает исключения**:
- `Exception`: Если не удается подготовить кампанию.

**Примеры**:
```python
# Пример вызова метода prepare_campaign
campaign_editor = CampaignEditor()
# Предполагается, что editor уже инициализирован и данные загружены
await campaign_editor.prepare_campaign()