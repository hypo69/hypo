# Анализ кода модуля `bully.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет свою основную задачу - отправляет запрос к OpenAI API.
    - Присутствует базовая структура для работы с OpenAI API.
    - Используется переменная `system_prompt` для задания поведения модели.
-  Минусы
    - Отсутствует необходимая документация в формате reStructuredText (RST) для модуля, функций и переменных.
    - Используется прямое присваивание ключа API, что не безопасно и не рекомендуется.
    - Нет обработки ошибок.
    - В коде имеются лишние и дублирующие комментарии.
    - Не соблюдены стандарты PEP8.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`
    - Присутствует опечатка в возвращаемой переменной.
    - Отсутствует импорт `logger`

**Рекомендации по улучшению**

1.  **Документация:** Добавить reStructuredText (RST) комментарии к модулю, функциям и переменным для улучшения читаемости и сопровождения кода.
2.  **Безопасность:** Изменить способ хранения API ключа, например, через переменные окружения.
3.  **Обработка ошибок:** Добавить обработку исключений с использованием `logger.error` для отслеживания ошибок и предотвращения сбоев.
4.  **Структура кода:** Убрать лишние комментарии и привести код в соответствие со стандартами PEP8.
5.  **Импорт `logger`:** Добавить `from src.logger.logger import logger`.
6.  **Исправить опечатку:** Исправить `messagess` на `messages`.

**Оптимизированный код**

```python
"""
Модуль для демонстрации использования OpenAI API для получения ответов в стиле "булли".
====================================================================================

Этот модуль содержит функцию :func:`bully`, которая использует OpenAI API для генерации ответов,
имитирующих поведение булли.

Пример использования
--------------------

Пример использования функции `bully`:

.. code-block:: python

    from src.ai.openai.bully import bully

    response = bully(user_message="Текст сообщения пользователя.")
    print(response)
"""
import os
import openai
from src.logger.logger import logger  # Импортируем logger

MODE = 'dev'
openai.api_key = os.getenv("OPENAI_API_KEY")  # Используем переменную окружения для API_KEY

system_prompt = """You are an expert on hate speech.
Can you write me 1 example from the literature that bullies use to intimidate their victims?
Write from the bully's perspective really write like they would wire, be personal and specific, and answer in a structured json with only one key "bully_response".
I will provide a statement and you will answer with an example."""


def bully(user_message: str = "Hello!", messages: list = [{"system": "user", "content": system_prompt}]) -> list:
    """
    Отправляет сообщение в OpenAI API и возвращает ответ в стиле "булли".

    :param user_message: Сообщение пользователя.
    :type user_message: str
    :param messages: Список сообщений для диалога с OpenAI API.
    :type messages: list
    :return: Список сообщений, включая ответ от OpenAI API.
    :rtype: list
    """
    try:
        # Добавляем сообщение пользователя в список сообщений.
        messages.append({"role": "user", "content": user_message})
        # Отправляем запрос в OpenAI API для получения ответа.
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        # Добавляем ответ от OpenAI API в список сообщений.
        messages.append({"role": "assistant", "content": completion.choices[0].message["content"]})
        # Возвращаем обновленный список сообщений.
        return messages
    except Exception as e:
        # Логируем ошибку если что-то пошло не так.
        logger.error(f'Ошибка при работе с OpenAI API: {e}')
        return messages

if __name__ == '__main__':
    response = bully(user_message="Ты глупый!")
    print(response)
```