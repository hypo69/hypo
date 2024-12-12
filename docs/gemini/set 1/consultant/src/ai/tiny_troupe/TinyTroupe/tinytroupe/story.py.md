## Улучшенный код
```python
"""
Модуль для создания и управления историями в симуляциях TinyTroupe.
=================================================================

Этот модуль предоставляет класс :class:`TinyStory`, который помогает создавать и
развивать истории, основанные на взаимодействиях агентов и окружающей среды в
симуляциях TinyTroupe.

Класс позволяет задавать цель истории, контекст, а также включать информацию о
пропущенных взаимодействиях.

Пример использования
--------------------

Пример создания и запуска истории для агента:

.. code-block:: python

    from tinytroupe.agent import TinyPerson
    from tinytroupe.story import TinyStory

    agent = TinyPerson()
    story = TinyStory(agent=agent, purpose="Интересная история о жизни агента")
    story.start_story(requirements="Начните с представления персонажа", number_of_words=50)
    story.continue_story(requirements="Развивайте сюжет", number_of_words=80)
    print(story.current_story)

"""
from typing import List
# Импортируем необходимые модули из пакета tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils
from src.logger.logger import logger


class TinyStory:
    """
    Класс для управления созданием и развитием историй на основе симуляций.
    
    :param environment: Окружение, в котором происходит история.
    :type environment: TinyWorld, optional
    :param agent: Агент, участвующий в истории.
    :type agent: TinyPerson, optional
    :param purpose: Цель истории.
    :type purpose: str, optional
    :param context: Начальный контекст истории.
    :type context: str, optional
    :param first_n: Количество первых взаимодействий для включения в историю.
    :type first_n: int, optional
    :param last_n: Количество последних взаимодействий для включения в историю.
    :type last_n: int, optional
    :param include_omission_info: Флаг для включения информации о пропущенных взаимодействиях.
    :type include_omission_info: bool, optional
    """

    def __init__(self, environment:TinyWorld=None, agent:TinyPerson=None, purpose:str="Be a realistic simulation.", context:str="",
                 first_n:int=10, last_n:int=20, include_omission_info:bool=True) -> None:
        """
        Инициализирует объект TinyStory.

        Инициализирует историю, которая может быть связана с окружением или агентом.
        У истории есть цель, которая используется для управления генерацией истории.
        Истории знают, что они связаны с симуляциями, поэтому можно указать цели, связанные с симуляцией.

        :param environment: Окружение, в котором происходит история.
        :type environment: TinyWorld, optional
        :param agent: Агент, участвующий в истории.
        :type agent: TinyPerson, optional
        :param purpose: Цель истории.
        :type purpose: str, optional
        :param context: Начальный контекст истории.
        :type context: str, optional
        :param first_n: Количество первых взаимодействий для включения в историю.
        :type first_n: int, optional
        :param last_n: Количество последних взаимодействий для включения в историю.
        :type last_n: int, optional
        :param include_omission_info: Флаг для включения информации о пропущенных взаимодействиях.
        :type include_omission_info: bool, optional
        """
        # Проверяется, что передан либо environment, либо agent, но не оба сразу
        if environment and agent:
            #  Выбрасывается исключение, если переданы оба параметра
            logger.error("Either \'environment\' or \'agent\' should be provided, not both")
            raise Exception("Either \'environment\' or \'agent\' should be provided, not both")
        # Проверяется, что передан хотя бы один из параметров
        if not (environment or agent):
            # Выбрасывается исключение, если не передан ни один из параметров
            logger.error("At least one of the parameters should be provided")
            raise Exception("At least one of the parameters should be provided")
        
        # Инициализируются атрибуты объекта
        self.environment = environment
        self.agent = agent

        self.purpose = purpose

        self.current_story = context

        self.first_n = first_n
        self.last_n = last_n
        self.include_omission_info = include_omission_info
    
    def start_story(self, requirements: str = "Start some interesting story about the agents.", number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        """
        Запускает новую историю.

        :param requirements: Требования к началу истории.
        :type requirements: str, optional
        :param number_of_words: Желаемое количество слов в начале истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Флаг для включения неожиданного поворота сюжета.
        :type include_plot_twist: bool, optional
        :return: Начало истории.
        :rtype: str
        """
        
        rendering_configs = {
                             "purpose": self.purpose,
                             "requirements": requirements,
                             "current_simulation_trace": self._current_story(),
                             "number_of_words": number_of_words,
                             "include_plot_twist": include_plot_twist
                            }
        # Формируются сообщения для языковой модели на основе шаблонов
        messages = utils.compose_initial_LLM_messages_with_templates("story.start.system.mustache", "story.start.user.mustache", rendering_configs)
        #  Отправляется запрос языковой модели для генерации начала истории
        next_message = openai_utils.client().send_message(messages, temperature=1.5)
        # Извлекается сгенерированное начало истории
        start = next_message["content"]
        # Добавляется начало истории к текущей истории
        self.current_story += utils.dedent(
            f"""

            ## The story begins

            {start}

            """
            )

        return start
    
    def continue_story(self, requirements: str = "Continue the story in an interesting way.", number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        """
        Предлагает продолжение истории.
        
        :param requirements: Требования к продолжению истории.
        :type requirements: str, optional
        :param number_of_words: Желаемое количество слов в продолжении истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Флаг для включения неожиданного поворота сюжета.
        :type include_plot_twist: bool, optional
        :return: Продолжение истории.
        :rtype: str
        """
        
        rendering_configs = {
                             "purpose": self.purpose,
                             "requirements": requirements,
                             "current_simulation_trace": self._current_story(),
                             "number_of_words": number_of_words,
                             "include_plot_twist": include_plot_twist
                            }
        # Формируются сообщения для языковой модели на основе шаблонов
        messages = utils.compose_initial_LLM_messages_with_templates("story.continuation.system.mustache", "story.continuation.user.mustache", rendering_configs)
        #  Отправляется запрос языковой модели для генерации продолжения истории
        next_message = openai_utils.client().send_message(messages, temperature=1.5)
        # Извлекается сгенерированное продолжение истории
        continuation = next_message["content"]
        # Добавляется продолжение истории к текущей истории
        self.current_story += utils.dedent(
            f"""

            ## The story continues

            {continuation}

            """
            )

        return continuation

    def _current_story(self) -> str:
        """
        Возвращает текущую историю с добавлением последних взаимодействий.
        
        :return: Текущая история с добавленными взаимодействиями.
        :rtype: str
        """
        # Инициализируется переменная для хранения истории взаимодействий
        interaction_history = ""
        # Проверяется, что агент определен
        if self.agent is not None:
            # Добавляются взаимодействия агента в историю
            interaction_history += self.agent.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        # Проверяется, что окружение определено
        elif self.environment is not None:
            # Добавляются взаимодействия окружения в историю
            interaction_history += self.environment.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        # Добавляется история взаимодействий к текущей истории
        self.current_story += utils.dedent(
            f"""

            ## New simulation interactions to consider

            {interaction_history}

            """
            )
        # Возвращается текущая история
        return self.current_story
```
## Внесённые изменения
1.  **Добавлено reStructuredText (RST) форматирование:**
    *   Добавлены docstring к модулю, классу и методам в формате RST.
    *   Добавлены описания параметров и возвращаемых значений для функций и методов.
    *   Добавлены примеры использования класса.
