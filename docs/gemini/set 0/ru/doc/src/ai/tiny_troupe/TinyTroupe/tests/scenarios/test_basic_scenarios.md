# Модуль `test_basic_scenarios.py`

## Обзор

Этот модуль содержит тесты сценариев для базовой функциональности библиотеки `tinytroupe`.  Тесты проверяют запуск, приостановку и завершение симуляции, а также создание и работу с агентами.

## Функции

### `test_scenario_1`

**Описание**: Тестирует базовый сценарий работы с симуляцией. Проверяет начальное состояние симуляции, запуск, создание агента,  запись точек останова и завершение.

**Вызывает исключения**:
- Возможные исключения (в зависимости от результата проверки).


**Описание Действий**:
1. Сбрасывает текущую симуляцию (control.reset()).
2. Проверяет, что текущая симуляция равна None.
3. Запускает симуляцию (control.begin()).
4. Проверяет, что статус симуляции соответствует Simulation.STATUS_STARTED.
5. Создает агента типа "Oscar the Architect" (create_oscar_the_architect()).
6. Устанавливает значения атрибутов агента: "age" и "nationality".
7. Проверяет, что симуляция имеет записанный трек событий (cached_trace) и трек выполнения (execution_trace).
8. Создаёт контрольные точки (checkpoint()).
9. Запускает действие агента (agent.listen_and_act()).
10. Устанавливает значение атрибута агента: "occupation".
11. Создаёт контрольные точки (checkpoint()).
12. Завершает симуляцию (control.end()).

**Примечание**:  В тесте присутствуют комментарии "TODO check file creation"  — необходимо добавить проверки на создание файлов, соответствующих контрольным точкам.
```