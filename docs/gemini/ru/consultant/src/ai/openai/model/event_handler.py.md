# Анализ кода модуля `event_handler.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и использует классы для обработки событий.
    - Присутствуют аннотации типов, что улучшает читаемость и облегчает отладку.
    - Код использует `override` для переопределения методов, что является хорошей практикой.
    - Использование `flush=True` гарантирует немедленный вывод данных.
-  Минусы
    - Отсутствует документация в формате reStructuredText (RST).
    - Не используется `logger` для логирования ошибок.
    - Комментарии не соответствуют стандарту RST.
    - Нет обработки исключений.

**Рекомендации по улучшению**

1.  Добавить docstring в формате RST для модуля и класса `EventHandler`, а также для каждого метода.
2.  Использовать `logger` для логирования ошибок и отладочной информации.
3.  Удалить ненужные комментарии `# -*- coding: utf-8 -*-` и `#! venv/Scripts/python.exe` и `#! venv/bin/python/python3.12`.
4.  Добавить обработку ошибок при выводе данных.
5.  Сделать импорты более явными и структурированными.

**Оптимизированный код**

```python
"""
Модуль для обработки событий ассистента OpenAI
=================================================

Этот модуль определяет класс `EventHandler`, который используется для обработки
событий, генерируемых ассистентом OpenAI при выполнении задач.
Класс реализует методы для обработки текстовых сообщений и вызовов инструментов.

Пример использования
--------------------

.. code-block:: python

    from openai import OpenAI
    from src.ai.openai.model.event_handler import EventHandler

    client = OpenAI()
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="What is 1+1?",
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_...",
    )

    event_handler = EventHandler()
    stream = client.beta.threads.runs.stream(run.id, thread_id=thread.id, event_handler=event_handler)

"""
from typing import Any

from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta

from src.logger.logger import logger


MODE = 'dev'


class EventHandler(AssistantEventHandler):
    """
    Обработчик событий ассистента.

    Этот класс переопределяет методы `AssistantEventHandler` для обработки
    событий создания и изменения текста и вызовов инструментов.
    """

    @override
    def on_text_created(self, text: Text) -> None:
        """
        Вызывается при создании нового текстового объекта.

        :param text: Объект Text, представляющий созданный текст.
        :return: None
        """
        print("\nassistant > ", end="", flush=True)
        # Выводит начало сообщения от ассистента

    @override
    def on_text_delta(self, delta: TextDelta, snapshot: Text):
        """
        Вызывается при изменении текстового объекта.

        :param delta: Объект TextDelta, представляющий изменение текста.
        :param snapshot: Объект Text, представляющий текущее состояние текста.
        :return: None
        """
        try:
            print(delta.value, end="", flush=True)
            # Выводит дельту текста
        except Exception as ex:
            logger.error(f'Ошибка при выводе дельты текста {ex}')
            ...

    @override
    def on_tool_call_created(self, tool_call: ToolCall):
        """
        Вызывается при создании нового вызова инструмента.

        :param tool_call: Объект ToolCall, представляющий вызов инструмента.
        :return: None
        """
        try:
            print(f"\nassistant > {tool_call.type}\n", flush=True)
             # Выводит информацию о вызове инструмента
        except Exception as ex:
            logger.error(f'Ошибка при выводе информации о вызове инструмента {ex}')
            ...

    @override
    def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
        """
        Вызывается при изменении вызова инструмента.

        :param delta: Объект ToolCallDelta, представляющий изменение вызова инструмента.
        :param snapshot: Объект ToolCall, представляющий текущее состояние вызова инструмента.
        :return: None
        """
        try:
            if delta.type == "code_interpreter" and delta.code_interpreter:
                if delta.code_interpreter.input:
                    print(delta.code_interpreter.input, end="", flush=True)
                if delta.code_interpreter.outputs:
                    print("\n\noutput >", flush=True)
                    for output in delta.code_interpreter.outputs:
                        if output.type == "logs":
                            print(f"\n{output.logs}", flush=True)
            # Код проверяет, что тип инструмента code_interpreter, и выводит его ввод и вывод
        except Exception as ex:
             logger.error(f'Ошибка при выводе информации о дельте вызова инструмента {ex}')
             ...
```