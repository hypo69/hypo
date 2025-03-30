# Модуль `event_handler`

## Обзор

Модуль `event_handler` предназначен для обработки событий, генерируемых ассистентом OpenAI. Он определяет, как должны обрабатываться различные типы событий, такие как создание текста, изменение текста, вызовы инструментов и т.д. Этот модуль позволяет настроить взаимодействие с ассистентом OpenAI и реагировать на его действия в реальном времени.

## Подробней

Модуль содержит класс `EventHandler`, который наследуется от `AssistantEventHandler` из библиотеки `openai`. `EventHandler` переопределяет методы для обработки различных событий, предоставляемых ассистентом. Это позволяет настроить поведение приложения в зависимости от действий ассистента, например, отображать текст, обрабатывать вызовы инструментов и логировать результаты.

## Классы

### `EventHandler`

**Описание**:
Класс `EventHandler` предназначен для обработки событий, генерируемых ассистентом OpenAI. Он содержит методы, которые переопределяют поведение по умолчанию для обработки различных типов событий.

**Методы**:
- `on_text_created`: Обрабатывает событие создания текста.
- `on_text_delta`: Обрабатывает событие изменения текста.
- `on_tool_call_created`: Обрабатывает событие создания вызова инструмента.
- `on_tool_call_delta`: Обрабатывает событие изменения вызова инструмента.

#### `on_text_created`

```python
def on_text_created(self, text: Text) -> None:
    """
    Args:
        text (Text): Объект `Text`, представляющий созданный текст.

    Returns:
        None

    Raises:
        No exceptions.

    Example:
        >>> event_handler = EventHandler()
        >>> from openai.types.beta.threads import Text
        >>> text = Text(id='text_id', value='Пример текста', created_at=12345, thread_id='thread_id', run_id='run_id', type='text')
        >>> event_handler.on_text_created(text)
        
    """
```

**Описание**:
Метод вызывается при создании текстового блока ассистентом.

**Параметры**:
- `text` (Text): Объект `Text`, представляющий созданный текст.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.

#### `on_text_delta`

```python
def on_text_delta(self, delta: TextDelta, snapshot: Text):
    """
    Args:
        delta (TextDelta): Объект `TextDelta`, представляющий изменение текста.
        snapshot (Text): Объект `Text`, представляющий текущий снимок текста.

    Returns:
        None

    Raises:
        No exceptions.
        
    Example:
        >>> event_handler = EventHandler()
        >>> from openai.types.beta.threads import TextDelta, Text
        >>> delta = TextDelta(value='изменение', type='text', text=None)
        >>> snapshot = Text(id='text_id', value='Пример текста', created_at=12345, thread_id='thread_id', run_id='run_id', type='text')
        >>> event_handler.on_text_delta(delta, snapshot)
        
    """
```

**Описание**:
Метод вызывается при изменении текстового блока ассистентом.

**Параметры**:
- `delta` (TextDelta): Объект `TextDelta`, представляющий изменение текста.
- `snapshot` (Text): Объект `Text`, представляющий текущий снимок текста.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.

#### `on_tool_call_created`

```python
def on_tool_call_created(self, tool_call: ToolCall):
    """
    Args:
        tool_call (ToolCall): Объект `ToolCall`, представляющий вызов инструмента.

    Returns:
        None

    Raises:
        No exceptions.

    Example:
        >>> event_handler = EventHandler()
        >>> from openai.types.beta.threads.runs import ToolCall, CodeInterpreter
        >>> code_interpreter = CodeInterpreter(input="print('Hello')", outputs=[])
        >>> tool_call = ToolCall(id='tool_call_id', type='code_interpreter', code_interpreter=code_interpreter, function=None)
        >>> event_handler.on_tool_call_created(tool_call)
        
    """
```

**Описание**:
Метод вызывается при создании вызова инструмента ассистентом.

**Параметры**:
- `tool_call` (ToolCall): Объект `ToolCall`, представляющий вызов инструмента.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.

#### `on_tool_call_delta`

```python
def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
    """
    Args:
        delta (ToolCallDelta): Объект `ToolCallDelta`, представляющий изменение вызова инструмента.
        snapshot (ToolCall): Объект `ToolCall`, представляющий текущий снимок вызова инструмента.

    Returns:
        None

    Raises:
        No exceptions.

    Example:
        >>> event_handler = EventHandler()
        >>> from openai.types.beta.threads.runs import ToolCallDelta, ToolCall, CodeInterpreter, CodeInterpreterDelta
        >>> code_interpreter_delta = CodeInterpreterDelta(input="print('World')", outputs=[])
        >>> delta = ToolCallDelta(id='tool_call_id', type='code_interpreter', code_interpreter=code_interpreter_delta, function=None)
        >>> code_interpreter = CodeInterpreter(input="print('Hello')", outputs=[])
        >>> tool_call = ToolCall(id='tool_call_id', type='code_interpreter', code_interpreter=code_interpreter, function=None)
        >>> event_handler.on_tool_call_delta(delta, tool_call)
    """
```

**Описание**:
Метод вызывается при изменении вызова инструмента ассистентом.

**Параметры**:
- `delta` (ToolCallDelta): Объект `ToolCallDelta`, представляющий изменение вызова инструмента.
- `snapshot` (ToolCall): Объект `ToolCall`, представляющий текущий снимок вызова инструмента.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.