# Анализ кода модуля `story`

**Качество кода**
-  Соответствие требованиям: 8/10
 -  Плюсы
    - Код хорошо структурирован и логически понятен.
    - Используются аннотации типов для улучшения читаемости и предотвращения ошибок.
    -  Применяется `utils.dedent` для форматирования строк.
    -  Функции имеют docstring, что соответствует стандартам документирования.
    -  Используются f-строки для форматирования.
    -  Обработка ошибок присутствует.
 -  Минусы
    -  Не все импорты соответствуют принятым стандартам, например `from src.logger import logger` отсутствует.
    -  Не используются `j_loads` или `j_loads_ns`.
    -  Не все комментарии в формате RST.
    -  Не все docstring в формате RST.

**Рекомендации по улучшению**

1.  **Импорты**:
    -   Добавить `from src.logger.logger import logger` для логирования.
    -   Импортировать `Path` из `pathlib`.

2.  **Форматирование**:
    -   Исправить docstring в формате RST.
    -   Добавить комментарии в формате RST для каждой функции и метода.
    -   Использовать одинарные кавычки для строк в коде.
    -   Использовать двойные кавычки только для вывода.
    
3.  **Обработка ошибок**:
    -   Заменить общий `Exception` на конкретный тип исключения, если это возможно.
    -   Использовать `logger.error` для логирования ошибок.

4.  **Сопровождение кода**:
    -   Добавить описание модуля.
    -   Добавить примеры использования.

**Оптимизиробанный код**

