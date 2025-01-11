## <алгоритм>
1.  **Инициализация:**
    *   Создается класс `EventHandler`, наследующий от `AssistantEventHandler`. Этот класс будет обрабатывать события, возникающие во время потоковой передачи ответов от OpenAI Assistant.
2.  **Обработка события `on_text_created`:**
    *   При создании нового текстового фрагмента (событие `on_text_created`) выводится строка `"\nassistant > "` в консоль.  
        *   Пример: Выводится `"\nassistant > "` перед началом потоковой передачи текста ответа.
3.  **Обработка события `on_text_delta`:**
    *   При получении дельты (изменения) текста (событие `on_text_delta`) выводится значение дельты (`delta.value`) в консоль. Это позволяет отображать текст ответа асинхронно по мере его поступления.
        *   Пример: По мере поступления текста выводится каждое слово или предложение, образуя полноценный ответ.
4.  **Обработка события `on_tool_call_created`:**
    *   При создании вызова инструмента (событие `on_tool_call_created`) выводится в консоль строка с типом инструмента `\nassistant > {tool_call.type}\n`.
        *   Пример: Если инструмент - `code_interpreter`, выводится строка `\nassistant > code_interpreter\n`.
5.  **Обработка события `on_tool_call_delta`:**
    *   При получении дельты вызова инструмента (событие `on_tool_call_delta`) проверяется, является ли инструмент `code_interpreter`.
        *   Если это `code_interpreter`:
            *   Если есть ввод (`delta.code_interpreter.input`), он выводится в консоль.
                 * Пример: `print("print(1+1)", flush=True)`
            *   Если есть вывод (`delta.code_interpreter.outputs`):
                *   Выводится строка `"\n\noutput >"` в консоль.
                *   Для каждого вывода проверяется, является ли он логами (`output.type == "logs"`).
                    *   Если это логи, они выводятся в консоль.
                          * Пример: `print("\n2", flush=True)`
6.  **Использование `EventHandler`:**
    *   Класс `EventHandler` предназначен для использования с SDK OpenAI `stream`, чтобы отслеживать и обрабатывать события при выполнении запроса к ассистенту.

## <mermaid>
```mermaid
flowchart TD
    classDef eventHandlerClass fill:#f9f,stroke:#333,stroke-width:2px
    classDef eventHandlerMethod fill:#ccf,stroke:#333,stroke-width:2px

    Start --> EventHandlerClass[EventHandler Class <br/> (Inherits AssistantEventHandler)]:::eventHandlerClass
    
    EventHandlerClass --> onTextCreatedMethod[on_text_created(text: Text): void]:::eventHandlerMethod
    EventHandlerClass --> onTextDeltaMethod[on_text_delta(delta: TextDelta, snapshot: Text): void]:::eventHandlerMethod
    EventHandlerClass --> onToolCallCreatedMethod[on_tool_call_created(tool_call: ToolCall): void]:::eventHandlerMethod
    EventHandlerClass --> onToolCallDeltaMethod[on_tool_call_delta(delta: ToolCallDelta, snapshot: ToolCall): void]:::eventHandlerMethod

    onTextCreatedMethod --> PrintTextCreated[Print "assistant >" to console]
    
    onTextDeltaMethod --> PrintTextDelta[Print delta.value to console]
    
    onToolCallCreatedMethod --> PrintToolCallType[Print tool_call.type to console]
    
    onToolCallDeltaMethod --> CheckToolType[Check if delta.type is "code_interpreter"]
    
    CheckToolType -- Yes --> CheckCodeInput[Check if delta.code_interpreter.input exists]
    CheckToolType -- No --> End
    
    CheckCodeInput -- Yes --> PrintCodeInput[Print delta.code_interpreter.input to console]
    CheckCodeInput -- No --> CheckCodeOutput[Check if delta.code_interpreter.outputs exists]

    CheckCodeOutput -- Yes --> PrintOutputHeader[Print "output >" to console]
    CheckCodeOutput -- No --> End
    
    PrintOutputHeader --> LoopThroughOutputs[Loop through delta.code_interpreter.outputs]
    
    LoopThroughOutputs --> CheckOutputType[Check if output.type is "logs"]
    
    CheckOutputType -- Yes --> PrintLogs[Print output.logs to console]
    CheckOutputType -- No --> LoopThroughOutputs
     PrintLogs --> LoopThroughOutputs
   
```

**Объяснение зависимостей в диаграмме:**
*   Диаграмма `mermaid` описывает логику класса `EventHandler` и его методов.
*   `EventHandlerClass` - это класс, который наследует от `AssistantEventHandler` и переопределяет его методы для обработки событий.
*   `on_text_created`, `on_text_delta`, `on_tool_call_created`, `on_tool_call_delta` - это методы, которые переопределяют методы родительского класса `AssistantEventHandler` и предназначены для обработки соответствующих событий.
*   Методы выводят информацию в консоль, используя `print`.
*   Метод `on_tool_call_delta` содержит сложную логику для обработки выводов инструмента `code_interpreter`, включая проверку типа вывода и вывод логов.
*   В диаграмме используется `classDef`, чтобы стилизовать блоки.

