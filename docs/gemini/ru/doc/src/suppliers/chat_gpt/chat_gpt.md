# Модуль `hypotez/src/suppliers/chat_gpt/chat_gpt.py`

## Обзор

Модуль `chat_gpt.py` предоставляет класс `ChatGpt` для работы с файлами диалогов, хранящимися в подкаталоге `conversations` в каталоге данных, заданном в `gs.path.data`.

## Классы

### `ChatGpt`

**Описание**: Класс `ChatGpt` предназначен для работы с файлами HTML-диалогов.

**Методы**:

#### `yeld_conversations_htmls`

**Описание**: Метод генерирует итератор по файлам HTML-диалогов, находящимся в каталоге `conversations`.

**Возвращает**:
- `str`: Итератор, содержащий пути к файлам HTML-диалогов. Возвращает `None`, если каталог пуст или содержит файлы некорректного формата.

**Используемые переменные**:

* `conversation_directory`: Путь к каталогу с файлами диалогов.


```python
class ChatGpt:

    def yeld_conversations_htmls(self) -> str:
        """
        Args:
            None

        Returns:
            str: Итератор по файлам HTML-диалогов. Возвращает None, если каталог пуст.

        Raises:
            FileNotFoundError: Если указанный каталог не найден.
            TypeError: Если файлы в каталоге не являются HTML-файлами.
        """
        conversation_directory = Path(gs.path.data / 'chat_gpt' / 'conversations')
        html_files = conversation_directory.glob("*.html")
        for file in html_files:
            yield str(file)
```


## Переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы.


```python
MODE = 'dev'
```

## Модули

### `header`

**Описание**: Импортируется для работы с заголовками.

### `pathlib`

**Описание**: Импортируется для работы с путями к файлам.

### `gs`

**Описание**: Импортируется для работы с настройками глобальных параметров.

### `src.utils.file`

**Описание**: Импортируется для работы с файлами.


```python
import header
from pathlib import Path
from src import gs
from src.utils.file import recursively_read_text_files
```

**Примечание**: Документация для `recursively_read_text_files` и других импортированных элементов не предоставлена, так как код не содержит их использования.  Также в коде есть неинициализированные переменные `header`, `gs` и `recursively_read_text_files`, поэтому их функции не документированы.