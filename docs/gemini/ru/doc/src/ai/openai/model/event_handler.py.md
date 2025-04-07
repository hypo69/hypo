# Модуль `event_handler`

## Обзор

Модуль `event_handler.py` предназначен для обработки событий, генерируемых ассистентом OpenAI, и предоставляет класс `EventHandler`, который определяет, как обрабатывать эти события в потоке ответов. Этот модуль использует библиотеку OpenAI для взаимодействия с API ассистента и обработки текстовых и инструментальных вызовов.

## Подробней

Этот модуль важен для реализации асинхронного взаимодействия с ассистентом OpenAI, позволяя реагировать на различные события в реальном времени. Он позволяет обрабатывать текстовые ответы, вызовы инструментов и другие события, генерируемые ассистентом.

## Классы

### `EventHandler`

**Описание**: Класс `EventHandler` наследует `AssistantEventHandler` из библиотеки OpenAI и переопределяет методы для обработки различных событий, генерируемых ассистентом.

**Принцип работы**:
Класс `EventHandler` предназначен для настройки обработки событий, генерируемых ассистентом OpenAI. Он переопределяет методы `on_text_created`, `on_text_delta`, `on_tool_call_created` и `on_tool_call_delta`, чтобы определить, как реагировать на создание текста, изменение текста и вызовы инструментов.

**Методы**:
- `on_text_created(self, text: Text) -> None`: Вызывается при создании нового текстового блока.
- `on_text_delta(self, delta: TextDelta, snapshot: Text) -> None`: Вызывается при изменении существующего текстового блока.
- `on_tool_call_created(self, tool_call: ToolCall) -> None`: Вызывается при создании нового вызова инструмента.
- `on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall) -> None`: Вызывается при изменении существующего вызова инструмента.

### `on_text_created`
```python
def on_text_created(self, text: Text) -> None:
    """
    Вызывается при создании нового текстового блока.

    Args:
        text (Text): Объект `Text`, содержащий информацию о созданном текстовом блоке.

    Returns:
        None

    """
    ...
```

**Параметры**:
- `text` (Text): Объект `Text`, содержащий информацию о созданном текстовом блоке.

**Возвращает**:
- `None`

**Как работает функция**:
1. Функция `on_text_created` вызывается при создании нового текстового блока ассистентом.
2. Она выводит в консоль символ ">" для обозначения начала ответа ассистента.

```
A
|
Вывод ">" в консоль
```

**Примеры**:

```python
event_handler = EventHandler()
text_object = Text(id='text_1', type='text', value='Hello')
event_handler.on_text_created(text_object)  # Выведет ">" в консоль
```

### `on_text_delta`
```python
def on_text_delta(self, delta: TextDelta, snapshot: Text):
    """
    Вызывается при изменении существующего текстового блока.

    Args:
        delta (TextDelta): Объект `TextDelta`, содержащий изменения в текстовом блоке.
        snapshot (Text): Объект `Text`, представляющий текущее состояние текстового блока.

    Returns:
        None

    """
    ...
```

**Параметры**:
- `delta` (TextDelta): Объект `TextDelta`, содержащий изменения в текстовом блоке.
- `snapshot` (Text): Объект `Text`, представляющий текущее состояние текстового блока.

**Возвращает**:
- `None`

**Как работает функция**:
1. Функция `on_text_delta` вызывается при изменении текстового блока ассистентом.
2. Она выводит в консоль значение изменения (`delta.value`).

```
A
|
Вывод delta.value в консоль
```

**Примеры**:

```python
event_handler = EventHandler()
delta_object = TextDelta(id='delta_1', type='text_delta', value=' world!')
snapshot_object = Text(id='text_1', type='text', value='Hello')
event_handler.on_text_delta(delta_object, snapshot_object)  # Выведет " world!" в консоль
```

### `on_tool_call_created`
```python
def on_tool_call_created(self, tool_call: ToolCall):
    """
    Вызывается при создании нового вызова инструмента.

    Args:
        tool_call (ToolCall): Объект `ToolCall`, содержащий информацию о вызове инструмента.

    Returns:
        None

    """
    ...
```

**Параметры**:
- `tool_call` (ToolCall): Объект `ToolCall`, содержащий информацию о вызове инструмента.

**Возвращает**:
- `None`

**Как работает функция**:
1. Функция `on_tool_call_created` вызывается при создании вызова инструмента ассистентом.
2. Она выводит в консоль тип вызова инструмента.

```
A
|
Вывод типа вызова инструмента в консоль
```

**Примеры**:

```python
event_handler = EventHandler()
tool_call_object = ToolCall(id='tool_call_1', type='code_interpreter', function=None)
event_handler.on_tool_call_created(tool_call_object)  # Выведет тип инструмента в консоль
```

### `on_tool_call_delta`
```python
def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
    """
    Вызывается при изменении существующего вызова инструмента.

    Args:
        delta (ToolCallDelta): Объект `ToolCallDelta`, содержащий изменения в вызове инструмента.
        snapshot (ToolCall): Объект `ToolCall`, представляющий текущее состояние вызова инструмента.

    Returns:
        None

    """
    ...
```

**Параметры**:
- `delta` (ToolCallDelta): Объект `ToolCallDelta`, содержащий изменения в вызове инструмента.
- `snapshot` (ToolCall): Объект `ToolCall`, представляющий текущее состояние вызова инструмента.

**Возвращает**:
- `None`

**Как работает функция**:
1. Функция `on_tool_call_delta` вызывается при изменении вызова инструмента ассистентом.
2. Если тип инструмента - `code_interpreter`, она выводит входные и выходные данные интерпретатора кода в консоль.

```
A
|
Проверка типа инструмента == code_interpreter
|
B (Если да)
|
Вывод входных и выходных данных интерпретатора кода в консоль
```

**Примеры**:

```python
event_handler = EventHandler()
delta_object = ToolCallDelta(id='delta_1', type='code_interpreter', code_interpreter=ToolCallDelta.CodeInterpreter(input='print("Hello")', outputs=[ToolCallDelta.CodeInterpreter.Output(type='logs', logs='Hello')]))
snapshot_object = ToolCall(id='tool_call_1', type='code_interpreter', function=None)
event_handler.on_tool_call_delta(delta_object, snapshot_object)  # Выведет входные и выходные данные code_interpreter в консоль
```