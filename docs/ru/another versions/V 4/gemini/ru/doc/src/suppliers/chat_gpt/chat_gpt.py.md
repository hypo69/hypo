# Модуль `chat_gpt`

## Обзор

Модуль предназначен для работы с ChatGpt. Включает в себя класс `ChatGpt`, который позволяет обрабатывать HTML-файлы с беседами.

## Подробнее

Этот модуль предоставляет функциональность для извлечения содержимого из HTML-файлов, расположенных в директории `conversations` внутри каталога данных `chat_gpt`. Он использует `gs.path.data` для определения пути к этим файлам.

## Классы

### `ChatGpt`

**Описание**: Класс для работы с беседами ChatGpt.

**Методы**:

- `yeld_conversations_htmls`: Метод для получения содержимого HTML-файлов с беседами.

#### `yeld_conversations_htmls`

```python
def yeld_conversations_htmls(self) -> str:
    """"""
    ...
```

**Описание**: Метод перебирает HTML-файлы в директории `conversations` и возвращает их содержимое.

**Возвращает**:
- `str`: Содержимое HTML-файлов с беседами.

**Примеры**:

```python
from pathlib import Path
from src import gs
from src.suppliers.chat_gpt.chat_gpt import ChatGpt

# Предположим, что gs.path.data указывает на корень данных проекта
# И в gs.path.data / 'chat_gpt' / 'conversations' лежат файлы *.html

chat_gpt_instance = ChatGpt()
html_content = chat_gpt_instance.yeld_conversations_htmls()
# html_content содержит содержимое html файлов