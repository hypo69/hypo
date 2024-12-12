# Анализ кода модуля `test_tinyworld`

**Качество кода**
8
- Плюсы
    - Код разбит на отдельные функции тестирования, что облегчает понимание и поддержку.
    - Используются фикстуры pytest для подготовки тестовых данных.
    - Присутствуют ассерты, проверяющие корректность работы кода.
    - Код покрывает основные сценарии работы с `TinyWorld`.

- Минусы
    - Отсутствуют docstring у функций, что затрудняет понимание их назначения.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Комментарии не соответствуют стандарту RST.
    - Используется прямое обращение к `sys.path` для добавления путей, что может быть не оптимально.

**Рекомендации по улучшению**
1. Добавить docstring в формате RST к каждой тестовой функции для описания её назначения и параметров.
2. Использовать `from src.logger.logger import logger` для логирования ошибок и отладки, если это необходимо.
3.  Заменить прямые манипуляции с `sys.path` на более гибкий подход, например, использование `conftest.py` для настройки путей.
4.  Привести в соответствие имена переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**
```python
"""
Модуль содержит тесты для проверки функциональности класса TinyWorld.
=========================================================================================

Этот модуль включает тесты для проверки основных операций класса TinyWorld,
таких как запуск, широковещательная рассылка, кодирование и декодирование состояний.

Примеры использования
--------------------
Запуск тестов:

.. code-block:: bash

    pytest test_tinyworld.py
"""
import pytest
#from src.logger.logger import logger  # TODO: использовать для логирования
import logging
logger = logging.getLogger("tinytroupe")

import sys
# Пути добавлены через conftest.py
#sys.path.append('../../tinytroupe/')
#sys.path.append('../../')
#sys.path.append('../')

from tinytroupe.examples import create_lisa_the_data_scientist, create_oscar_the_architect, create_marcos_the_physician
from tinytroupe.environment import TinyWorld
from testing_utils import *

def test_run(setup, focus_group_world):
    """
    Тестирует метод run класса TinyWorld.

    :param setup: Фикстура pytest для настройки окружения.
    :param focus_group_world: Фикстура pytest, представляющая экземпляр TinyWorld с агентами.
    """
    # Создание экземпляра TinyWorld без агентов
    world_1 = TinyWorld("Empty land", [])
    # Запуск мира на 2 шага
    world_1.run(2)

    # Использование мира с агентами
    world_2 = focus_group_world
    # Отправка сообщения всем агентам
    world_2.broadcast("Discuss ideas for a new AI product you'd love to have.")
    # Запуск мира на 2 шага
    world_2.run(2)

    # Проверка целостности сообщений в памяти агентов
    for agent in world_2.agents:
        for msg in agent.episodic_memory.retrieve_all():
            # Проверка, что ни один агент не является целью своего собственного сообщения
            if 'action' in msg['content'] and 'target' in msg['content']['action']:
                assert msg['content']['action']['target'] != agent.name, f"{agent.name} should not have any messages with itself as the target."

            # TODO stimulus integrity check?

def test_broadcast(setup, focus_group_world):
    """
    Тестирует метод broadcast класса TinyWorld.

    :param setup: Фикстура pytest для настройки окружения.
    :param focus_group_world: Фикстура pytest, представляющая экземпляр TinyWorld с агентами.
    """
    world = focus_group_world
    # Отправка сообщения всем агентам
    world.broadcast("""
                Folks, we need to brainstorm ideas for a new baby product. Something moms have been asking for centuries and never got.

                Please start the discussion now.
                """)

    for agent in focus_group_world.agents:
        # Проверка, что агенты получили сообщение
        assert "Folks, we need to brainstorm" in agent.episodic_memory.retrieve_first(1)[0]['content']['stimuli'][0]['content'], f"{agent.name} should have received the message."

def test_encode_complete_state(setup, focus_group_world):
    """
    Тестирует метод encode_complete_state класса TinyWorld.

    :param setup: Фикстура pytest для настройки окружения.
    :param focus_group_world: Фикстура pytest, представляющая экземпляр TinyWorld с агентами.
    """
    world = focus_group_world

    # Кодирование состояния мира
    state = world.encode_complete_state()

    # Проверка, что состояние не None
    assert state is not None, "The state should not be None."
    # Проверка имени мира в состоянии
    assert state['name'] == world.name, "The state should have the world name."
    # Проверка наличия агентов в состоянии
    assert state['agents'] is not None, "The state should have the agents."

def test_decode_complete_state(setup, focus_group_world):
    """
    Тестирует метод decode_complete_state класса TinyWorld.

    :param setup: Фикстура pytest для настройки окружения.
    :param focus_group_world: Фикстура pytest, представляющая экземпляр TinyWorld с агентами.
    """
    world = focus_group_world

    # Сохранение исходного имени и количества агентов
    name_1 = world.name
    n_agents_1 = len(world.agents)

    # Кодирование состояния мира
    state = world.encode_complete_state()

    # Изменение состояния мира для проверки декодирования
    world.name = "New name"
    world.agents = []

    # Декодирование состояния обратно в мир
    world_2 = world.decode_complete_state(state)

    # Проверка, что декодированный мир не None
    assert world_2 is not None, "The world should not be None."
    # Проверка, что имя мира восстановлено
    assert world_2.name == name_1, "The world should have the same name."
    # Проверка, что количество агентов восстановлено
    assert len(world_2.agents) == n_agents_1, "The world should have the same number of agents."
```