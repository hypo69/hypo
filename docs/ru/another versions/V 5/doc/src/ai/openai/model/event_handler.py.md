# Модуль `event_handler`

## Обзор

Модуль `event_handler` предназначен для обработки событий, связанных с ассистентом OpenAI. Он содержит класс `EventHandler`, который определяет, как обрабатывать события в потоке ответов, включая создание текста, изменение текста и вызовы инструментов.

## Подробней

Этот модуль предоставляет функциональность для работы с событиями, генерируемыми OpenAI Assistant API. Он использует класс `AssistantEventHandler` из библиотеки `openai` для обработки различных типов событий, таких как создание и изменение текста, а также вызовы инструментов. Класс `EventHandler` переопределяет методы `on_text_created`, `on_text_delta`, `on_tool_call_created` и `on_tool_call_delta` для обработки этих событий и вывода информации в консоль. Модуль помогает визуализировать взаимодействие с ассистентом, отображая текст, запросы инструментов и результаты их выполнения.

## Классы

### `EventHandler`

**Описание**: Класс `EventHandler` является обработчиком событий ассистента OpenAI. Он переопределяет методы класса `AssistantEventHandler` для обработки различных типов событий и вывода информации в консоль.

**Как работает класс**:

1.  При создании экземпляра класса `EventHandler` происходит инициализация обработчика событий.
2.  Метод `on_text_created` вызывается при создании текстового сообщения от ассистента и выводит в консоль префикс `assistant >`.
3.  Метод `on_text_delta` вызывается при изменении текстового сообщения от ассистента и выводит в консоль добавленные фрагменты текста.
4.  Метод `on_tool_call_created` вызывается при создании запроса на вызов инструмента и выводит в консоль тип инструмента.
5.  Метод `on_tool_call_delta` вызывается при изменении запроса на вызов инструмента и выводит в консоль детали изменения, такие как ввод и вывод code interpreter.

**Методы**:

*   `on_text_created`: Обрабатывает событие создания текста.
*   `on_text_delta`: Обрабатывает событие изменения текста.
*   `on_tool_call_created`: Обрабатывает событие создания вызова инструмента.
*   `on_tool_call_delta`: Обрабатывает событие изменения вызова инструмента.

### `EventHandler.on_text_created`

```python
  @override
  def on_text_created(self, text: Text) -> None:
    print(f"\nassistant > ", end="", flush=True)
```

**Описание**: Обрабатывает событие создания текста.

**Как работает функция**:

При вызове этого метода, он выводит в консоль строку `\nassistant > ` без перевода строки и с немедленной очисткой буфера вывода.

**Параметры**:

*   `text` (Text): Объект `Text`, содержащий информацию о созданном тексте.

**Возвращает**:

*   `None`

**Примеры**:

```python
event_handler = EventHandler()
# Создаем объект Text для имитации события
text_object = Text(id='text-123', value='Hello', created_at=1678848000, thread_id='thread-123', run_id='run-123', type='message')
event_handler.on_text_created(text_object)
```

### `EventHandler.on_text_delta`

```python
  @override
  def on_text_delta(self, delta: TextDelta, snapshot: Text):
    print(delta.value, end="", flush=True)
```

**Описание**: Обрабатывает событие изменения текста.

**Как работает функция**:

При вызове этого метода, он выводит в консоль значение `delta.value` без перевода строки и с немедленной очисткой буфера вывода.

**Параметры**:

*   `delta` (TextDelta): Объект `TextDelta`, содержащий информацию об изменении текста.
*   `snapshot` (Text): Объект `Text`, представляющий собой текущий снимок текста.

**Возвращает**:

*   `None`

**Примеры**:

```python
event_handler = EventHandler()
# Создаем объекты TextDelta и Text для имитации события
delta_object = TextDelta(id='text_delta-123', value=' world', created_at=1678848001, thread_id='thread-123', run_id='run-123', type='message')
snapshot_object = Text(id='text-123', value='Hello', created_at=1678848000, thread_id='thread-123', run_id='run-123', type='message')
event_handler.on_text_delta(delta_object, snapshot_object)
```

### `EventHandler.on_tool_call_created`

```python
  @override
  def on_tool_call_created(self, tool_call: ToolCall):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
```

**Описание**: Обрабатывает событие создания вызова инструмента.

**Как работает функция**:

При вызове этого метода, он выводит в консоль строку, содержащую тип инструмента (`tool_call.type`), с добавлением символов перевода строки в начале и в конце, и с немедленной очисткой буфера вывода.

**Параметры**:

*   `tool_call` (ToolCall): Объект `ToolCall`, содержащий информацию о вызове инструмента.

**Возвращает**:

*   `None`

**Примеры**:

```python
event_handler = EventHandler()
# Создаем объект ToolCall для имитации события
tool_call_object = ToolCall(id='tool_call-123', type='code_interpreter', code_interpreter=None, function=None)
event_handler.on_tool_call_created(tool_call_object)
```

### `EventHandler.on_tool_call_delta`

```python
  @override
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

**Описание**: Обрабатывает событие изменения вызова инструмента.

**Как работает функция**:

При вызове этого метода, он проверяет, является ли тип инструмента `code_interpreter`. Если да, и если в `delta.code_interpreter` есть ввод, он выводит его в консоль без перевода строки и с немедленной очисткой буфера вывода. Если в `delta.code_interpreter` есть вывод, он выводит в консоль строку `\n\noutput >` с немедленной очисткой буфера вывода. Затем для каждого элемента в `delta.code_interpreter.outputs` он проверяет, является ли тип вывода `logs`, и если да, он выводит логи в консоль с символом перевода строки в начале и с немедленной очисткой буфера вывода.

**Параметры**:

*   `delta` (ToolCallDelta): Объект `ToolCallDelta`, содержащий информацию об изменении вызова инструмента.
*   `snapshot` (ToolCall): Объект `ToolCall`, представляющий собой текущий снимок вызова инструмента.

**Возвращает**:

*   `None`

**Примеры**:

```python
event_handler = EventHandler()
# Создаем объекты ToolCallDelta и ToolCall для имитации события
delta_object = ToolCallDelta(id='tool_call_delta-123', type='code_interpreter', code_interpreter=ToolCallDelta.CodeInterpreter(input='print("Hello")', outputs=None), function=None)
snapshot_object = ToolCall(id='tool_call-123', type='code_interpreter', code_interpreter=None, function=None)
event_handler.on_tool_call_delta(delta_object, snapshot_object)