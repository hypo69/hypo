## Анализ кода модуля `experimentation.py`

**Качество кода**
8
-  Плюсы
    - Код достаточно хорошо структурирован, с использованием классов для `ABRandomizer` и `Intervention`.
    - Есть docstring для классов и методов, что облегчает понимание их назначения.
    - Присутствует разделение функциональности на отдельные методы.
    - Используется `random.Random` с заданным seed для воспроизводимости результатов.
-  Минусы
    - Отсутствуют необходимые импорты, например, `from src.logger.logger import logger`.
    -  В классе `Intervention` есть заглушка `raise NotImplementedError("TO-DO")`, что указывает на неполную реализацию.
    -   В классе `Intervention` не используется `logger` для логирования ошибок.
    -  Не хватает документации в стиле RST для функций и классов.
    - Присутствует избыточное использование `if-else` в методе `derandomize_name` класса `ABRandomizer`, которое можно упростить.
    -  Не все комментарии достаточно подробны и соответствуют стандарту (например, нужно уточнить, что за аргументы принимает функция `set_functional_precondition` )
    -  Отсутствует обработка возможных исключений в методе `apply` класса `Intervention`.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить необходимые импорты, включая `from src.logger.logger import logger`.
2.  **Документация:** Дополнить документацию в стиле RST для всех классов, методов и параметров, включая примеры использования.
3.  **Обработка ошибок:** Использовать `logger.error` вместо общих `Exception` в блоках `try-except`  и добавить обработку ошибок в `apply` метода в классе `Intervention`.
4.  **Упрощение логики:** Упростить логику в методе `derandomize_name` класса `ABRandomizer` для уменьшения количества `if-else` условий.
5.  **Реализация заглушек:** Заменить `raise NotImplementedError("TO-DO")` в методе `check_precondition` на корректную реализацию или логирование.
6.  **Комментарии:** Добавить более подробные комментарии, соответствующие стандарту, для лучшего понимания кода.

**Оптимизированный код**

