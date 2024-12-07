# Модуль `test_basic_scenarios.py`

## Обзор

Данный модуль содержит тесты для базовых сценариев работы с TinyTroupe, включая инициализацию симуляции, создание агентов, определение их характеристик, взаимодействие с окружающей средой, сохранение контрольных точек и завершение симуляции.

## Функции

### `test_scenario_1`

**Описание**: Тестирует базовый сценарий симуляции. Проверяет, что симуляция начинается и завершается корректно, что агенты могут быть созданы и их характеристики определены, а также что сохраняются контрольные точки.


**Вызывает функции**:
- `control.reset()`
- `control.begin()`
- `control.checkpoint()`
- `control.end()`
- `create_oscar_the_architect()`
- `agent.define("age", 19)`
- `agent.define("nationality", "Brazilian")`
- `agent.listen_and_act("How are you doing?")`
- `agent.define("occupation", "Engineer")`


**Утверждения (assert)**:
- `control._current_simulations["default"] is None`: Проверяет, что перед началом симуляции нет активной симуляции.
- `control._current_simulations["default"].status == Simulation.STATUS_STARTED`: Проверяет, что симуляция успешно запущена.
- `control._current_simulations["default"].cached_trace is not None`: Проверяет, что есть кэшированный след (trace).
- `control._current_simulations["default"].execution_trace is not None`: Проверяет, что есть след выполнения (execution trace).

**Примечания**:
- В тесте присутствуют комментарии `# TODO check file creation`, что указывает на необходимость добавить проверку создания файлов, связанных с контрольными точками.
```