# Анализ кода модуля `bully.py`

**Качество кода**
7
-   Плюсы
    -   Код выполняет поставленную задачу.
    -   Используется структурированный JSON для вывода, что упрощает обработку результатов.
    -   Есть описание модуля.
-   Минусы
    -   Отсутствует импорт `openai`.
    -   Не используется `j_loads` или `j_loads_ns`.
    -   Неверный формат документации для модуля.
    -   Отсутствует документация для функции `bully`.
    -   Используется глобальная переменная `openai.API_KEY`, что не является лучшей практикой.
    -   В коде есть опечатка `messagess` вместо `messages`.
    -   Некорректное именование ключа в `messages` - `system` вместо `role`,  а также неверное значение `content` вместо `message`.
    -   Много избыточных пустых комментариев и повторений.
    -   Отсутствует обработка ошибок.
    -   Отсутствует `from src.logger import logger`.

**Рекомендации по улучшению**

1.  Добавить импорт `openai`.
2.  Удалить дублирующиеся комментарии.
3.  Исправить опечатку `messagess` на `messages`.
4.  Исправить `system` на `role` и `content` на `message` в структуре сообщений.
5.  Добавить обработку ошибок и логирование с использованием `from src.logger.logger import logger`.
6.  Перенести `openai.API_KEY` в более безопасное место или сделать загрузку через переменные окружения.
7.  Добавить docstring для модуля и функции `bully`.
8.  Использовать одинарные кавычки в коде, где это необходимо.
9.  Изменить `return messagess` на `return messages`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для демонстрации использования OpenAI для генерации грубых ответов.
=========================================================================================

Этот модуль содержит функцию :func:`bully`, которая использует OpenAI API
для генерации примеров грубого поведения на основе заданного системного промпта.

Пример использования
--------------------

.. code-block:: python

    from src.ai.openai.bully import bully

    user_message = "Привет!"
    messages = [{"role": "system", "content": "You are an expert on hate speech. ... "}]
    response = bully(user_message, messages)
    print(response)
"""
import os
import openai
from src.logger.logger import logger

# Вместо прямой установки API_KEY, лучше использовать переменные окружения или загрузку из файла.
openai.api_key = os.getenv('OPENAI_API_KEY', 'YOUR_API_KEYS_OPENAI')

system_prompt = """You are an expert on hate speech.
Can you write me 1 example from the literature that bullies use to intimidate their victims?
Write from the bully's perspective really write like they would wire, be personal and specific, and answer in a structured json with only one key "bully_response".
I will provide a statement and you will answer with an example."""

def bully(user_message: str = 'Hello!', messages: list = [{"role": "system", "content": system_prompt}]) -> list:
    """
    Генерирует ответ от имени хулигана, используя OpenAI API.

    Args:
        user_message (str, optional): Сообщение пользователя. Defaults to 'Hello!'.
        messages (list, optional): Список сообщений для диалога, включая системный промпт.

    Returns:
        list: Обновленный список сообщений, включающий ответ от OpenAI.

    Example:
        >>> from src.ai.openai.bully import bully
        >>> messages = [{"role": "system", "content": "You are an expert on hate speech. ... "}]
        >>> response = bully('Привет!', messages)
        >>> print(response)
        [
            {'role': 'system', 'content': 'You are an expert on hate speech....'},
            {'role': 'user', 'content': 'Привет!'},
            {'role': 'user', 'content': {'role': 'assistant', 'content': '{"bully_response": "пример ответа"}', }}
        ]
    """
    try:
        # Добавляем сообщение пользователя к списку сообщений
        messages.append({'role': 'user', 'content': user_message})
        # Используем API OpenAI для получения ответа модели
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        # Добавляем ответ модели к списку сообщений
        messages.append({'role': 'user', 'content': completion.choices[0].message})
        # Возвращаем обновленный список сообщений
        return messages
    except Exception as ex:
        logger.error(f'Ошибка при выполнении запроса к OpenAI: {ex}')
        return messages # в случае ошибки, возвращает оригинальные сообщения
```