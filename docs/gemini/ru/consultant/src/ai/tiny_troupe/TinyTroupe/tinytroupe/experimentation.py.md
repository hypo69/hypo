## Анализ кода модуля `experimentation`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, используются классы для организации функциональности.
    - Присутствует документация для классов и методов, хотя и требует доработки.
    - Логика работы `ABRandomizer` понятна и соответствует поставленной задаче.
    - Используется `random.Random` для воспроизводимости результатов.
- Минусы
    -  Отсутствуют необходимые импорты.
    -  Не хватает проверок типов для аргументов функций.
    -  Используются `raise Exception`, вместо `logger.error`.
    -  Не все функции имеют docstring.
    -  Класс `Intervention` не имеет реализации, помечен как `TODO`.
    -   Используется  неоднородный стиль форматирования.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить отсутствующие импорты, например `from src.logger.logger import logger`.
2.  **Форматирование**: Использовать одинарные кавычки для строк в коде и двойные только для вывода.
3.  **Обработка ошибок**: Заменить `raise Exception` на `logger.error` для более информативного логирования ошибок.
4.  **Документация**: Дополнить docstring для всех функций, методов и классов.
5.  **Проверка типов**: Добавить проверки типов для аргументов функций (можно использовать аннотации типов).
6.  **Реализация `Intervention`**: Реализовать методы класса `Intervention` (хотя бы заглушки).
7.  **Общая структура**: Улучшить общую структуру модуля, добавив описание модуля в начале файла.
8.  **Соглашения**: Привести все имена переменных к единому стилю.
9.  **Комментарии**: Добавить более подробные комментарии для сложных участков кода.

**Оптимизированный код**

