## <алгоритм>

1. **Инициализация:**
   - Определяется глобальная переменная `MODE` со значением `'dev'`. Это может использоваться для переключения между режимами разработки и продакшна.
   - Импортируются необходимые классы и типы из библиотек `typing_extensions` и `openai`.

2. **Создание класса `EventHandler`:**
   - Создается класс `EventHandler`, который наследуется от `AssistantEventHandler`.
   - Этот класс переопределяет несколько методов, которые вызываются при возникновении различных событий во время стриминга ответа от OpenAI Assistant.

3. **Метод `on_text_created`:**
   - Вызывается, когда создается новый текстовый блок.
   - Печатает "assistant > " в консоль, подготавливая вывод текста от ассистента.

   ```python
   def on_text_created(self, text: Text) -> None:
       print(f"\nassistant > ", end="", flush=True)
   ```

4. **Метод `on_text_delta`:**
   - Вызывается при получении текстовой дельты (части текста).
   - Печатает полученную дельту в консоль, таким образом стримя текст по частям.

   ```python
   def on_text_delta(self, delta: TextDelta, snapshot: Text):
       print(delta.value, end="", flush=True)
   ```

5. **Метод `on_tool_call_created`:**
   - Вызывается, когда создается новый вызов инструмента (например, code interpreter).
   - Выводит в консоль тип вызванного инструмента.

   ```python
   def on_tool_call_created(self, tool_call: ToolCall):
       print(f"\nassistant > {tool_call.type}\n", flush=True)
   ```

6. **Метод `on_tool_call_delta`:**
   - Вызывается при получении дельты вызова инструмента.
   - Проверяет, является ли инструмент `code_interpreter`.
   - Если это code_interpreter, то выводит входной код и логи (выходы) в консоль.

   ```python
   def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
       if delta.type == "code_interpreter" and delta.code_interpreter:
           if delta.code_interpreter.input:
               print(delta.code_interpreter.input, end="", flush=True)
           if delta.code_interpreter.outputs:
               print(f"\n\noutput >", flush=True)
               for output in delta.code_interpreter.outputs:
                   if output.type == "logs":
                       print(f"\n{output.logs}", flush=True)
   ```

## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> EventHandlerClass[Class: <code>EventHandler</code>]
    
    EventHandlerClass --> on_text_created[Method: <code>on_text_created(text: Text)</code>]
    on_text_created --> PrintAssistantTextCreated[Print: "assistant > "]
    PrintAssistantTextCreated --> EndOnTextCreated[End: <code>on_text_created</code>]
    
    EventHandlerClass --> on_text_delta[Method: <code>on_text_delta(delta: TextDelta, snapshot: Text)</code>]
    on_text_delta --> PrintTextDelta[Print: <code>delta.value</code>]
     PrintTextDelta --> EndOnTextDelta[End: <code>on_text_delta</code>]
    
    EventHandlerClass --> on_tool_call_created[Method: <code>on_tool_call_created(tool_call: ToolCall)</code>]
    on_tool_call_created --> PrintToolCallType[Print: <code>tool_call.type</code>]
    PrintToolCallType --> EndOnToolCallCreated[End: <code>on_tool_call_created</code>]

    EventHandlerClass --> on_tool_call_delta[Method: <code>on_tool_call_delta(delta: ToolCallDelta, snapshot: ToolCall)</code>]
    on_tool_call_delta --> CheckToolType[Check: <code>delta.type == "code_interpreter"</code>]
    CheckToolType -- Yes --> CheckCodeInterpreterInput[Check: <code>delta.code_interpreter.input</code>]
     CheckCodeInterpreterInput -- Yes --> PrintCodeInterpreterInput[Print: <code>delta.code_interpreter.input</code>]
     PrintCodeInterpreterInput --> CheckCodeInterpreterOutputs[Check: <code>delta.code_interpreter.outputs</code>]
     CheckCodeInterpreterInput -- No --> CheckCodeInterpreterOutputs
     CheckCodeInterpreterOutputs -- Yes --> PrintOutputHeader[Print: "output >"]
      PrintOutputHeader --> LoopOutputs[Loop: for output in <code>delta.code_interpreter.outputs</code>]
        LoopOutputs --> CheckOutputType[Check: <code>output.type == "logs"</code>]
            CheckOutputType -- Yes --> PrintLogs[Print: <code>output.logs</code>]
             PrintLogs --> EndLoopOutputs[End loop]
            CheckOutputType -- No --> EndLoopOutputs
     CheckCodeInterpreterOutputs -- No --> EndOnToolCallDelta
    CheckToolType -- No --> EndOnToolCallDelta
   
    EndOnTextCreated --> End[End]
    EndOnTextDelta --> End
    EndOnToolCallCreated --> End
    EndOnToolCallDelta --> End
    EndLoopOutputs -->EndOnToolCallDelta
