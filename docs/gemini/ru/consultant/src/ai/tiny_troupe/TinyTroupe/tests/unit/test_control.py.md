# Анализ кода модуля `test_control.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на отдельные тестовые функции.
    - Используются фикстуры pytest для настройки окружения.
    - Тесты охватывают различные сценарии использования `control.py`, включая работу с агентами, миром и фабрикой персонажей.
    - Присутствуют проверки на корректность статусов симуляции, существование файлов кэша и корректность данных, полученных в результате выполнения.
    - Используется логгер для вывода отладочной информации.
- Минусы
    - Отсутствует документация в формате reStructuredText (RST).
    - Используются прямые проверки на `None` для `_current_simulations`, что может быть улучшено.
    - Присутствуют множественные вызовы `remove_file_if_exists` для одного и того же файла в разных тестах.
    - Использованы `sys.path.append` для импорта модулей, что не является лучшей практикой.
    - Некоторые проверки могут быть более детализированы.

**Рекомендации по улучшению**
1.  **Документация**: Добавить reStructuredText (RST) docstrings для всех модулей, функций, методов и переменных.
2.  **Импорты**: Использовать более структурированный способ импорта модулей, возможно, используя относительные импорты.
3.  **Обработка ошибок**: Заменить прямые проверки `assert` на обработку через `logger.error` для более информативного логирования.
4.  **Управление файлами**: Улучшить управление файлами, возможно, вынеся удаление файлов в отдельную функцию или фикстуру.
5.  **Улучшить проверки**:  Добавить больше проверок для убеждения в том, что симуляция работает правильно. Например, можно проверять контент файлов.
6.  **Ассерты**: Использовать более информативные сообщения в ассертах, чтобы облегчить отладку.
7.  **`sys.path.append`**:  Избегать использования `sys.path.append`, вместо этого настроить `PYTHONPATH` или использовать пакетную структуру.

