## Анализ кода модуля `validation.py`

**Качество кода:** 8/10
- **Плюсы:**
    - Код структурирован и логически понятен.
    - Используется `chevron` для шаблонизации.
    - Присутствует логирование.
    - Присутствует документация.
- **Минусы:**
    - Не все импорты упорядочены и соответствуют стандарту проекта.
    - Используется `json.loads` вместо `j_loads` или `j_loads_ns`.
    - Необходимо добавить более подробную документацию в формате RST для каждой функции.
    - Использование `logging.getLogger` вместо импорта `logger` из `src.logger.logger`

**Рекомендации по улучшению:**

1.  **Импорты:**
    -   Импортировать `logger` из `src.logger.logger`.
    -   Удалить неиспользуемые импорты, такие как `logging`.
    -   Использовать `from src.utils.jjson import j_loads`

2.  **Обработка JSON:**
    -   Использовать `j_loads` из `src.utils.jjson` вместо `json.loads`.

3.  **Логирование:**
    -   Использовать `logger.info` для информационных сообщений.
    -   Использовать `logger.error` для сообщений об ошибках.

4.  **Документация:**
    -   Добавить документацию в формате RST для класса и метода.
    -   Указать Args и Returns с типами данных для метода `validate_person`.

5.  **Форматирование кода:**
    -   Использовать одинарные кавычки в коде.
    -   Убрать лишние комментарии и добавить более информативные.
    -   Разделить код на логические блоки для повышения читаемости.

6.  **Обработка ошибок:**
    - Избегать избыточных try-except, использовать logger.error

**Оптимизированный код:**

```python
"""
Модуль для валидации TinyPerson с использованием OpenAI LLM.
==========================================================

Этот модуль содержит класс :class:`TinyPersonValidator`, который используется для проверки
качества ответов TinyPerson с помощью OpenAI LLM.

Пример использования
--------------------

Пример использования класса `TinyPersonValidator`:

.. code-block:: python

    validator = TinyPersonValidator()
    person = TinyPerson(name='John Doe', role='developer')
    score, justification = validator.validate_person(person)
    if score:
        print(f'Validation Score: {score}, Justification: {justification}')
    else:
        print('Validation failed')
"""
import os
import chevron
from src.utils.jjson import j_loads
from src.logger.logger import logger # Импорт logger из src.logger.logger

from tinytroupe import openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe import config
import tinytroupe.utils as utils
from pathlib import Path

default_max_content_display_length = config['OpenAI'].getint('MAX_CONTENT_DISPLAY_LENGTH', 1024)


class TinyPersonValidator:
    """
    Класс для валидации TinyPerson с использованием OpenAI LLM.
    """
    @staticmethod
    def validate_person(person: TinyPerson, expectations: str = None, include_agent_spec: bool = True, max_content_length: int = default_max_content_display_length) -> tuple[float, str] | tuple[None, None]:
        """
        Проверяет экземпляр TinyPerson, используя OpenAI LLM.

        Этот метод отправляет серию вопросов экземпляру TinyPerson для проверки его ответов с использованием OpenAI LLM.
        Метод возвращает значение float, представляющее оценку достоверности процесса проверки.
        Если процесс проверки не удался, метод возвращает None.

        Args:
            person (TinyPerson): Экземпляр TinyPerson для проверки.
            expectations (str, optional): Ожидания, используемые в процессе проверки. Defaults to None.
            include_agent_spec (bool, optional): Определяет, включать ли спецификацию агента в запрос. Defaults to True.
            max_content_length (int, optional): Максимальная длина содержимого для отображения при рендеринге разговора.

        Returns:
            tuple[float, str] | tuple[None, None]: Оценка достоверности (от 0.0 до 1.0) и обоснование или (None, None) в случае неудачи.
        
        Example:
            >>> person = TinyPerson(name='Test Person', role='tester')
            >>> validator = TinyPersonValidator()
            >>> score, justification = validator.validate_person(person)
            >>> if score:
            ...     print(f"Validation score: {score:.2f}, Justification: {justification}")
            ... else:
            ...     print("Validation failed")
        """
        # Инициализация списка сообщений
        current_messages = []

        # Формирование пути к шаблону промпта
        check_person_prompt_template_path = Path(os.path.dirname(__file__)) / 'prompts/check_person.mustache'
        
        # Чтение шаблона промпта
        with open(check_person_prompt_template_path, 'r') as f:
            check_agent_prompt_template = f.read()
        
        # Рендеринг системного промпта
        system_prompt = chevron.render(check_agent_prompt_template, {'expectations': expectations})

        # Формирование пользовательского промпта
        import textwrap
        user_prompt = textwrap.dedent(
            '''
            Now, based on the following characteristics of the person being interviewed, and following the rules given previously, 
            create your questions and interview the person. Good luck!
            '''
        )

        if include_agent_spec:
            user_prompt += f'\n\n{person.generate_agent_specification()}'
        else:
            user_prompt += f'\n\nMini-biography of the person being interviewed: {person.minibio()}'

        logger.info(f'Starting validation of the person: {person.name}')

        # Добавление системного и пользовательского промптов в список сообщений
        current_messages.append({'role': 'system', 'content': system_prompt})
        current_messages.append({'role': 'user', 'content': user_prompt})

        # Отправка начальных сообщений в LLM
        message = openai_utils.client().send_message(current_messages)

        # Определение маркера завершения разговора
        termination_mark = '```json'

        # Цикл для общения с LLM, пока не получен маркер завершения
        while message is not None and not (termination_mark in message['content']):
            # Добавление вопроса в текущие сообщения
            questions = message['content']
            current_messages.append({'role': message['role'], 'content': questions})
            logger.info(f'Question validation:\n{questions}')

            # Запрос ответов от персонажа
            person.listen_and_act(questions, max_content_length=max_content_length)
            responses = person.pop_actions_and_get_contents_for('TALK', False)
            logger.info(f'Person reply:\n{responses}')

            # Добавление ответа в текущий разговор
            current_messages.append({'role': 'user', 'content': responses})
            message = openai_utils.client().send_message(current_messages)

        # Проверка наличия сообщения
        if message is not None:
            # Извлечение JSON контента
            json_content = utils.extract_json(message['content'])
            # Чтение score и justification
            score = float(json_content['score'])
            justification = json_content['justification']
            logger.info(f'Validation score: {score:.2f}; Justification: {justification}')
            return score, justification
        else:
            return None, None