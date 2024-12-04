# Модуль tinytroupe.tools

## Обзор

Этот модуль предоставляет инструменты для агентов, позволяющие им выполнять специализированные задачи.  Он содержит классы для создания и управления инструментами, включая обработку действий, проверку владения, вывод подсказок для определения и ограничений действий.  Модуль включает в себя примеры инструментов, таких как `TinyCalendar` и `TinyWordProcessor`.

## Оглавление

* [TinyTool](#tinytool)
* [TinyCalendar](#tinycalendar)
* [TinyWordProcessor](#tinywordprocessor)

## Классы

### `TinyTool`

**Описание**: Базовый класс для инструментов.  Представляет собой инструмент, который может выполнять специализированные действия.  Этот класс отвечает за базовые проверки, такие как проверка наличия побочных эффектов в реальном мире и владения агентом инструментом.

**Атрибуты**:
- `name` (str): Имя инструмента.
- `description` (str): Краткое описание инструмента.
- `owner` (str): Агент, владеющий инструментом. Если `None`, инструмент может использоваться любым агентом.
- `real_world_side_effects` (bool): Признак наличия реальных побочных эффектов в инструменте.
- `exporter` (ArtifactExporter): Экспортер результатов действий инструмента. Может быть `None`.
- `enricher` (Enricher): Инструмент обогащения результатов. Может быть `None`.


**Методы**:
- `__init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None)`: Инициализирует новый инструмент.
    - `name` (str): Имя инструмента.
    - `description` (str): Краткое описание инструмента.
    - `owner` (str): Агент, владеющий инструментом.
    - `real_world_side_effects` (bool): Признак наличия реальных побочных эффектов в инструменте.
    - `exporter` (ArtifactExporter): Экспортер результатов действий инструмента.
    - `enricher` (Enricher): Инструмент обогащения результатов.
- `_process_action(self, agent, action: dict) -> bool`: Обрабатывает действие.  Должен быть реализован подклассами.
- `_protect_real_world(self)`: Выводит предупреждение, если инструмент имеет реальные побочные эффекты.
- `_enforce_ownership(self, agent)`: Проверяет владение агента инструментом.
- `set_owner(self, owner)`: Устанавливает владельца инструмента.
- `actions_definitions_prompt(self) -> str`: Возвращает подсказку для определения действий. Должен быть реализован подклассами.
- `actions_constraints_prompt(self) -> str`: Возвращает подсказку с ограничениями для действий. Должен быть реализован подклассами.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, используя `_process_action` и выполняя проверки.


### `TinyCalendar`

**Описание**: Инструмент для работы с календарем.  Позволяет агентам отслеживать встречи и назначения.

**Атрибуты**:
- `calenar` (dict): Словарь, хранящий события в календаре.


**Методы**:
- `__init__(self, owner=None)`: Инициализирует инструмент календаря.
- `add_event(self, date, title, description=None, owner=None, mandatory_attendees=None, optional_attendees=None, start_time=None, end_time=None)`: Добавляет событие в календарь.
- `find_events(self, year, month, day, hour=None, minute=None)`: Находит события в указанную дату и время.
- `_process_action(self, agent, action) -> bool`: Обрабатывает действия для создания событий.
- `actions_definitions_prompt(self) -> str`: Возвращает подсказку для определения действий.
- `actions_constraints_prompt(self) -> str`: Возвращает подсказку с ограничениями для действий.


### `TinyWordProcessor`

**Описание**: Инструмент текстового процессора. Позволяет агентам создавать документы.


**Атрибуты**:
-  `exporter`: Инструмент экспорта документации.
-  `enricher`: Инструмент обогащения документации.


**Методы**:
- `__init__(self, owner=None, exporter=None, enricher=None)`: Инициализирует инструмент.
- `write_document(self, title, content, author=None)`: Создает документ.
    -  `title` (str): Заголовок документа.
    - `content` (str): Содержимое документа.
    - `author` (str, optional): Автор документа.
- `_process_action(self, agent, action) -> bool`: Обрабатывает действие для создания документа.
- `actions_definitions_prompt(self) -> str`: Возвращает подсказку для определения действий.
- `actions_constraints_prompt(self) -> str`: Возвращает подсказку с ограничениями для действий.