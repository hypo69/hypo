# Анализ кода модуля `test_control.py`

**Качество кода**
8
-  Плюсы
    -  Код содержит тесты для проверки основных функций управления симуляциями.
    -  Используются `assert` для проверки корректности выполнения кода.
    -  Тесты покрывают различные сценарии использования, включая агентов, миры и фабрики персонажей.
    -  Есть  функция `remove_file_if_exists` для очистки тестовых файлов.
-  Минусы
    -  Импорты `sys.path.append` могут быть устранены при правильной настройке путей.
    -  Используется устаревший способ логирования `logging.getLogger("tinytroupe")`.
    -  Отсутствует документация в формате RST для функций и модуля.
    -  Используются двойные кавычки в строках.
    -  `logger.debug` используется без f-строк.
    -  Не все assert снабжены сообщением об ошибке.

**Рекомендации по улучшению**
1.  Использовать относительные импорты для модулей, чтобы избежать использования `sys.path.append`.
2.  Заменить импорт логгера на `from src.logger.logger import logger`.
3.  Добавить docstrings в формате RST к модулю и функциям.
4.  Использовать одинарные кавычки для строк.
5.  Использовать f-строки для форматирования логов.
6.  Добавить более информативные сообщения в `assert`.
7.  Использовать более конкретные имена переменных.
8.  Удалить неиспользуемые импорты `import importlib`.

