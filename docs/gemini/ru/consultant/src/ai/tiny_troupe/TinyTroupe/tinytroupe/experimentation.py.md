# Анализ кода модуля `experimentation.py`

**Качество кода: 7/10**

*   **Плюсы**
    *   Код логически структурирован, классы и методы имеют понятные названия.
    *   Используется `random.Random` с заданным `random_seed` для воспроизводимости.
    *   Класс `ABRandomizer` предоставляет функциональность для A/B-тестирования.
    *   Класс `Intervention` предоставляет базовый интерфейс для применения вмешательств.
    *   Используются docstrings для описания классов и методов, хотя и не в reStructuredText формате.
*   **Минусы**
    *   Отсутствуют необходимые импорты для использования `logger`.
    *   Docstrings не соответствуют стандарту reStructuredText (RST).
    *   Не используются `j_loads` или `j_loads_ns` для чтения файлов (хотя в данном файле это не требуется).
    *   В классе `Intervention` отсутствуют проверки на тип аргументов.
    *   Метод `check_precondition` класса `Intervention` не реализован.
    *   Не используются логирование ошибок.

**Рекомендации по улучшению**

1.  Импортировать `logger` из `src.logger.logger`.
2.  Переписать все docstrings в формате reStructuredText.
3.  Добавить логирование ошибок в методы `derandomize` и `derandomize_name` класса `ABRandomizer`.
4.  В классе `Intervention` добавить проверку типов для аргументов `agent`, `agents`, `environment` и `environments`.
5.  Реализовать метод `check_precondition` в классе `Intervention`.
6.  Добавить обработку исключений с помощью `logger.error` вместо общих `try-except`.
7.  Уточнить документацию к параметрам функций, особенно к `func` в `set_functional_precondition`, `effect_func` в `set_effect`.

**Оптимизированный код**

