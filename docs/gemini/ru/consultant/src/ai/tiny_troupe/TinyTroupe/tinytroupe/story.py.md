## Анализ кода модуля `story`

**Качество кода**
9
 -  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются docstrings для описания классов и методов.
    - Присутствует проверка на корректность входных параметров в конструкторе класса `TinyStory`.
    - Имеется возможность включения/выключения информации об опущенных взаимодействиях.
    - Применяется форматирование строк f-строками для улучшения читаемости.
    - Используется `utils.dedent` для удаления лишних отступов.
    - В целом, код соответствует стандартам PEP 8 и является читаемым.
 -  Минусы
    - Отсутствует импорт `logger` из `src.logger`.
    - Не используются `j_loads` или `j_loads_ns` для загрузки данных (хотя в данном коде нет загрузки файлов).
    - В docstring не хватает описания типов возвращаемых значений функций.
    - Некоторые комментарии можно было бы сделать более конкретными, а так же добавить документацию в формате RST

**Рекомендации по улучшению**

1.  Добавить импорт `logger` из `src.logger.logger`.
2.  Добавить `-> str` в аннотацию типов для функций `start_story`, `continue_story`, `_current_story`.
3.  В docstring для функций `start_story` и `continue_story` указать тип возвращаемого значения `str`.
4.  Добавить более подробные комментарии для некоторых блоков кода с использованием rst.
5.  Обеспечить соответствие с ранее обработанными файлами в части именования.
6.  В функции `_current_story` убрать лишнее добавление `self.current_story`. Добавить проверку на то, является ли `self.current_story` пустой строкой.

**Оптимизиробанный код**

```python
"""
Every simulation tells a story. This module provides helper mechanisms to help with crafting appropriate stories in TinyTroupe.
============================================================================================================================
Этот модуль содержит класс :class:`TinyStory`, который используется для создания и управления историями в симуляциях TinyTroupe.

Пример использования
--------------------

Пример создания и запуска истории:

.. code-block:: python

    from tinytroupe.environment import TinyWorld
    from tinytroupe.story import TinyStory

    world = TinyWorld()
    story = TinyStory(environment=world, purpose='To explore the world')
    start_story = story.start_story(requirements='Начните интересную историю о мире.')
    print(start_story)
"""

from typing import List
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils
from src.logger.logger import logger  # Импорт logger


class TinyStory:
    """
    Класс для управления историями в TinyTroupe.
    
    Этот класс позволяет создавать, продолжать и управлять историями на основе взаимодействий агентов или окружения.
    """

    def __init__(self, environment: TinyWorld = None, agent: TinyPerson = None, purpose: str = "Be a realistic simulation.", context: str = "",
                 first_n: int = 10, last_n: int = 20, include_omission_info: bool = True) -> None:
        """
        Инициализирует историю. История может быть связана с окружением или агентом. Также имеет цель, которая
        используется для управления генерацией истории. Истории учитывают, что они связаны с симуляциями, поэтому можно
        указывать цели, связанные с симуляцией.

        :param environment: Окружение, в котором происходит история.
        :type environment: TinyWorld, optional
        :param agent: Агент в истории.
        :type agent: TinyPerson, optional
        :param purpose: Цель истории.
        :type purpose: str, optional
        :param context: Текущий контекст истории. Фактическая история будет добавлена к этому контексту.
        :type context: str, optional
        :param first_n: Количество первых взаимодействий, которые нужно включить в историю.
        :type first_n: int, optional
        :param last_n: Количество последних взаимодействий, которые нужно включить в историю.
        :type last_n: int, optional
        :param include_omission_info:  Включать ли информацию об опущенных взаимодействиях.
        :type include_omission_info: bool, optional
        :raises Exception: Если не передан ни агент, ни окружение, или переданы оба параметра.
        """
        # проверка, что передан ровно один из параметров: environment или agent
        if environment and agent:
            raise Exception("Either \'environment\' or \'agent\' should be provided, not both")
        if not (environment or agent):
            raise Exception("At least one of the parameters should be provided")

        self.environment = environment
        self.agent = agent

        self.purpose = purpose

        self.current_story = context

        self.first_n = first_n
        self.last_n = last_n
        self.include_omission_info = include_omission_info

    def start_story(self, requirements: str = "Start some interesting story about the agents.", number_of_words: int = 100,
                    include_plot_twist: bool = False) -> str:
        """
        Начинает новую историю.

        :param requirements: Требования к началу истории.
        :type requirements: str, optional
        :param number_of_words:  Количество слов в начале истории.
        :type number_of_words: int, optional
        :param include_plot_twist:  Включать ли поворот сюжета.
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
        #  Формирование сообщений для LLM с использованием шаблонов
        messages = utils.compose_initial_LLM_messages_with_templates("story.start.system.mustache",
                                                                     "story.start.user.mustache", rendering_configs)
        #  Отправка сообщения в LLM и получение ответа
        try:
            next_message = openai_utils.client().send_message(messages, temperature=1.5)
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения в LLM: {e}")
            return ""

        start = next_message["content"]

        self.current_story += utils.dedent(
            f"""

            ## The story begins

            {start}

            """
        )

        return start

    def continue_story(self, requirements: str = "Continue the story in an interesting way.", number_of_words: int = 100,
                       include_plot_twist: bool = False) -> str:
        """
        Предлагает продолжение истории.

        :param requirements: Требования к продолжению истории.
        :type requirements: str, optional
        :param number_of_words: Количество слов в продолжении истории.
        :type number_of_words: int, optional
        :param include_plot_twist: Включать ли поворот сюжета.
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
        #  Формирование сообщений для LLM с использованием шаблонов
        messages = utils.compose_initial_LLM_messages_with_templates("story.continuation.system.mustache",
                                                                     "story.continuation.user.mustache",
                                                                     rendering_configs)
        #  Отправка сообщения в LLM и получение ответа
        try:
            next_message = openai_utils.client().send_message(messages, temperature=1.5)
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения в LLM: {e}")
            return ""

        continuation = next_message["content"]

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
        #  Проверка, что агент не None
        if self.agent is not None:
            interaction_history += self.agent.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n,
                                                                          include_omission_info=self.include_omission_info)
        #  Проверка, что environment не None
        elif self.environment is not None:
            interaction_history += self.environment.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n,
                                                                              include_omission_info=self.include_omission_info)
        #  Проверка, что current_story не пустая строка
        if self.current_story:
            self.current_story += utils.dedent(
                f"""
    
                ## New simulation interactions to consider
    
                {interaction_history}
    
                """
            )
        else:
            self.current_story += utils.dedent(
            f"""
    
            ## New simulation interactions to consider
    
            {interaction_history}
    
            """
            )

        return self.current_story