**Оптимизиробанный код**
```python
"""
Модуль для тестирования функциональности управления симуляциями.
=================================================================

Этот модуль содержит набор тестов, проверяющих корректность работы
класса :class:`Simulation` и функций управления симуляциями, включая
запуск, создание контрольных точек и завершение симуляций с агентами,
мирами и фабриками персонажей.

Примеры использования
--------------------

Примеры использования тестовых функций:

.. code-block:: python

    pytest.main(["-s", "test_control.py"])

"""
import pytest
import os
# #  Импортируем sys для добавления путей, но лучше использовать PYTHONPATH
# import sys
# sys.path.append('../../tinytroupe/')
# sys.path.append('../../')
# sys.path.append('../')

#  Импортируем необходимые модули из tinytroupe
from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.agent import TinyPerson, TinyToolUse
from tinytroupe.environment import TinyWorld
from tinytroupe.control import Simulation
import tinytroupe.control as control
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.tools import TinyWordProcessor

# Импортируем логгер из нашего модуля
from src.logger.logger import logger

import importlib

# Импортируем вспомогательные функции из файла testing_utils
from tests.unit.testing_utils import remove_file_if_exists


def test_begin_checkpoint_end_with_agent_only(setup):
    """
    Тестирует начало, создание контрольной точки и завершение симуляции только с агентами.

    :param setup: фикстура pytest для настройки тестовой среды.
    """
    # Удаляем файл кэша, если он существует
    remove_file_if_exists("control_test.cache.json")

    # Сбрасываем состояние контроллера симуляции
    control.reset()
    
    # Проверяем, что нет запущенных симуляций
    assert control._current_simulations["default"] is None, "На данный момент не должно быть запущенной симуляции."

    # Удаляем файл кэша, если он существует
    remove_file_if_exists("control_test.cache.json")

    # Начинаем новую симуляцию
    control.begin("control_test.cache.json")
    # Проверяем, что симуляция запущена
    assert control._current_simulations["default"].status == Simulation.STATUS_STARTED, "Симуляция должна быть запущена."


    # Создаем экспортер артефактов, обогатитель и факультет использования инструментов
    exporter = ArtifactExporter(base_output_folder="./synthetic_data_exports_3/")
    enricher = TinyEnricher()
    tooluse_faculty = TinyToolUse(tools=[TinyWordProcessor(exporter=exporter, enricher=enricher)])

    # Создаем агента 1 (Оскар Архитектор) и добавляем ему способности
    agent_1 = create_oscar_the_architect()
    agent_1.add_mental_faculties([tooluse_faculty])
    agent_1.define("age", 19)
    agent_1.define("nationality", "Brazilian")

    # Создаем агента 2 (Лиза Ученый по Данным) и добавляем ему способности
    agent_2 = create_lisa_the_data_scientist()
    agent_2.add_mental_faculties([tooluse_faculty])
    agent_2.define("age", 80)
    agent_2.define("nationality", "Argentinian")

    # Проверяем, что создан кэш и трассировка выполнения
    assert control._current_simulations["default"].cached_trace is not None, "Должна быть создана кэшированная трассировка."
    assert control._current_simulations["default"].execution_trace is not None, "Должна быть создана трассировка выполнения."

    # Создаем контрольную точку
    control.checkpoint()

    # Агенты выполняют действия
    agent_1.listen_and_act("How are you doing?")
    agent_2.listen_and_act("What\'s up?")

    # Проверяем, что файл контрольной точки создан
    assert os.path.exists("control_test.cache.json"), "Файл контрольной точки должен быть создан."

    # Завершаем симуляцию
    control.end()

    # Проверяем, что симуляция завершена
    assert control._current_simulations["default"].status == Simulation.STATUS_STOPPED, "Симуляция должна быть завершена."


def test_begin_checkpoint_end_with_world(setup):
    """
    Тестирует начало, создание контрольной точки и завершение симуляции с миром.

    :param setup: фикстура pytest для настройки тестовой среды.
    """
    # Удаляем файл кэша, если он существует
    remove_file_if_exists("control_test_world.cache.json")

    # Сбрасываем состояние контроллера симуляции
    control.reset()
    
    # Проверяем, что нет запущенных симуляций
    assert control._current_simulations["default"] is None, "На данный момент не должно быть запущенной симуляции."

    # Начинаем новую симуляцию
    control.begin("control_test_world.cache.json")
    # Проверяем, что симуляция запущена
    assert control._current_simulations["default"].status == Simulation.STATUS_STARTED, "Симуляция должна быть запущена."

    # Создаем мир и добавляем в него агентов
    world = TinyWorld("Test World", [create_oscar_the_architect(), create_lisa_the_data_scientist()])
    # Делаем всех агентов доступными друг для друга
    world.make_everyone_accessible()

    # Проверяем, что создан кэш и трассировка выполнения
    assert control._current_simulations["default"].cached_trace is not None, "Должна быть создана кэшированная трассировка."
    assert control._current_simulations["default"].execution_trace is not None, "Должна быть создана трассировка выполнения."

    # Запускаем мир на 2 шага
    world.run(2)

    # Создаем контрольную точку
    control.checkpoint()

    # Проверяем, что файл контрольной точки создан
    assert os.path.exists("control_test_world.cache.json"), "Файл контрольной точки должен быть создан."

    # Завершаем симуляцию
    control.end()

    # Проверяем, что симуляция завершена
    assert control._current_simulations["default"].status == Simulation.STATUS_STOPPED, "Симуляция должна быть завершена."


def test_begin_checkpoint_end_with_factory(setup):
    """
    Тестирует начало, создание контрольной точки и завершение симуляции с фабрикой персонажей.

    :param setup: фикстура pytest для настройки тестовой среды.
    """
    # Удаляем файл кэша, если он существует
    remove_file_if_exists("control_test_personfactory.cache.json")

    def aux_simulation_to_repeat(iteration, verbose=False):
        """
        Вспомогательная функция для повторения симуляций.

        :param iteration: номер итерации.
        :param verbose: флаг для включения подробного вывода.
        :return: сгенерированный агент.
        """
        # Сбрасываем состояние контроллера симуляции
        control.reset()
    
        # Проверяем, что нет запущенных симуляций
        assert control._current_simulations["default"] is None, "На данный момент не должно быть запущенной симуляции."

        # Начинаем новую симуляцию
        control.begin("control_test_personfactory.cache.json")
        # Проверяем, что симуляция запущена
        assert control._current_simulations["default"].status == Simulation.STATUS_STARTED, "Симуляция должна быть запущена."    
        
        # Создаем фабрику персонажей
        factory = TinyPersonFactory("We are interested in experts in the production of the traditional Gazpacho soup.")

        # Проверяем, что создан кэш и трассировка выполнения
        assert control._current_simulations["default"].cached_trace is not None, "Должна быть создана кэшированная трассировка."
        assert control._current_simulations["default"].execution_trace is not None, "Должна быть создана трассировка выполнения."

        # Генерируем персонажа
        agent = factory.generate_person("A Brazilian tourist who learned about Gazpaccho in a trip to Spain.")

        # Проверяем, что создан кэш и трассировка выполнения
        assert control._current_simulations["default"].cached_trace is not None, "Должна быть создана кэшированная трассировка."
        assert control._current_simulations["default"].execution_trace is not None, "Должна быть создана трассировка выполнения."

        # Создаем контрольную точку
        control.checkpoint()

        # Проверяем, что файл контрольной точки создан
        assert os.path.exists("control_test_personfactory.cache.json"), "Файл контрольной точки должен быть создан."

        # Завершаем симуляцию
        control.end()
        # Проверяем, что симуляция завершена
        assert control._current_simulations["default"].status == Simulation.STATUS_STOPPED, "Симуляция должна быть завершена."

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

    # Проверяем, что возраст и национальность одинаковы в обеих симуляциях
    assert age_1 == age_2, "Возраст должен быть одинаковым в обеих симуляциях."
    assert nationality_1 == nationality_2, "Национальность должна быть одинаковой в обеих симуляциях."