# Анализ кода модуля `test_story.py`

**Качество кода**
8
-   Плюсы
    -   Код хорошо структурирован и разбит на отдельные тестовые функции, что облегчает понимание и отладку.
    -   Используется `pytest` для организации тестов, что является стандартной практикой.
    -   Код импортирует необходимые модули и классы из проекта `tinytroupe`, что показывает его интеграцию с остальной частью системы.
    -   Используется `assert proposition_holds` для проверки результатов, что делает тесты более выразительными.
    -   Есть подготовка окружения для тестов через fixture `setup` и `focus_group_world`
-   Минусы
    -   Отсутствуют docstring для модуля и тестовых функций, что затрудняет понимание их назначения и использования.
    -   Используется `print` для отладки, что не является оптимальным подходом, лучше использовать логирование.
    -   В начале файла есть добавление путей в `sys.path`, что может быть избыточным и нежелательным.
    -   Не используется `from src.logger.logger import logger` для логирования ошибок.
    -   В импортах есть относительные пути, это не всегда хороший тон

**Рекомендации по улучшению**

1.  Добавить docstring для модуля и каждой тестовой функции, используя reStructuredText (RST) формат.
2.  Использовать `logger` вместо `print` для вывода информации в консоль.
3.  Удалить добавление путей в `sys.path`.
4.  Изменить импорты на абсолютные
5.  Добавить try-except для более надежной обработки ошибок.

**Оптимизированный код**

```python
"""
Модуль содержит тесты для проверки функциональности модуля `TinyStory`
=====================================================================

Модуль тестирует методы `start_story` и `continue_story` класса `TinyStory`,
убеждаясь, что они возвращают корректные текстовые фрагменты, которые могут
начать или продолжить историю с участием персонажей Lisa, Marcos и Oscar.

Примеры использования:
---------------------

.. code-block:: python

    # Пример запуска теста
    pytest test_story.py
"""
import pytest
# from src.logger.logger import logger # TODO добавить логгер
import logging

logger = logging.getLogger("tinytroupe")


import sys
# sys.path.append('../../tinytroupe/') #TODO удалить относительные пути
# sys.path.append('../../') #TODO удалить относительные пути
# sys.path.append('../') #TODO удалить относительные пути


import tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.extraction import ResultsExtractor
from tinytroupe.story import TinyStory

from tinytroupe.examples import create_lisa_the_data_scientist, create_oscar_the_architect, create_marcos_the_physician
from tinytroupe.extraction import default_extractor as extractor
import tinytroupe.control as control
from tinytroupe.control import Simulation

from tests.unit.testing_utils import *


def test_story_start(setup, focus_group_world):
    """
    Тест проверяет, что метод `start_story` возвращает корректное начало истории.

    :param setup: Фикстура для настройки тестового окружения.
    :param focus_group_world: Фикстура для создания мира с фокус-группой персонажей.
    """
    world = focus_group_world

    story = TinyStory(world)

    try:
        # Код вызывает метод start_story и сохраняет результат в переменной start
        start = story.start_story()
    except Exception as ex:
        logger.error(f"Ошибка при вызове story.start_story(): {ex}")
        raise

    # logger.info(f"Story start: {start}") #TODO заменить print на logger
    print("Story start: ", start) #TODO удалить print

    # Проверка, что сгенерированное начало истории соответствует ожидаемому
    assert proposition_holds(f"The following could plausibly be the start of a story involving people named either Lisa, Marcos or Oscar: \'{start}\'"), f"Proposition is false according to the LLM."


def test_story_start_2(setup, focus_group_world):
    """
    Тест проверяет, что метод `start_story` возвращает корректное начало истории,
    учитывая дополнительные требования к сюжету.

    :param setup: Фикстура для настройки тестового окружения.
    :param focus_group_world: Фикстура для создания мира с фокус-группой персонажей.
    """
    world = focus_group_world

    story = TinyStory(world)

    try:
        # Код вызывает метод start_story с дополнительными требованиями
        start = story.start_story(requirements="Start a story which is extremely crazy and out of this world.")
    except Exception as ex:
        logger.error(f"Ошибка при вызове story.start_story() с requirements: {ex}")
        raise

    # logger.info(f"Story start: {start}") #TODO заменить print на logger
    print("Story start: ", start) #TODO удалить print

    # Проверка, что начало истории соответствует заданным требованиям
    assert proposition_holds(f"The following could plausibly be the start of a very crazy story involving people named either Lisa, Marcos or Oscar: \'{start}\'"), f"Proposition is false according to the LLM."


def test_story_continuation(setup, focus_group_world):
    """
    Тест проверяет, что метод `continue_story` возвращает корректное продолжение истории,
    основываясь на заданном начале.

    :param setup: Фикстура для настройки тестового окружения.
    :param focus_group_world: Фикстура для создания мира с фокус-группой персонажей.
    """
    world = focus_group_world

    story_beginning = \
        """
            You were vacationing in the beautiful city of Rio de Janeiro, Brazil. You were walking down the beach when
            the most unexpected thing happened: an Alien spaceship landed right in front of you. The door opened and a
            friendly Alien stepped out. The Alien introduced itself as Zog, and explained that it was on a mission to
            learn more about Earth\'s cultures. You were intrigued by this encounter and decided to help Zog in its mission.
          """
    # Код добавляет начало истории в окружение
    world.broadcast(story_beginning)

    # Код запускает окружение на несколько шагов
    world.run(2)

    story = TinyStory(world)

    try:
        # Код вызывает метод continue_story и сохраняет результат в переменной continuation
        continuation = story.continue_story()
    except Exception as ex:
        logger.error(f"Ошибка при вызове story.continue_story(): {ex}")
        raise
    # logger.info(f"Story continuation: {continuation}")#TODO заменить print на logger
    print("Story continuation: ", continuation) #TODO удалить print
    # Проверка, что продолжение истории логически связано с ее началом
    assert proposition_holds(f"The following two text blocks could belong to the same story: \\n BLOCK 1: \'{story_beginning}\' and \\n BLOCK 2: \'{continuation}\'"), f"Proposition is false according to the LLM."
```