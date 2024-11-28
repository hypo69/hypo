# Модуль converstions_parser

## Обзор

Модуль `converstions_parser` предназначен для извлечения данных о беседах из файлов формата HTML.  Он предоставляет функцию `extract_conversations_from_html`, которая парсит HTML-документ и возвращает итератор, содержащий все элементы `<div class="conversation">`.

## Функции

### `extract_conversations_from_html`

**Описание**: Функция `extract_conversations_from_html` извлекает все элементы `<div class="conversation">` из указанного HTML-файла. Она возвращает итератор, который позволяет последовательно получать каждый извлечённый элемент.

**Параметры**:

- `file_path` (Path): Путь к файлу HTML.

**Возвращает**:

- итератор: Итератор, возвращающий каждый найденный элемент `<div class="conversation">`.

**Обрабатываемые исключения**:

- `FileNotFoundError`: Возникает, если указанный файл не найден.
- `UnicodeDecodeError`: Возникает, если файл не может быть декодирован в кодировке UTF-8.

**Пример использования**:

```python
from pathlib import Path
import gs  # Предполагается, что gs содержит путь к папке с данными
file_path = Path(gs.path.data / 'chat_gpt' / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())
```


## Модульные переменные

### `MODE`

**Описание**: Переменная `MODE` содержит строковое значение, вероятно, используемое для определения режима работы модуля. В текущем коде она имеет значение `'dev'`.

**Тип**: str


```python
MODE = 'dev'
```