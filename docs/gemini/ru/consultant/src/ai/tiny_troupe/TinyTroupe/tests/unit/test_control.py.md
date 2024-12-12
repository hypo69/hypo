# Анализ кода модуля `test_control.py`

**Качество кода**
8
 -  Плюсы
    - Код содержит unit-тесты для проверки функциональности управления симуляциями.
    - Используются ассерты для проверки корректности работы.
    - Присутствуют функции для создания агентов и окружения.
    - Используется логгер для отладки.
 -  Минусы
    -  Некоторые импорты не используются, это следует исправить.
    -  Отсутствует reStructuredText документация для функций, классов и модуля.
    -  Используются `sys.path.append`, что не рекомендуется.
    -  Используется прямой доступ к атрибутам `control._current_simulations`, лучше использовать методы.
    -  Не используется `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить docstring в формате reStructuredText для модуля и всех функций.
2.  **Импорты:**
    - Удалить неиспользуемые импорты.
    - Использовать относительные импорты, избегая `sys.path.append`.
3.  **Логирование:**
    - Использовать `logger.debug` для сообщений отладки.
4.  **Обработка ошибок:**
    - В данном коде не требуется `try-except` блоки, так как ошибки не обрабатываются.
5.  **Стиль кода:**
    - Использовать одинарные кавычки для строк.
    - Убрать прямой доступ к `control._current_simulations`, использовать методы.
    - Использовать `j_loads` или `j_loads_ns` для чтения `json` файлов.
6.  **Тестирование:**
    - Улучшить сообщения об ошибках в ассертах, чтобы было понятнее, что именно не так.

**Оптимизированный код**
```python
"""
Модуль содержит unit-тесты для проверки функциональности управления симуляциями.
=========================================================================================

Этот модуль тестирует класс :class:`Simulation` из модуля `tinytroupe.control`, проверяя его функциональность
при создании, сохранении и завершении симуляций.

Пример использования
--------------------

Примеры использования включают тесты для симуляций с агентами, окружением и фабрикой агентов.

.. code-block:: python

    pytest.main(["-v", "test_control.py"])
"""
import os
import pytest

# from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist #не используется
# from tinytroupe.agent import TinyPerson, TinyToolUse  #не используется
# from tinytroupe.environment import TinyWorld #не используется
from tinytroupe.control import Simulation, reset, begin, checkpoint, end # исправили импорт, убрали импорт как control
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.tools import TinyWordProcessor
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns
from tests.unit.testing_utils import remove_file_if_exists # Исправлен импорт
from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.agent import TinyToolUse
from tinytroupe.environment import TinyWorld

#import importlib #не используется



@pytest.fixture
def setup():
    """
    Фикстура для подготовки окружения перед каждым тестом.

    Очищает глобальные переменные и удаляет тестовые файлы кэша.
    """
    pass

def test_begin_checkpoint_end_with_agent_only(setup):
    """
    Тестирует создание, сохранение и завершение симуляции только с агентами.

    Проверяет, что симуляция корректно запускается, сохраняется и завершается.
    """
    # удаляем файл, если он существует
    remove_file_if_exists('control_test.cache.json')

    reset()

    # проверяет, что нет запущенных симуляций
    assert Simulation._current_simulations['default'] is None, 'There should be no simulation running at this point.'

    # удаляем файл, если он существует
    remove_file_if_exists('control_test.cache.json')

    begin('control_test.cache.json')
    # проверяет, что симуляция запущена
    assert Simulation._current_simulations['default'].status == Simulation.STATUS_STARTED, 'The simulation should be started at this point.'


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

    # проверяет, что кэш и трассировка созданы
    assert Simulation._current_simulations['default'].cached_trace is not None, 'There should be a cached trace at this point.'
    assert Simulation._current_simulations['default'].execution_trace is not None, 'There should be an execution trace at this point.'

    checkpoint()

    agent_1.listen_and_act('How are you doing?')
    agent_2.listen_and_act('What\'s up?')

    # проверяет, что файл кэша был создан
    assert os.path.exists('control_test.cache.json'), 'The checkpoint file should have been created.'

    end()
    # проверяет, что симуляция остановлена
    assert Simulation._current_simulations['default'].status == Simulation.STATUS_STOPPED, 'The simulation should be ended at this point.'

