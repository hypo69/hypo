# Модуль facebook_groups_widgets.py

## Обзор

Модуль `facebook_groups_widgets.py` предоставляет класс `FacebookGroupsWidget` для создания и отображения выпадающего списка с URL-адресами групп Facebook.  Этот виджет используется для выбора группы при подаче объявления.

## Оглавление

* [Модуль facebook_groups_widgets.py](#модуль-facebook_groups_widgets-py)
* [Класс FacebookGroupsWidget](#класс-facebookgroupswidget)
    * [Метод __init__](#метод-init)
    * [Метод create_dropdown](#метод-create_dropdown)
    * [Метод display_widget](#метод-display_widget)

## Класс FacebookGroupsWidget

**Описание**:  Класс `FacebookGroupsWidget` создает и отображает выпадающий список групп Facebook. Он принимает JSON-файл с данными групп и формирует соответствующий виджет.

### Метод __init__

**Описание**: Инициализирует объект класса `FacebookGroupsWidget`.

**Параметры**:

* `json_file_path` (Path): Путь к файлу JSON, содержащему информацию о группах Facebook.

**Возвращает**:

*  (None): Не возвращает ничего.

### Метод create_dropdown

**Описание**: Создает и возвращает виджет `Dropdown` с URL-адресами групп Facebook.

**Параметры**:

* Нет

**Возвращает**:

* `Dropdown`: Виджет выпадающего списка с URL-адресами групп.

### Метод display_widget

**Описание**: Отображает созданный виджет `Dropdown` в Jupyter Notebook.

**Параметры**:

* Нет

**Возвращает**:

* (None): Не возвращает ничего.