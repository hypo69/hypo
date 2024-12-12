## Улучшенный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для обработки событий ассистента OpenAI
=========================================================================================

Этот модуль определяет класс :class:`EventHandler`, который используется для обработки событий,
генерируемых ассистентом OpenAI, таких как создание текста, дельты текста, вызовы инструментов и их дельты.
Он использует библиотеку `openai` и `typing_extensions`.

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
        content="What is 1 + 1?",
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_...",
    )
    stream = client.beta.threads.runs.retrieve_stream(
        run_id=run.id,
        thread_id=thread.id,
        event_handler=EventHandler()
    )
    for event in stream:
        ...
"""
from typing import Any

from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta

from src.logger.logger import logger  # импорт логгера


MODE = 'dev'


class EventHandler(AssistantEventHandler):
  """
  Класс для обработки событий, генерируемых ассистентом OpenAI.

  Этот класс переопределяет методы `on_text_created`, `on_text_delta`,
  `on_tool_call_created` и `on_tool_call_delta` для обработки различных типов событий,
  возникающих во время работы ассистента.
  """

  @override
  def on_text_created(self, text: Text) -> None:
    """
    Обрабатывает событие создания нового текстового блока.

    :param text: Объект Text, представляющий созданный текстовый блок.
    :return: None
    """
    # Выводит в консоль начало нового текстового блока от ассистента.
    print('\nassistant > ', end='', flush=True)

  @override
  def on_text_delta(self, delta: TextDelta, snapshot: Text) -> None:
    """
    Обрабатывает событие изменения текстового блока.

    :param delta: Объект TextDelta, представляющий изменения в текстовом блоке.
    :param snapshot: Объект Text, представляющий текущее состояние текстового блока.
    :return: None
    """
    # Выводит в консоль дельту текстового блока от ассистента.
    print(delta.value, end='', flush=True)

  @override
  def on_tool_call_created(self, tool_call: ToolCall) -> None:
    """
    Обрабатывает событие создания нового вызова инструмента.

    :param tool_call: Объект ToolCall, представляющий созданный вызов инструмента.
    :return: None
    """
    # Выводит в консоль тип вызванного инструмента.
    print(f'\nassistant > {tool_call.type}\n', flush=True)

  @override
  def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall) -> None:
    """
    Обрабатывает событие изменения вызова инструмента.

    :param delta: Объект ToolCallDelta, представляющий изменения в вызове инструмента.
    :param snapshot: Объект ToolCall, представляющий текущее состояние вызова инструмента.
    :return: None
    """
    # Проверяет, является ли дельта вызовом code_interpreter и существует ли ввод.
    if delta.type == 'code_interpreter' and delta.code_interpreter:
        if delta.code_interpreter.input:
            # Выводит в консоль ввод code_interpreter.
            print(delta.code_interpreter.input, end='', flush=True)
        if delta.code_interpreter.outputs:
            # Выводит в консоль начало вывода code_interpreter.
            print('\n\noutput >', flush=True)
            for output in delta.code_interpreter.outputs:
                if output.type == 'logs':
                   # Выводит в консоль логи code_interpreter.
                   print(f'\n{output.logs}', flush=True)
```
## Внесённые изменения
1. **Добавлены импорты:**
   - Добавлен импорт `from src.logger.logger import logger` для логирования.
   - Добавлен импорт `from typing import Any` для определения типа Any
2. **Документация:**
   - Добавлены reStructuredText комментарии к модулю, классу и методам.
   - Добавлены подробные описания к каждому методу и их параметрам.
3. **Улучшение кода:**
   - Добавлены комментарии в коде для пояснения работы каждого блока кода.
   - Изменены строковые литералы для соответствия стандарту (использование одинарных кавычек).

## Оптимизированный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для обработки событий ассистента OpenAI
=========================================================================================

Этот модуль определяет класс :class:`EventHandler`, который используется для обработки событий,
генерируемых ассистентом OpenAI, таких как создание текста, дельты текста, вызовы инструментов и их дельты.
Он использует библиотеку `openai` и `typing_extensions`.

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
        content="What is 1 + 1?",
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_...",
    )
    stream = client.beta.threads.runs.retrieve_stream(
        run_id=run.id,
        thread_id=thread.id,
        event_handler=EventHandler()
    )
    for event in stream:
        ...
"""
from typing import Any

from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta

from src.logger.logger import logger  # импорт логгера


MODE = 'dev'


class EventHandler(AssistantEventHandler):
  """
  Класс для обработки событий, генерируемых ассистентом OpenAI.

  Этот класс переопределяет методы `on_text_created`, `on_text_delta`,
  `on_tool_call_created` и `on_tool_call_delta` для обработки различных типов событий,
  возникающих во время работы ассистента.
  """

  @override
  def on_text_created(self, text: Text) -> None:
    """
    Обрабатывает событие создания нового текстового блока.

    :param text: Объект Text, представляющий созданный текстовый блок.
    :return: None
    """
    # Выводит в консоль начало нового текстового блока от ассистента.
    print('\nassistant > ', end='', flush=True)

  @override
  def on_text_delta(self, delta: TextDelta, snapshot: Text) -> None:
    """
    Обрабатывает событие изменения текстового блока.

    :param delta: Объект TextDelta, представляющий изменения в текстовом блоке.
    :param snapshot: Объект Text, представляющий текущее состояние текстового блока.
    :return: None
    """
    # Выводит в консоль дельту текстового блока от ассистента.
    print(delta.value, end='', flush=True)

  @override
  def on_tool_call_created(self, tool_call: ToolCall) -> None:
    """
    Обрабатывает событие создания нового вызова инструмента.

    :param tool_call: Объект ToolCall, представляющий созданный вызов инструмента.
    :return: None
    """
    # Выводит в консоль тип вызванного инструмента.
    print(f'\nassistant > {tool_call.type}\n', flush=True)

  @override
  def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall) -> None:
    """
    Обрабатывает событие изменения вызова инструмента.

    :param delta: Объект ToolCallDelta, представляющий изменения в вызове инструмента.
    :param snapshot: Объект ToolCall, представляющий текущее состояние вызова инструмента.
    :return: None
    """
    # Проверяет, является ли дельта вызовом code_interpreter и существует ли ввод.
    if delta.type == 'code_interpreter' and delta.code_interpreter:
        if delta.code_interpreter.input:
            # Выводит в консоль ввод code_interpreter.
            print(delta.code_interpreter.input, end='', flush=True)
        if delta.code_interpreter.outputs:
            # Выводит в консоль начало вывода code_interpreter.
            print('\n\noutput >', flush=True)
            for output in delta.code_interpreter.outputs:
                if output.type == 'logs':
                   # Выводит в консоль логи code_interpreter.
                   print(f'\n{output.logs}', flush=True)