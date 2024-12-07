# Модуль `test_control.py`

## Обзор

Данный модуль содержит тесты для класса `Simulation` и связанных с ним функций в модуле `tinytroupe.control`. Тесты проверяют корректное начало, сохранение контрольных точек (checkpoint) и завершение симуляций с различными объектами (агентами, миром, фабрикой).

## Функции

### `test_begin_checkpoint_end_with_agent_only`

**Описание**: Тестирует цикл `begin`, `checkpoint`, `end` для симуляции, в которой участвуют только агенты.

**Параметры**:
- `setup` (объект): Предполагается, что этот параметр обеспечивает необходимые настройки для запуска тестов (например, создание необходимых объектов, инициализация переменных).


**Возвращает**:
-  None

**Вызывает исключения**:
-  Никаких исключений не ожидается.


### `test_begin_checkpoint_end_with_world`

**Описание**: Тестирует цикл `begin`, `checkpoint`, `end` для симуляции, в которой используется `TinyWorld`.

**Параметры**:
- `setup` (объект): Предполагается, что этот параметр обеспечивает необходимые настройки для запуска тестов (например, создание необходимых объектов, инициализация переменных).

**Возвращает**:
-  None

**Вызывает исключения**:
-  Никаких исключений не ожидается.


### `test_begin_checkpoint_end_with_factory`

**Описание**: Тестирует цикл `begin`, `checkpoint`, `end` для симуляции, в которой используется `TinyPersonFactory`.  Тест выполняется дважды, чтобы проверить согласованность результатов.

**Параметры**:
- `setup` (объект): Предполагается, что этот параметр обеспечивает необходимые настройки для запуска тестов (например, создание необходимых объектов, инициализация переменных).
- `iteration` (int): Номер итерации текущей симуляции.
- `verbose` (bool, optional): Флаг для включения/выключения подробной логирования. По умолчанию `False`.

**Возвращает**:
- `TinyPerson`: Объект агента, созданный в ходе симуляции.


**Вызывает исключения**:
-  Никаких исключений не ожидается.

**Примечания**: Функция `aux_simulation_to_repeat` выполняет повторяющиеся этапы симуляции с `TinyPersonFactory`, позволяя вызывать симуляцию для разных входных данных и проверки стабильности поведения.