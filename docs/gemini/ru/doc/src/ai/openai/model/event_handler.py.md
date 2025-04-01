# Модуль `event_handler`

## Обзор

Модуль `event_handler` предназначен для обработки событий, связанных с ассистентом OpenAI. Он определяет класс `EventHandler`, который переопределяет методы для обработки различных типов событий, таких как создание текста, изменение текста, создание вызова инструмента и изменение вызова инструмента. Модуль использует библиотеку `openai` для взаимодействия с API OpenAI.

## Подробнее

Этот модуль предоставляет механизм для обработки потока событий, генерируемых ассистентом OpenAI. Класс `EventHandler` определяет, как реагировать на различные типы событий, такие как создание и изменение текста, а также создание и изменение вызовов инструментов. Это позволяет разработчикам настраивать поведение приложения в зависимости от событий, происходящих в процессе взаимодействия с ассистентом OpenAI.

## Классы

### `EventHandler`

**Описание**: Класс `EventHandler` наследует `AssistantEventHandler` из библиотеки `openai` и переопределяет его методы для обработки различных событий, связанных с ассистентом OpenAI.

**Наследует**:
- `AssistantEventHandler`

**Методы**:
- `on_text_created`: Обрабатывает событие создания текста.
- `on_text_delta`: Обрабатывает событие изменения текста.
- `on_tool_call_created`: Обрабатывает событие создания вызова инструмента.
- `on_tool_call_delta`: Обрабатывает событие изменения вызова инструмента.

#### `on_text_created`

```python
@override
def on_text_created(self, text: Text) -> None:
    """
    Обрабатывает событие создания текста.

    Args:
        text (Text): Объект `Text`, представляющий созданный текст.

    Returns:
        None

    Raises:
        None
    """
    ...
```

**Назначение**:
Метод `on_text_created` вызывается при создании нового текстового блока ассистентом. Он выводит в консоль символ `\nassistant >` без перевода строки, подготавливая место для вывода текста ассистента.

**Параметры**:
- `text` (Text): Объект `Text`, содержащий информацию о созданном текстовом блоке.

**Возвращает**:
- `None`

**Как работает функция**:
1. Выводит в консоль строку `\nassistant >` без перевода строки, используя `print(f"\nassistant > ", end="", flush=True)`. Это нужно для того, чтобы последующий текст ассистента выводился на той же строке.

**Примеры**:
```python
event_handler = EventHandler()
text = Text(id='text_123', text='Привет, мир!', created_at=1678886400, thread_id='thread_123', run_id='run_123', type='text')
event_handler.on_text_created(text)
```

#### `on_text_delta`

```python
@override
def on_text_delta(self, delta: TextDelta, snapshot: Text):
    """
    Обрабатывает событие изменения текста.

    Args:
        delta (TextDelta): Объект `TextDelta`, представляющий изменение текста.
        snapshot (Text): Объект `Text`, представляющий текущее состояние текста.

    Returns:
        None

    Raises:
        None
    """
    ...
```

**Назначение**:
Метод `on_text_delta` вызывается при изменении текстового блока ассистентом. Он выводит в консоль добавленное значение (`delta.value`) без перевода строки, позволяя постепенно отображать текст ассистента.

**Параметры**:
- `delta` (TextDelta): Объект `TextDelta`, содержащий информацию об изменении текста.
- `snapshot` (Text): Объект `Text`, содержащий текущий "снимок" текстового блока.

**Возвращает**:
- `None`

**Как работает функция**:
1. Выводит в консоль значение `delta.value` без перевода строки, используя `print(delta.value, end="", flush=True)`. Это позволяет отображать текст ассистента по мере его генерации.

**Примеры**:
```python
event_handler = EventHandler()
delta = TextDelta(value='!', created_at=1678886401, thread_id='thread_123', run_id='run_123', type='text')
snapshot = Text(id='text_123', text='Привет, мир', created_at=1678886400, thread_id='thread_123', run_id='run_123', type='text')
event_handler.on_text_delta(delta, snapshot)
```