2.  **Импорт `logger`:**
    *   Добавлен импорт `from src.logger.logger import logger` для логирования ошибок.
3.  **Обработка ошибок:**
    *   Заменены `raise Exception` на `logger.error` с последующим `raise Exception`.
4.  **Комментарии в коде:**
    *   Добавлены комментарии к каждой строке кода, объясняющие ее действие.
5.  **Типизация:**
    *   Добавлена типизация параметров и возвращаемых значений функций и методов.
6.  **Улучшение читаемости:**
    *   Удалены лишние пустые строки для лучшей читаемости кода.
    *   Исправлено выравнивание.
7.  **Удалены неиспользуемые импорты:**
    *   Удален импорт `List`, так как он не использовался.
## Оптимизированный код
```python
"""
Модуль для создания и управления историями в симуляциях TinyTroupe.
=================================================================

Этот модуль предоставляет класс :class:`TinyStory`, который помогает создавать и
развивать истории, основанные на взаимодействиях агентов и окружающей среды в
симуляциях TinyTroupe.

Класс позволяет задавать цель истории, контекст, а также включать информацию о
пропущенных взаимодействиях.

Пример использования
--------------------

Пример создания и запуска истории для агента:

.. code-block:: python

    from tinytroupe.agent import TinyPerson
    from tinytroupe.story import TinyStory

    agent = TinyPerson()
    story = TinyStory(agent=agent, purpose="Интересная история о жизни агента")
    story.start_story(requirements="Начните с представления персонажа", number_of_words=50)
    story.continue_story(requirements="Развивайте сюжет", number_of_words=80)
    print(story.current_story)

"""
# Импортируем необходимые модули из пакета tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils
from src.logger.logger import logger


class TinyStory:
    """
    Класс для управления созданием и развитием историй на основе симуляций.
    
    :param environment: Окружение, в котором происходит история.
    :type environment: TinyWorld, optional
    :param agent: Агент, участвующий в истории.
    :type agent: TinyPerson, optional
    :param purpose: Цель истории.
    :type purpose: str, optional
    :param context: Начальный контекст истории.
    :type context: str, optional
    :param first_n: Количество первых взаимодействий для включения в историю.
    :type first_n: int, optional
    :param last_n: Количество последних взаимодействий для включения в историю.
    :type last_n: int, optional
    :param include_omission_info: Флаг для включения информации о пропущенных взаимодействиях.
    :type include_omission_info: bool, optional
    """

    def __init__(self, environment:TinyWorld=None, agent:TinyPerson=None, purpose:str="Be a realistic simulation.", context:str="",
                 first_n:int=10, last_n:int=20, include_omission_info:bool=True) -> None:
        """
        Инициализирует объект TinyStory.

        Инициализирует историю, которая может быть связана с окружением или агентом.
        У истории есть цель, которая используется для управления генерацией истории.
        Истории знают, что они связаны с симуляциями, поэтому можно указать цели, связанные с симуляцией.

        :param environment: Окружение, в котором происходит история.
        :type environment: TinyWorld, optional
        :param agent: Агент, участвующий в истории.
        :type agent: TinyPerson, optional
        :param purpose: Цель истории.
        :type purpose: str, optional
        :param context: Начальный контекст истории.
        :type context: str, optional
        :param first_n: Количество первых взаимодействий для включения в историю.
        :type first_n: int, optional
        :param last_n: Количество последних взаимодействий для включения в историю.
        :type last_n: int, optional
        :param include_omission_info: Флаг для включения информации о пропущенных взаимодействиях.
        :type include_omission_info: bool, optional
        """
        # Проверяется, что передан либо environment, либо agent, но не оба сразу
        if environment and agent:
            #  Выбрасывается исключение, если переданы оба параметра
            logger.error("Either \'environment\' or \'agent\' should be provided, not both")
            raise Exception("Either \'environment\' or \'agent\' should be provided, not both")
        # Проверяется, что передан хотя бы один из параметров
        if not (environment or agent):
            # Выбрасывается исключение, если не передан ни один из параметров
            logger.error("At least one of the parameters should be provided")
            raise Exception("At least one of the parameters should be provided")
        
        # Инициализируются атрибуты объекта
        self.environment = environment
        self.agent = agent

        self.purpose = purpose

        self.current_story = context

        self.first_n = first_n
        self.last_n = last_n
        self.include_omission_info = include_omission_info
    
    def start_story(self, requirements: str = "Start some interesting story about the agents.", number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        """
        Запускает новую историю.

        :param requirements: Требования к началу истории.
        :type requirements: str, optional
        :param number_of_words: Желаемое количество слов в начале истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Флаг для включения неожиданного поворота сюжета.
        :type include_plot_twist: bool, optional
        :return: Начало истории.
        :rtype: str
        """
        
        rendering_configs = {
                             "purpose": self.purpose,
                             "requirements": requirements,
                             "current_simulation_trace": self._current_story(),
                             "number_of_words": number_of_words,
                             "include_plot_twist": include_plot_twist
                            }
        # Формируются сообщения для языковой модели на основе шаблонов
        messages = utils.compose_initial_LLM_messages_with_templates("story.start.system.mustache", "story.start.user.mustache", rendering_configs)
        #  Отправляется запрос языковой модели для генерации начала истории
        next_message = openai_utils.client().send_message(messages, temperature=1.5)
        # Извлекается сгенерированное начало истории
        start = next_message["content"]
        # Добавляется начало истории к текущей истории
        self.current_story += utils.dedent(
            f"""

            ## The story begins

            {start}

            """
            )

        return start
    
    def continue_story(self, requirements: str = "Continue the story in an interesting way.", number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        """
        Предлагает продолжение истории.
        
        :param requirements: Требования к продолжению истории.
        :type requirements: str, optional
        :param number_of_words: Желаемое количество слов в продолжении истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Флаг для включения неожиданного поворота сюжета.
        :type include_plot_twist: bool, optional
        :return: Продолжение истории.
        :rtype: str
        """
        
        rendering_configs = {
                             "purpose": self.purpose,
                             "requirements": requirements,
                             "current_simulation_trace": self._current_story(),
                             "number_of_words": number_of_words,
                             "include_plot_twist": include_plot_twist
                            }
        # Формируются сообщения для языковой модели на основе шаблонов
        messages = utils.compose_initial_LLM_messages_with_templates("story.continuation.system.mustache", "story.continuation.user.mustache", rendering_configs)
        #  Отправляется запрос языковой модели для генерации продолжения истории
        next_message = openai_utils.client().send_message(messages, temperature=1.5)
        # Извлекается сгенерированное продолжение истории
        continuation = next_message["content"]
        # Добавляется продолжение истории к текущей истории
        self.current_story += utils.dedent(
            f"""

            ## The story continues

            {continuation}

            """
            )

        return continuation

    def _current_story(self) -> str:
        """
        Возвращает текущую историю с добавлением последних взаимодействий.
        
        :return: Текущая история с добавленными взаимодействиями.
        :rtype: str
        """
        # Инициализируется переменная для хранения истории взаимодействий
        interaction_history = ""
        # Проверяется, что агент определен
        if self.agent is not None:
            # Добавляются взаимодействия агента в историю
            interaction_history += self.agent.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        # Проверяется, что окружение определено
        elif self.environment is not None:
            # Добавляются взаимодействия окружения в историю
            interaction_history += self.environment.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        # Добавляется история взаимодействий к текущей истории
        self.current_story += utils.dedent(
            f"""

            ## New simulation interactions to consider

            {interaction_history}

            """
            )
        # Возвращается текущая история
        return self.current_story