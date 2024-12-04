# Модуль `hypotez/src/endpoints/advertisement/facebook/facebook_groups_widgets.py`

## Обзор

Данный модуль предоставляет класс `FacebookGroupsWidget` для создания и отображения выпадающего списка с URL групп Facebook. Список загружается из JSON-файла.

## Оглавление

- [Модуль `facebook_groups_widgets`](#модуль-facebook_groups_widgets)
- [Класс `FacebookGroupsWidget`](#класс-facebookgroupswidget)
  - [Метод `__init__`](#метод-init)
  - [Метод `create_dropdown`](#метод-createdropdown)
  - [Метод `display_widget`](#метод-displaywidget)

## Класс `FacebookGroupsWidget`

**Описание**: Создает выпадающий список с URL групп Facebook из предоставленного JSON-файла.

### Метод `__init__`

**Описание**: Инициализация виджета с выпадающим списком для групп Facebook.

**Параметры**:

- `json_file_path` (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.

**Возвращает**:

-  Не имеет возвращаемого значения.

### Метод `create_dropdown`

**Описание**: Создает и возвращает виджет выпадающего списка на основе данных групп.

**Параметры**:

- Нет

**Возвращает**:

- `Dropdown`: Виджет выпадающего списка с URL групп Facebook.


### Метод `display_widget`

**Описание**: Отображает виджет выпадающего списка.

**Параметры**:

- Нет

**Возвращает**:

- Не имеет возвращаемого значения.