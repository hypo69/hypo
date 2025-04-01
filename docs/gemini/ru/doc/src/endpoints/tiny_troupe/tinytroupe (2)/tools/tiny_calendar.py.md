# Модуль `tiny_calendar.py`

## Обзор

Модуль предоставляет класс `TinyCalendar`, который является инструментом для управления календарем агентов. Он позволяет агентам отслеживать встречи и события.

## Подробнее

Этот модуль предназначен для интеграции в систему агентов `tinytroupe`. Он обеспечивает возможность создания, поиска и управления событиями в календаре агента.

## Классы

### `TinyCalendar`

**Описание**: Класс `TinyCalendar` предоставляет функциональность календаря для агентов, позволяя им создавать и отслеживать события.

**Наследует**:
- `TinyTool`: Класс `TinyCalendar` наследует функциональность от класса `TinyTool`, что позволяет интегрировать его в систему инструментов агентов.

**Атрибуты**:
- `calenar (dict)`: Словарь, где ключами являются даты, а значениями - списки событий. Каждое событие представлено в виде словаря с ключами: "title", "description", "owner", "mandatory_attendees", "optional_attendees", "start_time", "end_time".

**Методы**:
- `__init__(self, owner=None)`: Инициализирует экземпляр класса `TinyCalendar`.
- `add_event(self, date, title, description=None, owner=None, mandatory_attendees=None, optional_attendees=None, start_time=None, end_time=None)`: Добавляет событие в календарь.
- `find_events(self, year, month, day, hour=None, minute=None)`: Ищет события в календаре.
- `_process_action(self, agent, action) -> bool`: Обрабатывает действия агента, связанные с календарем.
- `actions_definitions_prompt(self) -> str`: Возвращает prompt с определениями действий, которые может выполнять агент с календарем.
- `actions_constraints_prompt(self) -> str`: Возвращает prompt с ограничениями на действия, которые может выполнять агент с календарем.

### `__init__`

```python
def __init__(self, owner=None):
    """
    Инициализирует экземпляр класса `TinyCalendar`.

    Args:
        owner (Any, optional): Владелец календаря. По умолчанию `None`.

    Returns:
        None

    """
    ...
```
**Назначение**:
Инициализирует экземпляр класса `TinyCalendar`, вызывая конструктор родительского класса `TinyTool` и устанавливая атрибут `calenar` как пустой словарь.

**Как работает функция**:
1. Вызывается конструктор родительского класса `TinyTool` с передачей имени "calendar", описания, владельца и флага `real_world_side_effects=False`.
2. Инициализируется атрибут `self.calenar` как пустой словарь.

**Примеры**:
```python
calendar = TinyCalendar(owner="Agent1")
```

### `add_event`

```python
def add_event(self, date, title, description=None, owner=None, mandatory_attendees=None, optional_attendees=None, start_time=None, end_time=None):
    """
    Добавляет событие в календарь.

    Args:
        date (Any): Дата события.
        title (Any): Название события.
        description (Any, optional): Описание события. По умолчанию `None`.
        owner (Any, optional): Владелец события. По умолчанию `None`.
        mandatory_attendees (Any, optional): Список обязательных участников. По умолчанию `None`.
        optional_attendees (Any, optional): Список необязательных участников. По умолчанию `None`.
        start_time (Any, optional): Время начала события. По умолчанию `None`.
        end_time (Any, optional): Время окончания события. По умолчанию `None`.

    Returns:
        None

    """
    ...
```
**Назначение**:
Добавляет новое событие в календарь для указанной даты.

**Как работает функция**:
1. Проверяет, существует ли уже запись для указанной даты в словаре `self.calendar`.
2. Если даты нет в словаре, создает новую запись для этой даты в виде списка.
3. Добавляет словарь, представляющий событие, в список событий для указанной даты.

**Примеры**:
```python
calendar.add_event(date="2024-01-01", title="New Year", description="New Year celebration")
```

### `find_events`

```python
def find_events(self, year, month, day, hour=None, minute=None):
    """
    Ищет события в календаре.

    Args:
        year (Any): Год.
        month (Any): Месяц.
        day (Any): День.
        hour (Any, optional): Час. По умолчанию `None`.
        minute (Any, optional): Минута. По умолчанию `None`.

    Returns:
        None

    """
    ...
```
**Назначение**:
Поиск событий в календаре по указанным параметрам даты и времени.

**Как работает функция**:
Функция в данный момент не реализована (`pass`).

### `_process_action`

```python
def _process_action(self, agent, action) -> bool:
    """
    Обрабатывает действия агента, связанные с календарем.

    Args:
        agent (Any): Агент, выполняющий действие.
        action (dict): Словарь, представляющий действие.

    Returns:
        bool: `True`, если действие успешно обработано, `False` в противном случае.

    """
    ...
```
**Назначение**:
Обрабатывает действия агента, связанные с календарем, такие как создание события.

**Как работает функция**:
1. Проверяет, является ли тип действия "CREATE_EVENT" и не является ли содержимое действия `None`.
2. Если условие выполняется, пытается распарсить содержимое действия как JSON.
3. Проверяет, содержит ли распарсенный JSON допустимые ключи, используя функцию `utils.check_valid_fields`.
4. Использует полученные данные для создания нового события с помощью метода `self.add_event`.
5. Возвращает `True`, если действие успешно обработано.
6. В противном случае возвращает `False`.

**Примеры**:
```python
action = {'type': 'CREATE_EVENT', 'content': '{"title": "Meeting", "description": "Discuss project progress"}'}
result = calendar._process_action(agent="Agent1", action=action)
```

### `actions_definitions_prompt`

```python
def actions_definitions_prompt(self) -> str:
    """
    Возвращает prompt с определениями действий, которые может выполнять агент с календарем.

    Returns:
        str: Строка с определениями действий.

    """
    ...
```
**Назначение**:
Формирует и возвращает текстовое описание доступных действий для агента, связанных с управлением календарем.

**Как работает функция**:
1. Определяет строку `prompt`, содержащую описание действия "CREATE_EVENT" и его параметров в формате JSON.
2. Использует функцию `utils.dedent` для удаления лишних отступов в строке `prompt`.
3. Возвращает отформатированную строку `prompt`.

**Примеры**:
```python
prompt = calendar.actions_definitions_prompt()
print(prompt)
```

### `actions_constraints_prompt`

```python
def actions_constraints_prompt(self) -> str:
    """
    Возвращает prompt с ограничениями на действия, которые может выполнять агент с календарем.

    Returns:
        str: Строка с ограничениями на действия.

    """
    ...
```

**Назначение**:
Формирует и возвращает текстовое описание ограничений, накладываемых на действия агента при работе с календарем.

**Как работает функция**:
Функция в данный момент возвращает пустую строку, так как ограничения не определены (`pass`).

## Функции
В данном модуле функции отсутствуют.