# Модуль `converstions_parser.py`

## Обзор

Модуль предназначен для извлечения бесед (conversations) из HTML-файлов, содержащих структуру, созданную ChatGPT. Он использует библиотеку `BeautifulSoup` для парсинга HTML и поиска всех элементов `div` с классом `conversation`.

## Подробней

Этот модуль предоставляет функцию `extract_conversations_from_html`, которая принимает путь к HTML-файлу и возвращает генератор, выдающий каждый элемент `div` с классом `conversation`, найденный в файле. Это позволяет обрабатывать большие файлы, не загружая их целиком в память. Модуль используется для анализа истории переписки с ChatGPT.

## Функции

### `extract_conversations_from_html`

```python
def extract_conversations_from_html(file_path: Path):
    """Генератор, который читает один .html файл и извлекает все <div class="conversation">.

    :param file_path: Путь к .html файлу.
    """
```

**Как работает функция**:
1. Функция принимает путь к HTML-файлу (`file_path`) в качестве аргумента.
2. Открывает HTML-файл для чтения, используя кодировку UTF-8.
3. Создает объект `BeautifulSoup` для парсинга HTML-содержимого.
4. Использует метод `find_all` для поиска всех элементов `div` с классом `conversation` в HTML-документе.
5. Возвращает генератор, который последовательно выдает каждый найденный элемент `conversation`.

**Параметры**:
- `file_path` (Path): Путь к HTML-файлу, из которого требуется извлечь беседы.

**Возвращает**:
- Генератор, который выдает объекты `BeautifulSoup` для каждого найденного элемента `div` с классом `conversation`.

**Вызывает исключения**:
- Отсутствуют явные блоки обработки исключений, но могут возникнуть исключения, связанные с открытием файла или парсингом HTML.

**Примеры**:

```python
from pathlib import Path
from src import gs
# Пример использования
file_path = Path(gs.path.data / 'chat_gpt'  / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())  # Печатаем содержимое каждой найденной беседы