# Анализ кода модуля `test_control`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, с четкими тестами, проверяющими различные аспекты управления симуляциями.
    - Используется `pytest` для тестирования, что является хорошей практикой.
    - Присутствует логирование, что помогает в отладке.
    - Применяется `remove_file_if_exists` для очистки перед тестами.
-  Минусы
    -  Отсутствуют docstring у функций и модуля.
    -  Используется `sys.path.append` для добавления путей, что не всегда является лучшей практикой.
    -  Многократное использование `assert control._current_simulations["default"] is not None` можно вынести в отдельную функцию или использовать `pytest.mark.parametrize`
    -  Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    -  Не все assert сообщения достаточно информативны

**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring к модулю и функциям в формате RST.
2.  **Импорты:** Проверить и добавить отсутствующие импорты, если это необходимо.
3.  **Пути:** Рассмотреть возможность использования более гибких способов управления путями, чем `sys.path.append`.
4.  **Обработка ошибок:** Заменить стандартные `try-except` на использование `logger.error`.
5.  **Утверждения:**  Сделать сообщения `assert` более информативными, чтобы они помогали в отладке.
6.  **Рефакторинг:** Вынести повторяющиеся проверки  `assert control._current_simulations["default"] is not None` в отдельную функцию или использовать параметризацию.
7.  **Чтение файлов:** Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.

**Оптимизированный код**

