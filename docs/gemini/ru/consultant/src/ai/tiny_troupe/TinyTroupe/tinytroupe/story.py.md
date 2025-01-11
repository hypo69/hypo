### Анализ кода модуля `story`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются аннотации типов.
    - Присутствует базовая документация в docstring.
    - Используется `utils.dedent` для форматирования строк.
- **Минусы**:
    - Не используется `from src.logger import logger` для логирования.
    - Есть  `try-except` блоки, которые можно заменить на `logger.error`.
    - В docstring отсутствуют примеры использования, rtype, raise
    - Не используется `j_loads`/`j_loads_ns` из `src.utils.jjson`
    - Не выровнены импорты
    - Присутствуют `"""` для многострочных комментариев и необходимо использовать `'''`

**Рекомендации по улучшению**:
- Добавить `from src.logger import logger` и использовать для логирования ошибок.
- Избегать использования `try-except`, заменяя их на `logger.error`.
- Добавить в docstring примеры использования, rtype, raise
- Заменить `"""` на `'''` для многострочных строк
- Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
- Выровнять названия функций, переменных и импортов.
- Добавить RST-документацию для всех функций и методов, включая описание параметров и возвращаемых значений.
-  Добавить комментарии к не очевидным участкам кода.

**Оптимизированный код**:

```python
'''
Every simulation tells a story. This module provides helper mechanisms to help with crafting appropriate stories in TinyTroupe.
'''

from typing import List
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils
from src.logger import logger #  Импортируем logger

class TinyStory:
    '''
    Provides helper mechanisms to craft stories in TinyTroupe.

    This class manages the story generation for a simulation,
    handling both environment and agent-centric narratives.
    It supports starting, continuing, and tracking the story
    based on simulation interactions.

    :ivar environment: The simulation environment, if applicable.
    :vartype environment: TinyWorld
    :ivar agent: The agent within the simulation, if applicable.
    :vartype agent: TinyPerson
    :ivar purpose: The guiding purpose of the story.
    :vartype purpose: str
    :ivar current_story: The current story context, to which new elements are appended.
    :vartype current_story: str
    :ivar first_n: Number of first interactions to include in the story.
    :vartype first_n: int
    :ivar last_n: Number of last interactions to include in the story.
    :vartype last_n: int
    :ivar include_omission_info: Flag to include information about omitted interactions.
    :vartype include_omission_info: bool
    '''
    def __init__(
        self,
        environment: TinyWorld = None,
        agent: TinyPerson = None,
        purpose: str = 'Be a realistic simulation.',
        context: str = '',
        first_n: int = 10,
        last_n: int = 20,
        include_omission_info: bool = True
    ) -> None:
        '''
        Initializes a new TinyStory instance.

        :param environment: The environment in which the story takes place.
        :type environment: TinyWorld, optional
        :param agent: The agent in the story.
        :type agent: TinyPerson, optional
        :param purpose: The purpose of the story.
        :type purpose: str, optional
        :param context: The current story context. The actual story will be appended to this context.
        :type context: str, optional
        :param first_n: The number of first interactions to include in the story.
        :type first_n: int, optional
        :param last_n: The number of last interactions to include in the story.
        :type last_n: int, optional
        :param include_omission_info: Whether to include information about omitted interactions.
        :type include_omission_info: bool, optional
        :raises Exception: If both environment and agent are provided or if neither is provided.
        
        :Example:
           >>> environment = TinyWorld()
           >>> story = TinyStory(environment=environment, purpose='Test story')
           >>> print(story.purpose)
           Test story
        '''

        if environment and agent:
            # логируем ошибку
            logger.error("Either 'environment' or 'agent' should be provided, not both")
            raise Exception("Either 'environment' or 'agent' should be provided, not both")
        if not (environment or agent):
            # логируем ошибку
            logger.error("At least one of the parameters should be provided")
            raise Exception("At least one of the parameters should be provided")

        self.environment = environment
        self.agent = agent

        self.purpose = purpose

        self.current_story = context

        self.first_n = first_n
        self.last_n = last_n
        self.include_omission_info = include_omission_info

    def start_story(self, requirements: str = 'Start some interesting story about the agents.', number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        '''
        Starts a new story.

        This method generates the initial part of the story based on the provided requirements and configurations.
        It leverages LLM (Language Model) to generate the story content.

        :param requirements: The specific requirements for starting the story.
        :type requirements: str, optional
        :param number_of_words: The desired number of words for the generated story.
        :type number_of_words: int, optional
        :param include_plot_twist: Whether to include a plot twist in the story.
        :type include_plot_twist: bool, optional
        :return: The generated start of the story.
        :rtype: str
        
        :Example:
            >>> story = TinyStory(environment=TinyWorld(), purpose='Test')
            >>> start = story.start_story(requirements='A test start')
            >>> print(start)
            ...
        '''
        rendering_configs = {
            'purpose': self.purpose,
            'requirements': requirements,
            'current_simulation_trace': self._current_story(),
            'number_of_words': number_of_words,
            'include_plot_twist': include_plot_twist
        }

        messages = utils.compose_initial_LLM_messages_with_templates('story.start.system.mustache', 'story.start.user.mustache', rendering_configs)
        next_message = openai_utils.client().send_message(messages, temperature=1.5)

        start = next_message['content']

        self.current_story += utils.dedent(
            f'''

            ## The story begins

            {start}

            '''
        )

        return start

    def continue_story(self, requirements: str = 'Continue the story in an interesting way.', number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        '''
        Continues the existing story.

        This method generates a continuation of the story based on the provided requirements and configurations.
        It utilizes LLM to create the next segment of the narrative.

        :param requirements: The specific requirements for continuing the story.
        :type requirements: str, optional
        :param number_of_words: The desired number of words for the generated story continuation.
        :type number_of_words: int, optional
        :param include_plot_twist: Whether to include a plot twist in the story continuation.
        :type include_plot_twist: bool, optional
        :return: The generated continuation of the story.
        :rtype: str
        
        :Example:
            >>> story = TinyStory(environment=TinyWorld(), purpose='Test')
            >>> start = story.start_story(requirements='A test start')
            >>> continuation = story.continue_story(requirements='Continue the test story')
            >>> print(continuation)
            ...
        '''
        rendering_configs = {
            'purpose': self.purpose,
            'requirements': requirements,
            'current_simulation_trace': self._current_story(),
            'number_of_words': number_of_words,
            'include_plot_twist': include_plot_twist
        }

        messages = utils.compose_initial_LLM_messages_with_templates('story.continuation.system.mustache', 'story.continuation.user.mustache', rendering_configs)
        next_message = openai_utils.client().send_message(messages, temperature=1.5)

        continuation = next_message['content']

        self.current_story += utils.dedent(
            f'''

            ## The story continues

            {continuation}

            '''
        )

        return continuation

    def _current_story(self) -> str:
        '''
        Retrieves the current story context including the latest simulation interactions.

        This method compiles the current story text along with the formatted simulation interactions
        from either the environment or the agent, depending on which is available.

        :return: The combined story context and formatted interaction history.
        :rtype: str
        
        :Example:
            >>> story = TinyStory(agent=TinyPerson())
            >>> story._current_story()
            '\\n\\n            ## New simulation interactions to consider\\n\\n            \\n\\n            '
        '''
        interaction_history = ''

        if self.agent is not None:
            interaction_history += self.agent.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        elif self.environment is not None:
            interaction_history += self.environment.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)

        self.current_story += utils.dedent(
            f'''

            ## New simulation interactions to consider

            {interaction_history}

            '''
        )

        return self.current_story