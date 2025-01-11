# Анализ кода модуля test_control

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на отдельные тестовые функции, каждая из которых проверяет определенную функциональность.
    - Используются фикстуры pytest для настройки тестовой среды.
    - Присутствуют проверки состояния симуляции и создания файлов.
    - Применены логические утверждения `assert` для валидации поведения кода.
    - Код легко читаем и понятен, благодаря информативным названиям переменных и функций.
- Минусы
    -  Импорт `logger` выполнен не из `src.logger`, а напрямую из `logging`.
    -  Используется `sys.path.append` вместо `from` для импорта модулей, что не является лучшей практикой.
    -  Не хватает docstring для функций и модулей, что затрудняет понимание назначения кода.

**Рекомендации по улучшению**
1.  Импортировать `logger` из `src.logger.logger`.
2.  Использовать относительные импорты для модулей внутри пакета, заменив `sys.path.append`.
3.  Добавить docstring к модулю и каждой тестовой функции.
4.  Удалить избыточное дублирование кода, например, вызов `remove_file_if_exists`.
5.  В `aux_simulation_to_repeat` можно заменить множественные `assert` на одну общую проверку.
6.  Использовать `Path` из `pathlib` для работы с путями к файлам.
7.  Разделить логику `aux_simulation_to_repeat` на несколько более мелких функций для улучшения читаемости и повторного использования.

**Оптимизированный код**