**Оптимизированный код**
```python
"""
Модуль содержит unit тесты для проверки функциональности управления симуляциями в TinyTroupe.
=========================================================================================

Этот модуль тестирует основные функции управления симуляциями, включая запуск, создание контрольных точек
и завершение симуляций с различными типами объектов, таких как агенты, миры и фабрики персонажей.

Пример использования
--------------------

Пример запуска тестов:

.. code-block:: python

    pytest test_control.py
"""
import pytest
import os
# from src.logger.logger import logger
from src.logger import logger # Заменил импорт на from src.logger.logger import logger
from src.utils.testing_utils import remove_file_if_exists
from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.agent import TinyPerson, TinyToolUse
from tinytroupe.environment import TinyWorld
from tinytroupe.control import Simulation, reset, begin, checkpoint, end # Изменил импорт для явного указания используемых функций
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.tools import TinyWordProcessor

#import importlib # Удалил неиспользуемый импорт

def test_begin_checkpoint_end_with_agent_only(setup):
    """
    Тестирует запуск, создание контрольной точки и завершение симуляции с использованием агентов.

    Args:
        setup: Фикстура pytest для настройки окружения.
    """
    # удаление файла, если он существует
    remove_file_if_exists('control_test.cache.json')

    reset()

    # проверка, что нет запущенной симуляции
    assert control._current_simulations['default'] is None, 'Не должно быть запущенной симуляции.'

    # удаление файла, если он существует
    remove_file_if_exists('control_test.cache.json')

    begin('control_test.cache.json')
    # проверка, что симуляция запущена
    assert control._current_simulations['default'].status == Simulation.STATUS_STARTED, 'Симуляция должна быть запущена.'


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

    # проверка, что есть кэшированный и выполняемый трейс
    assert control._current_simulations['default'].cached_trace is not None, 'Должен быть кэшированный трейс.'
    assert control._current_simulations['default'].execution_trace is not None, 'Должен быть выполняемый трейс.'

    checkpoint()

    agent_1.listen_and_act('How are you doing?')
    agent_2.listen_and_act('What\'s up?')

    # проверка, что файл был создан
    assert os.path.exists('control_test.cache.json'), 'Файл контрольной точки должен быть создан.'

    end()

    # проверка, что симуляция остановлена
    assert control._current_simulations['default'].status == Simulation.STATUS_STOPPED, 'Симуляция должна быть остановлена.'

def test_begin_checkpoint_end_with_world(setup):
    """
    Тестирует запуск, создание контрольной точки и завершение симуляции с использованием мира.

    Args:
        setup: Фикстура pytest для настройки окружения.
    """
    # удаление файла, если он существует
    remove_file_if_exists('control_test_world.cache.json')

    reset()
    
    # проверка, что нет запущенной симуляции
    assert control._current_simulations['default'] is None, 'Не должно быть запущенной симуляции.'

    begin('control_test_world.cache.json')
    # проверка, что симуляция запущена
    assert control._current_simulations['default'].status == Simulation.STATUS_STARTED, 'Симуляция должна быть запущена.'

    world = TinyWorld('Test World', [create_oscar_the_architect(), create_lisa_the_data_scientist()])

    world.make_everyone_accessible()

    # проверка, что есть кэшированный и выполняемый трейс
    assert control._current_simulations['default'].cached_trace is not None, 'Должен быть кэшированный трейс.'
    assert control._current_simulations['default'].execution_trace is not None, 'Должен быть выполняемый трейс.'

    world.run(2)

    checkpoint()

    # проверка, что файл был создан
    assert os.path.exists('control_test_world.cache.json'), 'Файл контрольной точки должен быть создан.'

    end()

    # проверка, что симуляция остановлена
    assert control._current_simulations['default'].status == Simulation.STATUS_STOPPED, 'Симуляция должна быть остановлена.'


def test_begin_checkpoint_end_with_factory(setup):
    """
    Тестирует запуск, создание контрольной точки и завершение симуляции с использованием фабрики персонажей.

    Args:
        setup: Фикстура pytest для настройки окружения.
    """
    # удаление файла, если он существует
    remove_file_if_exists('control_test_personfactory.cache.json')

    def aux_simulation_to_repeat(iteration, verbose=False):
        """
        Вспомогательная функция для повторения симуляции.

        Args:
            iteration (int): Номер итерации.
            verbose (bool): Флаг для включения подробного вывода.

        Returns:
            TinyPerson: Сгенерированный агент.
        """
        reset()
    
        # проверка, что нет запущенной симуляции
        assert control._current_simulations['default'] is None, 'Не должно быть запущенной симуляции.'

        begin('control_test_personfactory.cache.json')
        # проверка, что симуляция запущена
        assert control._current_simulations['default'].status == Simulation.STATUS_STARTED, 'Симуляция должна быть запущена.'
        
        factory = TinyPersonFactory('We are interested in experts in the production of the traditional Gazpacho soup.')

        # проверка, что есть кэшированный и выполняемый трейс
        assert control._current_simulations['default'].cached_trace is not None, 'Должен быть кэшированный трейс.'
        assert control._current_simulations['default'].execution_trace is not None, 'Должен быть выполняемый трейс.'

        agent = factory.generate_person('A Brazilian tourist who learned about Gazpaccho in a trip to Spain.')

        # проверка, что есть кэшированный и выполняемый трейс
        assert control._current_simulations['default'].cached_trace is not None, 'Должен быть кэшированный трейс.'
        assert control._current_simulations['default'].execution_trace is not None, 'Должен быть выполняемый трейс.'

        checkpoint()

        # проверка, что файл был создан
        assert os.path.exists('control_test_personfactory.cache.json'), 'Файл контрольной точки должен быть создан.'

        end()
        # проверка, что симуляция остановлена
        assert control._current_simulations['default'].status == Simulation.STATUS_STOPPED, 'Симуляция должна быть остановлена.'

        if verbose:
            logger.debug(f'###################################################################################### Sim Iteration:{iteration}')
            logger.debug(f'###################################################################################### Agent configs:{agent._configuration}')

        return agent


    # ПЕРВАЯ симуляция ########################################################
    agent_1 = aux_simulation_to_repeat(1, verbose=True)
    age_1 = agent_1.get('age')
    nationality_1 = agent_1.get('nationality')


    # ВТОРАЯ симуляция ########################################################
    logger.debug('>>>>>>>>>>>>>>>>>>>>>>>>>> Second simulation...')
    agent_2 = aux_simulation_to_repeat(2, verbose=True)
    age_2 = agent_2.get('age')
    nationality_2 = agent_2.get('nationality')

    # проверка, что возраст и национальность одинаковы в обеих симуляциях
    assert age_1 == age_2, 'Возраст должен быть одинаковым в обеих симуляциях.'
    assert nationality_1 == nationality_2, 'Национальность должна быть одинаковой в обеих симуляциях.'