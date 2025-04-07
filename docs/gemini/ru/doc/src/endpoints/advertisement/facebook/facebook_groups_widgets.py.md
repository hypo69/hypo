# Модуль для создания виджета с группами Facebook
## Обзор

Модуль `facebook_groups_widgets.py` предназначен для создания интерактивного выпадающего списка, содержащего URL-адреса групп Facebook. Он использует библиотеку `ipywidgets` для создания этого виджета, что позволяет пользователям выбирать группы для дальнейших действий, например, для размещения рекламы.

## Подробней

Этот модуль упрощает выбор групп Facebook, предоставляя удобный графический интерфейс. Он загружает данные о группах из JSON-файла и отображает их в виде выпадающего списка. Это позволяет избежать ручного ввода URL-адресов групп и снижает вероятность ошибок.

## Классы

### `FacebookGroupsWidget`

**Описание**: Класс `FacebookGroupsWidget` создает виджет выпадающего списка с URL групп Facebook из предоставленного JSON-файла.

**Принцип работы**:
1.  При инициализации класса загружаются данные о группах из JSON-файла, указанного в `json_file_path`. Для этого используется функция `j_loads_ns`, которая преобразует JSON в пространство имен (`SimpleNamespace`).
2.  Создается выпадающий список (`Dropdown`) на основе ключей, извлеченных из данных о группах.
3.  Виджет отображается с помощью функции `display_widget`, что делает его доступным для взаимодействия в интерфейсе пользователя.

**Аттрибуты**:

*   `groups_data` (SimpleNamespace): Пространство имен, содержащее данные о группах Facebook, загруженные из JSON-файла.
*   `dropdown` (Dropdown): Виджет выпадающего списка с URL групп Facebook.

**Методы**:

*   `__init__(self, json_file_path: Path)`: Инициализирует виджет, загружает данные о группах и создает выпадающий список.
*   `create_dropdown(self) -> Dropdown`: Создает виджет выпадающего списка на основе данных групп.
*   `display_widget(self)`: Отображает виджет выпадающего списка.

### `__init__`

```python
    def __init__(self, json_file_path: Path):
        """
        Инициализация виджета с выпадающим списком для групп Facebook.

        Args:
            json_file_path (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.
        """
        self.groups_data: SimpleNamespace = j_loads_ns(json_file_path)
        self.dropdown = self.create_dropdown()
```

**Назначение**: Инициализирует экземпляр класса `FacebookGroupsWidget`, загружая данные о группах Facebook из JSON-файла и создавая на основе этих данных выпадающий список.

**Параметры**:

*   `json_file_path` (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.

**Как работает функция**:

1.  Загружает данные о группах Facebook из JSON-файла, используя функцию `j_loads_ns`, которая преобразует содержимое JSON-файла в объект `SimpleNamespace`. Это позволяет обращаться к данным как к атрибутам объекта.
2.  Создает виджет выпадающего списка, вызывая метод `create_dropdown`, который формирует список опций на основе загруженных данных о группах.
3.  Сохраняет ссылку на созданный виджет в атрибуте `self.dropdown` для дальнейшего использования.

**Примеры**:

```python
from pathlib import Path
# Пример использования
widget = FacebookGroupsWidget(Path('path/to/your/groups.json'))
```

### `create_dropdown`

```python
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
```

**Назначение**: Создает и настраивает виджет выпадающего списка (`Dropdown`) на основе данных о группах Facebook, загруженных из JSON-файла.

**Возвращает**:

*   `Dropdown`: Виджет выпадающего списка с URL-адресами групп Facebook.

**Как работает функция**:

1.  Извлекает ключи (URL-адреса групп) из атрибута `__dict__` объекта `self.groups_data`, который содержит данные, загруженные из JSON-файла.
2.  Создает экземпляр класса `Dropdown` из библиотеки `ipywidgets`, передавая ему список URL-адресов групп в качестве опций.
3.  Устанавливает описание виджета как "Facebook Groups:" для улучшения читаемости в пользовательском интерфейсе.
4.  Устанавливает свойство `disabled` в `False`, чтобы виджет был активен и доступен для выбора.
5.  Возвращает созданный виджет выпадающего списка.

**Примеры**:

```python
from pathlib import Path
from ipywidgets import Dropdown

# Пример использования
widget = FacebookGroupsWidget(Path('path/to/your/groups.json'))
dropdown = widget.create_dropdown()
display(dropdown)
```

### `display_widget`

```python
    def display_widget(self):
        """ Отображает виджет выпадающего списка."""
        display(self.dropdown)
```

**Назначение**: Отображает виджет выпадающего списка, созданный методом `create_dropdown`, в интерфейсе пользователя.

**Как работает функция**:

1.  Использует функцию `display` из библиотеки `IPython.display` для отображения виджета `self.dropdown`.

**Примеры**:

```python
from pathlib import Path

# Пример использования
widget = FacebookGroupsWidget(Path('path/to/your/groups.json'))
widget.display_widget()