# Модуль tinytroupe.tools

## Обзор

Этот модуль предоставляет инструменты для агентов, позволяющие им выполнять специализированные задачи. Он определяет базовый класс `TinyTool` и его подклассы, такие как `TinyCalendar` и `TinyWordProcessor`, предоставляя функциональность для управления действиями агента. Классы позволяют контролировать реальные последствия действий, проверять права доступа и предоставляют подсказки для определения и ограничения действий.

## Классы

### `TinyTool`

**Описание**: Базовый класс для инструментов. Определяет общие методы и свойства для всех инструментов.

**Методы**:

- `__init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None)`: Инициализирует новый инструмент.
    - **Параметры**:
        - `name` (str): Название инструмента.
        - `description` (str): Краткое описание инструмента.
        - `owner` (str): Агент, владеющий инструментом. Если None, инструмент может быть использован любым агентом.
        - `real_world_side_effects` (bool): Указывает, имеет ли инструмент реальные последствия в мире. Т.е., если он может изменить состояние мира за пределами симуляции. Если имеет, использовать с осторожностью.
        - `exporter` (ArtifactExporter): Экспортер, который может использоваться для экспорта результатов действий инструмента. Если None, инструмент не сможет экспортировать результаты.
        - `enricher` (Enricher): Инструмент обогащения, который может использоваться для обогащения результатов действий инструмента. Если None, инструмент не сможет обогащать результаты.
    - **Возвращает**:
        - None
- `_process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, которое производит инструмент.  Должно быть переопределено в подклассах.
- `_protect_real_world(self)`: Выводит предупреждение, если инструмент имеет реальные последствия.
- `_enforce_ownership(self, agent)`: Проверяет права доступа к инструменту.
- `set_owner(self, owner)`: Устанавливает владельца инструмента.
- `actions_definitions_prompt(self) -> str`: Возвращает подсказку для определения возможных действий. Должно быть переопределено в подклассах.
- `actions_constraints_prompt(self) -> str`: Возвращает подсказку для ограничений действий. Должно быть переопределено в подклассах.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, защищая от реальных последствий и проверяя права доступа.


### `TinyCalendar`

**Описание**: Инструмент для управления календарем.


**Методы**:

- `__init__(self, owner=None)`: Инициализирует новый календарь.
    - **Параметры**:
        - `owner` (str, опционально): Владелец календаря.
- `add_event(self, date, title, description=None, owner=None, mandatory_attendees=None, optional_attendees=None, start_time=None, end_time=None)`: Добавляет событие в календарь.
    - **Параметры**:
        - `date` (str): Дата события.
        - `title` (str): Заголовок события.
        - `description` (str, опционально): Описание события.
        - `owner` (str, опционально): Владелец события.
        - `mandatory_attendees` (list, опционально): Список обязательных участников.
        - `optional_attendees` (list, опционально): Список необязательных участников.
        - `start_time` (datetime, опционально): Время начала события.
        - `end_time` (datetime, опционально): Время окончания события.
- `find_events(self, year, month, day, hour=None, minute=None)`: Находит события по заданным критериям.
- `_process_action(self, agent, action) -> bool`: Обрабатывает действие создания события.
- `actions_definitions_prompt(self) -> str`: Предоставляет подсказку для создания события.
- `actions_constraints_prompt(self) -> str`: Предоставляет подсказку для ограничений действий.



### `TinyWordProcessor`

**Описание**: Инструмент для обработки текстовых документов.

**Методы**:

- `__init__(self, owner=None, exporter=None, enricher=None)`: Инициализирует новый инструмент обработки текста.
    - **Параметры**:
        - `owner` (str, опционально): Владелец инструмента.
        - `exporter` (ArtifactExporter, опционально): Экспортер.
        - `enricher` (Enricher, опционально): Инструмент обогащения.
- `write_document(self, title, content, author=None)`: Пишет документ.
    - **Параметры**:
        - `title` (str): Заголовок документа.
        - `content` (str): Содержимое документа.
        - `author` (str, опционально): Автор документа.
- `_process_action(self, agent, action) -> bool`: Обрабатывает действие записи документа.
- `actions_definitions_prompt(self) -> str`: Предоставляет подсказку для определения действий.
- `actions_constraints_prompt(self) -> str`: Предоставляет подсказку для ограничений действий.


## Функции


```
```