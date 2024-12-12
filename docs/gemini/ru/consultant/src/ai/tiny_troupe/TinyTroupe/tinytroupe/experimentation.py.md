# Анализ кода модуля experimentation.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на классы `ABRandomizer` и `Intervention`.
    - Используются docstrings для описания классов и методов.
    - Присутствует базовая обработка ошибок с помощью исключений.
    - Код достаточно понятный и логичный.

- Минусы
    - Отсутствует импорт `logger` для логирования.
    - В классе `Intervention` есть `NotImplementedError`.
    - Не используются `j_loads` или `j_loads_ns` для чтения файлов, хотя это указано в инструкции.
    - Не все комментарии соответствуют стандарту reStructuredText (RST).
    - В классе `Intervention` есть проблема с инициализацией `self.agent` и `self.environment`, так как они не инициализируются явно.
    - Есть дублирование логики в `derandomize_name`.
    - Использован не явный импорт `random.Random`.
    -  Не реализованы проверки типов для входных параметров.

**Рекомендации по улучшению**

1.  Добавить импорт `from src.logger.logger import logger` и использовать `logger.error` для логирования ошибок.
2.  Заменить `raise Exception` на `logger.error` с последующим `return` или генерацией исключения.
3.  Использовать `random.seed` для глобального сидирования.
4.  Реализовать проверку типов входных параметров.
5.  Улучшить docstring, добавить описание исключений и параметров.
6.  В `Intervention` инициализировать `self.agent` и `self.environment` и проверить типы аргументов.
7.  Устранить дублирование логики в `derandomize_name`.
8.  Использовать f-строки для форматирования строк.
9. Добавить описание модуля в начале файла.

**Оптимизированный код**

