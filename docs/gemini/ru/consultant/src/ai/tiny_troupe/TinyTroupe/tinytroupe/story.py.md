# Анализ кода модуля `story.py`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован и разбит на логические блоки.
    -   Используются docstring для описания классов и методов.
    -   Присутствует обработка исключений для проверки параметров.
    -   Используются `f-strings` для форматирования строк.
    -   Есть возможность настройки количества первых и последних взаимодействий, включаемых в историю.
    -   Используется `utils.dedent` для удаления лишних отступов.
-   Минусы
    -   Отсутствует импорт `from src.logger.logger import logger` и логирование ошибок.
    -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    -   Не все комментарии приведены в формат RST.
    -   В некоторых местах комментарии после `#` не полностью объясняют логику кода.
    -   Используются стандартные блоки `try-except` вместо обработки ошибок с помощью `logger.error`.
    -   `temperature=1.5` - высокое значение, лучше сделать его настраиваемым параметром.
    -   Не все функции имеют описание в формате reStructuredText.
**Рекомендации по улучшению**
1.  Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
2.  Заменить стандартные `Exception` на более конкретные, при необходимости.
3.  Использовать `logger.error` для обработки ошибок вместо общих `try-except`.
4.  Все комментарии к функциям, методам и переменным должны быть переписаны в формате reStructuredText (RST).
5.  В комментариях после `#` строки должны содержать подробное объяснение следующего за ними блока кода.
6.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это необходимо. В данном случае это не требуется, так как нет чтения файлов.
7.  `temperature` сделать настраиваемым параметром.

**Оптимизированный код**
```python
"""
Модуль для создания и управления историями в TinyTroupe.
=========================================================================================

Этот модуль предоставляет класс :class:`TinyStory`, который помогает создавать
интересные истории на основе симуляций агентов или окружений.

Класс позволяет начать, продолжить историю, добавляя в неё контекст
и информацию о взаимодействиях.

Пример использования
--------------------

Пример создания и использования класса `TinyStory`:

.. code-block:: python

    from tinytroupe.environment import TinyWorld
    from tinytroupe.story import TinyStory

    world = TinyWorld()
    story = TinyStory(environment=world, purpose="Создать интересную историю")
    story.start_story(requirements="Начать историю о мире")
    story.continue_story(requirements="Продолжить историю")

"""

from typing import List
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils
from src.logger.logger import logger # Добавлен импорт logger


class TinyStory:
    """
    Класс для управления созданием и развитием истории на основе симуляций.
    
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
    :param include_omission_info: Включать ли информацию об опущенных взаимодействиях.
    :type include_omission_info: bool, optional
    """
    def __init__(self, environment: TinyWorld = None, agent: TinyPerson = None, purpose: str = "Be a realistic simulation.", context: str = "",
                 first_n: int = 10, last_n: int = 20, include_omission_info: bool = True) -> None:
        """
        Инициализация истории.

        История может быть о среде или об агенте. У нее также есть цель, которая
        используется для направления генерации истории. Истории знают, что они связаны с симуляциями,
        поэтому можно указать цели, связанные с симуляцией.
        
        :raises Exception: Если не передан ни агент, ни окружение, или переданы оба.
        """
        # проверка, что передан или агент, или окружение, но не оба
        if environment and agent:
            msg = "Either 'environment' or 'agent' should be provided, not both"
            logger.error(msg) # Логирование ошибки
            raise ValueError(msg) # Используется ValueError вместо общего Exception
        if not (environment or agent):
            msg = "At least one of the parameters should be provided"
            logger.error(msg) # Логирование ошибки
            raise ValueError(msg) # Используется ValueError вместо общего Exception
            
        self.environment = environment
        self.agent = agent

        self.purpose = purpose

        self.current_story = context

        self.first_n = first_n
        self.last_n = last_n
        self.include_omission_info = include_omission_info

    def start_story(self, requirements: str = "Start some interesting story about the agents.", number_of_words: int = 100, include_plot_twist: bool = False, temperature: float = 1.0) -> str:
        """
        Начать новую историю.

        :param requirements: Требования к началу истории.
        :type requirements: str, optional
        :param number_of_words: Количество слов в начале истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Включить ли в историю неожиданный поворот.
        :type include_plot_twist: bool, optional
        :param temperature: Температура для генерации текста.
        :type temperature: float, optional
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

        messages = utils.compose_initial_LLM_messages_with_templates("story.start.system.mustache", "story.start.user.mustache", rendering_configs)
        
        try:
            # Код отправляет сообщение и получает ответ от модели
            next_message = openai_utils.client().send_message(messages, temperature=temperature)
            start = next_message["content"]
        except Exception as ex:
             logger.error('Ошибка при отправке сообщения в LLM', exc_info=ex)
             return ""
        
        self.current_story += utils.dedent(
            f"""

            ## The story begins

            {start}

            """
        )
        return start

    def continue_story(self, requirements: str = "Continue the story in an interesting way.", number_of_words: int = 100, include_plot_twist: bool = False, temperature:float=1.0) -> str:
        """
        Предложить продолжение истории.

        :param requirements: Требования к продолжению истории.
        :type requirements: str, optional
        :param number_of_words: Количество слов в продолжении истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Включить ли в историю неожиданный поворот.
        :type include_plot_twist: bool, optional
        :param temperature: Температура для генерации текста.
        :type temperature: float, optional
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

        messages = utils.compose_initial_LLM_messages_with_templates("story.continuation.system.mustache", "story.continuation.user.mustache", rendering_configs)
        
        try:
            # Код отправляет сообщение и получает ответ от модели
            next_message = openai_utils.client().send_message(messages, temperature=temperature)
            continuation = next_message["content"]
        except Exception as ex:
            logger.error('Ошибка при отправке сообщения в LLM', exc_info=ex)
            return ""

        self.current_story += utils.dedent(
            f"""

            ## The story continues

            {continuation}

            """
        )

        return continuation

    def _current_story(self) -> str:
        """
        Получить текущую историю.

        :return: Текущая история.
        :rtype: str
        """
        interaction_history = ""
        
        # проверка, какой объект участвует в истории - агент или окружение
        if self.agent is not None:
             # код добавляет историю взаимодействий агента в строку
            interaction_history += self.agent.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        elif self.environment is not None:
             # код добавляет историю взаимодействий окружения в строку
            interaction_history += self.environment.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        
        self.current_story += utils.dedent(
            f"""

            ## New simulation interactions to consider

            {interaction_history}

            """
        )
            
        return self.current_story
```