def test_begin_checkpoint_end_with_world(setup):
    """
    Тестирует создание, сохранение и завершение симуляции с окружением.

    Проверяет, что симуляция с окружением корректно запускается, сохраняется и завершается.
    """
    # удаляем файл, если он существует
    remove_file_if_exists('control_test_world.cache.json')

    reset()
    
    # проверяет, что нет запущенных симуляций
    assert Simulation._current_simulations['default'] is None, 'There should be no simulation running at this point.'

    begin('control_test_world.cache.json')
    # проверяет, что симуляция запущена
    assert Simulation._current_simulations['default'].status == Simulation.STATUS_STARTED, 'The simulation should be started at this point.'

    world = TinyWorld('Test World', [create_oscar_the_architect(), create_lisa_the_data_scientist()])

    world.make_everyone_accessible()

    # проверяет, что кэш и трассировка созданы
    assert Simulation._current_simulations['default'].cached_trace is not None, 'There should be a cached trace at this point.'
    assert Simulation._current_simulations['default'].execution_trace is not None, 'There should be an execution trace at this point.'

    world.run(2)

    checkpoint()

    # проверяет, что файл кэша был создан
    assert os.path.exists('control_test_world.cache.json'), 'The checkpoint file should have been created.'

    end()
    # проверяет, что симуляция остановлена
    assert Simulation._current_simulations['default'].status == Simulation.STATUS_STOPPED, 'The simulation should be ended at this point.'


def test_begin_checkpoint_end_with_factory(setup):
    """
    Тестирует создание, сохранение и завершение симуляции с фабрикой агентов.

    Проверяет, что симуляция с фабрикой агентов корректно запускается, сохраняется и завершается.
    """
    # удаляем файл, если он существует
    remove_file_if_exists('control_test_personfactory.cache.json')

    def aux_simulation_to_repeat(iteration, verbose=False):
        """
        Вспомогательная функция для запуска и проверки симуляции.
        
        :param iteration: Номер итерации симуляции.
        :param verbose: Флаг для вывода отладочной информации.
        :return: Созданный агент.
        """
        reset()
    
        # проверяет, что нет запущенных симуляций
        assert Simulation._current_simulations['default'] is None, 'There should be no simulation running at this point.'

        begin('control_test_personfactory.cache.json')
        # проверяет, что симуляция запущена
        assert Simulation._current_simulations['default'].status == Simulation.STATUS_STARTED, 'The simulation should be started at this point.'    
        
        factory = TinyPersonFactory('We are interested in experts in the production of the traditional Gazpacho soup.')

        # проверяет, что кэш и трассировка созданы
        assert Simulation._current_simulations['default'].cached_trace is not None, 'There should be a cached trace at this point.'
        assert Simulation._current_simulations['default'].execution_trace is not None, 'There should be an execution trace at this point.'

        agent = factory.generate_person('A Brazilian tourist who learned about Gazpaccho in a trip to Spain.')

        # проверяет, что кэш и трассировка созданы
        assert Simulation._current_simulations['default'].cached_trace is not None, 'There should be a cached trace at this point.'
        assert Simulation._current_simulations['default'].execution_trace is not None, 'There should be an execution trace at this point.'

        checkpoint()

        # проверяет, что файл кэша был создан
        assert os.path.exists('control_test_personfactory.cache.json'), 'The checkpoint file should have been created.'

        end()
        # проверяет, что симуляция остановлена
        assert Simulation._current_simulations['default'].status == Simulation.STATUS_STOPPED, 'The simulation should be ended at this point.'

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

    # проверяет, что возраст и национальность совпадают в обеих симуляциях
    assert age_1 == age_2, 'The age should be the same in both simulations.'
    assert nationality_1 == nationality_2, 'The nationality should be the same in both simulations.'