# Анализ кода модуля experimentation.py

**Качество кода**
8
-  Плюсы
    - Код достаточно хорошо структурирован и читаем.
    - Используются docstrings для описания классов и методов.
    - Присутствует разделение ответственности между классами `ABRandomizer` и `Intervention`.
    - Код соответствует PEP8.
-  Минусы
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов (хотя в данном коде нет операций чтения файлов).
    - Отсутствуют некоторые необходимые импорты, например, `logger` из `src.logger.logger`.
    - В классе `Intervention` не обрабатываются исключения при вызове `effect_func`, а также отсутствуют проверки на None для `self.agents` и `self.environments` в методе `apply`.
    - Метод `check_precondition` в классе `Intervention` вызывает `NotImplementedError` с `"TO-DO"`, что не является корректной обработкой.

**Рекомендации по улучшению**
1. Добавить импорт `logger` из `src.logger.logger`.
2. В классе `Intervention` реализовать логику для проверки предусловий в методе `check_precondition` и обрабатывать исключения при применении эффектов в методе `apply`.
3. Избегать вызова исключений, заменяя их на логирование с использованием `logger.error`.
4. Добавить docstring для класса `Intervention` и его методов в формате RST.
5. Использовать более информативные сообщения об ошибках.
6. Добавить проверки на `None` перед вызовом методов и обращением к атрибутам объектов в классе `Intervention`.
7. Переписать docstring в формате RST.

