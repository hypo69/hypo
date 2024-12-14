# Анализ кода модуля `event_handler.py`

**Качество кода**
8
- Плюсы
    - Код использует `typing_extensions.override` для переопределения методов, что повышает читаемость и безопасность.
    - Код логически разделен на обработку текстовых и инструментальных вызовов.
    - Имеется обработка `code_interpreter`, включая его ввод и вывод.
    - Присутствует использование `flush=True` для немедленного отображения вывода в консоль.
- Минусы
    - Отсутствует документация в формате RST.
    - Не используется логгер для записи ошибок и отладочной информации.
    - Не хватает обработки исключений, что может привести к проблемам при ошибках.
    - Используется стандартный `print` для вывода, что не очень гибко и не позволяет отслеживать события в более сложной системе.
    - Отсутствует описание модуля и класса.
    - Не хватает импорта `from src.logger.logger import logger`.

**Рекомендации по улучшению**
1. Добавить docstring в формате RST для модуля, класса и методов.
2. Использовать `from src.logger.logger import logger` для логирования ошибок и отладочной информации.
3. Заменить `print` на `logger.debug` для отладочных сообщений и `logger.info` для информационных.
4. Добавить обработку исключений в методах для повышения отказоустойчивости.
5. Уточнить комментарии, где это необходимо.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для обработки событий ассистента OpenAI
=========================================================================================

Этот модуль содержит класс :class:`EventHandler`, который используется для обработки событий,
возникающих при взаимодействии с ассистентом OpenAI.
Он обрабатывает текстовые сообщения и вызовы инструментов, предоставляя возможность отслеживать
и логировать эти события.

Пример использования
--------------------

Пример использования класса `EventHandler` для обработки событий:

.. code-block:: python

    event_handler = EventHandler()
    # Пример использования event_handler при запуске ассистента

"""
MODE = 'dev'

from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta
from src.logger.logger import logger


class EventHandler(AssistantEventHandler):
  """
  Класс для обработки событий ассистента OpenAI.

  Обрабатывает события создания текста, дельты текста, вызовы инструментов и их дельты.
  Используется для потоковой передачи ответов от ассистента и их отображения в консоли.
  """

  @override
  def on_text_created(self, text: Text) -> None:
    """
    Вызывается при создании нового текстового сообщения от ассистента.

    :param text: Объект Text, содержащий текст сообщения.
    """
    logger.debug(f"Создан текст от ассистента: {text=}") # Логирование создания текста
    print("\nassistant > ", end="", flush=True) # Вывод в консоль с флагом flush для немедленного отображения

  @override
  def on_text_delta(self, delta: TextDelta, snapshot: Text) -> None:
    """
    Вызывается при получении дельты текстового сообщения от ассистента.

    :param delta: Объект TextDelta, содержащий изменение текста.
    :param snapshot: Объект Text, представляющий текущий снимок текста.
    """
    logger.debug(f"Получена дельта текста: {delta.value=}") # Логирование дельты текста
    print(delta.value, end="", flush=True) # Вывод в консоль дельты текста

  @override
  def on_tool_call_created(self, tool_call: ToolCall) -> None:
    """
    Вызывается при создании вызова инструмента.

    :param tool_call: Объект ToolCall, представляющий вызов инструмента.
    """
    logger.debug(f"Создан вызов инструмента: {tool_call.type=}") # Логирование создания вызова инструмента
    print(f"\nassistant > {tool_call.type}\n", flush=True) # Вывод типа вызова инструмента в консоль

  @override
  def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall) -> None:
    """
    Вызывается при получении дельты вызова инструмента.

    :param delta: Объект ToolCallDelta, содержащий изменение вызова инструмента.
    :param snapshot: Объект ToolCall, представляющий текущий снимок вызова инструмента.
    """
    try:
        # Проверка типа дельты и наличие code_interpreter
        if delta.type == "code_interpreter" and delta.code_interpreter:
            # Обработка ввода code_interpreter
            if delta.code_interpreter.input:
                logger.debug(f"Получен ввод code_interpreter: {delta.code_interpreter.input=}")
                print(delta.code_interpreter.input, end="", flush=True)
            # Обработка вывода code_interpreter
            if delta.code_interpreter.outputs:
                print("\n\noutput >", flush=True)
                for output in delta.code_interpreter.outputs:
                    if output.type == "logs":
                        logger.debug(f"Получен вывод code_interpreter: {output.logs=}")
                        print(f"\n{output.logs}", flush=True)
    except Exception as ex:
        logger.error(f'Ошибка при обработке дельты вызова инструмента: {ex}', exc_info=True) # Логирование ошибки
```