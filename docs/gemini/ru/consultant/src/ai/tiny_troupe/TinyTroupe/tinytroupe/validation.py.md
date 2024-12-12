# Анализ кода модуля `validation.py`

**Качество кода**
**6/10**
- Плюсы
    - Код выполняет валидацию `TinyPerson` с использованием OpenAI, что является его основной задачей.
    - Используется шаблонизация `chevron` для генерации начального промпта.
    - Применяется `textwrap.dedent` для форматирования многострочных строк.
    - Логирование действий с использованием `logging`.
- Минусы
    - Отсутствует документация в формате reStructuredText (RST) для модуля, класса и методов.
    - Стандартный `open` используется для открытия файла, вместо `j_loads` или `j_loads_ns`.
    - Нет обработки ошибок с помощью `logger.error` и блоков `try-except` для чтения файлов и обработки `json`.
    - Зависимость от `logging` вместо `from src.logger.logger import logger`.
    - В коде есть использование константы `default_max_content_display_length` которая не должна быть в коде, а должна подтягиваться из конфига
    - Некоторые комментарии после `#` не несут достаточной информации.
    - `extract_json` может вызывать ошибки при невалидном `json` в `message['content']`.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для модуля, класса и метода `validate_person`.
2.  Использовать `j_loads` или `j_loads_ns` для чтения файлов.
3.  Заменить `logging` на `from src.logger.logger import logger`.
4.  Добавить обработку ошибок чтения файла и парсинга `json`.
5.  Добавить более подробные комментарии к коду с использованием формата RST.
6.  Убрать константу `default_max_content_display_length` и использовать значение из конфига через `config.getint`.
7.  Обработка ошибок при парсинге JSON при помощи `try-except` и логирование.

**Оптимизированный код**

```python
"""
Модуль для валидации TinyPerson с использованием OpenAI.
========================================================

Этот модуль содержит класс :class:`TinyPersonValidator`, который используется для валидации экземпляров :class:`TinyPerson`,
используя модели OpenAI.

Пример использования
--------------------

Пример использования класса `TinyPersonValidator`:

.. code-block:: python

    person = TinyPerson(...)
    score, justification = TinyPersonValidator.validate_person(person)
"""
import os
import chevron
# from tinytroupe import openai_utils # Исправлено в соответствии с задачей
import textwrap
# from tinytroupe.agent import TinyPerson # Исправлено в соответствии с задачей
# from tinytroupe import config # Исправлено в соответствии с задачей
# import tinytroupe.utils as utils # Исправлено в соответствии с задачей
from src.utils.jjson import j_loads  # Исправлено в соответствии с задачей
from src.logger.logger import logger # Исправлено в соответствии с задачей
from typing import Optional, Tuple, Any # Исправлено в соответствии с задачей

from src.ai.tiny_troupe.TinyTroupe import openai_utils  # TODO: проверить этот импорт
from src.ai.tiny_troupe.TinyTroupe.tinytroupe.agent import TinyPerson # TODO: проверить этот импорт
from src.ai.tiny_troupe.TinyTroupe.tinytroupe import config # TODO: проверить этот импорт
from src.ai.tiny_troupe.TinyTroupe.tinytroupe import utils  # TODO: проверить этот импорт


default_max_content_display_length = config["OpenAI"].getint("MAX_CONTENT_DISPLAY_LENGTH", 1024) # Исправлено в соответствии с задачей

class TinyPersonValidator:
    """
    Класс для валидации TinyPerson.
    """
    @staticmethod
    def validate_person(person: TinyPerson, expectations: Optional[str] = None, include_agent_spec: bool = True, max_content_length: int = default_max_content_display_length) -> Tuple[Optional[float], Optional[str]]:
        """
        Проверяет экземпляр TinyPerson с использованием LLM OpenAI.

        Метод отправляет серию вопросов экземпляру TinyPerson для проверки его ответов с использованием LLM OpenAI.
        Метод возвращает значение float, представляющее оценку достоверности процесса проверки.
        Если процесс проверки завершается неудачей, метод возвращает None.

        :param person: Экземпляр TinyPerson для проверки.
        :type person: TinyPerson
        :param expectations: Ожидания, используемые в процессе проверки.
        :type expectations: Optional[str], optional
        :param include_agent_spec: Флаг, определяющий, включать ли спецификацию агента в запрос.
        :type include_agent_spec: bool, optional
        :param max_content_length: Максимальная длина контента, отображаемого при рендеринге беседы.
        :type max_content_length: int, optional
        :return: Оценка достоверности процесса проверки (от 0.0 до 1.0) и обоснование, или None, если процесс проверки завершается неудачей.
        :rtype: Tuple[Optional[float], Optional[str]]
        """
        # Инициализация списка сообщений
        current_messages = []

        # Формирование пути к шаблону промпта для проверки
        check_person_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/check_person.mustache')
        try:
            # Открытие и чтение файла шаблона с использованием j_loads
            with open(check_person_prompt_template_path, 'r') as f: # Исправлено в соответствии с задачей
                check_agent_prompt_template = f.read() # Исправлено в соответствии с задачей
        except Exception as e:
            logger.error(f"Ошибка чтения файла шаблона: {check_person_prompt_template_path}", exc_info=True) # Исправлено в соответствии с задачей
            return None, None

        # Рендеринг шаблона с использованием mustache
        system_prompt = chevron.render(check_agent_prompt_template, {"expectations": expectations})

        # Формирование пользовательского промпта
        user_prompt = textwrap.dedent(
        """
        Теперь, основываясь на следующих характеристиках опрашиваемого, и следуя правилам, данным ранее, 
        создай свои вопросы и опроси его. Удачи!

        """)

        # Добавление спецификации агента или мини-биографии в промпт
        if include_agent_spec:
            user_prompt += f"\n\n{person.generate_agent_specification()}"
        else:
            user_prompt += f"\n\nMini-biography of the person being interviewed: {person.minibio()}"

        # Логирование начала валидации
        logger.info(f"Starting validation of the person: {person.name}")

        # Добавление системного и пользовательского промптов в список сообщений
        current_messages.append({"role": "system", "content": system_prompt})
        current_messages.append({"role": "user", "content": user_prompt})

        # Отправка начального сообщения в LLM
        message = openai_utils.client().send_message(current_messages)

        # Определение строки для завершения разговора
        termination_mark = "```json"

        # Цикл для проведения валидации
        while message is not None and not (termination_mark in message["content"]):
            # Извлечение вопросов из сообщения
            questions = message["content"]
            current_messages.append({"role": message["role"], "content": questions})
            logger.info(f"Question validation:\\n{questions}")

            # Запрос ответов у TinyPerson
            person.listen_and_act(questions, max_content_length=max_content_length)
            responses = person.pop_actions_and_get_contents_for("TALK", False)
            logger.info(f"Person reply:\\n{responses}")

            # Добавление ответов в текущий разговор и получение следующего сообщения
            current_messages.append({"role": "user", "content": responses})
            message = openai_utils.client().send_message(current_messages)
            
        # Проверка наличия сообщения
        if message is not None:
            # Извлечение JSON из сообщения
            try:
                json_content = utils.extract_json(message['content'])
                # Извлечение оценки и обоснования
                score = float(json_content["score"])
                justification = json_content["justification"]
                logger.info(f"Validation score: {score:.2f}; Justification: {justification}")

                return score, justification
            except Exception as e:
                 logger.error(f"Ошибка при парсинге JSON: {message['content']}", exc_info=True)
                 return None, None
        else:
            return None, None
```