# Модуль `event_handler`

## Обзор

Модуль `event_handler` предназначен для обработки событий, генерируемых ассистентом OpenAI при работе с потоками (stream). Он содержит класс `EventHandler`, который наследует `AssistantEventHandler` из библиотеки `openai` и переопределяет методы для обработки текстовых и инструментальных вызовов.

## Содержание

- [Классы](#Классы)
  - [`EventHandler`](#EventHandler)
- [Импорт](#Импорт)

## Импорт

Модуль импортирует следующие классы и функции из библиотек:

- `override` из `typing_extensions`
- `AssistantEventHandler`, `OpenAI` из `openai`
- `Text`, `TextDelta` из `openai.types.beta.threads`
- `ToolCall`, `ToolCallDelta` из `openai.types.beta.threads.runs`

## Классы

### `EventHandler`

**Описание**: Класс `EventHandler` наследует `AssistantEventHandler` и переопределяет его методы для обработки событий от ассистента OpenAI.

**Методы**:

- `on_text_created(self, text: Text) -> None`
- `on_text_delta(self, delta: TextDelta, snapshot: Text) -> None`
- `on_tool_call_created(self, tool_call: ToolCall) -> None`
- `on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall) -> None`

#### `on_text_created`

**Описание**: Метод вызывается при создании нового текстового объекта в потоке.

**Параметры**:
- `text` (Text): Объект типа Text, представляющий созданный текст.

**Возвращает**:
- `None`: Метод ничего не возвращает.

#### `on_text_delta`

**Описание**: Метод вызывается при изменении текстового объекта в потоке.

**Параметры**:
- `delta` (TextDelta): Объект типа TextDelta, представляющий изменения в тексте.
- `snapshot` (Text): Объект типа Text, представляющий текущий снимок текста.

**Возвращает**:
- `None`: Метод ничего не возвращает.

#### `on_tool_call_created`

**Описание**: Метод вызывается при создании нового инструментального вызова в потоке.

**Параметры**:
- `tool_call` (ToolCall): Объект типа ToolCall, представляющий созданный инструментальный вызов.

**Возвращает**:
- `None`: Метод ничего не возвращает.

#### `on_tool_call_delta`

**Описание**: Метод вызывается при изменении инструментального вызова в потоке.

**Параметры**:
- `delta` (ToolCallDelta): Объект типа ToolCallDelta, представляющий изменения в инструментальном вызове.
- `snapshot` (ToolCall): Объект типа ToolCall, представляющий текущий снимок инструментального вызова.

**Возвращает**:
- `None`: Метод ничего не возвращает.

**Логика**:
- Проверяет тип инструментального вызова. Если тип `code_interpreter`, печатает входные и выходные данные, если они доступны.