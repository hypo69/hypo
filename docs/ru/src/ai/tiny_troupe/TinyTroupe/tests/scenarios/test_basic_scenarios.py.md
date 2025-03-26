# test_basic_scenarios.py

## Обзор

Этот файл содержит набор тестов для проверки основных сценариев работы библиотеки TinyTroupe. Он проверяет создание, запуск и остановку симуляций, а также основные операции с агентами, такие как определение и изменение их характеристик.

## Оглавление

- [Функции](#функции)
    - [`test_scenario_1`](#test_scenario_1)

## Функции

### `test_scenario_1`

**Описание**: Тестирует базовый сценарий симуляции: запуск, создание агента, определение его параметров, сохранение состояния и остановку симуляции.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет
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