```python
"""
Модуль для проведения экспериментов и A/B тестирования.
=========================================================================================

Этот модуль содержит классы для A/B рандомизации и управления вмешательствами в экспериментах.
Класс `ABRandomizer` обеспечивает рандомизацию и дерандомизацию вариантов, а класс `Intervention`
представляет собой абстракцию для применения вмешательств в ходе эксперимента.

Пример использования
--------------------

Пример использования класса `ABRandomizer`:

.. code-block:: python

    randomizer = ABRandomizer(real_name_1='control', real_name_2='treatment', blind_name_a='A', blind_name_b='B')
    a, b = randomizer.randomize(0, 'option1', 'option2')
    print(f"Randomized: a={a}, b={b}")
    a, b = randomizer.derandomize(0, 'option1', 'option2')
    print(f"Derandomized: a={a}, b={b}")
    real_name = randomizer.derandomize_name(0, 'A')
    print(f"Derandomized name: {real_name}")


Пример использования класса `Intervention`:

.. code-block:: python

    def my_effect(agents, environments):
        print("Intervention applied")

    intervention = Intervention()
    intervention.set_effect(my_effect)
    intervention.apply()
"""
import random
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple, Union

import pandas as pd

from src.logger.logger import logger
from tinytroupe.agent import TinyPerson  # type: ignore


class ABRandomizer:
    """
    Утилитарный класс для рандомизации между двумя опциями и последующей дерандомизации.

    Выбор сохраняется в словаре, где ключом является индекс элемента.
    Реальные имена - это имена опций в данных, а слепые имена - это имена,
    которые отображаются пользователю. `passtrough_names` - это имена, которые не рандомизируются.

    Args:
        real_name_1 (str): Имя первой опции.
        real_name_2 (str): Имя второй опции.
        blind_name_a (str): Имя первой опции, отображаемое пользователю.
        blind_name_b (str): Имя второй опции, отображаемое пользователю.
        passtrough_name (list): Список имен, которые не должны рандомизироваться.
        random_seed (int): Случайное зерно для воспроизводимости.

    Example:
         >>> randomizer = ABRandomizer(real_name_1='control', real_name_2='treatment', blind_name_a='A', blind_name_b='B')
         >>> a, b = randomizer.randomize(0, 'option1', 'option2')
         >>> print(f"Randomized: a={a}, b={b}")
         Randomized: a=option1, b=option2
         >>> a, b = randomizer.derandomize(0, 'option1', 'option2')
         >>> print(f"Derandomized: a={a}, b={b}")
         Derandomized: a=option1, b=option2
         >>> real_name = randomizer.derandomize_name(0, 'A')
         >>> print(f"Derandomized name: {real_name}")
         Derandomized name: control
    """

    def __init__(
        self,
        real_name_1: str = "control",
        real_name_2: str = "treatment",
        blind_name_a: str = "A",
        blind_name_b: str = "B",
        passtrough_name: List[str] = [],
        random_seed: int = 42,
    ):
        self.choices: Dict[int, Tuple[int, int]] = {}
        self.real_name_1 = real_name_1
        self.real_name_2 = real_name_2
        self.blind_name_a = blind_name_a
        self.blind_name_b = blind_name_b
        self.passtrough_name = passtrough_name
        self.random_seed = random_seed

    def randomize(self, i: int, a: str, b: str) -> Tuple[str, str]:
        """
        Случайным образом меняет местами a и b и возвращает результат.

        Сохраняет информацию о том, были ли a и b переставлены для элемента i,
        чтобы можно было дерандомизировать позже.

        Args:
            i (int): Индекс элемента.
            a (str): Первый вариант.
            b (str): Второй вариант.

        Returns:
            Tuple[str, str]: Кортеж из двух строк, где порядок a и b может быть изменен.
        """
        #  код использует seed
        if random.Random(self.random_seed).random() < 0.5:
            self.choices[i] = (0, 1)
            return a, b
        else:
            self.choices[i] = (1, 0)
            return b, a

    def derandomize(self, i: int, a: str, b: str) -> Tuple[str, str]:
        """
        Дерандомизирует выбор для элемента i и возвращает результат.

        Args:
            i (int): Индекс элемента.
            a (str): Первый вариант.
            b (str): Второй вариант.

        Returns:
            Tuple[str, str]: Кортеж из двух строк, где порядок a и b может быть восстановлен.

        Raises:
            Exception: Если рандомизация для элемента i не найдена.
        """
        if self.choices[i] == (0, 1):
            return a, b
        elif self.choices[i] == (1, 0):
            return b, a
        else:
            logger.error(f"No randomization found for item {i}")
            raise Exception(f"No randomization found for item {i}")

    def derandomize_name(self, i: int, blind_name: str) -> str:
        """
        Декодирует выбор, сделанный пользователем, и возвращает реальное имя варианта.

        Args:
            i (int): Индекс элемента.
            blind_name (str): Выбор, сделанный пользователем.

        Returns:
            str: Реальное имя выбранного варианта.

        Raises:
            Exception: Если выбор не распознан или рандомизация для элемента i не найдена.
        """
        if i not in self.choices:
            logger.error(f"No randomization found for item {i}")
            raise Exception(f"No randomization found for item {i}")

        choice = self.choices[i]
        if blind_name in self.passtrough_name:
            return blind_name

        if choice == (0, 1) and blind_name == self.blind_name_a:
             return self.real_name_1
        elif choice == (0, 1) and blind_name == self.blind_name_b:
             return self.real_name_2
        elif choice == (1, 0) and blind_name == self.blind_name_a:
            return self.real_name_2
        elif choice == (1, 0) and blind_name == self.blind_name_b:
            return self.real_name_1
        else:
            logger.error(f"Choice '{blind_name}' not recognized")
            raise Exception(f"Choice '{blind_name}' not recognized")



# TODO under development
class Intervention:
    """
    Класс для представления вмешательства в эксперименте.

    Args:
        agent (TinyPerson, optional): Агент, к которому применяется вмешательство.
        agents (list[TinyPerson], optional): Список агентов, к которым применяется вмешательство.
        environment (Any, optional): Окружение, к которому применяется вмешательство.
        environments (list[Any], optional): Список окружений, к которым применяется вмешательство.

    Raises:
        Exception: Если передано одновременно `agent` и `agents`, или `environment` и `environments`.
        Exception: Если не передан ни один из параметров.

    Example:
        >>> def my_effect(agents, environments):
        ...     print("Intervention applied")
        >>> intervention = Intervention()
        >>> intervention.set_effect(my_effect)
        >>> intervention.apply()
        Intervention applied
    """

    def __init__(
        self,
        agent: TinyPerson | None = None,
        agents: List[TinyPerson] | None = None,
        environment: Any = None,
        environments: List[Any] | None = None,
    ):
        # Проверка на корректность параметров
        if agent and agents:
            logger.error("Either 'agent' or 'agents' should be provided, not both")
            raise Exception("Either 'agent' or 'agents' should be provided, not both")
        if environment and environments:
            logger.error("Either 'environment' or 'environments' should be provided, not both")
            raise Exception("Either 'environment' or 'environments' should be provided, not both")
        if not (agent or agents or environment or environments):
            logger.error("At least one of the parameters should be provided")
            raise Exception("At least one of the parameters should be provided")

        # Инициализация сущностей
        self.agents = None
        self.environments = None
        if agent is not None:
            self.agents = [agent]
        elif agents is not None:
             self.agents = agents
        elif environment is not None:
            self.environments = [environment]
        elif environments is not None:
             self.environments = environments

        # Инициализация предусловий
        self.text_precondition: str | None = None
        self.precondition_func: Callable[[Any, List[Any], Any, List[Any]], bool] | None = None

        # Эффекты
        self.effect_func: Callable[[List[Any], List[Any]], None] | None = None

    ################################################################################################
    # Intervention flow
    ################################################################################################

    def check_precondition(self) -> bool:
        """
        Проверяет, выполнено ли предусловие для вмешательства.

        Returns:
            bool: True, если предусловие выполнено, False в противном случае.
        Raises:
            NotImplementedError: Если метод не реализован.
        """
        # TODO: Implement precondition check logic
        logger.error("Precondition check not implemented")
        raise NotImplementedError("TO-DO")

    def apply(self):
        """
        Применяет вмешательство.
         Raises:
             Exception: Если функция эффекта не определена.
        """
        if self.effect_func:
            try:
                self.effect_func(self.agents, self.environments)
            except Exception as ex:
                 logger.error('Ошибка при применении вмешательства', ex)
                 raise Exception('Ошибка при применении вмешательства') from ex
        else:
            logger.error("Effect function not defined")
            raise Exception("Effect function not defined")
    ################################################################################################
    # Pre and post conditions
    ################################################################################################

    def set_textual_precondition(self, text: str):
        """
        Устанавливает предусловие в виде текста для интерпретации языковой моделью.

        Args:
            text (str): Текст предусловия.
        """
        self.text_precondition = text

    def set_functional_precondition(
        self, func: Callable[[Any, List[Any], Any, List[Any]], bool]
    ):
        """
        Устанавливает предусловие в виде функции для вычисления кодом.

        Args:
            func (Callable): Функция предусловия. Принимает аргументы: `agent`, `agents`, `environment`, `environments`.
        """
        self.precondition_func = func

    def set_effect(self, effect_func: Callable[[List[Any], List[Any]], None]):
        """
        Устанавливает функцию эффекта вмешательства.

        Args:
            effect_func (Callable): Функция эффекта. Принимает аргументы: `agents`, `environments`.
        """
        self.effect_func = effect_func