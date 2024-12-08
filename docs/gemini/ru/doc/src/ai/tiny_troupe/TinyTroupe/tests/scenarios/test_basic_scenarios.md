# Модуль test_basic_scenarios

## Обзор

Этот модуль содержит тесты для базовых сценариев работы с TinyTroupe. Он проверяет корректность инициализации симуляции, добавление агентов, их действия и сохранение состояния.

## Функции

### `test_scenario_1`

**Описание**: Тестирует базовый сценарий работы с TinyTroupe.

**Описание сценария**: Функция проверяет, что симуляция начинается и завершается успешно, что агенты добавляются и могут взаимодействовать.  Проверяет сохранение состояния симуляции при использовании `checkpoint`.

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из ожидаемых условий не выполнены (например, симуляция не запущена, нет кэшированной трассы).


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
## Замечания

В данном коде присутствуют TODO, которые нуждаются в реализации.  Необходимо добавить проверку создания файлов при вызове `checkpoint`.  В функции `test_scenario_1`  должны быть добавлены проверки, чтобы убедиться, что создаются ожидаемые файлы и что они содержат ожидаемый контент.