```python
"""
Модуль тестирования системы управления симуляциями TinyTroupe
============================================================

Этот модуль содержит набор тестов для проверки функциональности управления симуляциями в TinyTroupe,
включая запуск, сохранение состояния (checkpoint) и завершение симуляций с агентами, мирами и фабриками персонажей.

Примеры использования
--------------------

Примеры использования тестовых функций:

.. code-block:: python

    # Пример использования test_begin_checkpoint_end_with_agent_only
    def test_begin_checkpoint_end_with_agent_only(setup):
        ...

    # Пример использования test_begin_checkpoint_end_with_world
    def test_begin_checkpoint_end_with_world(setup):
        ...

    # Пример использования test_begin_checkpoint_end_with_factory
    def test_begin_checkpoint_end_with_factory(setup):
        ...
"""
import pytest
import os
# # TODO: проверить необходимость `sys.path.append` и заменить если нужно
import sys
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('..')

from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.agent import TinyPerson, TinyToolUse
from tinytroupe.environment import TinyWorld
from tinytroupe.control import Simulation
import tinytroupe.control as control
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.tools import TinyWordProcessor

import logging
from src.logger.logger import logger # Используем logger из src.logger.logger
import importlib
from src.utils.jjson import j_loads, j_loads_ns #  Импортируем j_loads и j_loads_ns
from tests.unit.testing_utils import remove_file_if_exists

def _check_simulation_exists():
    """
    Проверяет, что текущая симуляция существует и имеет статус "начата".

    :raises AssertionError: Если текущая симуляция не существует или не имеет статус "начата".
    """
    assert control._current_simulations["default"] is not None, "Текущая симуляция должна существовать."
    assert control._current_simulations["default"].status == Simulation.STATUS_STARTED, "Статус симуляции должен быть 'начата'."

def test_begin_checkpoint_end_with_agent_only(setup):
    """
    Тестирует жизненный цикл симуляции с агентами, включая запуск, checkpoint и остановку.

    :param setup: Фикстура pytest для настройки окружения.
    """
    # удаляем файл, если он существует
    remove_file_if_exists("control_test.cache.json")

    control.reset()
    
    assert control._current_simulations["default"] is None, "Не должно быть запущенных симуляций на данном этапе."

    # удаляем файл, если он существует
    remove_file_if_exists("control_test.cache.json")

    control.begin("control_test.cache.json")
    _check_simulation_exists() # Проверяем, что симуляция существует и запущена


    exporter = ArtifactExporter(base_output_folder="./synthetic_data_exports_3/")
    enricher = TinyEnricher()
    tooluse_faculty = TinyToolUse(tools=[TinyWordProcessor(exporter=exporter, enricher=enricher)])

    agent_1 = create_oscar_the_architect()
    agent_1.add_mental_faculties([tooluse_faculty])
    agent_1.define("age", 19)
    agent_1.define("nationality", "Brazilian")

    agent_2 = create_lisa_the_data_scientist()
    agent_2.add_mental_faculties([tooluse_faculty])
    agent_2.define("age", 80)
    agent_2.define("nationality", "Argentinian")

    assert control._current_simulations["default"].cached_trace is not None, "Должна быть сохраненная трассировка на этом этапе."
    assert control._current_simulations["default"].execution_trace is not None, "Должна быть трассировка исполнения на этом этапе."

    control.checkpoint()

    agent_1.listen_and_act("How are you doing?")
    agent_2.listen_and_act("What\'s up?")

    # проверка, что файл был создан
    assert os.path.exists("control_test.cache.json"), "Файл checkpoint должен быть создан."

    control.end()

    assert control._current_simulations["default"].status == Simulation.STATUS_STOPPED, "Симуляция должна быть остановлена на этом этапе."

def test_begin_checkpoint_end_with_world(setup):
    """
    Тестирует жизненный цикл симуляции с миром (TinyWorld), включая запуск, checkpoint и остановку.

    :param setup: Фикстура pytest для настройки окружения.
    """
    # удаляем файл, если он существует
    remove_file_if_exists("control_test_world.cache.json")

    control.reset()
    
    assert control._current_simulations["default"] is None, "Не должно быть запущенных симуляций на данном этапе."

    control.begin("control_test_world.cache.json")
    _check_simulation_exists() # Проверяем, что симуляция существует и запущена

    world = TinyWorld("Test World", [create_oscar_the_architect(), create_lisa_the_data_scientist()])

    world.make_everyone_accessible()

    assert control._current_simulations["default"].cached_trace is not None, "Должна быть сохраненная трассировка на этом этапе."
    assert control._current_simulations["default"].execution_trace is not None, "Должна быть трассировка исполнения на этом этапе."

    world.run(2)

    control.checkpoint()

    # проверка, что файл был создан
    assert os.path.exists("control_test_world.cache.json"), "Файл checkpoint должен быть создан."

    control.end()

    assert control._current_simulations["default"].status == Simulation.STATUS_STOPPED, "Симуляция должна быть остановлена на этом этапе."

def test_begin_checkpoint_end_with_factory(setup):
    """
    Тестирует жизненный цикл симуляции с фабрикой персонажей (TinyPersonFactory), включая запуск, checkpoint и остановку.

    :param setup: Фикстура pytest для настройки окружения.
    """
    # удаляем файл, если он существует
    remove_file_if_exists("control_test_personfactory.cache.json")

    def aux_simulation_to_repeat(iteration, verbose=False):
        """
        Вспомогательная функция для выполнения повторяющихся симуляций.

        :param iteration: Номер итерации симуляции.
        :param verbose: Флаг для включения подробного логирования.
        :return: Созданный агент.
        """
        control.reset()
    
        assert control._current_simulations["default"] is None, "Не должно быть запущенных симуляций на данном этапе."

        control.begin("control_test_personfactory.cache.json")
        _check_simulation_exists() # Проверяем, что симуляция существует и запущена
        
        factory = TinyPersonFactory("We are interested in experts in the production of the traditional Gazpacho soup.")

        assert control._current_simulations["default"].cached_trace is not None, "Должна быть сохраненная трассировка на этом этапе."
        assert control._current_simulations["default"].execution_trace is not None, "Должна быть трассировка исполнения на этом этапе."

        agent = factory.generate_person("A Brazilian tourist who learned about Gazpaccho in a trip to Spain.")

        assert control._current_simulations["default"].cached_trace is not None, "Должна быть сохраненная трассировка на этом этапе."
        assert control._current_simulations["default"].execution_trace is not None, "Должна быть трассировка исполнения на этом этапе."

        control.checkpoint()

        # проверка, что файл был создан
        assert os.path.exists("control_test_personfactory.cache.json"), "Файл checkpoint должен быть создан."

        control.end()
        assert control._current_simulations["default"].status == Simulation.STATUS_STOPPED, "Симуляция должна быть остановлена на этом этапе."

        if verbose:
            logger.debug(f"###################################################################################### Sim Iteration:{iteration}")
            logger.debug(f"###################################################################################### Agent configs:{agent._configuration}")

        return agent


    # ПЕРВАЯ симуляция ########################################################
    agent_1 = aux_simulation_to_repeat(1, verbose=True)
    age_1 = agent_1.get("age")
    nationality_1 = agent_1.get("nationality")


    # ВТОРАЯ симуляция ########################################################
    logger.debug(">>>>>>>>>>>>>>>>>>>>>>>>>> Second simulation...")
    agent_2 = aux_simulation_to_repeat(2, verbose=True)
    age_2 = agent_2.get("age")
    nationality_2 = agent_2.get("nationality")

    assert age_1 == age_2, "Возраст должен быть одинаковым в обеих симуляциях."
    assert nationality_1 == nationality_2, "Национальность должна быть одинаковой в обеих симуляциях."