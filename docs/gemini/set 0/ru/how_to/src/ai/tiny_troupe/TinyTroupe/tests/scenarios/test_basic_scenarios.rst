Как использовать этот блок кода
========================================================================================

Описание
-------------------------
Этот код содержит функцию `test_scenario_1`, которая тестирует начальную инициализацию и некоторые базовые операции симуляции TinyTroupe.  Функция проверяет состояние симуляции, создает агента (в данном случае архитектора Оскара), устанавливает его характеристики (возраст, национальность), сохраняет трассировку и делает проверку на наличие и корректность сохраненной трассировки.  Последующие `checkpoint()` позволяют сохранить промежуточные состояния симуляции.

Шаги выполнения
-------------------------
1. **Инициализация:** Функция `control.reset()` сбрасывает текущую симуляцию.
2. **Проверка состояния:** Проверяет, что текущей симуляции нет (`control._current_simulations["default"] is None`).
3. **Старт симуляции:** Функция `control.begin()` запускает симуляцию.
4. **Проверка состояния:** Проверяет, что статус симуляции `Simulation.STATUS_STARTED`.
5. **Создание агента:** Создает агента `Oscar` с помощью функции `create_oscar_the_architect()`.
6. **Определение характеристик агента:** Устанавливает значения характеристик агента `age` и `nationality`.
7. **Проверка наличия трассировки:** Проверяет, что кэшированная (`cached_trace`) и исполняемая (`execution_trace`) трассировка не равны `None`.
8. **Сохранение состояния (checkpoint):** Сохраняет промежуточное состояние симуляции с помощью `control.checkpoint()`.
9. **Взаимодействие агента:** Агент получает запрос `How are you doing?` и отвечает.
10. **Определение дополнительной характеристики:** Агент получает дополнительную характеристику `occupation`.
11. **Сохранение состояния (checkpoint):** Сохраняет промежуточное состояние симуляции с помощью `control.checkpoint()`.
12. **Остановка симуляции:** Функция `control.end()` останавливает симуляцию.


Пример использования
-------------------------
.. code-block:: python

    import pytest
    import logging
    logger = logging.getLogger("tinytroupe")

    import sys
    sys.path.append('../../tinytroupe/')
    sys.path.append('../../')
    sys.path.append('..')

    import tinytroupe
    from tinytroupe.agent import TinyPerson
    from tinytroupe.environment import TinyWorld, TinySocialNetwork
    from tinytroupe.factory import TinyPersonFactory
    from tinytroupe.extraction import ResultsExtractor
    from tinytroupe.examples import create_lisa_the_data_scientist, create_oscar_the_architect, create_marcos_the_physician
    from tinytroupe.extraction import default_extractor as extractor
    import tinytroupe.control as control
    from tinytroupe.control import Simulation
    from testing_utils import *

    def test_scenario_1():
        # ... (Остальной код из примера) ...