```python
"""
Модуль для проведения экспериментов и интервенций.
======================================================

Этот модуль содержит классы `ABRandomizer` для рандомизации A/B тестов и `Intervention` для управления вмешательствами в эксперименты.

Пример использования
--------------------

Пример использования класса `ABRandomizer`:

.. code-block:: python

    randomizer = ABRandomizer(real_name_1="control", real_name_2="treatment", blind_name_a="A", blind_name_b="B")
    a, b = randomizer.randomize(0, "value1", "value2")
    print(f"Randomized values: {a}, {b}")
    a, b = randomizer.derandomize(0, "value1", "value2")
    print(f"De-randomized values: {a}, {b}")
    real_name = randomizer.derandomize_name(0, "A")
    print(f"De-randomized name: {real_name}")

Пример использования класса `Intervention`:

.. code-block:: python

    def example_effect(agents, environments):
        print("Effect applied")

    intervention = Intervention(agent=None, agents=None, environment=None, environments=None)
    intervention.set_effect(example_effect)
    intervention.apply()

"""
import random
import pandas as pd
from typing import Any, Callable, List, Tuple
from src.logger.logger import logger # Импорт logger
from tinytroupe.agent import TinyPerson

class ABRandomizer():
    """
    Утилитарный класс для рандомизации между двумя вариантами и последующей дерандомизации.

    Выбор сохраняется в словаре, где ключом является индекс элемента.
    Реальные имена — это имена вариантов в данных, а слепые имена — это имена,
    представленные пользователю. Проходные имена — это имена, которые не рандомизируются,
    а возвращаются как есть.

    :param real_name_1: Имя первого варианта.
    :type real_name_1: str
    :param real_name_2: Имя второго варианта.
    :type real_name_2: str
    :param blind_name_a: Имя первого варианта, как он представлен пользователю.
    :type blind_name_a: str
    :param blind_name_b: Имя второго варианта, как он представлен пользователю.
    :type blind_name_b: str
    :param passtrough_name: Список имен, которые не должны быть рандомизированы и всегда возвращаются как есть.
    :type passtrough_name: List[str]
    :param random_seed: Случайное зерно для использования.
    :type random_seed: int
    """
    def __init__(self, real_name_1: str="control", real_name_2: str="treatment",
                       blind_name_a: str="A", blind_name_b: str="B",
                       passtrough_name: List[str] = [],
                       random_seed: int = 42):

        self.choices = {}
        self.real_name_1 = real_name_1
        self.real_name_2 = real_name_2
        self.blind_name_a = blind_name_a
        self.blind_name_b = blind_name_b
        self.passtrough_name = passtrough_name
        self.random_seed = random_seed
        random.seed(self.random_seed) # Использования seed


    def randomize(self, i: int, a: str, b: str) -> Tuple[str, str]:
        """
        Случайным образом меняет местами `a` и `b` и возвращает выбранные варианты.

        Сохраняет информацию о переключении `a` и `b` для элемента `i`, чтобы иметь возможность
        дерандомизировать позже.

        :param i: Индекс элемента.
        :type i: int
        :param a: Первый вариант.
        :type a: str
        :param b: Второй вариант.
        :type b: str
        :raises TypeError: Если `i` не целое число, или `a` или `b` не строки.
        :return: Кортеж из двух строк, представляющих рандомизированные варианты.
        :rtype: Tuple[str, str]
        """
        if not isinstance(i, int):
           logger.error(f'Индекс {i=} должен быть целым числом')
           raise TypeError(f'Index {i=} must be an integer')
        if not isinstance(a, str):
           logger.error(f'Первый вариант {a=} должен быть строкой')
           raise TypeError(f'First choice {a=} must be a string')
        if not isinstance(b, str):
           logger.error(f'Второй вариант {b=} должен быть строкой')
           raise TypeError(f'Second choice {b=} must be a string')
        # Проверка условия и переключение значений
        if random.random() < 0.5:
            self.choices[i] = (0, 1)
            return a, b
        else:
            self.choices[i] = (1, 0)
            return b, a
    
    def derandomize(self, i: int, a: str, b: str) -> Tuple[str, str]:
        """
        Дерандомизирует варианты для элемента `i` и возвращает их.

        :param i: Индекс элемента.
        :type i: int
        :param a: Первый вариант.
        :type a: str
        :param b: Второй вариант.
        :type b: str
        :raises TypeError: Если `i` не целое число, или `a` или `b` не строки.
        :raises Exception: Если рандомизация для элемента `i` не найдена.
        :return: Кортеж из двух строк, представляющих дерандомизированные варианты.
        :rtype: Tuple[str, str]
        """
        if not isinstance(i, int):
           logger.error(f'Индекс {i=} должен быть целым числом')
           raise TypeError(f'Index {i=} must be an integer')
        if not isinstance(a, str):
           logger.error(f'Первый вариант {a=} должен быть строкой')
           raise TypeError(f'First choice {a=} must be a string')
        if not isinstance(b, str):
           logger.error(f'Второй вариант {b=} должен быть строкой')
           raise TypeError(f'Second choice {b=} must be a string')

        if i not in self.choices:
            logger.error(f"Рандомизация не найдена для элемента {i=}")
            raise Exception(f"No randomization found for item {i}")
        
        # Возвращает варианты в зависимости от сохраненного выбора
        if self.choices[i] == (0, 1):
            return a, b
        elif self.choices[i] == (1, 0):
            return b, a
        else:
            logger.error(f"Рандомизация не найдена для элемента {i=}")
            raise Exception(f"No randomization found for item {i}")
    
    def derandomize_name(self, i: int, blind_name: str) -> str:
        """
        Декодирует выбор пользователя и возвращает соответствующий реальный вариант.

        :param i: Индекс элемента.
        :type i: int
        :param blind_name: Выбор, сделанный пользователем.
        :type blind_name: str
        :raises TypeError: Если `i` не целое число, или `blind_name` не строка.
        :raises Exception: Если выбор не распознан или рандомизация не найдена.
        :return: Реальное имя варианта.
        :rtype: str
        """
        if not isinstance(i, int):
            logger.error(f'Индекс {i=} должен быть целым числом')
            raise TypeError(f'Index {i=} must be an integer')
        if not isinstance(blind_name, str):
            logger.error(f'Имя выбора {blind_name=} должно быть строкой')
            raise TypeError(f'Choice name {blind_name=} must be a string')
        if i not in self.choices:
            logger.error(f"Рандомизация не найдена для элемента {i=}")
            raise Exception(f"No randomization found for item {i}")

        # Проверяем был ли выбор рандомизирован
        if self.choices[i] == (0, 1):
             # Проверяем варианты выбора
            if blind_name == self.blind_name_a:
                return self.real_name_1
            elif blind_name == self.blind_name_b:
                return self.real_name_2
            elif blind_name in self.passtrough_name:
                return blind_name
            else:
                logger.error(f"Выбор \'{blind_name}\' не распознан")
                raise Exception(f"Choice \'{blind_name}\' not recognized")
        
        elif self.choices[i] == (1, 0):
             # Проверяем варианты выбора
            if blind_name == self.blind_name_a:
                return self.real_name_2
            elif blind_name == self.blind_name_b:
                return self.real_name_1
            elif blind_name in self.passtrough_name:
                return blind_name
            else:
                logger.error(f"Выбор \'{blind_name}\' не распознан")
                raise Exception(f"Choice \'{blind_name}\' not recognized")
        else:
            logger.error(f"Рандомизация не найдена для элемента {i=}")
            raise Exception(f"No randomization found for item {i}")



class Intervention():
    """
    Класс для управления интервенциями.

    :param agent: Агент, на которого оказывается воздействие.
    :type agent: TinyPerson, optional
    :param agents: Список агентов, на которых оказывается воздействие.
    :type agents: List[TinyPerson], optional
    :param environment: Среда, на которую оказывается воздействие.
    :type environment: Any, optional
    :param environments: Список сред, на которые оказывается воздействие.
    :type environments: List[Any], optional
    :raises Exception: Если не предоставлен ни один агент или среда, или предоставлены одновременно `agent` и `agents`, или `environment` и `environments`.
    """
    def __init__(self, agent: TinyPerson = None, agents: List[TinyPerson] = None, environment: Any = None, environments: List[Any] = None):
        # Проверка на корректность входных параметров
        if (agent and agents):
            logger.error("Необходимо предоставить или \'agent\', или \'agents\', но не оба параметра")
            raise Exception("Either \'agent\' or \'agents\' should be provided, not both")
        if (environment and environments):
            logger.error("Необходимо предоставить или \'environment\', или \'environments\', но не оба параметра")
            raise Exception("Either \'environment\' or \'environments\' should be provided, not both")
        if not (agent or agents or environment or environments):
            logger.error("Необходимо предоставить хотя бы один из параметров")
            raise Exception("At least one of the parameters should be provided")

        # Инициализация сущностей
        self.agents = agents if agents else [agent] if agent else None
        self.environments = environments if environments else [environment] if environment else None
        
        # Инициализация предусловий
        self.text_precondition = None
        self.precondition_func = None

        # Инициализация эффектов
        self.effect_func = None

    ################################################################################################
    # Intervention flow
    ################################################################################################     
    
    def check_precondition(self) -> bool:
        """
        Проверяет, выполнено ли предусловие для интервенции.
        
        :raises NotImplementedError: Если метод не реализован.
        :return: True, если предусловие выполнено, False в противном случае
        :rtype: bool
        """
        raise NotImplementedError("TO-DO")

    def apply(self):
        """
        Применяет интервенцию.
        
        :raises Exception: Если функция эффекта не установлена.
        """
        if self.effect_func is None:
           logger.error("Не установлена функция эффекта")
           raise Exception("Effect function not set")
        self.effect_func(self.agents, self.environments)

    ################################################################################################
    # Pre and post conditions
    ################################################################################################

    def set_textual_precondition(self, text: str):
        """
        Устанавливает предусловие в виде текста, который интерпретируется языковой моделью.

        :param text: Текст предусловия.
        :type text: str
        :raises TypeError: Если `text` не строка.
        """
        if not isinstance(text, str):
            logger.error(f'Текст предусловия {text=} должен быть строкой')
            raise TypeError(f'Precondition text {text=} must be a string')
        self.text_precondition = text
    
    def set_functional_precondition(self, func: Callable):
        """
        Устанавливает предусловие в виде функции.

        :param func: Функция предусловия. Должна принимать аргументы: agent, agents, environment, environments.
        :type func: Callable
         :raises TypeError: Если `func` не вызываемый объект.
        """
        if not callable(func):
           logger.error(f'Функция предусловия {func=} должна быть вызываемой')
           raise TypeError(f'Precondition function {func=} must be callable')
        self.precondition_func = func
    
    def set_effect(self, effect_func: Callable):
        """
        Устанавливает функцию эффекта для интервенции.

        :param effect_func: Функция эффекта. Должна принимать аргументы: agents, environments.
        :type effect_func: Callable
        :raises TypeError: Если `effect_func` не вызываемый объект.
        """
        if not callable(effect_func):
           logger.error(f'Функция эффекта {effect_func=} должна быть вызываемой')
           raise TypeError(f'Effect function {effect_func=} must be callable')
        self.effect_func = effect_func