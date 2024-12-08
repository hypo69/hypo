# Модуль hypotez/src/ai/openai/model/event_handler.py

## Обзор

Данный модуль предоставляет класс `EventHandler` для обработки событий, генерируемых моделью OpenAI, во время выполнения диалога. Он позволяет получать и отображать текст, изменения текста, вызовы инструментов и, в частности, результаты работы инструмента "code interpreter".

## Классы

### `EventHandler`

**Описание**: Класс `EventHandler`, наследуемый от `AssistantEventHandler`, обрабатывает события, возвращаемые API OpenAI во время диалога с помощником.

**Методы**:

- **`on_text_created(self, text: Text) -> None`**:  Обрабатывает создание нового текстового фрагмента. Выводит в консоль полученный текст с префиксом "assistant > ".
- **`on_text_delta(self, delta: TextDelta, snapshot: Text)`**: Обрабатывает изменения в текстовом фрагменте. Добавляет изменения `delta.value` в вывод консоли.
- **`on_tool_call_created(self, tool_call: ToolCall)`**: Обрабатывает создание вызова инструмента. Выводит тип вызова инструмента в консоль.
- **`on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall)`**: Обрабатывает изменения в вызове инструмента.  Обрабатывает вызовы `code_interpreter`, выводит входные данные и результаты работы интерпретатора кода, включая лог-выводы.

## Константы

### `MODE`

**Описание**:  Переменная, хранящая режим работы (в данном случае 'dev').

## Использование

Модуль предназначен для интеграции с API OpenAI для обработки потоковых данных (stream) от диалога с помощником. Класс `EventHandler` служит для обработки событий и последующего вывода информации на экран.  Он особенно полезен для обработки результатов работы инструмента "code interpreter".


```
```python
from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta


# ... (определение класса EventHandler)
```
```

**Примечание**:  Для полноценного использования потребуется подключение к API OpenAI.  В приведенном коде представлены только определения методов обработки событий.  Необходимо также использовать этот класс в рамках потоковой обработки API OpenAI.