# Анализ кода модуля `validation.py`

**Качество кода**
8
-   **Плюсы**
    - Код использует `chevron` для работы с шаблонами.
    - Применяется `textwrap.dedent` для форматирования текста.
    - Код имеет базовую структуру для валидации `TinyPerson` с использованием LLM.
    - Используется логирование для отслеживания процесса валидации.
-   **Минусы**
    -  Отсутствуют docstring для модуля и класса.
    -  Используется стандартный `json.loads` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Не все комментарии соответствуют формату RST.
    -  Не используется `logger.error` для обработки ошибок, только `logger.info`.
    -  `default_max_content_display_length` не описана в docstring.
    -  В цикле while многократно обращаемся к `openai_utils.client().send_message(current_messages)`

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, класса и метода `validate_person`.
2.  Заменить `json.loads` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  Переписать все комментарии в формате RST.
4.  Использовать `logger.error` для обработки исключений.
5.  Добавить описание `default_max_content_display_length` в docstring.
6.  Уменьшить количество обращений к LLM в цикле.
7.  Использовать `from src.logger.logger import logger` для логирования.
8.  Добавить проверки на ошибки при работе с `json_content`.
9.  Более подробные логи, включая возможные причины неудач.
10. Использовать константу для `"TALK"` и `"system"`, `"user"`
11. Добавить проверку наличия `json_content` перед обращением к нему.

**Оптимизированный код**

```python
"""
Модуль для валидации TinyPerson с использованием LLM.
=====================================================

Этот модуль содержит класс :class:`TinyPersonValidator`, который используется для проверки
экземпляров класса :class:`tinytroupe.agent.TinyPerson` с помощью языковой модели OpenAI.

Пример использования
--------------------

.. code-block:: python

    person = TinyPerson(name='test_person', persona='test persona', initial_context='test context')
    score, justification = TinyPersonValidator.validate_person(person)
    if score:
        print(f"Validation score: {score:.2f}; Justification: {justification}")
    else:
        print("Validation failed.")
"""
import os
#   импортируем json из src.utils.jjson
from src.utils.jjson import j_loads
import chevron
#   импортируем logger
from src.logger.logger import logger
import textwrap
from typing import Any, Tuple, Optional


from tinytroupe import openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe import config
import tinytroupe.utils as utils

#   константа для максимальной длины контента
default_max_content_display_length = config["OpenAI"].getint("MAX_CONTENT_DISPLAY_LENGTH", 1024)
# константы для ролей
SYSTEM_ROLE = "system"
USER_ROLE = "user"
TALK_ACTION = "TALK"


class TinyPersonValidator:
    """
    Класс для валидации экземпляров :class:`tinytroupe.agent.TinyPerson`.

    Этот класс предоставляет метод для проверки экземпляров :class:`TinyPerson` с использованием LLM.
    """

    @staticmethod
    def validate_person(person: TinyPerson, expectations: Optional[str] = None, include_agent_spec: bool = True, max_content_length: int = default_max_content_display_length) -> Tuple[Optional[float], Optional[str]]:
        """
        Проверяет экземпляр :class:`TinyPerson` с помощью LLM.

        Этот метод отправляет серию вопросов экземпляру :class:`TinyPerson` для проверки его ответов с помощью LLM.
        Метод возвращает значение типа float, представляющее оценку достоверности процесса валидации.
        Если процесс валидации завершается неудачей, метод возвращает None.

        :param person: Экземпляр :class:`TinyPerson`, который необходимо проверить.
        :type person: TinyPerson
        :param expectations: Ожидания, которые будут использоваться в процессе валидации. По умолчанию None.
        :type expectations: Optional[str]
        :param include_agent_spec: Флаг, определяющий, нужно ли включать спецификацию агента в запрос. По умолчанию True.
        :type include_agent_spec: bool
        :param max_content_length: Максимальная длина содержимого для отображения при рендеринге разговора. По умолчанию `default_max_content_display_length`.
        :type max_content_length: int
        :raises Exception: Если возникает ошибка в процессе валидации.
        :return: Оценка достоверности процесса валидации (от 0.0 до 1.0), или None, если процесс валидации завершается неудачей.
        :rtype: Optional[float]
        :return: Обоснование оценки валидации, или None, если процесс валидации завершается неудачей.
        :rtype: Optional[str]
        """
        #   Инициализация списка сообщений
        current_messages = []
        #   формирование пути к шаблону запроса
        check_person_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/check_person.mustache')
        try:
            #   открытие и чтение шаблона
            with open(check_person_prompt_template_path, 'r') as f:
                check_agent_prompt_template = f.read()
        except Exception as e:
            logger.error(f"Ошибка при чтении шаблона: {check_person_prompt_template_path}", exc_info=True)
            return None, None
        #   рендеринг шаблона с заданными ожиданиями
        system_prompt = chevron.render(check_agent_prompt_template, {"expectations": expectations})

        #   формирование пользовательского запроса
        user_prompt = textwrap.dedent(
            """
        Now, based on the following characteristics of the person being interviewed, and following the rules given previously, 
        create your questions and interview the person. Good luck!

        """
        )
        #   добавление спецификации агента или мини-биографии в зависимости от флага `include_agent_spec`
        if include_agent_spec:
            user_prompt += f"\n\n{person.generate_agent_specification()}"
        else:
            user_prompt += f"\n\nMini-biography of the person being interviewed: {person.minibio()}"


        logger.info(f"Starting validation of the person: {person.name}")

        #   добавление системного и пользовательского запросов в список сообщений
        current_messages.append({"role": SYSTEM_ROLE, "content": system_prompt})
        current_messages.append({"role": USER_ROLE, "content": user_prompt})

        #   отправка начальных сообщений в LLM
        message = openai_utils.client().send_message(current_messages)

        #   условие для завершения цикла
        termination_mark = "```json"

        while message is not None and not (termination_mark in message["content"]):
            #   получение вопросов из ответа LLM
            questions = message["content"]
            #   добавление вопросов в список сообщений
            current_messages.append({"role": message["role"], "content": questions})
            logger.info(f"Question validation:\n{questions}")

            #   запрос ответа у TinyPerson
            person.listen_and_act(questions, max_content_length=max_content_length)
            #   получение ответов TinyPerson
            responses = person.pop_actions_and_get_contents_for(TALK_ACTION, False)
            logger.info(f"Person reply:\n{responses}")

            #   добавление ответов в текущий разговор и получение следующего сообщения
            current_messages.append({"role": USER_ROLE, "content": responses})
            message = openai_utils.client().send_message(current_messages)

        #   проверка наличия сообщения от LLM
        if message is not None:
            try:
                #   извлечение JSON из сообщения
                json_content = utils.extract_json(message['content'])
                #   проверка наличия json_content
                if not json_content:
                  logger.error(f"Ошибка: Не удалось извлечь JSON из сообщения: {message['content']}")
                  return None, None
                #   извлечение оценки и обоснования
                score = float(json_content.get("score"))
                justification = json_content.get("justification")
                logger.info(f"Validation score: {score:.2f}; Justification: {justification}")
                return score, justification
            except (ValueError, KeyError) as e:
                logger.error(f"Ошибка при обработке JSON: {e}", exc_info=True)
                return None, None
        else:
            logger.error("Ошибка: Нет ответа от LLM.")
            return None, None