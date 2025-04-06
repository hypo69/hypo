# Модуль для обработки событий Assistant API от OpenAI

## Обзор

Модуль `event_handler.py` предоставляет класс `EventHandler`, который используется для обработки событий, генерируемых ассистентом OpenAI. Он определяет, как должны обрабатываться различные события, такие как создание и обновление текста, а также вызовы инструментов (tool calls). Этот модуль позволяет организовать взаимодействие с API OpenAI Assistant, обрабатывая ответы в реальном времени.

## Подробнее

Этот модуль содержит класс `EventHandler`, который наследует `AssistantEventHandler` из библиотеки `openai`. Он переопределяет несколько методов, чтобы определить, как реагировать на различные типы событий, генерируемые ассистентом OpenAI. В частности, он обрабатывает события создания и обновления текста, а также вызовы инструментов, отображая соответствующую информацию в консоли.

## Классы

### `EventHandler`

**Описание**: Класс `EventHandler` предназначен для обработки событий, генерируемых ассистентом OpenAI. Он наследует класс `AssistantEventHandler` и переопределяет его методы для обработки различных типов событий.

**Наследует**:

- `AssistantEventHandler` из библиотеки `openai`.

**Методы**:

- `on_text_created(self, text: Text) -> None`: Обработчик события создания текста.
- `on_text_delta(self, delta: TextDelta, snapshot: Text)`: Обработчик события изменения текста.
- `on_tool_call_created(self, tool_call: ToolCall)`: Обработчик события создания вызова инструмента.
- `on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall)`: Обработчик события изменения вызова инструмента.

### `EventHandler.on_text_created`

```python
def on_text_created(self, text: Text) -> None:
    """
    Обработчик события создания текста.

    Args:
        text (Text): Объект `Text`, представляющий созданный текст.

    Returns:
        None

    """
    ...
```

**Назначение**: Этот метод вызывается при создании нового текстового блока ассистентом.

**Параметры**:

- `text` (Text): Объект, содержащий информацию о созданном тексте.

**Возвращает**:

- `None`

**Как работает функция**:

1.  Выводит в консоль строку "assistant > ".

ASCII flowchart:

```
A
↓
B
```

Где:

-   `A`: Получение события о создании текста.
-   `B`: Вывод в консоль строки "assistant > ".

**Примеры**:

```python
event_handler = EventHandler()
text = Text(id='text_id', value='Привет, мир!', created_at=1678886400, thread_id='thread_id', run_id='run_id', object='text')
event_handler.on_text_created(text)  # Выводит "\nassistant > " в консоль.
```

### `EventHandler.on_text_delta`

```python
def on_text_delta(self, delta: TextDelta, snapshot: Text):
    """
    Обработчик события изменения текста.

    Args:
        delta (TextDelta): Объект `TextDelta`, содержащий информацию об изменении текста.
        snapshot (Text): Объект `Text`, представляющий текущее состояние текста.

    Returns:
        None

    """
    ...
```

**Назначение**: Этот метод вызывается при изменении существующего текстового блока ассистентом.

**Параметры**:

- `delta` (TextDelta): Объект, содержащий информацию об изменении текста.
- `snapshot` (Text): Объект, представляющий текущее состояние текста.

**Возвращает**:

- `None`

**Как работает функция**:

1.  Выводит в консоль значение `delta.value`.

ASCII flowchart:

```
A
↓
B
```

Где:

-   `A`: Получение события об изменении текста.
-   `B`: Вывод в консоль значения `delta.value`.

**Примеры**:

```python
event_handler = EventHandler()
delta = TextDelta(value=' Дополнение', created_at=1678886401, thread_id='thread_id', run_id='run_id', object='text_delta', type='text_delta')
snapshot = Text(id='text_id', value='Привет, мир!', created_at=1678886400, thread_id='thread_id', run_id='run_id', object='text')
event_handler.on_text_delta(delta, snapshot)  # Выводит " Дополнение" в консоль.
```

### `EventHandler.on_tool_call_created`

```python
def on_tool_call_created(self, tool_call: ToolCall):
    """
    Обработчик события создания вызова инструмента.

    Args:
        tool_call (ToolCall): Объект `ToolCall`, представляющий вызов инструмента.

    Returns:
        None

    """
    ...
```

**Назначение**: Этот метод вызывается при создании нового вызова инструмента ассистентом.

**Параметры**:

- `tool_call` (ToolCall): Объект, содержащий информацию о вызове инструмента.

**Возвращает**:

- `None`

**Как работает функция**:

1.  Выводит в консоль тип вызова инструмента.

ASCII flowchart:

```
A
↓
B
```

Где:

-   `A`: Получение события о создании вызова инструмента.
-   `B`: Вывод в консоль типа вызова инструмента.

**Примеры**:

```python
event_handler = EventHandler()
tool_call = ToolCall(id='tool_call_id', type='code_interpreter', code_interpreter=None, function=None, object='tool_call')
event_handler.on_tool_call_created(tool_call)  # Выводит "\nassistant > code_interpreter\n" в консоль.
```

### `EventHandler.on_tool_call_delta`

```python
def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
    """
    Обработчик события изменения вызова инструмента.

    Args:
        delta (ToolCallDelta): Объект `ToolCallDelta`, содержащий информацию об изменении вызова инструмента.
        snapshot (ToolCall): Объект `ToolCall`, представляющий текущее состояние вызова инструмента.

    Returns:
        None

    """
    ...
```

**Назначение**: Этот метод вызывается при изменении существующего вызова инструмента ассистентом.

**Параметры**:

- `delta` (ToolCallDelta): Объект, содержащий информацию об изменении вызова инструмента.
- `snapshot` (ToolCall): Объект, представляющий текущее состояние вызова инструмента.

**Возвращает**:

- `None`

**Как работает функция**:

1.  Проверяет, является ли тип вызова инструмента `code_interpreter`.
2.  Если да, выводит в консоль ввод и вывод интерпретатора кода.

ASCII flowchart:

```
A
↓
B
↓
C
```

Где:

-   `A`: Получение события об изменении вызова инструмента.
-   `B`: Проверка типа вызова инструмента (`code_interpreter`).
-   `C`: Вывод в консоль ввода и вывода интерпретатора кода (если тип соответствует).

**Примеры**:

```python
event_handler = EventHandler()
delta = ToolCallDelta(type='code_interpreter', code_interpreter=ToolCallDelta.CodeInterpreter(input='print("Hello")', outputs=None), function=None)
snapshot = ToolCall(id='tool_call_id', type='code_interpreter', code_interpreter=None, function=None, object='tool_call')
event_handler.on_tool_call_delta(delta, snapshot)  # Выводит ввод интерпретатора кода в консоль.
```
```python
event_handler = EventHandler()
delta = ToolCallDelta(type='code_interpreter', code_interpreter=ToolCallDelta.CodeInterpreter(input=None, outputs=[{"type": "logs", "logs":"[LOGS] Hello from Python!"}]), function=None)
snapshot = ToolCall(id='tool_call_id', type='code_interpreter', code_interpreter=None, function=None, object='tool_call')
event_handler.on_tool_call_delta(delta, snapshot)  # Выводит вывод интерпретатора кода в консоль.
```