```python
"""
Модуль для проведения экспериментов и A/B тестирования.
=========================================================================================

Этот модуль содержит классы :class:`ABRandomizer` и :class:`Intervention` для проведения A/B тестов
и управления экспериментами.

Класс `ABRandomizer` используется для рандомизации и дерандомизации вариантов, а класс `Intervention`
предназначен для определения и применения различных видов воздействий в экспериментах.

Пример использования
--------------------

Пример использования класса `ABRandomizer`:

.. code-block:: python

    randomizer = ABRandomizer(real_name_1='control', real_name_2='treatment',
                              blind_name_a='A', blind_name_b='B', random_seed=42)
    a, b = randomizer.randomize(0, 'option_a', 'option_b')
    real_name = randomizer.derandomize_name(0, 'A')

Пример использования класса `Intervention`:

.. code-block:: python

    # TODO: Example usage after implementation

"""
import random
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple
import pandas as pd
from src.logger.logger import logger
from tinytroupe.agent import TinyPerson # TODO check import and use
# from tinytroupe.world import TinyWorld # TODO check import and use

class ABRandomizer:
    """
    Утилита для рандомизации между двумя вариантами и последующей дерандомизации.

    Атрибуты:
        choices (dict): Словарь, хранящий информацию о рандомизации для каждого элемента.
        real_name_1 (str): Название первого варианта.
        real_name_2 (str): Название второго варианта.
        blind_name_a (str): Название первого варианта для пользователя.
        blind_name_b (str): Название второго варианта для пользователя.
        passtrough_name (list): Список названий, которые не должны быть рандомизированы.
        random_seed (int): Зерно для генератора случайных чисел.
    """
    def __init__(
        self,
        real_name_1: str = 'control',
        real_name_2: str = 'treatment',
        blind_name_a: str = 'A',
        blind_name_b: str = 'B',
        passtrough_name: List[str] = [],
        random_seed: int = 42,
    ) -> None:
        """
        Инициализирует объект ABRandomizer.

        Args:
            real_name_1 (str): Название первого варианта.
            real_name_2 (str): Название второго варианта.
            blind_name_a (str): Название первого варианта, видимое пользователю.
            blind_name_b (str): Название второго варианта, видимое пользователю.
            passtrough_name (list): Список названий, которые не подвергаются рандомизации.
            random_seed (int): Зерно для генератора случайных чисел.
        """
        self.choices: Dict[int, Tuple[int, int]] = {}
        self.real_name_1: str = real_name_1
        self.real_name_2: str = real_name_2
        self.blind_name_a: str = blind_name_a
        self.blind_name_b: str = blind_name_b
        self.passtrough_name: List[str] = passtrough_name
        self.random_seed: int = random_seed

    def randomize(self, i: int, a: str, b: str) -> Tuple[str, str]:
        """
        Случайным образом меняет местами a и b и возвращает выбор.

        Сохраняет информацию о том, были ли переставлены a и b для элемента i,
        чтобы можно было дерандомизировать позже.

        Args:
            i (int): Индекс элемента.
            a (str): Первый вариант.
            b (str): Второй вариант.

        Returns:
            Tuple[str, str]: Кортеж с вариантами a и b (возможно, переставленными).
        """
        # использует seed для воспроизводимости
        if random.Random(self.random_seed).random() < 0.5:
            self.choices[i] = (0, 1)
            return a, b
        else:
            self.choices[i] = (1, 0)
            return b, a

    def derandomize(self, i: int, a: str, b: str) -> Tuple[str, str]:
        """
        Дерандомизирует выбор для элемента i и возвращает варианты.

        Args:
            i (int): Индекс элемента.
            a (str): Первый вариант.
            b (str): Второй вариант.

        Returns:
            Tuple[str, str]: Кортеж с вариантами a и b в исходном порядке.

        Raises:
            Exception: Если рандомизация для элемента i не найдена.
        """
        if self.choices[i] == (0, 1):
            return a, b
        elif self.choices[i] == (1, 0):
            return b, a
        else:
            logger.error(f'Рандомизация не найдена для элемента {i}')
            raise Exception(f'Рандомизация не найдена для элемента {i}')

    def derandomize_name(self, i: int, blind_name: str) -> str:
        """
        Декодирует выбор, сделанный пользователем, и возвращает соответствующий вариант.

        Args:
            i (int): Индекс элемента.
            blind_name (str): Выбор, сделанный пользователем.

        Returns:
            str: Исходное название выбранного варианта.

        Raises:
            Exception: Если выбор не распознан или рандомизация не найдена.
        """
        # проверяет, был ли рандомизирован выбор i
        if self.choices[i] == (0, 1):
            # если нет, возвращает выбор
            if blind_name == self.blind_name_a:
                return self.real_name_1
            elif blind_name == self.blind_name_b:
                return self.real_name_2
            elif blind_name in self.passtrough_name:
                return blind_name
            else:
                logger.error(f'Выбор \'{blind_name}\' не распознан')
                raise Exception(f'Выбор \'{blind_name}\' не распознан')
        elif self.choices[i] == (1, 0):
            # если да, возвращает противоположный выбор
            if blind_name == self.blind_name_a:
                return self.real_name_2
            elif blind_name == self.blind_name_b:
                return self.real_name_1
            elif blind_name in self.passtrough_name:
                return blind_name
            else:
                logger.error(f'Выбор \'{blind_name}\' не распознан')
                raise Exception(f'Выбор \'{blind_name}\' не распознан')
        else:
             logger.error(f'Рандомизация не найдена для элемента {i}')
             raise Exception(f'Рандомизация не найдена для элемента {i}')


# TODO under development
class Intervention:
    """
    Класс для представления вмешательства в эксперименте.
    """
    def __init__(self, agent: TinyPerson | None = None, agents: List[TinyPerson] | None = None, environment: Any = None, environments: List[Any] | None = None) -> None:
        """
        Инициализирует объект Intervention.

        Args:
            agent (TinyPerson, optional): Агент, к которому применяется вмешательство. Defaults to None.
            agents (list[TinyPerson], optional): Список агентов. Defaults to None.
            environment (Any, optional): Окружение, в котором применяется вмешательство. Defaults to None.
            environments (list[Any], optional): Список окружений. Defaults to None.

        Raises:
            Exception: Если переданы одновременно agent и agents или environment и environments.
            Exception: Если не передано ни одного из параметров.
        """
        # хотя бы один из параметров должен быть предоставлен. далее, либо одна сущность, либо список
        if agent and agents:
             logger.error('Должен быть предоставлен либо \'agent\', либо \'agents\', но не оба')
             raise Exception('Должен быть предоставлен либо \'agent\', либо \'agents\', но не оба')
        if environment and environments:
             logger.error('Должен быть предоставлен либо \'environment\', либо \'environments\', но не оба')
             raise Exception('Должен быть предоставлен либо \'environment\', либо \'environments\', но не оба')
        if not (agent or agents or environment or environments):
            logger.error('Необходимо предоставить хотя бы один из параметров')
            raise Exception('Необходимо предоставить хотя бы один из параметров')

        # инициализирует возможные сущности
        self.agents: List[TinyPerson] | None = None
        self.environments: List[Any] | None = None

        if agent is not None:
            self.agents = [agent]
        elif agents is not None:
            self.agents = agents
        elif environment is not None:
            self.environments = [environment]
        elif environments is not None:
             self.environments = environments


        # инициализирует возможные предварительные условия
        self.text_precondition: str | None = None
        self.precondition_func: Callable | None = None

        # эффекты
        self.effect_func: Callable | None = None

    ################################################################################################
    # Intervention flow
    ################################################################################################

    def check_precondition(self) -> bool:
        """
        Проверяет, выполнено ли предварительное условие для вмешательства.

        Raises:
            NotImplementedError: Метод должен быть переопределен в подклассе.
        """
        raise NotImplementedError('TO-DO')

    def apply(self) -> None:
        """
        Применяет вмешательство.
        """
        if self.effect_func:
            if self.agents and self.environments:
                self.effect_func(self.agents, self.environments)
            elif self.agents:
                self.effect_func(self.agents)
            elif self.environments:
                self.effect_func(self.environments)
            else:
                logger.error('Нет агентов или сред для применения эффекта')
                raise Exception('Нет агентов или сред для применения эффекта')
        else:
              logger.error('Функция эффекта не определена')
              raise Exception('Функция эффекта не определена')

    ################################################################################################
    # Pre and post conditions
    ################################################################################################

    def set_textual_precondition(self, text: str) -> None:
        """
        Устанавливает предварительное условие в виде текста.

        Args:
            text (str): Текст предварительного условия.
        """
        self.text_precondition = text

    def set_functional_precondition(self, func: Callable) -> None:
        """
        Устанавливает предварительное условие в виде функции.

        Args:
            func (Callable): Функция предварительного условия.
                Должна принимать аргументы: agent, agents, environment, environments.
        """
        self.precondition_func = func

    def set_effect(self, effect_func: Callable) -> None:
        """
        Устанавливает функцию, описывающую эффект вмешательства.

        Args:
            effect_func (Callable): Функция эффекта вмешательства.
        """
        self.effect_func = effect_func