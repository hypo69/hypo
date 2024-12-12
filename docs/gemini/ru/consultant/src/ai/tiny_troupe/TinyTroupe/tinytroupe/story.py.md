# Анализ кода модуля `story.py`

**Качество кода**

-   Соответствие требованиям по оформлению кода: 7/10
    -   Плюсы:
        -   Код разбит на логические блоки.
        -   Используется `utils.dedent` для форматирования строк.
        -   Используются docstring для документирования классов и методов.
    -   Минусы:
        -   Не все docstring соответствуют стандарту reStructuredText (RST).
        -   Отсутствуют импорты из `src.utils.jjson` и `src.logger.logger`.
        -   Используется стандартный `Exception` вместо обработки ошибок через `logger.error`.
        -   Не все комментарии после `#` соответствуют подробному объяснению кода.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить необходимые импорты `from src.utils.jjson import j_loads, j_loads_ns` и `from src.logger.logger import logger`.
2.  **Формат документации**: Переписать docstring в формате RST, чтобы они соответствовали стандартам Sphinx.
3.  **Обработка ошибок**: Использовать `logger.error` для обработки исключений вместо стандартных `try-except`.
4.  **Комментарии**: Дополнить комментарии после `#` для подробного объяснения кода.
5.  **Рефакторинг**: Переименовать `interaction_history` в более понятное имя `interactions_text`.
6.  **Избегание дублирования**: Вынести общую логику построения сообщений в отдельную функцию.

**Оптимизированный код**

```python
"""
Модуль для создания историй на основе симуляций.
=========================================================================================

Этот модуль предоставляет класс :class:`TinyStory`, который используется для создания и продолжения
историй на основе симуляций, с участием агентов и окружения.

Пример использования
--------------------

Пример использования класса `TinyStory`:

.. code-block:: python

    environment = TinyWorld()
    story = TinyStory(environment=environment, purpose='Исследование окружения')
    story.start_story()
    story.continue_story()
"""

from typing import List, Dict, Any
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils
# импортируем необходимые модули
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger


class TinyStory:
    """
    Класс для создания и управления историями на основе симуляций.

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

    def __init__(self, environment: TinyWorld = None, agent: TinyPerson = None, purpose: str = "Be a realistic simulation.", context: str = "",
                 first_n: int = 10, last_n: int = 20, include_omission_info: bool = True) -> None:
        """
        Инициализация объекта истории.

        Исключение:
            Если переданы и `environment` и `agent`, или если не передан ни один из них.
        """
        # Проверяем, что передан либо environment, либо agent, но не оба сразу
        if environment and agent:
            # Логируем ошибку и выбрасываем исключение
            logger.error("Исключение: Либо \'environment\', либо \'agent\' должен быть передан, но не оба")
            raise Exception("Either \'environment\' or \'agent\' should be provided, not both")
        if not (environment or agent):
            # Логируем ошибку и выбрасываем исключение
            logger.error("Исключение: Должен быть передан хотя бы один из параметров: \'environment\' или \'agent\'")
            raise Exception("At least one of the parameters should be provided")
        
        # Сохраняем переданные параметры
        self.environment = environment
        self.agent = agent

        self.purpose = purpose
        self.current_story = context
        self.first_n = first_n
        self.last_n = last_n
        self.include_omission_info = include_omission_info

    def _compose_story_messages(self, template_system: str, template_user: str, requirements: str, number_of_words: int, include_plot_twist: bool) -> List[Dict[str, str]]:
        """
        Составляет сообщения для LLM на основе шаблонов и параметров.

        :param template_system: Имя шаблона для системного сообщения.
        :type template_system: str
        :param template_user: Имя шаблона для пользовательского сообщения.
        :type template_user: str
        :param requirements: Требования к истории.
        :type requirements: str
        :param number_of_words: Количество слов в истории.
        :type number_of_words: int
        :param include_plot_twist: Включать ли поворот сюжета.
        :type include_plot_twist: bool
        :return: Список сообщений для LLM.
        :rtype: List[Dict[str, str]]
        """
        # Подготавливаем конфигурации для шаблонов
        rendering_configs = {
            "purpose": self.purpose,
            "requirements": requirements,
            "current_simulation_trace": self._current_story(),
            "number_of_words": number_of_words,
            "include_plot_twist": include_plot_twist
        }
        # Составляем сообщения с использованием шаблонов
        messages = utils.compose_initial_LLM_messages_with_templates(template_system, template_user, rendering_configs)
        return messages

    def start_story(self, requirements: str = "Start some interesting story about the agents.", number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        """
        Начинает новую историю.

        :param requirements: Требования к началу истории.
        :type requirements: str, optional
        :param number_of_words: Количество слов в истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Включать ли поворот сюжета.
        :type include_plot_twist: bool, optional
        :return: Начало истории.
        :rtype: str
        """
        # Составляем сообщения для LLM для начала истории
        messages = self._compose_story_messages("story.start.system.mustache", "story.start.user.mustache", requirements, number_of_words, include_plot_twist)
        # Отправляем сообщение и получаем ответ от LLM
        next_message = openai_utils.client().send_message(messages, temperature=1.5)
        # Извлекаем текст начала истории
        start = next_message["content"]
        # Добавляем начало истории к текущей истории
        self.current_story += utils.dedent(
            f"""

            ## The story begins

            {start}

            """
        )
        # Возвращаем начало истории
        return start

    def continue_story(self, requirements: str = "Continue the story in an interesting way.", number_of_words: int = 100, include_plot_twist: bool = False) -> str:
        """
        Предлагает продолжение истории.

        :param requirements: Требования к продолжению истории.
        :type requirements: str, optional
        :param number_of_words: Количество слов в истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Включать ли поворот сюжета.
        :type include_plot_twist: bool, optional
        :return: Продолжение истории.
        :rtype: str
        """
        # Составляем сообщения для LLM для продолжения истории
        messages = self._compose_story_messages("story.continuation.system.mustache", "story.continuation.user.mustache", requirements, number_of_words, include_plot_twist)
        # Отправляем сообщение и получаем ответ от LLM
        next_message = openai_utils.client().send_message(messages, temperature=1.5)
        # Извлекаем текст продолжения истории
        continuation = next_message["content"]
        # Добавляем продолжение истории к текущей истории
        self.current_story += utils.dedent(
            f"""

            ## The story continues

            {continuation}

            """
        )
        # Возвращаем продолжение истории
        return continuation

    def _current_story(self) -> str:
        """
        Возвращает текущую историю.

        :return: Текущая история.
        :rtype: str
        """
        # Инициализируем переменную для хранения текста взаимодействий
        interactions_text = ""
        # Если есть агент, получаем текст его взаимодействий
        if self.agent is not None:
            interactions_text += self.agent.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        # Если есть окружение, получаем текст его взаимодействий
        elif self.environment is not None:
            interactions_text += self.environment.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        # Добавляем текст взаимодействий к текущей истории
        self.current_story += utils.dedent(
            f"""

            ## New simulation interactions to consider

            {interactions_text}

            """
        )
        # Возвращаем текущую историю
        return self.current_story
```