```python
"""
Модуль для создания и управления историями в симуляциях TinyTroupe.
=================================================================

Этот модуль предоставляет класс :class:`TinyStory`, который помогает создавать и развивать истории
в контексте симуляций с агентами и окружениями.

Примеры использования
--------------------

Пример создания и начала истории с агентом:

.. code-block:: python

    from tinytroupe.agent import TinyPerson
    from tinytroupe.story import TinyStory

    agent = TinyPerson()
    story = TinyStory(agent=agent, purpose='Изучение поведения агента')
    start_text = story.start_story(requirements='Интересное начало о жизни агента')
    print(start_text)

Пример создания и продолжения истории с окружением:

.. code-block:: python

    from tinytroupe.environment import TinyWorld
    from tinytroupe.story import TinyStory

    env = TinyWorld()
    story = TinyStory(environment=env, purpose='Описание изменений в мире')
    start_text = story.start_story(requirements='Завязка сюжета', number_of_words=150)
    print(start_text)
    continue_text = story.continue_story(requirements='Развитие сюжета', number_of_words=120)
    print(continue_text)
"""
from typing import List
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils
from src.logger.logger import logger  #  Импорт logger
from pathlib import Path # Импорт Path


class TinyStory:
    """
    Класс для управления историями в симуляциях TinyTroupe.

    :param environment: Окружение, в котором происходит история.
    :type environment: TinyWorld, optional
    :param agent: Агент, участвующий в истории.
    :type agent: TinyPerson, optional
    :param purpose: Цель истории.
    :type purpose: str, optional
    :param context: Текущий контекст истории.
    :type context: str, optional
    :param first_n: Количество первых взаимодействий для включения в историю.
    :type first_n: int, optional
    :param last_n: Количество последних взаимодействий для включения в историю.
    :type last_n: int, optional
    :param include_omission_info: Включать ли информацию об опущенных взаимодействиях.
    :type include_omission_info: bool, optional
    """
    def __init__(self, environment: TinyWorld = None, agent: TinyPerson = None, purpose: str = 'Be a realistic simulation.', context: str = '',
                 first_n: int = 10, last_n: int = 20, include_omission_info: bool = True) -> None:
        """
        Инициализация объекта истории.

        Args:
            environment (TinyWorld, optional): Окружение, в котором происходит история. Defaults to None.
            agent (TinyPerson, optional): Агент, участвующий в истории. Defaults to None.
            purpose (str, optional): Цель истории. Defaults to "Be a realistic simulation.".
            context (str, optional): Текущий контекст истории. Defaults to "".
            first_n (int, optional): Количество первых взаимодействий для включения в историю. Defaults to 10.
            last_n (int, optional): Количество последних взаимодействий для включения в историю. Defaults to 20.
            include_omission_info (bool, optional): Включать ли информацию об опущенных взаимодействиях. Defaults to True.

        Raises:
             Exception: Если переданы и агент, и окружение, или если не передан ни один из них.
        """
        # Проверка на корректность входных параметров
        if environment and agent:
            raise Exception('Either \'environment\' or \'agent\' should be provided, not both')
        if not (environment or agent):
            raise Exception('At least one of the parameters should be provided')
        
        self.environment = environment
        self.agent = agent

        self.purpose = purpose

        self.current_story = context

        self.first_n = first_n
        self.last_n = last_n
        self.include_omission_info = include_omission_info
    
    def start_story(self, requirements: str = 'Start some interesting story about the agents.', number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        """
        Начинает новую историю.

        Args:
            requirements (str, optional): Требования к началу истории. Defaults to "Start some interesting story about the agents.".
            number_of_words (int, optional): Количество слов в начале истории. Defaults to 100.
            include_plot_twist (bool, optional): Включать ли сюжетный поворот. Defaults to False.

        Returns:
            str: Начало истории.
        """
        # Конфигурация для генерации начала истории
        rendering_configs = {
                             'purpose': self.purpose,
                             'requirements': requirements,
                             'current_simulation_trace': self._current_story(),
                             'number_of_words': number_of_words,
                             'include_plot_twist': include_plot_twist
                            }

        #  Формирование сообщений для LLM с использованием шаблонов
        messages = utils.compose_initial_LLM_messages_with_templates('story.start.system.mustache', 'story.start.user.mustache', rendering_configs)
        #  Отправка запроса в LLM
        try:
            next_message = openai_utils.client().send_message(messages, temperature=1.5)
        except Exception as ex:
            logger.error('Ошибка при отправке сообщения в LLM', exc_info=ex)
            return ''
        
        start = next_message['content']
        
        #  Добавление начала истории в общий контекст
        self.current_story += utils.dedent(
            f"""

            ## The story begins

            {start}

            """
            )
        
        return start
    
    def continue_story(self, requirements: str = 'Continue the story in an interesting way.', number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        """
        Предлагает продолжение истории.

        Args:
            requirements (str, optional): Требования к продолжению истории. Defaults to "Continue the story in an interesting way.".
            number_of_words (int, optional): Количество слов в продолжении истории. Defaults to 100.
            include_plot_twist (bool, optional): Включать ли сюжетный поворот. Defaults to False.

        Returns:
            str: Продолжение истории.
        """
        # Конфигурация для генерации продолжения истории
        rendering_configs = {
                             'purpose': self.purpose,
                             'requirements': requirements,
                             'current_simulation_trace': self._current_story(),
                             'number_of_words': number_of_words,
                             'include_plot_twist': include_plot_twist
                            }
        
        #  Формирование сообщений для LLM с использованием шаблонов
        messages = utils.compose_initial_LLM_messages_with_templates('story.continuation.system.mustache', 'story.continuation.user.mustache', rendering_configs)
        #  Отправка запроса в LLM
        try:
            next_message = openai_utils.client().send_message(messages, temperature=1.5)
        except Exception as ex:
            logger.error('Ошибка при отправке сообщения в LLM', exc_info=ex)
            return ''
        
        continuation = next_message['content']
        
        # Добавление продолжения истории в общий контекст
        self.current_story += utils.dedent(
            f"""

            ## The story continues

            {continuation}

            """
            )
        
        return continuation

    def _current_story(self) -> str:
        """
        Возвращает текущую историю.

        Returns:
            str: Текущая история.
        """
        interaction_history = ''
        
        #  Формирование истории взаимодействий в зависимости от наличия агента или окружения
        if self.agent is not None:
            interaction_history += self.agent.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        elif self.environment is not None:
            interaction_history += self.environment.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        
        #  Добавление информации о новых взаимодействиях в историю
        self.current_story += utils.dedent(
            f"""

            ## New simulation interactions to consider

            {interaction_history}

            """
            )
            
        return self.current_story