```python
"""
Модуль для проведения экспериментов и A/B тестирования.
========================================================

Этот модуль предоставляет классы для рандомизации вариантов A/B-тестирования
и применения вмешательств в экспериментах.

Содержит классы:
    - :class:`ABRandomizer` для рандомизации и дерандомизации вариантов.
    - :class:`Intervention` для определения и применения вмешательств.

Пример использования
--------------------

Пример использования класса :class:`ABRandomizer`:

.. code-block:: python

    randomizer = ABRandomizer()
    a, b = randomizer.randomize(0, "option_a", "option_b")
    print(f"Рандомизированные варианты: {a}, {b}")
    a, b = randomizer.derandomize(0, "option_a", "option_b")
    print(f"Дерандомизированные варианты: {a}, {b}")
    real_name = randomizer.derandomize_name(0, "A")
    print(f"Дерандомизированное имя: {real_name}")

Пример использования класса :class:`Intervention`:

.. code-block:: python

    def my_effect(agents, environments):
        if agents:
            for agent in agents:
                 print(f'Вмешательство применено к агенту: {agent}')
        if environments:
            for env in environments:
                print(f'Вмешательство применено к среде: {env}')


    intervention = Intervention()
    intervention.set_effect(my_effect)
    intervention.apply()
"""
import random
import pandas as pd
from typing import Any, List, Callable
# from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from tinytroupe.agent import TinyPerson


class ABRandomizer():
    """
    Утилитарный класс для рандомизации между двумя опциями и последующей дерандомизации.

    Выбор хранится в словаре, где ключ - индекс элемента.
    Реальные имена - это имена опций в данных, а слепые имена - это имена,
    представленные пользователю. Имена `passtrough` не рандомизируются и возвращаются как есть.

    :param real_name_1: Имя первой опции.
    :type real_name_1: str
    :param real_name_2: Имя второй опции.
    :type real_name_2: str
    :param blind_name_a: Имя первой опции, как она видна пользователю.
    :type blind_name_a: str
    :param blind_name_b: Имя второй опции, как она видна пользователю.
    :type blind_name_b: str
    :param passtrough_name: Список имен, которые не должны рандомизироваться.
    :type passtrough_name: list
    :param random_seed: Случайное зерно для воспроизводимости.
    :type random_seed: int
    """

    def __init__(self, real_name_1="control", real_name_2="treatment",
                       blind_name_a="A", blind_name_b="B",
                       passtrough_name=[],
                       random_seed=42):
        """Инициализация ABRandomizer."""
        self.choices = {}
        self.real_name_1 = real_name_1
        self.real_name_2 = real_name_2
        self.blind_name_a = blind_name_a
        self.blind_name_b = blind_name_b
        self.passtrough_name = passtrough_name
        self.random_seed = random_seed

    def randomize(self, i: int, a: str, b: str) -> tuple[str, str]:
        """
        Случайно меняет местами a и b и возвращает выбор.
        Сохраняет информацию о том, были ли a и b поменяны местами для элемента i,
        чтобы иметь возможность дерандомизировать позже.

        :param i: Индекс элемента.
        :type i: int
        :param a: Первый вариант.
        :type a: str
        :param b: Второй вариант.
        :type b: str
        :return: Кортеж из двух строк, где a и b могут быть поменяны местами.
        :rtype: tuple[str, str]
        """
        # код исполняет рандомизацию с использованием заданного seed
        if random.Random(self.random_seed).random() < 0.5:
            self.choices[i] = (0, 1)
            return a, b

        else:
            self.choices[i] = (1, 0)
            return b, a

    def derandomize(self, i: int, a: str, b: str) -> tuple[str, str]:
        """
        Дерандомизирует выбор для элемента i и возвращает выбор.

        :param i: Индекс элемента.
        :type i: int
        :param a: Первый вариант.
        :type a: str
        :param b: Второй вариант.
        :type b: str
        :return: Кортеж из двух строк, где a и b приведены к исходному порядку.
        :rtype: tuple[str, str]
        :raises Exception: Если рандомизация не найдена для элемента i.
        """
        # код исполняет дерандомизацию, восстанавливая исходный порядок вариантов
        if self.choices.get(i) == (0, 1):
            return a, b
        elif self.choices.get(i) == (1, 0):
            return b, a
        else:
            logger.error(f"No randomization found for item {i}")
            raise Exception(f"No randomization found for item {i}")

    def derandomize_name(self, i: int, blind_name: str) -> str:
        """
        Декодирует выбор пользователя и возвращает исходное имя варианта.

        :param i: Индекс элемента.
        :type i: int
        :param blind_name: Выбор пользователя (слепое имя).
        :type blind_name: str
        :return: Исходное имя варианта.
        :rtype: str
        :raises Exception: Если выбор не распознан или нет рандомизации для элемента i.
        """
        # код проверяет, была ли произведена рандомизация
        if self.choices.get(i) == (0, 1):
            # код проверяет соответствие имени и возвращает исходное имя
            if blind_name == self.blind_name_a:
                return self.real_name_1
            elif blind_name == self.blind_name_b:
                return self.real_name_2
            elif blind_name in self.passtrough_name:
                return blind_name
            else:
                logger.error(f"Choice \'{blind_name}\' not recognized")
                raise Exception(f"Choice \'{blind_name}\' not recognized")

        elif self.choices.get(i) == (1, 0):
            # код возвращает противоположный вариант, если была рандомизация
            if blind_name == self.blind_name_a:
                return self.real_name_2
            elif blind_name == self.blind_name_b:
                return self.real_name_1
            elif blind_name in self.passtrough_name:
                return blind_name
            else:
                logger.error(f"Choice \'{blind_name}\' not recognized")
                raise Exception(f"Choice \'{blind_name}\' not recognized")
        else:
             logger.error(f"No randomization found for item {i}")
             raise Exception(f"No randomization found for item {i}")


# TODO under development
class Intervention():
    """
    Класс для определения и применения вмешательств в эксперименте.

    :param agent: Агент, на которого оказывается вмешательство.
    :type agent: TinyPerson, optional
    :param agents: Список агентов, на которых оказывается вмешательство.
    :type agents: list[TinyPerson], optional
    :param environment: Среда, на которую оказывается вмешательство.
    :type environment: TinyWorld, optional
    :param environments: Список сред, на которые оказывается вмешательство.
    :type environments: list[TinyWorld], optional
    :raises Exception: Если не передан ни один параметр, или переданы оба параметра одновременно (agent и agents, environment и environments).
    """

    def __init__(self, agent: TinyPerson = None, agents: List[TinyPerson] = None, environment: Any = None, environments: List[Any] = None):
        """Инициализация Intervention."""
        # код проверяет, что передан хотя бы один параметр и не переданы оба варианта параметров одновременно
        if agent and agents:
            raise Exception("Either \'agent\' or \'agents\' should be provided, not both")
        if environment and environments:
            raise Exception("Either \'environment\' or \'environments\' should be provided, not both")
        if not (agent or agents or environment or environments):
            raise Exception("At least one of the parameters should be provided")

        # код инициализирует возможные сущности для вмешательства
        self.agents = None
        self.environments = None
        if agent is not None:
            if not isinstance(agent, TinyPerson):
                raise TypeError("agent must be an instance of TinyPerson")
            self.agents = [agent]
        elif agents is not None:
            if not all(isinstance(a, TinyPerson) for a in agents):
                raise TypeError("agents must be a list of TinyPerson instances")
            self.agents = agents
        elif environment is not None:
            self.environments = [environment]
        elif environments is not None:
            self.environments = environments


        # код инициализирует предусловия
        self.text_precondition = None
        self.precondition_func = None

        # код инициализирует эффекты
        self.effect_func = None

    ################################################################################################
    # Intervention flow
    ################################################################################################

    def check_precondition(self) -> bool:
        """
        Проверяет, выполнено ли предусловие для вмешательства.

        :raises NotImplementedError: Если метод не реализован.
        """
        # TODO: implement precondition check
        raise NotImplementedError("TO-DO")

    def apply(self) -> None:
        """
        Применяет вмешательство, вызывая функцию эффекта.
        """
        # код вызывает функцию эффекта с агентами и средами
        if self.effect_func:
             self.effect_func(self.agents, self.environments)
        else:
             logger.error("Effect function is not set")

    ################################################################################################
    # Pre and post conditions
    ################################################################################################

    def set_textual_precondition(self, text: str) -> None:
        """
        Устанавливает предусловие в виде текста, который интерпретируется языковой моделью.

        :param text: Текст предусловия.
        :type text: str
        """
        # код устанавливает текстовое предусловие
        self.text_precondition = text

    def set_functional_precondition(self, func: Callable[[List[TinyPerson], List[Any]], bool]) -> None:
        """
        Устанавливает предусловие в виде функции, которая оценивается кодом.

        :param func: Функция предусловия.
           Функция должна принимать аргументы: agent, agents, environment, environments и возвращать булево значение.
        :type func: Callable[[List[TinyPerson], List[Any]], bool]
        """
        # код устанавливает функциональное предусловие
        self.precondition_func = func

    def set_effect(self, effect_func: Callable[[List[TinyPerson], List[Any]], None]) -> None:
        """
        Устанавливает функцию эффекта вмешательства.

        :param effect_func: Функция эффекта.
           Функция должна принимать аргументы: агенты и среды.
        :type effect_func: Callable[[List[TinyPerson], List[Any]], None]
        """
        # код устанавливает функцию эффекта
        self.effect_func = effect_func
```