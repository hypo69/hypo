# Анализ кода модуля `validation.py`

**Качество кода: 7/10**
   - **Плюсы:**
        - Код выполняет валидацию `TinyPerson` с помощью OpenAI LLM, что является полезной функциональностью.
        - Используется `chevron` для шаблонизации промптов, что улучшает читаемость и поддержку.
        - Присутствует логгирование процесса валидации, что полезно для отладки и мониторинга.
        - Код структурирован в класс `TinyPersonValidator`, что способствует модульности.
        - Используется `textwrap.dedent` для форматирования многострочных промптов.
   - **Минусы:**
        - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        - Отсутствуют docstring для класса и метода.
        - `logger` импортируется из `logging` вместо `from src.logger import logger`.
        - Присутствует избыточное использование `try-except` блоков.
        - В коде присутствуют магические строки "```json" для определения окончания разговора.
        - Не везде используются одинарные кавычки.

**Рекомендации по улучшению:**

1.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Добавить docstring для класса `TinyPersonValidator` и метода `validate_person`, следуя стандартам RST.
3.  Импортировать `logger` из `src.logger.logger import logger`.
4.  Упростить обработку ошибок, используя `logger.error` вместо стандартных блоков `try-except`.
5.  Вынести магическую строку `termination_mark` в константу.
6.  Привести все кавычки в коде к одинарным, где это необходимо.
7.  Добавить проверку наличия ключей в `json_content` для избежания `KeyError`.
8.  Добавить обработку ситуации, когда `json_content` не является корректным JSON.

**Оптимизированный код:**
```python
"""
Модуль для валидации экземпляров TinyPerson с использованием OpenAI LLM.
======================================================================

Этот модуль предоставляет класс :class:`TinyPersonValidator`, который используется для валидации
экземпляров :class:`tinytroupe.agent.TinyPerson` с помощью моделей OpenAI.

Пример использования
--------------------

Пример валидации экземпляра `TinyPerson`:

.. code-block:: python

    person = TinyPerson(name='TestPerson', role='tester')
    score, justification = TinyPersonValidator.validate_person(person, expectations='быть внимательным')
    if score is not None:
        print(f"Score: {score}, Justification: {justification}")
    else:
        print("Validation failed")
"""
import os
import chevron
from textwrap import dedent
from src.logger.logger import logger
from tinytroupe import openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe import config
from tinytroupe import utils
from src.utils.jjson import j_loads  # Corrected import

_default_max_content_display_length = config['OpenAI'].getint('MAX_CONTENT_DISPLAY_LENGTH', 1024)
_termination_mark = '```json'

class TinyPersonValidator:
    """
    Класс для валидации экземпляров TinyPerson.

    Этот класс содержит статический метод :meth:`validate_person` для оценки соответствия
    экземпляра :class:`TinyPerson` заданным критериям с использованием OpenAI LLM.
    """
    @staticmethod
    def validate_person(person: TinyPerson, expectations: str = None, include_agent_spec: bool = True, max_content_length: int = _default_max_content_display_length) -> tuple[float, str] | tuple[None, None]:
        """
        Валидирует экземпляр TinyPerson, используя OpenAI LLM.

        Метод отправляет серию вопросов экземпляру `TinyPerson` для проверки его ответов
        с помощью OpenAI LLM. Возвращает оценку уверенности в валидации (от 0.0 до 1.0)
        и обоснование, или None, если валидация не удалась.

        Args:
            person (TinyPerson): Экземпляр `TinyPerson` для валидации.
            expectations (str, optional): Ожидания, используемые в процессе валидации. По умолчанию None.
            include_agent_spec (bool, optional): Флаг, указывающий, включать ли спецификацию агента в промпт. По умолчанию True.
            max_content_length (int, optional): Максимальная длина контента для отображения при рендеринге разговора.

        Returns:
            tuple[float, str] | tuple[None, None]: Кортеж, содержащий оценку уверенности валидации (от 0.0 до 1.0) и обоснование, или (None, None) при неудаче.

        Example:
           >>> person = TinyPerson(name='TestPerson', role='tester')
           >>> score, justification = TinyPersonValidator.validate_person(person, expectations='быть внимательным')
           >>> if score is not None:
           ...    print(f"Score: {score}, Justification: {justification}")
           ... else:
           ...    print("Validation failed")
        """
        # Инициализация текущих сообщений
        current_messages = []

        # Формирование пути к шаблону промпта
        check_person_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/check_person.mustache')
        try:
            with open(check_person_prompt_template_path, 'r') as f:
                check_agent_prompt_template = f.read()
        except Exception as e:
            logger.error(f'Ошибка при чтении шаблона промпта: {check_person_prompt_template_path}', exc_info=True)
            return None, None

        # Рендеринг системного промпта
        system_prompt = chevron.render(check_agent_prompt_template, {'expectations': expectations})

        # Формирование пользовательского промпта
        user_prompt = dedent(
            f"""
            Now, based on the following characteristics of the person being interviewed, and following the rules given previously, 
            create your questions and interview the person. Good luck!

            """
        )

        if include_agent_spec:
            user_prompt += f'\n\n{person.generate_agent_specification()}'
        else:
            user_prompt += f'\n\nMini-biography of the person being interviewed: {person.minibio()}'


        logger.info(f'Начало валидации персонажа: {person.name}')

        # Отправка начальных сообщений в LLM
        current_messages.append({'role': 'system', 'content': system_prompt})
        current_messages.append({'role': 'user', 'content': user_prompt})

        message = openai_utils.client().send_message(current_messages)

        # Цикл обработки сообщений до тех пор, пока не встретится маркер окончания разговора
        while message is not None and not (_termination_mark in message['content']):
            # Добавление вопросов к текущим сообщениям
            questions = message['content']
            current_messages.append({'role': message['role'], 'content': questions})
            logger.info(f'Вопрос валидации:\\n{questions}')

            # Отправка вопросов персонажу
            person.listen_and_act(questions, max_content_length=max_content_length)
            responses = person.pop_actions_and_get_contents_for('TALK', False)
            logger.info(f'Ответ персонажа:\\n{responses}')

            # Добавление ответов в текущую беседу и запрос следующего сообщения
            current_messages.append({'role': 'user', 'content': responses})
            message = openai_utils.client().send_message(current_messages)

        # Обработка финального сообщения, содержащего JSON
        if message is not None:
            try:
                json_content = j_loads(message['content'])
                if not isinstance(json_content, dict):
                    logger.error(f'Некорректный JSON формат: {json_content}')
                    return None, None
                # Чтение оценки и обоснования
                score = float(json_content.get('score'))
                justification = json_content.get('justification')
                logger.info(f'Оценка валидации: {score:.2f}; Обоснование: {justification}')
                return score, justification
            except (json.JSONDecodeError, KeyError, TypeError) as e:
                  logger.error(f'Ошибка обработки JSON содержимого: {e}', exc_info=True)
                  return None, None
        else:
            return None, None
```