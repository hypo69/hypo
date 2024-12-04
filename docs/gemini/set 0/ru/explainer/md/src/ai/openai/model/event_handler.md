# <input code>

```python
## \file hypotez/src/ai/openai/model/event_handler.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.ai.openai.model 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


""" https://github.com/openai/openai-python/blob/main/helpers.md#assistant-events """

from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta


# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.

class EventHandler(AssistantEventHandler):
  """ """

  @override
  def on_text_created(self, text: Text) -> None:
    print(f"\\nassistant > ", end="", flush=True)

  @override
  def on_text_delta(self, delta: TextDelta, snapshot: Text):
    print(delta.value, end="", flush=True)

  @override
  def on_tool_call_created(self, tool_call: ToolCall):
    print(f"\\nassistant > {tool_call.type}\\n", flush=True)

  @override
  def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
    if delta.type == "code_interpreter" and delta.code_interpreter:
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\\n\\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\\n{output.logs}", flush=True)

# Then, we use the `stream` SDK helper
# with the `EventHandler` class to create the Run
# and stream the response.
```

# <algorithm>

**Алгоритм работы кода:**

1. **Импорты:** Модули `typing_extensions`, `openai`, `Text`, `TextDelta`, `ToolCall`, `ToolCallDelta` импортируются для использования в классе `EventHandler`.
2. **Класс `EventHandler`:** Класс наследуется от `AssistantEventHandler` для обработки событий от API OpenAI.
3. **Методы обработчики:**
    - `on_text_created`: Выводит "assistant > " перед началом нового текста.
    - `on_text_delta`: Выводит новые части текста.
    - `on_tool_call_created`: Выводит тип инструмента (например, "code_interpreter").
    - `on_tool_call_delta`: Обрабатывает события, связанные с вызовами инструментов:
        - Если тип инструмента - "code_interpreter" и есть входные данные, выводит входные данные.
        - Если есть выходные данные, выводит "output >" и перебирает все выходные данные.
        - Если тип выходных данных - "logs", выводит логи.
4. **Использование (вне кода примера):** В другом месте кода (не показанном)  будет создание `Run` с использованием `EventHandler` и `stream` SDK, что вызовет обработчики класса `EventHandler` по мере получения событий.

**Пример данных:**

Входные данные для `on_tool_call_delta`:

```json
{
  "type": "code_interpreter",
  "code_interpreter": {
    "input": "print('Hello')",
    "outputs": [
      {
        "type": "logs",
        "logs": "Hello"
      }
    ]
  }
}
```


# <mermaid>

```mermaid
graph TD
    A[openai API] --> B(EventHandler);
    B --> C{on_text_created};
    C --Text--> D(print);
    B --> E{on_text_delta};
    E --Delta--> D;
    B --> F{on_tool_call_created};
    F --Type--> G(print);
    B --> H{on_tool_call_delta};
    H --Code Interpreter--> I[Check type];
    I --true--> J[Check Input];
    J --true--> D;
    I --false--> K[Check outputs];
    K --true--> L(loop);
    L --output.type == logs--> M(print);
    subgraph "OpenAI SDK"
        OpenAI ----> EventHandler;
    end
```

# <explanation>

**Импорты:**

- `from typing_extensions import override`: Импортирует аннотацию `@override`, которая используется для указания того, что метод переопределяет метод из родительского класса.
- `from openai import AssistantEventHandler, OpenAI`: Импортирует классы `AssistantEventHandler` и `OpenAI` из пакета `openai`.  `AssistantEventHandler`  позволяет обрабатывать события  от OpenAI API. `OpenAI`  предположительно используется для инициализации подключения к API.
- `from openai.types.beta.threads import Text, TextDelta`: Импортирует типы данных `Text` и `TextDelta`, которые представляют текстовые данные и их изменения в контексте потоков OpenAI.
- `from openai.types.beta.threads.runs import ToolCall, ToolCallDelta`: Импортирует типы данных `ToolCall` и `ToolCallDelta`, которые представляют вызовы инструментов и их изменения.
  Эти импорты связаны с `src.ai.openai` и `src.ai.openai.types` (предположительно).

**Классы:**

- `EventHandler`: Этот класс наследуется от `AssistantEventHandler` и предназначен для обработки событий, возвращаемых API OpenAI. Он содержит методы `on_text_created`, `on_text_delta`, `on_tool_call_created`, `on_tool_call_delta`, отвечающие за разные типы событий,  которые будут вызваны во время потока выполнения.

**Функции:**

- Все методы класса `EventHandler` являются обработчиками событий.
    - `on_text_created`: выводит строку "assistant >".
    - `on_text_delta`: выводит изменения в строке.
    - `on_tool_call_created`: выводит тип вызова инструмента.
    - `on_tool_call_delta`: выводит входные данные инструмента и результаты.

**Переменные:**

- `MODE = 'dev'`: Переменная, определяющая режим работы.


**Возможные ошибки и улучшения:**

- **Обработка исключений:**  Методы должны быть дополнены обработкой потенциальных исключений, связанных с данными, которые могут быть не в ожидаемом формате или отсутствовать. Например, в `on_tool_call_delta` необходимо проверить наличие атрибутов `delta.code_interpreter` и `delta.code_interpreter.outputs`.
- **Дополнительная валидация:** Проверка типа  `output.type` на `logs` должна быть расширена, чтобы обработать другие возможные типы вывода.
- **Логирование:** Добавление логгирования может помочь отследить поведение и диагностировать ошибки.
- **Документация:**  Добавление более подробной документации к методам, особенно аргументам и возвращаемым значениям, значительно улучшит читаемость и понимание кода.

**Взаимосвязи с другими частями проекта:**

Этот код взаимодействует с другими частями проекта (не показанными) посредством API OpenAI. Код в других файлах отвечает за инициализацию и вызов потоков.