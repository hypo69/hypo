# Модуль `hypotez/src/endpoints/advertisement/facebook/facebook_groups_widgets.py`

## Обзор

Модуль `facebook_groups_widgets.py` предоставляет класс `FacebookGroupsWidget`, предназначенный для создания и отображения виджета выпадающего списка с URL-адресами групп Facebook. Виджет создается на основе данных, загруженных из JSON-файла.

## Оглавление

* [Модуль `facebook_groups_widgets.py`](#модуль-facebook_groups_widgetspy)
* [Класс `FacebookGroupsWidget`](#класс-facebookgroupswidget)
    * [Метод `__init__`](#метод-init)
    * [Метод `create_dropdown`](#метод-createdropdown)
    * [Метод `display_widget`](#метод-displaywidget)


## Классы

### `FacebookGroupsWidget`

**Описание**: Класс `FacebookGroupsWidget` отвечает за создание и отображение виджета выпадающего списка с URL-адресами групп Facebook.

**Методы**:

#### `__init__`

**Описание**: Инициализирует виджет с выпадающим списком.

**Параметры**:

- `json_file_path` (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.

**Возвращает**:
-  Не возвращает ничего.

#### `create_dropdown`

**Описание**: Создает и возвращает виджет выпадающего списка на основе данных из JSON-файла.

**Параметры**:
-  Не принимает параметров.

**Возвращает**:
- `Dropdown`: Виджет выпадающего списка с URL-адресами групп Facebook.


#### `display_widget`

**Описание**: Отображает виджет выпадающего списка.

**Параметры**:
-  Не принимает параметров.

**Возвращает**:
-  Не возвращает ничего.


```
```python
MODE = 'dev'

import header
from IPython.display import display
from ipywidgets import Dropdown
from src.utils import j_loads_ns
from types import SimpleNamespace
from pathlib import Path
```

```python
class FacebookGroupsWidget:
    """ Создает выпадающий список с URL групп Facebook из предоставленного JSON."""

    def __init__(self, json_file_path: Path):
        """
        Инициализация виджета с выпадающим списком для групп Facebook.

        Args:
            json_file_path (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.
        """
        self.groups_data: SimpleNamespace = j_loads_ns(json_file_path)
        self.dropdown = self.create_dropdown()

    def create_dropdown(self) -> Dropdown:
        """ Создает и возвращает виджет выпадающего списка на основе данных групп.

        Returns:
            Dropdown: Виджет выпадающего списка с URL групп Facebook.
        """
        group_urls = list(self.groups_data.__dict__.keys())
        dropdown = Dropdown(
            options=group_urls,
            description='Facebook Groups:',
            disabled=False,
        )
        return dropdown

    def display_widget(self):
        """ Отображает виджет выпадающего списка."""
        display(self.dropdown)