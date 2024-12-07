# Модуль converstions_parser

## Обзор

Модуль `converstions_parser` предназначен для извлечения данных о беседах из файлов формата `.html`. Он предоставляет функцию `extract_conversations_from_html`, которая парсит HTML-документ и возвращает генератор, позволяющий итерироваться по элементам `div` с классом `conversation`.

## Функции

### `extract_conversations_from_html`

**Описание**: Функция `extract_conversations_from_html` принимает путь к файлу `.html` и возвращает генератор, который итеративно извлекает все элементы `<div class="conversation">` из HTML-документа.

**Параметры**:

- `file_path` (Path): Путь к файлу `.html`, который необходимо проанализировать.

**Возвращает**:

- генератор: Генератор, который итеративно возвращает каждый найденный элемент `<div class="conversation">`.

**Обрабатываемые исключения**:

- Нет описаний для обработки исключений.


## Пример использования

```python
from pathlib import Path
import gs
from src.suppliers.chat_gpt.converstions_parser import extract_conversations_from_html

file_path = Path(gs.path.data / 'chat_gpt' / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())
```


**Примечание**:  Код примера предполагает, что переменные `gs` и `Path` импортированы из соответствующих модулей.  Также,  внутри функции `extract_conversations_from_html` есть `...`, что предполагает наличие недостающего кода для обработки найденных элементов.  Этот недостающий код нужно добавить для полной реализации функциональности.
```