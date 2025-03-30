# Модуль facebook_groups_widgets

## Обзор

Модуль `facebook_groups_widgets.py` предназначен для создания интерактивного выпадающего списка с группами Facebook на основе данных, хранящихся в JSON-файле. Этот модуль облегчает выбор целевой группы для размещения рекламы.

## Подробней

Этот модуль предоставляет класс `FacebookGroupsWidget`, который инициализируется путем загрузки данных о группах из JSON-файла. Данные о группах затем используются для создания виджета `Dropdown` (выпадающий список), отображающего URL групп Facebook.  Модуль использует `j_loads_ns` для чтения JSON-файла, что позволяет избежать стандартных проблем с обработкой файлов и обеспечивает удобный доступ к данным.

## Классы

### `FacebookGroupsWidget`

**Описание**: Класс для создания и отображения выпадающего списка групп Facebook.

**Методы**:
- `__init__`: Инициализирует виджет, загружает данные о группах из JSON-файла и создает выпадающий список.
- `create_dropdown`: Создает виджет выпадающего списка на основе данных групп.
- `display_widget`: Отображает виджет выпадающего списка.

**Параметры**:
- `json_file_path` (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.

**Примеры**

```python
from pathlib import Path
from src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

# Предположим, что 'groups.json' содержит данные о группах Facebook
json_file_path = Path('groups.json')
widget = FacebookGroupsWidget(json_file_path)
widget.display_widget()
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

### `display_widget`

```python
def display_widget(self):
    """
    """
```

**Описание**: Отображает виджет выпадающего списка.