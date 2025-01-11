# Модуль `hypotez/src/suppliers/chat_gpt/chat_gpt.py`

## Обзор

Модуль `chat_gpt.py` предоставляет класс `ChatGpt` для работы с данными чат-ботов, скорее всего, в формате HTML.  Он позволяет получить HTML-представления диалогов.

## Оглавление

* [Модуль `chat_gpt.py`](#модуль-chat-gpt-py)
* [Класс `ChatGpt`](#класс-ChatGpt)
    * [Метод `yeld_conversations_htmls`](#метод-yeld-conversations-htmls)


## Классы

### `ChatGpt`

**Описание**: Класс для работы с данными диалогов чат-ботов.

**Методы**:

### `yeld_conversations_htmls`

**Описание**:  Возвращает итератор, позволяющий получить HTML-файлы диалогов.

**Возвращает**:
- `str`: Итератор, возвращающий пути к HTML-файлам.


```python
def yeld_conversations_htmls(self) -> str:
    """
    Args:
        self: Экземпляр класса.

    Returns:
        str: Итератор, возвращающий пути к HTML-файлам.

    Raises:
        FileNotFoundError: Если директория с файлами не найдена или файлы не найдены.
    """
    conversation_directory = Path(gs.path.data / 'chat_gpt' / 'conversations')
    html_files = conversation_directory.glob("*.html")
    for html_file in html_files:
        yield str(html_file)
```


## Константы

### `MODE`

**Описание**:  Переменная, скорее всего, задающая режим работы модуля. В данном случае, значение `'dev'`

```python

```
## Импорты

Модуль импортирует следующие библиотеки:

- `header`
- `Path` из `pathlib`
- `gs` из `src`
- `recursively_read_text_files` из `src.utils.file`

```python
import header
from pathlib import Path
from src import gs
from src.utils.file import recursively_read_text_files
```


**Примечание**: Документация для `header`, `gs`, и `recursively_read_text_files` отсутствует, поэтому их описание не включено.


```