```python
"""
Модуль содержит unit тесты для проверки функциональности управления симуляцией в TinyTroupe.
=========================================================================================

Модуль тестирует следующие возможности:
- Запуск, создание чекпоинтов и завершение симуляций с агентами.
- Запуск, создание чекпоинтов и завершение симуляций с мирами (TinyWorld).
- Запуск, создание чекпоинтов и завершение симуляций с фабриками агентов (TinyPersonFactory).

Пример использования
--------------------

Пример запуска всех тестов:

.. code-block:: bash

    pytest test_control.py
"""
import pytest
import os
from pathlib import Path

# from src.logger import logger
from src.logger.logger import logger  # Исправлен импорт logger
# import sys # Удалены избыточные sys.path.append
# sys.path.append('../../tinytroupe/')
# sys.path.append('../../')
# sys.path.append('..')


from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.agent import TinyPerson, TinyToolUse
from tinytroupe.environment import TinyWorld
from tinytroupe.control import Simulation
import tinytroupe.control as control
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.tools import TinyWordProcessor

import importlib

from tests.unit.testing_utils import remove_file_if_exists, setup # исправлен импорт


def _create_test_agents():
    """Создаёт тестовых агентов для использования в симуляциях."""
    exporter = ArtifactExporter(base_output_folder='./synthetic_data_exports_3/')
    enricher = TinyEnricher()
    tooluse_faculty = TinyToolUse(tools=[TinyWordProcessor(exporter=exporter, enricher=enricher)])

    agent_1 = create_oscar_the_architect()
    agent_1.add_mental_faculties([tooluse_faculty])
    agent_1.define('age', 19)
    agent_1.define('nationality', 'Brazilian')

    agent_2 = create_lisa_the_data_scientist()
    agent_2.add_mental_faculties([tooluse_faculty])
    agent_2.define('age', 80)
    agent_2.define('nationality', 'Argentinian')
    return agent_1, agent_2

def _assert_simulation_started(simulation_name: str) -> None:
    """Проверяет, что симуляция запущена."""
    assert control._current_simulations['default'].status == Simulation.STATUS_STARTED, "The simulation should be started at this point."

def _assert_simulation_ended(simulation_name: str) -> None:
    """Проверяет, что симуляция остановлена."""
    assert control._current_simulations['default'].status == Simulation.STATUS_STOPPED, "The simulation should be ended at this point."

def _assert_trace_created(simulation_name: str) -> None:
    """Проверяет, что кэш и трассировка созданы."""
    assert control._current_simulations['default'].cached_trace is not None, "There should be a cached trace at this point."
    assert control._current_simulations['default'].execution_trace is not None, "There should be an execution trace at this point."

def _assert_checkpoint_file_exists(file_path: str) -> None:
    """Проверяет, что файл чекпоинта был создан."""
    assert Path(file_path).exists(), "The checkpoint file should have been created."

def _begin_simulation(file_path: str) -> None:
    """Начинает симуляцию и проверяет её статус."""
    remove_file_if_exists(file_path) # Упрощено: вынесено за пределы функции
    control.reset()
    assert control._current_simulations['default'] is None, "There should be no simulation running at this point."
    control.begin(file_path)
    _assert_simulation_started('default')

@pytest.mark.unit
def test_begin_checkpoint_end_with_agent_only(setup):
    """
    Тестирует запуск, создание чекпоинта и завершение симуляции с агентами.

    Проверяет корректность создания и остановки симуляции с агентами, а также создание файла чекпоинта.
    """
    file_path = 'control_test.cache.json'
    _begin_simulation(file_path)

    agent_1, agent_2 = _create_test_agents()
    _assert_trace_created('default')
    
    control.checkpoint()
    agent_1.listen_and_act("How are you doing?")
    agent_2.listen_and_act("What's up?")
    _assert_checkpoint_file_exists(file_path)

    control.end()
    _assert_simulation_ended('default')

@pytest.mark.unit
def test_begin_checkpoint_end_with_world(setup):
    """
    Тестирует запуск, создание чекпоинта и завершение симуляции с миром (TinyWorld).

    Проверяет корректность создания и остановки симуляции с миром, а также создание файла чекпоинта.
    """
    file_path = 'control_test_world.cache.json'
    _begin_simulation(file_path)
    
    world = TinyWorld("Test World", [create_oscar_the_architect(), create_lisa_the_data_scientist()])
    world.make_everyone_accessible()
    _assert_trace_created('default')

    world.run(2)
    control.checkpoint()
    _assert_checkpoint_file_exists(file_path)
    
    control.end()
    _assert_simulation_ended('default')

@pytest.mark.unit
def test_begin_checkpoint_end_with_factory(setup):
    """
    Тестирует запуск, создание чекпоинта и завершение симуляции с фабрикой агентов (TinyPersonFactory).

    Проверяет корректность создания и остановки симуляции с использованием фабрики агентов,
    а также сохранение свойств агентов между симуляциями.
    """
    file_path = 'control_test_personfactory.cache.json'
    def aux_simulation_to_repeat(iteration, verbose=False):
        """Вспомогательная функция для повторения симуляции."""
        _begin_simulation(file_path)
        
        factory = TinyPersonFactory("We are interested in experts in the production of the traditional Gazpacho soup.")
        _assert_trace_created('default')

        agent = factory.generate_person("A Brazilian tourist who learned about Gazpaccho in a trip to Spain.")

        _assert_trace_created('default')
        control.checkpoint()
        _assert_checkpoint_file_exists(file_path)
        control.end()
        _assert_simulation_ended('default')

        if verbose:
            logger.debug(f"###################################################################################### Sim Iteration:{iteration}")
            logger.debug(f"###################################################################################### Agent configs:{agent._configuration}")
        return agent

    # FIRST simulation ########################################################
    agent_1 = aux_simulation_to_repeat(1, verbose=True)
    age_1 = agent_1.get("age")
    nationality_1 = agent_1.get("nationality")
    # SECOND simulation ########################################################
    logger.debug(">>>>>>>>>>>>>>>>>>>>>>>>>> Second simulation...")
    agent_2 = aux_simulation_to_repeat(2, verbose=True)
    age_2 = agent_2.get("age")
    nationality_2 = agent_2.get("nationality")
    assert age_1 == age_2, "The age should be the same in both simulations."
    assert nationality_1 == nationality_2, "The nationality should be the same in both simulations."