#### `on_tool_call_created`

```python
@override
def on_tool_call_created(self, tool_call: ToolCall):
    """
    Обрабатывает событие создания вызова инструмента.

    Args:
        tool_call (ToolCall): Объект `ToolCall`, представляющий вызов инструмента.

    Returns:
        None

    Raises:
        None
    """
    ...
```

**Назначение**:
Метод `on_tool_call_created` вызывается при создании нового вызова инструмента ассистентом. Он выводит в консоль тип вызова инструмента (`tool_call.type`) с префиксом `\nassistant >` и переводом строки, уведомляя о начале использования инструмента.

**Параметры**:
- `tool_call` (ToolCall): Объект `ToolCall`, содержащий информацию о вызове инструмента.

**Возвращает**:
- `None`

**Как работает функция**:
1. Выводит в консоль строку `\nassistant > {tool_call.type}\n`, используя `print(f"\nassistant > {tool_call.type}\n", flush=True)`. Это уведомляет о типе используемого инструмента.

**Примеры**:
```python
event_handler = EventHandler()
tool_call = ToolCall(id='tool_123', type='code_interpreter', function=None, code_interpreter=None, thread_id='thread_123', run_id='run_123')
event_handler.on_tool_call_created(tool_call)
```

#### `on_tool_call_delta`

```python
@override
def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
    """
    Обрабатывает событие изменения вызова инструмента.

    Args:
        delta (ToolCallDelta): Объект `ToolCallDelta`, представляющий изменение вызова инструмента.
        snapshot (ToolCall): Объект `ToolCall`, представляющий текущее состояние вызова инструмента.

    Returns:
        None

    Raises:
        None
    """
    if delta.type == "code_interpreter" and delta.code_interpreter:
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)
```

**Назначение**:
Метод `on_tool_call_delta` вызывается при изменении вызова инструмента ассистентом. Он обрабатывает изменения, специфичные для инструмента `code_interpreter`, выводя в консоль ввод и вывод (логи) интерпретатора кода.

**Параметры**:
- `delta` (ToolCallDelta): Объект `ToolCallDelta`, содержащий информацию об изменении вызова инструмента.
- `snapshot` (ToolCall): Объект `ToolCall`, содержащий текущий "снимок" вызова инструмента.

**Возвращает**:
- `None`

**Как работает функция**:
1. Проверяет, является ли изменение типа `code_interpreter` и существует ли `delta.code_interpreter`.
2. Если `delta.code_interpreter.input` существует, выводит его в консоль без перевода строки.
3. Если `delta.code_interpreter.outputs` существует, выводит в консоль префикс `\n\noutput >` с переводом строки, а затем перебирает все элементы в `delta.code_interpreter.outputs`.
4. Для каждого элемента в `delta.code_interpreter.outputs` проверяет, является ли его тип `logs`.
5. Если тип элемента `logs`, выводит его значение в консоль с переводом строки.

**Примеры**:
```python
event_handler = EventHandler()
delta = ToolCallDelta(id='tool_123', type='code_interpreter', code_interpreter=ToolCallDelta.CodeInterpreter(input='print("Hello")', outputs=None), function=None)
snapshot = ToolCall(id='tool_123', type='code_interpreter', function=None, code_interpreter=None, thread_id='thread_123', run_id='run_123')
event_handler.on_tool_call_delta(delta, snapshot)
```
```python
event_handler = EventHandler()
delta = ToolCallDelta(id='tool_123', type='code_interpreter', code_interpreter=ToolCallDelta.CodeInterpreter(input=None, outputs=[ToolCallDelta.CodeInterpreter.Output(type='logs', logs='Hello\nWorld')]), function=None)
snapshot = ToolCall(id='tool_123', type='code_interpreter', function=None, code_interpreter=None, thread_id='thread_123', run_id='run_123')
event_handler.on_tool_call_delta(delta, snapshot)