```

### Анализ зависимостей `mermaid`
- **`EventHandlerClass`**: Представляет класс `EventHandler`, который отвечает за обработку событий от OpenAI Assistant.
- **`on_text_created`, `on_text_delta`, `on_tool_call_created`, `on_tool_call_delta`**: Это методы класса `EventHandler`, которые обрабатывают различные типы событий.
- **`Text`, `TextDelta`, `ToolCall`, `ToolCallDelta`**: Типы данных, представляющие текстовые и инструментальные вызовы, используемые в методах.
- **`PrintAssistantTextCreated`, `PrintTextDelta`, `PrintToolCallType`, `PrintCodeInterpreterInput`, `PrintOutputHeader`, `PrintLogs`**: Операции вывода в консоль различных данных.
- **`CheckToolType`, `CheckCodeInterpreterInput`, `CheckCodeInterpreterOutputs`, `CheckOutputType`**: Логические проверки условий.
- **`LoopOutputs`**: Цикл для обработки нескольких выходов `code_interpreter`.

## <объяснение>

### Импорты

-   `from typing_extensions import override`: Импортируется декоратор `override`, который используется для аннотации методов, переопределяющих методы родительского класса. Это улучшает читаемость и помогает избежать ошибок при рефакторинге.
-   `from openai import AssistantEventHandler, OpenAI`: Импортируется `AssistantEventHandler` – базовый класс для обработки событий ассистента OpenAI и `OpenAI` - класс для взаимодействия с OpenAI API.
-   `from openai.types.beta.threads import Text, TextDelta`: Импортируются типы данных `Text` и `TextDelta`, представляющие текстовые данные и их изменения при стриминге. Эти типы используются для обработки текстовых ответов от ассистента.
-   `from openai.types.beta.threads.runs import ToolCall, ToolCallDelta`: Импортируются типы данных `ToolCall` и `ToolCallDelta`, представляющие вызовы инструментов (например, code interpreter) и их изменения при стриминге.

### Классы

-   **`EventHandler(AssistantEventHandler)`**:
    -   **Роль**: Этот класс обрабатывает события, возникающие во время стриминга ответов от OpenAI Assistant. Он наследуется от `AssistantEventHandler`, переопределяя его методы для кастомизации обработки событий.
    -   **Атрибуты**: Класс не имеет атрибутов.
    -   **Методы**:
        -   `on_text_created(self, text: Text) -> None`:
            -   **Аргументы**: `text` типа `Text` (новый текстовый блок).
            -   **Возвращаемое значение**: `None`.
            -   **Назначение**: Вызывается при создании нового текстового блока. Выводит в консоль "assistant > ", подготавливая вывод текста.
        -   `on_text_delta(self, delta: TextDelta, snapshot: Text)`:
            -   **Аргументы**: `delta` типа `TextDelta` (изменение текста), `snapshot` типа `Text` (текущий текст).
            -   **Возвращаемое значение**: `None`.
            -   **Назначение**: Вызывается при получении дельты текста. Выводит значение дельты в консоль, обеспечивая стриминг текста.
        -   `on_tool_call_created(self, tool_call: ToolCall)`:
            -   **Аргументы**: `tool_call` типа `ToolCall` (вызов инструмента).
            -   **Возвращаемое значение**: `None`.
            -   **Назначение**: Вызывается при создании вызова инструмента. Выводит в консоль тип вызванного инструмента.
        -   `on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall)`:
            -   **Аргументы**: `delta` типа `ToolCallDelta` (дельта вызова инструмента), `snapshot` типа `ToolCall` (текущий вызов инструмента).
            -   **Возвращаемое значение**: `None`.
            -   **Назначение**: Вызывается при получении дельты вызова инструмента. Если это вызов `code_interpreter`, выводит входной код и логи (выходы).
    -   **Взаимодействие**: Класс взаимодействует с API OpenAI, перехватывая события стриминга.

### Функции

-   В данном коде нет отдельных функций, все операции выполняются внутри методов класса `EventHandler`.

### Переменные

-   `MODE`: Глобальная переменная, определяющая режим работы (по умолчанию 'dev'). Возможно, используется для изменения поведения кода в разных средах.
- `text`:  Переменная типа `Text`, используется в методе `on_text_created`, представляет текстовый блок ответа от ассистента
- `delta`:  Переменная типа `TextDelta`, используется в методе `on_text_delta`, представляет изменение текста
- `snapshot`:  Переменная типа `Text`, используется в методе `on_text_delta`, представляет текущий текст
- `tool_call`: Переменная типа `ToolCall`, используется в методе `on_tool_call_created`, представляет вызов инструмента от ассистента
- `delta`:  Переменная типа `ToolCallDelta`, используется в методе `on_tool_call_delta`, представляет изменение вызова инструмента
- `snapshot`: Переменная типа `ToolCall`, используется в методе `on_tool_call_delta`, представляет текущий вызов инструмента
- `output`: Переменная итератор в цикле `for output in delta.code_interpreter.outputs`, которая представляет собой отдельный выход code_interpreter

### Потенциальные ошибки и области для улучшения

-   **Обработка ошибок**: Код не включает обработку ошибок, таких как ошибки API OpenAI или проблемы с сетью. Добавление обработки исключений сделает код более надежным.
-   **Логирование**: Вместо вывода в консоль, можно добавить логирование для отслеживания событий и ошибок в продакшене.
-   **Конфигурация**: Значение `MODE = 'dev'` задано статически. Можно сделать этот параметр конфигурируемым через переменные окружения или файл конфигурации.
-   **Управление состоянием**: Класс `EventHandler` не управляет состоянием стриминга. Добавление логики для управления состоянием (например, завершение стриминга) может быть полезным.

### Цепочка взаимосвязей

1.  **`hypotez/src/ai/openai/model/event_handler.py`** используется для обработки событий стриминга ответов от OpenAI Assistant.
2.  Он использует классы и типы данных из пакета **`openai`**, который предоставляет интерфейс для работы с OpenAI API.
3.  Класс `EventHandler` будет использован при создании `Run` в коде, взаимодействующем с OpenAI API для ассистентов.
4.  `MODE` может использоваться в других частях проекта для определения режима работы приложения.

Этот файл является важным компонентом для обеспечения стриминга и обработки ответов от OpenAI Assistant с инструментами, такими как code interpreter.