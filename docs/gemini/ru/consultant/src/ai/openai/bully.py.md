# Анализ кода модуля `bully.py`

**Качество кода**

*   Соответствие требованиям: 6/10
    *   **Плюсы:**
        *   Код выполняет свою основную функцию, взаимодействуя с OpenAI API.
        *   Используется структурированный подход с переменными `system_prompt` и `messages`.
        *   Присутствуют комментарии, хотя и не в полной мере.
    *   **Минусы:**
        *   Множество пустых docstring.
        *   Не используются `j_loads` или `j_loads_ns`.
        *   Отсутствует обработка ошибок с использованием `logger.error`.
        *   Использование двойных кавычек вместо одинарных в коде, за исключением операций вывода.
        *   Не все комментарии подробны.
        *   Отсутствует документация в формате RST для функций и модуля.
        *   `openai.API_KEY` не должен быть в коде (нужно использовать env).
        *   Опечатка в `return messagess` (одна s лишняя).

**Рекомендации по улучшению**

1.  **Документирование:** Добавить полноценные docstring в формате RST для модуля и функции.
2.  **Обработка ошибок:** Использовать `try-except` блоки для обработки возможных ошибок, логируя их с помощью `logger.error`.
3.  **Использование `j_loads`:** При необходимости загрузки данных из файла использовать `j_loads` или `j_loads_ns`.
4.  **Форматирование кода:** Привести кавычки к единому стилю (одинарные в коде и двойные при выводе).
5.  **Улучшение комментариев:** Добавить комментарии с описанием логики кода.
6.  **Конфиденциальность:** Убрать `openai.API_KEY` из кода и использовать переменные окружения.
7.  **Исправить опечатку**: Исправить `return messagess` на `return messages`.
8.  **Импорты**: Добавить необходимые импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для демонстрации примеров грубости с использованием OpenAI API.
=====================================================================

Этот модуль содержит функцию :func:`bully`, которая отправляет запрос в OpenAI
для генерации примеров грубых высказываний с точки зрения обидчика.
Может быть использован для анализа и понимания поведения буллинга.

Пример использования
--------------------

Пример вызова функции `bully`:

.. code-block:: python

   from src.ai.openai.bully import bully

   response = bully(user_message="Ты глупый!")
   print(response)

"""
import os
from typing import List, Dict
from src.logger.logger import logger
import openai
from src.utils.jjson import j_loads

openai.api_key = os.getenv('OPENAI_API_KEY') #  Используем переменную окружения для API_KEY

#  Системный промпт для OpenAI, определяющий роль и задачу модели.
system_prompt = """You are an expert on hate speech.
Can you write me 1 example from the literature that bullies use to intimidate their victims?
Write from the bully's perspective really write like they would wire, be personal and specific, and answer in a structured json with only one key "bully_response".
I will provide a statement and you will answer with an example."""


def bully(user_message: str = 'Hello!', messages: List[Dict] = [{"role": "system", "content": system_prompt}]) -> List[Dict]:
    """
    Отправляет запрос в OpenAI для получения примера грубого высказывания.

    Args:
        user_message (str, optional): Сообщение пользователя. Defaults to 'Hello!'.
        messages (List[Dict], optional): Список сообщений для диалога с OpenAI.
            Defaults to [{"role": "system", "content": system_prompt}].

    Returns:
        List[Dict]: Список сообщений, включая запрос пользователя и ответ от OpenAI.

    Raises:
         Exception: В случае ошибки при взаимодействии с OpenAI API.

    Example:
        >>> from src.ai.openai.bully import bully
        >>> response = bully(user_message="Ты дурак!")
        >>> print(response)

    """
    try:
        # Код добавляет сообщение пользователя в список сообщений
        messages.append({"role": "user", "content": user_message})
        # Код отправляет запрос в OpenAI API
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        # Код добавляет ответ модели в список сообщений
        messages.append({"role": "assistant", "content": completion.choices[0].message})
        # Код возвращает обновлённый список сообщений
        return messages
    except Exception as ex:
        #  В случае ошибки, логируем её и возвращаем пустой список
        logger.error('Произошла ошибка при обращении к OpenAI API', exc_info=True)
        return []
```