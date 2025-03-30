# Модуль `facebook_groups_widgets`

## Обзор

Модуль `facebook_groups_widgets` предоставляет класс `FacebookGroupsWidget`, который создает выпадающий список с URL групп Facebook на основе данных из JSON-файла. Этот модуль предназначен для использования в интерфейсах, где требуется выбор группы Facebook для, например, размещения объявлений.

## Подробней

Этот модуль облегчает выбор групп Facebook, отображая их в виде выпадающего списка. Он использует `ipywidgets` для создания интерактивного элемента интерфейса, который позволяет пользователю выбирать нужную группу из списка, загруженного из JSON-файла. Класс `FacebookGroupsWidget` инициализируется путем указания пути к JSON-файлу, содержащему информацию о группах.

## Классы

### `FacebookGroupsWidget`

**Описание**: Класс `FacebookGroupsWidget` создает и управляет выпадающим списком групп Facebook на основе данных из JSON-файла.

**Методы**:
- `__init__`: Инициализирует виджет, загружает данные из JSON и создает выпадающий список.
- `create_dropdown`: Создает виджет выпадающего списка на основе данных о группах.
- `display_widget`: Отображает виджет выпадающего списка.

**Параметры**:
- `json_file_path` (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.

**Примеры**:
```python
from pathlib import Path
from src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

# Пример использования класса FacebookGroupsWidget
json_file_path = Path('path/to/your/groups.json')
groups_widget = FacebookGroupsWidget(json_file_path)
groups_widget.display_widget()
```

## Функции

### `__init__`

```python
def __init__(self, json_file_path: Path):
    """
    Args:
        json_file_path (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.
    """
```

**Описание**: Инициализирует виджет с выпадающим списком для групп Facebook. Загружает данные из JSON-файла и создает выпадающий список.

**Параметры**:
- `json_file_path` (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.

**Примеры**:
```python
from pathlib import Path
from src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

json_file_path = Path('path/to/your/groups.json')
groups_widget = FacebookGroupsWidget(json_file_path)
```

### `create_dropdown`

```python
def create_dropdown(self) -> Dropdown:
    """
    Returns:
        Dropdown: Виджет выпадающего списка с URL групп Facebook.
    """
```

**Описание**: Создает и возвращает виджет выпадающего списка на основе данных групп.

**Возвращает**:
- `Dropdown`: Виджет выпадающего списка с URL групп Facebook.

**Примеры**:
```python
from pathlib import Path
from src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget
from ipywidgets import Dropdown

json_file_path = Path('path/to/your/groups.json')
groups_widget = FacebookGroupsWidget(json_file_path)
dropdown = groups_widget.create_dropdown()

if isinstance(dropdown, Dropdown):
    print("Dropdown created successfully")
```

### `display_widget`

```python
def display_widget(self):
    """
    """
```

**Описание**: Отображает виджет выпадающего списка.

**Примеры**:
```python
from pathlib import Path
from src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

json_file_path = Path('path/to/your/groups.json')
groups_widget = FacebookGroupsWidget(json_file_path)
groups_widget.display_widget()