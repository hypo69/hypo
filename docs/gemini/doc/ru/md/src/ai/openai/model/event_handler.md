# Модуль `hypotez/src/ai/openai/model/event_handler.py`

## Обзор

Этот модуль предоставляет класс `EventHandler`, который обрабатывает события, генерируемые OpenAI API, в потоковом режиме. Он расширяет базовый класс `AssistantEventHandler` и переопределяет методы для обработки различных событий, таких как создание текста, изменение текста, создание запроса к инструменту и изменение запроса к инструменту.

## Оглавление

- [Модуль `hypotez/src/ai/openai/model/event_handler.py`](#модуль-hypotezsrc-ai-openai-model-event-handler-py)
- [Обзор](#обзор)
- [Класс `EventHandler`](#класс-event-handler)
    - [`on_text_created`](#on-text-created)
    - [`on_text_delta`](#on-text-delta)
    - [`on_tool_call_created`](#on-tool-call-created)
    - [`on_tool_call_delta`](#on-tool-call-delta)


## Класс `EventHandler`

### Описание

Класс `EventHandler` предназначен для обработки событий, возвращаемых OpenAI API в потоковом режиме. Он переопределяет методы базового класса `AssistantEventHandler`, позволяя настраивать реакцию на различные типы событий.

### Методы

#### `on_text_created`

```python
  @override
  def on_text_created(self, text: Text) -> None:
    print(f"\\nassistant > ", end="", flush=True)
```

**Описание**: Метод `on_text_created` вызывается при создании нового фрагмента текста. Выводит в консоль префикс "assistant > ".

**Параметры**:

- `text` (Text): Объект `Text`, содержащий новый фрагмент текста.

**Возвращает**: `None`


#### `on_text_delta`

```python
  @override
  def on_text_delta(self, delta: TextDelta, snapshot: Text):
    print(delta.value, end="", flush=True)
```

**Описание**: Метод `on_text_delta` вызывается при изменении существующего фрагмента текста. Выводит в консоль изменение.

**Параметры**:

- `delta` (TextDelta): Объект `TextDelta`, содержащий изменения в тексте.
- `snapshot` (Text): Объект `Text`, представляющий текущую версию текста.

**Возвращает**: `None`


#### `on_tool_call_created`

```python
  @override
  def on_tool_call_created(self, tool_call: ToolCall):
    print(f"\\nassistant > {tool_call.type}\\n", flush=True)
```

**Описание**: Метод `on_tool_call_created` вызывается при создании запроса к инструменту. Выводит в консоль тип инструмента.

**Параметры**:

- `tool_call` (ToolCall): Объект `ToolCall`, описывающий запрос к инструменту.

**Возвращает**: `None`


#### `on_tool_call_delta`

```python
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
```

**Описание**: Метод `on_tool_call_delta` вызывается при изменении запроса к инструменту. Обрабатывает отдельные типы выводов инструмента, в том числе входные данные и логи.

**Параметры**:

- `delta` (ToolCallDelta): Объект `ToolCallDelta`, описывающий изменения в запросе к инструменту.
- `snapshot` (ToolCall): Объект `ToolCall`, представляющий текущую версию запроса к инструменту.

**Возвращает**: `None`


**Примечание:** Данные методы предполагают использование типов из библиотеки `openai`.