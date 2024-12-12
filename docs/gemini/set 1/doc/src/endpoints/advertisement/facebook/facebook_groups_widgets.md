# Модуль `hypotez/src/endpoints/advertisement/facebook/facebook_groups_widgets.py`

## Обзор

Этот модуль предоставляет класс `FacebookGroupsWidget` для создания и отображения выпадающего списка с URL групп Facebook.  Список загружается из JSON-файла.

## Оглавление

- [Модуль `facebook_groups_widgets.py`](#модуль-facebook_groups_widgetspy)
- [Класс `FacebookGroupsWidget`](#класс-facebookgroupswidget)
- [Метод `__init__`](#метод-init)
- [Метод `create_dropdown`](#метод-create_dropdown)
- [Метод `display_widget`](#метод-display_widget)


## Класс `FacebookGroupsWidget`

**Описание**:  Класс `FacebookGroupsWidget` создает виджет выпадающего списка, содержащий URL групп Facebook, загруженные из JSON-файла.

### Метод `__init__`

**Описание**: Инициализирует экземпляр класса `FacebookGroupsWidget`.

**Параметры**:

- `json_file_path` (Path): Путь к файлу JSON, содержащему информацию о группах Facebook.  

**Возвращает**:  
    Не возвращает значения.

### Метод `create_dropdown`

**Описание**: Создает и возвращает виджет `Dropdown` с URL групп Facebook.

**Параметры**:
    Нет параметров.

**Возвращает**:

- `Dropdown`: Виджет `Dropdown` с URL групп Facebook.


### Метод `display_widget`

**Описание**: Отображает созданный виджет `Dropdown`.

**Параметры**:
    Нет параметров.

**Возвращает**:
    Не возвращает значения.