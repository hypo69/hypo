# `test_basic_scenarios.py`

## Обзор

Этот файл содержит набор тестов для основных сценариев работы `tinytroupe`. Он проверяет корректность запуска, остановки и сохранения данных симуляции, а также базовое взаимодействие с агентом.

## Оглавление

- [Функции](#Функции)
    - [`test_scenario_1`](#test_scenario_1)

## Функции

### `test_scenario_1`

**Описание**: Тестирует базовый сценарий симуляции с одним агентом, проверяя запуск, остановку, создание контрольных точек и базовые действия агента.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.
    
**Вызывает исключения**:
- Нет исключений.
    
```python
def test_scenario_1():
    control.reset()

    assert control._current_simulations["default"] is None, "There should be no simulation running at this point."

    control.begin()
    assert control._current_simulations["default"].status == Simulation.STATUS_STARTED, "The simulation should be started at this point."

    agent = create_oscar_the_architect()

    agent.define("age", 19)
    agent.define("nationality", "Brazilian")

    assert control._current_simulations["default"].cached_trace is not None, "There should be a cached trace at this point."
    assert control._current_simulations["default"].execution_trace is not None, "There should be an execution trace at this point."

    control.checkpoint()
    # TODO check file creation

    agent.listen_and_act("How are you doing?")
    agent.define("occupation", "Engineer")

    control.checkpoint()
    # TODO check file creation

    control.end()
```