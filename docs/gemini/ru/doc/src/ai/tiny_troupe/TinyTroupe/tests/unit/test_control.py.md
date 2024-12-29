# Документация модуля `test_control.py`

## Обзор

Этот модуль содержит набор тестов для проверки функциональности управления симуляциями в `tinytroupe`. Он включает тесты для начала, создания контрольных точек и завершения симуляций с использованием агентов, мира и фабрики персонажей.

## Оглавление

- [Функции](#Функции)
    - [test_begin_checkpoint_end_with_agent_only](#test_begin_checkpoint_end_with_agent_only)
    - [test_begin_checkpoint_end_with_world](#test_begin_checkpoint_end_with_world)
    - [test_begin_checkpoint_end_with_factory](#test_begin_checkpoint_end_with_factory)
    - [aux_simulation_to_repeat](#aux_simulation_to_repeat)

## Функции

### `test_begin_checkpoint_end_with_agent_only`

**Описание**: Тестирует начало, создание контрольной точки и завершение симуляции с использованием только агентов.

**Параметры**:
- `setup`: Фикстура pytest для настройки тестового окружения.

**Возвращает**:
- `None`: Функция ничего не возвращает.

### `test_begin_checkpoint_end_with_world`

**Описание**: Тестирует начало, создание контрольной точки и завершение симуляции с использованием мира (`TinyWorld`).

**Параметры**:
- `setup`: Фикстура pytest для настройки тестового окружения.

**Возвращает**:
- `None`: Функция ничего не возвращает.

### `test_begin_checkpoint_end_with_factory`

**Описание**: Тестирует начало, создание контрольной точки и завершение симуляции с использованием фабрики персонажей (`TinyPersonFactory`).

**Параметры**:
- `setup`: Фикстура pytest для настройки тестового окружения.

**Возвращает**:
- `None`: Функция ничего не возвращает.

### `aux_simulation_to_repeat`

**Описание**: Вспомогательная функция для повторения симуляции с использованием `TinyPersonFactory`.

**Параметры**:
- `iteration` (int): Номер итерации симуляции.
- `verbose` (bool, optional): Флаг для включения подробного вывода в лог. По умолчанию `False`.

**Возвращает**:
- `agent` (TinyPerson): Возвращает созданного агента.