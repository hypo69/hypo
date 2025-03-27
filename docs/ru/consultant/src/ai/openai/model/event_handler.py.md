# Анализ кода модуля `event_handler`

**Качество кода**:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Использование `typing_extensions.override` для переопределения методов.
    - Наличие класса `EventHandler`, наследующегося от `AssistantEventHandler`.
    - Правильное использование `print` для вывода данных в консоль.
- **Минусы**:
    - Отсутствует документация к классу и методам в формате RST.
    - Не используется `logger` для отслеживания ошибок, что затрудняет отладку.
    -  Импорт `OpenAI` не используется в коде, поэтому он лишний.

**Рекомендации по улучшению**:

- Добавить документацию в формате RST для класса `EventHandler` и его методов. Это улучшит понимание кода и упростит его использование.
-  Импортировать `logger` из `src.logger` и использовать его для записи сообщений и ошибок.
- Удалить неиспользуемый импорт `OpenAI`.
- Добавить обработку ошибок через `try-except` с логированием в `logger.error`.
-  Переформатировать вывод сообщений для лучшей читаемости, разделив разные типы сообщений (assistant, tool call, output).
-  Заменить множественные `print` на `logger.info` для улучшения читаемости кода.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-
"""
Модуль для обработки событий ассистента OpenAI
=================================================

Модуль содержит класс :class:`EventHandler`, который наследуется от :class:`openai.AssistantEventHandler`
и используется для обработки событий, возникающих во время работы ассистента.

Пример использования
----------------------
.. code-block:: python

    event_handler = EventHandler()
    # Использование event_handler в stream
"""
from typing_extensions import override
from openai import AssistantEventHandler
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta
from src.logger import logger  #  Импортируем logger из src.logger


# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.
class EventHandler(AssistantEventHandler):
    """
    Обработчик событий ассистента.

    Этот класс переопределяет методы :meth:`on_text_created`, :meth:`on_text_delta`,
    :meth:`on_tool_call_created` и :meth:`on_tool_call_delta` для обработки событий,
    возникающих при работе ассистента.
    """
    @override
    def on_text_created(self, text: Text) -> None:
        """
        Обрабатывает событие создания текста.

        :param text: Объект Text, содержащий созданный текст.
        :type text: Text
        """
        try:
            logger.info("\nassistant > ", end="", flush=True) # Используем logger.info для вывода сообщения
        except Exception as e:
            logger.error(f"Error in on_text_created: {e}") # Логируем ошибку при возникновении исключения

    @override
    def on_text_delta(self, delta: TextDelta, snapshot: Text):
        """
        Обрабатывает событие изменения текста.

        :param delta: Объект TextDelta, содержащий изменение текста.
        :type delta: TextDelta
        :param snapshot: Объект Text, представляющий текущий снимок текста.
        :type snapshot: Text
        """
        try:
            logger.info(delta.value, end="", flush=True) # Используем logger.info для вывода изменения текста
        except Exception as e:
             logger.error(f"Error in on_text_delta: {e}") # Логируем ошибку при возникновении исключения


    @override
    def on_tool_call_created(self, tool_call: ToolCall):
        """
        Обрабатывает событие создания вызова инструмента.

        :param tool_call: Объект ToolCall, содержащий информацию о вызове инструмента.
        :type tool_call: ToolCall
        """
        try:
            logger.info(f"\nassistant > {tool_call.type}\n", flush=True) # Используем logger.info для вывода информации о вызове инструмента
        except Exception as e:
            logger.error(f"Error in on_tool_call_created: {e}") # Логируем ошибку при возникновении исключения


    @override
    def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
        """
        Обрабатывает событие изменения вызова инструмента.

        :param delta: Объект ToolCallDelta, содержащий изменения вызова инструмента.
        :type delta: ToolCallDelta
        :param snapshot: Объект ToolCall, представляющий текущий снимок вызова инструмента.
        :type snapshot: ToolCall
        """
        try:
             if delta.type == "code_interpreter" and delta.code_interpreter:
                 if delta.code_interpreter.input:
                    logger.info(delta.code_interpreter.input, end="", flush=True) # Используем logger.info для вывода ввода интерпретатора кода
                 if delta.code_interpreter.outputs:
                    logger.info("\n\noutput >", flush=True) # Используем logger.info для вывода заголовка вывода
                    for output in delta.code_interpreter.outputs:
                        if output.type == "logs":
                            logger.info(f"\n{output.logs}", flush=True) # Используем logger.info для вывода логов
        except Exception as e:
            logger.error(f"Error in on_tool_call_delta: {e}") # Логируем ошибку при возникновении исключения
# Then, we use the `stream` SDK helper
# with the `EventHandler` class to create the Run
# and stream the response.
```