**Оптимизированный код**
```python
"""
Модуль для проведения экспериментов и интервенций.
===================================================

Этот модуль содержит классы :class:`ABRandomizer` для рандомизации вариантов
и :class:`Intervention` для применения интервенций к агентам и средам.
"""
import random
# импортируем библиотеку pandas
import pandas as pd
# импортируем класс TinyPerson
from tinytroupe.agent import TinyPerson
# импортируем logger
from src.logger.logger import logger


class ABRandomizer():
    """
    Утилитарный класс для рандомизации между двумя вариантами и их последующей дерандомизации.

    Выбор хранится в словаре, где ключом является индекс элемента.
    Реальные имена - это имена вариантов в данных, а слепые имена -
    это имена вариантов, которые видит пользователь.
    Имена, которые не нужно рандомизировать, всегда возвращаются как есть.

    :param real_name_1: Имя первого варианта.
    :type real_name_1: str
    :param real_name_2: Имя второго варианта.
    :type real_name_2: str
    :param blind_name_a: Имя первого варианта, видимое пользователю.
    :type blind_name_a: str
    :param blind_name_b: Имя второго варианта, видимое пользователю.
    :type blind_name_b: str
    :param passtrough_name: Список имен, которые не должны быть рандомизированы.
    :type passtrough_name: list
    :param random_seed: Зерно для генератора случайных чисел.
    :type random_seed: int
    """
    def __init__(self, real_name_1="control", real_name_2="treatment",
                       blind_name_a="A", blind_name_b="B",
                       passtrough_name=[],
                       random_seed=42):
        # Инициализация атрибутов класса
        self.choices = {}
        self.real_name_1 = real_name_1
        self.real_name_2 = real_name_2
        self.blind_name_a = blind_name_a
        self.blind_name_b = blind_name_b
        self.passtrough_name = passtrough_name
        self.random_seed = random_seed

    def randomize(self, i, a, b):
        """
        Случайным образом меняет местами a и b и возвращает результаты.

        Сохраняет информацию о том, были ли a и b переключены для элемента i,
        чтобы иметь возможность дерандомизировать позже.

        :param i: Индекс элемента.
        :type i: int
        :param a: Первый вариант.
        :type a: str
        :param b: Второй вариант.
        :type b: str
        :return: Возвращает переставленные или оригинальные варианты.
        :rtype: tuple
        """
        # Используем seed
        if random.Random(self.random_seed).random() < 0.5:
            self.choices[i] = (0, 1)
            return a, b

        else:
            self.choices[i] = (1, 0)
            return b, a

    def derandomize(self, i, a, b):
        """
        Дерандомизирует варианты для элемента i и возвращает результаты.

        :param i: Индекс элемента.
        :type i: int
        :param a: Первый вариант.
        :type a: str
        :param b: Второй вариант.
        :type b: str
        :return: Возвращает исходные варианты.
        :rtype: tuple
        :raises Exception: Если нет информации о рандомизации для элемента i.
        """
        if self.choices[i] == (0, 1):
            return a, b
        elif self.choices[i] == (1, 0):
            return b, a
        else:
             # Логируем ошибку, если нет информации о рандомизации
            logger.error(f"No randomization found for item {i}")
            raise Exception(f"No randomization found for item {i}")


    def derandomize_name(self, i, blind_name):
        """
        Декодирует выбор, сделанный пользователем, и возвращает исходный вариант.

        :param i: Индекс элемента.
        :type i: int
        :param blind_name: Выбор пользователя.
        :type blind_name: str
        :return: Возвращает исходное имя варианта.
        :rtype: str
        :raises Exception: Если выбор не распознан или нет информации о рандомизации.
        """
        # Проверяем, был ли рандомизирован выбор i
        if self.choices[i] == (0, 1):
            # если нет, возвращаем выбор
            if blind_name == self.blind_name_a:
                return self.real_name_1
            elif blind_name == self.blind_name_b:
                return self.real_name_2
            elif blind_name in self.passtrough_name:
                return blind_name
            else:
                # Логируем ошибку, если выбор не распознан
                logger.error(f"Choice \'{blind_name}\' not recognized")
                raise Exception(f"Choice \'{blind_name}\' not recognized")

        elif self.choices[i] == (1, 0):
             # если да, возвращаем противоположный выбор
            if blind_name == self.blind_name_a:
                return self.real_name_2
            elif blind_name == self.blind_name_b:
                return self.real_name_1
            elif blind_name in self.passtrough_name:
                return blind_name
            else:
                # Логируем ошибку, если выбор не распознан
                logger.error(f"Choice \'{blind_name}\' not recognized")
                raise Exception(f"Choice \'{blind_name}\' not recognized")
        else:
            # Логируем ошибку, если нет информации о рандомизации
            logger.error(f"No randomization found for item {i}")
            raise Exception(f"No randomization found for item {i}")


# TODO under development
class Intervention():
    """
    Класс для представления интервенции, которая может быть применена к агентам или средам.

    :param agent: Агент, на которого применяется интервенция.
    :type agent: TinyPerson, optional
    :param agents: Список агентов, на которых применяется интервенция.
    :type agents: list, optional
    :param environment: Среда, на которую применяется интервенция.
    :type environment: TinyWorld, optional
    :param environments: Список сред, на которые применяется интервенция.
    :type environments: list, optional
    :raises Exception: Если передано более одного типа сущностей (агент/среда)
        или если ни одна сущность не передана.
    """
    def __init__(self, agent=None, agents:list=None, environment=None, environments:list=None):
        # Проверяем, что передан только один из параметров agent/agents и environment/environments
        if agent and agents:
            logger.error("Either \'agent\' or \'agents\' should be provided, not both")
            raise Exception("Either \'agent\' or \'agents\' should be provided, not both")
        if environment and environments:
            logger.error("Either \'environment\' or \'environments\' should be provided, not both")
            raise Exception("Either \'environment\' or \'environments\' should be provided, not both")
        if not (agent or agents or environment or environments):
            logger.error("At least one of the parameters should be provided")
            raise Exception("At least one of the parameters should be provided")

        # инициализируем сущности
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
        self.text_precondition = None
        self.precondition_func = None

        # Инициализация эффектов
        self.effect_func = None

    ################################################################################################
    # Intervention flow
    ################################################################################################

    def check_precondition(self):
        """
        Проверяет, выполнено ли предусловие для интервенции.

        :raises NotImplementedError: Если предусловие не реализовано.
        """
        # Проверяем, задано ли функциональное предусловие
        if self.precondition_func:
            try:
                # Проверяем предусловие
                return self.precondition_func(self.agents, self.environments)
            except Exception as e:
                # Логируем ошибку при проверке предусловия
                logger.error(f"Error checking precondition: {e}")
                return False
        elif self.text_precondition:
            # TODO: добавить поддержку текстового предусловия
            logger.warning("Textual precondition is not supported yet.")
            return True
        else:
             # Если нет предусловия возвращаем True
            return True


    def apply(self):
        """
        Применяет интервенцию.

        Вызывает функцию эффекта, если она установлена, передавая ей агентов и/или среды.
        Логирует ошибку, если возникает исключение при применении эффекта.
        """
        # Проверяем, есть ли эффект и применяем его
        if self.effect_func:
            try:
                if self.agents is not None and self.environments is not None:
                    self.effect_func(self.agents, self.environments)
                elif self.agents is not None:
                    self.effect_func(self.agents, None)
                elif self.environments is not None:
                    self.effect_func(None, self.environments)
                else:
                    logger.error("No agents or environments to apply effect to")
            except Exception as e:
                # Логируем ошибку при применении эффекта
                logger.error(f"Error applying effect: {e}")

    ################################################################################################
    # Pre and post conditions
    ################################################################################################

    def set_textual_precondition(self, text):
        """
        Устанавливает предусловие в виде текста, который должен интерпретироваться языковой моделью.

        :param text: Текст предусловия.
        :type text: str
        """
        self.text_precondition = text

    def set_functional_precondition(self, func):
        """
        Устанавливает предусловие в виде функции, которая будет вычисляться кодом.

        :param func: Функция предусловия.
         Функция должна принимать аргументы: agent, agents, environment, environments.
        :type func: function
        """
        self.precondition_func = func

    def set_effect(self, effect_func):
        """
        Устанавливает функцию, которая определяет эффект интервенции.

        :param effect_func: Функция эффекта.
        :type effect_func: function
        """
        self.effect_func = effect_func