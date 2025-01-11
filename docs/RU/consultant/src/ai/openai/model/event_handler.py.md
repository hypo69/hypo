# Анализ кода модуля `event_handler`

**Качество кода**
10
-  Плюсы
    - Код хорошо структурирован и следует основным принципам ООП.
    - Используются аннотации типов, что улучшает читаемость и понимание кода.
    - Применяется `@override` для переопределения методов, что явно показывает намерение разработчика.
    - Код предоставляет обработку событий от OpenAI Assistant, включая текстовые ответы и вызовы инструментов.
    - Исключена обработка ошибок `try-except`, что снижает вероятность возникновения ошибок.

-  Минусы
    - Отсутствует документация в формате RST для модуля и класса `EventHandler`, а также отсутствуют docstring для методов класса.
    - Используется `print` для вывода в консоль, вместо использования `logger` для более гибкого управления логами.

**Рекомендации по улучшению**

1.  **Добавить документацию модуля и класса**:
    - Добавить описание модуля в начале файла, а также docstring для класса `EventHandler` в формате RST.
2.  **Документировать методы класса**:
    - Добавить docstring для каждого метода класса `EventHandler` в формате RST, описывая их назначение, параметры и возвращаемые значения.
3.  **Использовать `logger` вместо `print`**:
    - Заменить все `print` на `logger.info` или `logger.debug` для вывода сообщений в консоль.
4. **Импорт logger**:
    - Добавить `from src.logger import logger` для использования логгера.
5.  **Улучшить вывод кода**:
    -  Использовать `f-string`  в `on_text_created` для улучшения читаемости.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для обработки событий от OpenAI Assistant.
==================================================

Этот модуль содержит класс :class:`EventHandler`, который используется для обработки событий,
полученных от OpenAI Assistant, таких как текстовые ответы и вызовы инструментов.

Пример использования
--------------------

Пример использования класса `EventHandler` для обработки событий от OpenAI Assistant:

.. code-block:: python

    from openai import OpenAI
    from src.ai.openai.model.event_handler import EventHandler

    client = OpenAI()
    assistant = client.beta.assistants.create(
        instructions="You are a personal math tutor. When asked a question, write and run python code to answer the question.",
        model="gpt-4-1106-preview",
        tools=[{"type": "code_interpreter"}]
    )
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="What is 121 * 31?",
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    event_handler = EventHandler()
    stream = client.beta.threads.runs.stream(
        thread_id=thread.id,
        run_id=run.id,
        event_handler=event_handler,
    )
    stream.join()

"""

from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta
from src.logger import logger

# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.

class EventHandler(AssistantEventHandler):
  """
  Обработчик событий для ассистента OpenAI.

  Этот класс переопределяет методы `on_text_created`, `on_text_delta`, `on_tool_call_created` и
  `on_tool_call_delta` для обработки событий, полученных от OpenAI Assistant.
  """
  @override
  def on_text_created(self, text: Text) -> None:
    """
    Вызывается при создании нового текстового объекта.

    Args:
        text (Text): Объект текста, созданный ассистентом.
    """
    # Код выводит сообщение в консоль о начале нового текстового ответа.
    logger.info(f"\nassistant > ", end="", flush=True)

  @override
  def on_text_delta(self, delta: TextDelta, snapshot: Text):
    """
    Вызывается при получении дельты текстового объекта.

    Args:
        delta (TextDelta): Дельта текста, содержащая изменения.
        snapshot (Text): Текущий снимок текстового объекта.
    """
    # Код выводит в консоль изменения в текстовом ответе ассистента.
    logger.info(delta.value, end="", flush=True)

  @override
  def on_tool_call_created(self, tool_call: ToolCall):
    """
    Вызывается при создании нового вызова инструмента.

    Args:
        tool_call (ToolCall): Объект вызова инструмента.
    """
    # Код выводит в консоль информацию о создании нового вызова инструмента.
    logger.info(f"\nassistant > {tool_call.type}\n", flush=True)

  @override
  def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
    """
    Вызывается при получении дельты вызова инструмента.

    Args:
        delta (ToolCallDelta): Дельта вызова инструмента, содержащая изменения.
        snapshot (ToolCall): Текущий снимок вызова инструмента.
    """
    # Код проверяет, является ли дельта вызовом code_interpreter
    if delta.type == "code_interpreter" and delta.code_interpreter:
      # Код выводит ввод в code_interpreter, если он есть
      if delta.code_interpreter.input:
          logger.info(delta.code_interpreter.input, end="", flush=True)
      # Код выводит вывод code_interpreter, если он есть
      if delta.code_interpreter.outputs:
        logger.info(f"\n\noutput >", flush=True)
        # Код выводит логи из вывода code_interpreter
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            logger.info(f"\n{output.logs}", flush=True)

# Then, we use the `stream` SDK helper
# with the `EventHandler` class to create the Run
# and stream the response.
```