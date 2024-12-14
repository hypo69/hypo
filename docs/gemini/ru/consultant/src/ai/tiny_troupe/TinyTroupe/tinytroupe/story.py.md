# Анализ кода модуля `story.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются docstring для описания классов и методов.
    - Применяются `typing` для аннотации типов.
    - Есть проверка на входные параметры (`environment` и `agent`).
    - Присутствует использование `utils.dedent` для форматирования строк.
    - Код соответствует PEP 8.
-  Минусы
    - Отсутствует обработка исключений с помощью `logger.error`.
    - Не все комментарии соответствуют reStructuredText (RST).
    - Нет импорта `logger`.
    - Не используется `j_loads` или `j_loads_ns`.
    - Использование `openai_utils.client()` без явного импорта и обработки ошибок.

**Рекомендации по улучшению**
1.  Добавить импорт `from src.logger.logger import logger`.
2.  Использовать `logger.error` для обработки исключений.
3.  Переписать docstring в формате RST.
4.  Заменить `openai_utils.client()` на вариант с обработкой ошибок.
5.  Добавить более подробные комментарии для некоторых блоков кода.

**Оптимизированный код**

```python
"""
Модуль для генерации историй на основе симуляций.
=====================================================

Этот модуль предоставляет класс :class:`TinyStory`, который используется для создания и продолжения историй,
основанных на взаимодействиях агентов и окружений в симуляции.

Пример использования
--------------------

Пример создания и использования класса `TinyStory`:

.. code-block:: python

    environment = TinyWorld()
    story = TinyStory(environment=environment, purpose="Исследовать мир")
    story.start_story(requirements="Начать захватывающую историю")
    story.continue_story(requirements="Продолжить историю")
"""

from typing import List, Optional
# импортируем logger
from src.logger.logger import logger
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils

class TinyStory:
    """
    Класс для управления генерацией историй на основе симуляций.

    :param environment: Окружение, в котором происходит история.
    :type environment: TinyWorld, optional
    :param agent: Агент, являющийся главным героем истории.
    :type agent: TinyPerson, optional
    :param purpose: Цель создания истории.
    :type purpose: str, optional
    :param context: Начальный контекст истории.
    :type context: str, optional
    :param first_n: Количество первых взаимодействий для включения в историю.
    :type first_n: int, optional
    :param last_n: Количество последних взаимодействий для включения в историю.
    :type last_n: int, optional
    :param include_omission_info: Флаг, указывающий, включать ли информацию об опущенных взаимодействиях.
    :type include_omission_info: bool, optional
    """
    def __init__(self, environment: Optional[TinyWorld] = None, agent: Optional[TinyPerson] = None, purpose: str = "Be a realistic simulation.", context: str = "",
                 first_n: int = 10, last_n: int = 20, include_omission_info: bool = True) -> None:
        """
        Инициализирует объект TinyStory.

        Исключение:
            Exception: Вызывается, если предоставлено и `environment`, и `agent`, или ни один из них.
        """
        # Проверка, что предоставлен либо environment, либо agent, но не оба сразу
        if environment and agent:
            raise Exception("Either \'environment\' or \'agent\' should be provided, not both")
        if not (environment or agent):
            raise Exception("At least one of the parameters should be provided")
        
        self.environment = environment
        self.agent = agent

        self.purpose = purpose
        # Сохраняет текущий контекст истории
        self.current_story = context

        self.first_n = first_n
        self.last_n = last_n
        self.include_omission_info = include_omission_info
    
    def start_story(self, requirements: str = "Start some interesting story about the agents.", number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        """
        Начинает новую историю.

        :param requirements: Требования к началу истории.
        :type requirements: str, optional
        :param number_of_words: Количество слов в начале истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Флаг, указывающий, включать ли неожиданный поворот сюжета.
        :type include_plot_twist: bool, optional
        :return: Начало истории.
        :rtype: str
        """
        # конфигурация для запроса к языковой модели
        rendering_configs = {
                             "purpose": self.purpose,
                             "requirements": requirements,
                             "current_simulation_trace": self._current_story(),
                             "number_of_words": number_of_words,
                             "include_plot_twist": include_plot_twist
                            }

        # Составление сообщений для языковой модели
        messages = utils.compose_initial_LLM_messages_with_templates("story.start.system.mustache", "story.start.user.mustache", rendering_configs)
        try:
            # Отправка сообщения в языковую модель и получение ответа
            next_message = openai_utils.client().send_message(messages, temperature=1.5)
            start = next_message["content"]
        except Exception as e:
            logger.error(f"Ошибка при получении начала истории: {e}")
            return ""
            

        # Добавление начала истории к текущему контексту
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
        :param number_of_words: Количество слов в продолжении истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Флаг, указывающий, включать ли неожиданный поворот сюжета.
        :type include_plot_twist: bool, optional
        :return: Продолжение истории.
        :rtype: str
        """
        # конфигурация для запроса к языковой модели
        rendering_configs = {
                             "purpose": self.purpose,
                             "requirements": requirements,
                             "current_simulation_trace": self._current_story(),
                             "number_of_words": number_of_words,
                             "include_plot_twist": include_plot_twist
                            }
        
        # Составление сообщений для языковой модели
        messages = utils.compose_initial_LLM_messages_with_templates("story.continuation.system.mustache", "story.continuation.user.mustache", rendering_configs)
        try:
            # Отправка сообщения в языковую модель и получение ответа
            next_message = openai_utils.client().send_message(messages, temperature=1.5)
            continuation = next_message["content"]
        except Exception as e:
            logger.error(f"Ошибка при получении продолжения истории: {e}")
            return ""
        
        # Добавление продолжения истории к текущему контексту
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

        :return: Текущая история.
        :rtype: str
        """
        interaction_history = ""
        # Получение истории взаимодействий агента или окружения
        if self.agent is not None:
            interaction_history += self.agent.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        elif self.environment is not None:
            interaction_history += self.environment.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        # Добавляет историю взаимодействий к текущему контексту истории
        self.current_story += utils.dedent(
            f"""

            ## New simulation interactions to consider

            {interaction_history}

            """
            )
        
        return self.current_story
```