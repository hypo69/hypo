# `converstions_parser.py`

## Обзор

Этот модуль предназначен для извлечения бесед из HTML-файлов, содержащих структуру чата, с использованием библиотеки `BeautifulSoup`. Он предоставляет функциональность для чтения HTML-файла и извлечения всех элементов `div` с классом `conversation`, которые обычно представляют отдельные блоки беседы в структуре чата.

## Подробней

Модуль `converstions_parser.py` предназначен для обработки HTML-файлов, содержащих беседы, и извлечения этих бесед для дальнейшего анализа или обработки. Он использует библиотеку `BeautifulSoup` для парсинга HTML и поиска всех элементов `div` с классом `conversation`. Это может быть полезно для анализа истории чатов, извлечения данных из веб-страниц с беседами и т.д.

## Функции

### `extract_conversations_from_html`

```python
def extract_conversations_from_html(file_path: Path):
    """Генератор, который читает один .html файл и извлекает все <div class="conversation">.

    :param file_path: Путь к .html файлу.
    """
    ...
```

**Описание**: Генератор, который читает один HTML-файл и извлекает все элементы `<div class="conversation">`.

**Параметры**:
- `file_path` (Path): Путь к HTML-файлу.

**Возвращает**:
- Generator: Генератор, который выдает каждый найденный элемент `conversation`.

**Примеры**:

```python
from pathlib import Path
from src import gs
file_path = Path(gs.path.data / 'chat_gpt'  / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())  # Печатаем содержимое каждой найденной беседы