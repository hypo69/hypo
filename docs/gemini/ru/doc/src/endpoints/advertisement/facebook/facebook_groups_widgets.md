# Модуль `hypotez/src/endpoints/advertisement/facebook/facebook_groups_widgets.py`

## Обзор

Модуль `facebook_groups_widgets.py` предоставляет класс `FacebookGroupsWidget`, который создает и отображает выпадающий список групп Facebook для выбора при подаче объявления.  Класс использует данные из JSON-файла, содержащего информацию о группах.

## Оглавление

- [Модуль `facebook_groups_widgets.py`](#модуль-facebook_groups_widgetspy)
- [Класс `FacebookGroupsWidget`](#класс-facebookgroupswidget)
    - [Метод `__init__`](#метод-init)
    - [Метод `create_dropdown`](#метод-create_dropdown)
    - [Метод `display_widget`](#метод-display_widget)

## Класс `FacebookGroupsWidget`

### Описание

Класс `FacebookGroupsWidget` создает выпадающий список с URL групп Facebook.  Он принимает путь к JSON-файлу, парсит его и формирует список доступных групп, после чего отображает виджет.

### Метод `__init__`

#### Описание

Инициализирует объект класса `FacebookGroupsWidget`.

#### Параметры

- `json_file_path` (Path): Путь к JSON-файлу, содержащему список URL групп Facebook.


### Метод `create_dropdown`

#### Описание

Создает и возвращает виджет выпадающего списка `Dropdown` на основе данных из JSON-файла.

#### Возвращает

- Dropdown: Виджет выпадающего списка с URL групп Facebook.


### Метод `display_widget`

#### Описание

Отображает созданный виджет выпадающего списка.