## <объяснение>
**Импорты:**

*   `from typing_extensions import override`: Импортирует декоратор `override` для явного указания переопределения методов родительского класса.
*   `from openai import AssistantEventHandler, OpenAI`: Импортирует базовый класс `AssistantEventHandler` и класс `OpenAI` из библиотеки `openai`. `AssistantEventHandler` - это абстрактный класс, который определяет интерфейс для обработки событий от ассистента OpenAI, а `OpenAI` - класс, представляющий клиент для работы с API OpenAI.
*   `from openai.types.beta.threads import Text, TextDelta`: Импортирует типы `Text` и `TextDelta`, представляющие текстовые фрагменты и их изменения в потоке ответов от ассистента OpenAI. `Text` представляет полный текстовый фрагмент, а `TextDelta` представляет изменения в тексте.
*   `from openai.types.beta.threads.runs import ToolCall, ToolCallDelta`: Импортирует типы `ToolCall` и `ToolCallDelta`, представляющие вызовы инструментов и их изменения в потоке ответов от ассистента OpenAI. `ToolCall` представляет вызов определенного инструмента, а `ToolCallDelta` представляет изменения в вызове инструмента.

**Классы:**

*   **`EventHandler(AssistantEventHandler)`**:
    *   **Роль**: Этот класс обрабатывает события, происходящие при потоковой передаче ответа от ассистента OpenAI. Он определяет, как должны быть обработаны различные типы событий, такие как создание текста, изменение текста, вызовы инструментов и изменения вызовов инструментов.
    *   **Атрибуты**: Нет явно определенных атрибутов.
    *   **Методы**:
        *   `on_text_created(self, text: Text) -> None`: Метод вызывается при создании нового текстового фрагмента. Он выводит `"\nassistant > "` в консоль.
        *   `on_text_delta(self, delta: TextDelta, snapshot: Text)`: Метод вызывается при получении изменения текстового фрагмента. Он выводит дельту (`delta.value`) в консоль.
        *   `on_tool_call_created(self, tool_call: ToolCall)`: Метод вызывается при создании вызова инструмента. Он выводит тип инструмента `tool_call.type` в консоль.
        *   `on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall)`: Метод вызывается при получении изменения в вызове инструмента. Он обрабатывает изменения, связанные с инструментом `code_interpreter`, выводя его ввод и логи в консоль.
    *   **Взаимодействие**: Этот класс предназначен для использования с SDK OpenAI `stream`, который будет передавать ему события для обработки. Он взаимодействует с консолью, выводя информацию об этих событиях.

**Функции**:

*   В коде явно не определены функции, кроме методов класса `EventHandler`. Все методы являются обработчиками событий и не имеют возвращаемых значений (`-> None`).

**Переменные**:

*   В коде не используется глобальных переменных, кроме тех, что импортируются из других модулей.
*   Переменные `text`, `delta`, `snapshot`, `tool_call` используются как параметры в методах класса `EventHandler`.

**Потенциальные ошибки и области для улучшения:**

1.  **Обработка ошибок**: Код не обрабатывает возможные ошибки при выводе в консоль. В реальном приложении, необходимо добавить обработку исключений.
2.  **Расширяемость**: Если потребуется обрабатывать другие типы инструментов, метод `on_tool_call_delta` нужно будет расширить, что может сделать его сложным. Возможно, стоит рассмотреть использование паттерна `strategy`.
3.  **Логирование**: Вывод в консоль полезен для отладки, но для production-приложения необходимо использовать систему логирования.
4.  **Конфигурация**: Жестко заданный вывод в консоль может быть неудобным. Можно было бы добавить возможность конфигурировать вывод, например, использовать разные потоки вывода.

**Цепочка взаимосвязей с другими частями проекта:**

1.  **`src.ai.openai.model`**: `event_handler.py` является частью модуля `model`, который, вероятно, занимается управлением и взаимодействием с моделями OpenAI.
2.  **`openai` SDK**: Этот код является частью потока работы с  `openai` SDK, который предоставляет функции для взаимодействия с API OpenAI.
3.  **Пользовательский интерфейс**: Вывод в консоль, который производится классом `EventHandler`, вероятно, предназначен для отображения в пользовательском интерфейсе или используется для отладки.

Этот код является важной частью системы для взаимодействия с OpenAI API и обработки потоковых ответов, обеспечивая асинхронный вывод текста и вызовов инструментов, что позволяет динамически отображать результат работы ассистента OpenAI.