# Модуль converstions_parser

## Обзор

Модуль `converstions_parser.py` предназначен для извлечения бесед из HTML-файлов, содержащих структуру чата. Он использует библиотеку `BeautifulSoup` для парсинга HTML и поиска элементов `div` с классом `conversation`, представляющих отдельные беседы.

## Подорбней

Этот модуль предоставляет функцию `extract_conversations_from_html`, которая принимает путь к HTML-файлу и возвращает генератор, последовательно выдающий каждую найденную беседу в формате `BeautifulSoup` объекта. Это позволяет обрабатывать большие файлы чатов, не загружая их целиком в память.

## Функции

### `extract_conversations_from_html`

```python
def extract_conversations_from_html(file_path: Path):
    """Генератор, который читает один .html файл и извлекает все <div class="conversation">.

    :param file_path: Путь к .html файлу.
    """
    ...
```

**Описание**: Генератор, который читает HTML-файл и извлекает все элементы `div` с классом `conversation`.

**Параметры**:
- `file_path` (Path): Путь к HTML-файлу.

**Возвращает**:
- `Generator[bs4.element.Tag, None, None]`: Генератор, выдающий каждый найденный элемент `conversation` в виде объекта `BeautifulSoup`.

**Примеры**:

```python
from pathlib import Path
from src import gs
file_path = Path(gs.path.data / 'chat_gpt'  / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())