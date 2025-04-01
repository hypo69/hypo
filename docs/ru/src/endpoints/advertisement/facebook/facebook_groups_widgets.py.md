# Модуль для создания виджета выбора групп Facebook

## Обзор

Модуль `facebook_groups_widgets.py` предназначен для создания интерактивного виджета в виде выпадающего списка, который позволяет пользователю выбирать группы Facebook из предварительно загруженного JSON-файла. Это может быть полезно для автоматизации процессов, связанных с размещением контента в различных группах Facebook.

## Подробнее

Модуль предоставляет класс `FacebookGroupsWidget`, который инициализируется путем указания пути к JSON-файлу, содержащему информацию о группах Facebook (например, их URL). Класс создает выпадающий список (`Dropdown`) с названиями групп, позволяя пользователю выбрать нужную группу. Виджет отображается с использованием функции `display` из библиотеки `IPython.display`.

## Классы

### `FacebookGroupsWidget`

**Описание**: Класс `FacebookGroupsWidget` создает выпадающий список с URL групп Facebook на основе данных из JSON-файла.

**Принцип работы**:

1.  При инициализации класса считывается JSON-файл, содержащий информацию о группах Facebook.
2.  Создается выпадающий список (`Dropdown`) с названиями групп, извлеченными из JSON-данных.
3.  Виджет отображается для взаимодействия с пользователем.

**Атрибуты**:

*   `groups_data` (SimpleNamespace): Объект, содержащий данные о группах Facebook, загруженные из JSON-файла.
*   `dropdown` (Dropdown): Виджет выпадающего списка с URL групп Facebook.

**Методы**:

*   `__init__(self, json_file_path: Path)`: Инициализирует виджет, загружает данные о группах из JSON-файла и создает выпадающий список.
*   `create_dropdown(self) -> Dropdown`: Создает и возвращает виджет выпадающего списка на основе данных групп.
*   `display_widget(self)`: Отображает виджет выпадающего списка.

### `__init__`

```python
 def __init__(self, json_file_path: Path):
    """
    Инициализация виджета с выпадающим списком для групп Facebook.

    Args:
        json_file_path (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.
    """
    ...
```

**Назначение**: Инициализирует виджет `FacebookGroupsWidget`, загружая данные о группах Facebook из JSON-файла и создавая выпадающий список.

**Параметры**:

*   `json_file_path` (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.

**Как работает функция**:

1.  Загружает данные из JSON-файла, используя функцию `j_loads_ns`, и сохраняет их в атрибуте `self.groups_data`.
2.  Вызывает метод `self.create_dropdown()` для создания виджета выпадающего списка.

**Примеры**:

```python
from pathlib import Path
# from src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget
# Путь к JSON файлу с данными о группах
json_file_path = Path('./groups_data.json')

# Создание экземпляра виджета
widget = FacebookGroupsWidget(json_file_path)
```

### `create_dropdown`

```python
 def create_dropdown(self) -> Dropdown:
    """ Создает и возвращает виджет выпадающего списка на основе данных групп.

    Returns:
        Dropdown: Виджет выпадающего списка с URL групп Facebook.
    """
    ...
```

**Назначение**: Создает и возвращает виджет выпадающего списка (`Dropdown`) на основе данных о группах Facebook, загруженных из JSON-файла.

**Возвращает**:

*   `Dropdown`: Виджет выпадающего списка с URL групп Facebook.

**Как работает функция**:

1.  Извлекает ключи (названия групп) из атрибута `self.groups_data.__dict__` и преобразует их в список.
2.  Создает экземпляр класса `Dropdown` из библиотеки `ipywidgets`, передавая список названий групп в качестве опций (`options`).
3.  Устанавливает описание (`description`) для выпадающего списка как "Facebook Groups:".
4.  Возвращает созданный виджет выпадающего списка.

**Примеры**:

```python
from pathlib import Path
from ipywidgets import Dropdown
# from src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

# Путь к JSON файлу с данными о группах
json_file_path = Path('./groups_data.json')

# Создание экземпляра виджета
widget = FacebookGroupsWidget(json_file_path)

# Получение виджета выпадающего списка
dropdown_widget = widget.create_dropdown()
assert isinstance(dropdown_widget, Dropdown)
```

### `display_widget`

```python
 def display_widget(self):
    """ Отображает виджет выпадающего списка."""
    ...
```

**Назначение**: Отображает виджет выпадающего списка, созданный методом `create_dropdown`.

**Как работает функция**:

1.  Использует функцию `display` из библиотеки `IPython.display` для отображения виджета `self.dropdown`.

**Примеры**:

```python
from pathlib import Path
# from src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

# Путь к JSON файлу с данными о группах
json_file_path = Path('./groups_data.json')

# Создание экземпляра виджета
widget = FacebookGroupsWidget(json_file_path)

# Отображение виджета
widget.display_widget()