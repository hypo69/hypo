# Модуль `facebook_groups_widgets.py`

## Обзор

Модуль `facebook_groups_widgets.py` предназначен для создания интерактивного виджета - выпадающего списка групп Facebook. Этот виджет позволяет пользователю выбирать группы Facebook из списка, полученного из JSON-файла. Модуль использует библиотеки `ipywidgets` для создания виджета и `src.utils.jjson` для загрузки данных из JSON-файла в объект `SimpleNamespace`.

## Подробней

Этот модуль предоставляет класс `FacebookGroupsWidget`, который инициализируется путем указания пути к JSON-файлу, содержащему информацию о группах Facebook. JSON-файл должен содержать структуру, где ключи - это URL групп. Класс создает выпадающий список (`Dropdown`) с этими URL в качестве опций.

Виджет отображается с использованием функции `display` из библиотеки `IPython.display`. Это позволяет использовать виджет в интерактивных средах, таких как Jupyter Notebook.

## Классы

### `FacebookGroupsWidget`

**Описание**: Класс для создания и отображения выпадающего списка групп Facebook.

**Принцип работы**:
1.  При инициализации класса `FacebookGroupsWidget` происходит загрузка данных о группах Facebook из JSON-файла с использованием функции `j_loads_ns` из модуля `src.utils.jjson`. Данные сохраняются в атрибуте `groups_data` в виде объекта `SimpleNamespace`.
2.  Создается выпадающий список с использованием метода `create_dropdown`, который извлекает URL групп из `groups_data` и создает виджет `Dropdown` с этими URL в качестве опций.
3.  Виджет отображается с помощью метода `display_widget`, который использует функцию `display` из библиотеки `IPython.display`.

**Атрибуты**:

*   `groups_data` (SimpleNamespace): Объект, содержащий данные о группах Facebook, загруженные из JSON-файла.
*   `dropdown` (Dropdown): Виджет выпадающего списка (`Dropdown`) с URL групп Facebook.

**Методы**:

*   `__init__(self, json_file_path: Path)`: Инициализирует экземпляр класса `FacebookGroupsWidget`.
*   `create_dropdown(self) -> Dropdown`: Создает и возвращает виджет выпадающего списка на основе данных о группах.
*   `display_widget(self)`: Отображает виджет выпадающего списка.

### `__init__(self, json_file_path: Path)`

```python
def __init__(self, json_file_path: Path):
    """
    Инициализация виджета с выпадающим списком для групп Facebook.

    Args:
        json_file_path (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.
    """
    ...
```

**Назначение**: Инициализирует виджет `FacebookGroupsWidget`, загружая данные из JSON-файла и создавая выпадающий список.

**Параметры**:

*   `json_file_path` (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.

**Как работает функция**:

1.  Загружает данные о группах Facebook из JSON-файла, используя функцию `j_loads_ns` из модуля `src.utils.jjson`.
2.  Сохраняет загруженные данные в атрибуте `groups_data` в виде объекта `SimpleNamespace`.
3.  Создает выпадающий список, вызывая метод `create_dropdown`.
    ```
    A: Загрузка данных из JSON
    |
    B: Сохранение данных в groups_data
    |
    C: Создание выпадающего списка
    ```

**Примеры**:

```python
from pathlib import Path
file_path = Path('groups.json')  # Предполагается, что файл groups.json существует
widget = FacebookGroupsWidget(file_path)
```

### `create_dropdown(self) -> Dropdown`

```python
def create_dropdown(self) -> Dropdown:
    """ Создает и возвращает виджет выпадающего списка на основе данных групп.

    Returns:
        Dropdown: Виджет выпадающего списка с URL групп Facebook.
    """
    ...
```

**Назначение**: Создает и возвращает виджет выпадающего списка (`Dropdown`) на основе данных о группах Facebook.

**Возвращает**:

*   `Dropdown`: Виджет выпадающего списка с URL групп Facebook.

**Как работает функция**:

1.  Извлекает URL групп из атрибута `groups_data`.
2.  Создает виджет `Dropdown` из библиотеки `ipywidgets`, используя URL групп в качестве опций.
3.  Устанавливает описание виджета как "Facebook Groups:".
4.  Возвращает созданный виджет `Dropdown`.

```
A: Извлечение URL групп
|
B: Создание виджета Dropdown
|
C: Установка описания виджета
|
D: Возврат виджета Dropdown
```

**Примеры**:

```python
from pathlib import Path
file_path = Path('groups.json')
widget = FacebookGroupsWidget(file_path)
dropdown = widget.create_dropdown()
```

### `display_widget(self)`

```python
def display_widget(self):
    """ Отображает виджет выпадающего списка."""
    ...
```

**Назначение**: Отображает виджет выпадающего списка (`Dropdown`).

**Как работает функция**:

1.  Использует функцию `display` из библиотеки `IPython.display` для отображения виджета `dropdown`.

```
A: Отображение виджета Dropdown
```

**Примеры**:

```python
from pathlib import Path
file_path = Path('groups.json')
widget = FacebookGroupsWidget(file_path)
widget.display_widget()
```

## Функции

В данном модуле функции отсутствуют.