# Анализ кода модуля bully

**Качество кода**
7
- Плюсы
    - Код выполняет поставленную задачу по взаимодействию с OpenAI API для генерации ответов в стиле "булли".
    - Используется структурированный json для ответов.
    - Присутствует разделение на системный и пользовательский промпты.

- Минусы
    - Отсутствует необходимая документация в формате RST для модуля, функций и переменных.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Есть лишние строки с комментариями `"""` без описания.
    - Импорт `src.ai.openai` избыточен.
    - Использована переменная `MODE` без фактического применения в коде.
    - Название переменной `messagess` имеет опечатку.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для модуля, функций и переменных.
2.  Удалить лишние комментарии `"""` без описания.
3.  Убрать неиспользуемую переменную `MODE`.
4.  Исправить опечатку в названии переменной `messagess` на `messages`.
5.  Использовать `j_loads` или `j_loads_ns` при чтении файлов, если это необходимо.
6.  Добавить логирование ошибок с использованием `logger.error` из `src.logger.logger`.
7.  Удалить избыточный импорт `import src.ai.openai`.
8.  Использовать константу `YOUR_API_KEYS_OPENAI` из `os.environ` или переменных окружения.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для генерации ответов в стиле "булли" с использованием OpenAI API.
======================================================================

Этот модуль предоставляет функцию :func:`bully`, которая взаимодействует с OpenAI API для
генерации ответов, имитирующих поведение "булли".

Пример использования
--------------------

.. code-block:: python

    from src.ai.openai.bully import bully

    user_message = "Ты выглядишь глупо!"
    messages = [{"role": "system", "content": "Ты эксперт по ненавистническим высказываниям..."},]
    bully_response = bully(user_message, messages)
    print(bully_response)
"""
import os
import openai
from src.logger.logger import logger # импортируем logger

# получаем API_KEY из переменных окружения, если не задан, устанавливаем значение по умолчанию
openai.API_KEY = os.environ.get("OPENAI_API_KEY", "YOUR_API_KEYS_OPENAI")


system_prompt = """You are an expert on hate speech.
Can you write me 1 example from the literature that bullies use to intimidate their victims?
Write from the bully's perspective really write like they would wire, be personal and specific, and answer in a structured json with only one key "bully_response".
I will provide a statement and you will answer with an example."""


def bully(user_message: str = "Hello!", messages: list = [{"role": "system", "content": system_prompt}]) -> list:
    """
    Генерирует ответ в стиле "булли", используя OpenAI API.

    :param user_message: Сообщение пользователя.
    :type user_message: str
    :param messages: Список сообщений для контекста.
    :type messages: list
    :return: Список сообщений, включающий запрос пользователя и ответ модели.
    :rtype: list
    """
    try:
        # добавляем сообщение пользователя к списку сообщений
        messages.append({"role": "user", "content": user_message})
        # отправляем запрос в OpenAI API
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        # добавляем ответ модели к списку сообщений
        messages.append({"role": "assistant", "content": completion.choices[0].message['content']})
        return messages
    except Exception as ex:
        # логируем ошибку
        logger.error(f'Ошибка при взаимодействии с OpenAI API: {ex}')
        return messages

```